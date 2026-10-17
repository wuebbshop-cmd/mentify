import logging
from concurrent.futures import ThreadPoolExecutor
from django.db import close_old_connections, connection
from django.utils import timezone

from prep.models import PrepCourse, PrepNotePrecomputeJob, PrepTopic, PrepTopicNotesJob

logger = logging.getLogger(__name__)

NOTE_LEVELS_IN_PRIORITY_ORDER = ("level_2", "level_1", "level_3")

# Shared background executor for note precomputations (avoids needing a separate terminal worker)
_NOTE_PRECOMPUTE_EXECUTOR = ThreadPoolExecutor(max_workers=2, thread_name_prefix="prep-notes-worker")


def enqueue_course_note_precompute(course, *, auto_run: bool = True):
    """
    Create or safely requeue the durable all-level notes preparation job.
    Automatically enqueues all topic jobs and submits them to the background worker pool.
    """
    job, created = PrepNotePrecomputeJob.objects.get_or_create(course=course)
    should_run = created
    if not created and job.status not in {"pending", "running"}:
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
            should_run = True

    # Expand topics immediately into per-topic note jobs
    enqueue_course_topic_note_jobs(course)

    # Automatically process in background thread
    if auto_run:
        _NOTE_PRECOMPUTE_EXECUTOR.submit(process_course_notes_in_background, course.id)

    return job, should_run


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


def process_single_topic_notes_job(job: PrepTopicNotesJob) -> bool:
    """
    Generate, validate, and persist notes for one specific PrepTopicNotesJob.
    """
    from services.prep_ai_router import (
        _note_completion_issues,
        _note_validation_options,
        _topic_notes_cache_signature,
        get_or_generate_topic_notes,
    )
    from services.credit_service import credits_for_usage
    from services.prep_course_billing import create_shared_course_cost, settle_course_cost_share
    from services.prep_pdf_artifacts import enqueue_topic_pdf_artifact

    topic = job.topic
    result = get_or_generate_topic_notes(
        topic.course.code,
        topic.title,
        subtopics=topic.subtopics if isinstance(topic.subtopics, list) else [],
        level=job.level,
        course_obj=topic.course,
        topic_obj=topic,
    )
    notes = str(result.get("notes") or result.get("content") or "").strip()
    usage = result.get("usage") if isinstance(result.get("usage"), dict) else {}
    model_name = str(result.get("model") or result.get("model_used") or "")
    if not notes:
        raise RuntimeError(
            result.get("error") or "The notes provider did not return validated notes."
        )
    if result.get("stale"):
        raise RuntimeError("A stale note cannot complete a job for the current source version.")
    review_status = result.get("review_status")
    if review_status and review_status != "passed":
        raise RuntimeError(
            "The notes worker rejected notes without a successful independent review: "
            + str(review_status)
        )
    if not result.get("cached") and review_status != "passed":
        raise RuntimeError(
            "Fresh notes cannot complete a job without a successful independent review."
        )

    validation_options = _note_validation_options(
        topic.course,
        topic.title,
        topic.summary,
        topic.subtopics,
        topic_obj=topic,
    )
    validation_issues = _note_completion_issues(
        notes,
        topic.title,
        **validation_options,
    )
    if validation_issues:
        raise RuntimeError(
            "The notes worker rejected unvalidated content: "
            + "; ".join(validation_issues)
        )

    if not result.get("cached") and job.level == "level_2":
        signature = _topic_notes_cache_signature(
            topic.course,
            topic,
            topic.title,
            topic.subtopics,
        )
        cost = create_shared_course_cost(
            course=topic.course,
            cost_type="topic_notes",
            total_credits=credits_for_usage(usage, minimum=1),
            source_key=f"topic-notes:{topic.pk}:{job.level}:{signature}",
            topic=topic,
            level=job.level,
            usage=usage,
            model_name=model_name or "deepseek-chat",
        )
        for share in cost.shares.select_related("user", "cost").all():
            settle_course_cost_share(share)

    job.status = "complete"
    job.completed_at = timezone.now()
    job.last_error = ""
    job.provider_usage = usage
    job.model_name = model_name
    job.save(
        update_fields=[
            "status",
            "completed_at",
            "last_error",
            "provider_usage",
            "model_name",
        ]
    )
    try:
        enqueue_topic_pdf_artifact(topic, "notes", job.level)
    except Exception:
        pass
    return True


def process_course_notes_in_background(course_id: int):
    """Background worker thread function that runs through all pending jobs for a course."""
    if not connection.in_atomic_block:
        close_old_connections()
    try:
        course = PrepCourse.objects.filter(pk=course_id).first()
        if not course:
            return

        level_order = {"level_2": 0, "level_1": 1, "level_3": 2}
        jobs = list(PrepTopicNotesJob.objects.filter(
            topic__course=course,
            status="pending"
        ))
        sorted_jobs = sorted(jobs, key=lambda j: (level_order.get(j.level, 3), j.id))

        for job in sorted_jobs:
            if not connection.in_atomic_block:
                close_old_connections()
            try:
                job.refresh_from_db()
            except Exception:
                continue
            if job.status != "pending":
                continue
            job.status = "running"
            job.attempts += 1
            job.started_at = timezone.now()
            job.save(update_fields=["status", "attempts", "started_at"])
            try:
                process_single_topic_notes_job(job)
                logger.info("Auto-worker generated %s notes for topic %s (%s)", job.level, job.topic_id, job.topic.title)
            except Exception as exc:
                logger.warning("Auto-worker error for note job %s topic %s: %s", job.id, job.topic_id, exc)
                job.status = "pending" if job.attempts < 3 else "failed"
                job.last_error = str(exc)[:4000]
                job.completed_at = timezone.now() if job.status == "failed" else None
                job.save(update_fields=["status", "last_error", "completed_at"])

        # Mark course precompute job complete if all jobs are complete
        all_jobs = PrepTopicNotesJob.objects.filter(topic__course=course)
        if all_jobs.exists() and not all_jobs.filter(status__in=["pending", "running"]).exists():
            PrepNotePrecomputeJob.objects.filter(course=course).update(
                status="complete",
                completed_at=timezone.now(),
                last_error="",
            )
    except Exception as exc:
        logger.exception("Unexpected error in process_course_notes_in_background for course %s: %s", course_id, exc)
    finally:
        if not connection.in_atomic_block:
            close_old_connections()


enqueue_course_level_two_precompute = enqueue_course_note_precompute
