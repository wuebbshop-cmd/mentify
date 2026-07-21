"""accounts/urls.py"""
from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views

app_name = "accounts"

urlpatterns = [
    # Auth
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.role_select, name="register"),
    path("register/learner/", views.register_learner, name="register_learner"),
    path("register/guardian/", views.register_guardian, name="register_guardian"),
    path("register/tutor/", views.register_tutor, name="register_tutor"),
    path("google/", views.google_login, name="google_login"),
    path("google/callback/", views.google_callback, name="google_callback"),

    # Password reset (Django built-in views, custom templates)
    path("password-reset/", PasswordResetView.as_view(
        template_name="accounts/password_reset.html",
        email_template_name="accounts/emails/password_reset_email.html",
        subject_template_name="accounts/emails/password_reset_subject.txt",
        success_url="/accounts/password-reset/done/",
    ), name="password_reset"),
    path("password-reset/done/", PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html"
    ), name="password_reset_done"),
    path("password-reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(
        template_name="accounts/password_reset_confirm.html",
        success_url="/accounts/password-reset/complete/",
    ), name="password_reset_confirm"),
    path("password-reset/complete/", PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset_complete.html"
    ), name="password_reset_complete"),

    # Dashboards
    path("dashboard/", views.dashboard_redirect, name="dashboard"),
    path("dashboard/learner/", views.learner_dashboard, name="learner_dashboard"),
    path("dashboard/tutor/", views.tutor_dashboard, name="tutor_dashboard"),
    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/admin/reports/", views.admin_reports, name="admin_reports"),
    path("dashboard/admin/guardian-requests/", views.admin_guardian_requests, name="admin_guardian_requests"),
    path("dashboard/guardian/", views.guardian_dashboard, name="guardian_dashboard"),
    path("dashboard/guardian/link/", views.guardian_link_request, name="guardian_link_request"),
    path("dashboard/guardian/link/confirm/<uuid:token>/", views.guardian_link_confirm, name="guardian_link_confirm"),

    # Profile
    path("profile/", views.profile_view, name="profile"),
]
