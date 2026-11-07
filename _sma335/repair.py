"""Deterministic repair of SMA 335 past-paper questions.

Each rule targets a defect that the application's own validator
(``services.prep_ingestion.assessment_question_rendering_issues``) rejects, so a
question is only un-flagged when the validator itself confirms it is clean.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django  # noqa: E402

django.setup()

from prep.models import PrepQuestion  # noqa: E402
from services.prep_ingestion import (  # noqa: E402
    _strip_safe_question_extraction_artifacts,
    assessment_question_rendering_issues,
)

COURSE_ID = 57

# Page furniture and next-paper cover pages. A question never resumes after a
# cover-page marker, so everything from the earliest match is discarded.
_TRUNCATE_MARKERS = [
    r"\\end\{document\}",
    r"\\textsc\{",
    r"UNIVERSITY\s+EXAMINATIONS?\b",
    r"a\s+higher\s+education\s+institution",
    # The university's name and crest, which head the next paper's cover page.
    r"\[\s*University\s+Logo\s*\]",
    r"\bK[EE]?RYATTA\b",
    r"(?m)^\s*[A-Z][A-Z'\s]{2,}\s+UNIVERSITY\s*$",
    r"\\fbox\{",
    r"\\begin\{minipage\}",
    r"\*\*Table\s+\d",
    r"\\setlength\{",
    r"\\renewcommand\{",
    r"\\begin\{tabular\}",
    # A bare course-code line left over from the next paper's masthead.
    r"(?m)^\s*\**\s*SMA\s*\d{3}(?:\s*/\s*\d{3})?\s*\**\s*$",
]
_TRUNCATE_RES = [
    re.compile(marker, re.IGNORECASE | re.MULTILINE) for marker in _TRUNCATE_MARKERS
]

# Page furniture that sits *between* sub-questions and must be deleted in place.
_INLINE_FOOTER_RES = [
    re.compile(
        r"\{?\**\s*(?:INVOLVEMENT\s+IN\s+)?(?:ANY\s+(?:FORM\s+OF\s+)?)?EXAMINATION\s+"
        r"(?:IRREGULARITY|MALPRACTICE|MAL\s*PRACTICE)\s*"
        r"(?:SHALL|WILL)\s+LEAD\s+TO\s+D\s*ISCONTINUATION\s*\**\}?",
        re.IGNORECASE,
    ),
    re.compile(
        r"\{?\**\s*(?:EXAMINATION\s+IRREGULARITY\s+IS\s+PUNISHABLE\s+BY\s+EXPULSION"
        r"|EXAMINATION\s+MALPRACTICE\s+(?:IS|WILL\s+BE)\s+[A-Z ]+)\s*\**\}?",
        re.IGNORECASE,
    ),
    re.compile(r"\{?\**\s*Page\s+\d+\s*of\s*\d+\s*\**\}?", re.IGNORECASE),
    re.compile(r"\{?\**\s*Scanned\s+(?:with|by)\s+CamScanner\s*\**\}?", re.IGNORECASE),
    re.compile(r"\{?\**\s*CamScanner\s*\**\}?", re.IGNORECASE),
    re.compile(r"\{?\**\s*VISIT\s+US\s+FOR\s*:[^\n]*", re.IGNORECASE),
    # A half-captured footer, e.g. "ANY MOVEMENT IN" with the rest on the next page.
    re.compile(r"\{?\**\s*ANY\s+MOVEMENT\b[^\n]*", re.IGNORECASE),
    re.compile(r"\{?\**\s*ANY\s+FORM\s+OF\b[^\n]*", re.IGNORECASE),
]

# Independent safety net: whatever the validator says, these must never reach a
# learner, so a repair that leaves one behind is rejected and reviewed by hand.
_RESIDUAL_FURNITURE_RE = re.compile(
    r"INVOLVEMENT|IRREGULARITY|MALPRACTICE|CamScanner|University\s+Logo|"
    r"^\s*Page\s+\d+\s+of\s+\d+|a\s+higher\s+education\s+institution|"
    r"K[EE]?RYATTA|UNIVERSITY\s+EXAMINATIONS",
    re.IGNORECASE | re.MULTILINE,
)

# Inspirational quotations that the papers print inside an advertising box.
_ADVERT_RES = [
    re.compile(r"^\s*\"[^\"\n]{10,120}\"\s*$", re.MULTILINE),
    re.compile(r"^\s*~+\s*[A-Z][A-Za-z. ]{2,40}\s*~+\s*$", re.MULTILINE),
    # The attribution line of the quotation box, sometimes left with maths delimiters.
    re.compile(r"^\s*\$?\\?sim\$?\s*[A-Z][A-Za-z. ]{2,40}\s*\$?\\?sim\$?\s*$", re.MULTILINE),
]

# Lines left behind after the furniture around them has been stripped: a bare
# "with" from "with CamScanner", a crest placeholder, a rule, or loose bold marks.
# Deliberately narrow so that a `$$` fence or a LaTeX line is never removed.
_JUNK_LINE_RE = re.compile(
    r"^\s*(?:[-–—_*.\s]+|with(?:\s+CamScanner)?|\[\s*University\s+Logo\s*\]|\[\s*Logo\s*\]"
    r"|~+\s*[A-Z][A-Za-z. ]*)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
_TRAILING_MARKS_RE = re.compile(r"(?:\s*\*{4,})+\s*$")

# A question that ends on one of these words has lost the rest of its sentence.
_DANGLING_END_RE = re.compile(
    r"(?i)\b(?:equation|equations|de|the|of|given|consider|that|solve|find|and|or|with|where|hence|to|by)\s*[:;,\-–—]?\s*$"
)

# The validator only rejects a bold marker that stands alone on the first line.
_LEADING_BOLD_RE = re.compile(r"^\s*\*\*\s*(?:\n+|$)")

# "(4 mks)" is ordinary shorthand, but the validator treats the abbreviation as
# OCR damage, so it is expanded to the word the mark scheme actually means.
_MARKS_DAMAGE_SUBS = [
    (re.compile(r"(?i)\bsmarlcs\b"), "5 marks"),
    (re.compile(r"(?i)\bmarlcs\b"), "marks"),
    (re.compile(r"(?i)\bmarkss\b"), "marks"),
    (re.compile(r"(?i)\bmks\b"), "marks"),
    (re.compile(r"(?i)\[\s*s\s*marks\s*\]"), "[5 marks]"),
]

_INLINE_MATH_RE = re.compile(r"\$([^$\n]+)\$|\\\((.+?)\\\)")


def strip_currency_dollars(text: str) -> str:
    """Remove dollar signs used as currency, never maths delimiters."""
    text = re.sub(r"(?<=[\s(])\$[ \t]+(?=\d)", "", text)
    if text.count("$") % 2:
        text = re.sub(r"(?<=[\s(])\$[=\d]", "", text)
    return text


def drop_inline_footers(text: str) -> str:
    for pattern in _INLINE_FOOTER_RES:
        text = pattern.sub("", text)
    return text


def drop_adverts(text: str) -> str:
    for pattern in _ADVERT_RES:
        text = pattern.sub("", text)
    return text


def strip_trailing_header(text: str) -> str:
    starts = [m.start() for m in (_r.search(text) for _r in _TRUNCATE_RES) if m]
    if starts:
        cut = min(starts)
        if cut > 40:
            return text[:cut].rstrip()
    return text


def insert_math_boundary_spaces(text: str) -> str:
    """Space out inline maths that extraction glued to the surrounding words.

    Only a compound expression (something other than a bare symbol) triggers the
    validator, and only an alphanumeric neighbour needs the space.
    """
    out = []
    last = 0
    for match in _INLINE_MATH_RE.finditer(text):
        body = (match.group(1) if match.group(1) is not None else match.group(2)).strip()
        out.append(text[last:match.start()])
        chunk = match.group(0)
        if re.fullmatch(r"[A-Za-z0-9_]+", body):
            out.append(chunk)
        else:
            before = text[match.start() - 1] if match.start() else ""
            after = text[match.end()] if match.end() < len(text) else ""
            if before and (before.isalnum() or before == "_"):
                out.append(" ")
            out.append(chunk)
            if after and (after.isalnum() or after == "_"):
                out.append(" ")
        last = match.end()
    out.append(text[last:])
    return "".join(out)


def close_dangling_bold(text: str) -> str:
    """Close a bold run left open by extraction, e.g. a bare ``**(5 marks)``.

    Only the last, short, single-line run is closed, so a ````**...**`` pair that
    legitimately spans several lines is never rewritten.
    """
    if text.count("**") % 2 == 0:
        return text
    last = text.rfind("**")
    tail = text[last + 2:]
    if "\n" not in tail and len(tail) <= 40:
        return text + "**"
    return text


def repair_text(raw: str) -> tuple[str, list[str]]:
    text = str(raw or "")
    changes: list[str] = []

    def apply(new: str, label: str) -> None:
        nonlocal text
        if new != text:
            changes.append(label)
            text = new

    apply(_strip_safe_question_extraction_artifacts(text), "stripped extraction artifacts")
    apply(_LEADING_BOLD_RE.sub("", text), "removed a stray leading bold marker")
    apply(drop_inline_footers(text), "removed inline page footer")
    apply(strip_trailing_header(text), "cut the next paper's cover page")
    apply(drop_adverts(text), "removed an advertising quotation")
    for pattern, replacement in _MARKS_DAMAGE_SUBS:
        apply(pattern.sub(replacement, text), "repaired an OCR-damaged marks annotation")
    apply(strip_currency_dollars(text), "removed currency dollar signs")
    apply(insert_math_boundary_spaces(text), "spaced inline maths away from the prose")
    apply(_JUNK_LINE_RE.sub("", text), "removed leftover page furniture")
    apply(_TRAILING_MARKS_RE.sub("", text), "removed trailing bold marks")
    apply(close_dangling_bold(text), "closed an unclosed bold run")
    apply(re.sub(r"\n{3,}", "\n\n", text).strip(), "collapsed blank lines")
    return text, changes


def is_acceptable(before: str, after: str) -> tuple[bool, str]:
    """Decide whether a deterministic repair is safe to publish.

    The validator alone is not enough: it does not recognise every footer wording,
    and it passes text that has been truncated down to a dangling fragment. So a
    repair must also keep most of the original content and leave no page furniture.
    """
    remaining = assessment_question_rendering_issues(after)
    if remaining:
        return False, "; ".join(remaining)
    if _RESIDUAL_FURNITURE_RE.search(after):
        return False, "page furniture survived the repair"
    kept = len("".join(after.split()))
    original = len("".join(before.split()))
    if original and kept < 0.15 * original:
        return False, f"repair would discard {100 * (1 - kept / original):.0f}% of the text"
    if _DANGLING_END_RE.search(after):
        return False, "repair would leave only a dangling fragment"
    return True, ""


def main() -> None:
    apply_write = "--apply" in sys.argv

    rows = list(PrepQuestion.objects.filter(topic__course_id=COURSE_ID).order_by("id"))
    flagged = [q for q in rows if q.verification_status == "flagged"]

    clean_now = []
    still_bad = []
    for q in flagged:
        before = q.question_latex or ""
        after, changes = repair_text(before)
        ok, why = is_acceptable(before, after) if after != before else (False, "no change")
        if ok:
            clean_now.append((q, after, changes))
        else:
            still_bad.append((q.id, why))

    print(f"flagged: {len(flagged)}")
    print(f"fixable deterministically: {len(clean_now)}")
    print(f"needs reconstruction: {len(still_bad)}")
    from collections import Counter

    c = Counter()
    for _id, why in still_bad:
        for part in why.split("; "):
            c[part] += 1
    for k, v in c.most_common():
        print(f"   {v:3d}  {k}")
    print("ids needing reconstruction:", sorted(i for i, _ in still_bad))

    if apply_write:
        for q, after, _changes in clean_now:
            q.question_latex = after
            q.verification_status = "auto_validated"
            q.save(update_fields=["question_latex", "verification_status"])
        print(f"wrote {len(clean_now)} rows")
    else:
        print("DRY RUN - nothing written.")


if __name__ == "__main__":
    main()
