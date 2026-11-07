"""Classify SMA 335 past-paper questions against the 13 syllabus topics.

Read-only. Splits each question into its lettered parts, assigns every part a set of
topics from explicit mathematical signatures, and reports the union per question with
the evidence that produced it. Nothing is written.
"""
from __future__ import annotations

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

import django  # noqa: E402

django.setup()

from django.db.models import Q  # noqa: E402

from prep.models import PrepQuestion, PrepTopic  # noqa: E402

COURSE_ID = 57

PART_SPLIT_RE = re.compile(r"(?m)^\s*\(?([a-h])[\).]\s*\S")

# (topic, label, compiled signature). A part can match several.
SIGNATURES: list[tuple[int, str, re.Pattern[str]]] = [
    (288, "Bernoulli / linear first order", re.compile(
        r"bernoulli|linear\s+differential\s+equation|"
        r"\\frac\{dy\}\{dx\}\s*\+\s*[^=\n]{0,40}y\s*=|"
        r"\\dfrac\{dy\}\{dx\}\s*\+\s*[^=\n]{0,30}y\s*=|"
        r"(?<!')y'(?!')\s*[-+]\s*[^=\n]{0,30}y\s*=", re.I)),
    (287, "exactness / integrating factor", re.compile(
        r"\bexact(?:ness|ly)?\b|test\s+for\s+exact|integrating\s+factor", re.I)),
    (295, "singular point / Frobenius", re.compile(
        r"singular\s+point|frobenius|regular\s+singular", re.I)),
    (296, "power series", re.compile(
        r"power\s+series|series\s+solution|recurrence\s+relation|about\s+(?:the\s+)?(?:ordinary\s+)?point", re.I)),
    (294, "first-order system", re.compile(
        r"homogeneous\s+system|\\frac\{dx\}\{dt\}|\\frac\{dy\}\{dt\}|\bdx/dt\b|\bdy/dt\b|"
        r"reduce\s+.*\b(?:system|simultaneous)\b|simultaneous\s+(?:differential\s+)?equations", re.I)),
    (291, "particular integral, short method", re.compile(
        r"particular\s+integral|short\s+method|\bshort\s+methods\b", re.I)),
    (292, "variable coefficients / Cauchy-Euler", re.compile(
        r"cauchy|euler\s+equation|variable\s+co-?efficients?|legendre|"
        r"x\s*\^?\s*\{?\s*2\s*\}?\s*y\s*''|"
        r"x\s*\^?\s*\{?\s*2\s*\}?\s*y\s*\"|"
        r"x\s*\^?\s*\{?\s*3\s*\}?\s*y\s*'''|"
        r"x\s*\^?\s*\{?\s*[23]\s*\}?\s*\\frac\{d\^|"
        r"\\frac\{d\^\{?2\}?y\}\{dx\^\{?2\}?\}\s*[-+]|"
        r"d\^\{?2\}?y/dx\^\{?2\}?\s*[-+]|"
        r"x\s*=\s*e\^t", re.I)),
    (290, "non-homogeneous second order", re.compile(
        r"variation\s+of\s+parameters|undetermined\s+co-?efficients?|"
        r"\(D\s*\^?\s*\{?\s*2\s*\}?[^)]*\)\s*y\s*=\s*(?!0\b)\S|"
        r"y''\s*[-+][^=\n]{0,40}=\s*(?!0\b)(?!\s*0\b)\S", re.I)),
    (293, "linear equation of order n", re.compile(
        r"\(D\s*\^?\s*\{?\s*[3-9]\s*\}?[^)]*\)\s*y|"
        r"\(D\s*[-+]\s*\d\s*\)\s*\(D|"
        r"y'''|\\frac\{d\^\{?3\}?y\}\{dx\^\{?3\}?\}|"
        r"one\s+of\s+the\s+roots|auxiliary\s+equation", re.I)),
    (289, "homogeneous second order, constant coefficients", re.compile(
        r"\(D\s*\^?\s*\{?\s*2\s*\}?[^)]*\)\s*y\s*=\s*0|"
        r"y''\s*(?:[-+]\s*\d*\s*y\s*')?\s*(?:[-+]\s*\d*\s*y)?\s*=\s*0", re.I)),
    (297, "application", re.compile(
        r"population|cooling|cooled|newton'?s\s+law|radioactiv|half[- ]?life|\bdecay\b|mixing|"
        r"growth\s+rate|proportional\s+to\s+the\s+(?:number|amount)|dilution|"
        r"electrical\s+circuit|simple\s+harmonic|orthogonal\s+trajector|"
        r"mug\s+of\s+coffee|room\s+at\s+a\s+constant\s+temperature|"
        r"temperature\s+of\s+the\s+(?:body|coffee)", re.I)),
    (172, "separable / homogeneous first order", re.compile(
        r"\bhomogeneo|separable|variables?\s+separable|"
        r"reduce\s+.*homogeneous|"
        r"y\s*=\s*vx|v\s*=\s*y/x|"
        r"\\tan\s*y\s*(?:\\,)?dx|\\sec\^?\{?2\}?\s*y\s*(?:\\,)?dy|"
        r"dy\s*[-+]\s*[^=\n]{0,60}dx\s*=\s*0", re.I)),
    (171, "order/degree/formation/solution ideas", re.compile(
        r"\border\b|\bdegree\b|linearity|primitive|eliminat\w+\s+the\s+arbitrary|"
        r"form\s+the\s+differential\s+equation|wronskian|linearly\s+independent|"
        r"verify\s+that|is\s+a\s+solution|general\s+(?:and\s+singular\s+)?solution|"
        r"singular\s+solution|\by\s*=\s*px\s*\+", re.I)),
]


def split_parts(text: str) -> list[tuple[str, str]]:
    """Return (label, body) for each lettered part, or one whole-body entry."""
    marks = list(PART_SPLIT_RE.finditer(text or ""))
    if len(marks) < 2:
        return [("", text or "")]
    parts = []
    for index, match in enumerate(marks):
        start = match.start()
        end = marks[index + 1].start() if index + 1 < len(marks) else len(text)
        parts.append((match.group(1), text[start:end]))
    return parts


def classify(text: str) -> tuple[set[int], dict[int, list[str]]]:
    evidence: dict[int, list[str]] = defaultdict(list)
    for label, body in split_parts(text):
        for topic, name, pattern in SIGNATURES:
            if pattern.search(body):
                evidence[topic].append(f"{label or 'whole'}:{name}")
    return set(evidence), evidence


def part_snippets(text: str) -> list[str]:
    """Compact one-line rendering of each part, for review."""
    out = []
    for label, body in split_parts(text):
        flat = " ".join((body or "").split())
        out.append(f"({label or '-'}) {flat[:170]}")
    return out


def load_rows() -> tuple[list[dict], dict[int, str]]:
    """Prefer the local cache so analysis does not depend on the flaky database."""
    cache = Path(__file__).resolve().parent / "texts.json"
    if cache.exists():
        data = json.loads(cache.read_text(encoding="utf-8"))
        return data["questions"], {t["id"]: t["title"] for t in data["topics"]}
    rows = (
        PrepQuestion.objects.filter(Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID))
        .distinct()
        .order_by("id")
    )
    questions = [
        {"id": q.id, "topic": q.topic_id, "text": q.question_latex or ""} for q in rows
    ]
    topics = {t.id: t.title for t in PrepTopic.objects.filter(course_id=COURSE_ID)}
    return questions, topics


def main() -> None:
    questions, topics = load_rows()

    result = []
    counts = Counter()
    for q in questions:
        targets, evidence = classify(q["text"])
        if not targets:
            targets = {q["topic"] or 171}
            evidence = {q["topic"] or 171: ["no signature: kept in current topic"]}
        counts.update(targets)
        result.append(
            {
                "id": q["id"],
                "current": q["topic"],
                "targets": sorted(targets),
                "evidence": {str(k): v for k, v in sorted(evidence.items())},
                "parts": part_snippets(q["text"]),
            }
        )

    print("rows:", len(questions))
    print()
    print("questions per topic under this classification")
    for tid, title in sorted(topics.items()):
        print(f"  {tid}  {counts.get(tid, 0):3d}  {title}")

    spread = Counter(len(r["targets"]) for r in result)
    print()
    print("topics per question:", dict(sorted(spread.items())))
    print("extra rows created by cross-listing:", sum(len(r["targets"]) - 1 for r in result))

    unmatched = [r["id"] for r in result if any("no signature" in " ".join(v) for v in r["evidence"].values())]
    print("questions with no signature:", len(unmatched), unmatched[:25])

    decisions = [r for r in result if set(r["targets"]) != {r["current"]}]
    print("questions whose topic set changes:", len(decisions))

    out = Path(__file__).resolve().parent / "topic_plan.json"
    out.write_text(json.dumps(result, indent=1), encoding="utf-8")
    print("plan written:", out)


if __name__ == "__main__":
    main()
