"""
services/prep_chatbot_service.py

Service for Mentify Prep Assistant powered by Google Gemini API.
Grounds the assistant in live Mentify Prep database context:
- Canonical course units and syllabus topics
- Past exam papers and CATs
- Credit consumption rules and wallet balances
- Subscription plans (Basic KES 399, Plus KES 499, Pro KES 799)
- Document upload and ingestion pipeline
- Smart markdown linking and KaTeX math formatting
"""

import os
import json
import logging
import requests
from urllib.parse import quote
from pathlib import Path
from dotenv import load_dotenv
from django.conf import settings

logger = logging.getLogger(__name__)

# Ensure .env is loaded
BASE_DIR = getattr(settings, "BASE_DIR", Path(__file__).resolve().parents[1])
load_dotenv(BASE_DIR / ".env", override=True)


def find_matching_course_inventory(query_text: str) -> tuple[list, bool]:
    """
    Checks if user is inquiring about a specific course code or title availability.
    Distinguishes specific course inquiries from general catalog questions.
    Returns (matches_list, was_specific_course_query).
    """
    if not query_text:
        return [], False

    import re
    from django.db.models import Q
    from prep.models import PrepCourse

    # 1. Check for course code patterns e.g. SMA 300, SMA300, STA 200, CIT 101, etc.
    code_matches = re.findall(r"\b([A-Za-z]{2,5}\s*\d{2,4}[A-Za-z]?)\b", query_text)
    if code_matches:
        q_filter = Q()
        for code in code_matches:
            clean_code = re.sub(r"\s+", "", code).upper()
            spaced_code = re.sub(r"([A-Za-z]+)(\d+)", r"\1 \2", clean_code)
            q_filter |= Q(code__iexact=spaced_code) | Q(code__iexact=clean_code) | Q(code__icontains=clean_code)

        try:
            results = list(PrepCourse.objects.filter(q_filter, is_active=True).prefetch_related("topics", "papers")[:5])
            return results, True
        except Exception:
            return [], True

    # 2. Check if asking generally about courses (e.g. "what courses are available?", "what courses do you offer?")
    is_general_catalog_question = bool(re.search(
        r"\b(what\s+courses|which\s+courses|all\s+courses|list\s+of\s+courses|show\s+me\s+courses|what\s+subjects|what\s+units|what\s+do\s+you\s+offer)\b",
        query_text,
        re.IGNORECASE,
    ))
    if is_general_catalog_question:
        return [], False

    # 3. Check for specific course subject inquiry: "is ABC available?", "do you have calculus?", etc.
    is_specific_inquiry = bool(re.search(
        r"\b(is|do you have|can i find|looking for|have|teach|cover)\b",
        query_text,
        re.IGNORECASE,
    ))

    stop_words = {
        "what", "which", "where", "have", "offer", "available", "there",
        "courses", "course", "about", "please", "mentify", "prep", "tell",
        "help", "with", "from", "that", "this", "some", "many", "much",
        "units", "unit", "does", "free", "credits", "credit", "study",
        "material", "exam", "exams", "paper", "papers", "online"
    }
    words = [w.strip() for w in re.findall(r"[A-Za-z]{3,}", query_text) if w.lower() not in stop_words]
    if words and is_specific_inquiry:
        q_title = Q()
        for w in words[:3]:
            q_title |= Q(title__icontains=w) | Q(code__icontains=w) | Q(category__icontains=w)
        try:
            results = list(PrepCourse.objects.filter(q_title, is_active=True).prefetch_related("topics", "papers")[:5])
            return results, True
        except Exception:
            return [], True

    return [], False


def get_prep_system_context(user=None, user_message: str = "") -> str:
    """
    Dynamically fetch real-time system context for Gemini without dumping the
    full course catalog. Accurately verifies specific course availability on demand.
    """
    course_query_block = ""
    matched_courses, was_course_query = find_matching_course_inventory(user_message)

    if was_course_query:
        if matched_courses:
            lines = []
            for c in matched_courses:
                topics = list(c.topics.all()[:4])
                topic_names = ", ".join([t.title for t in topics]) if topics else "Syllabus available"
                papers_count = c.papers.filter(is_published=True).count()
                course_url = f"/prep/courses/{quote(c.code)}/"
                lines.append(
                    f"- **{c.code}**: {c.title} (Level: {c.level}, Category: {c.category})\n"
                    f"  URL: {course_url}\n"
                    f"  Past Papers Available: {papers_count} | Sample Topics: {topic_names}"
                )
            course_query_block = f"""
### SPECIFIC COURSE AVAILABILITY CHECK (DATABASE SEARCH RESULTS):
The student inquired about course availability. The following course(s) match in the database:
{chr(10).join(lines)}

OPERATING INSTRUCTION: Confirm to the student that this course is available on Mentify Prep, include its clickable Markdown link [{matched_courses[0].code} - {matched_courses[0].title}](/prep/courses/{quote(matched_courses[0].code)}/), and summarize its available past papers and syllabus topics.
"""
        else:
            course_query_block = """
### SPECIFIC COURSE AVAILABILITY CHECK (DATABASE SEARCH RESULTS):
The student inquired about the availability of a specific course, but NO matching course was found in the active Mentify Prep database.

OPERATING INSTRUCTION: Politely inform the student that this course is not currently available or indexed on Mentify Prep. Direct them to search the catalog at [Courses & Syllabi](/prep/courses/) or encourage them to upload their past papers or lecture notes at [Upload Study Material](/prep/upload/) so our tutors can review and index it!
"""

    user_context_block = ""
    if user and user.is_authenticated:
        try:
            from prep.models import PrepWallet, PrepCourseEnrollment
            wallet = PrepWallet.get_or_create_wallet(user)
            enrolled = PrepCourseEnrollment.objects.filter(user=user).select_related("course")
            enrolled_codes = [e.course.code for e in enrolled]
            enrolled_str = ", ".join(enrolled_codes) if enrolled_codes else "None yet"
            plan_display = wallet.current_plan.title()
            if wallet.current_plan == "trial":
                plan_display = "Free Trial (3 Days)"
            elif wallet.current_plan == "plus":
                plan_display = "Plus (Semester Pass)"
            elif wallet.current_plan == "pro":
                plan_display = "Pro (Exam Master)"
            elif wallet.current_plan == "basic":
                plan_display = "Basic (Starter Prep)"

            user_context_block = f"""
### CURRENT STUDENT PROFILE:
- Student Name: {user.get_full_name() or user.username}
- Current Credit Balance: {wallet.credits_balance} credits
- Active Plan: {plan_display}
- Plan Expiration: {wallet.plan_expires_at.strftime('%Y-%m-%d %H:%M') if wallet.plan_expires_at else 'N/A'}
- Enrolled Courses: {enrolled_str}
"""
        except Exception as e:
            logger.warning(f"Could not load user wallet context: {e}")

    system_prompt = f"""You are Mentify Prep Assistant, the specialized AI academic revision and customer support assistant for Mentify Prep (https://mlaudit.info/prep/).

### PLATFORM OVERVIEW:
Mentify Prep is an exam readiness, syllabus study, and past-paper revision engine for students preparing for Continuous Assessment Tests (CATs) and final examinations.
Key capabilities:
1. **Interactive AI Study Tutor**:
   - Available on every syllabus topic page to guide students through concepts and problem-solving steps.
   - Learners can ask questions directly on the topic and receive clear, step-by-step guidance.
   - Learners can upload study materials directly to the tutor: PDFs (up to 8 MB, 4 pages) and images/photos (PNG/JPEG up to 3 images, 4 MB each) to receive complete step-by-step solutions and answers.
   - Digital text PDFs are parsed locally at no extra charge. Scanned PDF pages and images/photos use high-precision Vision OCR at 5 credits per image/page. Tutor replies cost 1 credit per message (based on AI token usage, minimum 1 credit).
2. **Course-Anchored Syllabus & Notes**:
   - Organizes study materials strictly by course unit, syllabus modules, and subtopics.
   - 3 Tone Levels for revision notes: Foundation & Intuition (Level 1), Core Concepts (Level 2), and Exam Focus (Level 3).
3. **Authentic Past Papers & CATs**:
   - Real Continuous Assessment Tests (CATs) and final examination papers mapped directly to syllabus topics.
   - Step-by-Step Verified Solutions & Marking Schemes displayed with high-contrast outlines and rubrics.
   - The AI Tutor and generators have complete context of past examination questions and marking schemes for every topic.
4. **AI Practice Question Generator**:
   - Synthesizes 1 to 5 exam-calibrated practice question variants with step-by-step marking rubrics to reinforce core syllabus concepts, grounded in both lecture notes and authentic past papers.
5. **Document Ingestion Pipeline**:
   - Students upload past papers, CATs, lecture notes, or tutorial sheets for review and indexing into the syllabus catalog.
6. **Study Pack Exports**:
   - Complete revision notes and past paper question packs downloadable as formatted PDF and Word DOCX files.

### COURSE CATALOG & AVAILABILITY POLICY:
- Mentify Prep covers courses across Mathematics, Statistics, Computing, Engineering, Business & Economics, and General Sciences.
- Do NOT output or dump a list of all courses under any circumstances.
- If a student asks generally "what courses do you offer?" or "what courses are available?", guide them to browse and search the catalog at [Courses & Syllabi](/prep/courses/), and let them know they can ask you if any specific course unit (e.g. SMA 300, STA 200, Real Analysis, etc.) is available.
{course_query_block}
### SUBSCRIPTION PLANS & BILLING:
- **Free Trial**: Every new student receives 30 free starter credits valid for 3 days upon signup ('Free' badge), with complete access to all platform features.
- **Basic (Starter Prep)**: KES 399 / month ('Basic' badge). Includes 250 credits/mo, up to 10 document uploads, 100 practice questions, 5 scanned OCR uploads.
- **Plus (Semester Pass - Recommended)**: KES 499 / month ('Plus' badge). Includes 450 credits/mo, up to 20 document uploads, 200 practice questions, 15 scanned OCR uploads, priority generation queue.
- **Pro (Exam Master)**: KES 799 / month ('Pro' badge). Includes 750 credits/mo, up to 40 document uploads, 350 practice questions, 30 scanned OCR uploads, top-priority queue & exam support.
- **Plan Upgrades & Lot Retention**: Students can upgrade plans anytime (e.g., Basic to Pro). Credits from existing subscriptions remain active and expire on their original schedule, while the active badge updates immediately to the upgraded tier.
- **Top-Up Pack**: KES 150 for 100 credits (30-day validity) for active subscribers.
- **Payment Method**: Secure M-Pesa STK Push and debit/credit cards processed seamlessly via Paystack.

### CREDIT CONSUMPTION RULES:
- **0 Credits (Free)**: Browsing course catalog, viewing syllabus topics, viewing cached past questions & verified solutions, viewing past revision history, downloading previously opened notes.
- **1 Credit**: AI Study Tutor conversation reply (minimum 1 credit); generating an AI practice question variant.
- **2 Credits**: Uploading a digital text PDF, DOCX, or Markdown document to course materials.
- **5 Credits**: AI Tutor image or scanned PDF upload (Vision OCR per image/page); uploading a handwritten exam or document scan; deep mathematical proof derivation.
- **3 Credits**: Generating on-demand AI topic summary notes.
{user_context_block}
### STRICT OPERATING RULES & GUARDRAILS:
1. **NO MENTION OF ACADEMIC LEVEL**: Strictly DO NOT use or mention academic level labels such as 'university', 'undergraduate', 'college', 'high school', or 'degree level' under any circumstances. Always refer to users neutrally as students or learners preparing for their courses and exams.
2. **Be Concise & Helpful**: Keep responses clear, professional, direct, and well-structured (100-220 words max).
3. **MANDATORY SMART LINKING**: ANY TIME you mention or reference ANY course, dashboard, upload page, billing page, or WhatsApp contact (+254731900577), you MUST format it as a standard clickable Markdown link [Text](URL). NEVER put backticks (`) around links!
   - **Course Link**: [Course Code - Title](/prep/courses/{'{CourseCode}'}/) (e.g. [SMA 300 - Real Analysis I](/prep/courses/SMA%20300/))
   - **Catalog Link**: [Courses & Syllabi](/prep/courses/)
   - **Study Library**: [Study Library](/prep/library/)
   - **Upload Page**: [Upload Study Material](/prep/upload/)
   - **Billing & Plans**: [Credits & Plans](/prep/billing/)
   - **Dashboard**: [Prep Dashboard](/prep/)
   - **Contact Support**: [Contact Support](/accounts/contact/)
   - **Terms**: [Terms of Service](/prep/terms/)
   - **Privacy**: [Privacy Policy](/prep/privacy/)
   - **Main Mentify App**: [Mentify Main App](/dashboard/)
   - **WhatsApp Support**: [Chat on WhatsApp (+254731900577)](https://wa.me/254731900577)
   NEVER write links in backticks or code spans. Write clean Markdown links directly in your text.
4. **STRICTLY STICK TO MENTIFY PREP**: Only answer questions about Mentify Prep, courses, past papers, syllabus modules, uploads, mathematical problem solving, credits, and billing plans.
   - If a student asks general non-educational questions (weather, general news, politics, sports), politely redirect them:
     "I am your Mentify Prep Assistant! I can help you with your courses, past papers, syllabus revision, uploads, and credit plans. How can I assist your exam preparation today?"
5. **NO EMOJIS**: Do NOT use any emojis in your responses under any circumstances. Use clean text and standard punctuation only.
6. **KaTeX Math Formatting**: When presenting mathematical expressions, equations, or formulas, always wrap them in LaTeX syntax: `$formula$` for inline math (e.g. `$f'(x) = 2x$`) or `$$formula$$` for block math equations.
"""
    return system_prompt


def generate_prep_chat_response(messages_history: list, user_message: str, user=None) -> str:
    """
    Calls the Gemini REST API with Prep database grounding context,
    strict token budgets, and history pruning.
    Matches the architecture and error handling of Mentify Assistant.
    """
    # 1. Check API Key
    api_key = os.environ.get("GEMINI_API_KEY", "").strip() or os.environ.get("GOOGLE_API_KEY", "").strip()
    if not api_key:
        load_dotenv(BASE_DIR / ".env", override=True)
        api_key = os.environ.get("GEMINI_API_KEY", "").strip() or os.environ.get("GOOGLE_API_KEY", "").strip()

def call_together_prep_fallback(messages_history: list, user_message: str, system_prompt: str) -> str | None:
    """
    Fallback chat completion using Together AI when Gemini token limits,
    quotas, or rate limits are reached for Mentify Prep Assistant.
    """
    api_key = (
        getattr(settings, "TOGETHERAI_API", "")
        or os.environ.get("TOGETHERAI_API", "")
    ).strip()
    if not api_key:
        load_dotenv(BASE_DIR / ".env", override=True)
        api_key = (
            getattr(settings, "TOGETHERAI_API", "")
            or os.environ.get("TOGETHERAI_API", "")
        ).strip()
    if not api_key:
        logger.warning("[Together AI Prep Fallback] TOGETHERAI_API key is not configured.")
        return None

    model = (
        getattr(settings, "TOGETHER_CHAT_MODEL", "")
        or os.environ.get("TOGETHER_CHAT_MODEL", "")
        or getattr(settings, "TOGETHER_REPAIR_MODEL", "deepseek-ai/DeepSeek-V4.1-Flash")
    ).strip()

    messages = [{"role": "system", "content": system_prompt}]
    if isinstance(messages_history, list):
        for msg in messages_history[-4:]:
            role = "assistant" if msg.get("role") in ["model", "assistant", "bot"] else "user"
            text = msg.get("text") or msg.get("content") or ""
            if text:
                messages.append({"role": role, "content": str(text)[:500]})

    user_text = str(user_message).strip()[:500]
    if not messages or messages[-1].get("content") != user_text:
        messages.append({"role": "user", "content": user_text})

    try:
        url = "https://api.together.xyz/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": 800,
            "temperature": 0.3,
        }
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        if resp.status_code == 200:
            data = resp.json()
            choices = data.get("choices", [])
            if choices:
                content = choices[0].get("message", {}).get("content")
                if content and isinstance(content, str) and content.strip():
                    logger.info("[Together AI Prep Fallback] Prep Assistant answered inquiry via %s", model)
                    return content.strip()
        logger.warning("[Together AI Prep Fallback] HTTP %s: %s", resp.status_code, resp.text[:200])
    except Exception as exc:
        logger.warning("[Together AI Prep Fallback] Exception calling Together AI: %s", exc)

    return None


def generate_prep_chat_response(messages_history: list, user_message: str, user=None) -> str:
    """
    Calls the Gemini REST API with strict grounding context, credit consumption rules,
    course/topic catalogs, and smart linking. Automatically falls back to Together AI
    if Gemini token limits, quotas, or rate limits are reached.
    """
    user_text = str(user_message).strip()[:500]
    system_prompt = get_prep_system_context(user=user, user_message=user_text)

    # 1. Check API Key
    api_key = os.environ.get("GEMINI_API_KEY", "").strip() or os.environ.get("GOOGLE_API_KEY", "").strip()
    if not api_key:
        load_dotenv(BASE_DIR / ".env", override=True)
        api_key = os.environ.get("GEMINI_API_KEY", "").strip() or os.environ.get("GOOGLE_API_KEY", "").strip()

    if not api_key:
        logger.warning("Gemini API key is not configured for Mentify Prep Assistant; checking Together AI fallback...")
        fallback = call_together_prep_fallback(messages_history, user_text, system_prompt)
        if fallback:
            return fallback
        return (
            "The Mentify Prep Assistant is momentarily unavailable while updating its study index. "
            "Please try again in a few moments, or explore your [Courses & Syllabi](/prep/courses/) directly."
        )

    # 2. Prune and format chat history (Max last 4 messages to preserve tokens)
    clean_history = []
    if isinstance(messages_history, list):
        for msg in messages_history[-4:]:
            role = msg.get("role", "user")
            text = msg.get("text") or msg.get("content") or ""
            if not text:
                continue
            gemini_role = "model" if role in ["model", "assistant", "bot"] else "user"
            clean_history.append({
                "role": gemini_role,
                "parts": [{"text": str(text)[:500]}]
            })

    if not clean_history or clean_history[-1].get("parts", [{}])[0].get("text") != user_text:
        clean_history.append({
            "role": "user",
            "parts": [{"text": user_text}]
        })

    # 3. Construct Gemini REST API Payload
    model_name = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash-lite").strip() or "gemini-2.5-flash-lite"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}

    payload = {
        "system_instruction": {
            "parts": [{"text": system_prompt}]
        },
        "contents": clean_history,
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 450,
            "topP": 0.95
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=12)
        response_data = response.json()

        if response.status_code != 200:
            error_msg = response_data.get("error", {}).get("message", "API call failed")
            error_code = response_data.get("error", {}).get("code", response.status_code)
            logger.error(f"Gemini API Error in Prep Assistant ({response.status_code} / {error_code}): {error_msg}")

            # Fallback to Together AI when Gemini token limits, quota, or rate limits are reached
            logger.info("Attempting Together AI fallback for Prep Assistant...")
            fallback = call_together_prep_fallback(messages_history, user_text, system_prompt)
            if fallback:
                return fallback

            if response.status_code == 429 or "quota" in error_msg.lower() or "rate limit" in error_msg.lower() or "RESOURCE_EXHAUSTED" in error_msg:
                return (
                    "I am currently receiving a high volume of student inquiries! "
                    "Please wait about a minute and try asking your question again, "
                    "or [Chat on WhatsApp (+254731900577)](https://wa.me/254731900577) for immediate assistance."
                )

            if "API_KEY_INVALID" in error_msg or "API key not valid" in error_msg:
                return "The AI assistant service is undergoing configuration. Please try again shortly or contact support on WhatsApp."

            return (
                "I am momentarily unavailable. Please try again in a moment, "
                "or [Chat on WhatsApp (+254731900577)](https://wa.me/254731900577) for direct help."
            )

        candidates = response_data.get("candidates", [])
        if candidates and "content" in candidates[0]:
            parts = candidates[0]["content"].get("parts", [])
            if parts and "text" in parts[0]:
                return parts[0]["text"].strip()

        # If candidates empty, try Together AI fallback
        fallback = call_together_prep_fallback(messages_history, user_text, system_prompt)
        if fallback:
            return fallback

        return (
            "I couldn't process that query right now. Please try rephrasing your question or "
            "[Chat on WhatsApp (+254731900577)](https://wa.me/254731900577) for assistance."
        )

    except requests.exceptions.Timeout:
        logger.error("Gemini API request timed out in Prep Assistant; triggering Together AI fallback...")
        fallback = call_together_prep_fallback(messages_history, user_text, system_prompt)
        if fallback:
            return fallback
        return (
            "My connection took a bit too long to respond. Please try asking your question again in a moment, "
            "or [Chat on WhatsApp (+254731900577)](https://wa.me/254731900577)."
        )
    except Exception as e:
        logger.error(f"Unexpected error calling Gemini API in Prep Assistant: {e}; triggering Together AI fallback...")
        fallback = call_together_prep_fallback(messages_history, user_text, system_prompt)
        if fallback:
            return fallback
        return (
            "An unexpected connection issue occurred. Please try again shortly or "
            "[Chat on WhatsApp (+254731900577)](https://wa.me/254731900577)."
        )
