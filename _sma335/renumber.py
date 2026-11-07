"""Give every distinct SMA 335 past-paper question a unique number within its paper.

`learner_visible_assessment_questions` keeps only one row per (paper, number). The merged
multi-year source PDFs numbered every question 1-5, so 42 different questions in
`0c4a82c1` all carried number 1 and only one of them could ever render.

This renumbers the questions of each paper sequentially in extraction order and copies the
new number onto each cross-listed twin so the same question keeps one identity everywhere.
Question text, marks and solutions are untouched.

Dry run by default; pass --apply to write.
"""
from __future__ import annotations

import io
import json
import os
import re
import sys
from collections import Counter, defaultdict
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

COURSE_ID = 57
BACKUP = Path(__file__).resolve().parent / "renumber_backup.json"
_MARKER = re.compile(r"^(?:[\s:;,.()\[\]|*_#-]+|\(\s*[a-z0-9]{1,3}\s*\)|[a-z0-9]{1,3}\s*[).:]\s*)+", re.I)


def signature(text: str) -> str:
    return _MARKER.sub("", " ".join((text or "").split()).casefold())


def main() -> None:
    apply = "--apply" in sys.argv
    rows = list(
        PrepQuestion.objects.filter(Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID))
        .order_by("paper_id", "number", "id")
    )
    sources = [q for q in rows if not (q.reconstruction_metadata or {}).get("cross_listed_from")]
    copies = [q for q in rows if (q.reconstruction_metadata or {}).get("cross_listed_from")]

    clusters = defaultdict(list)
    for q in sources:
        clusters[(q.paper_id, signature(q.question_latex))].append(q)
    clashes = {k: v for k, v in clusters.items() if len(v) > 1}
    print(f"sources with the same text in the same paper: {len(clashes)}")
    for (paper, sig), qs in list(clashes.items())[:10]:
        print(f"  {paper} x{len(qs)} :: {sig[:80]!r} ids={[q.id for q in qs]}")

    per_paper = defaultdict(list)
    for q in sources:
        per_paper[q.paper_id].append(q)

    new_numbers: dict[int, int] = {}
    for paper_id, qs in per_paper.items():
        for index, q in enumerate(sorted(qs, key=lambda r: (r.number or 0, r.id)), start=1):
            new_numbers[q.id] = index

    copies_total = 0
    for q in copies:
        source_id = (q.reconstruction_metadata or {})["cross_listed_from"]
        if source_id in new_numbers:
            new_numbers[q.id] = new_numbers[source_id]
            copies_total += 1

    changed = [qid for qid, number in new_numbers.items() if next(r.number for r in rows if r.id == qid) != number]
    print(f"rows to renumber: {len(changed)} of {len(new_numbers)} (copies synced: {copies_total})")
    print("per paper after renumbering:")
    for paper_id, qs in sorted(per_paper.items()):
        numbers = sorted(new_numbers[q.id] for q in qs)
        print(f"  {paper_id[:26]:26} questions={len(numbers):3d} range={numbers[0]}..{numbers[-1]}")
    orphans = [q.id for q in copies if q.id not in new_numbers]
    if orphans:
        print("copies without a resolvable source:", orphans[:20], f"({len(orphans)} total)")

    if not apply:
        print("DRY RUN - nothing written.")
        return

    BACKUP.write_text(
        json.dumps({str(q.id): q.number for q in rows}, indent=1), encoding="utf-8"
    )
    print("backup written:", BACKUP)
    for qid, number in new_numbers.items():
        PrepQuestion.objects.filter(pk=qid).update(number=number)
    print(f"renumbered {len(new_numbers)} rows")


if __name__ == "__main__":
    main()
