"""Production settings - DEBUG off, HTTPS enforced, Render-ready."""

from .base import *  # noqa: F401, F403
import os
import dj_database_url

DEBUG = False

# ─── Allowed Hosts ──────────────────────────────────────────────────────────
# Allow custom domains, Render domains, and dynamic RENDER_EXTERNAL_HOSTNAME
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

# ─── Database: Render uses PostgreSQL (via DATABASE_URL) ────────────────────
database_url = os.environ.get("DATABASE_URL")
if database_url:
    db_config = dj_database_url.parse(
        database_url,
        conn_max_age=600,
        conn_health_checks=True,
    )
    if "postgresql" in db_config.get("ENGINE", ""):
        invalid_pg_options = {"charset", "init_command"}
        for key in invalid_pg_options:
            db_config.pop(key, None)
        db_config["OPTIONS"] = {
            key: value
            for key, value in db_config.get("OPTIONS", {}).items()
            if key not in invalid_pg_options
        }
    DATABASES = {"default": db_config}

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

# ─── Static files: Render uses persistent storage only for /render/output/ ───
# WhiteNoise in middleware + compression via STATICFILES_STORAGE handle this
# Collect static files before deploy via render.yaml build command
WHITENOISE_MAX_AGE = 31536000

# ─── Email: Resend.com (Render-friendly, no SMTP ports required) ───────────
# Configured in base.py via RESEND_API_KEY + FROM_EMAIL / DEFAULT_FROM_EMAIL

# ─── Security: SameSite cookie setting ─────────────────────────────────────
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"
