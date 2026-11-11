"""Build the evidence-based SMA 102 topic assignment plan."""

from __future__ import annotations

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

COURSE_ID = 36
HERE = Path(__file__).resolve().parent

PATTERNS = {
    110: (r"quadratic|root(?:s)? of a quadr|discriminant|complet(?:e|ing) the square|inequality.*x\^?2", 110),
    111: (r"remainder theorem|factor theorem|factorize|polynomial|divisible by|remainder when", 111),
    112: (r"permutation|arrang|committee|select(?:ion)?|choose|combinat|ways.*(?:people|letters|digits)", 112),
    113: (r"binomial|coefficient|middle term", 113),
    114: (r"\bset(?:s)?\b|(?:union|intersection)\s*|venn|survey|geography|history", 114),
    115: (r"\blogic\b|proposition|truth table|tautology|contrapositive|converse|inverse", 115),
    116: (r"mathematical induction|induction|proof by|counterexample", 116),
    117: (r"complex(?: number)?|de moivre|argument|modulus|real(?: and)? imaginary|\bz(?:_|1|2|3)?\b|\((?:1\+i|\d+[\+\-]i)", 117),
}

MANUAL = {
    482: [112],
    484: [112],
    486: [112],
    502: [117],
    505: [110, 111, 112, 113, 116, 117],
    512: [110, 111, 114],
    518: [114],
    527: [110, 111],
    528: [112, 113, 116],
    529: [114, 115],
}


def main() -> int:
    rows = list(
        PrepQuestion.objects.filter(
            Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID)
        )
        .select_related("topic")
        .distinct()
        .order_by("id")
    )
    plan = []
    for q in rows:
        text = (q.question_latex or "").lower()
        targets = list(MANUAL.get(q.id, []))
        if not targets:
            for topic_id, (pattern, _topic) in PATTERNS.items():
                if re.search(pattern, text, flags=re.I):
                    if topic_id not in targets:
                        targets.append(topic_id)
        if not targets:
            targets = [q.topic_id] if q.topic_id is not None else []
        targets = sorted(set(targets))
        plan.append({"id": q.id, "targets": targets})

    path = HERE / f"topic_plan_{COURSE_ID}.json"
    path.write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {path}: {len(plan)} questions")
    for row in plan:
        if len(row["targets"]) > 1:
            print(f"q{row['id']}: {row['targets']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
