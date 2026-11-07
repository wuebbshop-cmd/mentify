"""SMA 230 (Vector Analysis, course 43) past-paper clean-up.

Dry run by default; pass --apply to write.
"""
from __future__ import annotations

import io
import json
import os
import re
import sys
from collections import Counter
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
from services.prep_ingestion import assessment_question_rendering_issues  # noqa: E402

COURSE_ID = 43
REFERENCE_PAPER = "sma230-doc-9bc3e153"

FOOTER = re.compile(
    r"(?:\*{0,3}\s*(?:involvement\s+in|examination\s+irregularity|mnu[a-z]*\s+2024/2025)"
    r"|[\*\s]*(?:date|time|instructions)\s*:"
    r"|[\*\s]*page\s+\d+\s+of\s+\d+"
    r"|\\end\s*\{\s*document\s*\})",
    re.I,
)

def strip_furniture(text: str) -> str:
    s = re.sub(r"^[\s*]+", "", text or "")
    s = re.sub(r"\*\*\*\*", "", s)
    s = re.sub(r"\bReferences?\b.*$", "", s, flags=re.I)
    match = FOOTER.search(s)
    if match:
        s = s[: match.start()]
    s = re.sub(r"\\end\s*\{\s*document\s*\}", "", s, flags=re.I)
    s = re.sub(r"oindent\s+oindent\s*", "", s, flags=re.I)
    s = re.sub(r"\*{2,}", "", s)
    return " ".join(s.split()).strip()


def repair_vector_text(text: str) -> str:
    s = strip_furniture(text)
    s = s.replace("\\propto", "\\alpha")
    s = s.replace("12 \\cos 2ti", "12 \\cos 2t\\,\\mathbf{i}")
    s = s.replace("- 8 \\sin tj", "- 8 \\sin t\\,\\mathbf{j}")
    s = s.replace("+ 16tk", "+ 16t\\,\\mathbf{k}")
    s = s.replace("2ti", "2t\\mathbf{i}")
    s = s.replace("3sin", "3\\sin")
    s = s.replace("12 \\cos 2t i", "12 \\cos 2t\\,\\mathbf{i}")
    s = s.replace("8 \\sin t j", "8 \\sin t\\,\\mathbf{j}")
    s = s.replace("16t k", "16t\\,\\mathbf{k}")
    s = s.replace("12 \\cos 2ti", "12 \\cos 2t\\,\\mathbf{i}")
    s = s.replace("8 \\sin tj", "8 \\sin t\\,\\mathbf{j}")
    s = s.replace("16tk", "16t\\,\\mathbf{k}")
    s = s.replace("4xi - 2y^2j + z^2k", "4x\\mathbf{i} - 2y^2\\mathbf{j} + z^2\\mathbf{k}")
    s = s.replace("4xi", "4x\\mathbf{i}")
    s = s.replace("2y^2j", "2y^2\\mathbf{j}")
    s = s.replace("z^2k", "z^2\\mathbf{k}")
    s = s.replace("14yzj", "14yz\\mathbf{j}")
    s = s.replace("20xz^2k", "20xz^2\\mathbf{k}")
    s = s.replace("6yi", "6y\\mathbf{i}")
    s = s.replace("3x^2", "3x^2")
    s = s.replace("3i - j", "3\\mathbf{i} - \\mathbf{j}")
    s = s.replace("j + 2k", "\\mathbf{j} + 2\\mathbf{k}")
    s = s.replace("i + 5j + 4k", "\\mathbf{i} + 5\\mathbf{j} + 4\\mathbf{k}")
    s = s.replace("A = i + j", "A = \\mathbf{i} + \\mathbf{j}")
    s = s.replace("B = 2i - 3j + k", "B = 2\\mathbf{i} - 3\\mathbf{j} + \\mathbf{k}")
    s = s.replace("C = 4j - 3k", "C = 4\\mathbf{j} - 3\\mathbf{k}")
    s = s.replace("A = 3i - j", "A = 3\\mathbf{i} - \\mathbf{j}")
    s = s.replace("t^2i", "t^2\\mathbf{i}")
    s = s.replace("tj", "t\\mathbf{j}")
    s = s.replace("tk", "t\\mathbf{k}")
    s = s.replace("(2t + 1)k", "(2t + 1)\\mathbf{k}")
    s = s.replace("(2t - 3)i", "(2t - 3)\\mathbf{i}")
    s = s.replace("- tk", "- t\\mathbf{k}")
    s = s.replace("(x^2 - y^2)i", "(x^2 - y^2)\\mathbf{i}")
    s = s.replace("2xyj", "2xy\\mathbf{j}")
    s = s.replace("(y^2 - xy)k", "(y^2 - xy)\\mathbf{k}")
    s = s.replace("(3x^2 + 6y)i", "(3x^2 + 6y)\\mathbf{i}")
    s = s.replace("4xi - 2y^2j + z^2k", "4x\\mathbf{i} - 2y^2\\mathbf{j} + z^2\\mathbf{k}")
    return s


def is_reference_or_fragment(q: PrepQuestion) -> bool:
    text = " ".join((q.question_latex or "").split())
    if q.paper_id == REFERENCE_PAPER:
        return True
    if text.startswith(("http://", "https://")):
        return True
    if re.search(r"\breferences?\b", text, re.I):
        return True
    if text.casefold().startswith(("the projection of", "\\(\\vec{a} \\cdot \\vec{b}\\)", "(a \u00b7 b)")) and len(text) < 70:
        return True
    return False


def has_unreadable_source(text: str) -> bool:
    t = text or ""
    if any(ord(c) in range(0xE000, 0xF900) for c in t):
        return True
    if any(c in t for c in ("\uf0b7", "\uf06f", "\uf03d", "\uf03c", "\uf04d", "\uf044")):
        return True
    if re.search(r"[]", t):
        return True
    return False


def main() -> None:
    apply = "--apply" in sys.argv
    rows = list(
        PrepQuestion.objects.filter(Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID))
        .select_related("paper")
        .order_by("id")
    )
    reconstructions = {q.reconstructed_from_id: q for q in rows if q.reconstructed_from_id}

    deletes, repairs, publishes, keeps = [], [], [], []
    for q in rows:
        text = q.question_latex or ""
        if q.reconstructed_from_id:
            if assessment_question_rendering_issues(text):
                deletes.append((q, "unusable reconstruction with rendering defects"))
            elif q.verification_status == "pending":
                publishes.append((q, "ready reconstruction"))
            else:
                keeps.append(q)
            continue
        if q.id in reconstructions:
            deletes.append((q, f"superseded by clean reconstruction q{reconstructions[q.id].id}"))
            continue
        if is_reference_or_fragment(q):
            deletes.append((q, "reference, URL, or incomplete extraction fragment"))
            continue
        if has_unreadable_source(text):
            deletes.append((q, "unreadable scan/private-use OCR"))
            continue
        if assessment_question_rendering_issues(text):
            fixed = repair_vector_text(text)
            if fixed != text and not assessment_question_rendering_issues(fixed):
                repairs.append((q, fixed))
            else:
                keeps.append(q)
            continue
        fixed = repair_vector_text(text) if FOOTER.search(text) else text
        if fixed != text and not assessment_question_rendering_issues(fixed):
            repairs.append((q, fixed))
            continue
        keeps.append(q)

    print(f"rows={len(rows)}")
    print(f"delete={len(deletes)} repair={len(repairs)} publish={len(publishes)} keep={len(keeps)}")
    print("deletions by reason:", dict(Counter(reason for _q, reason in deletes)))
    print("\n-- deletions outside superseded reconstructions --")
    for q, reason in deletes:
        if not reason.startswith("superseded by"):
            print(f"  q{q.id} [{q.verification_status}] {reason}: {' '.join((q.question_latex or '').split())[:120]}")
    print("\n-- repairs --")
    for q, fixed in repairs:
        print(f"  q{q.id}: {' '.join((q.question_latex or '').split())[:100]}")
        print(f"     -> {fixed[:160]}")
    print("\n-- publishes --")
    for q, _reason in publishes:
        print(f"  q{q.id} ref={q.reconstructed_from_id} sol={len((q.solution_latex or '').strip())}: {' '.join((q.question_latex or '').split())[:100]}")

    if not apply:
        print("\nDRY RUN - nothing written.")
        return

    backup = Path(__file__).resolve().parent / "repair_backup.json"
    backup.write_text(
        json.dumps(
            {
                "deleted": [
                    {"id": q.id, "paper": q.paper_id, "reason": reason, "text": q.question_latex, "status": q.verification_status}
                    for q, reason in deletes
                ],
                "repaired": [{"id": q.id, "before": q.question_latex, "after": fixed} for q, fixed in repairs],
                "published": [{"id": q.id, "before": q.verification_status} for q, _r in publishes],
            },
            indent=1,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print("\nbackup:", backup)

    for q, _reason in deletes:
        PrepQuestion.objects.filter(pk=q.id).delete()
    print(f"deleted {len(deletes)} rows")
    for q, fixed in repairs:
        PrepQuestion.objects.filter(pk=q.id).update(question_latex=fixed, verification_status="auto_validated")
    print(f"repaired {len(repairs)} rows")
    for q, _reason in publishes:
        PrepQuestion.objects.filter(pk=q.id).update(verification_status="reconstructed")
    print(f"published {len(publishes)} reconstructions")


if __name__ == "__main__":
    main()
