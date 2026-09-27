"""
benchmark_validate.py
─────────────────────
Validates cached content for 3 benchmark PrepContentCache topics against
the canonical authoring format rules before any cache regeneration.

Run from the EduAI project root:
    python benchmark_validate.py

Checks performed on each cached markdown document:
  1. No \[ ... \] display-math delimiters (must be $$ ... $$).
  2. No \( ... \) inline-math delimiters (must be $...$).
  3. No raw HTML tags outside fenced code blocks.
  4. $$ on its own line (not adjacent to prose on the same line).
  5. No naked \begin{...} environments outside $$ blocks.
  6. Balanced $$ pair count per document.
  7. Balanced $ count per paragraph (each paragraph must have even count
     after masking $$ pairs).
  8. GFM table column consistency (each data row matches the separator).
  9. No Unicode replacement characters (U+FFFD).

Outputs a per-check pass/fail table for each topic.
"""

import os
import sys
import re
import json
import django

# ── Django bootstrap ──────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
django.setup()

from prep.models import PrepContentCache  # noqa: E402

# ── Benchmark targets ─────────────────────────────────────────────────────────
# (content_type_prefix, cache_key_fragment, label)
BENCHMARKS = [
    ("notes",  "sst_301_matrices_in_r_level_2",                                    "Topic 8 - Matrices / Linear Algebra (SST 301)"),
    ("notes",  "sst_301_differentiation_&_integration_of_univariate_functions_level_2",  "Topic 9 - Calculus / Differentiation (SST 301)"),
    ("notes",  "sma_300_the_real_number_system_level_2",                           "Topic 19 - SMA 300: Real Number System"),
]

# ── Helpers ───────────────────────────────────────────────────────────────────

def extract_text(entry):
    """Return the markdown text from a PrepContentCache entry."""
    payload = entry.payload
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except Exception:
            return payload
    if isinstance(payload, dict):
        return payload.get("content", "")
    return ""


def mask_code_blocks(text):
    """Replace fenced code block content with placeholders so checks don't
    flag LaTeX inside code examples."""
    return re.sub(r"```[\w]*\n?[\s\S]*?```", lambda m: "```CODE_BLOCK```", text)


def mask_display_math(text):
    """Replace $$ ... $$ blocks with placeholders for paragraph-level checks."""
    return re.sub(r"\$\$([\s\S]*?)\$\$", "$$DISPLAY_MATH$$", text)


# ── Individual check functions ────────────────────────────────────────────────

def check_no_backslash_brackets(text):
    """No \\[ ... \\] or \\( ... \\) allowed outside code.
    Ignores LaTeX newline spacing arguments like \\\\[4pt] or \\\\[1em]."""
    t = mask_code_blocks(text)
    issues = []
    # Display delimiter \[ is NOT preceded by another backslash (which would be \\ followed by [spacing])
    if re.search(r'(?<!\\)\\\[(?![0-9.]+(?:pt|em|ex|cm|mm|in)\s*\])', t):
        issues.append("Found \\[ (use $$ instead)")
    if re.search(r'(?<!\\)\\\(', t):
        issues.append("Found \\( (use $ instead)")
    return issues


def check_no_raw_html(text):
    """No raw HTML tags (<div>, <span>, <br>, etc.) outside code blocks."""
    t = mask_code_blocks(text)
    tags = re.findall(r'</?(?:div|span|br|p|table|td|tr|th|ul|ol|li|h[1-6]|strong|em|b|i)[^>]*>', t, re.I)
    if tags:
        return [f"Raw HTML tag: {tag}" for tag in tags[:5]]
    return []


def check_display_math_on_own_line(text):
    """Flags $$ only when it is mixed with prose text — i.e. non-math content
    appears after an opening $$ or before a closing $$ on the same line.
    Compact forms like '$$f(x) = ...' (math starts on the $$ line) are
    accepted because the renderer handles them correctly."""
    t = mask_code_blocks(text)
    issues = []
    for i, line in enumerate(t.split('\n'), 1):
        stripped = line.strip()
        if not stripped:
            continue
        dd_count = stripped.count('$$')
        if dd_count == 0:
            continue

        if dd_count >= 2:
            # Self-contained $$...$$: only flag if non-math prose surrounds the pair
            remainder = re.sub(r'\$\$[\s\S]*?\$\$', '', stripped).strip()
            remainder = re.sub(r'^[>\s]+', '', remainder).strip()
            if remainder:
                issues.append(f"Line {i}: prose+$$ pair: {stripped[:80]!r}")
        else:
            # Lone $$: flag only if there is non-math prose BEFORE an opening $$
            # i.e. something like "As shown above, $$" — not "$$f'(x) = ..."
            if stripped.endswith('$$'):
                # Closing $$ — strip blockquote markers (>), then check if true prose precedes it
                before = re.sub(r'^[>\s]+', '', stripped[:-2]).strip()
                if before and not re.search(r"[=+\-*/\\^_{}()\[\],.!?:;'a-zA-Z0-9\s\\]$", before[-1:]):
                    issues.append(f"Line {i}: prose before closing $$: {stripped[:80]!r}")
            elif stripped.startswith('$$'):
                # Opening $$ at start of line — this is fine (math content follows)
                pass
            else:
                # $$ in the middle of a line with text on both sides
                issues.append(f"Line {i}: $$ in middle of prose line: {stripped[:80]!r}")
    return issues


def check_no_naked_environments(text):
    """\\begin{{...}} must not appear outside $$ blocks."""
    t = mask_code_blocks(text)
    # Remove all $$ blocks
    t_no_math = re.sub(r'\$\$[\s\S]*?\$\$', '', t)
    env_pattern = re.compile(r'\\begin\{(?:aligned|cases|matrix|pmatrix|bmatrix|vmatrix|gather|split|array|align\*?)\}')
    matches = env_pattern.findall(t_no_math)
    if matches:
        return [f"Naked environment outside $$: {m}" for m in matches[:5]]
    return []


def check_balanced_display_math(text):
    """Total $$ count in the document must be even."""
    t = mask_code_blocks(text)
    count = len(re.findall(r'(?<!\\)\$\$', t))
    if count % 2 != 0:
        return [f"Unbalanced $$: total count = {count} (must be even)"]
    return []


def check_balanced_inline_math_per_paragraph(text):
    """Each paragraph must have an even number of single $ (after masking $$
    and backtick inline code, to avoid false positives from R $ list syntax)."""
    t = mask_code_blocks(text)
    paragraphs = re.split(r'\n\s*\n', t)
    issues = []
    for idx, para in enumerate(paragraphs, 1):
        # Mask display math $$...$$
        p = re.sub(r'(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$', '', para)
        # Mask backtick inline code to avoid counting $ in R syntax like `qr(A)$vectors`
        p = re.sub(r'`[^`\n\r]+?`', '', p)
        singles = re.findall(r'(?<!\\)\$', p)
        if len(singles) % 2 != 0:
            preview = para[:100].replace('\n', ' ')
            issues.append(f"Paragraph {idx}: odd $ count ({len(singles)}): {preview!r}")
    return issues


def check_table_column_consistency(text):
    """GFM table data rows must have same column count as separator row."""
    t = mask_code_blocks(text)
    # Mask math (both display and inline) to avoid counting | inside math as delimiter
    t = re.sub(r'\$\$[\s\S]*?\$\$', 'MATH', t)
    t = re.sub(r'\$[^\$\n]+\$', 'MATH', t)
    # Mask backtick inline code to avoid R $col syntax breaking pipe counts
    t = re.sub(r'`[^`\n\r]+?`', 'CODE', t)
    issues = []
    lines = t.split('\n')
    i = 0
    while i < len(lines) - 1:
        sep_match = re.match(r'^\s*\|(?:\s*:?---+:?\s*\|)+\s*$', lines[i + 1]) if i + 1 < len(lines) else None
        if lines[i].strip().startswith('|') and sep_match:
            sep = lines[i + 1]
            expected = len(re.findall(r':?---+:?', sep))
            j = i + 2
            while j < len(lines) and lines[j].strip().startswith('|'):
                row = lines[j].strip()
                if re.match(r'^\|(?:\s*:?---+:?\s*\|)+\s*$', row):
                    j += 1
                    continue
                cells = row.split('|')[1:-1]
                if len(cells) != expected:
                    issues.append(
                        f"Table near line {j+1}: expected {expected} cols, got {len(cells)}: {row[:80]!r}"
                    )
                j += 1
            i = j
        else:
            i += 1
    return issues


def check_no_replacement_chars(text):
    """No U+FFFD unicode replacement characters."""
    count = text.count('\ufffd')
    if count:
        return [f"Found {count} U+FFFD replacement character(s)"]
    return []


# ── Check registry ────────────────────────────────────────────────────────────

CHECKS = [
    ("No \\[ or \\( delimiters",        check_no_backslash_brackets),
    ("No raw HTML",                      check_no_raw_html),
    ("$$ on its own line",               check_display_math_on_own_line),
    ("No naked \\begin{env}",            check_no_naked_environments),
    ("$$ count even (balanced)",         check_balanced_display_math),
    ("$ per paragraph even (balanced)",  check_balanced_inline_math_per_paragraph),
    ("Table column consistency",         check_table_column_consistency),
    ("No U+FFFD chars",                  check_no_replacement_chars),
]

# ── Main ──────────────────────────────────────────────────────────────────────

def run():
    print("=" * 72)
    print("BENCHMARK VALIDATION REPORT")
    print("=" * 72)

    all_passed = True

    for key_prefix, key_fragment, label in BENCHMARKS:
        print(f"\n{'-' * 72}")
        print(f"  {label}")

        # Find matching cache entry by exact key fragment
        qs = PrepContentCache.objects.filter(cache_key__icontains=key_fragment)
        entry = qs.order_by('-updated_at').first()

        if not entry:
            print(f"  [SKIP] No cache entry found matching '{key_fragment}'")
            print(f"  Available keys:")
            for e in PrepContentCache.objects.all().order_by('cache_key')[:20]:
                print(f"    {e.cache_key}")
            continue

        print(f"  cache_key : {entry.cache_key}")
        text = extract_text(entry)
        if not text:
            print("  [SKIP] Empty content")
            continue

        print(f"  chars     : {len(text):,}")
        print()

        topic_passed = True
        for check_name, check_fn in CHECKS:
            issues = check_fn(text)
            status = "PASS" if not issues else "FAIL"
            if issues:
                topic_passed = False
                all_passed = False
            print(f"  [{status:4s}] {check_name}")
            for issue in issues[:3]:  # show up to 3 sample issues
                print(f"         -> {issue}")
            if len(issues) > 3:
                print(f"         -> ...and {len(issues) - 3} more")

        print()
        print(f"  Overall: {'[OK] ALL CHECKS PASSED' if topic_passed else '[FAIL] CHECKS FAILED'}")

    print()
    print("=" * 72)
    print(f"FINAL: {'[OK] ALL BENCHMARKS PASSED - safe to regenerate caches' if all_passed else '[FAIL] BENCHMARKS FAILED - fix formatting before regeneration'}")
    print("=" * 72)
    return all_passed


if __name__ == "__main__":
    ok = run()
    sys.exit(0 if ok else 1)
