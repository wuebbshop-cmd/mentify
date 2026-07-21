"""content/views.py — Lesson browsing and resource access."""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import StreamingHttpResponse, Http404
from django.utils import timezone
from django.contrib import messages

from .models import Lesson, VideoAsset, Resource, LessonProgress
from .mixins import cohort_access_required, check_cohort_access
from courses.models import Cohort
from accounts.decorators import role_required


@login_required
@cohort_access_required
def cohort_lessons(request, cohort_id):
    """Learner views all lessons for an enrolled cohort."""
    cohort = get_object_or_404(Cohort, id=cohort_id)
    lessons = Lesson.objects.filter(cohort=cohort, is_published=True).order_by("order")

    # Progress lookup for this learner
    if request.user.is_learner:
        completed_ids = set(
            LessonProgress.objects.filter(
                learner=request.user, lesson__in=lessons, completed=True
            ).values_list("lesson_id", flat=True)
        )
    else:
        completed_ids = set()

    return render(request, "content/lesson_list.html", {
        "cohort": cohort,
        "lessons": lessons,
        "completed_ids": completed_ids,
    })


@login_required
@cohort_access_required
def lesson_detail(request, cohort_id, lesson_id):
    """Learner watches a lesson (Bunny embed + resources + assignment)."""
    cohort = get_object_or_404(Cohort, id=cohort_id)
    lesson = get_object_or_404(Lesson, id=lesson_id, cohort=cohort, is_published=True)

    video = getattr(lesson, "video", None)
    resources = lesson.resources.all().order_by("resource_type", "title")

    # Mark as viewed
    if request.user.is_learner:
        progress, created = LessonProgress.objects.get_or_create(
            learner=request.user, lesson=lesson
        )
        if not progress.completed:
            progress.completed = True
            progress.completed_at = timezone.now()
            progress.save()

    # Assignments
    assignments = lesson.assignments.filter(is_published=True)

    return render(request, "content/lesson_detail.html", {
        "cohort": cohort,
        "lesson": lesson,
        "video": video,
        "resources": resources,
        "assignments": assignments,
    })


@login_required
def resource_download(request, resource_id):
    """
    Proxy endpoint for GitHub-hosted PDFs.
    Streams the file from GitHub using the stored token — learner never sees the raw GitHub URL.
    """
    resource = get_object_or_404(Resource, id=resource_id)

    # Check access
    cohort = resource.lesson.cohort
    if not check_cohort_access(request.user, cohort):
        raise Http404("Resource not found or access denied.")

    if resource.resource_type != Resource.ResourceType.PDF or not resource.github_stored_path:
        raise Http404("Not a downloadable file.")

    from services.github_service import GitHubService
    from django.conf import settings

    try:
        svc = GitHubService(settings.GITHUB_TOKEN, settings.GITHUB_REPO, settings.GITHUB_BRANCH)
        file_bytes = svc.download_file(resource.github_stored_path)
    except Exception:
        raise Http404("File not available.")

    response = StreamingHttpResponse(
        streaming_content=iter([file_bytes]),
        content_type="application/pdf",
    )
    safe_name = resource.title.replace(" ", "_")
    response["Content-Disposition"] = f'attachment; filename="{safe_name}.pdf"'
    return response


# ─── Tutor content management ─────────────────────────────────────────────────

@login_required
@role_required("tutor", "admin")
def create_lesson(request, cohort_id):
    """Tutor creates a new lesson in their cohort."""
    from django.conf import settings

    if request.user.is_admin:
        cohort = get_object_or_404(Cohort, id=cohort_id)
    else:
        cohort = get_object_or_404(Cohort, id=cohort_id, tutor=request.user)

    from .forms import LessonForm
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.cohort = cohort
            lesson.created_by = request.user
            lesson.save()
            messages.success(request, f"Lesson '{lesson.title}' created.")
            return redirect("content:lesson_edit", cohort_id=cohort.id, lesson_id=lesson.id)
    else:
        # Auto-set order
        last_order = Lesson.objects.filter(cohort=cohort).order_by("-order").values_list("order", flat=True).first()
        form = LessonForm(initial={"order": (last_order or 0) + 1})

    return render(request, "content/lesson_form.html", {"form": form, "cohort": cohort, "action": "Create"})


@login_required
@role_required("tutor", "admin")
def edit_lesson(request, cohort_id, lesson_id):
    """Tutor edits lesson, video ID, and resources."""
    if request.user.is_admin:
        cohort = get_object_or_404(Cohort, id=cohort_id)
    else:
        cohort = get_object_or_404(Cohort, id=cohort_id, tutor=request.user)

    lesson = get_object_or_404(Lesson, id=lesson_id, cohort=cohort)
    video = getattr(lesson, "video", None)
    resources = lesson.resources.all()

    from .forms import LessonForm, VideoAssetForm, ResourceForm
    lesson_form = LessonForm(request.POST or None, instance=lesson)
    video_form = VideoAssetForm(request.POST or None, instance=video)
    resource_form = ResourceForm()

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "save_lesson" and lesson_form.is_valid():
            lesson_form.save()
            # Handle video
            if video_form.is_valid() and video_form.cleaned_data.get("bunny_video_id"):
                va = video_form.save(commit=False)
                va.lesson = lesson
                va.save()
            messages.success(request, "Lesson saved.")
            return redirect("content:lesson_edit", cohort_id=cohort.id, lesson_id=lesson.id)

        elif action == "add_resource":
            resource_form = ResourceForm(request.POST, request.FILES)
            if resource_form.is_valid():
                resource = resource_form.save(commit=False)
                resource.lesson = lesson
                # Handle PDF upload to GitHub
                if request.FILES.get("pdf_file"):
                    from services.github_service import GitHubService
                    from django.conf import settings
                    svc = GitHubService(settings.GITHUB_TOKEN, settings.GITHUB_REPO, settings.GITHUB_BRANCH)
                    result = svc.upload_file(
                        request.FILES["pdf_file"],
                        subdir=f"cohort_{cohort.id}/lesson_{lesson.id}"
                    )
                    if result:
                        resource.github_stored_path = result.stored_path
                resource.save()
                messages.success(request, f"Resource '{resource.title}' added.")
                return redirect("content:lesson_edit", cohort_id=cohort.id, lesson_id=lesson.id)

    return render(request, "content/lesson_edit.html", {
        "cohort": cohort,
        "lesson": lesson,
        "lesson_form": lesson_form,
        "video_form": video_form,
        "resource_form": resource_form,
        "resources": resources,
        "video": video,
    })
