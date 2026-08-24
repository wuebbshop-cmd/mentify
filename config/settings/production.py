"""Production settings - DEBUG off, HTTPS enforced, Render-ready."""

from .base import *  # noqa: F401,F403
import os

DEBUG = False

# Allowed hosts: custom domain, Render domains, and dynamic Render hostname.
env_hosts = [h.strip() for h in os.environ.get("ALLOWED_HOSTS", "").split(",") if h.strip()]
render_host = os.environ.get("RENDER_EXTERNAL_HOSTNAME", "").strip()

ALLOWED_HOSTS = list(set(
    ALLOWED_HOSTS
    + env_hosts
    + [
        "mlaudit.info",
        "www.mlaudit.info",
        ".onrender.com",
        "mentify-klm7.onrender.com",
        "localhost",
        "127.0.0.1",
    ]
    + ([render_host] if render_host else [])
))

# Database: production uses MySQL from DB_* environment variables in base.py.

# Security: HTTPS and HSTS.
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Render-specific proxy headers.
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_TRUSTED_ORIGINS = list(set(
    [origin.strip() for origin in os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",") if origin.strip()]
    + [
        "https://mlaudit.info",
        "https://www.mlaudit.info",
        "https://*.onrender.com",
        "https://mentify-klm7.onrender.com",
    ]
    + ([f"https://{render_host}"] if render_host else [])
))

# Static files.
WHITENOISE_MAX_AGE = 31536000

# Email is configured in base.py via RESEND_API_KEY + FROM_EMAIL / DEFAULT_FROM_EMAIL.

# SameSite cookie settings.
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"
