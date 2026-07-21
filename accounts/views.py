"""accounts/views.py — Auth + dashboard views."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models import Q

from .forms import (
    LearnerRegistrationForm,
    MentifyLoginForm,
    ProfileUpdateForm,
    UserUpdateForm,
    GuardianChildLinkForm,
)
from .models import User, Profile, Guardian, GuardianLinkRequest, GuardianLinkRequestLog
from .decorators import role_required


# ─── Admin Email Promotion ────────────────────────────────────────────────────
def promote_if_admin_email(user):
    """
    If the user’s email is in settings.ADMIN_EMAILS, ensure they have
    admin role, is_superuser, and is_staff. Saves only if changed.
    """
    admin_emails = [e.strip().lower() for e in getattr(settings, "ADMIN_EMAILS", [])]
    if not admin_emails or user.email.lower() not in admin_emails:
        return
    changed = False
    if not user.is_superuser:
        user.is_superuser = True
        changed = True
    if not user.is_staff:
        user.is_staff = True
        changed = True
    if getattr(user, "role", None) != "admin":
        user.role = "admin"
        changed = True
    if changed:
        user.save(update_fields=["is_superuser", "is_staff", "role"])


# ─── Public Pages ─────────────────────────────────────────────────────────────

def home(request):
    """Public landing page."""
    if request.user.is_authenticated:
        return redirect(request.user.get_dashboard_url())
    return render(request, "home.html")


def role_select(request):
    """Landing page where user picks their role before registering."""
    if request.user.is_authenticated:
        return redirect(request.user.get_dashboard_url())
    return render(request, "accounts/role_select.html")


def register_learner(request):
    """Learner self-registration."""
    if request.user.is_authenticated:
        return redirect(request.user.get_dashboard_url())

    if request.method == "POST":
        form = LearnerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "learner"
            user.save()
            Profile.objects.get_or_create(user=user)
            promote_if_admin_email(user)
            login(request, user)
            messages.success(request, f"Welcome to Mentify, {user.first_name}!")
            return redirect(user.get_dashboard_url())
    else:
        form = LearnerRegistrationForm()

    return render(request, "accounts/register_learner.html", {"form": form})


def register_guardian(request):
    """Guardian self-registration."""
    if request.user.is_authenticated:
        return redirect(request.user.get_dashboard_url())
    if request.method == "POST":
        form = LearnerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "guardian"
            user.save()
            Profile.objects.get_or_create(user=user)
            promote_if_admin_email(user)
            login(request, user)
            messages.success(request, f"Welcome to Mentify, {user.first_name}!")
            return redirect(user.get_dashboard_url())
    else:
        form = LearnerRegistrationForm()
    return render(request, "accounts/register_guardian.html", {"form": form})


def register_tutor(request):
    """Tutor self-registration."""
    if request.user.is_authenticated:
        return redirect(request.user.get_dashboard_url())
    if request.method == "POST":
        form = LearnerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "tutor"
            user.save()
            Profile.objects.get_or_create(user=user)
            promote_if_admin_email(user)
            login(request, user)
            messages.success(request, f"Welcome to Mentify, {user.first_name}!")
            return redirect(user.get_dashboard_url())
    else:
        form = LearnerRegistrationForm()
    return render(request, "accounts/register_tutor.html", {"form": form})


@login_required
@role_required("guardian")
def guardian_link_request(request):
    """Guardian self-service request to link to their learner's account."""
    if request.method == "POST":
        form = GuardianChildLinkForm(request.POST)
        if form.is_valid():
            learner = form.cleaned_data["email_or_username"]
            guardian = request.user
            notes = form.cleaned_data.get("notes", "")
            request_obj = GuardianLinkRequest.objects.filter(
                guardian=guardian,
                learner=learner,
            ).first()
            if request_obj:
                if request_obj.status == GuardianLinkRequest.Status.PENDING:
                    messages.info(request, "A pending request already exists for this learner.")
                    return redirect("accounts:guardian_dashboard")
                if request_obj.status == GuardianLinkRequest.Status.ACCEPTED:
                    messages.info(request, "This learner is already linked to your account.")
                    return redirect("accounts:guardian_dashboard")
                request_obj.status = GuardianLinkRequest.Status.PENDING
                request_obj.notes = notes or request_obj.notes
                request_obj.responded_at = None
                request_obj.save()
            else:
                request_obj = GuardianLinkRequest.objects.create(
                    guardian=guardian,
                    learner=learner,
                    notes=notes,
                )
            GuardianLinkRequestLog.objects.create(
                request=request_obj,
                event=GuardianLinkRequestLog.Event.REQUESTED,
                actor=guardian,
                message="Guardian requested link to learner account.",
            )
            confirm_url = request.build_absolute_uri(reverse("accounts:guardian_link_confirm", args=[request_obj.token]))
            subject = f"Guardian link request from {guardian.get_full_name()}"
            message_body = render_to_string("accounts/emails/guardian_link_request.txt", {
                "learner": learner,
                "guardian": guardian,
                "link_url": confirm_url,
                "PLATFORM_NAME": getattr(settings, "PLATFORM_NAME", "Mentify"),
            })
            send_mail(
                subject,
                message_body,
                settings.DEFAULT_FROM_EMAIL,
                [learner.email],
                fail_silently=True,
            )
            messages.success(request, "Your request has been sent. The learner will be notified by email.")
            return redirect("accounts:guardian_dashboard")
    else:
        form = GuardianChildLinkForm()

    pending_requests = GuardianLinkRequest.objects.filter(
        guardian=request.user
    ).select_related("learner").order_by("-created_at")

    return render(request, "accounts/guardian_link_request.html", {
        "form": form,
        "pending_requests": pending_requests,
    })


@login_required
@role_required("learner")
def guardian_link_confirm(request, token):
    """Learner confirms or rejects a guardian link request and notifies the guardian by email."""
    from django.utils import timezone

    request_obj = get_object_or_404(GuardianLinkRequest, token=token)
    if request.user != request_obj.learner:
        return HttpResponseForbidden("You are not authorized to confirm this link.")

    if request.method == "POST":
        action = request.POST.get("action")
        learner = request_obj.learner
        guardian = request_obj.guardian
        if action == "accept":
            request_obj.status = GuardianLinkRequest.Status.ACCEPTED
            request_obj.responded_at = timezone.now()
            request_obj.save()
            guardian_profile, _ = Guardian.objects.get_or_create(user=guardian)
            guardian_profile.learners.add(learner)
            GuardianLinkRequestLog.objects.create(
                request=request_obj,
                event=GuardianLinkRequestLog.Event.ACCEPTED,
                actor=request.user,
                message="Learner accepted guardian link request.",
            )
            # notify guardian
            subject = f"{learner.get_full_name()} accepted your guardian request"
            message_body = render_to_string("accounts/emails/guardian_link_accepted.txt", {
                "learner": learner,
                "guardian": guardian,
                "PLATFORM_NAME": getattr(settings, "PLATFORM_NAME", "Mentify"),
            })
            send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [guardian.email], fail_silently=True)

            messages.success(request, "Link accepted. Your guardian can now see your progress.")
        else:
            request_obj.status = GuardianLinkRequest.Status.REJECTED
            request_obj.responded_at = timezone.now()
            request_obj.save()
            GuardianLinkRequestLog.objects.create(
                request=request_obj,
                event=GuardianLinkRequestLog.Event.REJECTED,
                actor=request.user,
                message="Learner rejected guardian link request.",
            )
            # notify guardian
            subject = f"{learner.get_full_name()} declined your guardian request"
            message_body = render_to_string("accounts/emails/guardian_link_rejected.txt", {
                "learner": learner,
                "guardian": guardian,
                "PLATFORM_NAME": getattr(settings, "PLATFORM_NAME", "Mentify"),
            })
            send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [guardian.email], fail_silently=True)

            messages.info(request, "Link rejected. Your guardian will not be able to see your progress.")
        return redirect(request.user.get_dashboard_url())

    return render(request, "accounts/guardian_link_confirm.html", {"request_obj": request_obj})


def login_view(request):
    """Custom login using email."""
    if request.user.is_authenticated:
        return redirect(request.user.get_dashboard_url())

    if request.method == "POST":
        form = MentifyLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            promote_if_admin_email(user)  # auto-promote whitelisted admins
            login(request, user)
            next_url = request.GET.get("next") or user.get_dashboard_url()
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect(next_url)
        else:
            messages.error(request, "Invalid email or password. Please try again.")
    else:
        form = MentifyLoginForm(request)

    return render(request, "accounts/login.html", {"form": form})


@require_POST
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You've been signed out. See you soon!")
    return redirect("home")


# ─── Dashboards ───────────────────────────────────────────────────────────────

@login_required
def dashboard_redirect(request):
    """Smart redirect to the user's appropriate dashboard."""
    return redirect(request.user.get_dashboard_url())


@login_required
@role_required("learner")
def learner_dashboard(request):
    """Learner home: enrolled cohorts, upcoming sessions, subscription status + progress rollups."""
    from courses.models import Enrollment
    from live_sessions.models import LiveSession
    from payments.models import Subscription
    from content.models import Lesson, LessonProgress
    from assignments.models import Assignment, Submission
    from live_sessions.models import Attendance

    enrollments = (
        Enrollment.objects.filter(learner=request.user, status="active")
        .select_related("cohort__course", "cohort__tutor")
        .order_by("cohort__start_date")
    )

    # Active subscriptions
    active_subs = Subscription.objects.filter(
        learner=request.user,
        status="active"
    ).select_related("cohort")

    # Upcoming sessions for enrolled cohorts
    from django.utils import timezone
    cohort_ids = list(enrollments.values_list("cohort_id", flat=True))
    upcoming_sessions = (
        LiveSession.objects.filter(
            cohort_id__in=cohort_ids,
            scheduled_at__gte=timezone.now(),
            is_cancelled=False,
        )
        .select_related("cohort__course")
        .order_by("scheduled_at")[:5]
    )

    # ── Per-cohort progress rollups ──────────────────────────────
    cohort_progress = []
    for enrollment in enrollments:
        cohort = enrollment.cohort

        # 1. Lesson completion %
        total_lessons = Lesson.objects.filter(cohort=cohort, is_published=True).count()
        done_lessons = LessonProgress.objects.filter(
            learner=request.user, lesson__cohort=cohort, completed=True
        ).count()
        lessons_pct = round((done_lessons / total_lessons) * 100) if total_lessons else 0

        # 2. Assignment submission rate %
        total_assignments = Assignment.objects.filter(
            lesson__cohort=cohort, is_published=True
        ).count()
        submitted_assignments = Submission.objects.filter(
            learner=request.user,
            assignment__lesson__cohort=cohort,
            status__in=[Submission.Status.SUBMITTED, Submission.Status.GRADED],
        ).count()
        assignments_pct = round((submitted_assignments / total_assignments) * 100) if total_assignments else 0

        # 3. Attendance rate %
        total_sessions = LiveSession.objects.filter(
            cohort=cohort, scheduled_at__lt=timezone.now(), is_cancelled=False
        ).count()
        attended_count = Attendance.objects.filter(
            session__cohort=cohort, learner=request.user, status=Attendance.Status.ATTENDED
        ).count()
        attendance_pct = round((attended_count / total_sessions) * 100) if total_sessions else None

        cohort_progress.append({
            "enrollment": enrollment,
            "lessons_pct": lessons_pct,
            "done_lessons": done_lessons,
            "total_lessons": total_lessons,
            "assignments_pct": assignments_pct,
            "submitted_assignments": submitted_assignments,
            "total_assignments": total_assignments,
            "attendance_pct": attendance_pct,
            "attended_count": attended_count,
            "total_sessions": total_sessions,
        })

    graded_submissions_queryset = Submission.objects.filter(
        learner=request.user,
        status=Submission.Status.GRADED,
    ).select_related("assignment__lesson__cohort__course", "grade")

    graded_count = graded_submissions_queryset.count()
    average_grade_pct = None
    if graded_count:
        total_grade_pct = sum(
            s.grade.percentage for s in graded_submissions_queryset if getattr(s, "grade", None)
        )
        average_grade_pct = round(total_grade_pct / graded_count, 1)

    recent_graded_submissions = graded_submissions_queryset.order_by("-submitted_at")[:5]

    context = {
        "enrollments": enrollments,
        "active_subs": active_subs,
        "upcoming_sessions": upcoming_sessions,
        "cohort_progress": cohort_progress,
        "graded_count": graded_count,
        "average_grade_pct": average_grade_pct,
        "recent_graded_submissions": recent_graded_submissions,
    }
    return render(request, "accounts/learner_dashboard.html", context)


@login_required
@role_required("tutor", "admin")
def tutor_dashboard(request):
    """Tutor home: their cohorts, pending grading, upcoming sessions."""
    from courses.models import Cohort
    from live_sessions.models import LiveSession
    from assignments.models import Submission

    if request.user.is_admin:
        cohorts = Cohort.objects.filter(status="active").select_related("course", "tutor")
    else:
        cohorts = Cohort.objects.filter(tutor=request.user, status="active").select_related("course")

    from django.utils import timezone
    cohort_ids = cohorts.values_list("id", flat=True)

    upcoming_sessions = (
        LiveSession.objects.filter(
            cohort_id__in=cohort_ids,
            scheduled_at__gte=timezone.now(),
            is_cancelled=False,
        )
        .select_related("cohort__course")
        .order_by("scheduled_at")[:5]
    )

    pending_submissions = Submission.objects.filter(
        assignment__lesson__cohort_id__in=cohort_ids,
        status="submitted",
    ).select_related("learner", "assignment").count()

    context = {
        "cohorts": cohorts,
        "upcoming_sessions": upcoming_sessions,
        "pending_submissions_count": pending_submissions,
    }
    return render(request, "accounts/tutor_dashboard.html", context)


@login_required
@role_required("admin")
def admin_dashboard(request):
    """Admin overview: platform-wide stats and detailed cohort reporting."""
    from courses.models import Course, Cohort, Enrollment
    from payments.models import Subscription, Payment
    from live_sessions.models import LiveSession, Attendance
    from django.utils import timezone
    from django.db.models import Count, Sum, Q

    total_learners = User.objects.filter(role=User.Role.LEARNER).count()
    total_tutors = User.objects.filter(role=User.Role.TUTOR).count()
    active_cohorts = Cohort.objects.filter(status="active").count()
    active_subscriptions = Subscription.objects.filter(
        status="active", paid_until__gte=timezone.now().date()
    ).count()

    # Revenue this month
    from datetime import date
    today = date.today()
    monthly_revenue = Payment.objects.filter(
        status=Payment.Status.SUCCESS,
        paid_at__year=today.year,
        paid_at__month=today.month,
    ).aggregate(total=Sum("amount_kes"))["total"] or 0

    recent_payments = (
        Payment.objects.filter(status=Payment.Status.SUCCESS)
        .select_related("subscription__learner", "subscription__cohort__course", "recorded_by")
        .order_by("-paid_at")[:10]
    )

    revenue_by_cohort = (
        Cohort.objects.filter(status="active")
        .select_related("course", "tutor")
        .annotate(
            total_revenue=Sum(
                "subscriptions__payments__amount_kes",
                filter=Q(subscriptions__payments__status=Payment.Status.SUCCESS),
            ),
            active_learners=Count(
                "enrollments__learner",
                filter=Q(enrollments__status=Enrollment.Status.ACTIVE),
                distinct=True,
            ),
        )
        .order_by("-total_revenue")
    )

    attendance_sessions = (
        LiveSession.objects.filter(
            scheduled_at__lt=timezone.now(),
            is_cancelled=False,
        )
        .select_related("cohort__course")
        .annotate(
            attended_count=Count("attendances", filter=Q(attendances__status=Attendance.Status.ATTENDED)),
            missed_count=Count("attendances", filter=Q(attendances__status=Attendance.Status.MISSED)),
            excused_count=Count("attendances", filter=Q(attendances__status=Attendance.Status.EXCUSED)),
            total_marked=Count("attendances"),
        )
        .order_by("-scheduled_at")[:30]
    )

    attendance_trends = []
    for session in attendance_sessions:
        if session.total_marked:
            attendance_rate = round((session.attended_count / session.total_marked) * 100)
        else:
            attendance_rate = None
        attendance_trends.append({
            "session": session,
            "attendance_rate": attendance_rate,
        })

    context = {
        "total_learners": total_learners,
        "total_tutors": total_tutors,
        "active_cohorts": active_cohorts,
        "active_subscriptions": active_subscriptions,
        "monthly_revenue": monthly_revenue,
        "recent_payments": recent_payments,
        "revenue_by_cohort": revenue_by_cohort,
        "attendance_trends": attendance_trends,
    }
    return render(request, "accounts/admin_dashboard.html", context)


@login_required
@role_required("admin")
def admin_reports(request):
    """Admin: revenue by cohort + attendance trends."""
    from courses.models import Cohort
    from payments.models import Payment
    from live_sessions.models import LiveSession, Attendance
    from django.db.models import Sum, Count, Q
    from django.utils import timezone
    from datetime import date

    # ── Revenue by cohort (all time) ─────────────────────────────
    revenue_by_cohort = (
        Cohort.objects.filter(status="active")
        .select_related("course")
        .annotate(
            total_revenue=Sum(
                "subscriptions__payments__amount_kes",
                filter=Q(subscriptions__payments__status="success"),
            ),
            learner_count=Count(
                "enrollments__learner",
                filter=Q(enrollments__status="active"),
                distinct=True,
            ),
        )
        .order_by("-total_revenue")
    )

    # ── Last 30 days month-over-month revenue ────────────────────
    today = date.today()
    monthly_breakdown = []
    for month_offset in range(5, -1, -1):  # last 6 months oldest→newest
        from dateutil.relativedelta import relativedelta
        target = today - relativedelta(months=month_offset)
        rev = Payment.objects.filter(
            status="success",
            paid_at__year=target.year,
            paid_at__month=target.month,
        ).aggregate(total=Sum("amount_kes"))["total"] or 0
        monthly_breakdown.append({
            "label": target.strftime("%b %Y"),
            "revenue": float(rev),
        })

    # ── Attendance summary: last 30 past sessions ────────────────
    past_sessions = (
        LiveSession.objects.filter(
            scheduled_at__lt=timezone.now(),
            is_cancelled=False,
        )
        .select_related("cohort__course")
        .annotate(
            attended_count=Count("attendances", filter=Q(attendances__status=Attendance.Status.ATTENDED)),
            missed_count=Count("attendances", filter=Q(attendances__status=Attendance.Status.MISSED)),
            excused_count=Count("attendances", filter=Q(attendances__status=Attendance.Status.EXCUSED)),
            total_marked=Count("attendances"),
        )
        .order_by("-scheduled_at")[:30]
    )

    context = {
        "revenue_by_cohort": revenue_by_cohort,
        "monthly_breakdown": monthly_breakdown,
        "past_sessions": past_sessions,
    }
    return render(request, "accounts/admin_reports.html", context)


@login_required
@role_required("admin")
def admin_guardian_requests(request):
    """Admin review page for guardian link requests."""
    from django.utils import timezone
    if request.method == "POST":
        action = request.POST.get("action", "")
        if ":" in action:
            verb, pk = action.split(":", 1)
            try:
                req = GuardianLinkRequest.objects.get(pk=int(pk))
            except GuardianLinkRequest.DoesNotExist:
                messages.error(request, "Request not found.")
                return redirect("accounts:admin_guardian_requests")

            if verb == "accept" and req.status == GuardianLinkRequest.Status.PENDING:
                req.status = GuardianLinkRequest.Status.ACCEPTED
                req.responded_at = timezone.now()
                req.save()
                guardian_profile, _ = Guardian.objects.get_or_create(user=req.guardian)
                guardian_profile.learners.add(req.learner)
                GuardianLinkRequestLog.objects.create(
                    request=req,
                    event=GuardianLinkRequestLog.Event.ACCEPTED,
                    actor=request.user,
                    message="Admin accepted guardian link request.",
                )
                # notify guardian
                subject = f"{req.learner.get_full_name()} linked to your account"
                message_body = render_to_string("accounts/emails/guardian_link_accepted.txt", {
                    "learner": req.learner,
                    "guardian": req.guardian,
                    "PLATFORM_NAME": getattr(settings, "PLATFORM_NAME", "Mentify"),
                })
                send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [req.guardian.email], fail_silently=True)
                messages.success(request, "Request accepted and guardian notified.")
            elif verb == "reject" and req.status == GuardianLinkRequest.Status.PENDING:
                req.status = GuardianLinkRequest.Status.REJECTED
                req.responded_at = timezone.now()
                req.save()
                GuardianLinkRequestLog.objects.create(
                    request=req,
                    event=GuardianLinkRequestLog.Event.REJECTED,
                    actor=request.user,
                    message="Admin rejected guardian link request.",
                )
                subject = f"{req.learner.get_full_name()} declined your guardian request"
                message_body = render_to_string("accounts/emails/guardian_link_rejected.txt", {
                    "learner": req.learner,
                    "guardian": req.guardian,
                    "PLATFORM_NAME": getattr(settings, "PLATFORM_NAME", "Mentify"),
                })
                send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [req.guardian.email], fail_silently=True)
                messages.success(request, "Request rejected and guardian notified.")
        return redirect("accounts:admin_guardian_requests")

    requests = GuardianLinkRequest.objects.select_related("guardian", "learner").order_by("-created_at")
    return render(request, "accounts/admin_guardian_requests.html", {"requests": requests})


@login_required
@role_required("guardian")
def guardian_dashboard(request):
    """Guardian view: linked learners' progress and payment status."""
    from payments.models import Subscription
    from courses.models import Enrollment
    from content.models import Lesson, LessonProgress
    from assignments.models import Assignment, Submission
    from live_sessions.models import Attendance, LiveSession
    from django.utils import timezone

    try:
        guardian = request.user.guardian_profile
        learners = guardian.learners.all()
    except Exception:
        learners = User.objects.none()

    # Build per-learner summary for the guardian
    learners_data = []
    for learner in learners:
        enrollments = Enrollment.objects.filter(
            learner=learner, status="active"
        ).select_related("cohort__course")

        cohort_summaries = []
        for enrollment in enrollments:
            cohort = enrollment.cohort

            total_lessons = Lesson.objects.filter(cohort=cohort, is_published=True).count()
            done_lessons = LessonProgress.objects.filter(
                learner=learner, lesson__cohort=cohort, completed=True
            ).count()
            lessons_pct = round((done_lessons / total_lessons) * 100) if total_lessons else 0

            total_assignments = Assignment.objects.filter(
                lesson__cohort=cohort, is_published=True
            ).count()
            submitted = Submission.objects.filter(
                learner=learner,
                assignment__lesson__cohort=cohort,
                status__in=[Submission.Status.SUBMITTED, Submission.Status.GRADED],
            ).count()
            assignments_pct = round((submitted / total_assignments) * 100) if total_assignments else 0

            total_sessions = LiveSession.objects.filter(
                cohort=cohort, scheduled_at__lt=timezone.now(), is_cancelled=False
            ).count()
            present = Attendance.objects.filter(
                session__cohort=cohort, learner=learner, status=Attendance.Status.PRESENT
            ).count()
            attendance_pct = round((present / total_sessions) * 100) if total_sessions else None

            # Active subscription
            sub = Subscription.objects.filter(learner=learner, cohort=cohort).first()

            cohort_summaries.append({
                "cohort": cohort,
                "lessons_pct": lessons_pct,
                "assignments_pct": assignments_pct,
                "attendance_pct": attendance_pct,
                "sub": sub,
            })

        learners_data.append({
            "learner": learner,
            "cohort_summaries": cohort_summaries,
        })

    context = {"learners_data": learners_data}
    # Also pass raw learners queryset so template blocks that expect `learners` work
    context["learners"] = learners
    return render(request, "accounts/guardian_dashboard.html", context)


# ─── Profile ──────────────────────────────────────────────────────────────────

@login_required
def profile_view(request):
    """View and update own profile."""
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("accounts:profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(request, "accounts/profile.html", {
        "user_form": user_form,
        "profile_form": profile_form,
    })


# ─── Google OAuth ────────────────────────────────────────────────────────────

def google_login(request):
    """Initiates Google OAuth2 login flow."""
    import secrets
    from urllib.parse import urlencode

    action = request.GET.get("action", "login")
    role = request.GET.get("role", "learner")

    if not settings.GOOGLE_CLIENT_ID:
        messages.error(request, "Google sign-in is not configured yet.")
        return redirect("accounts:login")

    state = secrets.token_urlsafe(16)
    request.session["oauth_state"] = state
    request.session["pending_action"] = action
    request.session["pending_role"] = role

    # Resolve redirect URL
    redirect_uri = settings.GOOGLE_REDIRECT_URI or request.build_absolute_uri(reverse("accounts:google_callback"))

    params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": "openid email profile",
        "state": state,
    }
    google_auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}"
    return redirect(google_auth_url)


def google_callback(request):
    """Processes Google OAuth2 callback and logs in the user."""
    import requests
    from django.contrib.auth import get_user_model
    User = get_user_model()

    state = request.GET.get("state")
    session_state = request.session.pop("oauth_state", None)

    if not state or state != session_state:
        messages.error(request, "Google sign-in security check failed.")
        return redirect("accounts:login")

    action = request.session.pop("pending_action", "login")
    role = request.session.pop("pending_role", "learner")
    code = request.GET.get("code")

    if not code:
        messages.info(request, "Google sign-in was cancelled.")
        return redirect("accounts:login")

    # Resolve redirect URL
    redirect_uri = settings.GOOGLE_REDIRECT_URI or request.build_absolute_uri(reverse("accounts:google_callback"))

    # Exchange authorization code for access token
    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }
    
    try:
        response = requests.post(token_url, data=token_data, timeout=15)
        if not response.ok:
            messages.error(request, "Google token exchange failed.")
            return redirect("accounts:login")
        access_token = response.json().get("access_token")
    except Exception:
        messages.error(request, "Failed to connect to Google authentication server.")
        return redirect("accounts:login")

    if not access_token:
        messages.error(request, "Google authentication did not return a valid token.")
        return redirect("accounts:login")

    # Fetch user profile data
    profile_url = "https://www.googleapis.com/oauth2/v3/userinfo"
    try:
        profile_response = requests.get(
            profile_url,
            headers={"Authorization": f"Bearer {access_token}"},
            timeout=10,
        )
        if not profile_response.ok:
            messages.error(request, "Failed to fetch Google profile details.")
            return redirect("accounts:login")
        profile = profile_response.json()
    except Exception:
        messages.error(request, "Failed to connect to Google profile server.")
        return redirect("accounts:login")

    email = (profile.get("email") or "").strip().lower()
    if not email:
        messages.error(request, "Google authentication did not return an email address.")
        return redirect("accounts:login")

    # Get or create the user based on email
    user = User.objects.filter(email=email).first()
    
    if not user:
        if action == "login":
            messages.warning(request, "No account exists for this Google email. Please register first to choose your role.")
            return redirect("accounts:register")

        # Create new user for registration
        name = profile.get("name") or email.split("@")[0]
        first_name = profile.get("given_name") or name.split()[0]
        last_name = profile.get("family_name") or (name.split()[1] if len(name.split()) > 1 else "")
        username = email.split("@")[0]
        
        # Ensure username uniqueness
        base_username = username
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1

        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role,
        )
        # Mark email verified
        user.is_email_verified = True
        user.save()
        messages.success(request, f"Successfully registered and logged in as {user.first_name}!")
    else:
        # User already exists, log them in
        messages.success(request, f"Welcome back, {user.first_name}!")

    login(request, user)
    promote_if_admin_email(user)  # auto-promote whitelisted admins
    return redirect(user.get_dashboard_url())

