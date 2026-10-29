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
    """
    Suppressed to preserve Resend free-tier API quota for essential transactional emails.
    Account readiness is already confirmed on screen after signup.
    """
    logger.info("Welcome email suppressed for %s to preserve Resend free-tier quota.", getattr(user, "email", "user"))
    return True


def send_email_verification_email(user, verification_url: str) -> bool:
    """Send the one-time link required before a password account can sign in."""
    platform = getattr(settings, "PLATFORM_NAME", "Mentify")
    subject = f"Verify your {platform} email address"
    body = (
        f"Hello {user.first_name or 'there'},\n\n"
        f"Verify your email address to activate your {platform} account:\n\n"
        f"{verification_url}\n\n"
        "This link expires according to the site's password-reset timeout. "
        "If you did not create this account, you can ignore this email.\n\n"
        f"The {platform} Team"
    )
    html_body = (
        f'<p>Hello {user.first_name or "there"},</p>'
        f'<p>Verify your email address to activate your {platform} account.</p>'
        f'<p><a href="{verification_url}">Verify email address</a></p>'
        '<p>This link expires according to the site password-reset timeout. '
        'If you did not create this account, you can ignore this email.</p>'
    )
    return send_email_notification(subject, user.email, body, html_body=html_body)


def send_prep_note_generation_failure_email(guard) -> bool:
    """
    Suppressed to preserve admin Resend free-tier quota.
    Generation failures are already recorded in PrepNoteGenerationGuard in the database
    and visible in the Django Admin review queue without wasting email API credits.
    """
    logger.info(
        "Note generation review needed for guard %s (%s - %s). Logged to database; email suppressed to preserve quota.",
        getattr(guard, "pk", None),
        getattr(getattr(guard, "topic", None), "title", "Unknown"),
        getattr(guard, "level", "unknown"),
    )
    return True


def send_payment_confirmation_email(payment) -> bool:
    subscription = payment.subscription
    learner = subscription.learner
    cohort = subscription.cohort
    platform = getattr(settings, "PLATFORM_NAME", "Mentify")
    subject = f"Payment confirmed for {cohort.course.title}"
    body = (
        f"Hello {learner.first_name or 'there'},\n\n"
        f"We have confirmed your payment of KES {payment.amount_kes} for {cohort.course.title}.\n\n"
        f"Cohort: {cohort.name}\n"
        f"Reference: {payment.reference}\n"
        f"Access valid until: {subscription.paid_until}\n\n"
        "You can sign in and continue from your dashboard.\n\n"
        f"The {platform} Team"
    )
    return send_email_notification(subject, learner.email, body)


# ─── Mentify Prep Email Automations ──────────────────────────────────────────

def send_prep_review_completed_email(prep_doc) -> bool:
    """
    Suppressed to preserve email quota.
    Users check review & publication alerts directly on their dashboard via in-app PrepNotification.
    """
    logger.info(
        "Tutor review completed for document %s (%s). Logged to database; email suppressed (in-app dashboard notification used).",
        getattr(prep_doc, "pk", None),
        getattr(getattr(prep_doc, "course", None), "code", "Unknown"),
    )
    return True


def send_prep_credit_topup_email(wallet, credits_added: int, amount_kes: int, reference: str, package_name: str) -> bool:
    """
    Send an email receipt when an M-Pesa / Paystack credit top-up or plan purchase is confirmed.
    """
    user = wallet.user
    if not user or not user.email:
        return False

    platform = "Mentify Prep"
    subject = f"[{platform}] Credit Purchase Confirmed (+{credits_added} Credits)"
    base_url = getattr(settings, "BASE_URL", "http://127.0.0.1:8000").rstrip("/")
    billing_url = f"{base_url}/prep/billing/"

    body = (
        f"Hello {user.first_name or 'there'},\n\n"
        f"Thank you for your payment! We have confirmed your purchase of {package_name}.\n\n"
        f"Credits Added: +{credits_added} Credits\n"
        f"Amount Paid: KES {amount_kes}\n"
        f"Reference Code: {reference}\n"
        f"New Wallet Balance: {wallet.credits_balance} Credits\n"
        f"Current Plan: {wallet.get_current_plan_display()}\n\n"
        f"You can view your credit transactions and start practicing here:\n{billing_url}\n\n"
        f"Best regards,\nThe {platform} Team"
    )

    html_body = f"""
    <div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; max-width:600px; margin:0 auto; padding:24px; color:#1e293b; background:#ffffff; border:1px solid #e2e8f0; border-radius:8px;">
      <div style="border-bottom:2px solid #0f766e; padding-bottom:12px; margin-bottom:20px;">
        <h2 style="color:#0f766e; margin:0; font-size:1.4rem;">{platform}</h2>
        <span style="font-size:0.85rem; color:#64748b;">Credit Wallet & Payment Confirmation</span>
      </div>

      <p style="font-size:1rem; line-height:1.6;">Hello <strong>{user.first_name or 'Student'}</strong>,</p>
      <p style="font-size:0.95rem; line-height:1.6;">
        Your payment for <strong>{package_name}</strong> via M-Pesa / Paystack was successfully processed.
      </p>

      <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:6px; padding:16px; margin:20px 0;">
        <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
          <span style="color:#166534; font-weight:600;">Credits Added:</span>
          <span style="color:#16a34a; font-weight:700; font-size:1.1rem;">+{credits_added} Credits</span>
        </div>
        <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
          <span style="color:#166534; font-weight:600;">Amount Paid:</span>
          <span style="color:#1e293b; font-weight:600;">KES {amount_kes}</span>
        </div>
        <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
          <span style="color:#166534; font-weight:600;">New Wallet Balance:</span>
          <span style="color:#0f766e; font-weight:700; font-size:1.1rem;">{wallet.credits_balance} Credits</span>
        </div>
        <div style="display:flex; justify-content:space-between;">
          <span style="color:#166534; font-weight:600;">Reference:</span>
          <span style="color:#64748b; font-family:monospace; font-size:0.85rem;">{reference}</span>
        </div>
      </div>

      <div style="margin:24px 0; text-align:center;">
        <a href="{billing_url}" style="background:#0f766e; color:#ffffff; font-weight:600; padding:12px 24px; text-decoration:none; border-radius:6px; display:inline-block;">
          View Your Wallet & Start Practicing
        </a>
      </div>

      <p style="font-size:0.85rem; color:#64748b; line-height:1.5; margin-top:32px; border-top:1px solid #e2e8f0; padding-top:16px;">
        Mentify Prep &bull; High-accuracy syllabus readiness for universities and academic programs.
      </p>
    </div>
    """

    return send_email_notification(subject, user.email, body, html_body=html_body)


def send_prep_low_credits_email(wallet) -> bool:
    """
    Suppressed to preserve Resend free-tier quota.
    Low credit state is already prominently indicated in the in-app UI / credit pill.
    """
    logger.info("Low credit reminder email suppressed for user %s to preserve Resend quota.", getattr(wallet, "user_id", "unknown"))
    return True
