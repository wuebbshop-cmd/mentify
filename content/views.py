"""content/views.py - Lesson browsing and resource access."""
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
    from django.conf import settings
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

    # Build video embed URL — sign it server-side if token auth is enabled
    video_embed_url = None
    video_thumbnail_url = None
    video_is_direct = False
    if video:
        if video.github_stored_path:
            # Legacy proxy-streamed file (no Bunny CDN — direct from Django)
            video_embed_url = f"/content/video/{video.pk}/stream/"
            video_is_direct = True
        elif video.bunny_video_id:
            library_id = video.bunny_library_id or getattr(settings, "BUNNY_STREAM_LIBRARY_ID", "")
            token_auth_key = getattr(settings, "BUNNY_TOKEN_AUTH_KEY", "").strip()
            cdn_hostname = getattr(settings, "BUNNY_CDN_HOSTNAME", "").strip()

            if library_id and token_auth_key:
                # Token Authentication enabled — generate server-side signed URL.
                # 60-minute expiry: matches max lesson length, minimises replay window.
                from services.bunny_service import sign_bunny_embed_url
                video_embed_url = sign_bunny_embed_url(
                    library_id=library_id,
                    video_id=video.bunny_video_id,
                    token_auth_key=token_auth_key,
                    expires_seconds=3600,  # 60-minute window — matches max 45-min lesson
                )
            elif library_id:
                # No token auth — plain public embed URL
                video_embed_url = (
                    f"https://iframe.mediadelivery.net/embed/{library_id}/{video.bunny_video_id}"
                    f"?autoplay=false&loop=false&muted=false&preload=true&responsive=true"
                )

            # Bunny auto-generates a thumbnail at {cdn_hostname}/{video_id}/thumbnail.jpg
            # Used for the click-to-load facade (saves player JS from loading until user clicks play)
            if cdn_hostname and video.bunny_video_id:
                video_thumbnail_url = f"https://{cdn_hostname}/{video.bunny_video_id}/thumbnail.jpg"

            video_is_direct = False

    return render(request, "content/lesson_detail.html", {
        "cohort": cohort,
        "lesson": lesson,
        "video": video,
        "video_embed_url": video_embed_url,
        "video_thumbnail_url": video_thumbnail_url,
        "video_is_direct": video_is_direct,
        "resources": resources,
        "assignments": assignments,
    })


@login_required
def resource_download(request, resource_id):
    """
    Proxy endpoint for GitHub-hosted PDFs.
    Streams the file from GitHub using the stored token - learner never sees the raw GitHub URL.
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
        svc = GitHubService(
            settings.GITHUB_TOKEN,
            settings.GITHUB_REPO,
            settings.GITHUB_BRANCH,
            settings.GITHUB_UPLOAD_DIR,
        )
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


@login_required
def video_stream(request, video_id):
    """
    Proxy endpoint for streaming uploaded video assets securely.
    Supports HTTP Range requests so the browser's native <video> controls
    (seeking, scrubbing) work correctly — exactly like real CDN video delivery.
    """
    from .models import VideoAsset
    video = get_object_or_404(VideoAsset, id=video_id)
    cohort = video.lesson.cohort
    if not check_cohort_access(request.user, cohort):
        raise Http404("Video not found or access denied.")

    if not video.github_stored_path:
        raise Http404("No video file stream available.")

    from services.github_service import GitHubService
    from django.conf import settings
    from django.http import HttpResponse

    try:
        svc = GitHubService(
            settings.GITHUB_TOKEN,
            settings.GITHUB_REPO,
            settings.GITHUB_BRANCH,
            settings.GITHUB_UPLOAD_DIR,
        )
        file_bytes = svc.download_file(video.github_stored_path)
    except Exception:
        raise Http404("Video file not available.")

    file_size = len(file_bytes)
    content_type = "video/mp4"

    # --- HTTP Range support (seek/scrub support in HTML5 <video>) ---
    range_header = request.META.get("HTTP_RANGE", "").strip()
    if range_header and range_header.startswith("bytes="):
        try:
            ranges = range_header[6:].split("-")
            start = int(ranges[0]) if ranges[0] else 0
            end = int(ranges[1]) if len(ranges) > 1 and ranges[1] else file_size - 1
            end = min(end, file_size - 1)
            chunk = file_bytes[start:end + 1]
            response = HttpResponse(chunk, status=206, content_type=content_type)
            response["Content-Range"] = f"bytes {start}-{end}/{file_size}"
            response["Content-Length"] = len(chunk)
        except (ValueError, IndexError):
            response = HttpResponse(file_bytes, content_type=content_type)
            response["Content-Length"] = file_size
    else:
        response = HttpResponse(file_bytes, content_type=content_type)
        response["Content-Length"] = file_size

    response["Accept-Ranges"] = "bytes"
    response["Content-Disposition"] = "inline"
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
            try:
                lesson = form.save(commit=False)
                lesson.cohort = cohort
                lesson.created_by = request.user
                lesson.save()
                messages.success(request, f"Lesson '{lesson.title}' created.")
                return redirect("content:lesson_edit", cohort_id=cohort.id, lesson_id=lesson.id)
            except Exception as e:
                from django.db import IntegrityError
                if isinstance(e, IntegrityError):
                    messages.error(request, f"Lesson order #{form.cleaned_data.get('order')} is already used in this cohort. Please pick a different order number.")
                else:
                    messages.error(request, f"Failed to create lesson: {e}")
        else:
            messages.error(request, "Please correct the errors in the form below.")
    else:
        # Auto-set order
        last_order = Lesson.objects.filter(cohort=cohort).order_by("-order").values_list("order", flat=True).first()
        form = LessonForm(initial={"order": (last_order or 0) + 1})

    return render(request, "content/lesson_form.html", {"form": form, "cohort": cohort, "action": "Create"})


@login_required
@role_required("tutor", "admin")
def edit_lesson(request, cohort_id, lesson_id):
    """Tutor edits lesson, video file, and resources."""
    if request.user.is_admin:
        cohort = get_object_or_404(Cohort, id=cohort_id)
    else:
        cohort = get_object_or_404(Cohort, id=cohort_id, tutor=request.user)

    lesson = get_object_or_404(Lesson, id=lesson_id, cohort=cohort)
    video = getattr(lesson, "video", None)
    resources = lesson.resources.all()

    from .forms import LessonForm, VideoAssetForm, ResourceForm
    lesson_form = LessonForm(request.POST or None, instance=lesson)
    video_form = VideoAssetForm(request.POST or None, request.FILES or None, instance=video)
    resource_form = ResourceForm()

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "save_lesson":
            if lesson_form.is_valid():
                try:
                    lesson_form.save()
                except Exception as e:
                    from django.db import IntegrityError
                    if isinstance(e, IntegrityError):
                        messages.error(request, f"Lesson order #{lesson_form.cleaned_data.get('order')} is already used in this cohort. Please choose a different order number.")
                    else:
                        messages.error(request, f"Failed to save lesson: {e}")
                    return redirect("content:lesson_edit", cohort_id=cohort.id, lesson_id=lesson.id)

                # Handle video upload
                if video_form.is_valid():
                    video_file = video_form.cleaned_data.get("video_file")
                    if video_file:
                        from django.conf import settings
                        from .models import VideoAsset

                        uploaded_bunny = None
                        bunny_lib = getattr(settings, "BUNNY_STREAM_LIBRARY_ID", "").strip()
                        bunny_key = getattr(settings, "BUNNY_STREAM_API_KEY", "").strip()

                        if bunny_lib and bunny_key:
                            try:
                                from services.bunny_service import BunnyStreamService
                                service = BunnyStreamService(bunny_lib, bunny_key)
                                uploaded_bunny = service.upload(lesson.title, video_file)
                            except Exception as exc:
                                uploaded_bunny = None
                                _bunny_exc = str(exc)
                            else:
                                _bunny_exc = None
                        else:
                            uploaded_bunny = None
                            _bunny_exc = "Bunny Stream credentials not configured."

                        va, _ = VideoAsset.objects.get_or_create(lesson=lesson)
                        if uploaded_bunny:
                            va.bunny_video_id = uploaded_bunny.video_id
                            va.bunny_library_id = uploaded_bunny.library_id
                            va.github_stored_path = ""  # clear any legacy fallback path
                            va.save()
                            messages.success(request, "Lesson saved & video uploaded to Bunny Stream.")
                        else:
                            messages.error(
                                request,
                                f"Video upload failed — please try again or contact support. "
                                f"({_bunny_exc})"
                            )
                    elif video_form.cleaned_data.get("bunny_video_id"):
                        va = video_form.save(commit=False)
                        va.lesson = lesson
                        va.save()
                        messages.success(request, "Lesson details & video saved.")
                    else:
                        messages.success(request, "Lesson saved successfully.")
                else:
                    messages.error(request, "Please check the video upload details and try again.")
            else:
                messages.error(request, "Please correct the errors in the lesson details form.")
            return redirect("content:lesson_edit", cohort_id=cohort.id, lesson_id=lesson.id)

        elif action == "add_resource":
            resource_form = ResourceForm(request.POST, request.FILES)
            if resource_form.is_valid():
                try:
                    resource = resource_form.save(commit=False)
                    resource.lesson = lesson
                    # Handle PDF upload to GitHub
                    if request.FILES.get("pdf_file"):
                        from services.github_service import GitHubService
                        from django.conf import settings
                        svc = GitHubService(
                            settings.GITHUB_TOKEN,
                            settings.GITHUB_REPO,
                            settings.GITHUB_BRANCH,
                            settings.GITHUB_UPLOAD_DIR,
                        )
                        result = svc.upload_file(
                            request.FILES["pdf_file"],
                            subdir=f"cohort_{cohort.id}/lesson_{lesson.id}"
                        )
                        if result:
                            resource.github_stored_path = result.stored_path
                    resource.save()
                    messages.success(request, f"Resource '{resource.title}' added successfully.")
                except Exception as e:
                    messages.error(request, f"Could not add resource: {e}")
                return redirect("content:lesson_edit", cohort_id=cohort.id, lesson_id=lesson.id)
            messages.error(request, "Please correct the resource details and try again.")

    return render(request, "content/lesson_edit.html", {
        "cohort": cohort,
        "lesson": lesson,
        "lesson_form": lesson_form,
        "video_form": video_form,
        "resource_form": resource_form,
        "resources": resources,
        "video": video,
    })
