"""
Mentify Prep — Structured Block Schema, Validator, and Converters.

Industry-standard JSON Block Architecture for academic lecture notes,
derivations, callouts, and mathematical proofs.
"""

from __future__ import annotations
import re
from typing import Any, Dict, List, Optional, Tuple


VALID_BLOCK_TYPES = {
    "heading",
    "paragraph",
    "math",
    "table",
    "code",
    "callout",
    "list",
    "divider",
}

VALID_CALLOUT_STYLES = {
    "theorem",
    "definition",
    "proof",
    "example",
    "remark",
    "warning",
    "insight",
    "note",
}


def validate_structured_blocks(blocks: Any) -> Tuple[bool, str]:
    """
    Server-side validation for structured block notes.
    Rejects malformed output with specific error messages.
    """
    if not isinstance(blocks, list):
        return False, "Notes payload must be a JSON array of blocks."

    if len(blocks) == 0:
        return False, "Notes payload cannot be empty."

    for idx, b in enumerate(blocks):
        if not isinstance(b, dict):
            return False, f"Block at index {idx} is not an object."

        b_type = b.get("type")
        if b_type not in VALID_BLOCK_TYPES:
            return False, f"Block at index {idx} has invalid type '{b_type}'. Allowed: {sorted(VALID_BLOCK_TYPES)}"

        if b_type == "heading":
            level = b.get("level")
            text = b.get("text")
            if not isinstance(level, int) or not (1 <= level <= 6):
                return False, f"Heading block at index {idx} must have an integer level between 1 and 6."
            if not isinstance(text, str) or not text.strip():
                return False, f"Heading block at index {idx} has empty text."

        elif b_type == "paragraph":
            text = b.get("text")
            if not isinstance(text, str):
                return False, f"Paragraph block at index {idx} must have a string 'text' field."

        elif b_type == "math":
            latex = b.get("latex")
            if not isinstance(latex, str) or not latex.strip():
                return False, f"Math block at index {idx} has empty LaTeX string."
            # Check curly brace balance
            if latex.count("{") != latex.count("}"):
                return False, f"Math block at index {idx} has unbalanced curly braces: {latex[:80]}"

        elif b_type == "table":
            headers = b.get("headers")
            rows = b.get("rows")
            if not isinstance(headers, list) or len(headers) == 0:
                return False, f"Table block at index {idx} must have non-empty 'headers' list."
            if not isinstance(rows, list):
                return False, f"Table block at index {idx} must have a 'rows' list."
            expected_cols = len(headers)
            for r_idx, row in enumerate(rows):
                if not isinstance(row, list) or len(row) != expected_cols:
                    actual = len(row) if isinstance(row, list) else type(row).__name__
                    return False, (
                        f"Table block at index {idx}, row {r_idx} has {actual} columns; "
                        f"expected {expected_cols} (matching headers)."
                    )

        elif b_type == "code":
            code = b.get("code")
            if not isinstance(code, str):
                return False, f"Code block at index {idx} must have a string 'code' field."

        elif b_type == "callout":
            style = b.get("style", "note")
            if style not in VALID_CALLOUT_STYLES:
                return False, f"Callout block at index {idx} has invalid style '{style}'."
            if not b.get("title") and not b.get("content"):
                return False, f"Callout block at index {idx} must have either 'title' or 'content'."

        elif b_type == "list":
            items = b.get("items")
            if not isinstance(items, list):
                return False, f"List block at index {idx} must have an 'items' array."

    return True, ""


def blocks_to_markdown(blocks: List[Dict[str, Any]]) -> str:
    """
    Renders structured blocks to clean, standard GitHub Flavored Markdown
    for plain-text fallback, export, or CLI display.
    """
    md_parts: List[str] = []

    for b in blocks:
        t = b.get("type")
        if t == "heading":
            lvl = "#" * b.get("level", 2)
            md_parts.append(f"\n{lvl} {b.get('text', '').strip()}\n")

        elif t == "paragraph":
            text = b.get("text", "").strip()
            if text:
                md_parts.append(f"{text}\n")

        elif t == "math":
            latex = b.get("latex", "").strip()
            if latex:
                md_parts.append(f"$$\n{latex}\n$$\n")

        elif t == "table":
            headers = [str(h).strip() for h in b.get("headers", [])]
            rows = [[str(cell).strip() for cell in r] for r in b.get("rows", [])]
            if headers:
                header_line = "| " + " | ".join(headers) + " |"
                sep_line = "| " + " | ".join(["---"] * len(headers)) + " |"
                row_lines = ["| " + " | ".join(r) + " |" for r in rows]
                md_parts.append("\n" + "\n".join([header_line, sep_line] + row_lines) + "\n")

        elif t == "code":
            lang = b.get("language", "").strip()
            code = b.get("code", "")
            md_parts.append(f"\n```{lang}\n{code}\n```\n")

        elif t == "callout":
            title = b.get("title", "").strip()
            content = b.get("content", "").strip()
            math = b.get("math", "").strip()
            lines: List[str] = []
            if title:
                lines.append(f"> **{title}**")
            if content:
                for cl in content.split("\n"):
                    lines.append(f"> {cl}")
            if math:
                lines.append("> $$")
                for ml in math.split("\n"):
                    lines.append(f"> {ml}")
                lines.append("> $$")
            if lines:
                md_parts.append("\n" + "\n".join(lines) + "\n")

        elif t == "list":
            ordered = b.get("ordered", False)
            for idx, item in enumerate(b.get("items", []), 1):
                prefix = f"{idx}." if ordered else "-"
                md_parts.append(f"{prefix} {item}")
            md_parts.append("")

        elif t == "divider":
            md_parts.append("\n---\n")

    return "\n".join(md_parts).strip()


def parse_markdown_to_blocks(raw_markdown: str) -> List[Dict[str, Any]]:
    """
    Deterministically transforms existing/legacy Markdown into structured blocks.
    Accurately isolates:
    - Headings (##, ###)
    - Code fences (```...```)
    - Display math ($$...$$ and \\begin{env}...\\end{env})
    - Tables (| ... |)
    - Callout blocks (> **Theorem...**)
    - Regular paragraphs
    """
    if not raw_markdown:
        return []

    text = str(raw_markdown).replace("\r\n", "\n").replace("\r", "\n")
    # Normalize escaped newlines
    text = re.sub(r"\\n(?![a-zA-Z])", "\n", text)
    # Normalize unicode replacement characters
    text = text.replace('\ufffd', '—')

    lines = text.split("\n")
    blocks: List[Dict[str, Any]] = []

    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # 1. Blank line
        if not stripped:
            i += 1
            continue

        # 2. Markdown Headings (# Header)
        m_head = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m_head:
            level = len(m_head.group(1))
            h_text = m_head.group(2).strip()
            # Clean trailing dollars or markdown decorators
            h_text = re.sub(r"\$+$", "", h_text).strip()
            blocks.append({
                "type": "heading",
                "level": level,
                "text": h_text
            })
            i += 1
            continue

        # 3. Horizontal Rule
        if re.match(r"^(?:---|\*\*\*|___)$", stripped):
            blocks.append({"type": "divider"})
            i += 1
            continue

        # 4. Fenced Code Blocks (```lang ... ```)
        if stripped.startswith("```"):
            lang = stripped[3:].strip().lower()
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            if i < n and lines[i].strip().startswith("```"):
                i += 1  # Skip closing fence
            blocks.append({
                "type": "code",
                "language": lang or "text",
                "code": "\n".join(code_lines)
            })
            continue

        # 5. Display Math ($$ ... $$)
        if stripped == "$$" or stripped.startswith("$$"):
            # Check if self-contained on single line: $$ formula $$
            m_single = re.match(r"^\$\$(.+?)\$\$$", stripped)
            if m_single:
                latex = m_single.group(1).strip()
                if latex:
                    blocks.append({
                        "type": "math",
                        "display": True,
                        "latex": latex
                    })
                i += 1
                continue

            # Multi-line display math
            math_lines = []
            if len(stripped) > 2:
                math_lines.append(stripped[2:])
            i += 1
            while i < n and not lines[i].strip().endswith("$$"):
                math_lines.append(lines[i])
                i += 1
            if i < n:
                last_line = lines[i].strip()
                if last_line != "$$":
                    math_lines.append(last_line[:-2].strip())
                i += 1  # Skip closing $$
            latex = "\n".join(math_lines).strip()
            if latex:
                blocks.append({
                    "type": "math",
                    "display": True,
                    "latex": latex
                })
            continue

        # 6. Naked \\begin{env} ... \\end{env}
        env_match = re.match(r"^\s*(\\begin\{(aligned|cases|matrix|pmatrix|bmatrix|vmatrix|gather|split|array|align\*?)\}.*)$", line)
        if env_match:
            env_name = env_match.group(2)
            env_lines = [line.strip()]
            i += 1
            close_target = f"\\end{{{env_name}}}"
            while i < n:
                curr = lines[i].strip()
                env_lines.append(curr)
                i += 1
                if close_target in curr:
                    break
            blocks.append({
                "type": "math",
                "display": True,
                "latex": "\n".join(env_lines)
            })
            continue

        # 7. Markdown Tables (| ... |)
        if stripped.startswith("|") and stripped.endswith("|") and "|" in stripped[1:-1]:
            table_lines = [stripped]
            i += 1
            while i < n and lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
                table_lines.append(lines[i].strip())
                i += 1

            if len(table_lines) >= 2:
                headers = [c.strip() for c in table_lines[0].split("|")[1:-1]]
                row_start = 1
                # Skip separator row if present (|---|---|)
                if re.match(r"^[|\s\-:]+$", table_lines[1]):
                    row_start = 2
                rows = []
                for tl in table_lines[row_start:]:
                    cells = [c.strip() for c in tl.split("|")[1:-1]]
                    # Normalise cell count to match headers
                    if len(cells) < len(headers):
                        cells.extend([""] * (len(headers) - len(cells)))
                    elif len(cells) > len(headers):
                        cells = cells[:len(headers)]
                    rows.append(cells)

                blocks.append({
                    "type": "table",
                    "headers": headers,
                    "rows": rows
                })
                continue
            else:
                # Fallback to paragraph if only 1 line with pipes
                blocks.append({
                    "type": "paragraph",
                    "text": table_lines[0]
                })
                continue

        # 8. Callout Blocks (> **Theorem ...** or > **Definition ...**)
        if stripped.startswith(">"):
            callout_lines = []
            while i < n and (lines[i].strip().startswith(">") or (lines[i].strip() and not lines[i].strip().startswith("#"))):
                callout_lines.append(re.sub(r"^\s*>\s*", "", lines[i]))
                i += 1
            full_callout = "\n".join(callout_lines).strip()
            
            # Detect callout style and title
            style = "note"
            title = ""
            content = full_callout

            title_m = re.match(r"^\s*\*\*(Theorem|Definition|Lemma|Axiom|Proof|Example|Corollary|Remark|Warning|Insight|Pattern)[^\*]*\*\*[:\.]?\s*", full_callout, re.IGNORECASE)
            if title_m:
                matched_header = title_m.group(0).strip()
                kind = title_m.group(1).lower()
                style_map = {
                    "theorem": "theorem",
                    "lemma": "theorem",
                    "axiom": "theorem",
                    "corollary": "theorem",
                    "definition": "definition",
                    "proof": "proof",
                    "example": "example",
                    "pattern": "example",
                    "remark": "remark",
                    "warning": "warning",
                    "insight": "insight"
                }
                style = style_map.get(kind, "note")
                title = matched_header.strip("* :.")
                content = full_callout[len(matched_header):].strip()

            blocks.append({
                "type": "callout",
                "style": style,
                "title": title,
                "content": content
            })
            continue

        # 9. List Items (- Item or 1. Item)
        list_m = re.match(r"^(\*|-|\d+\.)\s+(.*)$", stripped)
        if list_m and not stripped.startswith("**"):
            ordered = list_m.group(1)[0].isdigit()
            items = [list_m.group(2).strip()]
            i += 1
            while i < n:
                next_stripped = lines[i].strip()
                next_m = re.match(r"^(\*|-|\d+\.)\s+(.*)$", next_stripped)
                if next_m and not next_stripped.startswith("**"):
                    items.append(next_m.group(2).strip())
                    i += 1
                elif not next_stripped:
                    # Look ahead 1 line
                    if i + 1 < n and re.match(r"^(\*|-|\d+\.)\s+", lines[i+1].strip()):
                        i += 1
                        continue
                    else:
                        break
                else:
                    break
            blocks.append({
                "type": "list",
                "ordered": ordered,
                "items": items
            })
            continue

        # 10. Regular Paragraph
        para_lines = [line]
        i += 1
        while i < n:
            curr = lines[i]
            curr_str = curr.strip()
            if not curr_str:
                break
            # Stop if next line starts a structural block
            if curr_str.startswith("#") or curr_str.startswith("```") or curr_str.startswith("$$") or curr_str.startswith(">") or (curr_str.startswith("|") and curr_str.endswith("|")):
                break
            if re.match(r"^(\*|-|\d+\.)\s+", curr_str) and not curr_str.startswith("**"):
                break
            para_lines.append(curr)
            i += 1

        blocks.append({
            "type": "paragraph",
            "text": "\n".join(para_lines).strip()
        })

    return blocks
