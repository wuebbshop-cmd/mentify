"""SMA 300 past-paper rendering cleanup.

Dry run by default; pass --apply to write.
"""
from __future__ import annotations

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

from django.db.models import Q  # noqa: E402
from prep.models import PrepQuestion  # noqa: E402
from services.prep_ingestion import assessment_question_rendering_issues  # noqa: E402

COURSE_ID = 8


def repair_text(text: str) -> str:
    s = text or ""
    s = s.replace("definition that$f", "definition that $f")
    s = s.replace("problem }", "problem}")
    s = s.replace("$\\Re$", "$\\mathbb{R}$")
    s = s.replace(r"\Re", r"\mathbb{R}")
    s = " ".join(s.split()).strip()
    s = s.replace("} }", "} }")
    return s


def main() -> None:
    apply = "--apply" in sys.argv
    rows = list(
        PrepQuestion.objects.filter(
            Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID)
        )
        .select_related("paper")
        .order_by("id")
    )
    reconstructions = {
        q.reconstructed_from_id: q
        for q in rows
        if q.reconstructed_from_id is not None
    }

    deletes, repairs, keeps = [], [], []
    for q in rows:
        text = q.question_latex or ""
        if q.reconstructed_from_id is not None:
            if assessment_question_rendering_issues(text):
                deletes.append((q, "unusable reconstruction with rendering defects"))
            else:
                keeps.append(q)
            continue
        if q.id in reconstructions:
            replacement = reconstructions[q.id]
            if not assessment_question_rendering_issues(replacement.question_latex):
                deletes.append((q, f"superseded by clean reconstruction q{replacement.id}"))
            else:
                deletes.append((q, f"superseded by unusable reconstruction q{replacement.id}"))
            continue
        if assessment_question_rendering_issues(text):
            fixed = repair_text(text)
            if fixed != text and not assessment_question_rendering_issues(fixed):
                repairs.append((q, fixed))
            else:
                keeps.append(q)
            continue
        fixed = repair_text(text)
        if fixed != text and not assessment_question_rendering_issues(fixed):
            repairs.append((q, fixed))
        else:
            keeps.append(q)

    print(f"rows={len(rows)} delete={len(deletes)} repair={len(repairs)} keep={len(keeps)}")
    print("deletions by reason:", dict(Counter(reason for _q, reason in deletes)))
    print("\n-- repairs --")
    for q, fixed in repairs:
        print(f"  q{q.id}: {' '.join((q.question_latex or '').split())[:120]}")
        print(f"     -> {fixed[:180]}")
    print("\n-- non-reconstruction deletions --")
    for q, reason in deletes:
        if not reason.startswith("superseded by"):
            print(f"  q{q.id} [{q.verification_status}] {reason}: {' '.join((q.question_latex or '').split())[:120]}")

    if not apply:
        print("\nDRY RUN - nothing written.")
        return

    backup = BASE_DIR / "_sma300" / "repair_backup.json"
    backup.parent.mkdir(parents=True, exist_ok=True)
    backup.write_text(
        json.dumps(
            {
                "deleted": [
                    {
                        "id": q.id,
                        "paper": str(q.paper_id),
                        "topic": q.topic_id,
                        "reason": reason,
                        "status": q.verification_status,
                        "text": q.question_latex,
                        "solution": q.solution_latex,
                    }
                    for q, reason in deletes
                ],
                "repaired": [
                    {"id": q.id, "before": q.question_latex, "after": fixed}
                    for q, fixed in repairs
                ],
            },
            indent=1,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print("\nbackup:", backup)

    for q, _reason in deletes:
        PrepQuestion.objects.filter(pk=q.id).delete()
    print(f"deleted {len(deletes)} rows")
    for q, fixed in repairs:
        PrepQuestion.objects.filter(pk=q.id).update(
            question_latex=fixed,
            verification_status="verified",
        )
    print(f"repaired {len(repairs)} rows")


if __name__ == "__main__":
    main()
