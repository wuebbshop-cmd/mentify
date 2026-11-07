"""Topic classifier for SST 204 (Probability and Statistics 1), course 46.

Works on the distinct statements: 528 rows collapse to 232 unique questions, and each
unique question gets one decision that is then applied to every row that repeats it.

Only explicit evidence is used - a topic is added when the statement actually asks about
it. Nothing is invented, and a question with no recognisable signature keeps its current
topic. Analysis only; writes the plan file.
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
sys.stdout = __import__("io").TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import django  # noqa: E402

django.setup()

COURSE_ID = 46
HERE = Path(__file__).resolve().parent

RANDOM_VARIABLES = 179
DISTRIBUTION_FUNCTIONS = 180
MODE_MEDIAN = 181
EXPECTATION = 182
MOMENTS_VARIANCE = 183
MGF_PGF = 184
SPECIAL_DISCRETE = 185
POISSON = 186
NORMAL = 187
GAMMA_EXP_BETA = 188
CHANGE_OF_VARIABLE = 189

_MARKER = re.compile(r"^(?:[\s:;,.()\[\]|*_#-]+|\(\s*[a-z0-9]{1,3}\s*\)|[a-z0-9]{1,3}\s*[).:]\s*)+", re.I)

ASK = r"(?:find|calculate|compute|determine|obtain|evaluate|derive|work\s+out|hence\s+(?:find|compute|calculate|determine)|state|write\s+down|give)"

RULES: list[tuple[int, re.Pattern[str]]] = [
    (POISSON, re.compile(r"\bpoisson\b", re.I)),
    (
        SPECIAL_DISCRETE,
        re.compile(
            r"\bbinomial\b|\bgeometric\b|hyper-?geometric|negative\s+binomial|"
            r"discrete\s+uniform|uniform\s+distribution|bernoulli",
            re.I,
        ),
    ),
    (
        NORMAL,
        re.compile(
            r"\bnormal(?:ly)?\b(?!\s+approximation)|standard\s+normal|\bz-?scores?\b|gaussian|"
            r"N\s*\(\s*0\s*,\s*1\s*\)",
            re.I,
        ),
    ),
    (
        GAMMA_EXP_BETA,
        re.compile(
            r"gamma\s+distribution|gamma\s+random|exponential\s+distribution|exponentially\s+distributed|"
            r"exponential\s+random|has\s+an\s+exponential|beta\s+distribution|beta\s+random|"
            r"waiting\s+time\s+is\s+exponential",
            re.I,
        ),
    ),
    (
        MGF_PGF,
        re.compile(
            r"moment\s+generating|m\.\s?g\.\s?f|probability\s+generating|p\.\s?g\.\s?f|"
            r"generating\s+function|(?-i:\bM_?\{?X\}?\s*\(\s*t\s*\))|(?-i:\bG\s*\(\s*t\s*\))",
            re.I,
        ),
    ),
    (
        CHANGE_OF_VARIABLE,
        re.compile(
            r"change\s+of\s+variable|jacobian|transformation\s+of\s+(?:a\s+)?(?:random\s+variable|variables)|"
            r"(?:density|distribution)\s+of\s+(?:the\s+random\s+variable\s+)?\$?Y\$?\b|(?-i:\bY\s*=\s*X)",
            re.I,
        ),
    ),
    (MODE_MEDIAN, re.compile(r"\bmode\b|\bmodal\b|\bmedian\b|\bquartiles?\b|\bpercentiles?\b", re.I)),
    (
        MOMENTS_VARIANCE,
        re.compile(
            ASK + r"[^.]{0,90}(?:variance|standard\s+deviation|second\s+moment|coefficient\s+of\s+variation)"
            r"|(?-i:\b[Vv]ar\s*\(\s*X)|coefficient\s+of\s+variation|skewness|"
            r"variance\s+of\s+(?:the\s+)?(?:random\s+variable\s+)?(?-i:\$?[XY]\$?)\b|"
            r"(?:mean|expectation)\s+and\s+variance",
            re.I,
        ),
    ),
    (
        EXPECTATION,
        re.compile(
            ASK + r"[^.]{0,90}(?:mean|expectation|expected\s+value)"
            r"|expected\s+(?:number|profit|value|gain|return|amount|cost|loss|daily|weekly|monthly)"
            r"|(?-i:\bE\s*\(\s*X)|(?-i:\bE\s*\(\s*Y)"
            r"|mean\s+of\s+(?:the\s+)?(?:random\s+variable|\$?X\$?)",
            re.I,
        ),
    ),
    (
        DISTRIBUTION_FUNCTIONS,
        re.compile(
            r"cumulative\s+(?:distribution|function)|distribution\s+function|\bc\.\s?d\.\s?f\b|"
            r"(?-i:\bF\s*\(\s*x\s*\))|find\s+the\s+distribution\s+of",
            re.I,
        ),
    ),
    (
        RANDOM_VARIABLES,
        re.compile(
            r"discrete\s+and\s+continuous|"
            + ASK
            + r"[^.]{0,60}value\s+of\s+(?:the\s+)?(?:constant\s+)?\$?k"
            r"|state\s+(?:two|the)\s+conditions?|is\s+a\s+(?:valid\s+)?probability|"
            r"valid\s+probability\s+(?:density|distribution|function)|"
            r"probability\s+distribution\s+of\s+(?:the\s+)?(?:random\s+variable\s+)?(?-i:\$?X\$?)|"
            r"obtain\s+the\s+(?:probability\s+)?distribution\s+of|"
            r"construct\s+the\s+(?:probability\s+)?distribution|"
            r"conditions?\s+(?:for|that)\s+(?:a\s+)?(?:function\s+)?(?-i:\$?f\s*\(\s*x\s*\))",
            re.I,
        ),
    ),
]



def signature(text: str) -> str:
    return _MARKER.sub("", " ".join((text or "").split()).casefold())


# Topics with unmistakable vocabulary. A question may keep its current topic when the
# evidence is merely incomplete, but it cannot stay on one of these without the words.
UNAMBIGUOUS = {MGF_PGF, CHANGE_OF_VARIABLE}
# Distribution topics: staying on a different distribution than the one stated is wrong.
DISTRIBUTION_TOPICS = {SPECIAL_DISCRETE, POISSON, NORMAL, GAMMA_EXP_BETA}


def resolve(current: int | None, detected: set[int]) -> list[int]:
    if not detected:
        return [current] if current else [RANDOM_VARIABLES]
    targets = set(detected)
    if current and current not in detected:
        contradicts = (current in UNAMBIGUOUS) or (
            current in DISTRIBUTION_TOPICS and (detected & DISTRIBUTION_TOPICS)
        )
        if not contradicts:
            targets.add(current)
    return sorted(targets)


def classify(text: str) -> tuple[set[int], dict[int, list[str]]]:
    evidence: dict[int, list[str]] = defaultdict(list)
    for topic, pattern in RULES:
        for match in pattern.finditer(text or ""):
            snippet = match.group(0).strip()
            if snippet and snippet.lower() not in evidence[topic]:
                evidence[topic].append(snippet.lower())
    return set(evidence), evidence



def main() -> None:
    data = json.loads((HERE / f"cache_{COURSE_ID}.json").read_text(encoding="utf-8"))
    titles = {t["id"]: t["title"] for t in data["topics"]}

    groups: dict[str, list[dict]] = defaultdict(list)
    for q in data["questions"]:
        groups[signature(q["text"])].append(q)

    plan, counts, no_signal = [], Counter(), []
    for sig, rows in groups.items():
        current = Counter(r["topic"] for r in rows).most_common(1)[0][0]
        detected, evidence = classify(rows[0]["text"])
        targets = resolve(current, detected)
        if not detected:
            evidence = {sorted(targets)[0]: ["no signature - current topic kept"]}
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
    print()
    for tid, title in sorted(titles.items()):
        print(f"  {tid}  {counts.get(tid, 0):4d}  {title}")
    print()
    print("topics per question:", dict(sorted(Counter(len(p['targets']) for p in plan if p['id'] in [r['id'] for r in data['questions']]).items())))
    print("questions with no signature (kept as-is):", len(no_signal))
    print("rows changing topic:", len([p for p in plan if set(p["targets"]) != {p["current"]}]))
    print("extra rows from cross-listing:", sum(len(p["targets"]) - 1 for p in plan))

    out = HERE / f"topic_plan_{COURSE_ID}.json"
    out.write_text(json.dumps(plan, indent=1), encoding="utf-8")
    print("plan written:", out)


if __name__ == "__main__":
    main()
