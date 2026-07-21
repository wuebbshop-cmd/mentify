"""sessions/urls.py"""
from django.urls import path
from . import views

app_name = "sessions"

urlpatterns = [
    # Tutor: manage sessions
    path("cohort/<int:cohort_id>/schedule/", views.schedule_session, name="schedule"),
    path("<int:session_id>/edit/", views.edit_session, name="edit"),
    path("<int:session_id>/attendance/", views.mark_attendance, name="attendance"),
    path("<int:session_id>/makeup/", views.schedule_makeup, name="schedule_makeup"),
    path("<int:session_id>/cancel/", views.cancel_session, name="cancel"),
    # Learner: view sessions
    path("cohort/<int:cohort_id>/", views.learner_sessions, name="learner_sessions"),
]
