"""Build and review the SMA 200 topic-placement plan."""
from __future__ import annotations

import io
import json
import os
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

COURSE_ID = 41
OUT = BASE_DIR / "_pastpaper" / "topic_plan_41.json"

TOPICS = {
    155: "Integration Of Functions Using Basic Formulae",
    156: "Integration Of Functions Using The Extension Of The Basic",
    157: "Integration Using Substitutions",
    158: "Integration By Parts",
    159: "Integration Using Trigonometric Identities",
    160: "Integration Using Partial Fractions",
    161: "Definite Integrals And The Fundamental Theorem Of The",
    162: "Area Under A Curve",
    163: "Improper Integrals",
    164: "Length Of Arc Of A Curve",
    165: "Volume And Surface Area Of Solids Of Revolution",
    166: "Numerical Integration (Trapezoidal And Simpsons Rules)",
}


def add(signatures: list[str], topic: int, text: str, targets: set[int]) -> None:
    if any(signature in text for signature in signatures):
        targets.add(topic)


def classify(text: str, current_topic: int | None) -> list[int]:
    t = " ".join((text or "").split()).casefold()
    targets: set[int] = set()

    add(["integration by parts", "\\int x \\sin", "\\int x\\sqrt", "reduction formula"], 158, t, targets)
    add(["trapezoidal", "simpson", "seven ordinates", "ordinate", "numerical approximation"], 166, t, targets)
    add(["improper integral", "improper integrals", "convergent", "divergent", "principal value"], 163, t, targets)
    add(["length of the arc", "length of arc", "arc of", "circumference", "cardioid", "cycloid", "spiral of archimedes"], 164, t, targets)
    add(["surface area", "volume generated", "volume of", "spheroid", "solid of revolution", "revolve", "rotat", "solids"], 165, t, targets)
    add(["area under", "area bounded", "area enclosed", "area common", "area of the region", "area between", "area in the", "region bounded", "area included"], 162, t, targets)
    add(["definite integral", "fundamental theorem", "\\int_{", "\\displaystyle\\int_{", "definite integrals"], 161, t, targets)
    add(["partial fraction", "\\frac{x^2+2x+3}{", "\\frac{2x+3}{", "\\frac{x^2}{", "\\frac{6-x}{"], 160, t, targets)
    add(["substitution", "substitutions", "change variable", "\\tan^5 x \\sec", "u="], 157, t, targets)
    add(["trigonometric identities", "sin^3", "sin^2", "cos^2", "cos^3", "sin 4x \\cos", "\\csc^", "\\sec^", "\\sin 3x", "\\cos 3x", "\\cos 4x", "\\sin 4x", "\\int \\sin", "\\int \\cos"], 159, t, targets)
    add(["extension formula", "extension of the basic", "first-degree", "first degree", "5x+2", "4x-1", "basic formula"], 156, t, targets)
    add(["basic formula", "indefinite integral", "\\int \\left(", "find the following indefinite integrals"], 155, t, targets)

    if not targets and current_topic in TOPICS:
        targets.add(current_topic)
    if not targets:
        targets.add(155)
    return sorted(targets)


def main() -> None:
    write = "--write" in sys.argv
    rows = list(
        PrepQuestion.objects.filter(Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID))
        .select_related("topic", "paper")
        .order_by("paper_id", "number", "id")
    )
    plan = []
    for q in rows:
        targets = classify(q.question_latex, q.topic_id if q.topic_id in TOPICS else None)
        plan.append({"id": q.id, "current": q.topic_id, "targets": targets})

    print(f"SMA 200 questions={len(rows)} placements={sum(len(row['targets']) for row in plan)}")
    print("placements per topic:")
    counts = {topic: sum(topic in row["targets"] for row in plan) for topic in TOPICS}
    for topic, title in TOPICS.items():
        print(f"  {topic}: {counts[topic]:3d} {title}")
    unmapped = sum(not row["targets"] for row in plan)
    print(f"unmapped={unmapped}")

    if write:
        OUT.write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"wrote {OUT}")
    else:
        print("DRY RUN - pass --write to create topic_plan_41.json")


if __name__ == "__main__":
    main()
