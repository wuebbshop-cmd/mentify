"""assignments/views.py"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from accounts.decorators import role_required
from content.mixins import check_cohort_access
from .models import Assignment, Submission, Grade, CriterionScore
from .forms import AssignmentForm, SubmissionForm, GradeForm


@login_required
def assignment_detail(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id, is_published=True)
    cohort = assignment.lesson.cohort
    if not check_cohort_access(request.user, cohort):
        messages.error(request, "You need an active subscription to access this assignment.")
        return redirect("payments:initiate", cohort_id=cohort.id)
    submission = None
    if request.user.is_learner:
        submission = Submission.objects.filter(assignment=assignment, learner=request.user).first()
    return render(request, "assignments/detail.html", {
        "assignment": assignment,
        "submission": submission,
        "criteria": assignment.criteria.all(),
    })


@login_required
@role_required("learner")
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id, is_published=True)
    cohort = assignment.lesson.cohort
    if not check_cohort_access(request.user, cohort):
        return redirect("payments:initiate", cohort_id=cohort.id)

    submission, _ = Submission.objects.get_or_create(
        assignment=assignment, learner=request.user
    )
    if submission.status == Submission.Status.GRADED:
        messages.warning(request, "This assignment has already been graded.")
        return redirect("assignments:detail", assignment_id=assignment_id)

    form = SubmissionForm(request.POST or None, request.FILES or None, instance=submission)
    if request.method == "POST" and form.is_valid():
        sub = form.save(commit=False)
        if request.FILES.get("submission_file"):
            from services.github_service import GitHubService
            from django.conf import settings
            svc = GitHubService(settings.GITHUB_TOKEN, settings.GITHUB_REPO, settings.GITHUB_BRANCH)
            result = svc.upload_file(
                request.FILES["submission_file"],
                subdir=f"submissions/assignment_{assignment.id}/learner_{request.user.id}"
            )
            if result:
                sub.github_stored_path = result.stored_path
        sub.status = Submission.Status.SUBMITTED
        sub.submitted_at = timezone.now()
        sub.save()
        messages.success(request, "Assignment submitted successfully!")
        return redirect("assignments:detail", assignment_id=assignment_id)

    return render(request, "assignments/submit.html", {
        "assignment": assignment,
        "form": form,
        "submission": submission,
    })


@login_required
@role_required("learner")
def learner_grade_view(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    submission = get_object_or_404(Submission, assignment=assignment, learner=request.user)
    grade = getattr(submission, "grade", None)
    return render(request, "assignments/my_grade.html", {
        "assignment": assignment,
        "submission": submission,
        "grade": grade,
        "criterion_scores": grade.criterion_scores.select_related("criterion").all() if grade else [],
    })


@login_required
@role_required("tutor", "admin")
def create_assignment(request, lesson_id):
    from content.models import Lesson
    lesson = get_object_or_404(Lesson, id=lesson_id)
    if not request.user.is_admin and lesson.cohort.tutor != request.user:
        messages.error(request, "You don't own this cohort.")
        return redirect("accounts:tutor_dashboard")

    form = AssignmentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        assignment = form.save(commit=False)
        assignment.lesson = lesson
        assignment.save()
        messages.success(request, f"Assignment '{assignment.title}' created.")
        return redirect("content:lesson_edit", cohort_id=lesson.cohort.id, lesson_id=lesson.id)

    return render(request, "assignments/create.html", {"form": form, "lesson": lesson})


@login_required
@role_required("tutor", "admin")
def assignment_submissions(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if not request.user.is_admin and assignment.lesson.cohort.tutor != request.user:
        messages.error(request, "Access denied.")
        return redirect("accounts:tutor_dashboard")
    submissions = assignment.submissions.filter(
        status=Submission.Status.SUBMITTED
    ).select_related("learner")
    return render(request, "assignments/submissions_list.html", {
        "assignment": assignment,
        "submissions": submissions,
    })


@login_required
@role_required("tutor", "admin")
def grade_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    assignment = submission.assignment
    if not request.user.is_admin and assignment.lesson.cohort.tutor != request.user:
        messages.error(request, "Access denied.")
        return redirect("accounts:tutor_dashboard")

    criteria = assignment.criteria.all()
    existing_grade = getattr(submission, "grade", None)

    if request.method == "POST":
        grade_form = GradeForm(request.POST, instance=existing_grade)
        if grade_form.is_valid():
            grade = grade_form.save(commit=False)
            grade.submission = submission
            grade.graded_by = request.user
            total = 0
            for criterion in criteria:
                score_val = float(request.POST.get(f"criterion_{criterion.id}", 0) or 0)
                total += score_val
            grade.total_score = total
            grade.save()
            for criterion in criteria:
                score_val = float(request.POST.get(f"criterion_{criterion.id}", 0) or 0)
                CriterionScore.objects.update_or_create(
                    grade=grade,
                    criterion=criterion,
                    defaults={
                        "score": score_val,
                        "comment": request.POST.get(f"comment_{criterion.id}", ""),
                    },
                )
            submission.status = Submission.Status.GRADED
            submission.save()
            messages.success(request, f"Grade submitted: {total}/{assignment.max_score}")
            return redirect("assignments:submissions", assignment_id=assignment.id)
    else:
        grade_form = GradeForm(instance=existing_grade)

    return render(request, "assignments/grade_form.html", {
        "submission": submission,
        "assignment": assignment,
        "grade_form": grade_form,
        "criteria": criteria,
        "existing_grade": existing_grade,
    })
