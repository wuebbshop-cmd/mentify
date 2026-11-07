"""Cross-list a course's past-paper questions into every topic their parts cover.

`PrepQuestion.topic` is a foreign key, so a question can only appear on one topic page.
Exam questions here are whole questions whose parts span several syllabus topics, so each
question is posted into every topic its parts belong to. Text, marks and solution are
copied verbatim, so the worked solution always matches the question shown.

Idempotent: a copy is only created when no row with the same paper, number, topic and text
already exists. The duplicate snapshot is rebuilt after the topic moves, so vacating a
topic never blocks the copy that belongs there.

Usage: python _pastpaper/crosslist.py <course_id> [--apply]
"""
from __future__ import annotations

import hashlib
import io
import json
import os
import sys
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import django  # noqa: E402

django.setup()

from prep.models import PrepQuestion  # noqa: E402

HERE = Path(__file__).resolve().parent


def digest(text: str) -> str:
    return hashlib.sha256(" ".join((text or "").split()).encode("utf-8")).hexdigest()


def primary_topic(targets: list[int], current: int | None) -> int:
    if current in targets:
        return current
    return sorted(targets)[0]


def snapshot(course_id: int) -> set[tuple]:
    keys = set()
    for q in PrepQuestion.objects.filter(topic__course_id=course_id).only(
        "paper_id", "topic_id", "number", "question_latex"
    ):
        keys.add((q.paper_id, q.topic_id, q.number, digest(q.question_latex)))
    for q in PrepQuestion.objects.filter(paper__course_id=course_id, topic__isnull=True).only(
        "paper_id", "topic_id", "number", "question_latex"
    ):
        keys.add((q.paper_id, q.topic_id, q.number, digest(q.question_latex)))
    return keys


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("usage: crosslist.py <course_id> [--apply]")
    course_id = int(sys.argv[1])
    apply = "--apply" in sys.argv
    plan = json.loads((HERE / f"topic_plan_{course_id}.json").read_text(encoding="utf-8"))
    by_id = {row["id"]: row for row in plan}
    rows = {q.id: q for q in PrepQuestion.objects.filter(pk__in=by_id)}

    moves = []
    for qid, row in rows.items():
        primary = primary_topic(by_id[qid]["targets"], row.topic_id)
        if row.topic_id != primary:
            moves.append((qid, row.topic_id, primary))

    if apply:
        for qid, _old, new in moves:
            PrepQuestion.objects.filter(pk=qid).update(topic_id=new)
        rows = {q.id: q for q in PrepQuestion.objects.filter(pk__in=by_id)}

    existing = snapshot(course_id)
    if not apply:
        for qid, old, new in moves:
            row = rows[qid]
            existing.discard((row.paper_id, old, row.number, digest(row.question_latex)))
            existing.add((row.paper_id, new, row.number, digest(row.question_latex)))

    creates = []
    for qid, row in rows.items():
        for topic in by_id[qid]["targets"]:
            if topic == row.topic_id:
                continue
            key = (row.paper_id, topic, row.number, digest(row.question_latex))
            if key in existing:
                continue
            existing.add(key)
            creates.append((qid, topic))

    print(f"course {course_id}: questions={len(rows)} moves={len(moves)} missing copies={len(creates)}")
    print("copies per topic:", dict(sorted(Counter(t for _q, t in creates).items())))

    if not apply:
        print("DRY RUN - nothing written.")
        return

    to_create = []
    for qid, topic in creates:
        src = rows[qid]
        metadata = dict(src.reconstruction_metadata or {})
        metadata["cross_listed_from"] = src.id
        to_create.append(
            PrepQuestion(
                paper_id=src.paper_id,
                topic_id=topic,
                topic_label="",
                number=src.number,
                marks=src.marks,
                question_type=src.question_type,
                question_latex=src.question_latex,
                solution_latex=src.solution_latex,
                verification_status=src.verification_status,
                source_document_id=src.source_document_id,
                source_page_number=src.source_page_number,
                extraction_confidence=src.extraction_confidence,
                reconstruction_metadata=metadata,
            )
        )
    PrepQuestion.objects.bulk_create(to_create, batch_size=100)
    print(f"moved {len(moves)} rows, created {len(to_create)} cross-listed rows")


if __name__ == "__main__":
    main()
