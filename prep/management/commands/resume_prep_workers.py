"""
prep/management/commands/resume_prep_workers.py

Single master command to resume and complete all pending or interrupted
Mentify Prep workers:
1. Topic Notes & Precompute Worker (run_prep_note_worker)
2. Past Paper Questions & Assessment Worker (run_prep_assessment_worker)
3. Downloadable PDF Artifacts Worker (run_prep_pdf_worker)
"""
import time
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection, close_old_connections

from prep.models import (
    PrepTopicNotesJob,
    PrepNotePrecomputeJob,
    PrepAssessmentIndexJob,
    PrepTopicPdfArtifact,
)


class Command(BaseCommand):
    help = "One-stop command to resume and complete all unfinished notes, past papers, and PDF worker jobs."

    def add_arguments(self, parser):
        parser.add_argument(
            "--watch",
            action="store_true",
            help="Keep running continuously in the background instead of exiting when current queue finishes.",
        )
        parser.add_argument(
            "--poll-seconds",
            type=float,
            default=5.0,
            help="Polling delay between cycles in watch mode.",
        )

    def handle(self, *args, **options):
        watch = options.get("watch", False)
        poll_seconds = max(1.0, options.get("poll_seconds", 5.0))

        self.stdout.write(self.style.SUCCESS("=" * 70))
        self.stdout.write(self.style.SUCCESS("  MENTIFY PREP MASTER WORKER RESUME"))
        self.stdout.write(self.style.SUCCESS("=" * 70))

        while True:
            close_old_connections()

            # Check queue counts
            pending_notes = PrepTopicNotesJob.objects.filter(status__in=["pending", "processing", "queued"]).count()
            pending_precompute = PrepNotePrecomputeJob.objects.filter(status__in=["pending", "processing", "queued"]).count()
            pending_assessments = PrepAssessmentIndexJob.objects.filter(status__in=["pending", "processing", "queued"]).count()
            pending_pdfs = PrepTopicPdfArtifact.objects.filter(status__in=["pending", "processing", "queued"]).count()

            total_pending = pending_notes + pending_precompute + pending_assessments + pending_pdfs

            self.stdout.write(
                f"\n[Status] Current Pending Jobs: "
                f"Notes={pending_notes + pending_precompute} | "
                f"Past Papers={pending_assessments} | "
                f"PDFs={pending_pdfs}"
            )

            # Step 1: Resume and process Topic Notes
            if pending_notes + pending_precompute > 0 or watch:
                self.stdout.write(self.style.WARNING("--> [1/3] Processing Notes Queue..."))
                try:
                    call_command("run_prep_note_worker", once=True)
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Notes worker error: {e}"))

            # Step 2: Resume and process Past Paper Assessment Questions
            if pending_assessments > 0 or watch:
                self.stdout.write(self.style.WARNING("--> [2/3] Processing Past Paper Questions Queue..."))
                try:
                    call_command("run_prep_assessment_worker", once=True)
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Assessment worker error: {e}"))

            # Step 3: Resume and process PDF Artifacts
            if pending_pdfs > 0 or watch:
                self.stdout.write(self.style.WARNING("--> [3/3] Processing PDF Artifacts Queue..."))
                try:
                    call_command("run_prep_pdf_worker", once=True)
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"PDF worker error: {e}"))

            close_old_connections()
            rem_notes = PrepTopicNotesJob.objects.filter(status__in=["pending", "processing", "queued"]).count()
            rem_precompute = PrepNotePrecomputeJob.objects.filter(status__in=["pending", "processing", "queued"]).count()
            rem_assessments = PrepAssessmentIndexJob.objects.filter(status__in=["pending", "processing", "queued"]).count()
            rem_pdfs = PrepTopicPdfArtifact.objects.filter(status__in=["pending", "processing", "queued"]).count()
            rem_total = rem_notes + rem_precompute + rem_assessments + rem_pdfs

            if not watch:
                self.stdout.write(self.style.SUCCESS("\n" + "=" * 70))
                self.stdout.write(
                    self.style.SUCCESS(
                        f"  COMPLETED BATCH: Finished {max(0, total_pending - rem_total)} job(s). Remaining: {rem_total}"
                    )
                )
                self.stdout.write(self.style.SUCCESS("=" * 70))
                break

            time.sleep(poll_seconds)
