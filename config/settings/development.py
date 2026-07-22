"""Development settings - DEBUG on, SQLite fallback not used (always MySQL)."""

from .base import *  # noqa: F401, F403

DEBUG = True

# In dev, allow all hosts
ALLOWED_HOSTS = ["*"]

# Uses Resend when RESEND_API_KEY is set (see base.py), otherwise console backend.

# Django debug toolbar (optional, install separately if needed)
# INSTALLED_APPS += ["debug_toolbar"]

INTERNAL_IPS = ["127.0.0.1"]
