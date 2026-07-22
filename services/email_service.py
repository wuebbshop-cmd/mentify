"""Resend.com email delivery for Mentify (works on Render free tier)."""
from __future__ import annotations

import logging

import requests
from django.conf import settings

logger = logging.getLogger(__name__)

RESEND_API_URL = "https://api.resend.com/emails"


def send_email_notification(
    subject: str,
    recipient: str,
    body: str,
    *,
    html_body: str | None = None,
    from_email: str | None = None,
    reply_to: str | None = None,
) -> bool:
    """Send a transactional email through Resend."""
    api_key = getattr(settings, "RESEND_API_KEY", "").strip()
    sender = (from_email or getattr(settings, "DEFAULT_FROM_EMAIL", "")).strip()
    recipient = recipient.strip()

    if not api_key:
        logger.warning("RESEND_API_KEY is not configured; email to %s was not sent.", recipient)
        return False
    if not sender:
        logger.warning("DEFAULT_FROM_EMAIL is not configured; email to %s was not sent.", recipient)
        return False
    if not recipient:
        return False

    payload: dict = {
        "from": sender,
        "to": [recipient],
        "subject": subject,
        "text": body,
    }
    if html_body:
        payload["html"] = html_body
    if reply_to:
        payload["reply_to"] = reply_to

    try:
        response = requests.post(
            RESEND_API_URL,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=15,
        )
    except requests.RequestException:
        logger.exception("Failed to reach Resend for %s", recipient)
        return False

    if response.status_code not in (200, 201):
        logger.error(
            "Resend rejected email to %s: %s %s",
            recipient,
            response.status_code,
            response.text,
        )
        return False

    return True


def send_welcome_email(user) -> bool:
    platform = getattr(settings, "PLATFORM_NAME", "Mentify")
    subject = f"Welcome to {platform}"
    body = (
        f"Hello {user.first_name or 'there'},\n\n"
        f"Thank you for joining {platform}. Your account is ready and you can now "
        f"sign in with your email address.\n\n"
        "If you did not create this account, you can ignore this email.\n\n"
        f"Welcome aboard,\nThe {platform} Team"
    )
    return send_email_notification(subject, user.email, body)
