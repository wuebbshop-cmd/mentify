"""Dry-run every deterministic repair across all SMA 335 questions.

Prints a summary and writes a unified diff per question so each proposed change
can be reviewed before anything is written. Pass --apply to write.
"""
from __future__ import annotations

import difflib
import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
sys.path.insert(0, str(Path(__file__).resolve().parent))

import django  # noqa: E402

django.setup()

from prep.models import PrepQuestion  # noqa: E402
from repair import is_acceptable, repair_text  # noqa: E402

COURSE_ID = 57


def main() -> None:
    apply_write = "--apply" in sys.argv

    questions = list(PrepQuestion.objects.filter(topic__course_id=COURSE_ID).order_by("id"))

    planned = []
    rejected = []
    for q in questions:
        before = q.question_latex or ""
        after, changes = repair_text(before)
        if after == before:
            continue
        ok, why = is_acceptable(before, after)
        if ok:
            planned.append((q.id, before, after, changes))
        else:
            rejected.append((q.id, why))

    print(f"questions: {len(questions)} | to repair: {len(planned)} | rejected: {len(rejected)}")
    labels: dict[str, int] = {}
    for _pk, _b, _a, changes in planned:
        for c in changes:
            labels[c] = labels.get(c, 0) + 1
    for label, count in sorted(labels.items(), key=lambda kv: -kv[1]):
        print(f"   {count:4d}  {label}")
    if rejected:
        print("rejected:", rejected)

    out_path = Path(__file__).resolve().parent / "rescan_diff.txt"
    with out_path.open("w", encoding="utf-8") as fh:
        for pk, before, after, changes in planned:
            fh.write("=" * 100 + "\n")
            fh.write(f"ID {pk} :: {', '.join(changes)}\n")
            fh.write("=" * 100 + "\n")
            fh.write(
                "\n".join(
                    difflib.unified_diff(
                        before.split("\n"), after.split("\n"), "before", "after", lineterm=""
                    )
                )
                + "\n\n"
            )
    print("diff written:", out_path)

    if apply_write:
        backup = Path(__file__).resolve().parent / "rescan_backup.json"
        backup.write_text(
            json.dumps({pk: b for pk, b, _a, _c in planned}, indent=1, ensure_ascii=False),
            encoding="utf-8",
        )
        for pk, _b, after, _c in planned:
            PrepQuestion.objects.filter(pk=pk).update(question_latex=after)
        print(f"applied to {len(planned)} rows | backup: {backup}")
    else:
        print("DRY RUN - nothing written.")


if __name__ == "__main__":
    main()
