"""SMA 200 (Calculus 2, course 41) past-paper clean-up.

The course's question bank is a mixture of three things:
  * four real examination papers whose questions were OCR-scanned (leading ``**``, exam
    footers, unreadable glyphs) but which already carry clean reconstructions,
  * one scanned textbook dump (Backhouse / Fulks chapters) that is mostly chapter prose,
    formula fragments and merged exercise lists,
  * one row that is only a reading list.

The clean-up keeps every real question, drops what is not a question at all, publishes the
ready reconstructions, and repairs the remaining scan artefacts. Nothing that is already a
question is rewritten.

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

COURSE_ID = 41
TEXTBOOK_PAPER = "sma200-doc-776f3d92"
READING_LIST_PAPER = "sma200-doc-e4204b55"

BOOK_MARKERS = re.compile(
    r"you\s+have\s+learnt|further\s+reading|\bsummary\b|\bchapter\b|\bexercise\s*\d|"
    r"\bsolution\b|\bexample\s*\d|backhouse|wiley|heinemann|longman|"
    r"pure\s+mathematics|advanced\s+calculus|additional\s+pure|"
    r"integration\s+of\s+functions\s+containing\s+first\s+degree|"
    r"the\s+following\s+are\s+the\s+formulae|"
    r"find\s+the\s+integrals\s+of\s+the\s+following",
    re.I,
)
ASK = re.compile(
    r"\b(find|evaluate|calculate|determine|show\s+that|prove|obtain|compute|estimate|"
    r"interpret|verify|sketch|plot|test|state|if)\b",
    re.I,
)
MERGED_LIST = re.compile(r"(?:\b\d{1,2}\.\s[^\n]{0,40}){3,}")
QUESTION_START = re.compile(
    r"^(if|find|evaluate|calculate|determine|show|prove|obtain|compute|estimate|interpret|"
    r"verify|sketch|plot|test|state|use|the\s+equation|a\s+car|a\s+particle|a\s+curve|"
    r"pure\s+mathematics)\b",
    re.I,
)
FORMULA_FRAGMENT = re.compile(r"=\s*\+\s*c\b|=\s*\+|\bdx\s*∫|e\.g\.\s*∫|n\s*≠|\\?int\s*\\?limits")

# Exam-paper furniture that follows the last real sub-question.
FOOTER = re.compile(
    r"(?:\*{0,3}\s*(?:involvement\s+in|any\s+form\s+of)\s*(?:any\s+)?examination\s+irregularity"
    r"|\*{0,3}\s*anastasia\s+nduta|\*{0,3}\s*nduta\s+na\s+spas|\*{0,3}\s*female\s+delegate"
    r"|\*{0,3}\s*for\s+female\s+delegate|\*{0,3}\s*nduta\s+for\s+female"
    r"|\*{0,3}\s*sma\s*20\d\s*:?\s*calculus"
    r"|\*{0,3}\s*date\s*:|\*{0,3}\s*time\s*:|\*{0,3}\s*instructions\s*:"
    r"|\*{0,3}\s*page\s+\d+\s+of\s+\d+)",
    re.I,
)


def strip_leading_noise(text: str) -> str:
    s = text.lstrip()
    s = re.sub(r"^[\s*]*\*{2,}\s*", "", s)
    s = re.sub(r"^[\s*]+", "", s)
    s = re.sub(r"^\.\s*[-–]?\s*\[\s*(?:compulsory|optional)\s*[-–]?\s*\]\s*", "", s, flags=re.I)
    s = re.sub(r"^[-–]\s*\[\s*(?:compulsory|optional)\s*[-–]?\s*\]\s*", "", s, flags=re.I)
    return s.strip()


def strip_furniture(text: str) -> str:
    s = re.sub(r"\\end\s*\{\s*do\s*\\?\s*ment\s*\}", " ", text, flags=re.I)
    s = re.sub(r"\\end\s*\{\s*document\s*\}", " ", s, flags=re.I)
    match = FOOTER.search(s)
    if match:
        s = s[: match.start()]
    s = re.sub(r"(?i)page\s+\d+\s+of\s+\d+", " ", s)
    return s.strip()


def close_environments(text: str) -> str:
    opened = re.findall(r"\\begin\s*\{([a-zA-Z*]+)\}", text)
    closed = re.findall(r"\\end\s*\{([a-zA-Z*]+)\}", text)
    missing = list(opened)
    for name in closed:
        if name in missing:
            missing.remove(name)
    out = text
    for name in reversed(missing):
        out = out.rstrip() + f" \\end{{{name}}}"
    return out


def repair(text: str) -> str:
    s = " ".join(strip_furniture(strip_leading_noise(text)).split())
    s = re.sub(r"\s+([,.;:])", r"\1", s)
    return close_environments(s)


def is_not_a_question(text: str) -> bool:
    t = " ".join((text or "").split())
    if BOOK_MARKERS.search(t) or FORMULA_FRAGMENT.search(t) or MERGED_LIST.search(t):
        return True
    if not QUESTION_START.search(t):
        return True
    if len(t) < 40:
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
        if q.paper_id == READING_LIST_PAPER:
            deletes.append((q, "reading list only"))
            continue
        if q.reconstructed_from_id:
            if q.verification_status == "pending" and not assessment_question_rendering_issues(text):
                publishes.append((q, "ready reconstruction"))
            else:
                keeps.append(q)
            continue
        if q.id in reconstructions:
            deletes.append((q, f"superseded by clean reconstruction q{reconstructions[q.id].id}"))
            continue
        if q.paper_id == TEXTBOOK_PAPER:
            if is_not_a_question(text):
                deletes.append((q, "textbook prose / formula fragment / merged exercise list"))
            else:
                keeps.append(q)
            continue
        if assessment_question_rendering_issues(text):
            fixed = repair(text)
            if fixed != text and not assessment_question_rendering_issues(fixed):
                repairs.append((q, fixed))
            else:
                deletes.append((q, "unreadable scan, no clean reconstruction"))
            continue
        # Cosmetic scan artefacts that the rendering gate tolerates but learners would see.
        if text.lstrip().startswith("*") or FOOTER.search(text) or "\\end{document}" in text:
            fixed = repair(text)
            if fixed != text:
                repairs.append((q, fixed))
                continue
        keeps.append(q)

    print(f"rows={len(rows)}")
    print(f"delete={len(deletes)} repair={len(repairs)} publish={len(publishes)} keep={len(keeps)}")
    print("deletions by reason:", dict(Counter(reason for _q, reason in deletes)))
    print("\n-- deletions outside the textbook paper --")
    for q, reason in deletes:
        if q.paper_id != TEXTBOOK_PAPER:
            print(f"  q{q.id} [{q.verification_status}] {reason}: {' '.join((q.question_latex or '').split())[:100]}")
    print("\n-- repairs --")
    for q, fixed in repairs:
        print(f"  q{q.id}: {' '.join((q.question_latex or '').split())[:90]}")
        print(f"     -> {fixed[:150]}")
    print("\n-- publishes --")
    for q, _reason in publishes:
        print(f"  q{q.id} ref={q.reconstructed_from_id} sol={len((q.solution_latex or '').strip())}: {' '.join((q.question_latex or '').split())[:100]}")
    print("\n-- kept from the textbook paper --")
    for q in keeps:
        if q.paper_id == TEXTBOOK_PAPER:
            print(f"  q{q.id} [{q.verification_status[:6]}] :: {' '.join((q.question_latex or '').split())[:120]}")

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
