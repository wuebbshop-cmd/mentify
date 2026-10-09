from django.utils import timezone

from prep.models import PrepNotePrecomputeJob, PrepTopic, PrepTopicNotesJob


NOTE_LEVELS_IN_PRIORITY_ORDER = ("level_2", "level_1", "level_3")


def enqueue_course_note_precompute(course):
    """Create or safely requeue the durable all-level notes preparation job."""
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


def enqueue_course_topic_note_jobs(course) -> int:
    """Expand a published course into idempotent jobs for each topic and note level."""
    from services.prep_ai_router import _topic_notes_cache_signature

    queued = 0
    topics = PrepTopic.objects.filter(course=course, is_active=True).order_by("order", "id")
    for topic in topics:
        signature = _topic_notes_cache_signature(course, topic, topic.title, topic.subtopics)
        for level in NOTE_LEVELS_IN_PRIORITY_ORDER:
            job, created = PrepTopicNotesJob.objects.get_or_create(
                topic=topic,
                level=level,
                source_signature=signature,
                defaults={"status": "pending"},
            )
            if created:
                queued += 1
                continue
            if job.status in {"pending", "running"}:
                continue
            if job.status == "complete":
                continue
            changed = PrepTopicNotesJob.objects.filter(
                pk=job.pk,
                status="failed",
            ).update(
                status="pending",
                attempts=0,
                last_error="",
                provider_usage={},
                model_name="",
                queued_at=timezone.now(),
                started_at=None,
                completed_at=None,
            )
            queued += int(bool(changed))
    return queued


enqueue_course_level_two_precompute = enqueue_course_note_precompute
