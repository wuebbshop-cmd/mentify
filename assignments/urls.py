"""assignments/urls.py"""
from django.urls import path
from . import views

app_name = "assignments"

urlpatterns = [
    # Learner
    path("<int:assignment_id>/", views.assignment_detail, name="detail"),
    path("<int:assignment_id>/submit/", views.submit_assignment, name="submit"),
    path("<int:assignment_id>/my-grade/", views.learner_grade_view, name="my_grade"),
    # Tutor
    path("lesson/<int:lesson_id>/create/", views.create_assignment, name="create"),
    path("<int:assignment_id>/submissions/", views.assignment_submissions, name="submissions"),
    path("submission/<int:submission_id>/grade/", views.grade_submission, name="grade"),
]
