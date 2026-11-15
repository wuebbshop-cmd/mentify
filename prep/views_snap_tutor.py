"""Views for the Universal Snap Tutor."""

from __future__ import annotations

import json
import logging
from typing import Any

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from prep.models import PrepSnapSession, PrepWallet
from services.credit_service import get_available_credits
from services.snap_tutor_service import (
    execute_snap_tutor_turn,
    get_or_create_snap_session,
    get_snap_session_messages,
    list_snap_sessions,
)

logger = logging.getLogger(__name__)


def prep_snap_tutor(request: HttpRequest) -> HttpResponse:
    """Render the full-screen universal snap tutor workspace."""
    user = request.user
    user_credits = 0
    if user.is_authenticated:
        wallet = PrepWallet.get_or_create_wallet(user)
        user_credits = get_available_credits(wallet)

    recent_sessions = list_snap_sessions(user) if user.is_authenticated else []

    context = {
        "active_tab": "mentify_ai",
        "user_credits": user_credits,
        "recent_sessions": recent_sessions,
        "education_levels": PrepSnapSession.EDUCATION_LEVEL_CHOICES,
        "subjects": PrepSnapSession.SUBJECT_CHOICES,
        "default_level": "secondary",
        "default_subject": "general",
    }
    return render(request, "prep/snap_tutor.html", context)


def prep_snap_tutor_api(request: HttpRequest) -> JsonResponse:
    """API endpoint for Universal Snap Tutor sessions and turns."""
    user = request.user

    if request.method == "GET":
        action = request.GET.get("action", "").strip()
        if action == "list_sessions":
            sessions = list_snap_sessions(user)
            return JsonResponse({"success": True, "sessions": sessions})

        session_id = request.GET.get("session_id", "").strip()
        if session_id:
            try:
                session = PrepSnapSession.objects.get(id=session_id)
                if user.is_authenticated and session.user and session.user != user and not user.is_staff:
                    return JsonResponse({"success": False, "error": "Access denied."}, status=403)
                messages = get_snap_session_messages(session)
                return JsonResponse({
                    "success": True,
                    "session": {
                        "id": str(session.id),
                        "title": session.title,
                        "education_level": session.education_level,
                        "education_level_display": session.get_education_level_display(),
                        "subject": session.subject,
                        "subject_display": session.get_subject_display(),
                    },
                    "messages": messages,
                })
            except (PrepSnapSession.DoesNotExist, ValueError):
                return JsonResponse({"success": False, "error": "Session not found."}, status=404)

        return JsonResponse({"success": True, "sessions": list_snap_sessions(user)})

    if request.method == "POST":
        user_message = request.POST.get("message", "").strip()
        session_id = request.POST.get("session_id", "").strip()
        education_level = request.POST.get("education_level", "secondary").strip()
        subject = request.POST.get("subject", "general").strip()

        uploaded_files = request.FILES.getlist("files") or request.FILES.getlist("file")

        if not user_message and not uploaded_files:
            return JsonResponse(
                {"success": False, "error": "Please type a question or upload a worksheet image."},
                status=400,
            )

        try:
            session = get_or_create_snap_session(
                user=user,
                session_id=session_id or None,
                education_level=education_level,
                subject=subject,
            )

            result = execute_snap_tutor_turn(
                user=user,
                session=session,
                user_message=user_message,
                uploaded_files=uploaded_files,
            )
            return JsonResponse(result)
        except Exception as exc:
            logger.exception("Error executing snap tutor turn: %s", exc)
            return JsonResponse({"success": False, "error": str(exc)}, status=500)

    if request.method == "DELETE":
        session_id = request.GET.get("session_id", "").strip()
        if not session_id:
            try:
                data = json.loads(request.body)
                session_id = data.get("session_id", "")
            except Exception:
                pass

        if not session_id:
            return JsonResponse({"success": False, "error": "session_id is required."}, status=400)

        try:
            lookup: dict[str, Any] = {"id": session_id}
            if user.is_authenticated and not user.is_staff:
                lookup["user"] = user
            PrepSnapSession.objects.filter(**lookup).delete()
            return JsonResponse({"success": True})
        except Exception as exc:
            return JsonResponse({"success": False, "error": str(exc)}, status=500)

    return JsonResponse({"success": False, "error": "Method not allowed."}, status=405)
