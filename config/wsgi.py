"""WSGI config for Mentify Platform."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
application = get_wsgi_application()

try:
    from whitenoise import WhiteNoise
    from django.conf import settings
    
    static_root = str(settings.STATIC_ROOT) if getattr(settings, "STATIC_ROOT", None) else str(settings.BASE_DIR / "staticfiles")
    application = WhiteNoise(application, root=static_root, prefix="/static/")
    
    raw_static = str(settings.BASE_DIR / "static")
    if os.path.isdir(raw_static):
        application.add_files(raw_static, prefix="/static/")
except Exception:
    pass

