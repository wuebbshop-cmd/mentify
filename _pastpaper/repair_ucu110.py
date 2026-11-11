"""Surgical repair of UCU 110 past-paper rows."""

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

COURSE_ID = 39
HERE = Path(__file__).resolve().parent
BACKUP = HERE / "ucu110_repair_backup.json"
PLAN = HERE / "topic_plan_39.json"

DELETE_SOURCE_IDS = {596, 597, 598, 599, 678, 681, 682, 683, 684, 687, 688, 689}
PROMOTE_IDS = {
    679, 685, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1234, 1235, 1236
}

MANUAL_TOPIC_TARGETS = {
    679: [137],
    680: [138],
    685: [135, 137],
    686: [137],
    690: [137],
    691: [137],
    692: [137, 138],
    693: [137, 138],
    694: [137],
    695: [137],
    696: [137, 138],
    697: [135, 136],
    698: [136],
    699: [135, 137],
    700: [135],
    701: [135],
    702: [135],
    1227: [137],
    1228: [138],
    1229: [137, 138],
    1230: [133, 135, 136],
    1231: [137],
    1232: [137, 138],
    1233: [137, 138],
    1234: [138],
    1235: [137, 138],
    1236: [136, 137],
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
    replacements = {q.id: q for q in rows if q.reconstructed_from_id}

    print(f"UCU 110: {len(rows)} database rows")
    print(f"superseded source rows to delete: {len(DELETE_SOURCE_IDS)}")
    print(f"pending/reconstructed replacements to promote: {len(PROMOTE_IDS)}")

    missing_promotions = sorted(qid for qid in PROMOTE_IDS if qid not in replacements)
    missing_deletes = sorted(qid for qid in DELETE_SOURCE_IDS if not any(q.id == qid for q in rows))
    if missing_promotions:
        print(f"missing promotion ids: {missing_promotions}")
    if missing_deletes:
        print(f"missing source ids: {missing_deletes}")

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

    for qid in PROMOTE_IDS:
        q = PrepQuestion.objects.filter(pk=qid).first()
        if q is None:
            continue
        metadata = dict(q.reconstruction_metadata or {})
        metadata["review_status"] = "promoted_replacement"
        q.verification_status = "reconstructed"
        q.reconstruction_metadata = metadata
        q.save(update_fields=["verification_status", "reconstruction_metadata"])

    deleted, _ = PrepQuestion.objects.filter(pk__in=DELETE_SOURCE_IDS).delete()
    print(f"deleted superseded source rows: {deleted}")

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
