import logging
import time

from django.core.management.base import BaseCommand
from django.db import OperationalError, close_old_connections, connection

from prep.models import PrepTopicPdfArtifact
from services.prep_pdf_artifacts import enqueue_existing_topic_pdf_artifacts, process_next_pdf_artifact


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generate versioned topic PDF artifacts in the isolated PDF worker."

    def add_arguments(self, parser):
        parser.add_argument("--once", action="store_true", help="Process available jobs, then exit.")
        parser.add_argument("--poll-seconds", type=float, default=5.0)
        parser.add_argument(
            "--reconcile-seconds",
            type=float,
            default=900.0,
            help="Rescan published notes and questions for missing or stale artifacts.",
        )
        parser.add_argument(
            "--skip-initial-scan",
            action="store_true",
            help="Do not enqueue existing topic artifacts on worker startup.",
        )

    def handle(self, *args, **options):
        once = options["once"]
        poll_seconds = max(1.0, options["poll_seconds"])
        reconcile_seconds = max(60.0, options["reconcile_seconds"])
        self._wait_for_job_table(once, poll_seconds)
        initial_scan_complete = options["skip_initial_scan"]
        next_reconciliation = (
            time.monotonic() + reconcile_seconds
            if initial_scan_complete
            else 0.0
        )

        while True:
            close_old_connections()
            if not initial_scan_complete or time.monotonic() >= next_reconciliation:
                try:
                    queued = enqueue_existing_topic_pdf_artifacts()
                    self.stdout.write(
                        f"Reconciled published topic PDFs; queued {queued} missing or stale artifact(s)."
                    )
                    initial_scan_complete = True
                    next_reconciliation = time.monotonic() + reconcile_seconds
                except Exception:
                    if once:
                        raise
                    logger.exception("Topic PDF reconciliation failed; retrying after the poll interval.")
                    time.sleep(poll_seconds)
                    continue
            try:
                processed = process_next_pdf_artifact()
            except OperationalError:
                if once:
                    raise
                logger.exception("Database error in the PDF worker.")
                processed = False

            if processed:
                continue
            if once:
                return
            time.sleep(poll_seconds)

    def _wait_for_job_table(self, once, poll_seconds):
        table_name = PrepTopicPdfArtifact._meta.db_table
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
            logger.error("PDF worker is waiting for database readiness: %s", error)
            time.sleep(poll_seconds)
