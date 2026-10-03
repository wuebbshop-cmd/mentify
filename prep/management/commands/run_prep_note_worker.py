import time
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import OperationalError, transaction
from django.utils import timezone

from prep.models import PrepNotePrecomputeJob, PrepTopic


class Command(BaseCommand):
    help = "Prepare shared Level 2 course notes from the durable publication queue."

    def add_arguments(self, parser):
        parser.add_argument("--once", action="store_true", help="Process available jobs, then exit.")
        parser.add_argument("--poll-seconds", type=float, default=5.0)

    def handle(self, *args, **options):
        once = options["once"]
        poll_seconds = max(1.0, options["poll_seconds"])
        while True:
            try:
                self._recover_stale_jobs()
                job = self._claim_job()
            except OperationalError:
                if once:
                    raise
                time.sleep(poll_seconds)
                continue
            if not job:
                if once:
                    return
                time.sleep(poll_seconds)
                continue
            self._process_job(job)

    def _recover_stale_jobs(self):
        cutoff = timezone.now() - timedelta(minutes=30)
        PrepNotePrecomputeJob.objects.filter(
            status="running",
            started_at__lt=cutoff,
        ).update(status="pending", started_at=None)

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

    def _process_job(self, job):
        from services.prep_ai_router import (
            _topic_notes_cache_signature,
            get_or_generate_topic_notes,
        )
        from services.credit_service import credits_for_usage
        from services.prep_course_billing import create_shared_course_cost, settle_course_cost_share

        try:
            course = job.course
            topics = PrepTopic.objects.filter(course=course, is_active=True).order_by("order", "id")
            for topic in topics.iterator():
                job.started_at = timezone.now()
                job.save(update_fields=["started_at"])
                result = get_or_generate_topic_notes(
                    course.code,
                    topic.title,
                    subtopics=topic.subtopics if isinstance(topic.subtopics, list) else [],
                    level="level_2",
                    course_obj=course,
                    topic_obj=topic,
                )
                notes = str(result.get("notes") or result.get("content") or "").strip()
                if not notes:
                    raise RuntimeError(result.get("error") or f"No validated Level 2 notes for {topic.title}.")

                if not result.get("cached"):
                    usage = result.get("usage") or {}
                    cost_credits = credits_for_usage(usage, minimum=1)
                    signature = _topic_notes_cache_signature(
                        course,
                        topic,
                        topic.title,
                        topic.subtopics,
                    )
                    cost = create_shared_course_cost(
                        course=course,
                        cost_type="topic_notes",
                        total_credits=cost_credits,
                        source_key=f"topic-notes:{topic.pk}:level_2:{signature}",
                        topic=topic,
                        level="level_2",
                        usage=usage,
                        model_name=result.get("model") or "deepseek-chat",
                    )
                    for share in cost.shares.select_related("user", "cost").all():
                        settle_course_cost_share(share)

            job.status = "complete"
            job.completed_at = timezone.now()
            job.save(update_fields=["status", "completed_at", "last_error"])
            self.stdout.write(self.style.SUCCESS(f"Prepared Level 2 notes for {course.code}."))
        except Exception as exc:
            job.last_error = str(exc)[:4000]
            job.status = "pending" if job.attempts < 3 else "failed"
            job.save(update_fields=["status", "last_error"])
            self.stderr.write(self.style.ERROR(f"Level 2 precompute failed for {job.course.code}: {exc}"))