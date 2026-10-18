import json
import logging
import random
from django.conf import settings
from django.utils import timezone
from prep.models import (
    PrepTopic,
    PrepTopicQuizQuestion,
    PrepTopicQuizAttempt,
    PrepStudentSpacedCard,
    PrepStudentQuizSeen,
)
from services.prep_ai_router import (
    call_deepseek,
    call_together_repair,
    repair_question_and_solution_text,
    robust_json_loads,
    _approved_course_source_context,
)
from services.prep_spaced_repetition import review_spaced_card, RATING_MAP

import re

logger = logging.getLogger(__name__)


def _detect_course_discipline(course) -> str:
    """Detect whether a course is Computing, Mathematics, Statistics, Physics, Chemistry, or General."""
    if not course:
        return "General"
    code = str(course.code or "").strip().upper()
    title = str(course.title or "").strip().lower()
    prefix = re.split(r"[\s\-_0-9]+", code)[0] if code else ""

    if prefix in {"CIT", "CCS", "CSC", "ICS", "BIT", "SIT", "COM", "CSE"} or any(
        kw in title for kw in ("computer", "computing", "programming", "software", "algorithm", "database", "data structure", "information technology", "coding", "python", "java", "sql", "windows")
    ):
        return "Computing"

    if prefix in {"SST", "STA", "ACT"} or any(
        kw in title for kw in ("statistic", "probability", "regression", "sampling", "actuarial", "r programming", "data analysis", "matrix")
    ):
        return "Statistics"

    if prefix in {"SMA", "MAT", "MATH", "MTH", "CAL", "ALG", "GEO"} or any(
        kw in title for kw in ("mathematic", "calculus", "geometry", "algebra", "trigonometry", "differential equation", "linear algebra")
    ):
        return "Mathematics"

    if prefix in {"SPH", "PHY"} or any(
        kw in title for kw in ("physics", "mechanics", "electromagnetism", "quantum", "optics")
    ):
        return "Physics"

    if prefix in {"SCH", "CHE", "BCH"} or any(
        kw in title for kw in ("chemistry", "chemical", "organic", "inorganic", "biochemistry")
    ):
        return "Chemistry"

    return "General"


def _extract_json_objects_from_array(text: str) -> list[dict]:
    """
    Parses individual JSON question objects by tracking curly brace depth
    while properly skipping string literals and escape characters.
    This guarantees nested objects (like explanation.why_others_wrong)
    and LaTeX math backslashes are extracted in full without regex truncation.
    """
    objs = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] == '{':
            depth = 1
            start = i
            i += 1
            in_str = False
            escape = False
            while i < n and depth > 0:
                ch = text[i]
                if in_str:
                    if escape:
                        escape = False
                    elif ch == '\\':
                        escape = True
                    elif ch == '"':
                        in_str = False
                else:
                    if ch == '"':
                        in_str = True
                    elif ch == '{':
                        depth += 1
                    elif ch == '}':
                        depth -= 1
                i += 1
            if depth == 0:
                raw_chunk = text[start:i]
                chunk_sanitized = re.sub(r'\\u(?![0-9a-fA-F]{4})', r'\\\\u', raw_chunk)
                chunk_sanitized = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', chunk_sanitized)
                try:
                    obj = json.loads(chunk_sanitized, strict=False)
                    if isinstance(obj, dict) and "question" in obj and "options" in obj:
                        objs.append(obj)
                except Exception:
                    try:
                        obj = robust_json_loads(chunk_sanitized)
                        if isinstance(obj, dict) and "question" in obj and "options" in obj:
                            objs.append(obj)
                    except Exception:
                        pass
        else:
            i += 1
    return objs


def parse_quiz_json_response(raw_text: str) -> list[dict]:
    """
    Robust JSON parser specifically engineered for quiz questions across disciplines.
    Handles LaTeX equations ($...$), code snippets (`...`), unescaped quotes,
    escaped backslashes (e.g. \\times, \\frac), and nested explanations.
    """
    content = str(raw_text or "").strip()
    if not content:
        return []

    # Strip markdown code blocks if wrapped
    if content.startswith("```json"):
        content = content[7:]
    elif content.startswith("```"):
        content = content[3:]
    if content.endswith("```"):
        content = content[:-3]
    content = content.strip()

    # 1. Try robust_json_loads directly
    try:
        parsed = robust_json_loads(content)
        if isinstance(parsed, list):
            valid = [q for q in parsed if isinstance(q, dict) and "question" in q and "options" in q]
            if valid:
                return valid
        elif isinstance(parsed, dict) and "question" in parsed and "options" in parsed:
            return [parsed]
    except Exception as e:
        logger.debug(f"[Topic Quiz Parser] Direct robust_json_loads failed: {e}")

    # 2. Extract objects with brace-depth parser (handles nested dicts and LaTeX backslashes)
    extracted = _extract_json_objects_from_array(content)
    if extracted:
        return extracted

    # 3. Repair LaTeX / Code unescaped backslashes and auto-close truncated arrays
    repaired = content
    repaired = re.sub(r'\\u(?![0-9a-fA-F]{4})', r'\\\\u', repaired)
    repaired = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', repaired)

    if "[" in repaired:
        start_bracket = repaired.find("[")
        last_brace = repaired.rfind("}")
        if last_brace > start_bracket:
            candidate = repaired[start_bracket:last_brace + 1].strip() + "\n]"
            try:
                parsed = json.loads(candidate, strict=False)
                if isinstance(parsed, list):
                    valid = [q for q in parsed if isinstance(q, dict) and "question" in q and "options" in q]
                    if valid:
                        return valid
            except Exception:
                pass

    # 4. Fallback to sanitized robust_json_loads
    try:
        sanitized_fallback = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', content)
        res = robust_json_loads(sanitized_fallback)
        if isinstance(res, list):
            return [q for q in res if isinstance(q, dict) and "question" in q and "options" in q]
        if isinstance(res, dict) and "question" in res and "options" in res:
            return [res]
    except Exception:
        pass

    return []


def generate_topic_quiz_questions(
    topic: PrepTopic,
    count: int = 5,
    difficulty: str = "medium",
) -> list[PrepTopicQuizQuestion]:
    """
    Generates high-yield multiple-choice questions for a syllabus topic with
    detailed distractor explanations (why the right answer is right, and why each wrong answer is wrong).
    Persists valid questions to PrepTopicQuizQuestion.
    """
    if not topic or not topic.pk:
        return []

    course = topic.course
    course_name = f"{course.code} - {course.title}" if course else "University Course"
    topic_title = topic.title

    # Gather contextual source material from approved course documents
    source_context = ""
    try:
        source_context = _approved_course_source_context(course, topic_title, limit=5000)
    except Exception as exc:
        logger.warning(f"[Topic Quiz] Could not retrieve source context for {topic_title}: {exc}")

    # Fallback to topic summary if source context is empty
    if not source_context and topic.summary:
        source_context = f"Topic Summary: {topic.summary}"

    from services.prep_sanitizer import purge_institutional_metadata
    source_context = purge_institutional_metadata(source_context)

    discipline = _detect_course_discipline(course)
    if discipline in {"Mathematics", "Statistics", "Physics"}:
        discipline_rules = (
            "DISCIPLINE GUIDELINES (Mathematics / Statistics / Physics):\n"
            "- Mathematical Formulation: Use standard LaTeX notation enclosed in $...$ for inline formulas (e.g., $x^2 + y^2 = r^2$, $\\int_0^1 x\\,dx$) or $$...$$ for block equations.\n"
            "- Escape Backslashes: In your JSON string values, ALWAYS double-escape LaTeX backslashes (e.g. write \\\\times, \\\\frac, \\\\sqrt, \\\\alpha, \\\\beta, \\\\sum, \\\\int) so the JSON parser does not fail on unescaped backslashes.\n"
            "- Structured Multi-Line Derivations: In both 'summary' and 'why_others_wrong', NEVER write multi-step mathematical derivations in a single cramped sentence. Break steps onto separate lines using bullet points (e.g. '- Identify general formula: ...\\n- Substitute known values: ...\\n- Conclude result: ...') or block LaTeX ($$...$$), allowing students to visually scan each calculation step.\n"
            "- Code in Statistics / R: If referencing statistical commands, syntax, or output matrices, use code backticks (`...`) and use single quotes ('...') inside code strings."
        )
    elif discipline == "Computing":
        discipline_rules = (
            "DISCIPLINE GUIDELINES (Computing / Software / Programming / Databases):\n"
            "- Code & Syntax Formatting: For any programming commands, functions, syntax, code snippets, database queries, or variables (e.g. in Python, R, C++, Java, SQL, bash), enclose them in backticks (`...`) or block code fences with language tags (e.g. ```python\\n...\\n```).\n"
            "- Multi-line Tracing & Output: Never squash multi-line code, algorithms, or execution traces into a single line. In 'summary' and 'why_others_wrong', use block code fences or distinct bulleted execution steps so code structure, indentation, and output are crystal clear.\n"
            "- Quotation Escaping: Inside code strings and values, use single quotes ('...') or properly escaped double quotes (\\\") so they do not break JSON string boundaries."
        )
    elif discipline == "Chemistry":
        discipline_rules = (
            "DISCIPLINE GUIDELINES (Chemistry / Biochemistry):\n"
            "- Chemical Notation: Format chemical equations and formulas using LaTeX (e.g. $\\text{H}_2\\text{SO}_4$, $\\to$, $\\Delta H$) with properly double-escaped backslashes.\n"
            "- Step-by-Step Mechanisms: Break reaction mechanisms, stoichiometry steps, and oxidation-state calculations into clear numbered or bulleted lines, rather than continuous run-on paragraphs.\n"
            "- Scientific Accuracy: Distractors must reflect plausible misconceptions about oxidation states, stoichiometry, mechanisms, or functional groups."
        )
    else:
        discipline_rules = (
            "DISCIPLINE GUIDELINES (Conceptual & Applied Domain):\n"
            "- Clear Structural Formatting: Use paragraphs and bullet points for explanations with multiple points or comparative factors. Avoid dense monolithic walls of text.\n"
            "- Deep Understanding: Focus on applied scenarios, critical definitions, comparative principles, and real-world domain problems.\n"
            "- Clean JSON: Use single quotes ('...') inside question text when quoting phrases or titles."
        )

    system_prompt = (
        "You are an expert university examiner. You create rigorous, high-yield "
        "multiple choice questions for university students. Each question must test conceptual understanding, "
        "analytical reasoning, or problem-solving. Every question must have exactly 4 options (A, B, C, D), "
        "one clearly correct answer, and detailed explanations of why the correct option is right and "
        "why each incorrect distractor is wrong.\n"
        "STRICT INSTITUTIONAL ANONYMITY: Never mention any specific university, college, lecturer, or department name. If source material uses an institution as an example, generalize it to 'a higher education institution' or 'an academic institution'.\n"
        "Return ONLY a valid JSON list of question objects with no markdown fences, no preamble, and no HTML."
    )

    user_prompt = f"""Generate {count} multiple-choice drill questions for the university course "{course_name}", topic: "{topic_title}".
Target difficulty level: {difficulty}.

Available Syllabus / Topic Material:
\"\"\"
{source_context[:4500]}
\"\"\"

{discipline_rules}

Required JSON schema:
[
  {{
    "question": "Clear problem statement or question using LaTeX ($...$ or $$...$$) for any mathematical notation or backticks (`...`) for code",
    "options": {{
      "A": "Option text",
      "B": "Option text",
      "C": "Option text",
      "D": "Option text"
    }},
    "correct_option": "A",
    "explanation": {{
      "summary": "Detailed, step-by-step reasoning explaining why the correct option is right. Format math steps or code derivations across clear paragraphs or bullet points (- Step 1: ..., - Step 2: ...), never crammed into a single run-on sentence.",
      "why_others_wrong": {{
        "B": "Specific explanation of the mistake or misconception in option B. Use line breaks or bullet points if explaining a calculation error.",
        "C": "Specific explanation of why option C is invalid or incorrect.",
        "D": "Specific explanation of why option D is invalid or incorrect."
      }}
    }},
    "difficulty": "{difficulty}"
  }}
]

Important rules:
1. Every question must have exactly 4 choices: A, B, C, and D.
2. The correct_option must be exactly one uppercase letter ('A', 'B', 'C', or 'D').
3. Distractors (incorrect options) must represent authentic, common misconceptions rather than absurd choices.
4. Follow the DISCIPLINE GUIDELINES above for math formulas vs code syntax.
5. STRICT INSTITUTIONAL ANONYMITY: Do NOT mention any specific university, college, or lecturer name. Generalize any institutional examples to 'a higher education institution' or 'an academic institution'.
6. Return ONLY a single raw JSON array of objects.
"""

    model_name = getattr(settings, "DEEPSEEK_CHAT_MODEL", "deepseek-chat")
    ai_response = call_deepseek(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        model=model_name,
        max_tokens=5000,
        temperature=0.2,
    )

    if not ai_response.get("success") or not ai_response.get("content"):
        logger.warning(
            f"[Topic Quiz] DeepSeek call failed for topic {topic.id}: {ai_response.get('error')}. Attempting Together AI fallback..."
        )
        together_model = getattr(settings, "TOGETHER_CHAT_MODEL", "deepseek-ai/DeepSeek-V3")
        if getattr(settings, "TOGETHERAI_API", ""):
            try:
                ai_response = call_together_repair(
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    model=together_model,
                    max_tokens=5000,
                    json_mode=True,
                )
            except Exception as fb_err:
                logger.error(f"[Topic Quiz] Together AI fallback failed for topic {topic.id}: {fb_err}")

    if not ai_response.get("success") or not ai_response.get("content"):
        logger.error(f"[Topic Quiz] All AI providers failed for topic {topic.id}: {ai_response.get('error')}")
        return []

    content = str(ai_response.get("content") or "").strip()
    parsed_items = parse_quiz_json_response(content)
    if not isinstance(parsed_items, list) or not parsed_items:
        logger.warning(f"[Topic Quiz] Failed to parse JSON list from AI response for topic {topic.id}")
        return []

    created_questions = []
    valid_letters = {"A", "B", "C", "D"}

    for item in parsed_items:
        if not isinstance(item, dict):
            continue

        q_text = repair_question_and_solution_text(str(item.get("question") or "").strip())
        raw_options = item.get("options")
        correct_letter = str(item.get("correct_option") or "").strip().upper()
        raw_explanation = item.get("explanation")

        if not q_text or not isinstance(raw_options, dict) or correct_letter not in valid_letters:
            continue

        # Ensure all 4 options exist
        clean_options = {}
        for letter in ("A", "B", "C", "D"):
            val = str(raw_options.get(letter) or raw_options.get(letter.lower()) or "").strip()
            if not val:
                break
            clean_options[letter] = repair_question_and_solution_text(val)

        if len(clean_options) != 4:
            continue

        # Format explanation
        clean_explanation = {}
        if isinstance(raw_explanation, dict):
            clean_explanation["summary"] = repair_question_and_solution_text(
                str(raw_explanation.get("summary") or "")
            )
            raw_why = raw_explanation.get("why_others_wrong") or {}
            clean_why = {}
            if isinstance(raw_why, dict):
                for k, v in raw_why.items():
                    k_upper = str(k).strip().upper()
                    if k_upper in valid_letters and k_upper != correct_letter:
                        clean_why[k_upper] = repair_question_and_solution_text(str(v or ""))
            clean_explanation["why_others_wrong"] = clean_why
        elif isinstance(raw_explanation, str):
            clean_explanation = {
                "summary": repair_question_and_solution_text(raw_explanation),
                "why_others_wrong": {},
            }
        else:
            clean_explanation = {"summary": "Correct answer verified.", "why_others_wrong": {}}

        clean_q_text = repair_question_and_solution_text(q_text)
        item_diff = str(item.get("difficulty") or difficulty).lower()
        if item_diff not in {"easy", "medium", "hard"}:
            item_diff = "medium"

        # Check for duplicate question text in this topic
        existing = PrepTopicQuizQuestion.objects.filter(
            topic=topic,
            question_text=clean_q_text,
        ).first()
        if existing:
            created_questions.append(existing)
            continue

        question_obj = PrepTopicQuizQuestion.objects.create(
            topic=topic,
            question_text=clean_q_text,
            options=clean_options,
            correct_option=correct_letter,
            explanation=clean_explanation,
            difficulty=item_diff,
            is_active=True,
        )
        created_questions.append(question_obj)

    logger.info(f"[Topic Quiz] Generated {len(created_questions)} questions for topic {topic.title} ({topic.id})")
    return created_questions


def get_or_create_topic_quiz(
    topic: PrepTopic,
    count: int = 5,
    user=None,
    force_fresh: bool = False,
    mark_seen: bool = True,
) -> list[PrepTopicQuizQuestion]:
    """
    Returns `count` active quiz questions for a topic.
    Guarantees that a student never receives questions they have already seen/paid for.
    If fewer than `count` unseen questions exist or `force_fresh=True`, generates new ones.
    Records delivered questions in PrepStudentQuizSeen for authenticated students.
    """
    if not topic:
        return []

    # 1. Identify question IDs already seen by this user
    seen_ids = set()
    if user and user.is_authenticated:
        seen_ids = set(
            PrepStudentQuizSeen.objects.filter(
                user=user,
                topic=topic,
            ).values_list("quiz_question_id", flat=True)
        )

    # 2. Query available active questions excluding questions already seen by user
    available_qs = PrepTopicQuizQuestion.objects.filter(
        topic=topic,
        is_active=True,
    )
    if seen_ids:
        available_qs = available_qs.exclude(id__in=seen_ids)

    # 3. Fast-path: If enough unseen questions exist and fresh is not forced, serve them
    if not force_fresh and available_qs.count() >= count:
        all_ids = list(available_qs.values_list("id", flat=True))
        selected_ids = random.sample(all_ids, min(count, len(all_ids)))
        selected = list(available_qs.filter(id__in=selected_ids).order_by("?"))
        if mark_seen and user and user.is_authenticated and selected:
            records = [
                PrepStudentQuizSeen(user=user, quiz_question=q, topic=topic)
                for q in selected
            ]
            PrepStudentQuizSeen.objects.bulk_create(records, ignore_conflicts=True)
        return selected

    # 4. Fresh generation needed (unseen count < count, or user requested "New Questions")
    needed = count if force_fresh else max(1, count - available_qs.count())
    target_count = max(needed, 5)
    new_questions = generate_topic_quiz_questions(topic, count=target_count)

    # Resilient retry: if first attempt produced 0 questions, retry once
    if not new_questions:
        logger.warning(f"[Topic Quiz] Initial generation returned 0 questions for topic {topic.id}. Retrying once...")
        new_questions = generate_topic_quiz_questions(topic, count=target_count)

    # Re-query unseen questions (includes newly generated questions, excluding already seen)
    available_qs = PrepTopicQuizQuestion.objects.filter(
        topic=topic,
        is_active=True,
    )
    if seen_ids:
        available_qs = available_qs.exclude(id__in=seen_ids)

    if available_qs.exists():
        all_ids = list(available_qs.values_list("id", flat=True))
        selected_ids = random.sample(all_ids, min(count, len(all_ids)))
        selected = list(available_qs.filter(id__in=selected_ids).order_by("?"))
        if mark_seen and user and user.is_authenticated and selected:
            records = [
                PrepStudentQuizSeen(user=user, quiz_question=q, topic=topic)
                for q in selected
            ]
            PrepStudentQuizSeen.objects.bulk_create(records, ignore_conflicts=True)
        return selected

    # 5. Fallback recycle: If all unseen questions are exhausted and new questions could not be prepared,
    # recycle from the entire active topic question bank so the student can continuously practice active recall!
    recycle_qs = PrepTopicQuizQuestion.objects.filter(topic=topic, is_active=True)
    if recycle_qs.exists():
        logger.info(f"[Topic Quiz] Unseen questions exhausted for topic {topic.id}. Recycling active question bank.")
        # Reset seen history for this topic so the student enters a new recall cycle
        if user and user.is_authenticated:
            PrepStudentQuizSeen.objects.filter(user=user, topic=topic).delete()
        all_ids = list(recycle_qs.values_list("id", flat=True))
        selected_ids = random.sample(all_ids, min(count, len(all_ids)))
        selected = list(recycle_qs.filter(id__in=selected_ids).order_by("?"))
        if mark_seen and user and user.is_authenticated and selected:
            records = [
                PrepStudentQuizSeen(user=user, quiz_question=q, topic=topic)
                for q in selected
            ]
            PrepStudentQuizSeen.objects.bulk_create(records, ignore_conflicts=True)
        return selected

    return []


def format_explanation_for_display(text: str) -> str:
    """
    Ensures mathematical derivations, code executions, and step-by-step
    reasoning are cleanly separated across multiple lines rather than crammed
    into a single continuous line.
    """
    if not text or not isinstance(text, str):
        return ""
    cleaned = text.strip()
    if "\n\n" in cleaned or "\n- " in cleaned or "\n* " in cleaned or "\n1. " in cleaned:
        return cleaned

    # Step indicators (e.g. "Step 1:", "Step 2:")
    cleaned = re.sub(r'(?:^|\s*)(?:[-•*]\s*)?(Step\s*\d+[:.-]?)\s*', r'\n\n- **\1** ', cleaned, flags=re.IGNORECASE)

    # Transition words after sentence-ending punctuation
    cleaned = re.sub(
        r'([.;])\s+(Here\b|Thus\b|Therefore\b|Hence\b|Substituting\b|Substitute\b|First\b|Next\b|Then\b|Finally\b|Solving\b|Recall that\b|Using the formula\b|By definition\b|In general\b|Note that\b)',
        r'\1\n\n\2',
        cleaned,
        flags=re.IGNORECASE,
    )

    # Code outputs after introductory colon
    cleaned = re.sub(r':\s*(`[^`]+`)\s*\.?$', r':\n\n\1', cleaned)

    return cleaned.strip()


def evaluate_quiz_answer(
    quiz_question_id: int,
    selected_option: str,
    user=None,
) -> dict:
    """
    Evaluates a student's answer choice against the correct option.
    Records the attempt and links to FSRS spaced repetition if incorrect.
    """
    question = PrepTopicQuizQuestion.objects.filter(id=quiz_question_id, is_active=True).select_related("topic", "topic__course").first()
    if not question:
        return {"success": False, "error": "Quiz question not found."}

    clean_selected = str(selected_option or "").strip().upper()
    valid_letters = {"A", "B", "C", "D"}
    if clean_selected not in valid_letters:
        return {"success": False, "error": "Invalid option selected. Must be A, B, C, or D."}

    is_correct = clean_selected == question.correct_option.upper()

    # Record attempt if user is authenticated
    if user and user.is_authenticated:
        PrepTopicQuizAttempt.objects.create(
            user=user,
            quiz_question=question,
            selected_option=clean_selected,
            is_correct=is_correct,
        )

        # FSRS Spaced Repetition Integration:
        # If student got it wrong, schedule this question for spaced review!
        if not is_correct:
            spaced_card, _ = PrepStudentSpacedCard.objects.get_or_create(
                user=user,
                topic=question.topic,
                quiz_question=question,
                defaults={
                    "card_title": f"Drill: {question.topic.title} (Q{question.id})",
                    "prompt_text": question.question_text,
                    "answer_text": f"Correct: Option {question.correct_option}\n{question.explanation.get('summary', '')}",
                    "due_date": timezone.now(),
                    "state": 0,
                },
            )
            # Grade as "again" (lapse)
            try:
                review_spaced_card(spaced_card.id, user, "again")
            except Exception as exc:
                logger.warning(f"[Topic Quiz] Could not update spaced card for user {user.id}: {exc}")

    # Build response with rich multi-line explanation
    explanation = question.explanation or {}
    summary = format_explanation_for_display(explanation.get("summary") or "Correct answer verified.")
    why_others = explanation.get("why_others_wrong") or {}
    formatted_why_others = {}
    if isinstance(why_others, dict):
        for k, v in why_others.items():
            formatted_why_others[k] = format_explanation_for_display(str(v or ""))
    selected_why_wrong = formatted_why_others.get(clean_selected, "")

    return {
        "success": True,
        "is_correct": is_correct,
        "selected_option": clean_selected,
        "correct_option": question.correct_option,
        "summary_explanation": summary,
        "why_selected_is_wrong": selected_why_wrong if not is_correct else "",
        "why_others_wrong": formatted_why_others,
    }
