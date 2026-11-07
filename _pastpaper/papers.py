"""Per-paper profile for one course: statuses, duplicate detection, sample text.

Usage: python _pastpaper/papers.py <course_id>
"""
from __future__ import annotations

import io
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

from prep.models import PrepPaper, PrepQuestion  # noqa: E402
from services.prep_ingestion import assessment_question_rendering_issues  # noqa: E402

_MARKER = re.compile(r"^(?:[\s:;,.()\[\]|*_#-]+|\(\s*[a-z0-9]{1,3}\s*\)|[a-z0-9]{1,3}\s*[).:]\s*)+", re.I)


def signature(text: str) -> str:
    return _MARKER.sub("", " ".join((text or "").split()).casefold())[:120]


def main() -> None:
    course_id = int(sys.argv[1])
    papers = PrepPaper.objects.filter(course_id=course_id).order_by("id")
    all_sigs: dict[str, set[int]] = defaultdict(set)
    for paper in papers:
        rows = list(PrepQuestion.objects.filter(paper=paper).order_by("number", "id"))
        if not rows:
            continue
        statuses = Counter(q.verification_status for q in rows)
        bad = [q for q in rows if assessment_question_rendering_issues(q.question_latex)]
        sigs = Counter(signature(q.question_latex) for q in rows)
        for s in sigs:
            all_sigs[s].add(hash(paper.id))
        print(f"\n=== {str(paper.id)[:34]} pub={paper.is_published} rows={len(rows)} statuses={dict(statuses)}")
        print(f"    failing gate={len(bad)} distinct={len(sigs)} duplicated={sum(v - 1 for v in sigs.values())}")
        for q in rows[:3]:
            print(f"    q{q.id} n{q.number} :: {' '.join((q.question_latex or '').split())[:120]}")
    shared = {s: p for s, p in all_sigs.items() if len(p) > 1}
    print(f"\nstatements appearing in more than one paper: {len(shared)}")
    unmapped = PrepQuestion.objects.filter(Q(topic__course_id=course_id) | Q(paper__course_id=course_id), topic__isnull=True).count()
    print("unmapped rows:", unmapped)


if __name__ == "__main__":
    main()
