"""
services/chatbot_service.py

Service for Mentify Customer Service AI Chatbot powered by Google Gemini API.
Handles dynamic database context extraction, system prompt construction, token usage control,
smart course linking, and chat history management.
"""

import os
import json
import logging
import requests
from pathlib import Path
from dotenv import load_dotenv
from django.conf import settings

logger = logging.getLogger(__name__)

# Ensure .env is loaded
BASE_DIR = getattr(settings, "BASE_DIR", Path(__file__).resolve().parents[1])
load_dotenv(BASE_DIR / ".env", override=True)


def get_mentify_system_context() -> str:
    """
    Dynamically fetch active courses, cohorts, pricing, and platform features from Django DB
    to construct a real-time system context for Gemini.
    """
    courses_context_lines = []
    
    try:
        from courses.models import Course, Cohort
        
        active_courses = Course.objects.filter(is_active=True).prefetch_related("cohorts")
        for course in active_courses:
            cohort_info = []
            for cohort in course.cohorts.filter(status=Cohort.Status.ACTIVE):
                tutor_name = cohort.tutor.get_full_name() if cohort.tutor else "Expert Tutor"
                cohort_info.append(
                    f"  - Cohort '{cohort.name}': KES {cohort.price_kes:.0f}/month (Tutor: {tutor_name}, Start: {cohort.start_date or 'TBA'})"
                )
            
            cohort_str = "\n".join(cohort_info) if cohort_info else "  - No active public cohort right now (1-on-1 custom tutoring available)."
            
            desc_short = course.description[:180].replace("\n", " ") + "..." if len(course.description) > 180 else course.description
            courses_context_lines.append(
                f"- **Title**: {course.title} | **URL**: /courses/{course.slug}/\n"
                f"  Track: {course.get_track_display()} | Level: {course.get_level_display()} | Subject: {course.subject_area or 'General'}\n"
                f"  Summary: {desc_short}\n"
                f"  Cohorts: {cohort_str}\n"
            )
    except Exception as e:
        logger.warning(f"Could not load dynamic courses context: {e}")
        courses_context_lines.append("- Catalog available at /courses/")

    courses_block = "\n".join(courses_context_lines)

    system_prompt = f"""You are Mentify Assistant, the friendly, intelligent AI customer service assistant for Mentify (https://mlaudit.info).

### PLATFORM OVERVIEW:
Mentify is an online learning platform offering high-quality courses and tutoring for primary school learners, JSS, senior school students, graduates, and adults.
- **Learning Tracks**:
  1. Tech Track: Programming (Python, Web Development), Machine Learning, AI, Software Engineering, Math & Statistics for ML.
  2. CBE Academic Track: Kenyan Competency Based Education subjects (Mathematics, Science, English, etc.) for Primary & JSS learners.
  3. Specialist Track: Robotics, Cybersecurity, and specialized tech topics.
- **Delivery**: Live online video sessions, pre-recorded video lessons, assignments with tutor grading, and progress tracking.
- **Payments**: Monthly subscriptions paid securely via M-Pesa or Card through Paystack.
- **1-on-1 Custom Programs & Tutoring**: Students or parents who want private 1-on-1 personalized tutoring or custom schedules can chat directly on WhatsApp at +254731900577 (or click WhatsApp links on course pages).

### ACTIVE COURSE CATALOG:
{courses_block}

### STRICT OPERATING RULES & GUARDRAILS:
1. **Be Helpful & Concise**: Keep responses concise, clear, and encouraging (100-200 words max).
2. **MANDATORY SMART LINKING**: ANY TIME you mention or reference ANY course, cohort, platform page, or WhatsApp contact (+254731900577), you MUST format it as a clickable Markdown link `[Text](URL)`:
   - **Course Links**: `[Course Title](/courses/course-slug/)` (e.g. `[Building with AI](/courses/building-with-ai/)`)
   - **WhatsApp Contact Links**: `[Chat on WhatsApp (+254731900577)](https://wa.me/254731900577)`
   - **Catalog Link**: `[Browse All Courses](/courses/)`
   - **Contact Link**: `[Contact Us](/contact/)`
   - **Registration Link**: `[Join Mentify Free](/accounts/register/)`
   NEVER mention a course title, phone number (+254731900577), or page reference as plain unlinked text!
3. **STRICTLY STICK TO MENTIFY CONTEXT**: Only answer questions about Mentify, its courses, cohorts, enrollment, pricing, tracks, tutors, learning features, or custom tutoring options.
   - If a user asks non-Mentify questions (e.g. general coding debugging unrelated to course inquiries, weather, recipes, politics, general trivia), politely reply:
     "I am Mentify's AI guide! I can only answer questions about Mentify's platform, courses, tutoring, and enrollment. How can I help you explore our learning programs?"
4. **Accurate Pricing & Information**: Do not invent courses, pricing, or features not listed in the context.
5. **Formatting**: Use Markdown formatting (bold text, lists, line breaks) so the UI renders your response cleanly.
6. **NO EMOJIS**: Do NOT use any emojis in your responses under any circumstances. Use clean text and standard punctuation only.
"""
    return system_prompt


def generate_chat_response(messages_history: list, user_message: str) -> str:
    """
    Calls the Gemini REST API with strict token limits, system grounding context,
    and history pruning.
    """
    # 1. Check API Key
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        # Re-try loading .env
        load_dotenv(BASE_DIR / ".env", override=True)
        api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    
    if not api_key:
        return (
            "The Gemini API key is missing. Please add `GEMINI_API_KEY=your_key_here` "
            "to your `.env` file to activate the Mentify AI Assistant."
        )

    # 2. Prune and format chat history (Max last 4 messages to save tokens)
    clean_history = []
    if isinstance(messages_history, list):
        for msg in messages_history[-4:]:
            role = msg.get("role", "user")
            text = msg.get("text") or msg.get("content") or ""
            if not text:
                continue
            # Map standard roles to Gemini roles
            gemini_role = "model" if role in ["model", "assistant", "bot"] else "user"
            clean_history.append({
                "role": gemini_role,
                "parts": [{"text": str(text)[:500]}]  # Cap turn length
            })

    # Add current user message if not already in history
    user_text = str(user_message).strip()[:500]
    if not clean_history or clean_history[-1].get("parts", [{}])[0].get("text") != user_text:
        clean_history.append({
            "role": "user",
            "parts": [{"text": user_text}]
        })

    # 3. System Prompt Context
    system_prompt = get_mentify_system_context()

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
            "maxOutputTokens": 400,
            "topP": 0.95
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=12)
        response_data = response.json()

        if response.status_code != 200:
            error_msg = response_data.get("error", {}).get("message", "API call failed")
            error_code = response_data.get("error", {}).get("code", response.status_code)
            
            # Log exact technical error internally
            logger.error(f"Gemini API Error ({response.status_code} / {error_code}): {error_msg}")

            # Return clean, user-friendly responses without exposing raw API or quota details
            if response.status_code == 429 or "quota" in error_msg.lower() or "rate limit" in error_msg.lower() or "RESOURCE_EXHAUSTED" in error_msg:
                return (
                    "I am currently receiving a high volume of inquiries! "
                    "Please wait about a minute and try asking your question again, "
                    "or [Chat on WhatsApp (+254731900577)](https://wa.me/254731900577) for immediate assistance."
                )
            
            if "API_KEY_INVALID" in error_msg or "API key not valid" in error_msg:
                return "The AI assistant service is undergoing configuration. Please try again shortly or contact us on WhatsApp."

            return (
                "I am momentarily unavailable. Please try again in a moment, "
                "or [Chat on WhatsApp (+254731900577)](https://wa.me/254731900577) to reach us directly!"
            )

        candidates = response_data.get("candidates", [])
        if candidates and "content" in candidates[0]:
            parts = candidates[0]["content"].get("parts", [])
            if parts and "text" in parts[0]:
                return parts[0]["text"].strip()
        
        return (
            "I couldn't process that query right now. Please try rephrasing your question or "
            "[Chat on WhatsApp (+254731900577)](https://wa.me/254731900577) for help."
        )

    except requests.exceptions.Timeout:
        logger.error("Gemini API request timed out")
        return (
            "My connection took a bit too long to respond. Please try asking your question again in a moment, "
            "or [Chat on WhatsApp (+254731900577)](https://wa.me/254731900577)."
        )
    except Exception as e:
        logger.error(f"Unexpected error calling Gemini API: {e}")
        return (
            "An unexpected connection issue occurred. Please try again shortly or "
            "[Chat on WhatsApp (+254731900577)](https://wa.me/254731900577)."
        )
