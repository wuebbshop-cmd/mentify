"""Why are SMA 335 topics 171/172 carrying almost every question?

Read-only analysis: lists the topic distribution, then classifies each question in
topics 171/172 against the twelve more specific SMA 335 topics using the mathematical
content of the question rather than its stored topic.
"""
from __future__ import annotations

import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django  # noqa: E402

django.setup()

from django.db.models import Q  # noqa: E402

from prep.models import PrepQuestion, PrepTopic  # noqa: E402

COURSE_ID = 57

# Ordered: the first rule that matches wins, so the most specific signature is first.
RULES: list[tuple[int, str, re.Pattern[str]]] = [
    (288, "Bernoulli", re.compile(r"bernoulli", re.I)),
    (287, "integrating factor / exact", re.compile(r"integrating\s+factor|\bexact(?:ness)?\b|test\s+for\s+exact", re.I)),
    (296, "power series", re.compile(r"power\s+series|series\s+solution|frobenius|about\s+the\s+(?:ordinary\s+)?point|recurrence\s+relation", re.I)),
    (294, "system reduction", re.compile(r"homogeneous\s+system|\bsystem\b.*\b(?:dx/dt|dy/dt)|reduc\w*\s+.*first\s+order\s+system", re.I)),
    (290, "second order non-homogeneous", re.compile(
        r"variation\s+of\s+parameters|undetermined\s+co-?efficients|particular\s+(?:integral|solution)", re.I)),
    (291, "short methods for particular integrals", re.compile(r"short\s+method|\bD-?operator\b", re.I)),
    (297, "applications", re.compile(
        r"population|cool|cooling|radioactiv|decay|half[- ]life|newton'?s\s+law|orthogonal\s+trajector|"
        r"mixing|compound\s+interest|growth\s+rate|dilution|electrical\s+circuit|simple\s+harmonic", re.I)),
    (292, "second order variable coefficients", re.compile(
        r"cauchy[- ]euler|x\^?\{?2\}?\s*(?:y''|\\frac\{d\^2)|euler\s+equation|variable\s+co-?efficients", re.I)),
    (293, "linear equations of order n", re.compile(r"\(D\^?\{?[3-9]|D\^?\{?\\?[3-9]\}?|order\s+(?:three|four|n\b)|auxiliary\s+equation", re.I)),
    (289, "second order homogeneous", re.compile(
        r"\(D\^?\{?2\}?[^)]*\)\s*y\s*=\s*0|y''\s*[-+]\s*\d*\s*y'\s*[-+]\s*\d*\s*y\s*=\s*0|second\s+order", re.I)),
    (172, "first order separable / homogeneous", re.compile(
        r"\bhomogeneo|\bseparable|variables?\s+separable|\\frac\{dy\}\{dx\}|\bdy\b.*\bdx\b", re.I)),
    (171, "order / degree / formation / general solution", re.compile(
        r"\border\b|\bdegree\b|linearity|primitive|eliminat|form\s+the\s+differential|wronskian|"
        r"verify\s+that|is\s+a\s+solution", re.I)),
]


def classify(text: str) -> list[int]:
    hits = [topic for topic, _label, pattern in RULES if pattern.search(text or "")]
    return hits or [171]


def main() -> None:
    topics = {t.id: t.title for t in PrepTopic.objects.filter(course_id=COURSE_ID)}
    rows = list(
        PrepQuestion.objects.filter(Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID))
        .select_related("paper")
        .distinct()
        .order_by("id")
    )
    print("current distribution")
    for tid, title in sorted(topics.items()):
        print(f"  {tid}  {sum(1 for q in rows if q.topic_id == tid):3d}  {title}")

    print()
    print("proposed home for questions currently in 171/172")
    moved = defaultdict(list)
    multi = 0
    for q in rows:
        if q.topic_id not in (171, 172):
            continue
        hits = classify(q.question_latex or "")
        primary = hits[0]
        if len(hits) > 1:
            multi += 1
        moved[primary].append(q.id)
    for tid, ids in sorted(moved.items(), key=lambda kv: -len(kv[1])):
        print(f"  {tid}  {len(ids):3d}  {topics.get(tid, '?')}")

    print()
    print(f"questions touching more than one topic: {multi}")
    print(f"total currently in 171/172: {sum(len(v) for v in moved.values())}")

    print()
    print("sample of the biggest moves")
    for tid, ids in sorted(moved.items(), key=lambda kv: -len(kv[1]))[:5]:
        if tid in (171, 172):
            continue
        print("=" * 90)
        print(f"-> {tid} {topics.get(tid)}  ({len(ids)} questions) e.g. {ids[:4]}")
        for qid in ids[:2]:
            q = next(r for r in rows if r.id == qid)
            print("   ", (q.question_latex or "")[:230].replace("\n", " "))


if __name__ == "__main__":
    main()
