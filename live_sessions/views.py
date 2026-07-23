"""sessions/views.py"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from accounts.decorators import role_required
from courses.models import Cohort, Enrollment
from .models import LiveSession, Attendance
from .forms import LiveSessionForm, MakeupSessionForm


@login_required
@role_required("tutor", "admin")
def schedule_session(request, cohort_id):
    """Tutor schedules a new live session for their cohort."""
    if request.user.is_admin:
        cohort = get_object_or_404(Cohort, id=cohort_id)
    else:
        cohort = get_object_or_404(Cohort, id=cohort_id, tutor=request.user)

    form = LiveSessionForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:
                session = form.save(commit=False)
                session.cohort = cohort
                session.created_by = request.user
                session.save()
                messages.success(request, f"Session '{session.title}' scheduled for {session.scheduled_at.strftime('%d %b %Y %H:%M')}.")
                return redirect("courses:tutor_cohort_manage", cohort_id=cohort.id)
            except Exception as e:
                messages.error(request, f"Failed to schedule session: {e}")
        else:
            messages.error(request, "Please correct the session form errors below.")

    return render(request, "sessions/schedule_form.html", {"form": form, "cohort": cohort})


@login_required
@role_required("tutor", "admin")
def edit_session(request, session_id):
    """Tutor edits an existing session."""
    session = get_object_or_404(LiveSession, id=session_id)
    if not request.user.is_admin and session.cohort.tutor != request.user:
        messages.error(request, "Access denied.")
        return redirect("accounts:tutor_dashboard")

    form = LiveSessionForm(request.POST or None, instance=session)
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Session updated.")
                return redirect("courses:tutor_cohort_manage", cohort_id=session.cohort.id)
            except Exception as e:
                messages.error(request, f"Failed to update session: {e}")
        else:
            messages.error(request, "Please correct the form details.")

    return render(request, "sessions/schedule_form.html", {
        "form": form, "cohort": session.cohort, "session": session
    })


@login_required
@role_required("tutor", "admin")
def mark_attendance(request, session_id):
    """
    Tutor marks attendance for all enrolled learners in this session.
    Displays all enrolled learners with attendance status dropdowns.
    """
    session = get_object_or_404(LiveSession, id=session_id)
    if not request.user.is_admin and session.cohort.tutor != request.user:
        messages.error(request, "Access denied.")
        return redirect("accounts:tutor_dashboard")

    enrollments = Enrollment.objects.filter(
        cohort=session.cohort, status="active"
    ).select_related("learner")

    if request.method == "POST":
        for enrollment in enrollments:
            learner = enrollment.learner
            status = request.POST.get(f"attendance_{learner.id}", Attendance.AttendanceStatus.MISSED)
            Attendance.objects.update_or_create(
                session=session,
                learner=learner,
                defaults={
                    "status": status,
                    "marked_by": request.user,
                    "notes": request.POST.get(f"notes_{learner.id}", ""),
                },
            )
        messages.success(request, "Attendance saved successfully.")
        return redirect("courses:tutor_cohort_manage", cohort_id=session.cohort.id)

    # Load existing attendance records
    existing = {
        a.learner_id: a
        for a in Attendance.objects.filter(session=session)
    }

    learner_attendance = [
        (e.learner, existing.get(e.learner_id))
        for e in enrollments
    ]

    return render(request, "sessions/mark_attendance.html", {
        "session": session,
        "learner_attendance": learner_attendance,
        "status_choices": Attendance.AttendanceStatus.choices,
    })


@login_required
@role_required("tutor", "admin")
def schedule_makeup(request, session_id):
    """Schedule a makeup session for learners who missed an original session."""
    original = get_object_or_404(LiveSession, id=session_id)
    if not request.user.is_admin and original.cohort.tutor != request.user:
        messages.error(request, "Access denied.")
        return redirect("accounts:tutor_dashboard")

    form = MakeupSessionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        makeup = form.save(commit=False)
        makeup.cohort = original.cohort
        makeup.is_makeup = True
        makeup.original_session = original
        makeup.created_by = request.user
        makeup.save()
        messages.success(request, f"Makeup session '{makeup.title}' scheduled.")
        return redirect("courses:tutor_cohort_manage", cohort_id=original.cohort.id)

    return render(request, "sessions/makeup_form.html", {
        "form": form,
        "original_session": original,
    })


@login_required
@role_required("tutor", "admin")
def cancel_session(request, session_id):
    """Cancel a session."""
    session = get_object_or_404(LiveSession, id=session_id)
    if not request.user.is_admin and session.cohort.tutor != request.user:
        messages.error(request, "Access denied.")
        return redirect("accounts:tutor_dashboard")
    if request.method == "POST":
        session.is_cancelled = True
        session.save()
        messages.success(request, f"Session '{session.title}' cancelled.")
    return redirect("courses:tutor_cohort_manage", cohort_id=session.cohort.id)


@login_required
@role_required("learner")
def learner_sessions(request, cohort_id):
    """Learner views all sessions for an enrolled cohort."""
    from courses.models import Enrollment
    enrollment = get_object_or_404(Enrollment, learner=request.user, cohort_id=cohort_id, status="active")
    cohort = enrollment.cohort

    now = timezone.now()
    upcoming = LiveSession.objects.filter(
        cohort=cohort, scheduled_at__gte=now, is_cancelled=False
    ).order_by("scheduled_at")
    past = LiveSession.objects.filter(
        cohort=cohort, scheduled_at__lt=now, is_cancelled=False
    ).order_by("-scheduled_at")[:10]

    # This learner's attendance records
    my_attendance = {
        a.session_id: a
        for a in Attendance.objects.filter(learner=request.user, session__cohort=cohort)
    }

    # Bundle past sessions with attendance for easy rendering
    past_with_attendance = [
        (session, my_attendance.get(session.id))
        for session in past
    ]

    return render(request, "sessions/learner_sessions.html", {
        "cohort": cohort,
        "upcoming": upcoming,
        "past_with_attendance": past_with_attendance,
    })
