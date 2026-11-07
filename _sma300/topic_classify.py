import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django  # noqa: E402

django.setup()

from django.db.models import Q  # noqa: E402
from prep.models import PrepQuestion  # noqa: E402

COURSE_ID = 8

RULES = [
    (19, (
        "real number system", "completeness axiom", "complete ordered field",
        "field axiom", "order axiom", "supremum", "infimum",
        "maximum", "minimum", "bounded above", "bounded below", "density",
        "rational", "irrational", "archimedean",
    )),
    (20, (
        "open set", "closed set", "topology", "compact", "interior",
        "closure", "neighbourhood", "neighborhood", "accumulation point",
        "limit point", "metric space", "open interval", "arbitrary union",
        "arbitrary intersection", "complement is open",
    )),
    (21, (
        "sequence", "sequences", "cauchy", "limsup", "lim inf", "limit inferior",
        "limit superior", "monotone", "bounded sequence", "s_n", "{s_n}",
        "x_n", "\\{x_n", "\\lim_{n", "convergent sequence",
    )),
    (22, (
        "series", "summation", "\\sum", "ratio test", "root test",
        "comparison test", "integral test", "alternating series",
        "absolute convergence", "absolute convergent", "conditionally convergent",
        "converges", "diverges", "partial sum", "geometric series",
    )),
    (23, (
        "countable", "uncountable", "denumerable", "natural numbers",
        "bijection", "one-to-one correspondence", "cartesian product",
    )),
    (24, (
        "function", "functions", "continuity", "continuous", "uniformly continuous",
        "limit of a function", "\\lim_{x", "discontinuous", "piecewise",
    )),
]


def main() -> None:
    rows = list(
        PrepQuestion.objects.filter(
            Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID)
        )
        .exclude(reconstruction_metadata__cross_listed_from__isnull=False)
        .order_by("id")
    )
    plan = []
    for q in rows:
        text = (q.question_latex or "").casefold().replace("\u00a0", " ")
        targets = {
            topic_id
            for topic_id, needles in RULES
            if any(needle.casefold() in text for needle in needles)
        }
        if not targets and q.topic_id:
            targets.add(q.topic_id)
        if not targets:
            targets.add(19)
        plan.append({"id": q.id, "targets": sorted(targets)})

    out = BASE_DIR / "_pastpaper" / f"topic_plan_{COURSE_ID}.json"
    out.write_text(json.dumps(plan, indent=1, ensure_ascii=False), encoding="utf-8")
    from collections import Counter
    print(f"wrote {out}: {len(plan)} questions")
    print("placements:", dict(sorted(Counter(t for row in plan for t in row["targets"]).items())))


if __name__ == "__main__":
    main()
