"""Validate SMA 335 notes and publish them into the note cache.

Usage (run from the repository root):
    python _sma335/apply.py --check 171_level_1 171_level_2
    python _sma335/apply.py 171_level_1 171_level_2 171_level_3
    python _sma335/apply.py --topic 171        # check all three levels of one topic
    python _sma335/apply.py --audit            # fast database-level audit, no AI

Each ``<topic_pk>_<level>`` key reads Markdown from ``_sma335/new/<key>.md``.
A note is written to the database only after it passes the same validation the
reader gate applies, so failing content can never reach a learner.  Nothing here
calls an AI provider: notes are authored on disk and published locally at zero
API cost.
"""

from __future__ import annotations

import copy
import os
import re
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

COURSE_PK = 57
LEVELS = ("level_1", "level_2", "level_3")
MIN_WORDS = 5000
NEW_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "new")


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


def math_defects(text):
    """Cheap structural defects that break KaTeX rendering in the shared renderer."""
    normalized = router.normalize_math_delimiters(text)
    return (
        len(re.findall(r"\\\(|\\\)|\\\[|\\\]", normalized))
        + len(re.findall(r"(?:\\\)|\$)\s*[\^_]", normalized))
        + normalized.count("```")
        + normalized.count("\\$")
    )


def validate(course, topic, level, content):
    options = router._note_validation_options(course, topic.title, topic_obj=topic)
    issues = router._note_completion_issues(content, topic.title, level=level, **options)
    blocks = parse_markdown_to_blocks(content)
    blocks_ok, block_message = validate_structured_blocks(blocks)
    words = len(content.split())
    problems = list(issues)

    # The reader gate re-validates the *normalized* content, which can differ from
    # the source file, so check the same way it does.
    normalized = router.normalize_math_delimiters(content).strip()
    if normalized != content.strip():
        problems.extend(
            f"after math normalization: {issue}"
            for issue in router._note_completion_issues(
                normalized, topic.title, level=level, **options
            )
        )
    if "\\$" in content:
        problems.append(r"contains the escaped dollar \$ which breaks math delimiter pairing")
    if math_defects(content):
        problems.append(f"structural math defects: {math_defects(content)}")
    if not content.lstrip().startswith("## 1. Foundational Concepts"):
        problems.append("does not start with the required first section heading")

    if not blocks_ok:
        problems.append(f"structured blocks invalid: {block_message}")
    if words < MIN_WORDS:
        problems.append(f"only {words} words; at least {MIN_WORDS} are required")
    return problems, blocks


def read_note(key):
    path = os.path.join(NEW_DIR, f"{key}.md")
    with open(path, encoding="utf-8") as handle:
        return handle.read().replace("\r\n", "\n").strip() + "\n"


def check_key(course, key):
    topic_pk, level = key.split("_", 1)
    topic = PrepTopic.objects.get(pk=int(topic_pk), course=course)
    content = read_note(key)
    problems, blocks = validate(course, topic, level, content)
    print(
        f"{'PASS' if not problems else 'FAIL'} {key} "
        f"words={len(content.split())} blocks={len(blocks)}"
    )
    for problem in problems:
        print("   -", problem)
    return not problems


def apply_key(course, rows, key):
    topic_pk, level = key.split("_", 1)
    topic = PrepTopic.objects.get(pk=int(topic_pk), course=course)
    content = read_note(key)

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

    key_value = router.compute_cache_key(
        "notes", router.NOTE_VALIDATION_STATE, course.code, topic.title, level
    )
    if row is None:
        row = PrepContentCache(
            content_type="topic_notes",
            topic=topic,
            course=course,
            cache_key=key_value,
            prompt_hash=router.compute_prompt_hash(course.code, topic.title, level),
            payload=payload,
        )
    else:
        row.payload = payload
        row.cache_key = row.cache_key or key_value
        row.prompt_hash = row.prompt_hash or router.compute_prompt_hash(
            course.code, topic.title, level
        )
    row.save()

    for cache_key in (
        f"prep_pub_levels_{topic.pk}_True",
        f"prep_pub_levels_{topic.pk}_False",
        f"prep_pub_topic_notes_{topic.pk}",
    ):
        cache.delete(cache_key)

    published = router.get_published_topic_note_levels(topic, validated_only=True)
    ok = level in published
    print(
        f"{'PUBLISHED' if ok else 'SAVED-NOT-PUBLISHED'} {key} "
        f"row={row.pk} words={len(content.split())} blocks={len(blocks)}"
    )
    if not ok:
        options = router._note_validation_options(course, topic.title, topic_obj=topic)
        print(
            "   reader gate issues:",
            router._note_completion_issues(content, topic.title, level=level, **options),
        )
    return ok


def audit(course):
    """Fast database-level check: current signature, validation state, size, math."""
    rows = current_rows(course)
    ok = 0
    problems = []
    print(f"{'pk':>4} {'#':>2} {'topic':44} {'L1':>8} {'L2':>8} {'L3':>8}")
    print("-" * 78)
    for topic in course.topics.filter(is_active=True).order_by("order"):
        signature = router._topic_notes_cache_signature(
            course, topic, topic.title, topic.subtopics
        )
        cells = []
        for level in LEVELS:
            row = rows.get((topic.pk, level))
            if row is None:
                cells.append("--")
                problems.append(f"missing {topic.pk}_{level}")
                continue
            payload = row.payload or {}
            content = payload.get("content") or ""
            issues = []
            if payload.get("source_signature") != signature:
                issues.append("stale signature")
            if payload.get("validation_state") != router.NOTE_VALIDATION_STATE:
                issues.append("validation state")
            if math_defects(content):
                issues.append(f"math defects {math_defects(content)}")
            if len(content.split()) < MIN_WORDS:
                issues.append("too short")
            if issues:
                cells.append("BAD")
                problems.append(f"{topic.pk}_{level}: {issues}")
            else:
                cells.append(f"{len(content.split())}w")
                ok += 1
        print(f"{topic.pk:>4} {topic.order:>2} {topic.title[:44]:44} " + " ".join(f"{c:>8}" for c in cells))
    print("-" * 78)
    print(f"PUBLISHABLE {ok}/39 | problems {problems or 'NONE'}")
    return ok, problems


def main(argv):
    course = PrepCourse.objects.get(pk=COURSE_PK)
    check_only = "--check" in argv
    argv = [arg for arg in argv if arg != "--check"]

    if argv and argv[0] == "--audit":
        ok, problems = audit(course)
        return 0 if ok == 39 and not problems else 1

    if argv and argv[0] == "--topic":
        topic_pk = int(argv[1])
        keys = [f"{topic_pk}_{level}" for level in LEVELS]
        check_only = True
    elif not argv or argv[0] == "--all":
        keys = [
            f"{topic.pk}_{level}"
            for topic in course.topics.filter(is_active=True).order_by("order")
            for level in LEVELS
            if os.path.exists(os.path.join(NEW_DIR, f"{topic.pk}_{level}.md"))
        ]
    else:
        keys = argv

    rows = current_rows(course)
    if check_only:
        results = [(key, check_key(course, key)) for key in keys]
    else:
        results = [(key, apply_key(course, rows, key)) for key in keys]
    failed = [key for key, ok in results if not ok]
    print(
        f"\nSUMMARY {'checked' if check_only else 'applied'}="
        f"{len(results) - len(failed)} failed={len(failed)}"
    )
    if failed:
        print("FAILED:", ", ".join(failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
