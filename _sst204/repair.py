"""Repair SST 204 past-paper questions.

Conservative, deterministic repair. It removes extraction debris that carries no
mathematical content, then re-validates with the very function the app uses before
any row is written. Rows that still fail are reported, never guessed at.

Nothing here calls an AI provider.

Usage (from the repository root):
    python _sst204/repair.py --dry-run
    python _sst204/repair.py --apply
    python _sst204/repair.py --apply --phase 1
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from collections import Counter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django

django.setup()

from prep.models import PrepCourse, PrepQuestion
from services.prep_ingestion import (
    _strip_safe_question_extraction_artifacts,
    _topic_match_for_question,
    assessment_question_rendering_issues,
)

COURSE = "SST 204"

# Markers that begin the *next* paper's cover page. A question never resumes after
# one of these, so everything from the earliest match onwards is discarded.
_TRUNCATE_MARKERS = [
    r"\\end\{document\}",
    r"\\textsc\{",
    r"UNIVERSITY\s+EXAMINATIONS?\b",
    r"a\s+higher\s+education\s+institution",
    # Advertising box that the papers print at the foot of a page.
    r"\\fbox\{",
    r"\\begin\{minipage\}",
    # Statistical tables appended after the last question of a paper.
    r"\*\*Table\s+\d",
    r"\\setlength\{",
    r"\\renewcommand\{",
    r"\\begin\{tabular\}",
]
_TRUNCATE_RES = [
    re.compile(marker, re.IGNORECASE | re.MULTILINE) for marker in _TRUNCATE_MARKERS
]

# Inline page furniture that appears *between* sub-questions of the same question.
# These must be deleted in place, never used to truncate: the question continues
# after them on the next page.
_INLINE_FOOTER_RES = [
    re.compile(r"\{?\**\s*INVOLVEMENT\s+IN\s+ANY\s+EXAMINATION\s+IRREGULARITY\s*"
               r"SHALL\s+LEAD\s+TO\s+DISCONTINUATION\s*\**\}?", re.IGNORECASE),
    re.compile(r"\{?\**\s*Page\s+\d+\s+of\s+\d+\s*\**\}?", re.IGNORECASE),
    re.compile(r"\{?\**\s*Scanned\s+with\s+CamScanner\s*\**\}?", re.IGNORECASE),
    re.compile(r"\{?\**\s*VISIT\s+US\s+FOR\s*:[^\n]*", re.IGNORECASE),
]

# Leading extraction debris with no meaning: bold runs left by the extractor and
# stray closing braces carried over from the previous question's display block.
_LEADING_JUNK_RE = re.compile(r"^\s*(?:\*{2,}|[}\s]*\}+|\*\s*)+")

def strip_currency_dollars(text: str) -> str:
    """Remove dollar signs used as currency symbols, never maths delimiters.

    Two provably safe cases only:

    1. A dollar sign followed by whitespace is currency. A maths delimiter is always
       written tight against its expression, so ``$ 2.5`` is never an opening delimiter.
    2. After that pass, if the remaining count is odd the text can never render, so a
       stray dollar immediately followed by a digit must be the currency symbol.
    """
    text = re.sub(r"(?<=[\s(])\$[ \t]+(?=\d)", "", text)
    if text.count("$") % 2:
        text = re.sub(r"(?<=[\s(])\$(?=\d)", "", text)
    return text

_SCAFFOLD_PATTERNS = [
    (r"```(?:latex|tex)\s*\n", "\n"),
    (r"\\documentclass(?:\[[^\]]*\])?\{[^}]*\}", ""),
    (r"\\usepackage(?:\[[^\]]*\])?\{[^}]*\}", ""),
    (r"\\begin\{document\}", ""),
    (r"\\end\{document\}", ""),
    # The equation wrapper around a display block is replaced by a line break so the
    # surrounding words never run together ("given byf(x)").
    (r"\\begin\{equation\*?\}", "\n\n"),
    (r"\\end\{equation\*?\}", "\n\n"),
]


def drop_inline_footers(text: str) -> str:
    """Delete page furniture that sits between sub-questions, keeping the content."""
    for pattern in _INLINE_FOOTER_RES:
        text = pattern.sub("", text)
    return text


def strip_trailing_header(text: str) -> str:
    """Cut everything from the earliest next-paper cover-page marker."""
    starts = [match.start() for match in (_r.search(text) for _r in _TRUNCATE_RES) if match]
    if starts:
        cut = min(starts)
        if cut > 40:
            return text[:cut].rstrip()
    return text


def strip_scaffolding(text: str) -> str:
    for pattern, replacement in _SCAFFOLD_PATTERNS:
        text = re.sub(pattern, replacement, text)
    return text


def repair_cases_rows(text: str) -> str:
    """Restore a row separator inside a cases/array block where extraction lost it.

    Text extraction drops the ``\\\\`` between rows surprisingly often, leaving two
    rows on adjacent lines with no separator. Inside such a block every physical line
    after the first is a new row, so a missing separator is unambiguous.
    """
    def fix(match: re.Match[str]) -> str:
        body = match.group(2)
        lines = body.split("\n")
        rebuilt = []
        for index, line in enumerate(lines):
            stripped = line.rstrip()
            tail = [later for later in lines[index + 1:] if later.strip()]
            is_last = not tail
            needs_separator = (
                bool(stripped)
                and not is_last
                and not stripped.endswith("\\\\")
                and "\\end{" not in stripped
            )
            rebuilt.append(stripped + (" \\\\" if needs_separator else ""))
        return match.group(1) + "\n".join(rebuilt) + match.group(3)

    return re.sub(
        r"(\\begin\{(?:cases|array)\}(?:\{[^}]*\})?\s*)([\s\S]*?)(\s*\\end\{(?:cases|array)\})",
        fix,
        text,
    )


def repair_text(raw: str) -> tuple[str, list[str]]:
    """Apply every safe deterministic repair and return the text plus a change log."""
    changes = []
    text = str(raw or "")

    def apply(new: str, label: str) -> None:
        nonlocal text
        if new != text:
            changes.append(label)
            text = new

    apply(_strip_safe_question_extraction_artifacts(text), "stripped extraction artifacts")
    apply(drop_inline_footers(text), "removed inline page footer")
    apply(strip_trailing_header(text), "cut the next paper's cover page")
    apply(_LEADING_JUNK_RE.sub("", text), "stripped leading debris")
    apply(
        strip_currency_dollars(text),
        "removed currency dollar signs that unbalanced the delimiters",
    )
    apply(strip_scaffolding(text), "removed raw LaTeX document scaffolding")
    apply(repair_cases_rows(text), "restored a missing row separator in a cases block")
    apply(re.sub(r"(?<!\\begin\{)\{\}", "", text), "removed an empty brace group")
    apply(re.sub(r"\n{3,}", "\n\n", text).strip(), "collapsed blank lines")
    return text, changes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write changes (default is a dry run)")
    parser.add_argument("--phase", type=int, choices=(1, 2, 3), help="run only one phase")
    parser.add_argument("--show", type=int, default=0, help="print the first N repaired texts")
    args = parser.parse_args()

    course = PrepCourse.objects.get(code__iexact=COURSE)
    questions = PrepQuestion.objects.filter(paper__course=course).select_related("topic")
    todo = questions.filter(verification_status__in=("flagged", "pending"))
    print(f"{COURSE}: {questions.count()} questions total, {todo.count()} flagged or pending")

    repaired = []
    unfixable = []
    for question in todo.order_by("id").iterator():
        text, changes = repair_text(question.question_latex)
        remaining = assessment_question_rendering_issues(text)
        if text != question.question_latex and not remaining:
            repaired.append((question, text, changes))
        else:
            unfixable.append((question, text, remaining, changes))

    print("\nPHASE 1 - deterministic repair")
    print(f"  repairable to a valid state : {len(repaired)}")
    print(f"  still invalid               : {len(unfixable)}")
    reasons = Counter()
    for _, _, remaining, _ in unfixable:
        for issue in remaining or ["text unchanged and still invalid"]:
            reasons[issue] += 1
    for issue, count in reasons.most_common():
        print(f"    {count:4}  {issue}")

    change_counts = Counter()
    for _, _, changes in repaired:
        for change in changes:
            change_counts[change] += 1
    print("  repairs applied:")
    for change, count in change_counts.most_common():
        print(f"    {count:4}  {change}")

    if args.show:
        for question, text, changes in repaired[: args.show]:
            print("\n" + "=" * 70)
            print(f"ID {question.pk} Q{question.number} :: {changes}")
            print(text[:500])

    unmapped = list(questions.filter(topic__isnull=True))
    mapping = [(q, _topic_match_for_question(course, q.question_latex)) for q in unmapped]
    print("\nPHASE 3 - topic mapping")
    print(f"  unmapped questions: {len(unmapped)}")
    for question, topic in mapping:
        label = topic.title if topic else "UNRESOLVED"
        print(f"    ID {question.pk} Q{question.number} -> {label}")

    if not args.apply:
        print("\nDRY RUN: nothing written. Re-run with --apply to save.")
        return 0

    written = 0
    if args.phase in (None, 1, 2):
        for question, text, changes in repaired:
            metadata = question.reconstruction_metadata if isinstance(
                question.reconstruction_metadata, dict
            ) else {}
            metadata = dict(metadata)
            metadata.setdefault("original_transcription", question.question_latex)
            metadata["review_status"] = "deterministically_repaired"
            metadata["deterministic_repair"] = changes
            question.question_latex = text
            question.reconstruction_metadata = metadata
            question.verification_status = "auto_validated"
            question.verified_by = None
            question.save(
                update_fields=[
                    "question_latex",
                    "reconstruction_metadata",
                    "verification_status",
                    "verified_by",
                ]
            )
            written += 1
    if args.phase in (None, 3):
        for question, topic in mapping:
            if topic and question.topic_id != topic.pk:
                question.topic = topic
                question.topic_label = topic.title
                question.save(update_fields=["topic", "topic_label"])
                written += 1

    print(f"\nWROTE {written} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
