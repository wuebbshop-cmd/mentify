"""Measure how SMA 335 past-paper questions are actually structured.

Past papers are printed as "Question One (30 marks)" with parts (a)...(g), each part on
a different syllabus topic. This counts the parts, checks the schema for a many-to-many
topic link, and reports how many rows carry a worked solution (which would be orphaned
by splitting).
"""
from __future__ import annotations

import os
import re
import sys
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django  # noqa: E402

django.setup()

from django.db.models import Q  # noqa: E402

from prep.models import PrepQuestion  # noqa: E402

COURSE_ID = 57
PART_RE = re.compile(r"(?m)^\s*\(?([a-h])\)\s+\S")


def main() -> None:
    print("PrepQuestion topic relation:", PrepQuestion._meta.get_field("topic").__class__.__name__)
    m2m = [f.name for f in PrepQuestion._meta.many_to_many]
    print("many-to-many fields:", m2m or "none")

    rows = list(
        PrepQuestion.objects.filter(Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID))
        .distinct()
        .order_by("id")
    )
    shape: Counter[str] = Counter()
    parts_total = 0
    with_solution = 0
    for q in rows:
        text = q.question_latex or ""
        labels = PART_RE.findall(text)
        distinct = sorted(set(labels))
        if len(distinct) >= 2:
            shape[f"{len(distinct)} parts"] += 1
            parts_total += len(distinct)
        else:
            shape["single part"] += 1
        if (q.solution_latex or "").strip():
            with_solution += 1

    print()
    print("row shape:", dict(shape))
    print("rows with a solution:", with_solution, "of", len(rows))
    print("parts found across multi-part rows:", parts_total)

    multi = [q for q in rows if len(set(PART_RE.findall(q.question_latex or ""))) >= 2]
    multi_with_solution = [q.id for q in multi if (q.solution_latex or "").strip()]
    print("multi-part rows:", len(multi), "| of which have a solution:", len(multi_with_solution))
    print("examples with solutions:", multi_with_solution[:10])

    print()
    print("--- how a multi-part row looks ---")
    sample = next(q for q in multi if "exact" in (q.question_latex or "").lower())
    print(f"ID {sample.id} | topic {sample.topic_id} | marks {sample.marks} | solution {len(sample.solution_latex or '')} chars")
    print(sample.question_latex[:900])


if __name__ == "__main__":
    main()
