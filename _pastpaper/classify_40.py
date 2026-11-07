"""Generate a multi-topic placement plan for SST 101 past-paper questions.

Each target must be backed by wording in the question itself. The script is
reviewable and dry-run by default; it is separate from the database applicator.
"""

import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache_40.json"
OUT = HERE / "topic_plan_40.json"

TOPICS = {
    140: "Introduction To Statistics And Probability",
    141: "Types Of Data",
    142: "Data Collection Methods",
    143: "Data Representation",
    144: "Measures Of Central Tendency",
    145: "Measures Of Dispersion",
    146: "Probability Concepts",
    147: "Probability Distributions",
    148: "Sampling Techniques",
    149: "Estimation And Confidence Intervals",
    150: "Hypothesis Testing",
    151: "Correlation And Regression",
    152: "Skewness And Kurtosis",
    153: "Moments",
    154: "Uses Of Statistics In Real Life",
}

PATTERNS = {
    140: [
        r"\bstatistics\b.*\bdefinitions?\b",
        r"\bparameter\b.*\bstatistic\b",
        r"\buses of statistics\b",
        r"\bdistinguish between categorical data and numerical data\b",
    ],
    141: [
        r"\bcategorical\b|\bnumerical data\b|\bqualitative\b|\bquantitative\b",
        r"\bcontinuous\b|\bdiscrete\b|\bnominal\b|\bordinal\b|\btypes of data\b",
    ],
    142: [
        r"\bsurvey\b|\bquestionnaire\b|\bdata collection\b|\bcollected data\b",
        r"\bfamilies was surveyed\b|\bdata were (?:collected|recorded)\b",
    ],
    143: [
        r"\bstem[- ]and[- ]leaf\b|\bhistogram\b|\bfrequency polygon\b|\bogive\b",
        r"\bfrequency distribution\b|\bfrequency table\b|\bgrouped data\b|\bcumulative frequency\b",
        r"\bclass boundaries\b|\bclass intervals?\b|\bconstruct a table\b|\btabulate\b",
    ],
    144: [
        r"\bmean\b|\bmedian\b|\bmode\b|\baverage\b|\barithmetic mean\b|\bgeometric mean\b",
        r"\bquartile\b|\bmeasures of central tendency\b",
    ],
    145: [
        r"\bvariance\b|\bstandard deviation\b|\bcoefficient of variation\b|\bdispersion\b",
        r"\bquartile deviation\b|\binterquartile range\b|\bsemi-interquartile\b|\brange\b",
    ],
    146: [
        r"\bprobability\b|\bevent(s)?\b|\bconditional probability\b|\bbayes\b",
        r"\bmutually exclusive\b|\bindependent events?\b|\bwith replacement\b|\bwithout replacement\b",
        r"\bdice\b|\bdie\b|\bcoin(s)?\b|\bballs?\b|\bour?\b",
    ],
    147: [
        r"\brandom variable\b|\bprobability distribution\b|\bbinomial distribution\b",
        r"\bpoisson\b|\bnormal distribution\b|\bbernoulli\b|\bexpected value\b|\bexpectation\b",
    ],
    148: [
        r"\bsampling\b|\bsample\b|\bsampled\b|\brandom sample\b|\brandomly selected\b",
        r"\bstratified\b|\bsystematic sample\b|\bcluster sample\b|\bpopulation\b",
    ],
    149: [
        r"\bconfidence interval\b|\bconfidence level\b|\bmargin of error\b|\bestimator\b|\bunbiased estimator\b",
    ],
    150: [
        r"\bhypothesi(s|es)\b|\bnull hypothesis\b|\balternative hypothesis\b|\bsignificance level\b",
        r"\bcritical value\b|\btest statistic\b|\breject the hypothesis\b|\btest of hypothesis\b",
    ],
    151: [
        r"\bcorrelation\b|\bregression\b|\bleast squares\b|\bscatter diagram\b|\bscatter plot\b",
        r"\brank correlation\b|\bspearman\b|\bpearson\b|\bcovariance\b|\brelationship\b",
    ],
    152: [
        r"\bskewness\b|\bkurtosis\b|\bpeakedness\b|\bshape\b|\bsymmetric\b",
    ],
    153: [
        r"\bmoment(s)?\b|\bmoment about\b|\bcentral moment\b|\bmoment coefficient\b",
    ],
    154: [
        r"\breal[- ]life\b|\beveryday situation\b|\bpractical application\b|\bapplications?\b",
    ],
}


MANUAL_OVERRIDES = {
    810: [143],
    811: [143],
    812: [143],
    816: [151],
    792: [151],
    821: [151],
    838: [151],
    839: [143, 144, 145, 152],
    1255: [143, 144, 145, 152, 153],
}


def classify(text: str) -> list[int]:
    normalized = " ".join((text or "").lower().replace("\\(", "$").replace("\\)", "$").split())
    targets = []
    for topic_id in sorted(PATTERNS):
        if any(re.search(pattern, normalized) for pattern in PATTERNS[topic_id]):
            targets.append(topic_id)
    return targets


def main() -> None:
    data = json.loads(CACHE.read_text(encoding="utf-8"))
    plan = []
    for question in data["questions"]:
        targets = MANUAL_OVERRIDES.get(question["id"], classify(question["text"]))
        evidence = {}
        normalized = " ".join((question["text"] or "").lower().replace("\\(", "$").replace("\\)", "$").split())
        for topic_id in targets:
            matches = []
            for pattern in PATTERNS[topic_id]:
                if re.search(pattern, normalized):
                    matches.append(pattern)
            evidence[str(topic_id)] = matches or ["manual review override"]
        plan.append(
            {
                "id": question["id"],
                "targets": targets,
                "evidence": evidence,
                "current": question.get("topic"),
            }
        )
    OUT.write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
    counts = {}
    unmapped = []
    for row in plan:
        if not row["targets"]:
            unmapped.append(row["id"])
        for topic in row["targets"]:
            counts[topic] = counts.get(topic, 0) + 1
    print(f"questions={len(plan)} unmapped={len(unmapped)} plan={OUT}")
    print("placements:", " ".join(f"{topic}:{counts.get(topic, 0)}" for topic in TOPICS))
    if unmapped:
        print("unmapped ids:", unmapped)


if __name__ == "__main__":
    main()
