"""courses/urls.py"""
from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.course_list, name="list"),
    # Static paths must come BEFORE <slug:slug>/ so slug doesn't catch them
    path("manage/", views.tutor_cohort_list, name="tutor_cohorts"),
    path("manage/cohort/<int:cohort_id>/", views.tutor_cohort_manage, name="tutor_cohort_manage"),
    path("manage/cohort/<int:cohort_id>/learners/", views.cohort_learners, name="cohort_learners"),
    path("cohort/<int:cohort_id>/", views.cohort_detail, name="cohort_detail"),
    path("cohort/<int:cohort_id>/enroll/", views.enroll, name="enroll"),
    path("<slug:slug>/", views.course_detail, name="detail"),
]
