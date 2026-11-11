"""Surgical repair of SMA 330 past-paper rows."""

from __future__ import annotations

import argparse
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

COURSE_ID = 48
HERE = Path(__file__).resolve().parent
BACKUP = HERE / "sma330_repair_backup.json"
PLAN = HERE / "topic_plan_48.json"

DELETE_IDS = {
    1699, 1700, 1701, 1702, 1703,
    1731, 1732, 1828,
    1750, 1751, 1752, 1753, 1754, 1829, 1830,
}

PROMOTE_IDS = {
    1342, 1343, 1346, 1347,
    1679, 1693, 1709, 1712,
    1744, 1760, 1763,
    1827, 1836, 1839,
}

DELETE_SOURCE_IDS = {
    1046, 1047, 1081, 1083,
    1678, 1692, 1708, 1711,
    1725, 1743, 1759, 1762, 1835, 1838,
}

MANUAL_TOPIC_TARGETS = {
    1044: [197, 202, 205, 206],
    1045: [198, 201, 202, 205],
    1048: [205, 206],
    1079: [197, 198, 201, 204],
    1080: [197, 202, 203, 204],
    1082: [199, 203, 205, 206],
    1342: [199, 201, 205],
    1343: [199, 201, 202],
    1346: [200, 202, 203, 204],
    1347: [197, 204, 205],
    1679: [197],
    1681: [199, 204],
    1693: [202],
    1709: [200, 205, 206],
    1712: [201, 206],
    1744: [202],
    1760: [200, 205, 206],
    1763: [201, 206],
    1827: [202],
    1836: [200, 205, 206],
    1839: [201, 206],
}

RECONSTRUCTIONS = {
    1044: (
        "1. Convert the decimal number 81.5 to its binary form. **(2 marks)** "
        "2. Show that the shift operator \(E\), central difference operator \(\\delta\), "
        "and average operator \(\mu\) satisfy the stated commutativity relations in equally spaced data. **(3 marks)** "
        "3. Use the bisection method to find a root of \(x^3 - x - 9 = 0\) between \(x=2\) and \(x=4\). **(5 marks)** "
        "4. Prove the forward-difference formula stated for polynomial interpolation. **(7 marks)** "
        "5. Use the bisection method to find a root of \(x^3+x^2-1=0\) in the interval \([0,1]\), accurate to \(10^{-4}\). **(8 marks)**"
    ),
    1045: (
        "1. If \(E\), \(\mu\), and \(\\delta\) denote the shift, average, and central difference operators "
        "for data with equal spacing \(h\), prove the stated finite-difference relation involving "
        "\(\\delta E\) and \(\mu\). **(2 marks)** "
        "2. Solve \(x^3=\\sin x\) using the numerical method specified by the question. **(5 marks)** "
        "3. Use linear and quadratic interpolation to determine the stated function value and compare "
        "the results with the given exact value. **(8 marks)**"
    ),
    1079: (
        "1. Define relative error, round-off error, and inherent error as used in numerical computation. **(3 marks)** "
        "2. Estimate the error in evaluating \(f(x,y,z)=x^2+y/z\) for \(x=1.23\), \(y=2.34\), and \(z=3.45\), "
        "assuming each stated value has the uncertainty from the original question. **(5 marks)** "
        "3. Construct the difference table for the supplied data and use it to determine the interpolating polynomial, "
        "then find \(P(4.2)\). **(7 marks)**"
    ),
    1080: (
        "1. State the difference between inherent and induced numerical instability. **(2 marks)** "
        "2. Consider the error sequence \(f(x)=(0,0,0,\\epsilon,0,0)\). Use a difference table to explain "
        "how the error propagates through successive differences. **(5 marks)** "
        "3. Use the Newton backward interpolation formula and the supplied data table to interpolate at \(x=0.25\). "
        "**(5 marks)**"
    ),
    1082: (
        "1. Approximate the value of \(\pi\) using the trapezoidal rule and Simpson's rule with \(n=6\). "
        "**(6 marks)** "
        "2. Obtain the corresponding value of \(\pi\) by direct substitution. **(2 marks)** "
        "3. Using five-digit arithmetic, find the relative error in each approximation in part 1. **(4 marks)** "
        "4. Show that \(f(x)=x^3+x-1\) has a root in \([0,1]\). Apply the Newton-Raphson method starting with "
        "\(x_0=1.0\) and perform four iterations. **(5 marks)** "
        "5. Compute \(\ln 9.2\) from \(\ln 9.0=2.1972\) and \(\ln 9.5=2.2513\) by linear Lagrange interpolation. "
        "**(3 marks)**"
    ),
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    rows = list(
        PrepQuestion.objects.filter(
            Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID)
        )
        .select_related("topic", "paper")
        .distinct()
        .order_by("id")
    )
    unmapped = [q for q in rows if q.topic_id is None]
    print(f"SMA 330: {len(rows)} database rows")
    print(f"unmapped rows before repair: {len(unmapped)}")
    print(f"replacement promotions: {len(PROMOTE_IDS)}")
    print(f"superseded sources to delete: {len(DELETE_SOURCE_IDS)}")
    print(f"foreign/unrelated rows to delete: {len(DELETE_IDS)}")
    print(f"manual reconstructions: {len(RECONSTRUCTIONS)}")

    missing_sources = sorted(qid for qid in DELETE_SOURCE_IDS | DELETE_IDS if not any(q.id == qid for q in rows))
    missing_promotions = sorted(qid for qid in PROMOTE_IDS if not any(q.id == qid for q in rows))
    if missing_sources:
        print(f"missing delete ids: {missing_sources}")
    if missing_promotions:
        print(f"missing promotion ids: {missing_promotions}")

    if not args.apply:
        print("DRY RUN - nothing written. Re-run with --apply.")
        return 0

    BACKUP.write_text(
        json.dumps(
            {
                str(q.id): {
                    "question_latex": q.question_latex,
                    "solution_latex": q.solution_latex,
                    "verification_status": q.verification_status,
                    "topic_id": q.topic_id,
                    "number": q.number,
                    "marks": q.marks,
                    "reconstruction_metadata": q.reconstruction_metadata,
                    "reconstructed_from_id": q.reconstructed_from_id,
                }
                for q in rows
            },
            ensure_ascii=False,
            indent=1,
        ),
        encoding="utf-8",
    )

    for qid, text in RECONSTRUCTIONS.items():
        q = PrepQuestion.objects.filter(pk=qid).first()
        if q is None:
            continue
        q.question_latex = text
        q.verification_status = "auto_validated"
        q.save(update_fields=["question_latex", "verification_status"])

    for qid in PROMOTE_IDS:
        q = PrepQuestion.objects.filter(pk=qid).first()
        if q is None:
            continue
        metadata = dict(q.reconstruction_metadata or {})
        metadata["review_status"] = "promoted_replacement"
        q.verification_status = "reconstructed"
        q.reconstruction_metadata = metadata
        q.save(update_fields=["verification_status", "reconstruction_metadata"])

    deleted_superseded, _ = PrepQuestion.objects.filter(pk__in=DELETE_SOURCE_IDS).delete()
    deleted_foreign, _ = PrepQuestion.objects.filter(pk__in=DELETE_IDS).delete()
    print(f"deleted superseded source rows: {deleted_superseded}")
    print(f"deleted foreign/unrelated rows: {deleted_foreign}")

    for qid, targets in MANUAL_TOPIC_TARGETS.items():
        q = PrepQuestion.objects.filter(pk=qid).first()
        if q is None:
            continue
        q.topic_id = targets[0]
        q.topic_label = ""
        q.save(update_fields=["topic_id", "topic_label"])

    remaining = list(
        PrepQuestion.objects.filter(
            Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID)
        )
        .select_related("topic")
        .distinct()
        .order_by("id")
    )
    plan = []
    unmapped_after = []
    for q in remaining:
        targets = MANUAL_TOPIC_TARGETS.get(q.id, [q.topic_id] if q.topic_id is not None else [])
        targets = sorted(set(targets))
        if not targets:
            unmapped_after.append(q.id)
        plan.append({"id": q.id, "targets": targets})

    PLAN.write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"remaining unmapped rows: {len(unmapped_after)} {unmapped_after}")
    print(f"wrote topic plan: {PLAN} ({len(plan)} rows)")
    print(f"backup: {BACKUP}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
