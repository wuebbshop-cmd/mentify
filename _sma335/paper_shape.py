"""Inspect SMA 335 papers that contain repeated question numbers with distinct text."""
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

COURSE_ID = 57


def norm(text: str) -> str:
    return " ".join((text or "").split())


def main() -> None:
    rows = list(
        PrepQuestion.objects.filter(
            Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID),
            paper__is_published=True,
        )
        .select_related("paper")
        .order_by("paper_id", "number", "id")
    )
    print("number field:", PrepQuestion._meta.get_field("number").__class__.__name__)

    groups: dict[tuple, list] = defaultdict(list)
    for q in rows:
        groups[(q.paper_id, q.number)].append(q)

    per_paper: dict[str, dict] = defaultdict(lambda: {"rows": 0, "numbers": set(), "distinct": set()})
    for q in rows:
        info = per_paper[q.paper_id]
        info["rows"] += 1
        info["numbers"].add(q.number)
        info["distinct"].add((q.number, norm(q.question_latex)))

    print(f"{'paper':26} {'rows':>5} {'distinct':>9} {'numbers':>8}  title")
    for paper_id, info in sorted(per_paper.items(), key=lambda kv: -kv[1]["rows"]):
        paper = next(q.paper for q in rows if q.paper_id == paper_id)
        flag = "  <-- LOSES" if len(info["distinct"]) < info["rows"] else ""
        print(
            f"{paper_id[:26]:26} {info['rows']:5d} {len(info['distinct']):9d} {len(info['numbers']):8d}  "
            f"{(paper.title or '')[:44]}{flag}"
        )

    hidden = sum(len({norm(q.question_latex) for q in qs}) - 1 for qs in groups.values())
    print("distinct questions lost to the (paper, number) dedupe:", hidden)

    detail = []
    for (paper, number), qs in groups.items():
        texts = {norm(q.question_latex) for q in qs}
        if len(texts) > 1:
            detail.append(
                {
                    "paper": paper,
                    "number": number,
                    "rows": [{"id": q.id, "topic": q.topic_id, "text": norm(q.question_latex)[:120]} for q in qs],
                }
            )
    Path(BASE_DIR / "_sma335" / "number_clashes.json").write_text(
        json.dumps(detail, indent=1, ensure_ascii=False), encoding="utf-8"
    )
    print("detail written to _sma335/number_clashes.json:", len(detail), "groups")


if __name__ == "__main__":
    main()
