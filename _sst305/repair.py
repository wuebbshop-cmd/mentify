"""Deterministic repair of SST 305 past-paper questions.

SST 305's damage is mostly *structural*: text extraction closed a display-math
block too early, so a ``\\begin{cases}`` ends up outside the maths and renders as
raw LaTeX, and fences get left stranded. Regular expressions cannot tell an
opening ``$$`` from a closing one, so the display maths is rebuilt by splitting the
text on the fences (which alternates prose, block, prose, block ...) and re-emitting
it. That is parity-safe: an unterminated trailing block is folded back into the
prose instead of inventing a boundary.

A question is only un-flagged once the application's own validator *and* a stricter
check of my own both pass.
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

COURSE_ID = 27

_TRUNCATE_MARKERS = [
    # NOTE: \\end{document} is deliberately absent - the extractor emits it in the
    # middle of a question (part (e) follows it), so truncating there deletes content.
    r"\\textsc\{",
    r"UNIVERSITY\s+EXAMINATIONS?\b",
    r"a\s+higher\s+education\s+institution",
    r"\[\s*University\s+Logo\s*\]",
    r"\\fbox\{",
    r"\\begin\{minipage\}",
    r"\*\*Table\s+\d",
    r"(?m)^\s*#{1,4}\s*(?:Appendix|TABLE)\b",
    r"(?m)^\s*#{1,4}\s*SST\s*\d{3}\b",
    r"(?i)\bAppendix\s+[A-Z]\b",
    r"(?i)\bTABLE\s+[A-Z]\s*\.?\s*\d",
    r"\\setlength\{",
    r"\\renewcommand\{",
    r"\\begin\{tabular\}",
]
_TRUNCATE_RES = [re.compile(m, re.IGNORECASE | re.MULTILINE) for m in _TRUNCATE_MARKERS]

_INLINE_FOOTER_RES = [
    re.compile(r"\{?\**\s*INVOLVEMENT\b[^\n]*", re.IGNORECASE),
    re.compile(r"\{?\**\s*ANY\s+(?:FORM\s+OF\s+)?EXAMINATION\b[^\n]*", re.IGNORECASE),
    re.compile(r"\{?\**\s*EXAMINATION\s+(?:IRREGULARITY|MALPRACTICE)\b[^\n]*", re.IGNORECASE),
    re.compile(r"\{?\**\s*Page\s+\d+\s*of\s*\d+\s*\**\}?", re.IGNORECASE),
    re.compile(r"\{?\**\s*Scanned\s+(?:with|by)\s+CamScanner\s*\**\}?", re.IGNORECASE),
    re.compile(r"\{?\**\s*CamScanner\s*\**\}?", re.IGNORECASE),
    re.compile(r"\{?\**\s*VISIT\s+US\s+FOR\s*:[^\n]*", re.IGNORECASE),
    re.compile(r"(?i)^\s*The\s+image\s+has\s+been\s+rotated[^\n]*$", re.MULTILINE),
    re.compile(r"(?i)^\s*OCR\s+result\s*:?\s*$", re.MULTILINE),
]
_JUNK_LINE_RE = re.compile(r"^\s*(?:[-–—_*.\s]+|with(?:\s+CamScanner)?|\*{2,})\s*$", re.MULTILINE)
_ADVERT_RES = [
    re.compile(r"^\s*\"[^\"\n]{10,120}\"\s*$", re.MULTILINE),
    re.compile(r"^\s*~+\s*[A-Z][A-Za-z. ]{2,40}\s*~*\s*$", re.MULTILINE),
]

_RESIDUAL_FURNITURE_RE = re.compile(
    r"INVOLVEMENT|IRREGULARITY|MALPRACTICE|CamScanner|University\s+Logo|"
    r"^\s*Page\s+\d+\s*of\s*\d+|a\s+higher\s+education\s+institution",
    re.IGNORECASE | re.MULTILINE,
)

_MATH_ENV_NAMES = (
    r"cases|array|align\*?|aligned|matrix|pmatrix|bmatrix|vmatrix|Vmatrix|"
    r"eqnarray\*?|gathered|split|alignat\*?"
)
_MATH_ENV_RE = re.compile(rf"\\begin\{{(?:{_MATH_ENV_NAMES})\}}")
_ENV_ANY_RE = re.compile(
    rf"(\\begin\{{(?:{_MATH_ENV_NAMES})\}}[\s\S]*?\\end\{{(?:{_MATH_ENV_NAMES})\}})"
)
_ENV_ONLY_RE = re.compile(
    rf"^\\begin\{{(?:{_MATH_ENV_NAMES})\}}[\s\S]*\\end\{{(?:{_MATH_ENV_NAMES})\}}$"
)
_INLINE_MULTILINE_RE = re.compile(r"\$([^$\n]*\n[^$]*?)\$")
_INLINE_MATH_RE = re.compile(r"\$([^$\n]+)\$|\\\((.+?)\\\)")

_LEADING_JUNK_RE = re.compile(r"^\s*(?:\*{2,}|[}\s]*\}+|\*\s*)+")
_TRAILING_MARKS_RE = re.compile(r"(?:\s*\*{4,})+\s*$")
_EMPTY_PLACEHOLDER_RE = re.compile(r"(?<!\\)\[\s*\]")
_BLANK_IN_DISPLAY_RE = re.compile(r"(\$\$[^$]*?)\n[ \t]*\n([^$]*?\$\$)")


def strip_currency_dollars(text: str) -> str:
    """Remove dollar signs used as currency, never maths delimiters."""
    text = re.sub(r"(?<=[\s(])\$[ \t]+(?=\d)", "", text)
    # "US$" and "US$ 2.04" are currency; a maths delimiter never follows a letter.
    text = re.sub(r"(?<=\bUS)\$", "", text)
    text = re.sub(r"(?<=[A-Za-z])\$(?=[\s\d.,;:)])", "", text)
    if text.count("$") % 2:
        text = re.sub(r"(?<=[\s(])\$(?=\d)", "", text)
    return text


def drop_inline_footers(text: str) -> str:
    for pattern in _INLINE_FOOTER_RES:
        text = pattern.sub("", text)
    return text


def strip_trailing_header(text: str) -> str:
    starts = [m.start() for m in (_r.search(text) for _r in _TRUNCATE_RES) if m]
    if starts:
        cut = min(starts)
        if cut > 40:
            return text[:cut].rstrip()
    return text


def strip_scaffolding(text: str) -> str:
    text = re.sub(r"^\s*\\(?:begin|end)\{document\}\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(
        r"^\s*\\(?:documentclass|usepackage|geometry)\b[^\n]*$", "", text, flags=re.MULTILINE
    )
    return re.sub(r"(?m)^\s*```(?:latex|tex)?\s*$", "", text)


def looks_like_prose(content: str) -> bool:
    """True when a "display block" actually holds a sentence, not an expression.

    Extraction frequently leaves a stray fence pair wrapped around ordinary
    question text, e.g. ``$$ Show that the statistic $T$ is sufficient. $$``.
    Rendering that as display maths destroys the sentence, so it is unwrapped.
    """
    if _MATH_ENV_RE.search(content):
        return False
    without_inline = re.sub(r"\\\([\s\S]*?\\\)", " ", content)
    without_inline = re.sub(r"\$[^$]*\$", " ", without_inline)
    words = re.findall(r"[A-Za-z]{3,}", without_inline)
    return len(words) >= 6


_INLINE_PAIR_RE = re.compile(r"\$([^$]*)\$")


def fix_inline_pairs(prose: str) -> str:
    """Repair single-dollar pairs that span a newline.

    An inline pair cannot cross a line break, so extraction that dropped a fence
    leaves one. When the span is really an expression it becomes a display block;
    when it holds prose the stray dollars are removed and the words kept.
    """

    def repl(match: re.Match[str]) -> str:
        body = match.group(1)
        if "\n" not in body:
            return match.group(0)
        stripped = body.strip()
        words = re.findall(r"[A-Za-z]{3,}", stripped)
        if not stripped:
            return ""
        if len(words) >= 4:
            return stripped
        return "$$\n" + stripped + "\n$$"

    return _INLINE_PAIR_RE.sub(repl, prose)


_MATH_LINE_CHARS = re.compile(r"^[\s\d.A-Za-z+\-*/=<>\\{}\[\]()^_,:;!|&~%]+$")


def wrap_bare_latex_lines(text: str) -> str:
    """Give a display block to a maths line that lost its fences.

    Only lines that (i) sit outside display maths, (ii) begin with a LaTeX command,
    and (iii) hold no word of four or more letters outside their commands are
    wrapped, so ordinary prose is never affected.
    """
    pieces = text.split("$$")
    for index in range(0, len(pieces), 2):
        lines = pieces[index].split("\n")
        for position, line in enumerate(lines):
            stripped = line.strip()
            if (
                stripped.startswith("\\")
                and not stripped.startswith(("\\begin{", "\\end{"))
                and _MATH_LINE_CHARS.match(stripped)
                and not re.search(r"[A-Za-z]{4,}", re.sub(r"\\[A-Za-z]+", "", stripped))
            ):
                lines[position] = "$$\n" + stripped + "\n$$"
        pieces[index] = "\n".join(lines)
    return "$$".join(pieces)


# A single dollar stretched around a display block: "$f(x,θ) = $$ cases $$ $".
_DOLLAR_WRAPPED_DISPLAY_RE = re.compile(
    r"\$([^$\n]*?)\s*\$\$(\s*\\begin\{[\s\S]*?\\end\{[^}]*\})\s*\$\$\s*\$"
)
_DOLLAR_ONLY_DISPLAY_RE = re.compile(r"\$\s*\n?\s*\$\$(\s*\\begin\{[\s\S]*?\\end\{[^}]*\})\s*\$\$\s*\$")


def unwrap_dollar_wrapped_display(text: str) -> str:
    """Turn ``$expr $$ env $$ $`` into a single display block.

    A closing ``$`` on its own line after a display block is always spurious; the
    expression and the environment belong in one block.
    """

    def join(match: re.Match[str]) -> str:
        head = (match.group(1) or "").strip()
        env = match.group(2).strip()
        return "$$\n" + (head + "\n" + env if head else env) + "\n$$"

    def join_only(match: re.Match[str]) -> str:
        return "$$\n" + match.group(1).strip() + "\n$$"

    previous = None
    while previous != text:
        previous = text
        text = _DOLLAR_WRAPPED_DISPLAY_RE.sub(join, text)
        text = _DOLLAR_ONLY_DISPLAY_RE.sub(join_only, text)
    return text


def normalize_display_math(text: str) -> str:
    """Repair the display-math structure while preserving every other byte."""
    text = text.replace("\\[", "$$").replace("\\]", "$$")
    if "$$" not in text:
        return text

    pieces = text.split("$$")
    units = [
        {"kind": "display" if index % 2 else "prose", "text": chunk}
        for index, chunk in enumerate(pieces)
    ]
    if len(pieces) % 2 == 0:
        orphan = units.pop()
        units[-1]["text"] += orphan["text"]

    merged: list[dict[str, str]] = []
    index = 0
    while index < len(units):
        unit = units[index]
        if (
            unit["kind"] == "display"
            and index + 2 < len(units)
            and units[index + 1]["kind"] == "prose"
            and not units[index + 1]["text"].strip()
            and units[index + 2]["kind"] == "display"
            and _ENV_ONLY_RE.match(units[index + 2]["text"].strip() or "x")
        ):
            merged.append(
                {
                    "kind": "display",
                    "text": unit["text"].rstrip() + "\n" + units[index + 2]["text"].strip() + "\n",
                }
            )
            index += 3
            continue
        merged.append({"kind": unit["kind"], "text": unit["text"]})
        index += 1

    # A maths environment left in prose would print as raw LaTeX, so it is given
    # its own display block.
    expanded: list[dict[str, str]] = []
    for unit in merged:
        if unit["kind"] == "prose" and _MATH_ENV_RE.search(unit["text"]):
            cursor = 0
            for match in _ENV_ANY_RE.finditer(unit["text"]):
                expanded.append({"kind": "prose", "text": unit["text"][cursor:match.start()]})
                expanded.append({"kind": "display", "text": match.group(1)})
                cursor = match.end()
            expanded.append({"kind": "prose", "text": unit["text"][cursor:]})
        else:
            expanded.append(unit)

    rendered = []
    for unit in expanded:
        if unit["kind"] != "display":
            rendered.append(fix_inline_pairs(unit["text"]))
            continue
        if not unit["text"].strip():
            continue
        if looks_like_prose(unit["text"]):
            rendered.append(fix_inline_pairs(unit["text"]))
        else:
            body = re.sub(r"\n[ \t]*\n+", "\n", unit["text"].strip())
            rendered.append("$$" + body + "$$")
    return "".join(rendered)


def hoist_multiline_inline_math(text: str) -> str:
    """An inline pair stretched over a newline is really display maths."""
    return _INLINE_MULTILINE_RE.sub(lambda m: "$$\n" + m.group(1).strip() + "\n$$", text)


def insert_math_boundary_spaces(text: str) -> str:
    out, last = [], 0
    for match in _INLINE_MATH_RE.finditer(text):
        body = (match.group(1) if match.group(1) is not None else match.group(2) or "").strip()
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


def environments_outside_math(text: str) -> list[str]:
    stripped = re.sub(r"\$\$[\s\S]*?\$\$", "", text)
    stripped = re.sub(r"\\\[[\s\S]*?\\\]", "", stripped)
    stripped = re.sub(r"\\\([\s\S]*?\\\)", "", stripped)
    return _MATH_ENV_RE.findall(stripped)


def orphan_fences(text: str) -> list[str]:
    """A lone ``$`` on its own line is always a broken fence.

    A ``$$`` line is the correct way to open a display block, so it is not flagged;
    empty or unclosed blocks are caught by the application's own validator.
    """
    return [line.strip() for line in text.split("\n") if line.strip() == "$"]


def repair_text(raw: str) -> tuple[str, list[str]]:
    text = str(raw or "")
    changes: list[str] = []

    def apply(new: str, label: str) -> None:
        nonlocal text
        if new != text:
            changes.append(label)
            text = new

    apply(_strip_safe_question_extraction_artifacts(text), "stripped extraction artifacts")
    apply(strip_scaffolding(text), "removed the document scaffold")
    apply(_LEADING_JUNK_RE.sub("", text), "removed a stray leading brace or bold marker")
    apply(drop_inline_footers(text), "removed inline page footer")
    apply(strip_trailing_header(text), "cut the next paper's cover page")
    for pattern in _ADVERT_RES:
        apply(pattern.sub("", text), "removed an advertising quotation")
    apply(_EMPTY_PLACEHOLDER_RE.sub("", text), "removed an empty extraction placeholder")
    apply(unwrap_dollar_wrapped_display(text), "unwrapped a display block held in single dollars")
    apply(normalize_display_math(text), "repaired the display-math structure")
    apply(wrap_bare_latex_lines(text), "gave a display block to a stray maths line")
    apply(strip_currency_dollars(text), "removed currency dollar signs")
    apply(insert_math_boundary_spaces(text), "spaced inline maths away from the prose")
    apply(_BLANK_IN_DISPLAY_RE.sub(r"\1\n\2", text), "removed a blank line inside display math")
    apply(_TRAILING_MARKS_RE.sub("", text), "removed trailing bold marks")
    apply(_JUNK_LINE_RE.sub("", text), "removed leftover page furniture")
    apply(re.sub(r"\n{3,}", "\n\n", text).strip(), "collapsed blank lines")
    return text, changes


def is_acceptable(before: str, after: str) -> tuple[bool, str]:
    remaining = assessment_question_rendering_issues(after)
    if remaining:
        return False, "; ".join(remaining)
    if _RESIDUAL_FURNITURE_RE.search(after):
        return False, "page furniture survived the repair"
    stranded = environments_outside_math(after)
    if stranded:
        return False, f"maths environment outside display math ({', '.join(sorted(set(stranded)))})"
    frozen = orphan_fences(after)
    if frozen:
        return False, f"{len(frozen)} stranded math fence line(s)"
    kept = len("".join(after.split()))
    original = len("".join(before.split()))
    if original and kept < 0.15 * original:
        return False, f"repair would discard {100 * (1 - kept / original):.0f}% of the text"
    return True, ""


def main() -> None:
    apply_write = "--apply" in sys.argv

    rows = list(PrepQuestion.objects.filter(topic__course_id=COURSE_ID).order_by("id"))
    flagged = [q for q in rows if q.verification_status == "flagged"]

    clean_now, still_bad = [], []
    for q in flagged:
        before = q.question_latex or ""
        if not assessment_question_rendering_issues(before):
            # Already valid: rewriting it here would only risk breaking it, because
            # the normaliser re-emits display blocks.
            still_bad.append((q, "already passes the validator (stale flag)"))
            continue
        after, changes = repair_text(before)
        if after == before:
            still_bad.append((q, "no change"))
            continue
        ok, why = is_acceptable(before, after)
        if ok:
            clean_now.append((q, after, changes))
        else:
            still_bad.append((q, why))

    print(f"flagged: {len(flagged)} | fixable: {len(clean_now)} | still failing: {len(still_bad)}")
    from collections import Counter

    counter = Counter()
    for _q, why in still_bad:
        for part in str(why).split("; "):
            counter[part] += 1
    for label, count in counter.most_common():
        print(f"   {count:3d}  {label}")
    print("ids still failing:", sorted(q.id for q, _ in still_bad))

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
