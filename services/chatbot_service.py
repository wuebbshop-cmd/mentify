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
            
            courses_context_lines.append(
                f"- **Title**: {course.title}\n"
                f"  **Slug**: {course.slug}\n"
                f"  **URL**: /courses/{course.slug}/\n"
                f"  **Track**: {course.get_track_display()}\n"
                f"  **Level**: {course.get_level_display()}\n"
                f"  **Subject Area**: {course.subject_area or 'General'}\n"
                f"  **Description**: {course.description}\n"
                f"  **Available Cohorts**:\n{cohort_str}\n"
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
2. **SMART COURSE LINKING**: Whenever you mention, explain, or recommend any course, you MUST include its direct Markdown link using the exact format `[Course Title](/courses/course-slug/)`. For example, `[Building with AI](/courses/building-with-ai/)`.
3. **STRICTLY STICK TO MENTIFY CONTEXT**: Only answer questions about Mentify, its courses, cohorts, enrollment, pricing, tracks, tutors, learning features, or custom tutoring options.
   - If a user asks non-Mentify questions (e.g. general coding debugging unrelated to course inquiries, weather, recipes, politics, general trivia), politely reply:
     "I am Mentify's AI guide! I can only answer questions about Mentify's platform, courses, tutoring, and enrollment. How can I help you explore our learning programs?"
4. **Accurate Pricing & Information**: Do not invent courses, pricing, or features not listed in the context.
5. **Formatting**: Use Markdown formatting (bold text, lists, line breaks) so the UI renders your response cleanly.
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

    # 2. Prune and format chat history (Max last 6 messages to stay under free tier token limits)
    clean_history = []
    if isinstance(messages_history, list):
        for msg in messages_history[-6:]:
            role = msg.get("role", "user")
            text = msg.get("text") or msg.get("content") or ""
            if not text:
                continue
            # Map standard roles to Gemini roles
            gemini_role = "model" if role in ["model", "assistant", "bot"] else "user"
            clean_history.append({
                "role": gemini_role,
                "parts": [{"text": str(text)[:1000]}]  # Cap input message length
            })

    # Add current user message if not already in history
    user_text = str(user_message).strip()[:1000]
    if not clean_history or clean_history[-1].get("parts", [{}])[0].get("text") != user_text:
        clean_history.append({
            "role": "user",
            "parts": [{"text": user_text}]
        })

    # 3. System Prompt Context
    system_prompt = get_mentify_system_context()

    # 4. Construct Gemini REST API Payload
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    
    payload = {
        "system_instruction": {
            "parts": [{"text": system_prompt}]
        },
        "contents": clean_history,
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 600,
            "topP": 0.95
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=12)
        response_data = response.json()

        if response.status_code != 200:
            error_msg = response_data.get("error", {}).get("message", "API call failed")
            logger.error(f"Gemini API Error ({response.status_code}): {error_msg}")
            if "API_KEY_INVALID" in error_msg or "API key not valid" in error_msg:
                return "The configured `GEMINI_API_KEY` in `.env` appears to be invalid. Please check your API key."
            return f"I ran into an issue connecting to my brain. Please try again shortly. ({error_msg})"

        candidates = response_data.get("candidates", [])
        if candidates and "content" in candidates[0]:
            parts = candidates[0]["content"].get("parts", [])
            if parts and "text" in parts[0]:
                return parts[0]["text"].strip()
        
        return "I'm sorry, I couldn't generate a response for that query. Please try rephrasing your question!"

    except requests.exceptions.Timeout:
        logger.error("Gemini API request timed out")
        return "The request timed out while contacting the AI service. Please try again in a moment."
    except Exception as e:
        logger.error(f"Unexpected error calling Gemini API: {e}")
        return "An error occurred while processing your chat request. Please try again."
