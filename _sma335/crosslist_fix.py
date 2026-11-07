"""Complete SMA 335 cross-listing.

The first pass built its duplicate-check snapshot before applying the topic moves, so
when a question's primary topic changed the copy it still needed in its old topic was
skipped as a false duplicate (83 rows). This pass moves first, rebuilds the snapshot from
the database afterwards, then creates whatever copies are genuinely missing.

Idempotent: re-running must report 0 moves and 0 copies.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django  # noqa: E402

django.setup()

from prep.models import PrepQuestion  # noqa: E402

COURSE_ID = 57
SPECIFIC_TOPICS = set(range(287, 298))
PLAN = Path(__file__).resolve().parent / "topic_plan.json"


def digest(text: str) -> str:
    return hashlib.sha256(" ".join((text or "").split()).encode("utf-8")).hexdigest()


def primary_topic(targets: list[int], current: int | None) -> int:
    specific = sorted(t for t in targets if t in SPECIFIC_TOPICS)
    if specific:
        return specific[0]
    if current in targets:
        return current
    return sorted(targets)[0]


def snapshot() -> set[tuple]:
    keys = set()
    for q in PrepQuestion.objects.filter(topic__course_id=COURSE_ID).only(
        "paper_id", "topic_id", "number", "question_latex"
    ):
        keys.add((q.paper_id, q.topic_id, q.number, digest(q.question_latex)))
    for q in PrepQuestion.objects.filter(
        paper__course_id=COURSE_ID, topic__isnull=True
    ).only("paper_id", "topic_id", "number", "question_latex"):
        keys.add((q.paper_id, q.topic_id, q.number, digest(q.question_latex)))
    return keys


def main() -> None:
    apply = "--apply" in sys.argv
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    by_id = {row["id"]: row for row in plan}
    rows = {q.id: q for q in PrepQuestion.objects.filter(pk__in=by_id)}

    # Step 1: park each question on its primary topic.
    moves = []
    for qid, row in rows.items():
        primary = primary_topic(by_id[qid]["targets"], row.topic_id)
        if row.topic_id != primary:
            moves.append((qid, row.topic_id, primary))

    # Step 2: snapshot after the moves so a vacated topic is no longer "taken".
    if apply:
        for qid, _old, new in moves:
            PrepQuestion.objects.filter(pk=qid).update(topic_id=new)
        rows = {q.id: q for q in PrepQuestion.objects.filter(pk__in=by_id)}
    else:
        for qid, _old, new in moves:
            rows[qid].topic_id = new

    existing = snapshot()
    if not apply:
        for qid, _old, new in moves:
            existing.discard((rows[qid].paper_id, _old, rows[qid].number, digest(rows[qid].question_latex)))
            existing.add((rows[qid].paper_id, new, rows[qid].number, digest(rows[qid].question_latex)))

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

    print(f"questions: {len(rows)}")
    print(f"topic moves: {len(moves)}")
    print(f"missing copies: {len(creates)}")
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
