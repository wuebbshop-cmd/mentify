"""Production settings - DEBUG off, HTTPS enforced, Render-ready."""

from .base import *  # noqa: F401, F403
import os
import dj_database_url

DEBUG = False

# ─── Database: Render uses PostgreSQL (via DATABASE_URL) ────────────────────
# Render provides DATABASE_URL in production environment
db_from_env = dj_database_url.config(default=None, conn_max_age=600)
if db_from_env:
    DATABASES["default"] = db_from_env
else:
    # Fallback if DATABASE_URL not set (shouldn't happen on Render)
    DATABASES["default"]["ENGINE"] = "django.db.backends.postgresql"
    DATABASES["default"]["NAME"] = os.environ.get("DB_NAME", "")
    DATABASES["default"]["USER"] = os.environ.get("DB_USER", "")
    DATABASES["default"]["PASSWORD"] = os.environ.get("DB_PASSWORD", "")
    DATABASES["default"]["HOST"] = os.environ.get("DB_HOST", "localhost")
    DATABASES["default"]["PORT"] = os.environ.get("DB_PORT", "5432")

# ─── Security: HTTPS and HSTS ──────────────────────────────────────────────
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# ─── Render-specific proxy headers ─────────────────────────────────────────
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# ─── Static files: Render uses persistent storage only for /render/output/ ───
# WhiteNoise in middleware + compression via STATICFILES_STORAGE handle this
# Collect static files before deploy via render.yaml build command

# ─── Email: Gmail SMTP for all notifications ──────────────────────────────
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", "587"))
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")

# ─── Security: SameSite cookie setting ─────────────────────────────────────
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"
