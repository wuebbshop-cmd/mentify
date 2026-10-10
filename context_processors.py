"""
mentify/context_processors.py

Global template context — platform name, current user's role info, subscription badges, etc.
"""
from django.conf import settings
from django.utils import timezone


def get_user_plan_badge(user) -> dict | None:
    """
    Returns active subscription plan badge configuration with matching colors from billing pricing cards.
    - Active 3-day free trial: 'Free' badge
    - Basic plan: 'Basic' badge with #2563eb theme
    - Plus plan: 'Plus' badge with #0f766e (var(--green)) theme
    - Pro plan: 'Pro' badge with #7c3aed theme
    - Expired plan or ended trial: None (no badge displayed)
    """
    if not user or not getattr(user, "is_authenticated", False):
        return None

    try:
        from prep.models import PrepWallet
        wallet = PrepWallet.objects.filter(user=user).first()
        if not wallet:
            return None

        now = timezone.now()
        # When trial or current plan has expired, no badge displays
        if wallet.plan_expires_at and wallet.plan_expires_at <= now:
            return None
        if wallet.current_plan == "expired":
            return None

        if wallet.current_plan == "trial":
            return {
                "plan": "trial",
                "label": "Free",
                "color": "#0284c7",
                "bg": "rgba(2, 132, 199, 0.12)",
                "border": "rgba(2, 132, 199, 0.3)",
            }
        elif wallet.current_plan == "basic":
            return {
                "plan": "basic",
                "label": "Basic",
                "color": "#2563eb",
                "bg": "rgba(37, 99, 235, 0.12)",
                "border": "rgba(37, 99, 235, 0.3)",
            }
        elif wallet.current_plan == "plus":
            return {
                "plan": "plus",
                "label": "Plus",
                "color": "#0f766e",
                "bg": "rgba(15, 118, 110, 0.12)",
                "border": "rgba(15, 118, 110, 0.3)",
            }
        elif wallet.current_plan == "pro":
            return {
                "plan": "pro",
                "label": "Pro",
                "color": "#7c3aed",
                "bg": "rgba(124, 58, 237, 0.12)",
                "border": "rgba(124, 58, 237, 0.3)",
            }
        return None
    except Exception:
        return None


def site_context(request):
    user = getattr(request, "user", None)
    return {
        "PLATFORM_NAME": getattr(settings, "PLATFORM_NAME", "Mentify"),
        "PAYSTACK_PUBLIC_KEY": getattr(settings, "PAYSTACK_PUBLIC_KEY", ""),
        "SUPPORT_EMAIL": getattr(settings, "SUPPORT_EMAIL", "mentify@mlaudit.info"),
        "user_plan_badge": get_user_plan_badge(user),
    }
