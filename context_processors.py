"""
mentify/context_processors.py

Global template context — platform name, current user's role info, etc.
"""
from django.conf import settings


def site_context(request):
    return {
        "PLATFORM_NAME": getattr(settings, "PLATFORM_NAME", "Mentify"),
        "PAYSTACK_PUBLIC_KEY": getattr(settings, "PAYSTACK_PUBLIC_KEY", ""),
        "SUPPORT_EMAIL": getattr(settings, "SUPPORT_EMAIL", "mentify@mlaudit.info"),
    }
