from django.utils import timezone

from prep.models import PrepNotePrecomputeJob


def enqueue_course_level_two_precompute(course):
    """Create or safely requeue the single durable Level 2 job for a course."""
    job, created = PrepNotePrecomputeJob.objects.get_or_create(course=course)
    if created:
        return job, True
    if job.status in {"pending", "running"}:
        return job, False

    changed = PrepNotePrecomputeJob.objects.filter(
        pk=job.pk,
        status__in=["complete", "failed"],
    ).update(
        status="pending",
        attempts=0,
        last_error="",
        queued_at=timezone.now(),
        started_at=None,
        completed_at=None,
    )
    if changed:
        job.refresh_from_db()
    return job, bool(changed)
