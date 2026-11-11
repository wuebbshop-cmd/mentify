"""Surgical repair of SST 304 past-paper rows."""

from __future__ import annotations

import argparse
import io
import json
import os
import re
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

COURSE_ID = 3635
HERE = Path(__file__).resolve().parent
BACKUP = HERE / "sst304_repair_backup.json"
PLAN = HERE / "topic_plan_3635.json"

PROMOTE_IDS = {
    1389, 1391, 1393, 1405, 1383, 1395, 1420, 1422,
    1385, 1387, 1397, 1409, 1424, 1399, 1412, 1401,
    1403, 1427, 1429, 983, 985, 971, 973, 978, 1334,
    1331, 1332, 1333,
}

DELETE_SOURCE_IDS = {
    1388, 1390, 1392, 1404, 1382, 1394, 1419, 1421,
    1384, 1386, 1396, 1408, 1423, 1398, 1411, 1400,
    1402, 1426, 1428, 982, 984, 970, 972, 977, 979,
    965, 967, 968,
}

MANUAL_TOPIC_TARGETS = {
    966: [168],
    969: [170],
    975: [169],
    980: [170],
    981: [170],
    986: [168],
    1383: [167, 168],
    1385: [169],
    1387: [169],
    1391: [168],
    1393: [169],
    1395: [168],
    1397: [169],
    1399: [167, 168],
    1401: [170],
    1403: [170],
    1409: [168],
    1412: [169],
    1420: [169],
    1422: [167],
    1424: [168],
    1427: [169],
    1429: [170],
    983: [169],
    985: [167, 168],
    971: [167],
    973: [168],
    978: [168],
    1334: [167],
    1331: [167],
    1332: [169],
    1333: [167, 168],
    1389: [167],
    1405: [167],
}

RECONSTRUCTIONS = {
    966: (
        "Let \(\mathbf{X}=(X_1,X_2,X_3)'\) have a trivariate normal distribution with "
        r"dispersion matrix \(\Sigma\) and quadratic form "
        r"\(Q=(\mathbf{X}-\boldsymbol{\mu})'\Sigma^{-1}(\mathbf{X}-\boldsymbol{\mu})\). "
        "1. Identify \(\Sigma^{-1}\) from the coefficients of \(Q\), and hence determine \(\Sigma\) "
        "and the normalizing constant \(c\). "
        "2. Obtain the marginal density of a stated subset of the random vector. "
        "3. Obtain the conditional density of one component given the remaining components."
    ),
    969: (
        "Define convergence in distribution, convergence in probability, convergence in mean square, "
        "and almost-sure convergence for a sequence of random variables. "
        "State the main relationships among these modes of convergence and give one brief application "
        "of the Weak Law of Large Numbers."
    ),
}


def clean_exam_header(text: str) -> str:
    text = text.strip()
    while text.startswith("[Max: ]**"):
        text = text[len("[Max: ]**"):].lstrip()
    return text


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
    print(f"SST 304: {len(rows)} database rows")
    print(f"unmapped before repair: {len(unmapped)}")
    print(f"replacement promotions: {len(PROMOTE_IDS)}")
    print(f"superseded sources to delete: {len(DELETE_SOURCE_IDS)}")

    missing_delete = sorted(qid for qid in DELETE_SOURCE_IDS if not any(q.id == qid for q in rows))
    missing_promote = sorted(qid for qid in PROMOTE_IDS if not any(q.id == qid for q in rows))
    if missing_delete:
        print(f"missing delete ids: {missing_delete}")
    if missing_promote:
        print(f"missing promotion ids: {missing_promote}")

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
                    "topic_label": q.topic_label,
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

    for q in PrepQuestion.objects.filter(
        Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID),
        question_latex__startswith="[Max: ]**",
    ).distinct():
        q.question_latex = clean_exam_header(q.question_latex)
        q.save(update_fields=["question_latex"])

    for qid in (1410, 1425):
        q = PrepQuestion.objects.filter(pk=qid).first()
        if q is None:
            continue
        text = (q.question_latex or "").strip()
        text = text.removeprefix("**").strip()
        text = re.sub(r"\s+\*\*\[([^\]]+)\]\*\*", r" [\1]", text)
        q.question_latex = text
        q.verification_status = "auto_validated"
        q.save(update_fields=["question_latex", "verification_status"])

    q1116 = PrepQuestion.objects.filter(pk=1116).first()
    if q1116 is not None:
        text = q1116.question_latex or ""
        new = (
            r"Let \(A=\begin{pmatrix}2 & 1 \\ 1 & 3\end{pmatrix}\) and"
        )
        updated, count = re.subn(
            r"Let \$A=\n\n\$\$.*?\$\$\n\n\$ and",
            new,
            text,
            flags=re.DOTALL,
        )
        if count:
            text = updated
            q1116.question_latex = text
            q1116.save(update_fields=["question_latex"])

    for qid in PROMOTE_IDS:
        q = PrepQuestion.objects.filter(pk=qid).first()
        if q is None:
            continue
        metadata = dict(q.reconstruction_metadata or {})
        metadata["review_status"] = "promoted_replacement"
        q.verification_status = "reconstructed"
        q.reconstruction_metadata = metadata
        q.save(update_fields=["verification_status", "reconstruction_metadata"])

    deleted, _ = PrepQuestion.objects.filter(pk__in=DELETE_SOURCE_IDS).delete()
    print(f"deleted superseded source rows: {deleted}")

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
