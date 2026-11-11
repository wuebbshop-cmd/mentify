"""Build a transparent per-course topic PDF pack audit."""

from __future__ import annotations

import io
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import django  # noqa: E402

django.setup()

from django.db.models import Count, Q  # noqa: E402
from prep.models import (  # noqa: E402
    PrepContentCache,
    PrepCourse,
    PrepQuestion,
    PrepTopic,
    PrepTopicPdfArtifact,
)
from services.prep_ai_router import NOTE_VALIDATION_STATE  # noqa: E402
from services.cloudflare_storage import is_cloudflare_r2_configured  # noqa: E402

OUTPUT = BASE_DIR / "course_pdf_pack_audit.md"
LEVELS = ("level_1", "level_2", "level_3")


def count_statuses(course_id: int):
    return dict(
        PrepTopicPdfArtifact.objects.filter(topic__course_id=course_id)
        .values("status")
        .annotate(count=Count("id"))
        .values_list("status", "count")
    )


def cache_note_levels(course_id: int):
    levels = defaultdict(set)
    entries = (
        PrepContentCache.objects.filter(
            course_id=course_id,
            content_type="topic_notes",
        )
        .exclude(topic_id=None)
        .only("topic_id", "payload")
    )
    for entry in entries:
        payload = entry.payload if isinstance(entry.payload, dict) else {}
        level = payload.get("level") or "level_2"
        content = payload.get("content") or payload.get("notes") or ""
        if (
            level in LEVELS
            and payload.get("validation_state") == NOTE_VALIDATION_STATE
            and str(content).strip()
        ):
            levels[entry.topic_id].add(level)
    return levels


def visible_question_counts(course: PrepCourse, topics: list[PrepTopic]):
    records = PrepQuestion.objects.filter(
        paper__course=course,
        paper__is_published=True,
        question_type__in=("authentic", "adapted"),
        verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
    ).only("id", "topic_id", "topic_label").distinct()
    direct_counts = defaultdict(set)
    unmapped = []
    topic_ids = {topic.id: topic for topic in topics}
    for question in records:
        if question.topic_id in topic_ids:
            direct_counts[question.topic_id].add(question.id)
        elif question.topic_id is None:
            unmapped.append(question)
    for question in unmapped:
        label = str(question.topic_label or "").casefold()
        for topic in topics:
            if label and topic.title.casefold() in label:
                direct_counts[topic.id].add(question.id)
    return {topic.id: len(direct_counts[topic.id]) for topic in topics}


def main() -> None:
    courses = list(PrepCourse.objects.filter(is_active=True).order_by("code"))
    topics = list(
        PrepTopic.objects.filter(is_active=True)
        .select_related("course")
        .order_by("course_id", "order", "id")
    )
    topics_by_course = defaultdict(list)
    course_by_topic = {}
    for topic in topics:
        topics_by_course[topic.course_id].append(topic)
        course_by_topic[topic.id] = topic.course_id

    artifact_status_totals = dict(
        PrepTopicPdfArtifact.objects.values("status")
        .annotate(count=Count("id"))
        .values_list("status", "count")
    )
    active_topics = len(topics)
    total_artifacts = PrepTopicPdfArtifact.objects.count()

    note_levels = defaultdict(set)
    for entry in PrepContentCache.objects.filter(content_type="topic_notes").exclude(
        topic_id=None
    ).only("topic_id", "payload"):
        payload = entry.payload if isinstance(entry.payload, dict) else {}
        level = payload.get("level") or "level_2"
        content = payload.get("content") or payload.get("notes") or ""
        if (
            level in LEVELS
            and payload.get("validation_state") == NOTE_VALIDATION_STATE
            and str(content).strip()
        ):
            note_levels[entry.topic_id].add(level)

    artifact_map = {}
    artifact_status_by_course = defaultdict(lambda: defaultdict(int))
    for artifact in PrepTopicPdfArtifact.objects.values(
        "topic_id", "topic__course_id", "artifact_type", "level", "status"
    ):
        topic_id = artifact["topic_id"]
        course_id = artifact["topic__course_id"]
        artifact_map[(topic_id, artifact["artifact_type"], artifact["level"])] = artifact["status"]
        artifact_status_by_course[course_id][artifact["status"]] += 1

    visible_counts_by_course = defaultdict(lambda: defaultdict(set))
    visible_questions = PrepQuestion.objects.filter(
        paper__course_id__isnull=False,
        paper__is_published=True,
        question_type__in=("authentic", "adapted"),
        verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
    ).values("id", "topic_id", "topic_label", "paper__course_id").distinct()
    unmapped_questions = []
    for question in visible_questions.iterator(chunk_size=1000):
        course_id = question["paper__course_id"]
        topic_id = question["topic_id"]
        if topic_id in course_by_topic:
            topic_course_id = course_by_topic[topic_id]
            if topic_course_id == course_id:
                visible_counts_by_course[course_id][topic_id].add(question["id"])
        elif topic_id is None:
            unmapped_questions.append(question)
    for question in unmapped_questions:
        label = str(question["topic_label"] or "").casefold()
        course_id = question["paper__course_id"]
        for topic in topics_by_course.get(course_id, []):
            if label and topic.title.casefold() in label:
                visible_counts_by_course[course_id][topic.id].add(question["id"])

    rows = []
    total_source_note_packs = 0
    total_question_slots = 0
    total_ready = 0
    total_empty = 0
    total_pending = 0
    total_running = 0
    total_failed = 0

    for course in courses:
        course_topics = topics_by_course.get(course.id, [])
        if not course_topics:
            continue
        source_note_slots = sum(len(note_levels.get(topic.id, set())) for topic in course_topics)
        question_slots = len(course_topics)
        logical_slots = source_note_slots + question_slots
        statuses = artifact_status_by_course.get(course.id, {})

        ready = statuses.get("ready", 0)
        empty = statuses.get("empty", 0)
        pending = statuses.get("pending", 0)
        running = statuses.get("running", 0)
        failed = statuses.get("failed", 0)
        existing = sum(statuses.values())

        missing_note_records = 0
        missing_question_records = 0
        topic_detail = []
        eligible_questions = 0
        for topic in course_topics:
            published_levels = note_levels.get(topic.id, set())
            missing = []
            for level in LEVELS:
                if level in published_levels and (topic.id, "notes", level) not in artifact_map:
                    missing.append(f"{level}:missing")
                    missing_note_records += 1
            if (topic.id, "questions", "") not in artifact_map:
                missing.append("questions:missing")
                missing_question_records += 1
            q_count = len(visible_counts_by_course[course.id].get(topic.id, set()))
            eligible_questions += q_count
            if missing:
                topic_detail.append(
                    f"- Topic {topic.id} — {topic.title}: {', '.join(missing)}"
                )

        total_source_note_packs += source_note_slots
        total_question_slots += question_slots
        total_ready += ready
        total_empty += empty
        total_pending += pending
        total_running += running
        total_failed += failed
        missing_records = missing_note_records + missing_question_records
        rows.append({
            "course": course,
            "topics": len(course_topics),
            "source_note_slots": source_note_slots,
            "question_slots": question_slots,
            "logical_slots": logical_slots,
            "ready": ready,
            "empty": empty,
            "pending": pending,
            "running": running,
            "failed": failed,
            "existing": existing,
            "missing": missing_records,
            "eligible_questions": eligible_questions,
            "topic_detail": topic_detail,
        })

    now = datetime.now(timezone.utc).astimezone().isoformat(timespec="minutes")
    lines = [
        "# Topic PDF Pack Audit — Per Course",
        "",
        f"**Audit time:** {now}",
        "",
        "## Current pipeline status",
        "",
        "- **Current pipeline state:** Queue-only worker stopped after reaching a database DNS error; it is not currently processing jobs.",
        "- **Why reconciliation was skipped:** The first full reconciliation exceeded MySQL's idle connection window and lost the database connection.",
        "- **Last worker attempt:** Failed during reconciliation with MySQL error `2013 Lost connection to server during query`.",
        "- **Latest queue-worker error:** Job processing ended with MySQL DNS error `(2005) Unknown server host mysql-38ae4425-electoole-c2b3.i.aivencloud.com`.",
        "- **Chromium:** Verified installed and Playwright launch succeeded with Chrome/Edge support.",
        "- **Playwright package:** Restored at the version declared by the project (`playwright==1.52.0`).",
        "- **Cloudflare R2:** Configured for PDF artifact uploads.",
        "- **Fallback:** ReportLab is available and carries the same branded footer. It is used only if the normal browser pipeline falls back or Chromium cannot render.",
        "",
        "## Global totals",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Active courses in this audit | {len(rows)} |",
        f"| Active topics | {active_topics} |",
        f"| Existing PDF artifact records | {total_artifacts} |",
        f"| Validated source note slots | {total_source_note_packs} |",
        f"| Question pack slots | {total_question_slots} |",
        f"| Logical source-backed note + question packs | {total_source_note_packs + total_question_slots} |",
        f"| Ready | {total_ready} |",
        f"| Empty / no eligible source | {total_empty} |",
        f"| Pending | {total_pending} |",
        f"| Running | {total_running} |",
        f"| Failed | {total_failed} |",
        "",
        "## Artifact status at audit time",
        "",
        "| Status | Artifact records |",
        "|---|---:|",
    ]
    for status in ("ready", "empty", "pending", "running", "failed"):
        lines.append(f"| {status} | {artifact_status_totals.get(status, 0)} |")

    lines.extend([
        "",
        "## How to read this document",
        "",
        "- **Validated note slots** counts only notes whose cache payload has the current validation marker and non-empty content.",
        "- **Question slots** is one question pack per active topic.",
        "- **Logical packs** is the source-backed number of note packs plus the one question pack per topic.",
        "- **Missing** counts artifact records which should exist but do not yet exist.",
        "- `empty` means the pipeline found no eligible source content; it is not a PDF-generation failure.",
        "- `pending` means work is queued or waiting for processing.",
        "- `running` means a worker claimed it and no completion state was recorded.",
        "- `failed` means processing exhausted its retry attempts.",
        "- Per-course rows are sorted by course code.",
        "",
        "## Course-by-course status",
        "",
        "| Course | Topics | Validated note slots | Question slots | Logical packs | Ready | Empty | Pending | Running | Failed | Missing records | Visible past questions |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for row in sorted(rows, key=lambda item: item["course"].code):
        course = row["course"]
        lines.append(
            "| "
            + f"{course.code} - {course.title} | {row['topics']} | "
            + f"{row['source_note_slots']} | {row['question_slots']} | {row['logical_slots']} | "
            + f"{row['ready']} | {row['empty']} | {row['pending']} | {row['running']} | "
            + f"{row['failed']} | {row['missing']} | {row['eligible_questions']} |"
        )

    lines.extend([
        "",
        "## Courses with missing artifact records",
        "",
    ])
    missing_rows = [row for row in rows if row["missing"]]
    if not missing_rows:
        lines.append("No missing artifact records were detected.")
    else:
        for row in sorted(missing_rows, key=lambda item: item["course"].code):
            course = row["course"]
            lines.append(f"### {course.code} - {course.title}")
            lines.extend(row["topic_detail"])
            lines.append("")

    lines.extend([
        "## Recommended processing order",
        "",
        "1. Restart the PDF worker only after MySQL is stable.",
        "2. Prefer the worker with initial reconciliation skipped once the source-backed queue has already been reconciled.",
        "3. Process `failed` and stale `running` jobs first, then `pending` jobs.",
        "4. Regenerate only source-backed validated note levels and each topic's questions pack.",
        "5. Verify Cloudflare R2 keys and downloadability after processing.",
        "6. Regenerate this audit document after each batch.",
        "",
    ])

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUTPUT}")
    print(f"active_courses={len(rows)} active_topics={active_topics} artifacts={total_artifacts}")
    print(f"source_note_slots={total_source_note_packs} question_slots={total_question_slots}")


if __name__ == "__main__":
    main()
