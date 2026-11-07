from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import current_thread, main_thread

from django.core.management.base import BaseCommand
from django.core.cache import cache
from django.db import close_old_connections

from prep.models import PrepContentCache, PrepTopic
from services.prep_ai_router import (
    NOTE_VALIDATION_STATE,
    _cache_payload_as_dict,
    _course_study_profile_version,
    _note_validation_options,
    _revalidate_topic_note_cache_entry,
    _topic_content_rules_version,
    _topic_notes_cache_signature,
)


class Command(BaseCommand):
    help = "Revalidate cached topic notes against current course rules and refresh stale signatures."

    def add_arguments(self, parser):
        parser.add_argument("--course", help="Limit to a course code or numeric course ID.")
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Validate without changing note records or jobs.",
        )
        parser.add_argument(
            "--no-queue-invalid",
            action="store_true",
            help="Do not queue current-signature jobs for cached levels that fail validation.",
        )
        parser.add_argument(
            "--workers",
            type=int,
            default=4,
            help="Concurrent topic checks (1-8; default: 4).",
        )

    def handle(self, *args, **options):
        topics = (
            PrepTopic.objects.filter(
                is_active=True,
                cached_contents__content_type="topic_notes",
            )
            .select_related("course")
            .distinct()
            .order_by("course_id", "order", "id")
        )
        course_filter = options["course"]
        if course_filter:
            if course_filter.isdigit():
                topics = topics.filter(course_id=int(course_filter))
            else:
                topics = topics.filter(course__code__iexact=course_filter)

        dry_run = options["dry_run"]
        queue_invalid = not options["no_queue_invalid"] and not dry_run
        totals = {"checked": 0, "refreshed": 0, "passed": 0, "rejected": 0, "queued": 0}
        topic_ids = list(topics.values_list("id", flat=True))
        workers = max(1, min(8, options["workers"]))
        if workers == 1:
            for topic_id in topic_ids:
                result, messages = self._process_topic(
                    topic_id,
                    dry_run=dry_run,
                    queue_invalid=queue_invalid,
                )
                self._report_topic_result(topic_id, result, messages, totals)
        else:
            with ThreadPoolExecutor(max_workers=workers) as executor:
                futures = {
                    executor.submit(
                        self._process_topic,
                        topic_id,
                        dry_run=dry_run,
                        queue_invalid=queue_invalid,
                    ): topic_id
                    for topic_id in topic_ids
                }
                for future in as_completed(futures):
                    result, messages = future.result()
                    self._report_topic_result(futures[future], result, messages, totals)

        mode = "Dry run" if dry_run else "Applied"
        self.stdout.write(
            self.style.SUCCESS(
                f"{mode}: checked {totals['checked']} cache entries; "
                f"refreshed {totals['refreshed']}; passed {totals['passed']}; "
                f"rejected {totals['rejected']}; ensured {totals['queued']} current jobs are pending."
            )
        )

    def _report_topic_result(self, topic_id, result, messages, totals):
        for key in totals:
            totals[key] += result[key]
        for message in messages:
            self.stderr.write(message)
        self.stdout.write(
            f"Checked topic {topic_id} ({totals['checked']} cache entries so far)"
        )

    @staticmethod
    def _process_topic(topic_id, *, dry_run, queue_invalid):
        manage_connection = current_thread() is not main_thread()
        if manage_connection:
            close_old_connections()
        totals = {"checked": 0, "refreshed": 0, "passed": 0, "rejected": 0, "queued": 0}
        messages = []
        try:
            topic = PrepTopic.objects.select_related("course").get(pk=topic_id)
            signature = _topic_notes_cache_signature(
                topic.course, topic, topic.title, topic.subtopics
            )
            validation_options = None
            entries = PrepContentCache.objects.filter(
                content_type="topic_notes",
                topic=topic,
            ).order_by("-updated_at", "-id")
            published_levels = set()
            rejected_levels = {}
            for entry in entries:
                payload = _cache_payload_as_dict(entry.payload)
                if not payload or payload.get("review_status") == "skipped_no_source":
                    continue
                level = str(payload.get("level") or "level_2")
                if level not in {"level_1", "level_2", "level_3"}:
                    continue

                totals["checked"] += 1
                try:
                    cached_content = str(
                        payload.get("content") or payload.get("notes") or ""
                    ).strip()
                    metadata_current = (
                        payload.get("validation_state") == NOTE_VALIDATION_STATE
                        and payload.get("source_signature") == signature
                        and bool(cached_content)
                        and int(payload.get("study_profile_version", 0) or 0)
                        == _course_study_profile_version(topic.course)
                        and int(payload.get("topic_content_rules_version", 0) or 0)
                        == _topic_content_rules_version(topic)
                    )
                except (TypeError, ValueError):
                    metadata_current = False

                if metadata_current:
                    published_levels.add(level)
                    totals["passed"] += 1
                    continue

                if validation_options is None:
                    validation_options = _note_validation_options(
                        topic.course,
                        topic.title,
                        topic.summary,
                        topic.subtopics,
                        topic_obj=topic,
                    )

                refreshed, issues = _revalidate_topic_note_cache_entry(
                    entry,
                    payload,
                    topic,
                    signature,
                    validation_options=validation_options,
                    persist=not dry_run and not metadata_current,
                )
                if refreshed:
                    published_levels.add(level)
                    totals["passed"] += 1
                    if not metadata_current:
                        totals["refreshed"] += 1
                else:
                    rejected_levels.setdefault(level, issues)
                    totals["rejected"] += 1
                    messages.append(
                        f"Rejected {topic.course.code} / {topic.title} / {level}: "
                        + "; ".join(issues)
                    )

            for level, issues in rejected_levels.items():
                if level in published_levels:
                    continue
                if queue_invalid:
                    from services.prep_note_precompute import enqueue_topic_note_job

                    job = enqueue_topic_note_job(topic, level, signature)
                    if job and job.status == "pending":
                        totals["queued"] += 1
                elif dry_run:
                    messages.append(
                        f"Would queue {topic.course.code} / {topic.title} / {level} "
                        "for current-source generation."
                    )

            if not dry_run:
                cache.delete(f"prep_pub_levels_{topic.pk}_True")
                cache.delete(f"prep_pub_levels_{topic.pk}_False")
            return totals, messages
        finally:
            if manage_connection:
                close_old_connections()
