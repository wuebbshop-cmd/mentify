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


def get_prep_system_context(user=None) -> str:
    """
    Dynamically fetch active courses, syllabus modules, paper counts,
    and user wallet/enrollment state to build real-time system context for Gemini.
    """
    course_lines = []

    try:
        from prep.models import PrepCourse
        courses = PrepCourse.objects.filter(is_active=True).prefetch_related("topics", "papers")[:25]
        for c in courses:
            topics = list(c.topics.all()[:4])
            topic_names = ", ".join([t.title for t in topics]) if topics else "Syllabus in indexing"
            papers_count = c.papers.filter(is_published=True).count()
            course_url = f"/prep/courses/{quote(c.code)}/"
            course_lines.append(
                f"- **{c.code}**: {c.title} (Level: {c.level}, Category: {c.category})\n"
                f"  URL: {course_url}\n"
                f"  Past Papers Available: {papers_count} | Sample Topics: {topic_names}"
            )
    except Exception as e:
        logger.warning(f"Could not load dynamic prep courses context: {e}")
        course_lines.append("- Catalog available at /prep/courses/")

    courses_block = "\n".join(course_lines) if course_lines else "- No courses indexed yet."

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
Mentify Prep is an exam readiness and past-paper revision engine tailored for university undergraduate and college students in Kenya and East Africa.
Key capabilities:
1. **Course-Anchored Revision**: Organizes study materials strictly by course code (e.g. SMA 300, STA 200, CIT 100), syllabus modules, and subtopics.
2. **Authentic Past Papers & CATs**: Real Continuous Assessment Tests and final examination papers with step-by-step verified mathematical proofs and derivations.
3. **Multi-Level AI Proofs & Explanations**: 
   - Intuitive (high-level visual intuition)
   - Step-by-Step (structured working with intermediate steps)
   - Deep Theoretical (rigorous formal proofs, theorems, edge cases, SymPy verified)
4. **AI Practice Question Generator**: Generates targeted exam problem variants with customizable difficulty to reinforce core syllabus concepts.
5. **Document Ingestion Pipeline**:
   - Students upload past papers, CATs, lecture notes, or tutorial sheets.
   - Stage 1: Ingestion & Extraction (pdfplumber digital parser, Vision OCR for handwritten documents/photos).
   - Stage 2: Tutor Review Gate (ensures academic accuracy and syllabus alignment).
   - Stage 3: Published to the global catalog for instant revision.
6. **Study Pack Exports**: Complete revision notes and solved papers downloadable as formatted PDF and Word DOCX files.

### SUBSCRIPTION PLANS & BILLING:
- **Free Trial**: Every new student receives 30 free starter credits valid for 3 days upon signup, with complete access to all platform features.
- **Basic (Starter Prep)**: KES 399 / month. Includes 250 credits/mo, up to 10 document uploads, 100 practice questions, 5 scanned OCR uploads.
- **Plus (Semester Pass - Recommended)**: KES 499 / month. Includes 450 credits/mo, up to 20 document uploads, 200 practice questions, 15 scanned OCR uploads, priority generation queue. (Best value for active semester revision).
- **Pro (Exam Master)**: KES 799 / month. Includes 750 credits/mo, up to 40 document uploads, 350 practice questions, 30 scanned OCR uploads, top-priority queue & exam support.
- **Top-Up Pack**: KES 150 for 100 credits anytime for users with an active subscription.
- **Payment Method**: Secure M-Pesa STK Push and debit/credit cards processed seamlessly via Paystack.

### CREDIT CONSUMPTION RULES:
- **0 Credits (Free)**: Browsing course catalog, viewing syllabus topics, viewing verified/cached solutions, viewing past revision history, downloading previously opened notes.
- **2 Credits**: Uploading a digital text PDF, DOCX, or Markdown document.
- **5 Credits**: Uploading a scanned handwritten document or camera photo (Vision OCR).
- **5 Credits**: Uncached deep mathematical derivation or complex formal proof.
- **1 Credit**: Generating an AI practice question variant.
- **3 Credits**: Generating on-demand AI topic summary notes.
{user_context_block}
### AVAILABLE COURSES IN PREP:
{courses_block}

### STRICT OPERATING RULES & GUARDRAILS:
1. **Be Concise & Helpful**: Keep responses clear, professional, direct, and well-structured (100-220 words max).
2. **MANDATORY SMART LINKING**: ANY TIME you mention or reference ANY course, dashboard, upload page, billing page, or WhatsApp contact (+254731900577), you MUST format it as a clickable Markdown link `[Text](URL)`:
   - **Course Link**: `[Course Code - Title](/prep/courses/{'{CourseCode}'}/)` (e.g. `[SMA 300 - Real Analysis I](/prep/courses/SMA%20300/)`)
   - **Catalog Link**: `[Courses & Syllabi](/prep/courses/)`
   - **Upload Page**: `[Upload Study Material](/prep/upload/)`
   - **Billing & Plans**: `[Credits & Plans](/prep/billing/)`
   - **Dashboard**: `[Prep Dashboard](/prep/)`
   - **Terms**: `[Terms of Service](/prep/terms/)`
   - **Privacy**: `[Privacy Policy](/prep/privacy/)`
   - **Main Mentify App**: `[Mentify Main App](/dashboard/)`
   - **WhatsApp Support**: `[Chat on WhatsApp (+254731900577)](https://wa.me/254731900577)`
   NEVER leave a course code, page reference, or contact number unlinked!
3. **STRICTLY STICK TO MENTIFY PREP**: Only answer questions about Mentify Prep, courses, past papers, syllabus modules, uploads, mathematical problem solving, credits, and billing plans.
   - If a student asks general non-educational questions (weather, general news, politics, sports), politely redirect them:
     "I am your Mentify Prep Assistant! I can help you with your courses, past papers, syllabus revision, uploads, and credit plans. How can I assist your exam preparation today?"
4. **NO EMOJIS**: Do NOT use any emojis in your responses under any circumstances. Use clean text and standard punctuation only.
5. **KaTeX Math Formatting**: When presenting mathematical expressions, equations, or formulas, always wrap them in LaTeX syntax: `$formula$` for inline math (e.g. `$f'(x) = 2x$`) or `$$formula$$` for block math equations.
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

    if not api_key:
        return (
            "The Gemini API key is missing. Please add `GEMINI_API_KEY=your_key_here` "
            "to your `.env` file to activate the Mentify Prep Assistant."
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

    user_text = str(user_message).strip()[:500]
    if not clean_history or clean_history[-1].get("parts", [{}])[0].get("text") != user_text:
        clean_history.append({
            "role": "user",
            "parts": [{"text": user_text}]
        })

    # 3. System Prompt Context
    system_prompt = get_prep_system_context(user=user)

    # 4. Construct Gemini REST API Payload
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

        return (
            "I couldn't process that query right now. Please try rephrasing your question or "
            "[Chat on WhatsApp (+254731900577)](https://wa.me/254731900577) for assistance."
        )

    except requests.exceptions.Timeout:
        logger.error("Gemini API request timed out in Prep Assistant")
        return (
            "My connection took a bit too long to respond. Please try asking your question again in a moment, "
            "or [Chat on WhatsApp (+254731900577)](https://wa.me/254731900577)."
        )
    except Exception as e:
        logger.error(f"Unexpected error calling Gemini API in Prep Assistant: {e}")
        return (
            "An unexpected connection issue occurred. Please try again shortly or "
            "[Chat on WhatsApp (+254731900577)](https://wa.me/254731900577)."
        )
