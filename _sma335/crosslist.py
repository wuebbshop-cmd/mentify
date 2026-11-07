"""Cross-list SMA 335 questions into every topic they actually cover.

The syllabus topics are a ForeignKey, so a question can only appear on one topic page.
Past-paper questions here are whole exam questions whose parts span several topics
(155 of 273 touch more than one), so each question is posted into every topic its parts
belong to. Text, marks and solution are copied verbatim - nothing is rewritten, so the
worked solution always matches the question shown.

Idempotent: a row is only created when no row with the same paper, number, topic and
text already exists. Dry run by default; pass --apply to write.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
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
    """Prefer a specific syllabus topic over the two generic ones."""
    specific = sorted(t for t in targets if t in SPECIFIC_TOPICS)
    if specific:
        return specific[0]
    if current in targets:
        return current
    return sorted(targets)[0]


def main() -> None:
    apply = "--apply" in sys.argv
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    by_id = {row["id"]: row for row in plan}

    existing = {
        (q.paper_id, q.topic_id, q.number, digest(q.question_latex))
        for q in PrepQuestion.objects.filter(topic__course_id=COURSE_ID).only(
            "paper_id", "topic_id", "number", "question_latex"
        )
    }
    # Rows that belong to the course through their paper but are not yet topic-scoped.
    for q in PrepQuestion.objects.filter(paper__course_id=COURSE_ID, topic__isnull=True).only(
        "paper_id", "topic_id", "number", "question_latex"
    ):
        existing.add((q.paper_id, q.topic_id, q.number, digest(q.question_latex)))

    rows = {q.id: q for q in PrepQuestion.objects.filter(pk__in=by_id)}

    moves, creates, skipped = [], [], []
    for qid, row in rows.items():
        targets = by_id[qid]["targets"]
        primary = primary_topic(targets, row.topic_id)
        if row.topic_id != primary:
            moves.append((qid, row.topic_id, primary))
        for topic in targets:
            if topic == primary:
                continue
            key = (row.paper_id, topic, row.number, digest(row.question_latex))
            if key in existing:
                skipped.append((qid, topic))
                continue
            existing.add(key)
            creates.append((qid, topic))

    print(f"questions: {len(rows)}")
    print(f"topic moves: {len(moves)}")
    print(f"cross-listed copies: {len(creates)}")
    print(f"skipped by the duplicate check: {len(skipped)}")
    from collections import Counter

    print("copies per topic:", dict(sorted(Counter(t for _q, t in creates).items())))
    if skipped:
        print("skipped sample:", skipped[:10])
        dupe = Counter((rows[q].paper_id, by_id[q]["targets"][0]) for q, _t in skipped)
        print("skipped grouped by paper:", dict(list(dupe.items())[:5]))

    if not apply:
        print("DRY RUN - nothing written.")
        return

    backup = {
        str(qid): {"topic_id": row.topic_id}
        for qid, row in rows.items()
        if row.topic_id is not None
    }
    out = Path(__file__).resolve().parent / "crosslist_backup.json"
    out.write_text(json.dumps(backup, indent=1), encoding="utf-8")
    print("backup written:", out)

    for qid, old, new in moves:
        PrepQuestion.objects.filter(pk=qid).update(topic_id=new)
    print(f"moved {len(moves)} rows")

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
    print(f"created {len(to_create)} cross-listed rows")


if __name__ == "__main__":
    main()
