import logging
import time
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import OperationalError, close_old_connections, connection, transaction
from django.utils import timezone

from prep.models import PrepAssessmentIndexJob
from services.prep_assessment_index import (
    assessment_source_signature,
    enqueue_assessment_index,
)


logger = logging.getLogger(__name__)
MAX_ATTEMPTS = 3
STALE_JOB_MINUTES = 30
MAX_RETRY_DELAY_MINUTES = 30


class Command(BaseCommand):
    help = "Index approved past-paper questions from the dedicated assessment queue."

    def add_arguments(self, parser):
        parser.add_argument("--once", action="store_true", help="Process available jobs, then exit.")
        parser.add_argument("--poll-seconds", type=float, default=5.0)

    def handle(self, *args, **options):
        once = options["once"]
        poll_seconds = max(1.0, options["poll_seconds"])
        self._wait_for_job_table(once, poll_seconds)
        while True:
            if not connection.in_atomic_block:
                close_old_connections()
            try:
                self._recover_stale_jobs()
                job = self._claim_job()
            except OperationalError:
                if once:
                    raise
                time.sleep(poll_seconds)
                continue
            if job:
                try:
                    self._process_job(job)
                except Exception as exc:
                    logger.exception("Assessment worker error for job %s: %s", getattr(job, "pk", None), exc)
                continue
            if once:
                return
            time.sleep(poll_seconds)

    def _wait_for_job_table(self, once, poll_seconds):
        table_name = PrepAssessmentIndexJob._meta.db_table
        while True:
            try:
                if table_name in connection.introspection.table_names():
                    return
                error = RuntimeError(
                    f"Required table {table_name} is missing; apply the prep migrations first."
                )
            except OperationalError as exc:
                error = exc
            if once:
                raise error
            logger.error("Assessment worker is waiting for database readiness: %s", error)
            time.sleep(poll_seconds)

    def _recover_stale_jobs(self):
        cutoff = timezone.now() - timedelta(minutes=STALE_JOB_MINUTES)
        now = timezone.now()
        stale = PrepAssessmentIndexJob.objects.filter(
            status="running",
            started_at__lt=cutoff,
        )
        stale.filter(attempts__lt=MAX_ATTEMPTS).update(
            status="pending",
            stage="retry_wait",
            started_at=None,
            next_attempt_at=now,
            last_error="Recovered after the assessment worker stopped during processing.",
        )
        stale.filter(attempts__gte=MAX_ATTEMPTS).update(
            status="failed",
            stage="failed",
            started_at=None,
            completed_at=now,
            last_error="The assessment worker stopped after exhausting the retry budget.",
        )

    def _claim_job(self):
        now = timezone.now()
        with transaction.atomic():
            job = (
                PrepAssessmentIndexJob.objects.select_for_update(skip_locked=True)
                .filter(status="pending", next_attempt_at__lte=now)
                .order_by("queued_at", "id")
                .first()
            )
            if job is None:
                return None
            job.status = "running"
            job.stage = "indexing"
            job.attempts += 1
            job.started_at = now
            job.last_error = ""
            job.save(update_fields=[
                "status", "stage", "attempts", "started_at", "last_error",
            ])
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
            paper = job.paper
            document = job.source_document
            current_signature = assessment_source_signature(document)
            if (
                document.stage != "stage_3"
                or current_signature != job.source_signature
                or paper.source_document_id != document.pk
            ):
                if document.stage == "stage_3" and paper.source_document_id == document.pk:
                    enqueue_assessment_index(
                        paper,
                        reconstruct_invalid=job.reconstruct_invalid,
                    )
                job.status = "superseded"
                job.stage = "superseded"
                job.completed_at = timezone.now()
                job.last_error = "The paper source changed after this job was queued."
                self._save_job_resilient(job, update_fields=[
                    "status", "stage", "completed_at", "last_error",
                ])
                return

            from services.prep_ingestion import index_assessment_questions
            from services.prep_solution_precompute import precompute_solutions_for_paper

            indexed = index_assessment_questions(
                document,
                paper,
                reconstruct_invalid=job.reconstruct_invalid,
            )

            # Precompute and verify solutions in the background without blocking or locking
            try:
                precompute_solutions_for_paper(paper, sleep_seconds=1.0)
            except Exception as sol_err:
                logger.warning(
                    "Background solution precomputation encountered error for paper %s: %s",
                    paper.pk,
                    sol_err,
                )

            if assessment_source_signature(document) != job.source_signature:
                enqueue_assessment_index(
                    paper,
                    reconstruct_invalid=job.reconstruct_invalid,
                )
                job.status = "superseded"
                job.stage = "superseded"
                job.completed_at = timezone.now()
                job.last_error = "The paper source changed while this job was processing."
                self._save_job_resilient(job, update_fields=[
                    "status", "stage", "completed_at", "last_error",
                ])
                return

            job.status = "complete"
            job.stage = "complete"
            job.indexed_questions = indexed
            job.completed_at = timezone.now()
            job.started_at = None
            job.last_error = ""
            self._save_job_resilient(job, update_fields=[
                "status", "stage", "indexed_questions", "completed_at",
                "started_at", "last_error",
            ])
            self.stdout.write(
                self.style.SUCCESS(
                    f"Indexed assessment paper {paper.pk}; {indexed} new question(s)."
                )
            )
        except Exception as exc:
            logger.exception("Assessment indexing job %s failed.", job.pk)
            retry_delay = min(2 ** job.attempts, MAX_RETRY_DELAY_MINUTES)
            job.last_error = str(exc)[:4000]
            job.started_at = None
            if job.attempts < MAX_ATTEMPTS:
                job.status = "pending"
                job.stage = "retry_wait"
                job.next_attempt_at = timezone.now() + timedelta(minutes=retry_delay)
            else:
                job.status = "failed"
                job.stage = "failed"
                job.completed_at = timezone.now()
            try:
                self._save_job_resilient(job, update_fields=[
                    "status", "stage", "last_error", "started_at",
                    "next_attempt_at", "completed_at",
                ])
            except Exception as save_err:
                logger.error("Failed to persist assessment job state for %s: %s", job.pk, save_err)
            self.stderr.write(
                self.style.ERROR(
                    f"Assessment indexing job {job.pk} failed "
                    f"(attempt {job.attempts}/{MAX_ATTEMPTS}): {exc}"
                )
            )
