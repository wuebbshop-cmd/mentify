"""Surgical repair of SST 202 past-paper rows."""

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

COURSE_ID = 45
HERE = Path(__file__).resolve().parent
BACKUP = HERE / "sst202_repair_backup.json"
PLAN = HERE / "topic_plan_45.json"

DELETE_IDS = {
    1069, 1070, 1071, 1072,
    1344, 1345,
    2305, 2308, 2310, 2311, 2312, 2313, 2314, 2315,
}

MANUAL_TOPIC_TARGETS = {
    1059: [190, 192, 193],
    1060: [190, 191, 194],
    1061: [190, 191],
    1062: [190, 191],
    1063: [190, 191, 194],
    1064: [190, 192, 195],
    1065: [190, 191, 194, 195],
    1066: [190, 191, 194, 195],
    1067: [190, 191],
    1068: [190, 191],
    2304: [190],
    2306: [193, 195],
    2307: [190, 192, 194],
    2309: [190, 191],
}


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
    unmapped = [q for q in rows if q.topic_id is None]
    pending = [q for q in rows if q.verification_status == "pending"]
    flagged = [q for q in rows if q.verification_status == "flagged"]
    print(f"SST 202: {len(rows)} database rows")
    print(f"unmapped rows: {len(unmapped)}")
    print(f"pending rows: {len(pending)}; flagged rows: {len(flagged)}")
    print(f"rows to delete: {len(DELETE_IDS)}")

    missing_deletes = sorted(qid for qid in DELETE_IDS if not any(q.id == qid for q in rows))
    if missing_deletes:
        print(f"missing delete ids: {missing_deletes}")

    if not args.apply:
        print("DRY RUN - nothing written. Re-run with --apply.")
        return 0

    BACKUP.write_text(
        json.dumps(
            {
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
            },
            ensure_ascii=False,
            indent=1,
        ),
        encoding="utf-8",
    )

    q1066 = PrepQuestion.objects.filter(pk=1066).first()
    if q1066 is not None:
        text = q1066.question_latex or ""
        text = text.replace("Write ajava program", "Write a Java program")
        text = text.replace("(iv)- Main", "(iv) Main")
        text = text.replace("String []args", "String array parameter named args")
        text = text.replace("String[] args", "String array parameter named args")
        metadata = dict(q1066.reconstruction_metadata or {})
        metadata["review_status"] = "formatting_repaired"
        q1066.question_latex = text
        q1066.verification_status = "reconstructed"
        q1066.reconstruction_metadata = metadata
        q1066.save(update_fields=["question_latex", "verification_status", "reconstruction_metadata"])

    deleted, _ = PrepQuestion.objects.filter(pk__in=DELETE_IDS).delete()
    print(f"deleted invalid, foreign, superseded, or duplicate rows: {deleted}")

    remaining = list(
        PrepQuestion.objects.filter(
            Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID)
        )
        .select_related("topic")
        .distinct()
        .order_by("id")
    )
    plan = []
    for q in remaining:
        targets = MANUAL_TOPIC_TARGETS.get(q.id, [q.topic_id] if q.topic_id is not None else [])
        targets = sorted(set(targets))
        plan.append({"id": q.id, "targets": targets})
    PLAN.write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote topic plan: {PLAN} ({len(plan)} rows)")
    print(f"backup: {BACKUP}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
