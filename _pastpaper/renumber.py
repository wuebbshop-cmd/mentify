"""Give every distinct past-paper question a unique number within its paper.

`learner_visible_assessment_questions` keeps only one row per (paper, number), and the
multi-year source PDFs numbered every question 1-5, so distinct questions silently
collapsed into one on both paper pages and topic pages.

Renumbers the questions of each paper sequentially in extraction order and copies the new
number onto each cross-listed twin. Question text, marks and solutions are untouched.

Usage: python _pastpaper/renumber.py <course_id> [--apply]
"""
from __future__ import annotations

import io
import json
import os
import sys
from collections import defaultdict
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


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("usage: renumber.py <course_id> [--apply]")
    course_id = int(sys.argv[1])
    apply = "--apply" in sys.argv
    backup_path = Path(__file__).resolve().parent / f"renumber_backup_{course_id}.json"

    rows = list(
        PrepQuestion.objects.filter(Q(topic__course_id=course_id) | Q(paper__course_id=course_id)).order_by(
            "paper_id", "number", "id"
        )
    )
    sources = [q for q in rows if not (q.reconstruction_metadata or {}).get("cross_listed_from")]
    copies = [q for q in rows if (q.reconstruction_metadata or {}).get("cross_listed_from")]

    per_paper: dict[str, list] = defaultdict(list)
    for q in sources:
        if q.paper_id is None:
            continue
        per_paper[q.paper_id].append(q)

    new_numbers: dict[int, int] = {}
    for _paper_id, qs in per_paper.items():
        for index, q in enumerate(sorted(qs, key=lambda r: (r.number or 0, r.id)), start=1):
            new_numbers[q.id] = index
    orphan_copies = 0
    for q in copies:
        source_id = (q.reconstruction_metadata or {}).get("cross_listed_from")
        if source_id in new_numbers:
            new_numbers[q.id] = new_numbers[source_id]
        else:
            orphan_copies += 1

    current = {q.id: q.number for q in rows}
    changed = [qid for qid, number in new_numbers.items() if current.get(qid) != number]
    print(f"course {course_id}: rows={len(rows)} sources={len(sources)} copies={len(copies)}")
    print(f"rows to renumber: {len(changed)}")
    if orphan_copies:
        print(f"copies whose source is missing: {orphan_copies}")
    print("per paper after renumbering:")
    for paper_id, qs in sorted(per_paper.items(), key=lambda kv: str(kv[0])):
        numbers = sorted(new_numbers[q.id] for q in qs)
        print(f"  {str(paper_id)[:30]:30} questions={len(numbers):3d} range={numbers[0]}..{numbers[-1]}")

    if not apply:
        print("DRY RUN - nothing written.")
        return

    backup_path.write_text(json.dumps({str(k): v for k, v in current.items()}, indent=1), encoding="utf-8")
    for qid, number in new_numbers.items():
        if current.get(qid) != number:
            PrepQuestion.objects.filter(pk=qid).update(number=number)
    print(f"renumbered {len([q for q in changed])} rows; backup -> {backup_path}")


if __name__ == "__main__":
    main()
