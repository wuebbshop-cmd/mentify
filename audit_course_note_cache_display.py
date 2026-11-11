"""Generate a read-only worklist of note levels not currently displayable."""

from __future__ import annotations

import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django

django.setup()

from prep.models import PrepContentCache, PrepCourse
from services.prep_ai_router import (
    NOTE_VALIDATION_STATE,
    _cache_payload_as_dict,
    _course_study_profile_version,
    _topic_content_rules_version,
    _topic_notes_cache_signature,
)

OUT = os.path.join(BASE_DIR, "course_note_cache_display_audit.md")
LEVELS = ("level_1", "level_2", "level_3")


def ready_levels(topic) -> set[str]:
    """Return current validated levels without revalidating or changing cache rows."""
    signature = _topic_notes_cache_signature(
        topic.course, topic, topic.title, topic.subtopics
    )
    profile_version = _course_study_profile_version(topic.course)
    rules_version = _topic_content_rules_version(topic)
    available: set[str] = set()

    entries = PrepContentCache.objects.filter(
        topic=topic, content_type="topic_notes"
    ).order_by("-updated_at", "-id")
    for entry in entries:
        payload = _cache_payload_as_dict(entry.payload)
        level = str(payload.get("level") or "level_2")
        if level not in LEVELS or level in available:
            continue
        if payload.get("validation_state") != NOTE_VALIDATION_STATE:
            continue
        if str(payload.get("source_signature") or "") != signature:
            continue
        if int(payload.get("study_profile_version", 0) or 0) != profile_version:
            continue
        if int(payload.get("topic_content_rules_version", 0) or 0) != rules_version:
            continue
        content = str(payload.get("content") or payload.get("notes") or "").strip()
        if content:
            available.add(level)
    return available


def main() -> None:
    lines: list[str] = []
    add = lines.append
    courses = list(PrepCourse.objects.filter(topics__is_active=True).distinct().order_by("code"))
    topic_total = 0
    topic_complete = 0
    levels_ready = 0
    remaining: list[tuple[object, list[tuple[object, list[str]]]]] = []

    for course_index, course in enumerate(courses, start=1):
        print(f"auditing {course_index}/{len(courses)}: {course.code}", flush=True)
        missing_for_course: list[tuple[object, list[str]]] = []
        for topic in course.topics.filter(is_active=True).order_by("order", "id"):
            topic_total += 1
            available = ready_levels(topic)
            levels_ready += len(available)
            missing = [level for level in LEVELS if level not in available]
            if missing:
                missing_for_course.append((topic, missing))
            else:
                topic_complete += 1
        if missing_for_course:
            remaining.append((course, missing_for_course))

    remaining_topics = topic_total - topic_complete
    remaining_levels = topic_total * len(LEVELS) - levels_ready
    stamp = datetime.now(ZoneInfo("Africa/Nairobi")).strftime("%Y-%m-%d %H:%M EAT")

    add("# Remaining Course Note Display Worklist")
    add("")
    add(f"**Audit time:** {stamp}  ")
    add(
        "**Scope:** Active courses and topics in the local database. Courses and topics with all "
        "three validated, current note levels are deliberately omitted."
    )
    add(
        "**Method:** Read-only cache audit. A level is counted as displayable only when it has "
        "the current validation marker, source signature, course profile version, topic rule "
        "version and non-empty content. No cache record, job or question was changed."
    )
    add("")
    add("## Summary")
    add("")
    add(f"- Active courses checked: **{len(courses)}**")
    add(f"- Active topics checked: **{topic_total}**")
    add(f"- Topics complete at all three levels: **{topic_complete}**")
    add(f"- Remaining topics: **{remaining_topics}**")
    add(f"- Displayable note levels: **{levels_ready}** of **{topic_total * len(LEVELS)}**")
    add(f"- Remaining note levels: **{remaining_levels}**")
    add("")
    add("## Remaining Courses and Topics")
    add("")
    for course, rows in remaining:
        add(f"### {course.code} - {course.title}")
        add("")
        add("| Topic | Note levels still required |")
        add("|---|---|")
        for topic, missing in rows:
            labels = ", ".join(level.replace("level_", "Level ") for level in missing)
            add(f"| {topic.display_title} | {labels} |")
        add("")

    if not remaining:
        add("All active topics have validated notes at Levels 1, 2 and 3.")
        add("")

    with open(OUT, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines))

    print(
        f"wrote {OUT}: courses={len(courses)} topics={topic_total} "
        f"complete_topics={topic_complete} remaining_levels={remaining_levels}"
    )


if __name__ == "__main__":
    main()
