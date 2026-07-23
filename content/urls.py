"""content/urls.py"""
from django.urls import path
from . import views

app_name = "content"

urlpatterns = [
    path("cohort/<int:cohort_id>/lessons/", views.cohort_lessons, name="cohort_lessons"),
    path("cohort/<int:cohort_id>/lesson/<int:lesson_id>/", views.lesson_detail, name="lesson_detail"),
    path("resource/<int:resource_id>/download/", views.resource_download, name="resource_download"),
    path("video/<int:video_id>/stream/", views.video_stream, name="video_stream"),
    path("cohort/<int:cohort_id>/lesson/<int:lesson_id>/submit-completion/", views.mark_lesson_submitted, name="mark_lesson_submitted"),
    # Tutor management
    path("cohort/<int:cohort_id>/verifications/", views.verify_lesson_progress, name="verify_lesson_progress"),
    path("cohort/<int:cohort_id>/lesson/new/", views.create_lesson, name="lesson_create"),
    path("cohort/<int:cohort_id>/lesson/<int:lesson_id>/edit/", views.edit_lesson, name="lesson_edit"),
]
