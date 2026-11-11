"""Surgical repair of SMA 103 past-paper rows."""

from __future__ import annotations

import argparse
import io
import json
import os
import re
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

COURSE_ID = 37
HERE = Path(__file__).resolve().parent
BACKUP = HERE / "sma103_repair_backup.json"
PLAN = HERE / "topic_plan_37.json"

# Keep these valid sources and delete their redundant reconstruction rows.
KEEP_SOURCE_IDS = {550, 552, 554, 557, 565, 567, 570, 577, 580, 583, 585, 587, 589, 594}
DELETE_REDUNDANT_REPLACEMENT_IDS = {551, 553, 555, 558, 566, 568, 571, 578, 581, 584, 586, 588, 590, 595}

# These source IDs belong to malformed or pending replacements and must be deleted.
DELETE_SOURCE_IDS = {548, 549, 559, 561, 562, 563, 591}
PROMOTE_IDS = {1221, 1222}

SPLITS = {
    572: 573,
    574: 575,
}

MANUAL_TOPIC_TARGETS = {
    550: [127, 126, 131],
    552: [127, 126],
    554: [129, 127],
    557: [130],
    560: [131, 130, 127, 126, 128],
    564: [126],
    567: [131],
    570: [130, 129, 127, 126],
    572: [131, 130],
    574: [129, 128],
    585: [127, 126, 130, 131],
    587: [132],
    589: [127, 126],
    592: [129, 127],
    594: [130, 131],
    1221: [132],
    1222: [132],
    1223: [127],
    1224: [129],
}


def clean_split_suffix(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\n+\*+\s*This document is available on.*$", "", text, flags=re.I | re.S)
    text = re.sub(r"\n+\*+\s*$", "", text).strip()
    return text


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

    replacements = [q for q in rows if q.reconstructed_from_id]
    linked_source_ids = {q.reconstructed_from_id for q in replacements}
    all_delete_ids = (linked_source_ids | DELETE_SOURCE_IDS) - KEEP_SOURCE_IDS
    all_delete_ids |= DELETE_REDUNDANT_REPLACEMENT_IDS | set(SPLITS.values())

    print(f"SMA 103: {len(rows)} database rows")
    print(f"replacement rows: {len(replacements)}")
    print(f"rows to delete: {len(all_delete_ids)}")
    print(f"pending replacements to promote: {len(PROMOTE_IDS)}")
    print(f"split parts to merge: {len(SPLITS)}")

    for qid, suffix_id in SPLITS.items():
        q = next((row for row in rows if row.id == qid), None)
        suffix = next((row for row in rows if row.id == suffix_id), None)
        if q is None or suffix is None:
            continue
        merged = (q.question_latex or "").strip() + "\n\n" + clean_split_suffix(suffix.question_latex or "")
        issues = assessment_question_rendering_issues(merged)
        print(f"merge q{qid}+q{suffix_id}: issues={issues or 'OK'}")

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

    for qid, suffix_id in SPLITS.items():
        q = PrepQuestion.objects.filter(pk=qid).first()
        suffix = PrepQuestion.objects.filter(pk=suffix_id).first()
        if q is None or suffix is None:
            continue
        merged = (q.question_latex or "").strip() + "\n\n" + clean_split_suffix(suffix.question_latex or "")
        issues = assessment_question_rendering_issues(merged)
        if issues:
            raise RuntimeError(f"merged q{qid}+q{suffix_id} remains invalid: {issues}")
        q.question_latex = merged
        q.save(update_fields=["question_latex"])

    for qid in PROMOTE_IDS:
        q = PrepQuestion.objects.filter(pk=qid).first()
        if q is None:
            continue
        metadata = dict(q.reconstruction_metadata or {})
        metadata["review_status"] = "promoted_replacement"
        q.verification_status = "reconstructed"
        q.reconstruction_metadata = metadata
        q.save(update_fields=["verification_status", "reconstruction_metadata"])

    deleted, _ = PrepQuestion.objects.filter(pk__in=all_delete_ids).delete()
    print(f"deleted superseded or split rows: {deleted}")

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
