"""Surgical repair of ASC 100 past-paper rows."""

from __future__ import annotations

import argparse
import io
import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import django  # noqa: E402

django.setup()

from django.db.models import Q  # noqa: E402

from prep.models import PrepQuestion  # noqa: E402
from services.prep_ingestion import assessment_question_rendering_issues  # noqa: E402

COURSE_ID = 28
TOPICS = {
    "Introduction to Sociology": 54,
    "Social Structure": 56,
    "Social Organisation": 57,
    "Founding Thinkers": 58,
    "Sociological Concepts": 59,
    "Social Change": 60,
}
HERE = Path(__file__).resolve().parent
BACKUP = HERE / "asc100_repair_backup.json"

VALID_SOURCE_REPAIRS = {
    101: (
        """Explain the meaning of the following concepts as used in sociology.

1. Rationality
2. Authority
3. Social structure
4. Determinism

(20 marks)""",
        59,
        20,
    ),
    117: (
        """a) Discuss the key elements of culture with relevant examples.

b) Examine the means through which people are socialized in society.

(10 marks)""",
        56,
        10,
    ),
    119: (
        """Examine the contributions of game theory and social exchange theory to the study of society, using appropriate examples.

(20 marks)""",
        56,
        20,
    ),
}

EXPLICIT_TOPIC_MOVES = {
    102: 54,
}

MALFORMED_SOURCE_IDS = {107, 109, 111, 113}
SUPERSEDED_REPLACEMENT_IDS = {272, 277, 278}
REPLACEMENT_IDS = {273, 274, 275, 276}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    rows = list(
        PrepQuestion.objects.filter(
            Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID)
        )
        .select_related("topic", "paper")
        .distinct()
        .order_by("id")
    )

    print(f"ASC 100: {len(rows)} database rows")
    print(f"valid sources to clean/promote: {len(VALID_SOURCE_REPAIRS)}")
    print(f"malformed sources to delete: {len(MALFORMED_SOURCE_IDS)}")
    print(f"superseded replacements to delete: {len(SUPERSEDED_REPLACEMENT_IDS)}")
    print(f"clean replacements to keep: {len(REPLACEMENT_IDS)}")

    changes = []
    for q in rows:
        if q.id in VALID_SOURCE_REPAIRS:
            text, topic_id, marks = VALID_SOURCE_REPAIRS[q.id]
            issues = assessment_question_rendering_issues(text)
            changes.append((q.id, "clean source", text, topic_id, marks, issues))
        elif q.id in REPLACEMENT_IDS:
            text = q.question_latex or ""
            if q.id == 274:
                text = (
                    "a) Define sociology. [2 marks]\n\n"
                    "b) Using examples, explain how sociology is a science. [8 marks]"
                )
            issues = assessment_question_rendering_issues(text)
            changes.append((q.id, "clean replacement", text, q.topic_id, q.marks, issues))

    for qid, kind, text, topic_id, marks, issues in changes:
        print(f"q{qid} {kind}: marks={marks} topic={topic_id} issues={issues or 'OK'}")

    if not args.apply:
        print("DRY RUN - nothing written. Re-run with --apply.")
        return 0

    backup = {
        str(q.id): {
            "question_latex": q.question_latex,
            "solution_latex": q.solution_latex,
            "verification_status": q.verification_status,
            "topic_id": q.topic_id,
            "number": q.number,
            "marks": q.marks,
            "reconstruction_metadata": q.reconstruction_metadata,
            "reconstructed_from_id": q.reconstructed_from_id,
        }
        for q in rows
    }
    BACKUP.write_text(json.dumps(backup, ensure_ascii=False, indent=1), encoding="utf-8")

    for qid, kind, text, topic_id, marks, issues in changes:
        if issues:
            raise RuntimeError(f"q{qid} remains invalid: {issues}")
        q = PrepQuestion.objects.get(pk=qid)
        q.question_latex = text
        q.topic_id = topic_id
        q.marks = marks
        if q.verification_status == "flagged" or q.verification_status == "pending":
            q.verification_status = "reconstructed"
        metadata = dict(q.reconstruction_metadata or {})
        if kind == "clean source":
            metadata["review_status"] = "formatting_repaired_source"
        else:
            metadata["review_status"] = "promoted_replacement"
        q.reconstruction_metadata = metadata
        q.save(update_fields=[
            "question_latex",
            "topic_id",
            "marks",
            "verification_status",
            "reconstruction_metadata",
        ])

    for qid, topic_id in EXPLICIT_TOPIC_MOVES.items():
        q = PrepQuestion.objects.filter(pk=qid).first()
        if q is not None and q.topic_id != topic_id:
            q.topic_id = topic_id
            q.save(update_fields=["topic_id"])

    delete_ids = MALFORMED_SOURCE_IDS | SUPERSEDED_REPLACEMENT_IDS
    deleted, _ = PrepQuestion.objects.filter(pk__in=delete_ids).delete()
    print(f"deleted superseded rows: {deleted}")
    print(f"backup: {BACKUP}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
