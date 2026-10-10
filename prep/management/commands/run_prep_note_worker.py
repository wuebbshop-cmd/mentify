import time
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import OperationalError, close_old_connections, connection, transaction
from django.db.models import Case, Exists, OuterRef, Q, Value, When
from django.utils import timezone

from prep.models import PrepNotePrecomputeJob, PrepTopic, PrepTopicNotesJob


class Command(BaseCommand):
    help = "Prepare all shared note levels from the durable publication queue."

    def add_arguments(self, parser):
        parser.add_argument("--once", action="store_true", help="Process available jobs, then exit.")
        parser.add_argument("--poll-seconds", type=float, default=5.0)

    def handle(self, *args, **options):
        once = options["once"]
        poll_seconds = max(1.0, options["poll_seconds"])
        last_expiry_sweep = 0.0
        while True:
            if not connection.in_atomic_block:
                close_old_connections()
            try:
                if time.time() - last_expiry_sweep >= 3600:
                    self._expire_due_credits()
                    last_expiry_sweep = time.time()
                self._recover_stale_jobs()
                notes_job = self._claim_topic_notes_job()
                job = None if notes_job else self._claim_job()
            except OperationalError:
                if once:
                    raise
                time.sleep(poll_seconds)
                continue
            if notes_job:
                try:
                    self._process_topic_notes_job(notes_job)
                except Exception as exc:
                    self.stderr.write(
                        self.style.ERROR(f"Unexpected worker error for notes job {notes_job.id}: {exc}")
                    )
                continue
            if not job:
                if once:
                    return
                time.sleep(poll_seconds)
                continue
            try:
                self._process_job(job)
            except Exception as exc:
                self.stderr.write(
                    self.style.ERROR(f"Unexpected error processing course precompute job {job.id}: {exc}")
                )

    def _expire_due_credits(self):
        from prep.models import PrepWallet
        from services.credit_service import expire_wallet_credits

        for wallet in PrepWallet.objects.all().iterator():
            expire_wallet_credits(wallet)

    def _recover_stale_jobs(self):
        cutoff = timezone.now() - timedelta(minutes=30)
        PrepNotePrecomputeJob.objects.filter(
            status="running",
            started_at__lt=cutoff,
        ).update(status="pending", started_at=None)
        PrepTopicNotesJob.objects.filter(
            status="running",
            started_at__lt=cutoff,
        ).update(status="pending", started_at=None)

    def _claim_topic_notes_job(self):
        completed_level_two = PrepTopicNotesJob.objects.filter(
            topic_id=OuterRef("topic_id"),
            level="level_2",
            source_signature=OuterRef("source_signature"),
            status="complete",
        )
        with transaction.atomic():
            job = (
                PrepTopicNotesJob.objects.select_for_update(skip_locked=True)
                .filter(status="pending")
                .annotate(level_two_complete=Exists(completed_level_two))
                .exclude(Q(level__in=["level_1", "level_3"]) & Q(level_two_complete=False))
                .order_by(
                    Case(
                        When(level="level_2", then=Value(0)),
                        When(level="level_1", then=Value(1)),
                        default=Value(2),
                    ),
                    "queued_at",
                    "id",
                )
                .first()
            )
            if not job:
                return None
            job.status = "running"
            job.attempts += 1
            job.started_at = timezone.now()
            job.last_error = ""
            job.save(update_fields=["status", "attempts", "started_at", "last_error"])
            return job

    def _claim_job(self):
        with transaction.atomic():
            job = (
                PrepNotePrecomputeJob.objects.select_for_update(skip_locked=True)
                .filter(status="pending")
                .order_by("queued_at", "id")
                .first()
            )
            if not job:
                return None
            job.status = "running"
            job.attempts += 1
            job.started_at = timezone.now()
            job.last_error = ""
            job.save(update_fields=["status", "attempts", "started_at", "last_error"])
            return job

    @staticmethod
    def _save_job_resilient(job, update_fields):
        if not connection.in_atomic_block:
            close_old_connections()
        try:
            job.save(update_fields=update_fields)
        except OperationalError:
            if not connection.in_atomic_block:
                close_old_connections()
            job.save(update_fields=update_fields)

    def _process_job(self, job):
        try:
            from services.prep_note_precompute import enqueue_course_topic_note_jobs

            queued = enqueue_course_topic_note_jobs(job.course)
            job.status = "complete"
            job.completed_at = timezone.now()
            job.last_error = ""
            self._save_job_resilient(job, update_fields=["status", "completed_at", "last_error"])
            self.stdout.write(
                self.style.SUCCESS(
                    f"Queued all-level note preparation for {job.course.code} "
                    f"({queued} topic-level jobs)."
                )
            )
        except Exception as exc:
            job.last_error = str(exc)[:4000]
            job.status = "pending" if job.attempts < 3 else "failed"
            try:
                self._save_job_resilient(job, update_fields=["status", "last_error"])
            except Exception as save_err:
                self.stderr.write(self.style.ERROR(f"Failed to record error for {job.id}: {save_err}"))
            self.stderr.write(self.style.ERROR(f"Course notes precompute failed for {job.course.code}: {exc}"))

    def _process_topic_notes_job(self, job):
        from services.prep_ai_router import (
            _note_completion_issues,
            _note_validation_options,
            _topic_notes_cache_signature,
            get_or_generate_topic_notes,
        )
        from services.credit_service import credits_for_usage
        from services.prep_course_billing import create_shared_course_cost, settle_course_cost_share

        try:
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
            self._save_job_resilient(
                job,
                update_fields=[
                    "status",
                    "completed_at",
                    "last_error",
                    "provider_usage",
                    "model_name",
                ],
            )
            self.stdout.write(
                self.style.SUCCESS(f"Prepared {job.level} notes for topic {topic.pk}.")
            )
        except Exception as exc:
            job.status = "pending" if job.attempts < 3 else "failed"
            job.last_error = str(exc)[:4000]
            job.completed_at = timezone.now() if job.status == "failed" else None
            try:
                self._save_job_resilient(job, update_fields=["status", "last_error", "completed_at"])
            except Exception as save_err:
                self.stderr.write(
                    self.style.ERROR(
                        f"Failed to record topic job error for {job.id}: {save_err}"
                    )
                )
            self.stderr.write(
                self.style.ERROR(
                    f"Topic notes worker failed for topic {job.topic_id} ({job.level}): {exc}"
                )
            )