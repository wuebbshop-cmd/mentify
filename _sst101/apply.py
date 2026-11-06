"""Validate rebuilt SST 101 notes and publish them into the existing note cache.

Usage:
    python _sst101/apply.py 140_level_2 140_level_1 ...
    python _sst101/apply.py --all

Each argument is a ``<topic_pk>_<level>`` key whose Markdown lives in
``_sst101/new/<key>.md``.  The script refreshes the existing cache row in place
(or creates the missing one) only after the note passes the same validation the
app applies, so a failing note never becomes visible to learners.
"""

from __future__ import annotations

import copy
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
os.chdir(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django

django.setup()

from django.core.cache import cache
from django.utils import timezone

from prep.models import PrepContentCache, PrepCourse, PrepTopic
from services import prep_ai_router as router
from services.prep_blocks import parse_markdown_to_blocks, validate_structured_blocks

COURSE_PK = 40
LEVELS = ("level_1", "level_2", "level_3")
MIN_WORDS = 5000
NEW_DIR = os.path.join(os.path.dirname(__file__), "new")


def current_rows(course):
    rows = {}
    for row in PrepContentCache.objects.filter(
        content_type="topic_notes", topic__course=course
    ).order_by("topic_id", "-updated_at", "-id"):
        payload = row.payload if isinstance(row.payload, dict) else {}
        level = payload.get("level") or "level_2"
        if level in LEVELS and (row.topic_id, level) not in rows:
            rows[(row.topic_id, level)] = row
    return rows


def validate(course, topic, level, content):
    options = router._note_validation_options(course, topic.title, topic_obj=topic)
    issues = router._note_completion_issues(content, topic.title, level=level, **options)
    blocks = parse_markdown_to_blocks(content)
    blocks_ok, block_message = validate_structured_blocks(blocks)
    words = len(content.split())
    problems = list(issues)

    # The reader gate re-validates the *normalized* content, which can differ from
    # the source (for example "\$" currency escapes break delimiter pairing). Check
    # the same way the gate does so a note cannot be saved but never displayed.
    normalized = router.normalize_math_delimiters(content).strip()
    if normalized != content.strip():
        normalized_issues = router._note_completion_issues(
            normalized, topic.title, level=level, **options
        )
        problems.extend(
            f"after math normalization: {issue}" for issue in normalized_issues
        )
    if "\\$" in content:
        problems.append(r"contains the escaped dollar \$ which breaks math delimiter pairing")

    if not blocks_ok:
        problems.append(f"structured blocks invalid: {block_message}")
    if words < MIN_WORDS:
        problems.append(f"only {words} words; at least {MIN_WORDS} are required")
    return problems, blocks


def check_key(course, key):
    topic_pk, level = key.split("_", 1)
    topic = PrepTopic.objects.get(pk=int(topic_pk), course=course)
    path = os.path.join(NEW_DIR, f"{key}.md")
    with open(path, encoding="utf-8") as handle:
        content = handle.read().replace("\r\n", "\n").strip() + "\n"
    problems, blocks = validate(course, topic, level, content)
    print(f"{'PASS' if not problems else 'FAIL'} {key} words={len(content.split())} blocks={len(blocks)}")
    for problem in problems:
        print("   -", problem)
    return not problems


def apply_key(course, rows, key):
    topic_pk, level = key.split("_", 1)
    topic = PrepTopic.objects.get(pk=int(topic_pk), course=course)
    path = os.path.join(NEW_DIR, f"{key}.md")
    with open(path, encoding="utf-8") as handle:
        content = handle.read().replace("\r\n", "\n").strip() + "\n"

    problems, blocks = validate(course, topic, level, content)
    if problems:
        print(f"REJECTED {key}: {len(problems)} issue(s)")
        for problem in problems:
            print("   -", problem)
        return False

    row = rows.get((topic.pk, level))
    payload = copy.deepcopy(row.payload) if row and isinstance(row.payload, dict) else {}
    payload.update(
        {
            "level": level,
            "content": content,
            "blocks": blocks,
            "schema_version": payload.get("schema_version") or 2,
            "review_status": "passed",
            "source_signature": router._topic_notes_cache_signature(
                course, topic, topic.title, topic.subtopics
            ),
            "validation_state": router.NOTE_VALIDATION_STATE,
            "validated_at": timezone.now().isoformat(),
            "study_profile_version": router._course_study_profile_version(course),
            "topic_content_rules_version": router._topic_content_rules_version(topic),
        }
    )

    if row is None:
        # cache_key is unique and cannot be left blank when more than one row exists.
        row = PrepContentCache(
            content_type="topic_notes",
            topic=topic,
            course=course,
            cache_key=router.compute_cache_key(
                "notes", router.NOTE_VALIDATION_STATE, course.code, topic.title, level
            ),
            prompt_hash=router.compute_prompt_hash(course.code, topic.title, level),
            payload=payload,
        )
    else:
        row.payload = payload
        if not row.cache_key:
            row.cache_key = router.compute_cache_key(
                "notes", router.NOTE_VALIDATION_STATE, course.code, topic.title, level
            )
        if not row.prompt_hash:
            row.prompt_hash = router.compute_prompt_hash(course.code, topic.title, level)
    row.save()

    cache.delete(f"prep_pub_levels_{topic.pk}_True")
    cache.delete(f"prep_pub_levels_{topic.pk}_False")
    cache.delete(f"prep_pub_topic_notes_{topic.pk}")

    published = router.get_published_topic_note_levels(topic, validated_only=True)
    ok = level in published
    print(
        f"{'PUBLISHED' if ok else 'SAVED-NOT-PUBLISHED'} {key} "
        f"row={row.pk} words={len(content.split())} blocks={len(blocks)}"
    )
    if not ok:
        options = router._note_validation_options(course, topic.title, topic_obj=topic)
        recheck = router._note_completion_issues(content, topic.title, level=level, **options)
        print("   reader gate issues:", recheck)
    return ok


def main(argv):
    course = PrepCourse.objects.get(pk=COURSE_PK)
    check_only = "--check" in argv
    argv = [arg for arg in argv if arg != "--check"]
    rows = current_rows(course)
    if not argv or argv[0] == "--all":
        keys = [
            f"{topic.pk}_{level}"
            for topic in course.topics.filter(is_active=True).order_by("order")
            for level in LEVELS
            if os.path.exists(os.path.join(NEW_DIR, f"{topic.pk}_{level}.md"))
        ]
    else:
        keys = argv

    if check_only:
        results = [(key, check_key(course, key)) for key in keys]
    else:
        results = [(key, apply_key(course, rows, key)) for key in keys]
    failed = [key for key, ok in results if not ok]
    print(f"\nSUMMARY {'checked' if check_only else 'applied'}={len(results) - len(failed)} failed={len(failed)}")
    if failed:
        print("FAILED:", ", ".join(failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
