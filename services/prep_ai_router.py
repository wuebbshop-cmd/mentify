"""
services/prep_ai_router.py

Mentify Prep AI Model Router & Zero-Cost Content Cache:
1. Zero-marginal-cost Database Cache (PrepContentCache).
2. SymPy Deterministic Symbolic Mathematics ($0 token cost, 100% precision).
3. Dual-Model Router:
   - DeepSeek-V3 (`deepseek-chat`) for concept explanations and practice questions.
   - DeepSeek-R1 (`deepseek-reasoner`) for complex mathematical proofs and derivations.
4. Strict safety caps (MAX_TOKENS_EXPLANATION, MAX_TOKENS_REASONING).
"""
from __future__ import annotations

import hashlib
import json
import logging
import os
import re
import requests
try:
    import sympy as sp
except ImportError:
    sp = None
from django.conf import settings
from django.utils import timezone

logger = logging.getLogger(__name__)


def compute_prompt_hash(*args) -> str:
    """Compute deterministic SHA-256 hash of string arguments."""
    normalized = "||".join(str(a).strip().lower() for a in args)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def compute_cache_key(content_type: str, *parts) -> str:
    """Generate a clean namespaced cache key."""
    joined = "_".join(str(p).strip().replace(" ", "_").lower() for p in parts if p)
    return f"{content_type}:{joined}"[:250]


def _topic_notes_cache_signature(course_obj, topic_obj, topic_title: str, subtopics: list | None) -> str:
    """Fingerprint the approved syllabus inputs that determine generated notes."""
    topic_summary = getattr(topic_obj, "summary", "") if topic_obj else ""
    curriculum = []
    if course_obj:
        try:
            curriculum = list(
                course_obj.topics.order_by("order", "id").values_list("order", "title")
            )
        except Exception as exc:
            logger.warning("[Topic Notes] Could not fingerprint curriculum: %s", exc)

    return compute_prompt_hash(
        topic_title,
        topic_summary,
        json.dumps(subtopics or [], ensure_ascii=True, sort_keys=True),
        json.dumps(curriculum, ensure_ascii=True),
    )[:16]


NOTES_CACHE_VERSION = "markdown-katex-v6"
NOTE_VALIDATION_STATE = "validated"
NOTE_MAX_FAILED_GENERATION_CYCLES = 2


def _merge_usage(*usage_items) -> dict:
    """Add provider usage counters across initial and continuation calls."""
    merged = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    for usage in usage_items:
        if not isinstance(usage, dict):
            continue
        prompt = int(usage.get("prompt_tokens") or usage.get("input_tokens") or 0)
        completion = int(usage.get("completion_tokens") or usage.get("output_tokens") or 0)
        total = int(usage.get("total_tokens") or prompt + completion)
        merged["prompt_tokens"] += prompt
        merged["completion_tokens"] += completion
        merged["total_tokens"] += total
    return merged


def _required_note_sections(topic_title: str) -> list[str]:
    """Return the section headings a generated topic note must contain."""
    topic_lower = (topic_title or "").lower()
    is_overview = any(
        word in topic_lower
        for word in ("overview", "introduction", "intro", "outline", "syllabus", "orientation", "prerequisite")
    )
    section_count = 4 if is_overview else 5
    return [f"## {index}." for index in range(1, section_count + 1)]


def _table_cell_count(line: str) -> int:
    """Count Markdown table cells while ignoring the outer pipe characters."""
    return len(line.strip().strip("|").split("|"))


def _markdown_table_issues(content: str) -> list[str]:
    """Find truncated or structurally incomplete Markdown tables."""
    lines = content.splitlines()
    issues: list[str] = []
    index = 0

    while index < len(lines) - 1:
        header = lines[index].strip()
        separator = lines[index + 1].strip()
        is_header = header.startswith("|") and header.endswith("|") and "|" in header[1:-1]
        is_separator = bool(re.fullmatch(r"\|\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|", separator))
        if not (is_header and is_separator):
            index += 1
            continue

        expected_cells = _table_cell_count(header)
        index += 2
        while index < len(lines):
            row = lines[index].strip()
            if not row:
                index += 1
                continue
            if not row.startswith("|"):
                break
            if not row.endswith("|"):
                issues.append(f"incomplete Markdown table row near line {index + 1}")
            elif _table_cell_count(row) != expected_cells:
                issues.append(
                    f"incomplete Markdown table row near line {index + 1} "
                    f"(expected {expected_cells} cells, found {_table_cell_count(row)})"
                )
            index += 1

    return issues


def _display_math_issues(content: str) -> list[str]:
    """Reject malformed display math before it can reach the shared renderer."""
    # Dollar signs in fenced code such as R's `data$column` must never be
    # interpreted as mathematical delimiters.
    source = re.sub(r"```[\s\S]*?```", "", content)
    issues: list[str] = []

    for index, match in enumerate(re.finditer(r"\$\$([\s\S]*?)\$\$", source), start=1):
        expression = match.group(1)
        if not expression.strip():
            issues.append(f"empty display-math block {index}")
            continue
        if re.search(r"\n[ \t]*\n", expression):
            issues.append(f"display-math block {index} contains a blank structural break")
        if re.search(r"\\(?:left|right)[ \t]*(?:\r?\n|$)", expression):
            issues.append(f"display-math block {index} has a split \\left or \\right delimiter")

        left_count = len(re.findall(r"\\left(?![A-Za-z])", expression))
        right_count = len(re.findall(r"\\right(?![A-Za-z])", expression))
        if left_count != right_count:
            issues.append(
                f"display-math block {index} has unmatched \\left/\\right delimiters "
                f"({left_count} left, {right_count} right)"
            )

    return issues


def _unescaped_token_count(value: str, token: str) -> int:
    """Count a one-character token that is not escaped by an odd backslash run."""
    count = 0
    backslashes = 0
    for char in value:
        if char == "\\":
            backslashes += 1
            continue
        if char == token and backslashes % 2 == 0:
            count += 1
        backslashes = 0
    return count


def _latex_syntax_issues(content: str) -> list[str]:
    """Validate LaTex boundaries and grouping without changing note source text."""
    source = re.sub(r"```[\s\S]*?```", "", content)
    issues: list[str] = []

    # Validate inline math after removing complete display blocks. Dollar signs
    # in code have already been removed above.
    source_without_display = re.sub(r"\$\$[\s\S]*?\$\$", "", source)
    inline_dollars = _unescaped_token_count(source_without_display, "$")
    if inline_dollars % 2:
        issues.append("unmatched inline-math delimiter")

    inline_opening = None
    backslashes = 0
    for index, char in enumerate(source_without_display):
        if char == "\\":
            backslashes += 1
            continue
        escaped = backslashes % 2 == 1
        backslashes = 0
        if char != "$" or escaped:
            continue
        if (index > 0 and source_without_display[index - 1] == "$") or (
            index + 1 < len(source_without_display) and source_without_display[index + 1] == "$"
        ):
            continue
        if inline_opening is None:
            inline_opening = index
        else:
            if "\n" in source_without_display[inline_opening + 1:index] or "\r" in source_without_display[inline_opening + 1:index]:
                issues.append("inline-math expression crosses a physical line break")
            inline_opening = None

    for index, match in enumerate(re.finditer(r"\$\$([\s\S]*?)\$\$", source), start=1):
        expression = match.group(1)
        curly_depth = 0
        square_depth = 0
        backslashes = 0

        for char in expression:
            if char == "\\":
                backslashes += 1
                continue
            escaped = backslashes % 2 == 1
            backslashes = 0
            if escaped:
                continue
            if char == "{":
                curly_depth += 1
            elif char == "}":
                curly_depth -= 1
                if curly_depth < 0:
                    issues.append(f"display-math block {index} has an unmatched closing brace")
                    curly_depth = 0
            elif char == "[":
                square_depth += 1
            elif char == "]":
                square_depth -= 1
                if square_depth < 0:
                    issues.append(f"display-math block {index} has an unmatched closing bracket")
                    square_depth = 0

        if curly_depth:
            issues.append(f"display-math block {index} has unmatched braces")
        if square_depth:
            issues.append(f"display-math block {index} has unmatched brackets")

    return issues


def _code_block_issues(content: str) -> list[str]:
    """Reject structural code corruption in generated question and answer blocks."""
    if not isinstance(content, str):
        return []

    issues = []
    if content.count("```") % 2:
        return ["unclosed fenced code block"]

    for index, match in enumerate(re.finditer(r"```([^\n`]*)\n([\s\S]*?)```", content), start=1):
        language = match.group(1).strip().lower()
        code = match.group(2)
        if language in {"r", "rscript"} and re.search(r"\|\s*\r?\n\s*\|", code):
            issues.append(f"R code block {index} has a duplicated boolean operator across lines")
    return issues


def _note_completion_issues(content: str, topic_title: str) -> list[str]:
    """Detect incomplete note output before it is displayed or cached."""
    if not isinstance(content, str) or not content.strip():
        return ["empty content"]

    issues: list[str] = []
    for heading in _required_note_sections(topic_title):
        if not re.search(rf"(?m)^\s*{re.escape(heading)}(?:\s|$)", content):
            issues.append(f"missing section {heading}")

    # A heading alone is not enough: a truncated response can contain the
    # final heading while missing its actual teaching content.
    headings = list(re.finditer(r"(?m)^\s*##\s+\d+\.[^\n]*", content))
    if headings:
        final_body = content[headings[-1].end():].strip()
        if len(final_body) < 120:
            issues.append("final section has insufficient content")

    if content.count("```") % 2:
        issues.append("unclosed fenced code block")
    structural_source = re.sub(r"```[\s\S]*?```", "", content)
    if structural_source.count("$$") % 2:
        issues.append("unclosed display-math block")

    issues.extend(_display_math_issues(content))
    issues.extend(_latex_syntax_issues(content))

    environments = re.findall(r"\\begin\{([^{}]+)\}", structural_source)
    for environment in set(environments):
        if environments.count(environment) != len(re.findall(rf"\\end\{{{re.escape(environment)}\}}", structural_source)):
            issues.append(f"unclosed LaTeX environment {environment}")

    if re.search(r"\\\s*$", content):
        issues.append("content ends at an escape delimiter")

    last_nonempty_line = next((line.strip() for line in reversed(content.splitlines()) if line.strip()), "")
    if last_nonempty_line == "|" or (last_nonempty_line.startswith("|") and not last_nonempty_line.endswith("|")):
        issues.append("content ends with an incomplete Markdown table fragment")

    issues.extend(_markdown_table_issues(content))
    return issues


def get_cached_content(cache_key: str) -> dict | None:
    """
    Retrieve pre-generated verified content from PrepContentCache.
    If found, increments hit_count and returns payload at $0 token cost.
    """
    from prep.models import PrepContentCache
    try:
        cache_entry = PrepContentCache.objects.filter(cache_key=cache_key).first()
        if cache_entry:
            cache_entry.hit_count += 1
            # Reading a cache must not make the note appear freshly edited or
            # invalidate browser/server cache headers based on updated_at.
            cache_entry.save(update_fields=["hit_count"])
            logger.info(f"[PrepCache HIT] {cache_key} (Total hits: {cache_entry.hit_count})")
            payload = cache_entry.payload
            if isinstance(payload, str):
                import json
                try:
                    while isinstance(payload, str):
                        payload = json.loads(payload)
                except Exception:
                    pass
            if isinstance(payload, dict):
                return payload
            return None
    except Exception as e:
        logger.error(f"[PrepCache] Error reading cache {cache_key}: {e}")
    return None


def store_cached_content(
    cache_key: str,
    content_type: str,
    prompt_hash: str,
    payload: dict,
    course=None,
    topic=None,
):
    """Store generated content in PrepContentCache for zero-cost reuse."""
    from prep.models import PrepContentCache
    try:
        PrepContentCache.objects.update_or_create(
            cache_key=cache_key,
            defaults={
                "content_type": content_type,
                "prompt_hash": prompt_hash,
                "payload": payload,
                "course": course,
                "topic": topic,
            },
        )
        logger.info(f"[PrepCache STORED] {cache_key}")
    except Exception as e:
        logger.error(f"[PrepCache] Error storing cache {cache_key}: {e}")


def _cache_payload_as_dict(payload) -> dict | None:
    """Normalize legacy cache payloads without changing the stored record."""
    if isinstance(payload, str):
        try:
            while isinstance(payload, str):
                payload = json.loads(payload)
        except (TypeError, ValueError, json.JSONDecodeError):
            return None
    return payload if isinstance(payload, dict) else None


def repair_json_escaped_latex_newlines(content: str) -> str:
    """Repair JSON-decoded ``\\n`` LaTex commands only while inside math mode.

    Some providers return ``\\notin`` or ``\\neq`` with one slash in JSON. A
    JSON decoder then turns ``\\n`` into a physical newline, leaving ``otin`` or
    ``eq`` inside a math expression. This is a narrow, deterministic repair;
    normal prose line breaks and arbitrary malformed LaTex are left untouched.
    """
    if not isinstance(content, str) or "\n" not in content:
        return content or ""

    suffixes = ("otin", "eq", "abla", "u", "atural", "ewcommand")
    output = []
    mode = None
    index = 0
    backslashes = 0
    length = len(content)

    while index < length:
        char = content[index]
        if char == "\\":
            output.append(char)
            backslashes += 1
            index += 1
            continue

        escaped = backslashes % 2 == 1
        backslashes = 0
        if char == "$" and not escaped:
            is_display = index + 1 < length and content[index + 1] == "$"
            if is_display:
                output.append("$$")
                if mode == "display":
                    mode = None
                elif mode is None:
                    mode = "display"
                index += 2
                continue
            output.append(char)
            if mode == "inline":
                mode = None
            elif mode is None:
                mode = "inline"
            index += 1
            continue

        if char == "\n" and mode:
            remainder = content[index + 1:]
            suffix = next((item for item in suffixes if remainder.startswith(item)), None)
            if suffix:
                boundary = len(suffix)
                if boundary == len(remainder) or not remainder[boundary].isalpha():
                    output.append("\\n")
                    index += 1
                    continue

        output.append(char)
        index += 1

    return "".join(output)


def _publish_legacy_note_cache(entry, payload: dict, topic_title: str) -> dict | None:
    """Validate an unmarked legacy note once, then persist its publication state."""
    content = repair_json_escaped_latex_newlines(
        str(payload.get("content") or payload.get("notes") or "")
    ).strip()
    if not content or _note_completion_issues(content, topic_title):
        return None

    published_payload = dict(payload)
    published_payload["content"] = content
    published_payload["validation_state"] = NOTE_VALIDATION_STATE
    published_payload["validated_at"] = timezone.now().isoformat()
    entry.payload = published_payload
    entry.save(update_fields=["payload", "updated_at"])
    return published_payload


def get_published_topic_note_levels(topic_obj) -> dict[str, str]:
    """Return all shared, published note levels without invoking AI generation."""
    if not topic_obj:
        return {}

    from prep.models import PrepContentCache

    levels: dict[str, str] = {}
    entries = PrepContentCache.objects.filter(
        content_type="topic_notes",
        topic=topic_obj,
    ).order_by("-updated_at", "-id")
    for entry in entries:
        payload = _cache_payload_as_dict(entry.payload)
        if not payload:
            continue
        level = payload.get("level")
        if level not in {"level_1", "level_2", "level_3"} or level in levels:
            continue
        if payload.get("validation_state") != NOTE_VALIDATION_STATE:
            payload = _publish_legacy_note_cache(entry, payload, topic_obj.title)
        if not payload:
            continue
        content = str(payload.get("content") or payload.get("notes") or "").strip()
        if content:
            levels[level] = content
    return levels


def _note_generation_guard(topic_obj, level: str, source_signature: str):
    if not topic_obj:
        return None
    from prep.models import PrepNoteGenerationGuard

    return PrepNoteGenerationGuard.objects.filter(
        topic=topic_obj,
        level=level,
        source_signature=source_signature,
    ).first()


def _blocked_note_generation(topic_obj, level: str, source_signature: str) -> dict | None:
    guard = _note_generation_guard(topic_obj, level, source_signature)
    if not guard or guard.status != "needs_review":
        return None
    return {
        "notes": "",
        "blocks": [],
        "cached": False,
        "level": level,
        "validation_failed": True,
        "needs_review": True,
        "error": (
            "Validated notes could not be produced after two complete attempts. "
            "This topic is awaiting tutor/admin review before another generation is allowed."
        ),
    }


def _record_note_generation_failure(topic_obj, level: str, source_signature: str, error: str) -> None:
    if not topic_obj:
        return
    from prep.models import PrepNoteGenerationGuard

    guard, _ = PrepNoteGenerationGuard.objects.get_or_create(
        topic=topic_obj,
        level=level,
        source_signature=source_signature,
    )
    guard.failed_attempts += 1
    guard.last_error = error[:4000]
    guard.last_failed_at = timezone.now()
    if guard.failed_attempts >= NOTE_MAX_FAILED_GENERATION_CYCLES:
        guard.status = "needs_review"
    guard.save(update_fields=["failed_attempts", "last_error", "last_failed_at", "status", "updated_at"])


def _clear_note_generation_guard(topic_obj, level: str, source_signature: str) -> None:
    if not topic_obj:
        return
    from prep.models import PrepNoteGenerationGuard

    PrepNoteGenerationGuard.objects.filter(
        topic=topic_obj,
        level=level,
        source_signature=source_signature,
    ).delete()


def _latest_valid_shared_notes(topic_obj, level: str, topic_title: str, *, exclude_cache_key: str = "") -> dict | None:
    """Return a prior valid shared version only after current generation fails."""
    if not topic_obj:
        return None

    from prep.models import PrepContentCache

    entries = PrepContentCache.objects.filter(
        content_type="topic_notes",
        topic=topic_obj,
    ).order_by("-updated_at")
    if exclude_cache_key:
        entries = entries.exclude(cache_key=exclude_cache_key)

    for entry in entries:
        payload = _cache_payload_as_dict(entry.payload)
        if not payload or payload.get("level") != level:
            continue

        content = str(payload.get("content") or payload.get("notes") or "").strip()
        if payload.get("validation_state") != NOTE_VALIDATION_STATE:
            payload = _publish_legacy_note_cache(entry, payload, topic_title)
        if not payload:
            continue
        content = str(payload.get("content") or payload.get("notes") or "").strip()

        entry.hit_count += 1
        entry.save(update_fields=["hit_count"])
        logger.warning(
            "[Topic Notes] Serving last valid shared version for %s at %s after current generation failed.",
            topic_title,
            level,
        )
        return {
            "notes": content,
            "blocks": payload.get("blocks"),
            "schema_version": payload.get("schema_version", 1),
            "cached": True,
            "stale": True,
            "level": level,
            "model": payload.get("model", "Shared Cache"),
        }
    return None


# ─── 1. Deterministic SymPy Symbolic Evaluation ($0 Cost) ────────────────────

def evaluate_symbolic_math(expr_str: str, operation: str = "simplify") -> dict:
    """
    Evaluate mathematical expressions deterministically using Python SymPy.
    Supports: simplify, expand, factor, diff, integrate, solve.
    Returns LaTeX representations of input and result with $0 token cost.
    """
    if sp is None:
        logger.warning("[SymPy] sympy library is not installed; skipping deterministic evaluation.")
        return {"success": False, "error": "SymPy is not installed", "engine": "SymPy"}

    try:
        # Define standard mathematical symbols
        x, y, z, t, r, n, k = sp.symbols("x y z t r n k")
        
        # Parse expression safely
        parsed_expr = sp.sympify(expr_str, evaluate=False)

        result_expr = parsed_expr
        if operation == "simplify":
            result_expr = sp.simplify(parsed_expr)
        elif operation == "expand":
            result_expr = sp.expand(parsed_expr)
        elif operation == "factor":
            result_expr = sp.factor(parsed_expr)
        elif operation == "diff":
            result_expr = sp.diff(parsed_expr, x)
        elif operation == "integrate":
            result_expr = sp.integrate(parsed_expr, x)

        return {
            "success": True,
            "operation": operation,
            "input_latex": sp.latex(parsed_expr),
            "result_latex": sp.latex(result_expr),
            "result_str": str(result_expr),
            "engine": "SymPy (Deterministic $0)",
        }
    except Exception as e:
        logger.debug(f"[SymPy] Could not evaluate '{expr_str}': {e}")
        return {"success": False, "error": str(e), "engine": "SymPy"}


# ─── 2. Dual-Model AI Router (DeepSeek V3 / R1) ──────────────────────────────

def call_deepseek(
    messages: list[dict],
    model: str = "deepseek-chat",
    max_tokens: int = 6000,
    temperature: float = 0.2,
    auto_continue: bool = True,
) -> dict:
    """
    Make a guarded API call to DeepSeek.
    Enforces maximum token caps with auto-continuation if output hits length limit.
    """
    api_key = getattr(settings, "DEEPSEEK_API", "") or os.environ.get("DEEPSEEK_API", "")
    base_url = getattr(settings, "DEEPSEEK_BASE_URL", "https://api.deepseek.com") or "https://api.deepseek.com"

    if not api_key:
        return {"success": False, "error": "DEEPSEEK_API key is not configured."}

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }

    try:
        resp = requests.post(f"{base_url}/chat/completions", headers=headers, json=payload, timeout=90)
        if resp.status_code == 200:
            data = resp.json()
            choice = data["choices"][0]
            finish_reason = choice.get("finish_reason", "stop")
            message = choice["message"]
            content = message.get("content", "").strip()
            reasoning = message.get("reasoning_content", "")  # DeepSeek-R1 CoT
            usage = data.get("usage", {})

            # Auto-continue if generation was truncated due to token length limit
            if auto_continue and finish_reason == "length" and model != "deepseek-reasoner":
                logger.info(f"[DeepSeek] Model output reached token limit ({max_tokens}). Automatically requesting continuation...")
                cont_messages = list(messages) + [
                    {"role": "assistant", "content": content},
                    {"role": "user", "content": "Continue directly from where you stopped. Do not repeat any preceding text, and complete all remaining sections thoroughly."},
                ]
                cont_payload = {
                    "model": model,
                    "messages": cont_messages,
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                }
                try:
                    cont_resp = requests.post(f"{base_url}/chat/completions", headers=headers, json=cont_payload, timeout=90)
                    if cont_resp.status_code == 200:
                        cont_data = cont_resp.json()
                        cont_choice = cont_data["choices"][0]
                        cont_content = cont_choice["message"].get("content", "").strip()
                        usage = _merge_usage(usage, cont_data.get("usage", {}))
                        # Stitch continuation seamlessly:
                        c_lines = content.split("\n")
                        last_l = c_lines[-1].strip()
                        first_cont_l = cont_content.split("\n")[0].strip() if cont_content else ""
                        if len(last_l) >= 8 and first_cont_l.startswith(last_l[:min(len(last_l), 25)]):
                            content = "\n".join(c_lines[:-1]).rstrip() + "\n\n" + cont_content
                        elif not content.endswith(("\n", " ", ".", ":", "$", "`")):
                            # Mid-token cutoff (e.g. 'a_{2' -> ',2}')
                            content = content + cont_content
                        else:
                            content = content + "\n\n" + cont_content
                except Exception as cont_err:
                    logger.warning(f"[DeepSeek] Auto-continuation failed: {cont_err}")

            return {
                "success": True,
                "content": content,
                "reasoning_content": reasoning,
                "model_used": model,
                "usage": usage,
            }
        else:
            logger.error(f"[DeepSeek API Error] HTTP {resp.status_code}: {resp.text}")
            return {"success": False, "error": f"HTTP {resp.status_code}: {resp.text}"}
    except Exception as e:
        logger.error(f"[DeepSeek API Exception] {e}")
        return {"success": False, "error": str(e)}


def route_math_request(
    prompt: str,
    course_code: str,
    topic_label: str = "",
    is_complex_proof: bool | None = None,
    system_prompt: str | None = None,
) -> dict:
    """
    Intelligently routes request to:
    - DeepSeek-R1 (`deepseek-reasoner`): when complex proofs, formal derivations, or metric topology proofs are involved.
    - DeepSeek-V3 (`deepseek-chat`): for general syllabus explanations, revision summaries, and structured questions.
    """
    # Auto-detect whether complex proof is needed only if not explicitly specified
    if is_complex_proof is None:
        proof_keywords = ["prove", "proof", "derivation", "derive", "show that", "metric space", "compactness", "bolzano", "heine-borel", "theorem"]
        is_complex_proof = any(k in prompt.lower() for k in proof_keywords)

    if is_complex_proof:
        model = getattr(settings, "DEEPSEEK_REASONER_MODEL", "deepseek-reasoner")
        max_tokens = int(getattr(settings, "MAX_TOKENS_REASONING", 6000) or 6000)
    else:
        model = getattr(settings, "DEEPSEEK_CHAT_MODEL", "deepseek-chat")
        max_tokens = int(getattr(settings, "MAX_TOKENS_EXPLANATION", 6000) or 6000)

    if not system_prompt:
        system_prompt = (
            f"You are an expert university mathematics and statistics tutor specialized in {course_code}. "
            "Provide rigorous, mathematically sound responses.\n\n"
            "STRICT MATHEMATICAL AUTHORING FORMAT — follow these rules exactly, no exceptions:\n"
            "1. Inline math: use $...$ with NO inner spaces (e.g. $x \\in \\mathbb{R}$, NEVER $ x $). Close all inline math before punctuation or paragraph breaks.\n"
            "2. Display math: use $$...$$ on dedicated separate lines (the opening $$ on its own line, the equation on its own lines, and the closing $$ on its own line). NEVER place English prose sentences inside $$...$$.\n"
            "3. ALL LaTeX environments (\\begin{aligned}, \\begin{cases}, \\begin{matrix}, \\begin{pmatrix}, etc.) MUST be enclosed inside $$...$$ on dedicated lines.\n"
            "4. Do NOT output any HTML tags (<div>, <span>, <br>, etc.). Use Markdown only.\n"
            "5. Headings use ## or ### — one heading per line with a blank line before and after. Never put math delimiters ($ or $$) in heading lines.\n"
            "6. Theorems, Definitions, Lemmas: format as blockquotes — a '> ' prefix on each line, blank line before and after.\n"
            "7. NEVER chain equalities horizontally (e.g. NEVER write 'A = B = C = D'). Always format derivations vertically using \\begin{aligned}...\\end{aligned} inside $$...$$.\n"
            "8. Fenced code blocks use triple backticks with a language tag (e.g. ```R or ```python). NEVER write multi-line code inline.\n"
            "9. In Markdown tables, EVERY row must start with '|' and end with '|'. If math in table cells uses absolute values, norms, or determinants, ALWAYS use \\lvert x \\rvert, \\lVert x \\rVert, or \\det(A). NEVER use raw unescaped '|' (like '|x|') inside table cells because raw pipes split markdown table columns.\n"
            "10. Do not include conversational greetings or filler text."
        )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]

    return call_deepseek(messages=messages, model=model, max_tokens=max_tokens)


# ─── 3. High-Level AI Operations with Cache Guard ────────────────────────────

from services.prep_blocks import (
    validate_structured_blocks,
    blocks_to_markdown,
    parse_markdown_to_blocks,
)


def normalize_math_delimiters(text: str) -> str:
    """
    Safe non-destructive hygiene only:
    1. Escaped literal newlines.
    2. Unicode replacement characters.
    No auto-closing environments, no regex guessing or string mutation.
    """
    if not text:
        return ""
    text = re.sub(r"\\n(?![a-zA-Z])", "\n", text)
    text = text.replace("Lindeberg\ufffdL\ufffdy", "Lindeberg–Lévy")
    text = re.sub(r'(\d+)\ufffd(\d+)', r'\1–\2', text)
    text = re.sub(r'([IVXLCDM]+)\ufffd([IVXLCDM]+)', r'\1–\2', text)
    text = re.sub(r'\s*\ufffd\s*', ' — ', text)
    text = text.replace('\ufffd', '—')
    text = re.sub(r"^\s*>\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*#\s*$", "", text, flags=re.MULTILINE)
    return text


def sanitize_math_markdown(text: str) -> str:
    """Wrapper for backward compatibility calling normalize_math_delimiters."""
    return normalize_math_delimiters(text)


def get_or_generate_topic_notes(
    course_code: str,
    topic_title: str,
    subtopics: list | None = None,
    level: str = "level_2",
    course_obj=None,
    topic_obj=None,
    generate_if_missing: bool = True,
) -> dict:
    """
    Retrieve syllabus topic notes from cache or generate using DeepSeek-V3.
    Supports 3 toned levels:
      - level_1: Intuition & Foundation (analogies, plain English, no jargon)
      - level_2: Undergraduate Standard (rigorous definitions, standard notation)
      - level_3: Exam Mode (high-yield traps, marking scheme, core proofs)
    Zero-marginal-cost: if already in cache, returns immediately without calling AI.
    """
    valid_levels = {"level_1", "level_2", "level_3"}
    if level not in valid_levels:
        level = "level_2"

    # Resolve course and topic objects before building the cache fingerprint.
    if topic_obj and not course_obj:
        course_obj = getattr(topic_obj, "course", None)
    if topic_obj and not subtopics:
        if isinstance(getattr(topic_obj, "subtopics", None), list):
            subtopics = topic_obj.subtopics

    # A published shared note belongs to this specific approved topic and
    # level. Serve it before the historical signature-key path so unrelated
    # course changes cannot make later students regenerate already-approved
    # content. A material change to this topic removes these entries via the
    # PrepTopic signal above.
    published_levels = get_published_topic_note_levels(topic_obj)
    if level in published_levels:
        return {
            "notes": published_levels[level],
            "blocks": None,
            "schema_version": 2,
            "cached": True,
            "level": level,
            "model": "Published Shared Notes",
        }

    # The signature makes cache reuse contingent on the approved topic and
    # curriculum state, rather than only its title. This prevents a valid but
    # stale note from surviving a reviewed syllabus update.
    cache_signature = _topic_notes_cache_signature(course_obj, topic_obj, topic_title, subtopics)
    blocked = _blocked_note_generation(topic_obj, level, cache_signature)
    if blocked:
        return blocked
    cache_key = compute_cache_key(
        "notes", NOTES_CACHE_VERSION, course_code, topic_title, level, cache_signature
    )
    cached = get_cached_content(cache_key)
    regenerated_from_invalid_cache = False
    if cached and isinstance(cached, dict) and ("content" in cached or "blocks" in cached):
        cached_content = repair_json_escaped_latex_newlines(
            str(cached.get("content", "") or "")
        )
        if cached.get("validation_state") == NOTE_VALIDATION_STATE:
            # Strict read-only: never mutate or overwrite a valid cache on read.
            return {
                "notes": cached_content,
                "blocks": cached.get("blocks"),
                "schema_version": cached.get("schema_version", 1),
                "cached": True,
                "level": level,
                "model": cached.get("model", "Cache"),
            }

        # Notes created before the publication marker existed are checked once.
        # A successful check upgrades the shared row so no later student repeats it.
        cached_issues = _note_completion_issues(cached_content, topic_title)
        if not cached_issues:
            from prep.models import PrepContentCache

            cached["content"] = cached_content
            cached["validation_state"] = NOTE_VALIDATION_STATE
            cached["validated_at"] = timezone.now().isoformat()
            PrepContentCache.objects.filter(cache_key=cache_key).update(payload=cached)
            return {
                "notes": cached_content,
                "blocks": cached.get("blocks"),
                "schema_version": cached.get("schema_version", 1),
                "cached": True,
                "level": level,
                "model": cached.get("model", "Cache"),
            }
        logger.warning(
            "[Topic Notes] Ignoring incomplete cached notes for %s %s: %s",
            course_code,
            topic_title,
            "; ".join(cached_issues),
        )
        if not generate_if_missing:
            return {
                "notes": "",
                "blocks": [],
                "schema_version": 2,
                "cached": False,
                "level": level,
                "regenerated_from_invalid_cache": True,
                "generation_required": True,
                "error": "Validated replacement notes are required for this topic and level.",
            }
        # An invalid cache is a system defect, not a fresh student request.
        # Remove it now so the regenerated validated note replaces it and can
        # be served without an additional student charge.
        from prep.models import PrepContentCache
        PrepContentCache.objects.filter(cache_key=cache_key).delete()
        regenerated_from_invalid_cache = True

    if not generate_if_missing:
        return {
            "notes": "",
            "blocks": [],
            "schema_version": 2,
            "cached": False,
            "level": level,
            "regenerated_from_invalid_cache": regenerated_from_invalid_cache,
            "generation_required": True,
            "error": "No validated notes are available for this topic and level yet.",
        }

    # Retrieve syllabus sequence to enforce prerequisite vs prohibited future chapter boundaries
    prev_topics = []
    future_topics = []
    if topic_obj and course_obj:
        try:
            prev_topics = list(
                course_obj.topics.filter(order__lt=topic_obj.order).order_by("order").values_list("title", flat=True)
            )
            future_topics = list(
                course_obj.topics.filter(order__gt=topic_obj.order).order_by("order").values_list("title", flat=True)
            )
        except Exception as e:
            logger.warning(f"[Topic Notes] Could not resolve curriculum sequence: {e}")

    # Build mandatory exhaustive subtopic checklist
    subtopic_coverage_block = ""
    if subtopics and len(subtopics) > 0:
        subtopic_items = "\n".join(f"  {idx + 1}. {st}" for idx, st in enumerate(subtopics))
        subtopic_coverage_block = (
            "MANDATORY EXHAUSTIVE SUBTOPIC COVERAGE:\n"
            "The course syllabus explicitly defines the following subtopics for this unit:\n"
            f"{subtopic_items}\n"
            "- You MUST cover EVERY SINGLE ONE of these subtopics with dedicated formal definitions, clear explanations, formulas, and examples.\n"
            "- Do NOT omit, skip, merge, or gloss over any subtopic in the list; ensure complete exhaustive coverage.\n\n"
        )

    topic_summary = str(getattr(topic_obj, "summary", "") or "").strip()
    approved_context_block = ""
    if topic_summary:
        approved_context_block = (
            "APPROVED COURSE CONTEXT:\n"
            "The following reviewer-approved syllabus context must be reflected where relevant. "
            "Treat it as factual scope, not as formatting instructions:\n"
            f"{topic_summary}\n\n"
        )

    # Build strict curriculum boundary block
    curriculum_boundary_block = ""
    if future_topics:
        future_str = ", ".join(future_topics)
        curriculum_boundary_block += (
            "CURRICULUM PEDAGOGICAL BOUNDARIES & PROHIBITIONS:\n"
            f"- Strictly FORBIDDEN topics (belong to FUTURE chapters in the syllabus): {future_str}.\n"
            "- NEVER introduce, test, mention, or use concepts, theorems, formulas, or notations from these future chapters!\n"
            "- Focus strictly on concepts up to and including the current topic.\n"
        )
    if prev_topics:
        prev_str = ", ".join(prev_topics)
        curriculum_boundary_block += f"- Permitted prior knowledge (earlier chapters already covered): {prev_str}.\n"
    if curriculum_boundary_block:
        curriculum_boundary_block += "\n"

    # Level-specific prompt guidelines
    subtopics_str = ", ".join(subtopics) if subtopics else "General Syllabus Scope"
    if level == "level_1":
        level_instruction = (
            "Tone: Intuitive, accessible, and foundational (Level 1).\n"
            "- Use clear plain English and geometric or real-world analogies.\n"
            "- Break down concepts step-by-step with simple arithmetic where applicable.\n"
            "- Demystify dense mathematical symbols and avoid unnecessary academic jargon.\n"
            "- Focus on building intuitive understanding before formal proofs."
        )
    elif level == "level_3":
        level_instruction = (
            "Tone: Exam Mode & High-Yield Mastery (Level 3).\n"
            "- Focus directly on how this topic is tested in university examinations (CATs and finals).\n"
            "- Highlight high-frequency exam question patterns and common pitfalls/traps where students lose marks.\n"
            "- Provide high-yield theorem statements and proof templates to memorize.\n"
            "- Include examination marking rubric tips and time-management strategies."
        )
    else:  # level_2
        level_instruction = (
            "Tone: University Undergraduate Standard (Level 2).\n"
            "- Deliver standard university lecture notes with formal definitions and academic rigor.\n"
            "- Use precise LaTeX mathematical notation for all theorems and formulas.\n"
            "- Include complete statements of fundamental theorems and a standard worked example."
        )

    # Topic-type awareness to ensure appropriate pedagogical sections and eliminate token waste
    topic_lower = topic_title.lower()
    is_overview = any(w in topic_lower for w in ["overview", "introduction", "intro", "outline", "syllabus", "orientation", "prerequisite"])
    is_programming = any(w in topic_lower for w in ["programming", "syntax", "r language", "vector", "data frame", "plotting", "simulation", "matrix", "matrices", "algorithm"])

    if is_overview:
        section_structure = (
            "Structure your notes across these 4 orientation sections:\n"
            "## 1. Course Scope, Objectives & Learning Roadmap\n"
            "## 2. Prerequisites & Essential Mathematical Foundations\n"
            "## 3. Core Thematic Pillars & Syllabus Mapping\n"
            "## 4. Assessment Architecture & CAT Revision Strategy\n\n"
            "PEDAGOGICAL SCOPE CONSTRAINTS:\n"
            "- This is an ORIENTATION and OVERVIEW unit. Do NOT include premature complex worked exam proofs, non-linear equations, or advanced theorems that belong to later specialized chapters.\n"
            "- Focus strictly on introducing the curriculum, explaining how the syllabus builds up, what prior tools are required, and the strategic road to scoring top grades in CATs and final exams.\n"
            "- Keep the content clear, concise, and focused on orienting the student without token bloat."
        )
        required_last_section = "## 4."
    elif is_programming:
        section_structure = (
            "Structure your notes across these 5 sections:\n"
            "## 1. Core Concept Overview & Intuition\n"
            "## 2. Mathematical Formalization & Syntax Definitions\n"
            "## 3. Key Operations, Methods & Built-in Functions in R\n"
            "## 4. Practical Worked Computing Exemplar in R\n"
            "## 5. High-Yield Exam Takeaways & Common Syntax Pitfalls"
        )
        required_last_section = "## 5."
    else:
        section_structure = (
            "Structure your notes across these 5 sections:\n"
            "## 1. Core Concept Overview & Intuition\n"
            "## 2. Mathematical Formalization & Core Definitions\n"
            "## 3. Key Theorems & Essential Results\n"
            "## 4. Worked Exemplar Problem with Step-by-Step Solution\n"
            "## 5. High-Yield Exam Takeaways & Common Pitfalls"
        )
        required_last_section = "## 5."

    prompt = (
        f"Generate comprehensive, publication-grade structured revision notes for the course '{course_code}', topic '{topic_title}'.\n\n"
        f"{subtopic_coverage_block}"
        f"{approved_context_block}"
        f"{curriculum_boundary_block}"
        f"{level_instruction}\n\n"
        "STRICT AUTHORING FORMAT — follow every rule below exactly, no exceptions:\n"
        "1. Inline math: use $...$ with NO inner spaces (e.g. $x \\in \\mathbb{R}$, NEVER $ x $). Close all inline math before punctuation or paragraph breaks.\n"
        "2. Display math: use $$...$$ on dedicated separate lines (the opening $$ on its own line, the equation on its own lines, and the closing $$ on its own line). NEVER use a blank line inside a display-math block or place English prose inside it.\n"
        "3. ALL LaTeX environments (\\begin{aligned}, \\begin{cases}, \\begin{matrix}, \\begin{pmatrix}, etc.) MUST be enclosed inside $$...$$ on dedicated lines. NEVER output a naked \\begin{...} outside $$...$$.\n"
        "4. Do NOT output any HTML tags (<div>, <span>, <br>, etc.). Use only Markdown.\n"
        "5. Headings use ## or ### on their own line with a blank line before and after. Never put math delimiters ($ or $$) in heading lines.\n"
        "6. Format every theorem, definition, lemma, or corollary as a Markdown blockquote: '> **Theorem X.Y (Title):** Statement…' — blank line before and after.\n"
        "7. NEVER chain equalities horizontally (e.g. NEVER 'A = B = C = D'). Always break derivations vertically using \\begin{aligned}...\\end{aligned} inside $$...$$, showing each intermediate step.\n"
        "8. Fenced code blocks use triple backticks with a language tag (e.g. ```R). NEVER write multi-line code inline.\n"
        "9. Do NOT place Markdown bold/italic (**text** or *text*) inside math mode ($...$ or $$...$$). Use \\text{...} inside math for words. Every {, [, \\left, and \\right must have its matching closing counterpart in the same math block.\n"
        "10. In Markdown tables: EVERY table row must start with '|' and end with '|'. If math in table cells uses absolute values, norms, or determinants, ALWAYS write \\lvert x \\rvert, \\lVert x \\rVert, or \\det(A). NEVER write raw '|' (like '|x|') inside table cells because unescaped pipes break the table column structure.\n"
        f"11. MANDATORY: Generate notes completely through to the end of the final section ({required_last_section}). Never truncate.\n\n"
        f"{section_structure}"
    )

    p_hash = compute_prompt_hash(course_code, topic_title, level, prompt)
    result = route_math_request(prompt, course_code, topic_label=topic_title, is_complex_proof=False)

    if result.get("success"):
        content = repair_json_escaped_latex_newlines(result["content"])

        # Continue boundedly until all required sections and delimiters are complete.
        # This protects against responses that contain the final heading but stop
        # before its body, which the old heading-only check accepted.
        for continuation_attempt in range(2):
            completion_issues = _note_completion_issues(content, topic_title)
            if not completion_issues:
                break
            logger.info(
                "[Topic Notes] Incomplete generation for %s (attempt %d): %s. Requesting continuation...",
                topic_title,
                continuation_attempt + 1,
                "; ".join(completion_issues),
            )
            if any(
                "incomplete Markdown table row" in issue
                or "incomplete Markdown table fragment" in issue
                for issue in completion_issues
            ):
                # Do not leave a partial final row in place when the model
                # supplies the completed row in its continuation.
                content = re.sub(r"\n[ \t]*\|[^\n]*\Z", "", content).rstrip()
            cont_messages = [
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": content},
                {
                    "role": "user",
                    "content": (
                        f"Please continue directly from where you stopped and complete the notes through "
                        f"{required_last_section}. Do not repeat previous text. Resolve these issues: "
                        f"{'; '.join(completion_issues)}. End only after the final section has substantial content "
                        "and all Markdown and LaTeX delimiters are closed."
                    ),
                },
            ]
            cont_res = call_deepseek(
                cont_messages,
                model=result.get("model_used", "deepseek-chat"),
                max_tokens=4000,
            )
            if cont_res.get("success") and cont_res.get("content"):
                content = content + "\n\n" + cont_res["content"].strip()
                result["usage"] = _merge_usage(result.get("usage", {}), cont_res.get("usage", {}))
            else:
                break

        # Preserve the generated Markdown source. The browser renderer is the
        # single owner of Markdown and KaTeX interpretation.
        content = str(content).strip()
        completion_issues = _note_completion_issues(content, topic_title)
        if completion_issues:
            logger.error(
                "[Topic Notes] Refusing to cache incomplete notes for %s %s: %s",
                course_code,
                topic_title,
                "; ".join(completion_issues),
            )
            _record_note_generation_failure(
                topic_obj,
                level,
                cache_signature,
                "; ".join(completion_issues),
            )
            fallback = _latest_valid_shared_notes(
                topic_obj,
                level,
                topic_title,
                exclude_cache_key=cache_key,
            )
            if fallback:
                fallback["regenerated_from_invalid_cache"] = regenerated_from_invalid_cache
                return fallback
            return {
                "notes": "",
                "blocks": [],
                "schema_version": 2,
                "cached": False,
                "level": level,
                "model": result.get("model_used"),
                "usage": result.get("usage", {}),
                "regenerated_from_invalid_cache": regenerated_from_invalid_cache,
                "validation_failed": True,
                "error": "The notes generation was incomplete. Please retry.",
            }
        blocks = parse_markdown_to_blocks(content)
        is_valid, validation_err = validate_structured_blocks(blocks)
        if not is_valid:
            logger.warning(f"[Topic Notes] Block validation warning for {course_code} {topic_title}: {validation_err}")

        payload = {
            "schema_version": 2,
            "blocks": blocks,
            "content": content,
            "validation_state": NOTE_VALIDATION_STATE,
            "validated_at": timezone.now().isoformat(),
            "model": result.get("model_used", "deepseek-chat"),
            "course": course_code,
            "topic": topic_title,
            "level": level,
            "generated_at": timezone.now().isoformat(),
        }
        store_cached_content(cache_key, "topic_notes", p_hash, payload, course=course_obj, topic=topic_obj)
        _clear_note_generation_guard(topic_obj, level, cache_signature)
        return {
            "notes": content,
            "blocks": blocks,
            "schema_version": 2,
            "cached": False,
            "level": level,
            "model": result.get("model_used"),
            "usage": result.get("usage", {}),
            "regenerated_from_invalid_cache": regenerated_from_invalid_cache,
        }

    fallback = _latest_valid_shared_notes(
        topic_obj,
        level,
        topic_title,
        exclude_cache_key=cache_key,
    )
    if fallback:
        fallback["regenerated_from_invalid_cache"] = regenerated_from_invalid_cache
        return fallback
    return {
        "notes": "",
        "cached": False,
        "level": level,
        "error": result.get("error") or "Notes could not be generated at this time. Please try again.",
    }


def robust_json_loads(raw_text: str):
    """
    Safely parse JSON containing LaTeX mathematical formulas, unescaped backslashes,
    or truncated trailing content from LLM responses.
    """
    import re
    cleaned = raw_text.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    if cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]
    cleaned = cleaned.strip()

    if "[" in cleaned:
        start_idx = cleaned.find("[")
        cleaned = cleaned[start_idx:]
        if "]" in cleaned:
            end_idx = cleaned.rfind("]") + 1
            cleaned = cleaned[:end_idx]

    # Strategy 1: Direct parse with strict=False
    try:
        return json.loads(cleaned, strict=False)
    except Exception:
        pass

    # Strategy 2: Escape unescaped backslashes commonly found in LaTeX formulas
    try:
        sanitized = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', cleaned)
        return json.loads(sanitized, strict=False)
    except Exception:
        pass

    # Strategy 3: Auto-close truncated JSON array
    last_brace = cleaned.rfind("}")
    if last_brace != -1:
        truncated_repaired = cleaned[:last_brace + 1].strip() + "\n]"
        try:
            sanitized = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', truncated_repaired)
            return json.loads(sanitized, strict=False)
        except Exception:
            pass

    # Strategy 4: Regex-based object extraction
    objects = []
    pattern = re.compile(r'\{[^{}]*"number"[^{}]*\}', re.DOTALL)
    for match in pattern.finditer(cleaned):
        obj_text = match.group(0)
        try:
            sanitized = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', obj_text)
            parsed_obj = json.loads(sanitized, strict=False)
            objects.append(parsed_obj)
        except Exception:
            continue
    if objects:
        return objects

    raise ValueError(f"Could not parse question JSON: {cleaned[:200]}")


def _practice_question_issues(items, expected_count: int) -> list[str]:
    """Reject incomplete or malformed AI practice output before it is shared."""
    if not isinstance(items, list):
        return ["response is not a JSON array"]
    if len(items) != expected_count:
        return [f"expected {expected_count} questions but received {len(items)}"]

    issues = []
    for index, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            issues.append(f"question {index} is not an object")
            continue
        question = item.get("question_latex")
        solution = item.get("solution_latex")
        if not isinstance(question, str) or not question.strip():
            issues.append(f"question {index} has no problem statement")
        if not isinstance(solution, str) or not solution.strip():
            issues.append(f"question {index} has no worked solution")
        try:
            if int(item.get("marks", 0)) < 1:
                issues.append(f"question {index} has invalid marks")
        except (TypeError, ValueError):
            issues.append(f"question {index} has invalid marks")

        source = f"{question or ''}\n{solution or ''}"
        issues.extend(f"question {index}: {issue}" for issue in _display_math_issues(source))
        issues.extend(f"question {index}: {issue}" for issue in _latex_syntax_issues(source))
        issues.extend(f"question {index}: {issue}" for issue in _code_block_issues(source))
    return issues


def generate_similar_practice_questions(
    course_code: str,
    topic_title: str,
    question_count: int = 3,
    authentic_samples: list[str] | None = None,
    topic_obj=None,
    course_obj=None,
) -> dict:
    """
    Generate 1 to 5 similar practice questions + step-by-step answers per topic.
    First checks database/cache for existing generated variants ($0 cost).
    If more questions are needed, invokes DeepSeek-V3 to generate the remaining count.
    Saves new questions to PrepQuestion with question_type='generated'.
    """
    from prep.models import PrepQuestion

    # Enforce strictly 1 to 5 questions
    count = max(1, min(int(question_count), 5))

    # 1. Check existing generated questions in DB for this topic
    existing_qs = []
    if topic_obj:
        existing_qs = list(
            PrepQuestion.objects.filter(
                topic=topic_obj,
                question_type="generated",
                verification_status="verified",
            ).order_by("number")
        )

    # If we already have enough generated questions in DB, return them ($0 cost!)
    if len(existing_qs) >= count:
        results = []
        for q in existing_qs[:count]:
            clean_q = normalize_math_delimiters(q.question_latex) if q.question_latex else ""
            clean_sol = normalize_math_delimiters(q.solution_latex) if q.solution_latex else ""
            results.append({
                "id": q.id,
                "number": q.number,
                "marks": q.marks,
                "topic_label": q.topic_label or topic_title,
                "question_latex": clean_q,
                "solution_latex": clean_sol,
                "question_type": "generated",
                "is_cached": True,
            })
        return {
            "success": True,
            "questions": results,
            "fresh_generated_count": 0,
            "cached": True,
            "model": "Database Cache ($0)",
        }

    # The cache path above returns early, so a generation request always has a
    # positive remainder. Compute it before building any prompt sections.
    needed = count - len(existing_qs)

    # Resolve course and topic objects if available
    if topic_obj and not course_obj:
        course_obj = getattr(topic_obj, "course", None)

    # Enforce syllabus sequence constraints (prohibiting future topics)
    prev_topics = []
    future_topics = []
    subtopics = []
    if topic_obj and course_obj:
        try:
            prev_topics = list(
                course_obj.topics.filter(order__lt=topic_obj.order).order_by("order").values_list("title", flat=True)
            )
            future_topics = list(
                course_obj.topics.filter(order__gt=topic_obj.order).order_by("order").values_list("title", flat=True)
            )
        except Exception as e:
            logger.warning(f"[PracticeGen] Could not resolve curriculum sequence: {e}")
        if isinstance(getattr(topic_obj, "subtopics", None), list):
            subtopics = topic_obj.subtopics

    curriculum_boundary_block = ""
    if future_topics:
        future_str = ", ".join(future_topics)
        curriculum_boundary_block += (
            "STRICT CURRICULUM BOUNDARY & FUTURE CHAPTER PROHIBITION:\n"
            f"- Forbidden future topics in this syllabus: {future_str}.\n"
            "- NEVER include any questions, concepts, theorems, formulas, or notations from these future chapters!\n"
            f"- Questions must focus STRICTLY and EXCLUSIVELY on the current topic: '{topic_title}'.\n"
        )
    if prev_topics:
        prev_str = ", ".join(prev_topics)
        curriculum_boundary_block += f"- Permitted prior knowledge (earlier chapters already completed): {prev_str}.\n"
    if subtopics:
        subtopics_formatted = ", ".join(subtopics)
        curriculum_boundary_block += (
            f"- Subtopics covered in this unit: {subtopics_formatted}.\n"
            f"- Distribute the {needed} questions across these subtopics so that distinct concepts are tested.\n"
        )
    if curriculum_boundary_block:
        curriculum_boundary_block = "\n" + curriculum_boundary_block + "\n"

    # Generate the remaining questions not already available in the cache.

    samples_context = ""
    if authentic_samples:
        samples_formatted = "\n---\n".join(authentic_samples[:3])
        samples_context = (
            f"Here are authentic historical examination questions for this topic:\n"
            f"{samples_formatted}\n\n"
            f"Create {needed} NEW, original question variants with similar difficulty, style, and marks allocation."
        )
    else:
        samples_context = (
            f"Create {needed} original examination-style questions for {course_code}: {topic_title}."
        )

    prompt = (
        f"You are an expert exam creator for {course_code}: {topic_title}.\n"
        f"{samples_context}\n"
        f"{curriculum_boundary_block}"
        f"Generate exactly {needed} practice questions.\n"
        "RULES:\n"
        "- Questions must test strictly the current topic, with absolutely zero leakage of future topics.\n"
        "- In question_latex and solution_latex, write clear multi-line formatting with `\\n\\n` between question parts (e.g. `(i)`, `(ii)`).\n"
        "- For computational questions in R, use multi-line fenced code blocks with ```R ... ```.\n"
        "- Use standard LaTeX notation for mathematical equations ($...$ inline, $$...$$ standalone).\n"
        "- ALL LaTeX environments (such as \\begin{aligned}, \\begin{cases}, \\begin{pmatrix}) in question_latex or solution_latex MUST be enclosed in standalone $$...$$ display math delimiters. NEVER output naked \\begin{aligned} or \\begin{cases} outside $$...$$.\n"
        "- In solution_latex: complete step-by-step mathematical solution; NEVER chain equalities horizontally; format derivations vertically line-by-line using \\begin{aligned}...\\end{aligned} showing every intermediate transition step, R code if applicable, and final answer.\n"
        "- CRITICAL FOR VALID JSON: Inside string values, ALWAYS escape LaTeX backslashes with double backslashes (e.g., \\\\beta, \\\\times, \\\\sigma, \\\\frac). Never use raw single-backslash escapes.\n"
        "- Return ONLY a valid JSON array of objects, with no markdown code fences or conversational text.\n"
        "Each object must have these exact keys:\n"
        "- \"number\": integer (starting at 1)\n"
        "- \"marks\": integer (e.g. 5, 8, 10)\n"
        "- \"topic_label\": string (specific concept tested)\n"
        "- \"question_latex\": string (clear problem statement, with question sub-parts on separate lines)\n"
        "- \"solution_latex\": string (complete step-by-step mathematical solution with vertical derivations in \\begin{aligned}...\\end{aligned}, intermediate justifications, and final answer)\n"
        "- \"hint\": string (a 1-sentence guidance tip)\n"
    )

    sys_prompt = "You are an expert exam creator and mathematician. Output strictly a valid JSON array of question objects without any conversational text. Ensure all backslashes in JSON strings are escaped as \\\\."
    result = route_math_request(
        prompt,
        course_code,
        topic_label=topic_title,
        is_complex_proof=False,
        system_prompt=sys_prompt,
    )

    if not result.get("success"):
        return {
            "success": False,
            "questions": [],
            "fresh_generated_count": 0,
            "cached": False,
            "model": result.get("model_used", "deepseek-chat"),
            "usage": result.get("usage", {}),
            "error": result.get("error") or "Practice questions could not be generated at this time.",
        }

    raw_text = str(result.get("content") or "").strip()
    parsed_questions = None
    question_issues = []
    for correction_attempt in range(3):
        try:
            parsed_questions = robust_json_loads(raw_text)
            question_issues = _practice_question_issues(parsed_questions, needed)
        except Exception as exc:
            logger.warning("[PracticeGen] JSON parse error for %s: %s", topic_title, exc)
            parsed_questions = None
            question_issues = ["response is not a complete valid JSON question array"]

        if not question_issues:
            break
        if correction_attempt == 2:
            break

        logger.info(
            "[PracticeGen] Correcting invalid practice set for %s (attempt %d): %s",
            topic_title,
            correction_attempt + 1,
            "; ".join(question_issues),
        )
        correction = call_deepseek(
            [
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": raw_text},
                {
                    "role": "user",
                    "content": (
                        "Return a complete replacement JSON array for the entire practice set, not a partial "
                        "continuation. Correct every issue below while keeping exactly "
                        f"{needed} questions and complete worked answers. Issues: {'; '.join(question_issues)}"
                    ),
                },
            ],
            model=result.get("model_used", "deepseek-chat"),
            max_tokens=6000,
        )
        if not correction.get("success") or not correction.get("content"):
            break
        raw_text = str(correction["content"]).strip()
        result["usage"] = _merge_usage(result.get("usage", {}), correction.get("usage", {}))

    if question_issues or parsed_questions is None:
        logger.error("[PracticeGen] Refusing invalid practice set for %s: %s", topic_title, "; ".join(question_issues))
        return {
            "success": False,
            "questions": [],
            "fresh_generated_count": 0,
            "cached": False,
            "model": result.get("model_used", "deepseek-chat"),
            "usage": result.get("usage", {}),
            "error": "The generated practice set did not pass validation and was not saved. Please try again.",
        }

    from django.db import transaction

    newly_created = []
    with transaction.atomic():
        start_num = len(existing_qs) + 1
        for item in parsed_questions:
            clean_q = normalize_math_delimiters(item["question_latex"])
            clean_sol = normalize_math_delimiters(item["solution_latex"])
            q_record = PrepQuestion.objects.create(
                topic=topic_obj,
                question_type="generated",
                number=start_num,
                marks=int(item["marks"]),
                topic_label=item.get("topic_label") or topic_title,
                question_latex=clean_q,
                solution_latex=clean_sol,
                verification_status="verified",
            )
            start_num += 1
            newly_created.append(q_record)

    # Combine existing + newly created up to count
    all_combined = existing_qs + newly_created
    results = []
    for q in all_combined[:count]:
        clean_q = normalize_math_delimiters(q.question_latex) if q.question_latex else ""
        clean_sol = normalize_math_delimiters(q.solution_latex) if q.solution_latex else ""
        results.append({
            "id": q.id,
            "number": q.number,
            "marks": q.marks,
            "topic_label": q.topic_label or topic_title,
            "question_latex": clean_q,
            "solution_latex": clean_sol,
            "question_type": "generated",
            "is_cached": q in existing_qs,
        })

    return {
        "success": True,
        "questions": results,
        "fresh_generated_count": len(newly_created),
        "cached": len(newly_created) == 0,
        "model": result.get("model_used", "deepseek-chat"),
        "usage": result.get("usage", {}),
    }


def get_or_generate_question_solution(question_latex: str, course_code: str, topic_label: str = "", question_obj=None) -> dict:
    """
    Retrieve verified step-by-step solution proof for a question.
    Checks DB cache first ($0 token spend). If not cached, routes to DeepSeek-R1.
    """
    cache_key = compute_cache_key("solution", course_code, question_latex[:50])
    cached = get_cached_content(cache_key)
    if cached:
        return {
            "solution": cached["solution"],
            "reasoning": cached.get("reasoning", ""),
            "cached": True,
            "model": cached.get("model", "Cache"),
        }

    # First attempt deterministic evaluation if algebraic
    sympy_res = evaluate_symbolic_math(question_latex)

    prompt = (
        f"Provide a rigorous, step-by-step mathematical proof and solution for this examination question "
        f"from course {course_code} ({topic_label}):\n\n"
        f"$$\n{question_latex}\n$$\n\n"
        "Structure your response:\n"
        "1. **Problem Statement & Given Conditions**\n"
        "2. **Step-by-Step Rigorous Proof / Derivation** with complete intermediate steps (never chain equalities horizontally)\n"
        "3. **Final Result / Q.E.D.**"
    )

    p_hash = compute_prompt_hash(course_code, question_latex)
    # Complex proof -> DeepSeek-R1
    result = route_math_request(prompt, course_code, topic_label=topic_label, is_complex_proof=True)

    if result.get("success"):
        solution_text = normalize_math_delimiters(result["content"])
        reasoning_text = result.get("reasoning_content", "")

        # Save to question object in DB if provided
        if question_obj and not question_obj.solution_latex:
            question_obj.solution_latex = solution_text
            question_obj.verification_status = "verified"
            question_obj.save(update_fields=["solution_latex", "verification_status"])

        payload = {
            "solution": solution_text,
            "reasoning": reasoning_text,
            "model": result.get("model_used", "deepseek-reasoner"),
            "course": course_code,
            "generated_at": timezone.now().isoformat(),
        }
        store_cached_content(cache_key, "solution_derivation", p_hash, payload)

        return {
            "solution": solution_text,
            "reasoning": reasoning_text,
            "cached": False,
            "model": result.get("model_used"),
            "usage": result.get("usage", {}),
            "sympy_check": sympy_res if sympy_res.get("success") else None,
        }

    return {
        "solution": "Solution derivation is being processed. Please try again shortly.",
        "cached": False,
        "error": result.get("error"),
    }
