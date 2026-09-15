"""
services/chat_views.py

Django view endpoint for Mentify AI Chatbot.
Receives user message and chat history from frontend AJAX requests,
invokes chatbot_service, and returns JSON response.
"""

import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from services.chatbot_service import generate_chat_response


@require_POST
def chatbot_api_view(request):
    """
    POST /api/chat/
    Body: JSON { "message": "user text", "history": [ { "role": "user"|"model", "text": "..." } ] }
    Returns: JSON { "status": "success", "response": "AI response text" }
    """
    try:
        data = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "error": "Invalid JSON format."}, status=400)

    user_message = data.get("message", "").strip()
    if not user_message:
        return JsonResponse({"status": "error", "error": "Message cannot be empty."}, status=400)

    history = data.get("history", [])
    if not isinstance(history, list):
        history = []

    # Also keep session history fallback
    session_history = request.session.get("chat_history", [])
    if not history and session_history:
        history = session_history

    # Generate response
    ai_response = generate_chat_response(messages_history=history, user_message=user_message)

    # Append to session history
    updated_history = history + [
        {"role": "user", "text": user_message},
        {"role": "model", "text": ai_response},
    ]
    request.session["chat_history"] = updated_history[-10:]  # keep last 10 entries in session

    return JsonResponse({"status": "success", "response": ai_response})
