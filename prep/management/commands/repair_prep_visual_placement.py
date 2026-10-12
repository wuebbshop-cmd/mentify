"""Re-anchor approved source figures in one shared topic without AI generation."""

from django.core.management.base import BaseCommand, CommandError

from prep.models import PrepContentCache, PrepTopic
from services.prep_ai_router import (
    NOTE_VALIDATION_STATE,
    _note_completion_issues,
    _note_validation_options,
    _topic_notes_cache_signature,
    normalize_approved_visual_placement,
)
from services.prep_blocks import parse_markdown_to_blocks


class Command(BaseCommand):
    help = (
        "Re-anchor approved source images for one topic. Runs without an AI call "
        "and preserves the existing note text, equations, and headings."
    )

    def add_arguments(self, parser):
        parser.add_argument("--topic-id", type=int, required=True)
        parser.add_argument("--apply", action="store_true")

    def handle(self, *args, **options):
        try:
            topic = PrepTopic.objects.select_related("course").get(pk=options["topic_id"])
        except PrepTopic.DoesNotExist as exc:
            raise CommandError(f"Topic {options['topic_id']} does not exist.") from exc

        validation_options = _note_validation_options(
            topic.course,
            topic.title,
            topic.summary,
            topic.subtopics,
            topic_obj=topic,
        )
        source_references = validation_options["source_references"]
        signature = _topic_notes_cache_signature(
            topic.course, topic, topic.title, topic.subtopics
        )
        entries = PrepContentCache.objects.filter(
            topic=topic, content_type="topic_notes"
        ).order_by("-updated_at", "-id")
        latest_by_level = {}
        for entry in entries:
            payload = entry.payload if isinstance(entry.payload, dict) else {}
            level = str(payload.get("level") or "level_2")
            latest_by_level.setdefault(level, entry)

        if not latest_by_level:
            raise CommandError(f"{topic}: no cached note levels found.")

        changed = 0
        for level, entry in sorted(latest_by_level.items()):
            payload = dict(entry.payload) if isinstance(entry.payload, dict) else {}
            original = str(payload.get("content") or payload.get("notes") or "").strip()
            if not original:
                self.stdout.write(self.style.WARNING(f"{level}: skipped empty content"))
                continue
            updated = normalize_approved_visual_placement(original, source_references)
            issues = _note_completion_issues(
                updated, topic.title, **validation_options
            )
            if issues:
                raise CommandError(
                    f"{topic} {level}: placement repair failed validation: {'; '.join(issues)}"
                )
            old_images = original.count("![")
            new_images = updated.count("![")
            self.stdout.write(
                f"{level}: images {old_images} -> {new_images}; "
                f"{'changed' if updated != original else 'unchanged'}"
            )
            if options["apply"] and updated != original:
                payload.update({
                    "content": updated,
                    "blocks": parse_markdown_to_blocks(updated),
                    "source_references": source_references,
                    "source_signature": signature,
                    "validation_state": NOTE_VALIDATION_STATE,
                })
                entry.payload = payload
                entry.save(update_fields=["payload", "updated_at"])
                changed += 1

        mode = "applied" if options["apply"] else "dry run"
        self.stdout.write(self.style.SUCCESS(f"{topic}: {mode}; {changed} level(s) updated."))
