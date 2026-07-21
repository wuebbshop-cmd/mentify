"""accounts/home_urls.py — Root URL patterns (home page, dashboard redirect)."""
from django.urls import path
from .views import home, dashboard_redirect

urlpatterns = [
    path("", home, name="home"),
    path("dashboard/", dashboard_redirect, name="dashboard"),
]
