"""
Mentify Platform - Root URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as static_serve
from accounts.sitemap_views import sitemap, robots_txt
import os

urlpatterns = [
    # Django admin (platform owner only)
    path("admin/", admin.site.urls),

    # SEO: Sitemap for Google Search Console
    path("sitemap.xml", sitemap, name="sitemap"),
    
    # SEO: robots.txt for crawler directives
    path("robots.txt", robots_txt, name="robots"),
    
    # SEO: Google Search Console verification
    path('google20c3024f708d9e69.html', lambda request: static_serve(request, 'google20c3024f708d9e69.html', document_root=settings.BASE_DIR)),

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
