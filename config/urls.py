"""
Mentify Platform - Root URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as static_serve
from django.contrib.staticfiles import finders
from django.http import FileResponse, Http404
from accounts.sitemap_views import sitemap, robots_txt, llms_txt
from services.cdn_views import assets_proxy, github_asset_proxy
from services.cloudflare_views import cloudflare_asset_proxy
from services.chat_views import chatbot_api_view
from accounts.views import contact_page, privacy_policy, terms_of_service, cookie_policy
from prep.internal_views import internal_ingest_document_api, internal_worker_health_api
import os

def health_check(request):
    """Minimal health check for Render and uptime monitoring."""
    from django.http import HttpResponse

    try:
        from django.db import connection

        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
    except Exception:
        return HttpResponse("unhealthy", status=503, content_type="text/plain")

    return HttpResponse("ok", content_type="text/plain")


def static_fallback_serve(request, path):
    """Serve collected static files, then fall back to app static finders."""
    try:
        return static_serve(
            request,
            path,
            document_root=settings.STATIC_ROOT or (settings.BASE_DIR / "static"),
        )
    except Http404:
        found = finders.find(path)
        if found and os.path.isfile(found):
            return FileResponse(open(found, "rb"))
        raise


def media_fallback_serve(request, path):
    """
    Serve media files from Cloudflare R2 if configured, local disk, or GitHub storage proxy.
    """
    clean_path = str(path or "").lstrip("/")

    # 1. Check Cloudflare R2
    try:
        from services.cloudflare_storage import is_cloudflare_r2_configured
        if is_cloudflare_r2_configured():
            try:
                return cloudflare_asset_proxy(request, clean_path)
            except Http404:
                pass
    except Exception:
        pass

    # 2. Check local MEDIA_ROOT
    try:
        return static_serve(
            request,
            path,
            document_root=settings.MEDIA_ROOT,
        )
    except Http404:
        pass

    # 3. Fallback to GitHub for legacy assets
    candidates = [
        clean_path,
        f"mentify-uploads/{clean_path}".replace("mentify-uploads/mentify-uploads/", "mentify-uploads/"),
    ]
    for candidate in candidates:
        try:
            resp = assets_proxy(request, candidate)
            if resp and resp.status_code == 200:
                try:
                    local_dest = settings.MEDIA_ROOT / candidate
                    local_dest.parent.mkdir(parents=True, exist_ok=True)
                    if not local_dest.exists() and hasattr(resp, "content"):
                        with open(local_dest, "wb") as f:
                            f.write(resp.content)
                except Exception:
                    pass
                return resp
        except Exception:
            continue

    raise Http404(f"Media file '{path}' not found in Cloudflare R2, locally, or on GitHub.")


def favicon(request):
    """Serve a real favicon.ico response for browsers that bypass page metadata."""
    return FileResponse(
        open(settings.BASE_DIR / "static" / "favicon.ico", "rb"),
        content_type="image/x-icon",
    )

urlpatterns = [
    # Health check for uptime monitoring & diagnostics
    path("health/", health_check, name="health_check"),

    # Dedicated Background Worker Web Service Endpoints (Option B)
    path(
        "api/internal/ingest-document/",
        internal_ingest_document_api,
        name="internal_ingest_document",
    ),
    path(
        "api/internal/health/",
        internal_worker_health_api,
        name="internal_worker_health",
    ),

    # Mentify AI Customer Service Chatbot API
    path("api/chat/", chatbot_api_view, name="chatbot_api"),

    # Browser tab icon fallback. Most pages also declare the favicon in base.html.
    path("favicon.ico", favicon, name="favicon"),

    # Django admin (platform owner only)
    path("admin/", admin.site.urls),

    # SEO: Sitemap for Google Search Console
    path("sitemap.xml", sitemap, name="sitemap"),
    
    # SEO: robots.txt for crawler directives
    path("robots.txt", robots_txt, name="robots"),
    
    # GEO (Generative Engine Optimization): llms.txt for AI Search Engines (ChatGPT, Perplexity, Gemini, Claude)
    path("llms.txt", llms_txt, name="llms_txt"),
    
    # SEO: Google Search Console verification
    path('google20c3024f708d9e69.html', lambda request: static_serve(request, 'google20c3024f708d9e69.html', document_root=settings.BASE_DIR)),

    # Cloudflare R2 asset proxy (uploaded PDFs, visual crops, notes PDFs)
    path(
        "cdn/cloudflare/<path:filepath>",
        cloudflare_asset_proxy,
        name="cloudflare_asset_proxy",
    ),

    # GitHub asset proxy (course banners, avatars, etc.)
    path(
        "cdn/assets/<path:filepath>",
        assets_proxy,
        name="assets_proxy",
    ),
    path(
        "cdn/github/<str:owner>/<str:repo>/<str:ref>/<path:filepath>",
        github_asset_proxy,
        name="github_asset_proxy",
    ),

    # Direct vanity and policy endpoints
    path("contact/", contact_page, name="contact"),
    path("terms/", terms_of_service, name="terms"),
    path("terms-of-service/", terms_of_service, name="terms_of_service"),
    path("privacy/", privacy_policy, name="privacy"),
    path("privacy-policy/", privacy_policy, name="privacy_policy"),
    path("cookies/", cookie_policy, name="cookie_policy"),

    # Auth + accounts
    path("accounts/", include("accounts.urls")),

    # Courses (browsing / enrollment)
    path("courses/", include("courses.urls")),

    # Content (lessons / resources)
    path("content/", include("content.urls")),

    # Assignments
    path("assignments/", include("assignments.urls")),

    # Live sessions
    path("sessions/", include("live_sessions.urls")),

    # Payments
    path("payments/", include("payments.urls")),

    # Blog & Content Hub
    path("blog/", include("blog.urls")),

    # Mentify Prep Engine
    path("prep/", include("prep.urls")),

    # Root redirect
    path("", include("accounts.home_urls")),
]

# Custom Error Handlers
handler404 = "accounts.views.custom_404"
handler500 = "accounts.views.custom_500"
handler403 = "accounts.views.custom_403"
handler400 = "accounts.views.custom_400"

from django.urls import re_path

# Fallback serving of static and media files (ensures assets are always served)
urlpatterns += [
    re_path(
        r"^static/(?P<path>.*)$",
        static_fallback_serve,
    ),
    re_path(
        r"^media/(?P<path>.*)$",
        media_fallback_serve,
    ),
]
