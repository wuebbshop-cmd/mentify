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

COURSE_ID = 43

TOPIC_RE = [
    (243, ("reciprocal",)),
    (242, (
        "dot product", "cross product", "vector product", "triple product",
        "parallelepiped", "area of the triangle", "area triangle", "projection",
        "orthogonal", "commutative", "distributive", "coplanar",
        "scalar and a vector", "resultant vector", "magnitude of the vector",
        "a \\cdot b", "a \\times b", "\\wedge b",
    )),
    (244, (
        "differential equation", "acceleration", "velocity", "unit tangent",
        "principal normal", "binormal", "directional derivative", "gradient",
        "divergence", "curl", "laplacian", "conservative", "irrotational",
        "solenoidal", "scalar potential", "position vector", "\\vec{r}(t)",
        "d\\vec{r}", "d r", "space curve", "parametric equation",
        "div\\, r", "div r",
    )),
    (245, (
        "green's theorem", "green theorem", "stokes", "stoke's",
        "divergence theorem", "gauss", "line integral", "\\oint_c",
        "\\oint_C", "\\int_c", "\\int_C", "surface integral", "work done",
    )),
    (246, (
        "curvilinear", "cylindrical coordinate", "spherical coordinate",
        "scale factor", "orthogonal coordinate", "jacobian",
    )),
]


def main() -> None:
    rows = (
        PrepQuestion.objects
        .filter(Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID))
        .exclude(reconstruction_metadata__cross_listed_from__isnull=False)
        .order_by("id")
    )
    plan = []
    for q in rows:
        text = (q.question_latex or "").casefold()
        targets = set()
        for topic_id, needles in TOPIC_RE:
            if any(needle.casefold() in text for needle in needles):
                targets.add(topic_id)
        if not targets and q.topic_id:
            targets.add(q.topic_id)
        if not targets:
            targets.add(241)
        plan.append({"id": q.id, "targets": sorted(targets)})

    out = BASE_DIR / "_pastpaper" / f"topic_plan_{COURSE_ID}.json"
    out.write_text(json.dumps(plan, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {out}: {len(plan)} questions")


if __name__ == "__main__":
    main()
