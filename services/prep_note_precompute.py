import logging
from concurrent.futures import ThreadPoolExecutor
from django.conf import settings
from django.db import close_old_connections, connection
from django.utils import timezone

from prep.models import PrepCourse, PrepNotePrecomputeJob, PrepTopic, PrepTopicNotesJob

logger = logging.getLogger(__name__)

NOTE_LEVELS_IN_PRIORITY_ORDER = ("level_2", "level_1", "level_3")

# Shared background executor for note precomputations (avoids needing a separate terminal worker)
_NOTE_PRECOMPUTE_EXECUTOR = ThreadPoolExecutor(max_workers=2, thread_name_prefix="prep-notes-worker")


def automatic_note_preparation_enabled() -> bool:
    """Whether this process may create or execute AI topic-note jobs."""
    return bool(getattr(settings, "PREP_AUTOMATIC_NOTE_PREPARATION", True))


def enqueue_course_note_precompute(course, *, auto_run: bool = True):
    """
    Create or safely requeue the durable all-level notes preparation job.
    Automatically enqueues all topic jobs and submits them to the background worker pool.
    """
    if not automatic_note_preparation_enabled():
        logger.info(
            "[Prep] Automatic note preparation is disabled; course %s was not queued.",
            course.pk,
        )
        return None, False

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
        try:
            _NOTE_PRECOMPUTE_EXECUTOR.submit(process_course_notes_in_background, course.id)
        except RuntimeError as exc:
            # Raised when the interpreter is already shutting down (dev autoreload,
            # worker restart). The durable job rows above are already queued, so the
            # work is picked up later instead of 500-ing the request that triggered it.
            logger.warning(
                "[Prep] note precompute not scheduled for course %s: %s", course.id, exc
            )

    return job, should_run


def enqueue_course_topic_note_jobs(course) -> int:
    """Expand a published course into idempotent jobs for each topic and note level."""
    if not automatic_note_preparation_enabled():
        return 0

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
            if job.status == "complete" and _has_current_topic_note_cache(topic, level, signature):
                continue
            changed = PrepTopicNotesJob.objects.filter(
                pk=job.pk,
                status__in=["complete", "failed"],
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


def enqueue_topic_note_job(topic: PrepTopic, level: str, source_signature: str) -> PrepTopicNotesJob | None:
    """Ensure this topic-level has a current job, recovering completed jobs with no published cache."""
    if not automatic_note_preparation_enabled():
        logger.info(
            "[Prep] Automatic note preparation is disabled; topic %s / %s was not queued.",
            topic.pk,
            level,
        )
        return None

    from prep.models import PrepNoteGenerationGuard

    job, created = PrepTopicNotesJob.objects.get_or_create(
        topic=topic,
        level=level,
        source_signature=source_signature,
        defaults={"status": "pending"},
    )
    should_retry = (
        job.status == "complete"
        and not _has_current_topic_note_cache(topic, level, source_signature)
    )
    if job.status == "failed":
        guard = PrepNoteGenerationGuard.objects.filter(
            topic=topic,
            level=level,
            source_signature=source_signature,
        ).first()
        should_retry = not guard or guard.status != "needs_review"
    if not created and should_retry:
        PrepTopicNotesJob.objects.filter(
            pk=job.pk,
            status=job.status,
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
        job.refresh_from_db()
    return job


def process_single_topic_notes_job(job: PrepTopicNotesJob) -> bool:
    """
    Generate, validate, and persist notes for one specific PrepTopicNotesJob.
    """
    if not automatic_note_preparation_enabled():
        logger.info(
            "[Prep] Automatic note preparation is disabled; job %s was not processed.",
            job.pk,
        )
        return False

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
    topic.refresh_from_db(fields=["title", "summary", "subtopics", "content_rules", "content_rules_version"])
    topic.course.refresh_from_db(fields=["study_profile", "study_profile_version"])
    if _supersede_stale_topic_notes_job(
        job,
        topic,
        _topic_notes_cache_signature(
            topic.course,
            topic,
            topic.title,
            topic.subtopics if isinstance(topic.subtopics, list) else [],
        ),
    ):
        return False

    result = get_or_generate_topic_notes(
        topic.course.code,
        topic.title,
        subtopics=topic.subtopics if isinstance(topic.subtopics, list) else [],
        level=job.level,
        course_obj=topic.course,
        topic_obj=topic,
    )
    topic.refresh_from_db(fields=["title", "summary", "subtopics", "content_rules", "content_rules_version"])
    topic.course.refresh_from_db(fields=["study_profile", "study_profile_version"])
    if _supersede_stale_topic_notes_job(
        job,
        topic,
        _topic_notes_cache_signature(
            topic.course,
            topic,
            topic.title,
            topic.subtopics if isinstance(topic.subtopics, list) else [],
        ),
    ):
        return False

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
    acceptable_review_statuses = {"passed", "skipped", None}
    if review_status not in acceptable_review_statuses:
        raise RuntimeError(
            "The notes worker rejected notes without a successful independent review: "
            + str(review_status)
        )
    if not result.get("cached") and review_status and review_status not in acceptable_review_statuses:
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
        level=job.level,
        **validation_options,
    )
    if validation_issues:
        raise RuntimeError(
            "The notes worker rejected unvalidated content: "
            + "; ".join(validation_issues)
        )
    if not _has_current_topic_note_cache(topic, job.level, job.source_signature):
        raise RuntimeError(
            "The notes worker did not find a validated cache entry for the current topic source."
        )

    # Level 2 (Core Concepts) notes are 100% free for all students.
    # Level 1 and Level 3 are charged flat on-demand token spending upon note fetch.
    # Background worker precompute costs are absorbed by the platform.

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
    from django.core.cache import cache
    cache.delete(f"prep_pub_levels_{topic.pk}_True")
    cache.delete(f"prep_pub_levels_{topic.pk}_False")
    if topic.course:
        cache.delete(f"prep_course_topics_summary_v4_{topic.course.pk}")
    try:
        enqueue_topic_pdf_artifact(topic, "notes", job.level)
    except Exception:
        pass
    return True


def _has_current_topic_note_cache(topic: PrepTopic, level: str, source_signature: str) -> bool:
    from services.prep_ai_router import _topic_notes_cache_signature, get_published_topic_note_levels

    current_signature = _topic_notes_cache_signature(
        topic.course,
        topic,
        topic.title,
        topic.subtopics,
    )
    return (
        current_signature == source_signature
        and level in get_published_topic_note_levels(topic, validated_only=True)
    )


def _recover_valid_cached_topic_notes_job(job: PrepTopicNotesJob, topic: PrepTopic, current_signature: str) -> bool:
    """Treat a stale job as complete when a current validated cache already exists."""
    if current_signature == job.source_signature:
        return False
    if not _has_current_topic_note_cache(topic, job.level, current_signature):
        return False

    existing_current_sig = PrepTopicNotesJob.objects.filter(
        topic=job.topic,
        level=job.level,
        source_signature=current_signature,
    ).exclude(pk=getattr(job, "pk", None)).exists()

    if not existing_current_sig:
        job.source_signature = current_signature
        update_fields = ["source_signature", "status", "completed_at", "last_error"]
    else:
        update_fields = ["status", "completed_at", "last_error"]

    job.status = "complete"
    job.completed_at = timezone.now()
    job.last_error = ""
    job.save(update_fields=update_fields)
    return True


def _supersede_stale_topic_notes_job(job: PrepTopicNotesJob, topic: PrepTopic, current_signature: str) -> bool:
    if current_signature == job.source_signature:
        return False
    if _recover_valid_cached_topic_notes_job(job, topic, current_signature):
        return True
    job.status = "failed"
    job.completed_at = timezone.now()
    job.last_error = "Superseded because the approved topic source changed during note preparation."
    job.save(update_fields=["status", "completed_at", "last_error"])
    enqueue_course_topic_note_jobs(topic.course)
    return True


def process_course_notes_in_background(course_id: int):
    """Background worker thread function that runs through all pending jobs for a course."""
    if not automatic_note_preparation_enabled():
        logger.info(
            "[Prep] Automatic note preparation is disabled; course %s was not processed.",
            course_id,
        )
        return

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
                completed = process_single_topic_notes_job(job)
                if completed:
                    logger.info("Auto-worker generated %s notes for topic %s (%s)", job.level, job.topic_id, job.topic.title)
                else:
                    logger.info("Auto-worker superseded stale %s note job for topic %s", job.level, job.topic_id)
            except Exception as exc:
                logger.warning("Auto-worker error for note job %s topic %s: %s", job.id, job.topic_id, exc)
                job.status = "pending" if job.attempts < 3 else "failed"
                job.last_error = str(exc)[:4000]
                job.completed_at = timezone.now() if job.status == "failed" else None
                job.save(update_fields=["status", "last_error", "completed_at"])

        # Mark course precompute job complete if all jobs are complete
        all_jobs = PrepTopicNotesJob.objects.filter(topic__course=course)
        if all_jobs.exists() and not all_jobs.exclude(status="complete").exists():
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
