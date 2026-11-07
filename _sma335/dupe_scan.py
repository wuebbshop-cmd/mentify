"""Analyse duplicate questions and meaningless numbering in published SMA 335 papers."""
from __future__ import annotations

import io
import re
import sys
import os
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
_MARKER = re.compile(r"^(?:[\s:;,.()\[\]|*_#-]+|\(\s*[a-z0-9]{1,3}\s*\)|[a-z0-9]{1,3}\s*[).:]\s*)+", re.I)


def signature(text: str) -> str:
    s = " ".join((text or "").split()).casefold()
    s = _MARKER.sub("", s)
    return s


def main() -> None:
    rows = list(
        PrepQuestion.objects.filter(
            Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID),
            paper__is_published=True,
        )
        .select_related("paper")
        .order_by("paper_id", "id")
    )
    copies = [q for q in rows if (q.reconstruction_metadata or {}).get("cross_listed_from")]
    print("rows:", len(rows), " cross-listed copies:", len(copies))

    per_paper = defaultdict(list)
    for q in rows:
        per_paper[q.paper_id].append(q)

    total_clusters = total_rows = 0
    for paper_id, qs in sorted(per_paper.items()):
        clusters = defaultdict(list)
        for q in qs:
            clusters[signature(q.question_latex)].append(q)
        distinct = len(clusters)
        dup_rows = len(qs) - distinct
        total_clusters += distinct
        total_rows += len(qs)
        biggest = max((len(v) for v in clusters.values()), default=0)
        print(f"{paper_id[:26]:26} rows={len(qs):4d} distinct={distinct:4d} dup_rows={dup_rows:4d} largest_cluster={biggest}")
    print(f"TOTAL rows={total_rows} distinct_texts={total_clusters} duplicated_rows={total_rows - total_clusters}")

    # cluster composition for the worst paper
    worst = max(per_paper.items(), key=lambda kv: len(kv[1]))
    print(f"\nworst paper {worst[0]}:")
    clusters = defaultdict(list)
    for q in worst[1]:
        clusters[signature(q.question_latex)].append(q)
    for sig, qs in sorted(clusters.items(), key=lambda kv: -len(kv[1]))[:15]:
        kinds = Counter(
            "copy" if (q.reconstruction_metadata or {}).get("cross_listed_from") else q.question_type for q in qs
        )
        has_sol = sum(1 for q in qs if (q.solution_latex or "").strip())
        print(f"  x{len(qs)} sol={has_sol} {dict(kinds)} :: {sig[:80]!r}")
    print("clusters total in worst paper:", len(clusters))


if __name__ == "__main__":
    main()
