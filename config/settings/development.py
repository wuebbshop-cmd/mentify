"""Development settings - DEBUG on, SQLite fallback not used (always MySQL)."""

import os
from .base import *  # noqa: F401, F403

DEBUG = os.environ.get("DJANGO_DEBUG", os.environ.get("DEBUG", "True")).lower() in ("true", "1", "yes")

# In dev, allow all hosts
ALLOWED_HOSTS = ["*"]

# Uses Resend when RESEND_API_KEY is set (see base.py), otherwise console backend.

# Django debug toolbar (optional, install separately if needed)
# INSTALLED_APPS += ["debug_toolbar"]

INTERNAL_IPS = ["127.0.0.1"]

# CSRF Trusted Origins for local development (resolves fetch 403 Forbidden Origin checks)
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://localhost",
]

