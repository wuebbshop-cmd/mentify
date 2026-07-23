"""courses/views.py"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count

from .models import Course, Cohort, Enrollment
from accounts.decorators import role_required
from payments.models import Subscription


def course_list(request):
    """Course catalog - redirects non-learners to their role dashboards/cohorts."""
    if request.user.is_authenticated:
        if request.user.is_tutor:
            return redirect("courses:tutor_cohorts")
        elif request.user.is_guardian:
            return redirect("accounts:guardian_dashboard")
        elif request.user.is_admin:
            return redirect("accounts:admin_dashboard")

    courses = Course.objects.filter(is_active=True).annotate(
        cohort_count=Count("cohorts", distinct=True)
    )
    track = request.GET.get("track", "")
    if track:
        courses = courses.filter(track=track)
    return render(request, "courses/list.html", {"courses": courses, "selected_track": track})


def course_detail(request, slug):
    """Public course detail with active cohorts."""
    course = get_object_or_404(Course, slug=slug, is_active=True)
    cohorts = course.cohorts.filter(status="active").select_related("tutor")
    return render(request, "courses/detail.html", {"course": course, "cohorts": cohorts})


def cohort_detail(request, cohort_id):
    """Cohort detail - learners can see schedule, price, tutor."""
    cohort = get_object_or_404(
        Cohort.objects.select_related("course", "tutor"),
        id=cohort_id,
        status="active",
    )
    is_enrolled = False
    if request.user.is_authenticated and request.user.is_learner:
        is_enrolled = Enrollment.objects.filter(
            learner=request.user, cohort=cohort, status="active"
        ).exists()
    return render(request, "courses/cohort_detail.html", {
        "cohort": cohort,
        "is_enrolled": is_enrolled,
    })


@login_required
@role_required("learner")
def enroll(request, cohort_id):
    """Handle enrollment - triggers payment flow."""
    cohort = get_object_or_404(Cohort, id=cohort_id, status="active")
    existing = Enrollment.objects.filter(learner=request.user, cohort=cohort).first()

    if existing and existing.status == "active":
        messages.info(request, "You are already enrolled in this cohort.")
        return redirect("content:cohort_lessons", cohort_id=cohort.id)

    # Create enrollment as PENDING - only activated after successful payment
    enrollment, created = Enrollment.objects.get_or_create(
        learner=request.user, cohort=cohort,
        defaults={"status": "pending"}
    )
    if not created and enrollment.status != "active":
        enrollment.status = "pending"
        enrollment.save()

    # Redirect to payment
    return redirect("payments:initiate", cohort_id=cohort.id)


@login_required
@role_required("tutor", "admin")
def tutor_cohort_list(request):
    """Tutor sees their own cohorts."""
    if request.user.is_admin:
        cohorts = Cohort.objects.all().select_related("course", "tutor")
    else:
        cohorts = Cohort.objects.filter(tutor=request.user).select_related("course")
    return render(request, "courses/tutor_cohorts.html", {"cohorts": cohorts})


@login_required
@role_required("tutor", "admin")
def tutor_cohort_manage(request, cohort_id):
    """Tutor manages a specific cohort (lessons, sessions, etc.)."""
    if request.user.is_admin:
        cohort = get_object_or_404(Cohort, id=cohort_id)
    else:
        cohort = get_object_or_404(Cohort, id=cohort_id, tutor=request.user)

    from content.models import Lesson
    from live_sessions.models import LiveSession
    lessons = Lesson.objects.filter(cohort=cohort).order_by("order")
    sessions = LiveSession.objects.filter(cohort=cohort).order_by("-scheduled_at")

    return render(request, "courses/tutor_manage.html", {
        "cohort": cohort,
        "lessons": lessons,
        "sessions": sessions,
    })


@login_required
@role_required("tutor", "admin")
def cohort_learners(request, cohort_id):
    """Tutor views enrolled learners for their cohort."""
    if request.user.is_admin:
        cohort = get_object_or_404(Cohort, id=cohort_id)
    else:
        cohort = get_object_or_404(Cohort, id=cohort_id, tutor=request.user)

    enrollments = Enrollment.objects.filter(
        cohort=cohort, status="active"
    ).select_related("learner__profile").order_by("learner__last_name")

    return render(request, "courses/cohort_learners.html", {
        "cohort": cohort,
        "enrollments": enrollments,
    })
