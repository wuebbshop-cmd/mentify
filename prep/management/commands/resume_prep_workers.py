"""
prep/management/commands/resume_prep_workers.py

Single master command to resume and complete all pending or interrupted
Mentify Prep workers:
1. Topic Notes & Precompute Worker (run_prep_note_worker)
2. Past Paper Questions & Assessment Worker (run_prep_assessment_worker)
3. Downloadable PDF Artifacts Worker (run_prep_pdf_worker)
"""
import sys
import threading
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

ACTIVE_STATUSES = ["pending", "processing", "queued"]


class Command(BaseCommand):
    help = "One-stop command to resume and complete all unfinished notes, past papers, and PDF worker jobs."

    # Job identities are printed before each step so the terminal shows what is being
    # worked on, and a heartbeat keeps printing while a worker call is in flight.
    def _queue_counts(self) -> dict:
        return {
            "notes": PrepTopicNotesJob.objects.filter(status__in=ACTIVE_STATUSES).count(),
            "precompute": PrepNotePrecomputeJob.objects.filter(status__in=ACTIVE_STATUSES).count(),
            "assessments": PrepAssessmentIndexJob.objects.filter(status__in=ACTIVE_STATUSES).count(),
            "pdfs": PrepTopicPdfArtifact.objects.filter(status__in=ACTIVE_STATUSES).count(),
        }

    def _counts_text(self, counts: dict) -> str:
        return (
            f"Notes={counts['notes'] + counts['precompute']} | "
            f"Past Papers={counts['assessments']} | "
            f"PDFs={counts['pdfs']}"
        )

    def _describe_queue(self, limit: int = 8) -> None:
        """Print one line per queued job so progress is identifiable, not just a count."""
        self.stdout.write("    queued work:")
        shown = 0
        try:
            for job in (
                PrepTopicNotesJob.objects.filter(status__in=ACTIVE_STATUSES)
                .select_related("topic", "topic__course")[:limit]
            ):
                topic = getattr(job, "topic", None)
                course = getattr(topic, "course", None)
                label = f"{getattr(course, 'code', '?')} | {str(getattr(topic, 'title', ''))[:38]}"
                self.stdout.write(
                    f"      - notes      job {job.pk}  {label}  "
                    f"level={getattr(job, 'level', '?')}  status={job.status}  "
                    f"attempts={getattr(job, 'attempts', 0)}"
                )
                shown += 1
            for job in (
                PrepNotePrecomputeJob.objects.filter(status__in=ACTIVE_STATUSES)
                .select_related("course")[: max(0, limit - shown)]
            ):
                self.stdout.write(
                    f"      - precompute job {job.pk}  course={getattr(job.course, 'code', '?')}  "
                    f"status={job.status}  attempts={getattr(job, 'attempts', 0)}"
                )
                shown += 1
            for job in (
                PrepAssessmentIndexJob.objects.filter(status__in=ACTIVE_STATUSES)[: max(0, limit - shown)]
            ):
                self.stdout.write(
                    f"      - past paper job {job.pk}  status={job.status}  "
                    f"attempts={getattr(job, 'attempts', 0)}"
                )
                shown += 1
            for job in (
                PrepTopicPdfArtifact.objects.filter(status__in=ACTIVE_STATUSES)[: max(0, limit - shown)]
            ):
                self.stdout.write(
                    f"      - pdf        job {job.pk}  status={job.status}  "
                    f"attempts={getattr(job, 'attempts', 0)}"
                )
                shown += 1
        except Exception as exc:  # never let reporting break the worker run
            self.stdout.write(f"      (queue detail unavailable: {exc})")
        remaining = sum(self._queue_counts().values()) - shown
        if remaining > 0:
            self.stdout.write(f"      ... and {remaining} more")

    def _run_step(self, label: str, command_name: str, poll_seconds: float) -> None:
        """Run one worker command, printing a heartbeat until it returns."""
        started = time.monotonic()
        stop = threading.Event()

        def heartbeat() -> None:
            while not stop.wait(max(5.0, poll_seconds)):
                elapsed = int(time.monotonic() - started)
                sys.stdout.write(f"      ... {label} worker still running ({elapsed}s elapsed)\n")
                sys.stdout.flush()

        thread = threading.Thread(target=heartbeat, daemon=True)
        thread.start()
        try:
            call_command(command_name, once=True)
        except Exception as exc:
            self.stderr.write(self.style.ERROR(f"    {label} worker error: {exc}"))
        finally:
            stop.set()
            thread.join(timeout=1)
            self.stdout.write(f"    {label} step finished in {int(time.monotonic() - started)}s")
            sys.stdout.flush()

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
        self.stdout.flush()

        cycle = 0
        while True:
            cycle += 1
            close_old_connections()

            counts = self._queue_counts()
            total_pending = sum(counts.values())
            self.stdout.write("")
            self.stdout.write(
                self.style.HTTP_INFO(
                    f"[Cycle {cycle}] {time.strftime('%H:%M:%S')} - pending: {self._counts_text(counts)}"
                )
            )
            if total_pending:
                self._describe_queue()
            self.stdout.flush()

            steps = (
                (1, "Notes", ("notes", "precompute"), "run_prep_note_worker", "Processing Notes Queue"),
                (2, "Past Papers", ("assessments",), "run_prep_assessment_worker", "Processing Past Paper Questions Queue"),
                (3, "PDFs", ("pdfs",), "run_prep_pdf_worker", "Processing PDF Artifacts Queue"),
            )
            for index, label, keys, command_name, description in steps:
                pending = sum(counts[key] for key in keys)
                if pending == 0 and not watch:
                    self.stdout.write(
                        self.style.WARNING(f"--> [{index}/3] {description}: queue empty, skipped")
                    )
                    continue
                self.stdout.write(
                    self.style.WARNING(f"--> [{index}/3] {description} ({pending} pending)")
                )
                self.stdout.flush()
                self._run_step(label, command_name, poll_seconds)

            close_old_connections()
            remaining = self._queue_counts()
            rem_total = sum(remaining.values())
            finished = max(0, total_pending - rem_total)
            self.stdout.write(
                self.style.SUCCESS(
                    f"    cycle {cycle} complete: {finished} job(s) finished, {rem_total} still queued "
                    f"({self._counts_text(remaining)})"
                )
            )

            if not watch:
                self.stdout.write(self.style.SUCCESS("=" * 70))
                self.stdout.write(
                    self.style.SUCCESS(f"  COMPLETED BATCH: Finished {finished} job(s). Remaining: {rem_total}")
                )
                self.stdout.write(self.style.SUCCESS("=" * 70))
                self.stdout.flush()
                break

            time.sleep(poll_seconds)
