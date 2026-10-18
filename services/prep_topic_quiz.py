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
)
from services.prep_ai_router import (
    call_deepseek,
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


def parse_quiz_json_response(raw_text: str) -> list[dict]:
    """
    Robust JSON parser specifically engineered for quiz questions across disciplines.
    Handles LaTeX equations ($...$), code snippets (`...`), unescaped quotes,
    escaped backslashes (e.g. \\times, \\frac), and auto-repairs truncated JSON arrays.
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
            return parsed
        if isinstance(parsed, dict):
            return [parsed]
    except Exception as e:
        logger.debug(f"[Topic Quiz Parser] Direct robust_json_loads failed: {e}")

    # 2. Repair LaTeX / Code unescaped backslashes and auto-close truncated arrays
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
                    return parsed
            except Exception:
                pass

    # 3. Regex extraction of individual valid question objects
    extracted = []
    pattern = re.compile(
        r'\{[^{}]*"question"\s*:\s*".*?"options"\s*:\s*\{[^{}]*\}.*?"correct_option"\s*:\s*"[A-D]".*?\}',
        re.DOTALL
    )
    for m in pattern.finditer(content):
        chunk = m.group(0)
        try:
            chunk_sanitized = re.sub(r'\\u(?![0-9a-fA-F]{4})', r'\\\\u', chunk)
            chunk_sanitized = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', chunk_sanitized)
            obj = json.loads(chunk_sanitized, strict=False)
            if isinstance(obj, dict) and "question" in obj and "options" in obj:
                extracted.append(obj)
        except Exception:
            continue

    if extracted:
        return extracted

    # Fallback to secondary extraction using robust_json_loads with sanitized string
    try:
        sanitized_fallback = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', content)
        res = robust_json_loads(sanitized_fallback)
        if isinstance(res, list):
            return res
        if isinstance(res, dict):
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

    discipline = _detect_course_discipline(course)
    if discipline in {"Mathematics", "Statistics", "Physics"}:
        discipline_rules = (
            "DISCIPLINE GUIDELINES (Mathematics / Statistics / Physics):\n"
            "- Mathematical Formulation: Use standard LaTeX notation enclosed in $...$ for inline formulas (e.g., $x^2 + y^2 = r^2$, $\\int_0^1 x\\,dx$) or $$...$$ for block equations.\n"
            "- Escape Backslashes: In your JSON string values, ALWAYS double-escape LaTeX backslashes (e.g. write \\\\times, \\\\frac, \\\\sqrt, \\\\alpha, \\\\beta, \\\\sum, \\\\int) so the JSON parser does not fail on unescaped backslashes.\n"
            "- Code in Statistics / R: If referencing statistical commands, syntax, or output matrices, use code backticks (`...`) and use single quotes ('...') inside code strings."
        )
    elif discipline == "Computing":
        discipline_rules = (
            "DISCIPLINE GUIDELINES (Computing / Software / Programming / Databases):\n"
            "- Code & Syntax Formatting: For any programming commands, functions, syntax, code snippets, database queries, or variables (e.g. in Python, R, C++, Java, SQL, bash), enclose them in backticks (`...`) or block code fences.\n"
            "- Quotation Escaping: Inside code strings and values, use single quotes ('...') or properly escaped double quotes (\\\") so they do not break JSON string boundaries.\n"
            "- Output & Tracing: When asking what code outputs or how an algorithm executes, provide clear, exact code representation."
        )
    elif discipline == "Chemistry":
        discipline_rules = (
            "DISCIPLINE GUIDELINES (Chemistry / Biochemistry):\n"
            "- Chemical Notation: Format chemical equations and formulas using LaTeX (e.g. $\\text{H}_2\\text{SO}_4$, $\\to$, $\\Delta H$) with properly double-escaped backslashes.\n"
            "- Scientific Accuracy: Distractors must reflect plausible misconceptions about oxidation states, stoichiometry, mechanisms, or functional groups."
        )
    else:
        discipline_rules = (
            "DISCIPLINE GUIDELINES (Conceptual & Applied Domain):\n"
            "- Deep Understanding: Focus on applied scenarios, critical definitions, comparative principles, and real-world domain problems.\n"
            "- Clean JSON: Use single quotes ('...') inside question text when quoting phrases or titles."
        )

    system_prompt = (
        "You are an expert university examiner. You create rigorous, high-yield "
        "multiple choice questions for university students. Each question must test conceptual understanding, "
        "analytical reasoning, or problem-solving. Every question must have exactly 4 options (A, B, C, D), "
        "one clearly correct answer, and detailed explanations of why the correct option is right and "
        "why each incorrect distractor is wrong.\n"
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
      "summary": "Detailed, step-by-step reasoning explaining why the correct option is right.",
      "why_others_wrong": {{
        "B": "Specific explanation of the mistake or misconception in option B.",
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
5. Return ONLY a single raw JSON array of objects.
"""

    model_name = getattr(settings, "DEEPSEEK_CHAT_MODEL", "deepseek-flash")
    ai_response = call_deepseek(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        model=model_name,
        max_tokens=5000,
        temperature=0.2,
        thinking_enabled=False,
    )

    if not ai_response.get("success"):
        logger.error(f"[Topic Quiz] AI call failed for topic {topic.id}: {ai_response.get('error')}")
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

        q_text = str(item.get("question") or "").strip()
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
) -> list[PrepTopicQuizQuestion]:
    """
    Returns `count` active quiz questions for a topic.
    If fewer than `count` exist or `force_fresh=True`, generates new ones.
    Prioritizes questions the user hasn't mastered yet.
    """
    if not topic:
        return []

    qs = PrepTopicQuizQuestion.objects.filter(topic=topic, is_active=True)

    if not force_fresh and qs.count() >= count:
        all_ids = list(qs.values_list("id", flat=True))
        # If user is authenticated, prioritize questions the user hasn't gotten correct recently
        if user and user.is_authenticated:
            correctly_answered = set(
                PrepTopicQuizAttempt.objects.filter(
                    user=user,
                    quiz_question__topic=topic,
                    is_correct=True,
                ).values_list("quiz_question_id", flat=True)
            )
            unmastered_ids = [qid for qid in all_ids if qid not in correctly_answered]
            if len(unmastered_ids) >= count:
                selected_ids = random.sample(unmastered_ids, count)
            else:
                remaining_needed = count - len(unmastered_ids)
                mastered_ids = [qid for qid in all_ids if qid in correctly_answered]
                selected_ids = unmastered_ids + random.sample(mastered_ids, min(remaining_needed, len(mastered_ids)))
        else:
            selected_ids = random.sample(all_ids, min(count, len(all_ids)))

        return list(qs.filter(id__in=selected_ids).order_by("?"))

    # Need to generate more questions
    needed = max(count - qs.count(), 3)
    new_questions = generate_topic_quiz_questions(topic, count=max(needed, count))
    
    # Return fresh selection
    combined = list(PrepTopicQuizQuestion.objects.filter(topic=topic, is_active=True).order_by("?"))
    return combined[:count]


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

    # Build response with rich explanation
    explanation = question.explanation or {}
    summary = explanation.get("summary") or "Correct answer verified."
    why_others = explanation.get("why_others_wrong") or {}
    selected_why_wrong = why_others.get(clean_selected, "")

    return {
        "success": True,
        "is_correct": is_correct,
        "selected_option": clean_selected,
        "correct_option": question.correct_option,
        "summary_explanation": summary,
        "why_selected_is_wrong": selected_why_wrong if not is_correct else "",
        "why_others_wrong": why_others,
    }
