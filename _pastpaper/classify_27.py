"""Topic classifier for SST 305 (Statistical Estimation), course 27.

Each question is posted into every topic its parts actually exercise: a question that asks
for a maximum-likelihood estimate and then for its bias belongs on both pages. Interval
estimation topics overlap by design (46 vs 52 vs 53), so a confidence-interval question is
assigned to exactly one of them - two-sample to 53, known population sigma to 46, the rest
to 52.

Usage: python _pastpaper/classify_27.py   (writes topic_plan_27.json)
"""
from __future__ import annotations

import io
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
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import django  # noqa: E402

django.setup()

COURSE_ID = 27
HERE = Path(__file__).resolve().parent

PROPERTIES = 45
CONFIDENCE_MEAN = 46
SUFFICIENCY = 47
MOMENTS = 48
MLE = 49
LEAST_SQUARES = 50
MIN_VARIANCE = 51
INTERVAL = 52
TWO_MEANS = 53
INTERVAL_TOPICS = {CONFIDENCE_MEAN, INTERVAL, TWO_MEANS}

_MARKER = re.compile(r"^(?:[\s:;,.()\[\]|*_#-]+|\(\s*[a-z0-9]{1,3}\s*\)|[a-z0-9]{1,3}\s*[).:]\s*)+", re.I)

PATTERNS: dict[int, re.Pattern[str]] = {
    PROPERTIES: re.compile(
        r"unbias|consisten(?:cy|t)|efficien|\bMSE\b|mean\s+squared\s+error|"
        r"properties?\s+of\s+(?:a\s+)?(?:good\s+|an\s+)?estimator|"
        r"define\s+(?:an?\s+)?(?:unbiased|relative|efficient)|"
        r"show\s+that\s+\S+\s+is\s+(?:an?\s+)?unbiased|asymptotically",
        re.I,
    ),
    SUFFICIENCY: re.compile(
        r"sufficien|factorization\s+theorem|rao-?blackwell|minimal\s+sufficient", re.I
    ),
    MOMENTS: re.compile(r"method\s+of\s+moments?|moment\s+(?:estimator|estimation)", re.I),
    MLE: re.compile(r"maximum\s+likelihood|log-?likelihood|likelihood\s+function|\bMLE\b", re.I),
    LEAST_SQUARES: re.compile(
        r"least\s+squares?|normal\s+equations?|regression\s+(?:line|coefficients?)|"
        r"line\s+of\s+best\s+fit",
        re.I,
    ),
    MIN_VARIANCE: re.compile(
        r"cramer-?rao|minimum\s+variance|best\s+unbiased|\bMVUE\b|lower\s+bound|"
        r"efficient\s+estimator|attains?\s+the\s+bound",
        re.I,
    ),
    INTERVAL: re.compile(
        r"confidence\s+(?:interval|limits?|coefficient)|interval\s+estimat|"
        r"degrees?\s+of\s+freedom|t-?distribution|t-?value|pivotal",
        re.I,
    ),
    TWO_MEANS: re.compile(
        r"two\s+independent\s+(?:random\s+)?(?:samples|populations|groups|processes|types)|"
        r"independent\s+random\s+samples\s+from\s+two|"
        r"difference\s+between\s+(?:the\s+)?(?:two\s+)?(?:means|averages)|"
        r"independent\s+random\s+samples\s+are\s+taken\s+from\s+(?:each|two)",
        re.I,
    ),
}

PAIRED_SAMPLE_MEANS = re.compile(r"\\bar\s*\{?\s*[xy]\s*\}?\s*_?\s*\{?\s*[12]\s*\}?", re.I)


def is_two_sample(text: str) -> bool:
    if PATTERNS[TWO_MEANS].search(text):
        return True
    means = {m.group(0).replace(" ", "").lower() for m in PAIRED_SAMPLE_MEANS.finditer(text)}
    return len(means) >= 2


KNOWN_SIGMA = re.compile(
    r"known\s+(?:population\s+)?standard\s+deviation|standard\s+deviation\s+(?:is\s+)?known|"
    r"known\s+\$?\\?sigma|\\sigma\s*=\s*\d|population\s+standard\s+deviation\s*(?:of|=|\$?\\?sigma)",
    re.I,
)
UNKNOWN_SIGMA = re.compile(
    r"unknown\s+(?:population\s+)?(?:variance|standard\s+deviation)|sample\s+(?:variance|standard\s+deviation)|"
    r"\\bar\{?s\}?\s*\^?2|s\^2|degrees\s+of\s+freedom",
    re.I,
)


def signature(text: str) -> str:
    return _MARKER.sub("", " ".join((text or "").split()).casefold())


def classify(text: str, current: int | None = None) -> tuple[list[int], dict[int, list[str]]]:
    evidence: dict[int, list[str]] = defaultdict(list)
    interval_evidence = []
    for topic, pattern in PATTERNS.items():
        for match in pattern.finditer(text or ""):
            snippet = match.group(0).strip().lower()
            if topic in INTERVAL_TOPICS:
                if snippet not in interval_evidence:
                    interval_evidence.append(snippet)
            elif snippet not in evidence[topic]:
                evidence[topic].append(snippet)

    if interval_evidence:
        if is_two_sample(text or ""):
            chosen = TWO_MEANS
        elif current in INTERVAL_TOPICS:
            chosen = current
        elif KNOWN_SIGMA.search(text or "") and not UNKNOWN_SIGMA.search(text or ""):
            chosen = CONFIDENCE_MEAN
        else:
            chosen = INTERVAL
        evidence[chosen] = interval_evidence

    return sorted(evidence), evidence


def main() -> None:
    data = json.loads((HERE / f"cache_{COURSE_ID}.json").read_text(encoding="utf-8"))
    titles = {t["id"]: t["title"] for t in data["topics"]}

    groups: dict[str, list[dict]] = defaultdict(list)
    for q in data["questions"]:
        groups[signature(q["text"])].append(q)

    plan, counts, no_signal = [], Counter(), []
    for sig, rows in groups.items():
        current = Counter(r["topic"] for r in rows).most_common(1)[0][0]
        targets, evidence = classify(rows[0]["text"], current)
        if not targets:
            targets = [current] if current else [PROPERTIES]
            evidence = {targets[0]: ["no signature - current topic kept"]}
            no_signal.append(rows[0]["id"])
        counts.update(targets)
        for r in rows:
            plan.append(
                {
                    "id": r["id"],
                    "current": r["topic"],
                    "targets": sorted(targets),
                    "evidence": {str(k): v for k, v in sorted(evidence.items())},
                    "parts": [" ".join((r["text"] or "").split())[:160]],
                }
            )

    print(f"rows: {len(data['questions'])}  distinct statements: {len(groups)}")
    for tid, title in sorted(titles.items()):
        print(f"  {tid}  {counts.get(tid, 0):3d}  {title}")
    print()
    distinct_plans = len({tuple(sorted((p['targets']))) for p in plan})
    print("distinct target sets:", distinct_plans)
    print("questions with no signature (kept as-is):", len(no_signal))
    print("rows changing primary topic:", len([p for p in plan if p['current'] not in p['targets']]))
    print("extra rows from cross-listing:", sum(len(p["targets"]) - 1 for p in plan))

    out = HERE / f"topic_plan_{COURSE_ID}.json"
    out.write_text(json.dumps(plan, indent=1), encoding="utf-8")
    print("plan written:", out)


if __name__ == "__main__":
    main()

