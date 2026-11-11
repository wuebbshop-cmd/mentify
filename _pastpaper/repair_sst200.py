"""Surgical repair of SST 200 past-paper topic assignments."""

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

COURSE_ID = 44
HERE = Path(__file__).resolve().parent
BACKUP = HERE / "sst200_repair_backup.json"
PLAN = HERE / "topic_plan_44.json"

DELETE_IDS = {2319}

MANUAL_TOPIC_TARGETS = {
    2321: [236],
    2322: [236],
    2323: [236],
    2331: [236, 239, 240],
    2334: [236, 238, 240],
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
    print(f"SST 200: {len(rows)} database rows")
    print(f"unmapped rows: {len(unmapped)}")
    print(f"foreign/unrelated rows to delete: {len(DELETE_IDS)}")
    print(f"unmapped rows to assign: {len(MANUAL_TOPIC_TARGETS)}")

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

    deleted, _ = PrepQuestion.objects.filter(pk__in=DELETE_IDS).delete()
    print(f"deleted foreign/unrelated rows: {deleted}")

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
