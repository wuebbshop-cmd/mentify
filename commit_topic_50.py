import json
import os
import re
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
import django
django.setup()

from django.db import transaction
from django.utils import timezone
from prep.models import (
    PrepContentCache,
    PrepCourse,
    PrepNoteGenerationGuard,
    PrepNoteRepair,
    PrepTopic,
    PrepTopicNotesJob,
)
from services.prep_ai_router import (
    NOTE_VALIDATION_STATE,
    NOTES_CACHE_VERSION,
    _course_study_profile_version,
    _note_completion_issues,
    _note_validation_options,
    _required_note_sections,
    _topic_content_rules_version,
    _topic_notes_cache_signature,
    compute_cache_key,
    compute_prompt_hash,
    get_published_topic_note_levels,
    normalize_math_delimiters,
)

base = Path(__file__).parent
content = (base / "topic_50_level_2_candidate.md").read_text(encoding="utf-8")
export = json.loads((base / "topic_50_prompt_data.json").read_text(encoding="utf-8"))
course = PrepCourse.objects.get(code=export["course"]["code"])
topic = PrepTopic.objects.get(pk=export["topic"]["id"], course=course)
level = export["level"]
options = _note_validation_options(
    course, topic.title, topic.summary, topic.subtopics, topic_obj=topic
)
issues = _note_completion_issues(content, topic.title, **options)
profile = export["course_study_profile"]
required_sections = [
    f"## {index}. {title}"
    for index, title in enumerate(profile.get("note_structure", []), start=1)
]
actual_sections = [line for line in content.splitlines() if line.startswith("## ")]
if issues:
    raise RuntimeError(f"Refusing to commit invalid note: {issues}")
if actual_sections != required_sections:
    raise RuntimeError("Refusing to commit: headings differ from the exported course profile.")
if options["allow_code"] is False and "```" in content:
    raise RuntimeError("Refusing to commit code blocks for a no-code topic.")
if re.search(r"\\\\[A-Za-z]", content):
    raise RuntimeError("Refusing to commit a matrix row separator adjacent to a LaTeX command.")

signature = _topic_notes_cache_signature(
    course, topic, topic.title, topic.subtopics
)
cache_key = compute_cache_key(
    "notes", NOTES_CACHE_VERSION, course.code, topic.title, level, signature
)
if signature != export["source_signature"] or cache_key != export["current_cache_key"]:
    raise RuntimeError("Refusing to commit: source signature or cache key changed since export.")

active_jobs = PrepTopicNotesJob.objects.filter(
    topic=topic,
    level=level,
    source_signature=signature,
    status__in=["pending", "running"],
)
if active_jobs.exists():
    raise RuntimeError("Refusing to commit while a current-signature note job is active.")
if PrepNoteGenerationGuard.objects.filter(
    topic=topic, level=level, source_signature=signature
).exists():
    raise RuntimeError("Refusing to commit while a current-signature generation guard exists.")

entry = PrepContentCache.objects.filter(
    cache_key=cache_key, topic=topic, content_type="topic_notes"
).first()
if not entry:
    raise RuntimeError("Refusing to commit: the exported target cache row no longer exists.")
old_payload = entry.payload if isinstance(entry.payload, dict) else {}
old_content = str(old_payload.get("content") or old_payload.get("notes") or "")
if old_payload.get("model") != "Manual Offline Source-Grounded Notes":
    raise RuntimeError("Refusing to overwrite a note not authored by this manual workflow.")
if len(old_content) < 15000:
    raise RuntimeError(
        f"Refusing to overwrite an unexpectedly short manual row ({len(old_content)} characters)."
    )

repair = PrepNoteRepair.objects.filter(
    topic=topic,
    level=level,
    source_signature=signature,
    cache_key=cache_key,
).first()
if not repair:
    raise RuntimeError("Refusing to commit without the exported repair record.")

payload = {
    "content": content,
    "blocks": None,
    "schema_version": 2,
    "level": level,
    "model": "Manual Offline Source-Grounded Notes",
    "validation_state": NOTE_VALIDATION_STATE,
    "validated_at": timezone.now().isoformat(),
    "source_signature": signature,
    "study_profile_version": _course_study_profile_version(course),
    "topic_content_rules_version": _topic_content_rules_version(topic),
    "source_references": options["source_references"],
    "review_status": "manual_source_verified",
}

with transaction.atomic():
    entry.payload = payload
    entry.prompt_hash = compute_prompt_hash(
        course.code, topic.title, level, "manual-offline-source-grounded", content
    )
    entry.save(update_fields=["payload", "prompt_hash", "updated_at"])
    PrepNoteRepair.objects.filter(pk=repair.pk).update(
        current_content=content,
        validation_issues=[],
        status="validated",
        last_error="",
        updated_at=timezone.now(),
    )
    current_levels = get_published_topic_note_levels(topic, validated_only=True)
    expected_served = normalize_math_delimiters(content).strip()
    if current_levels.get(level) != expected_served:
        raise RuntimeError("App publication check did not return the committed note.")

published = get_published_topic_note_levels(topic, validated_only=True).get(level, "")
print("COMMITTED", course.code, "Topic", topic.pk, topic.title, level)
print("OLD_CHARACTERS", len(old_content), "NEW_CHARACTERS", len(content))
print("PUBLISHED_CHARACTERS", len(published), "VALIDATION_ISSUES", len(issues))
print("MODEL", payload["model"], "REVIEW_STATUS", payload["review_status"])
