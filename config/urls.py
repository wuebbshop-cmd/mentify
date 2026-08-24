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
from accounts.sitemap_views import sitemap, robots_txt
from services.cdn_views import assets_proxy, github_asset_proxy
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


def favicon(request):
    """Serve a real favicon.ico response for browsers that bypass page metadata."""
    return FileResponse(
        open(settings.BASE_DIR / "static" / "favicon.ico", "rb"),
        content_type="image/x-icon",
    )

urlpatterns = [
    # Health check for uptime monitoring & diagnostics
    path("health/", health_check, name="health_check"),

    # Browser tab icon fallback. Most pages also declare the favicon in base.html.
    path("favicon.ico", favicon, name="favicon"),

    # Django admin (platform owner only)
    path("admin/", admin.site.urls),

    # SEO: Sitemap for Google Search Console
    path("sitemap.xml", sitemap, name="sitemap"),
    
    # SEO: robots.txt for crawler directives
    path("robots.txt", robots_txt, name="robots"),
    
    # SEO: Google Search Console verification
    path('google20c3024f708d9e69.html', lambda request: static_serve(request, 'google20c3024f708d9e69.html', document_root=settings.BASE_DIR)),

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
        static_serve,
        {"document_root": settings.MEDIA_ROOT},
    ),
]
