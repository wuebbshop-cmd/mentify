"""Order-aware topic classifier for SMA 335.

The regex-only approach could not separate "linear first order" from a second-order
equation that merely contains a ``y'`` term, so the order of the equation is detected
first and the topic rules are then applied within that order. Analysis only; writes
nothing but the plan file.
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

from prep.models import PrepQuestion, PrepTopic  # noqa: E402

COURSE_ID = 57
PART_SPLIT_RE = re.compile(r"(?m)^\s*\(?([a-h])[\).]\s*\S")

THIRD = re.compile(
    r"y'''|d\^\{?3\}?y|\\frac\{d\^\{?3\}?y\}|d\^3y|"
    r"\(D\s*\^?\s*\{?\s*[3-9]\s*\}?|\(D\s*[-+]\s*\w\s*\)\s*\(D|"
    r"\bd\s*[3-9]\s*y\b",
    re.I,
)
SECOND = re.compile(
    r"y''|y\"|d\^\{?2\}?y|\\frac\{d\^\{?2\}?y\}|d\^2y|\\dfrac\{d\^\{?2\}?y\}|"
    r"\(D\s*\^?\s*\{?\s*2\s*\}?|\(D\s*\^?\s*2\b|\bd\s*2\s*y\b",
    re.I,
)
FIRST = re.compile(r"(?<!')(?:y'|\\frac\{dy\}\{dx\}|\\dfrac\{dy\}\{dx\}|dy\s*/\s*dx)(?!')", re.I)

VARIABLE_COEFF = re.compile(
    r"cauchy|euler\s+equation|variable\s+co-?efficients?|legendre|"
    r"x\s*\^?\s*\{?\s*[23]\s*\}?\s*(?:y|\\frac|d)|x\s*=\s*e\^t", re.I
)
EXACT = re.compile(r"\bexact(?:ness|ly)?\b|integrating\s+factor", re.I)
BERNOULLI = re.compile(r"bernoulli", re.I)
LINEAR_FORM = re.compile(
    r"linear\s+differential\s+equation|"
    r"\\frac\{dy\}\{dx\}\s*\+\s*[^=\n]{0,40}y\s*=|"
    r"\\dfrac\{dy\}\{dx\}\s*\+\s*[^=\n]{0,40}y\s*=|"
    r"(?<!')y'(?!')\s*[-+]\s*[^=\n]{0,30}y\s*=",
    re.I,
)
HOMOGENEOUS_OR_SEPARABLE = re.compile(
    r"\bhomogeneo|separable|variables?\s+separable|reduce\s+.*homogeneous|"
    r"y\s*=\s*vx|v\s*=\s*y/x|\\tan\s*y\s*(?:\\,)?dx|\\sec\^?\{?2\}?\s*y\s*(?:\\,)?dy",
    re.I,
)
APPLICATION = re.compile(
    r"population|cooling|cooled|newton'?s\s+law|radioactiv|half[- ]?life|\bdecay\b|mixing|"
    r"growth\s+rate|proportional\s+to\s+the\s+(?:number|amount)|dilution|electrical\s+circuit|"
    r"simple\s+harmonic|orthogonal\s+trajector|mug\s+of\s+coffee|"
    r"room\s+at\s+a\s+constant\s+temperature|temperature\s+of\s+the\s+(?:body|coffee)",
    re.I,
)
POWER_SERIES = re.compile(r"power\s+series|series\s+solution|recurrence\s+relation", re.I)
SINGULAR = re.compile(r"singular\s+point|frobenius|regular\s+singular", re.I)
SYSTEM = re.compile(
    r"homogeneous\s+system|\\frac\{dx\}\{dt\}|\\frac\{dy\}\{dt\}|\bdx/dt\b|\bdy/dt\b|"
    r"simultaneous\s+(?:differential\s+)?equations",
    re.I,
)
SHORT_METHOD = re.compile(r"particular\s+integral|short\s+method", re.I)
NONHOMOGENEOUS_METHOD = re.compile(
    r"variation\s+of\s+parameters|undetermined\s+co-?efficients?", re.I
)
CONCEPTUAL = re.compile(
    r"\border\b|\bdegree\b|linearity|primitive|eliminat\w+\s+the\s+arbitrary|"
    r"form\s+the\s+differential\s+equation|wronskian|linearly\s+independent|"
    r"verify\s+that|\bis\s+a\s+solution\b|singular\s+solution|\by\s*=\s*px\s*\+",
    re.I,
)


def has_nonzero_rhs(body: str) -> bool:
    """True when a D-operator equation is given a right-hand side that is not zero.

    Only the ``(D^2 + ...)y = ...`` form is inspected. A general ``=`` scan is
    unreliable: it reads the given relation ``Ax^2 + By^2 = 1`` and the ansatz
    ``y = c1 y1 + c2 y2`` as right-hand sides.
    """
    for match in re.finditer(r"\)\s*y\s*=\s*([^\n]{1,60})", body):
        rhs = match.group(1).strip()
        if rhs and not re.match(r"^0\b", rhs):
            return True
    return False


def classify_part(body: str) -> set[int]:
    topics: set[int] = set()
    order = 3 if THIRD.search(body) else (2 if SECOND.search(body) else 1)

    if APPLICATION.search(body):
        topics.add(297)
    if SYSTEM.search(body):
        topics.add(294)
    if SINGULAR.search(body):
        topics.add(295)
    if POWER_SERIES.search(body):
        topics.add(296)
    if EXACT.search(body):
        topics.add(287)
    if BERNOULLI.search(body) or (order == 1 and LINEAR_FORM.search(body)):
        topics.add(288)
    if order == 1 and HOMOGENEOUS_OR_SEPARABLE.search(body):
        topics.add(172)
    if order == 2:
        if VARIABLE_COEFF.search(body):
            topics.add(292)
        if SHORT_METHOD.search(body):
            # "Find the particular integral" is both the method topic and the
            # non-homogeneous topic, so it belongs in both.
            topics.add(291)
            topics.add(290)
        elif NONHOMOGENEOUS_METHOD.search(body) or has_nonzero_rhs(body):
            topics.add(290)
        elif not VARIABLE_COEFF.search(body):
            topics.add(289)
    if order >= 3:
        topics.add(293)
        if SHORT_METHOD.search(body):
            topics.add(291)
    if CONCEPTUAL.search(body):
        topics.add(171)
    if not topics:
        topics.add(171 if order >= 2 else 172)
    return topics


def split_parts(text: str) -> list[tuple[str, str]]:
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
        for topic in sorted(classify_part(body)):
            evidence[topic].append(label or "whole")
    return set(evidence), evidence


def part_snippets(text: str) -> list[str]:
    return [
        f"({label or '-'}) " + " ".join((body or "").split())[:170]
        for label, body in split_parts(text)
    ]


def load_rows() -> tuple[list[dict], dict[int, str]]:
    cache = Path(__file__).resolve().parent / "texts.json"
    if cache.exists():
        data = json.loads(cache.read_text(encoding="utf-8"))
        return data["questions"], {t["id"]: t["title"] for t in data["topics"]}
    rows = PrepQuestion.objects.filter(topic__course_id=COURSE_ID).order_by("id")
    questions = [{"id": q.id, "topic": q.topic_id, "text": q.question_latex or ""} for q in rows]
    topics = {t.id: t.title for t in PrepTopic.objects.filter(course_id=COURSE_ID)}
    return questions, topics


def main() -> None:
    questions, topics = load_rows()
    result, counts = [], Counter()
    for q in questions:
        targets, evidence = classify(q["text"])
        if not targets:
            targets = {q["topic"] or 171}
            evidence = {q["topic"] or 171: ["no signature"]}
        counts.update(targets)
        result.append(
            {
                "id": q["id"],
                "current": q["topic"],
                "targets": sorted(targets),
                "evidence": {str(k): sorted(set(v)) for k, v in sorted(evidence.items())},
                "parts": part_snippets(q["text"]),
            }
        )

    print(f"rows: {len(questions)}")
    print()
    for tid, title in sorted(topics.items()):
        print(f"  {tid}  {counts.get(tid, 0):3d}  {title}")
    print()
    print("topics per question:", dict(sorted(Counter(len(r["targets"]) for r in result).items())))
    print("extra rows from cross-listing:", sum(len(r["targets"]) - 1 for r in result))
    print(
        "no signature:",
        len([r for r in result if any("no signature" in v for v in r["evidence"].values())]),
    )
    print("topic set changes:", len([r for r in result if set(r["targets"]) != {r["current"]}]))
    out = Path(__file__).resolve().parent / "topic_plan.json"
    out.write_text(json.dumps(result, indent=1), encoding="utf-8")
    print("plan written:", out)


if __name__ == "__main__":
    main()
