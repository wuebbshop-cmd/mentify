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
    source_context = _approved_course_source_context(course_obj, topic_title)
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
        json.dumps(_course_study_profile(course_obj), ensure_ascii=True, sort_keys=True),
        hashlib.sha256(source_context.encode("utf-8", errors="ignore")).hexdigest(),
    )[:16]


NOTES_CACHE_VERSION = "markdown-katex-v7-profiled"
NOTE_VALIDATION_STATE = "validated-v2"
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


def _course_study_profile(course_obj) -> dict:
    profile = getattr(course_obj, "study_profile", None)
    return profile if isinstance(profile, dict) and profile.get("subject_family") else {}


def _course_study_profile_version(course_obj) -> int:
    return int(getattr(course_obj, "study_profile_version", 0) or 0)


def _required_note_sections(topic_title: str, study_profile: dict | None = None) -> list[str]:
    """Return the section headings a generated topic note must contain."""
    if study_profile and isinstance(study_profile.get("note_structure"), list):
        section_count = len(study_profile["note_structure"])
        if section_count:
            return [f"## {index}." for index in range(1, section_count + 1)]
    topic_lower = (topic_title or "").lower()
    is_overview = any(
        word in topic_lower
        for word in ("overview", "introduction", "intro", "outline", "syllabus", "orientation", "prerequisite")
    )
    section_count = 4 if is_overview else 5
    return [f"## {index}." for index in range(1, section_count + 1)]


def _note_allows_code(course_obj, topic_title: str, summary: str = "", subtopics=None) -> bool:
    """Allow code only when notes-backed profile and this topic support it."""
    scope_parts = [
        str(topic_title or ""),
        str(summary or ""),
        " ".join(str(item) for item in (subtopics or [])),
    ]
    profile = _course_study_profile(course_obj)
    if profile:
        capabilities = profile.get("capabilities") if isinstance(profile.get("capabilities"), dict) else {}
        if not capabilities.get("code"):
            return False
    else:
        scope_parts.extend([
            str(getattr(course_obj, "title", "") or ""),
            str(getattr(course_obj, "description", "") or ""),
        ])
    scope = " ".join(scope_parts).lower()
    explicit_code_terms = (
        "programming", "software", "python", "r language", "r programming", "data frame",
        "source code", "computer algorithm", "coding", "syntax", "plotting",
    )
    profile = _course_study_profile(course_obj)
    family = str(profile.get("subject_family") or "").lower()
    return any(term in scope for term in explicit_code_terms) or (
        family == "computing" and bool(re.search(r"\br\b", scope))
    )


def _note_allows_math(course_obj) -> bool | None:
    """Return the approved source capability, or None for legacy courses."""
    profile = _course_study_profile(course_obj)
    if not profile:
        return None
    capabilities = profile.get("capabilities") if isinstance(profile.get("capabilities"), dict) else {}
    return bool(capabilities.get("math_notation") or capabilities.get("chemical_equations"))


def _note_validation_options(course_obj, topic_title: str, summary: str = "", subtopics=None) -> dict:
    return {
        "allow_code": _note_allows_code(course_obj, topic_title, summary, subtopics),
        "allow_math": _note_allows_math(course_obj),
        "study_profile": _course_study_profile(course_obj),
    }


def _approved_course_source_context(course_obj, topic_title: str, limit: int = 8000) -> str:
    """Return bounded excerpts from approved coursework for grounded generation."""
    if not course_obj:
        return ""
    from prep.models import PrepDocument

    documents = PrepDocument.objects.filter(
        course=course_obj,
        stage="stage_3",
        doc_type__in=["Lecture Notes", "Revision Sheet"],
    ).exclude(extracted_text="").order_by("-updated_at", "-id")
    topic_words = [word for word in re.findall(r"[A-Za-z0-9]+", topic_title.lower()) if len(word) > 3]
    selected = []
    seen_hashes = set()
    total_length = 0
    for document in documents:
        text = str(document.extracted_text or "").strip()
        if not text:
            continue
        text_hash = hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()
        if text_hash in seen_hashes:
            continue
        is_topic_document = any(word in text.lower() for word in topic_words[:4])
        is_course_document = str(document.topic_name or "").strip().lower() == "full syllabus"
        if not is_topic_document and not is_course_document:
            continue
        seen_hashes.add(text_hash)
        excerpt_limit = min(limit - total_length, limit if is_topic_document else 5000)
        if excerpt_limit <= 0:
            break
        selected.append(text[:excerpt_limit])
        total_length += excerpt_limit
        if total_length >= limit:
            break
    return "\n\n--- APPROVED COURSEWORK EXCERPT ---\n\n".join(selected)[:limit]


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


def _markdown_theorem_issues(content: str) -> list[str]:
    """Reject theorem titles split into Markdown list-looking fragments."""
    lines = content.splitlines()
    issues: list[str] = []
    theorem_start = re.compile(r"^\s*>\s*\*\*(?:Theorem|Definition|Lemma|Corollary)\b")

    for index, line in enumerate(lines):
        if not re.match(r"^\s*(?:>\s*)?-[A-Za-z]", line):
            continue
        previous_lines = lines[max(0, index - 2):index]
        if any(theorem_start.match(previous) for previous in previous_lines):
            issues.append(f"theorem blockquote title is split near line {index + 1}")

    return issues


def _note_format_issues(content: str) -> list[str]:
    """Return local Markdown/LaTeX issues without requiring note sections."""
    issues = []
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
    issues.extend(_markdown_theorem_issues(content))
    return issues


def _note_repair_scope(content: str, topic_title: str) -> tuple[str, str, str]:
    """Select one invalid section while preserving every other section verbatim."""
    headings = list(re.finditer(r"(?m)^\s*##\s+\d+\.[^\n]*", content))
    sections = []
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(content)
        section = content[heading.start():end]
        issues = _note_format_issues(section)
        if issues:
            sections.append((heading.start(), end, section))
    if len(sections) == 1:
        start, end, section = sections[0]
        return content[:start], section, content[end:]
    return "", content, ""


def _note_needs_section_regeneration(issues: list[str]) -> bool:
    """Identify failures that cannot be fixed with an old_block/new_block patch."""
    return any(
        issue.startswith("missing section")
        or issue in {
            "unclosed display-math block",
            "unclosed fenced code block",
            "content ends at an escape delimiter",
            "final section has insufficient content",
            "code block is not allowed for this topic",
        }
        for issue in issues
    )


def _regenerate_invalid_note_sections(
    topic_obj,
    level: str,
    source_signature: str,
    cache_key: str,
    content: str,
    issues: list[str],
):
    """Regenerate only the contiguous invalid/missing section range."""
    from prep.models import PrepContentCache, PrepNoteRepair

    required_numbers = [int(heading.split()[1].rstrip(".")) for heading in _required_note_sections(topic_obj.title)]
    headings = list(re.finditer(r"(?m)^\s*##\s+(\d+)\.[^\n]*", content))
    section_issues = {}
    existing_numbers = {int(heading.group(1)) for heading in headings}
    missing_numbers = set(required_numbers) - existing_numbers
    for index, heading in enumerate(headings):
        number = int(heading.group(1))
        end = headings[index + 1].start() if index + 1 < len(headings) else len(content)
        local_issues = _note_format_issues(content[heading.start():end])
        if missing_numbers and number == max(existing_numbers, default=number):
            local_issues = [issue for issue in local_issues if issue != "final section has insufficient content"]
        if local_issues:
            section_issues[number] = local_issues

    affected_numbers = set(section_issues) | missing_numbers
    if not affected_numbers:
        return None

    first_number = min(affected_numbers)
    last_number = max(affected_numbers)
    first_match = next((heading for heading in headings if int(heading.group(1)) == first_number), None)
    next_match = next(
        (heading for heading in headings if int(heading.group(1)) > last_number),
        None,
    )
    prefix = content[:first_match.start()] if first_match else content
    suffix = content[next_match.start():] if next_match else ""
    requested_sections = ", ".join(f"## {number}." for number in range(first_number, last_number + 1))
    validation_options = _note_validation_options(
        topic_obj.course,
        topic_obj.title,
        topic_obj.summary,
        topic_obj.subtopics,
    )
    allows_code = validation_options["allow_code"]
    source_excerpt = _approved_course_source_context(topic_obj.course, topic_obj.title)

    repair, _ = PrepNoteRepair.objects.get_or_create(
        topic=topic_obj,
        level=level,
        source_signature=source_signature,
        defaults={
            "cache_key": cache_key,
            "original_content": content,
            "current_content": content,
            "validation_issues": issues,
        },
    )
    if repair.status == "validated" or repair.status == "needs_review":
        return None

    working_content = repair.current_content or content
    for _ in range(repair.attempts, 2):
        repair.attempts += 1
        repair.validation_issues = issues
        repair.save(update_fields=["attempts", "validation_issues", "updated_at"])
        code_instruction = (
            "Code is permitted only when directly required by the topic.\n"
            if allows_code
            else "Do not include R, Python, pseudocode, or any fenced code blocks.\n"
        )
        prompt = (
            f"Regenerate only these incomplete note sections: {requested_sections}.\n"
            f"Topic: {topic_obj.title}\nLevel: {level}\n"
            "Preserve the existing valid sections exactly. Return only the replacement sections, "
            "including their Markdown headings. Use the required Markdown and KaTeX rules.\n"
            + code_instruction
            + "Validation errors:\n" + json.dumps(issues) + "\n"
            + "Approved coursework source:\n" + source_excerpt + "\n"
            "Existing note context:\n" + working_content[:4000]
        )
        result = route_math_request(prompt, topic_obj.course.code, topic_label=topic_obj.title, is_complex_proof=False)
        if not result.get("success") or not result.get("content"):
            continue
        replacement = normalize_math_delimiters(result["content"]).strip()
        candidate = prefix.rstrip() + "\n\n" + replacement
        if suffix:
            candidate += "\n\n" + suffix.lstrip()
        candidate_issues = _note_completion_issues(
            candidate,
            topic_obj.title,
            **validation_options,
        )
        if candidate_issues:
            working_content = candidate
            issues = candidate_issues
            repair.current_content = candidate
            repair.validation_issues = candidate_issues
            repair.save(update_fields=["current_content", "validation_issues", "updated_at"])
            continue

        entry = PrepContentCache.objects.filter(cache_key=cache_key).first()
        if not entry:
            return None
        payload = _cache_payload_as_dict(entry.payload) or {}
        payload.update({
            "content": candidate,
            "validation_state": NOTE_VALIDATION_STATE,
            "validated_at": timezone.now().isoformat(),
            "level": level,
            "study_profile_version": _course_study_profile_version(topic_obj.course),
        })
        entry.payload = payload
        entry.save(update_fields=["payload", "updated_at"])
        repair.current_content = candidate
        repair.validation_issues = []
        repair.status = "validated"
        repair.save(update_fields=["current_content", "validation_issues", "status", "updated_at"])
        return {
            "notes": candidate,
            "cached": False,
            "repaired": True,
            "usage": result.get("usage", {}),
            "model": result.get("model_used", "deepseek-chat"),
        }

    repair.status = "needs_review"
    repair.last_error = "; ".join(issues)
    repair.save(update_fields=["status", "last_error", "updated_at"])
    _record_note_generation_failure(topic_obj, level, source_signature, repair.last_error, force_review=True)
    return None


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
    source_without_display = re.sub(r"\\\[[\s\S]*?\\\]", "", source_without_display)
    source_without_display = re.sub(r"`+[^`]*`+", "", source_without_display)
    for environment in sorted(set(re.findall(r"\\begin\{([^{}]+)\}", source_without_display))):
        issues.append(f"LaTeX environment {environment} is outside display math")

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

        if curly_depth:
            issues.append(f"display-math block {index} has unmatched braces")

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


def _note_completion_issues(
    content: str,
    topic_title: str,
    *,
    allow_code: bool | None = None,
    allow_math: bool | None = None,
    study_profile: dict | None = None,
) -> list[str]:
    """Detect incomplete note output before it is displayed or cached."""
    if not isinstance(content, str) or not content.strip():
        return ["empty content"]

    issues: list[str] = []
    family = str((study_profile or {}).get("subject_family") or "").strip().lower()
    if family in {"social_science", "humanities", "business_economics", "general_science"}:
        if _nontechnical_solution_has_proof_scaffold(content):
            issues.append("mathematical proof scaffold is not allowed for this subject family")

    for heading in _required_note_sections(topic_title, study_profile):
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

    issues.extend(_note_format_issues(content))
    if allow_code is False and re.search(r"```[A-Za-z0-9_+-]*\s*\n", content):
        issues.append("code block is not allowed for this topic")
    if allow_math is False:
        math_source = re.sub(r"```[\s\S]*?```", "", content)
        if re.search(r"\$\$?|\\\\\[|\\\\\(|\\\\begin\{|\\\\(?:frac|int|sum|prod|lim|mathbb)", math_source):
            issues.append("math notation is not supported by the approved course notes")
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
    if not isinstance(content, str):
        return content or ""

    def repair_escaped_dollars_inside_math(source: str) -> str:
        """Remove an impossible literal dollar only when it occurs in math.

        A provider occasionally emits ``\\$\\lim`` inside an already-open
        expression. KaTeX treats that as a literal dollar, not a delimiter,
        which corrupts the rest of the expression. A literal dollar is never
        meaningful inside LaTeX math, so this is a bounded transport repair;
        escaped currency in prose is deliberately left untouched.
        """
        output = []
        mode = None
        index = 0
        while index < len(source):
            char = source[index]
            next_char = source[index + 1] if index + 1 < len(source) else ""
            if char == "\\" and next_char == "$":
                if mode is None:
                    output.extend((char, next_char))
                # Inside math, omit only the accidental literal dollar.
                index += 2
                continue
            if char == "$":
                if next_char == "$":
                    mode = None if mode == "display" else ("display" if mode is None else mode)
                    output.extend((char, next_char))
                    index += 2
                    continue
                mode = None if mode == "inline" else ("inline" if mode is None else mode)
            output.append(char)
            index += 1
        return "".join(output)

    if "\n" not in content:
        return repair_escaped_dollars_inside_math(content)

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

    return repair_escaped_dollars_inside_math("".join(output))


def _publish_legacy_note_cache(
    entry,
    payload: dict,
    topic_title: str,
    *,
    allow_code: bool | None = None,
    allow_math: bool | None = None,
    study_profile: dict | None = None,
) -> dict | None:
    """Validate an unmarked legacy note once, then persist its publication state."""
    content = repair_json_escaped_latex_newlines(
        str(payload.get("content") or payload.get("notes") or "")
    ).strip()
    if not content or _note_completion_issues(
        content,
        topic_title,
        allow_code=allow_code,
        allow_math=allow_math,
        study_profile=study_profile,
    ):
        return None

    published_payload = dict(payload)
    published_payload["content"] = content
    published_payload["validation_state"] = NOTE_VALIDATION_STATE
    published_payload["validated_at"] = timezone.now().isoformat()
    entry.payload = published_payload
    entry.save(update_fields=["payload", "updated_at"])
    return published_payload


def get_published_topic_note_levels(topic_obj, *, validated_only: bool = False) -> dict[str, str]:
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
        if int(payload.get("study_profile_version", 0) or 0) != _course_study_profile_version(topic_obj.course):
            continue
        validation_options = _note_validation_options(
            topic_obj.course,
            topic_obj.title,
            topic_obj.summary,
            topic_obj.subtopics,
        )
        if validated_only and payload.get("validation_state") != NOTE_VALIDATION_STATE:
            continue
        if payload.get("validation_state") != NOTE_VALIDATION_STATE:
            payload = _publish_legacy_note_cache(
                entry,
                payload,
                topic_obj.title,
                **validation_options,
            )
        if not payload:
            continue
        content = normalize_math_delimiters(
            str(payload.get("content") or payload.get("notes") or "")
        ).strip()
        content_issues = _note_completion_issues(content, topic_obj.title, **validation_options)
        if content_issues:
            # A new policy can invalidate an older published row without
            # changing the underlying syllabus source.
            continue
        if content != payload.get("content"):
            payload = dict(payload)
            payload["content"] = content
            payload["validation_state"] = NOTE_VALIDATION_STATE
            payload["validated_at"] = timezone.now().isoformat()
            payload["study_profile_version"] = _course_study_profile_version(topic_obj.course)
            entry.payload = payload
            entry.save(update_fields=["payload", "updated_at"])
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
    _notify_note_generation_failure(guard.pk)
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


def _notify_note_generation_failure(guard_id: int) -> None:
    """Send a one-time admin alert, retaining failed delivery for later retry."""
    from django.db import transaction
    from prep.models import PrepNoteGenerationGuard
    from services.email_service import send_prep_note_generation_failure_email

    with transaction.atomic():
        guard = (
            PrepNoteGenerationGuard.objects.select_for_update()
            .select_related("topic__course")
            .filter(pk=guard_id, status="needs_review", notification_sent_at__isnull=True)
            .first()
        )
        if not guard:
            return
        if send_prep_note_generation_failure_email(guard):
            guard.notification_sent_at = timezone.now()
            guard.save(update_fields=["notification_sent_at", "updated_at"])


def _record_note_generation_failure(
    topic_obj,
    level: str,
    source_signature: str,
    error: str,
    *,
    force_review: bool = False,
) -> None:
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
    if force_review or guard.failed_attempts >= NOTE_MAX_FAILED_GENERATION_CYCLES:
        guard.status = "needs_review"
    guard.save(update_fields=["failed_attempts", "last_error", "last_failed_at", "status", "updated_at"])
    if guard.status == "needs_review":
        _notify_note_generation_failure(guard.pk)


def _clear_note_generation_guard(topic_obj, level: str, source_signature: str) -> None:
    if not topic_obj:
        return
    from prep.models import PrepNoteGenerationGuard

    PrepNoteGenerationGuard.objects.filter(
        topic=topic_obj,
        level=level,
        source_signature=source_signature,
    ).delete()


def _mark_cached_note_valid(topic_obj, level: str, source_signature: str, content: str) -> None:
    if not topic_obj:
        return
    from prep.models import PrepNoteRepair

    PrepNoteRepair.objects.filter(
        topic=topic_obj,
        level=level,
        source_signature=source_signature,
    ).exclude(status="validated").update(
        current_content=content,
        validation_issues=[],
        status="validated",
        last_error="",
        updated_at=timezone.now(),
    )
    _clear_note_generation_guard(topic_obj, level, source_signature)


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
    validation_options = _note_validation_options(
        topic_obj.course,
        topic_title,
        topic_obj.summary,
        topic_obj.subtopics,
    )

    for entry in entries:
        payload = _cache_payload_as_dict(entry.payload)
        if not payload or payload.get("level") != level:
            continue
        if int(payload.get("study_profile_version", 0) or 0) != _course_study_profile_version(topic_obj.course):
            continue

        content = normalize_math_delimiters(
            str(payload.get("content") or payload.get("notes") or "")
        ).strip()
        if payload.get("validation_state") != NOTE_VALIDATION_STATE:
            payload = _publish_legacy_note_cache(entry, payload, topic_title, **validation_options)
        if not payload:
            continue
        content = repair_json_escaped_latex_newlines(
            str(payload.get("content") or payload.get("notes") or "")
        ).strip()
        if not content or _note_completion_issues(content, topic_title, **validation_options):
            continue

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


# ─── Targeted invalid-note repair ────────────────────────────────────────────

def _repair_invalid_note_cache(topic_obj, level, source_signature, cache_key, content, issues):
    """Quarantine invalid notes and attempt bounded block-level repair."""
    from prep.models import PrepContentCache, PrepNoteRepair

    repair, _ = PrepNoteRepair.objects.get_or_create(
        topic=topic_obj,
        level=level,
        source_signature=source_signature,
        defaults={"cache_key": cache_key, "original_content": content, "current_content": content, "validation_issues": issues},
    )
    if repair.status == "validated":
        return {"notes": repair.current_content, "usage": {}}
    if repair.status == "needs_review" or repair.attempts >= 3:
        return None

    working_content = repair.current_content or content
    validation_options = _note_validation_options(
        topic_obj.course,
        topic_obj.title,
        topic_obj.summary,
        topic_obj.subtopics,
    )
    for _ in range(repair.attempts, 3):
        repair.attempts += 1
        repair.validation_issues = issues
        repair.save(update_fields=["attempts", "validation_issues", "updated_at"])
        prefix, repair_scope, suffix = _note_repair_scope(working_content, topic_obj.title)
        result = call_together_repair(
            [
                {"role": "system", "content": "Return JSON only. Repair one Markdown/LaTeX block surgically. Never split words, theorem titles, or sentences across lines. Preserve Markdown blockquote prefixes on every theorem line."},
                {"role": "user", "content": "Return old_block and new_block. Change only the reported issue; preserve all other text.\nIssues: " + json.dumps(issues) + "\nSource (only the affected section when identifiable):\n" + repair_scope},
            ],
            model=getattr(settings, "TOGETHER_REPAIR_MODEL", "deepseek-ai/DeepSeek-V4.1-Flash"),
            max_tokens=2000,
        )
        if not result.get("success"):
            continue
        try:
            patch = robust_json_loads(str(result.get("content") or ""))
            old_block = str(patch.get("old_block") or "")
            new_block = str(patch.get("new_block") or "")
            if not old_block or not new_block or repair_scope.count(old_block) != 1:
                raise ValueError("repair block missing or not unique")
            repaired_scope = repair_scope.replace(old_block, new_block, 1)
            candidate = prefix + repaired_scope + suffix
            candidate_issues = _note_completion_issues(
                candidate,
                topic_obj.title,
                **validation_options,
            )
            if candidate_issues:
                working_content = candidate
                issues = candidate_issues
                repair.current_content = candidate
                repair.validation_issues = candidate_issues
                repair.save(update_fields=["current_content", "validation_issues", "updated_at"])
                continue
            entry = PrepContentCache.objects.filter(cache_key=cache_key).first()
            if not entry:
                return None
            payload = _cache_payload_as_dict(entry.payload) or {}
            payload.update({
                "content": candidate,
                "validation_state": NOTE_VALIDATION_STATE,
                "validated_at": timezone.now().isoformat(),
                "study_profile_version": _course_study_profile_version(topic_obj.course),
            })
            entry.payload = payload
            entry.save(update_fields=["payload", "updated_at"])
            repair.current_content = candidate
            repair.validation_issues = []
            repair.status = "validated"
            repair.save(update_fields=["current_content", "validation_issues", "status", "updated_at"])
            return {"notes": candidate, "cached": False, "repaired": True, "usage": result.get("usage", {})}
        except Exception as exc:
            logger.warning(
                "[Topic Notes] targeted repair patch rejected for %s: %s",
                topic_obj.title,
                exc,
            )
            continue

    repair.status = "needs_review"
    repair.last_error = "; ".join(issues)
    repair.save(update_fields=["status", "last_error", "updated_at"])
    _record_note_generation_failure(
        topic_obj,
        level,
        source_signature,
        repair.last_error,
        force_review=True,
    )
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


def call_together_repair(messages: list[dict], model: str, max_tokens: int = 2000) -> dict:
    """Make one bounded Together.ai repair call with no continuation."""
    api_key = getattr(settings, "TOGETHERAI_API", "") or os.environ.get("TOGETHERAI_API", "")
    if not api_key:
        return {"success": False, "error": "TOGETHERAI_API key is not configured."}

    try:
        response = requests.post(
            "https://api.together.xyz/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={"model": model, "messages": messages, "max_tokens": max_tokens, "temperature": 0.1},
            timeout=60,
        )
        if response.status_code != 200:
            return {"success": False, "error": f"Together HTTP {response.status_code}: {response.text[:500]}"}
        data = response.json()
        choice = data["choices"][0]
        return {
            "success": True,
            "content": choice.get("message", {}).get("content", "").strip(),
            "model_used": model,
            "usage": data.get("usage", {}),
        }
    except Exception as exc:
        logger.warning("[Together Repair] request failed: %s", exc)
        return {"success": False, "error": str(exc)}


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
            "7. Never split a word, theorem title, or sentence across lines. Keep the complete title on one logical Markdown line, and preserve '> ' on every continuation line inside a blockquote.\n"
            "8. NEVER chain equalities horizontally (e.g. NEVER write 'A = B = C = D'). Always format derivations vertically using \\begin{aligned}...\\end{aligned} inside $$...$$.\n"
            "9. If code is explicitly required by the topic, fenced code blocks must use a language tag and remain complete. Otherwise, do not output code blocks.\n"
            "10. In Markdown tables, EVERY row must start with '|' and end with '|'. If math in table cells uses absolute values, norms, or determinants, ALWAYS use \\lvert x \\rvert, \\lVert x \\rVert, or \\det(A). NEVER use raw unescaped '|' (like '|x|') inside table cells because raw pipes split markdown table columns.\n"
            "11. Do not include conversational greetings or filler text."
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
    Shared renderer hygiene for notes, authentic questions, generated questions,
    and PDF exports. It performs only deterministic transport repairs and does
    not guess at or auto-close mathematical expressions.
    """
    if not text:
        return ""
    text = repair_json_escaped_latex_newlines(str(text))
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
    topic_summary = str(getattr(topic_obj, "summary", "") or "").strip() if topic_obj else ""
    study_profile = _course_study_profile(course_obj)
    validation_options = _note_validation_options(course_obj, topic_title, topic_summary, subtopics)
    allows_code = validation_options["allow_code"]
    allows_math = validation_options["allow_math"]

    # A published shared note belongs to this specific approved topic and
    # level. Serve it before the historical signature-key path so unrelated
    # course changes cannot make later students regenerate already-approved
    # content. A material change to this topic removes these entries via the
    # PrepTopic signal above.
    published_levels = get_published_topic_note_levels(topic_obj, validated_only=True)
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
    cache_key = compute_cache_key(
        "notes", NOTES_CACHE_VERSION, course_code, topic_title, level, cache_signature
    )
    cached = get_cached_content(cache_key)
    regenerated_from_invalid_cache = False
    if cached and isinstance(cached, dict) and ("content" in cached or "blocks" in cached):
        cached_content = repair_json_escaped_latex_newlines(
            str(cached.get("content", "") or "")
        )
        cached_issues = _note_completion_issues(cached_content, topic_title, **validation_options)
        if cached.get("validation_state") == NOTE_VALIDATION_STATE and not cached_issues:
            # Strict read-only: never mutate or overwrite a valid cache on read.
            _mark_cached_note_valid(topic_obj, level, cache_signature, cached_content)
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
        if not cached_issues:
            from prep.models import PrepContentCache

            cached["content"] = cached_content
            cached["validation_state"] = NOTE_VALIDATION_STATE
            cached["validated_at"] = timezone.now().isoformat()
            PrepContentCache.objects.filter(cache_key=cache_key).update(payload=cached)
            _mark_cached_note_valid(topic_obj, level, cache_signature, cached_content)
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
        # Missing or truncated sections require section regeneration; local
        # formatting defects use exact block replacement instead.
        if _note_needs_section_regeneration(cached_issues):
            repair = _regenerate_invalid_note_sections(
                topic_obj,
                level,
                cache_signature,
                cache_key,
                cached_content,
                cached_issues,
            )
        else:
            repair = _repair_invalid_note_cache(
                topic_obj,
                level,
                cache_signature,
                cache_key,
                cached_content,
                cached_issues,
            )
        if repair:
            repair["level"] = level
            repair["regenerated_from_invalid_cache"] = True
            return repair
        fallback = _latest_valid_shared_notes(
            topic_obj,
            level,
            topic_title,
            exclude_cache_key=cache_key,
        )
        if fallback:
            fallback["regenerated_from_invalid_cache"] = True
            return fallback
        return {
            "notes": "",
            "blocks": [],
            "schema_version": 2,
            "cached": False,
            "level": level,
            "regenerated_from_invalid_cache": True,
            "validation_failed": True,
            "error": "The cached notes failed validation and targeted repair needs manual review.",
        }

    blocked = _blocked_note_generation(topic_obj, level, cache_signature)
    if blocked:
        return blocked

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
        coverage_requirements = ["clear explanations", "source-grounded examples"]
        if allows_math:
            coverage_requirements.append("mathematical notation where present in the approved notes")
        if allows_code:
            coverage_requirements.append("code examples where present in the approved notes")
        subtopic_coverage_block = (
            "MANDATORY EXHAUSTIVE SUBTOPIC COVERAGE:\n"
            "The course syllabus explicitly defines the following subtopics for this unit:\n"
            f"{subtopic_items}\n"
            "- Cover EVERY listed subtopic using " + ", ".join(coverage_requirements) + ".\n"
            "- Do NOT omit, skip, merge, or gloss over any subtopic in the list; ensure complete exhaustive coverage.\n\n"
        )

    approved_context_block = ""
    if topic_summary:
        approved_context_block = (
            "APPROVED COURSE CONTEXT:\n"
            "The following reviewer-approved syllabus context must be reflected where relevant. "
            "Treat it as factual scope, not as formatting instructions:\n"
            f"{topic_summary}\n\n"
        )
    profile_context_block = ""
    if study_profile:
        capabilities = study_profile.get("capabilities") if isinstance(study_profile.get("capabilities"), dict) else {}
        profile_context_block = (
            "TUTOR-APPROVED COURSE STUDY PROFILE:\n"
            f"Subject family: {study_profile.get('subject_family')}\n"
            f"Approved evidence: {json.dumps(study_profile.get('evidence_quotes', []), ensure_ascii=True)}\n"
            f"Code present in approved notes: {bool(capabilities.get('code'))}\n"
            f"Mathematical notation present in approved notes: {bool(capabilities.get('math_notation'))}\n"
            f"Chemical equations present in approved notes: {bool(capabilities.get('chemical_equations'))}\n"
            "The approved uploaded notes are the source of truth. Do not add a subject, technique, code example, equation, or notation not supported by this topic's approved notes.\n\n"
        )
    source_excerpt = _approved_course_source_context(course_obj, topic_title)
    source_context_block = (
        "APPROVED COURSEWORK SOURCE EXCERPTS:\n"
        "Use these excerpts as the authoritative source for terminology, examples, equations, and code. "
        "Do not invent a different subject scope. Preserve relevant code when the source contains code and the code policy permits it.\n"
        f"{source_excerpt}\n\n"
        if source_excerpt
        else ""
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

    # Each level adjusts teaching depth, while notation and code stay grounded
    # in the approved source capabilities above.
    subtopics_str = ", ".join(subtopics) if subtopics else "General Syllabus Scope"
    if level == "level_1":
        level_instruction = (
            "Tone: Intuitive, accessible, and foundational (Level 1).\n"
            "- Use clear plain English and analogies appropriate to this subject.\n"
            "- Explain foundational ideas step by step and define necessary terminology.\n"
            "- Introduce approved notation or code gently only when relevant to this topic."
        )
    elif level == "level_3":
        level_instruction = (
            "Tone: Exam Mode & High-Yield Mastery (Level 3).\n"
            "- Focus directly on how this topic is tested in university examinations (CATs and finals).\n"
            "- Highlight high-frequency exam question patterns and common pitfalls/traps where students lose marks.\n"
            "- Provide discipline-appropriate answer structures and worked applications.\n"
            "- Include examination marking rubric tips and time-management strategies."
        )
    else:  # level_2
        level_instruction = (
            "Tone: University Undergraduate Standard (Level 2).\n"
            "- Deliver standard university notes with precise definitions and academic rigor.\n"
            "- Include a representative worked example or application grounded in the approved notes.\n"
            "- Use formal notation only where supported by the approved source and relevant to this topic."
        )
    if study_profile and study_profile.get("subject_family") in {
        "social_science", "humanities", "business_economics", "general_science",
    }:
        level_instruction = (
            f"Tone: University-level {study_profile['subject_family'].replace('_', ' ')} teaching (Level {level[-1]}).\n"
            "- Explain the approved concepts, evidence, context, and applications clearly.\n"
            "- Do not introduce mathematical derivations or programming unless the approved source capability explicitly allows them."
        )
    if allows_math:
        level_instruction += "\n- Include relevant source-supported equations or derivations at the depth appropriate to this level."
    else:
        level_instruction += "\n- Do not add equations, mathematical derivations, or proof templates."
    if allows_code:
        level_instruction += "\n- Include source-supported code examples when relevant to this topic."
    else:
        level_instruction += "\n- Do not include code or programming syntax."

    # Topic-type awareness is driven by approved course metadata and scope;
    # mathematical notation must not be mistaken for programming.
    topic_lower = topic_title.lower()
    is_overview = any(w in topic_lower for w in ["overview", "introduction", "intro", "outline", "syllabus", "orientation", "prerequisite"])
    profile_sections = study_profile.get("note_structure") if isinstance(study_profile.get("note_structure"), list) else []

    if study_profile and profile_sections:
        section_structure = (
            "Use this approved subject-specific structure, keeping the numbered headings exactly as shown:\n"
            + "\n".join(f"## {index}. {title}" for index, title in enumerate(profile_sections, start=1))
            + "\n\nCover only the current topic and the uploaded notes' content. Do not add unsupported subjects."
        )
        required_last_section = f"## {len(profile_sections)}."
    elif is_overview:
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
    elif allows_code:
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

    code_policy = (
        "CODE POLICY: Include code only when approved notes support it and it is relevant to this topic. Use source-grounded examples only.\n"
        if allows_code
        else "CODE POLICY: Do not include code, pseudocode, programming syntax, or fenced code blocks.\n"
    )
    math_policy = (
        "MATHEMATICS POLICY: Use equations and notation only when evidenced in approved notes and relevant to this topic. Do not invent formulas.\n"
        if allows_math is not False
        else "MATHEMATICS POLICY: Approved notes contain no mathematical notation. Do not include equations, formulas, symbolic derivations, LaTeX, or mathematical examples.\n"
    )
    authoring_rules = (
        "Use clear Markdown prose, lists, and headings. Do not use math delimiters, LaTeX commands, equations, formulas, or symbolic derivations. "
        "Do not add a formula merely to make the notes look technical. Every factual claim and example must stay within the approved notes.\n"
        if allows_math is False
        else (
            "STRICT MATHEMATICAL AUTHORING FORMAT:\n"
            "1. Inline math uses $...$ with no inner spaces and closes before punctuation or paragraph breaks.\n"
            "2. Display math uses $$...$$ on dedicated lines; do not put prose or blank structural breaks inside it.\n"
            "3. Enclose every LaTeX environment in display math.\n"
            "4. Do not output HTML.\n"
            "5. Put Markdown headings on their own lines; do not put math delimiters in headings.\n"
            "6. Preserve complete words, theorem titles, and blockquote prefixes.\n"
            "7. Do not chain long equalities; use aligned derivations when the source requires them.\n"
            "8. Use complete, language-tagged code blocks only when the CODE POLICY permits code.\n"
            "9. Keep all math delimiters and LaTeX groups balanced.\n"
            "10. Keep Markdown table rows complete and escape mathematical pipes.\n"
        )
    )

    prompt = (
        f"Generate comprehensive, publication-grade structured revision notes for the course '{course_code}', topic '{topic_title}'.\n\n"
        f"{subtopic_coverage_block}"
        f"{approved_context_block}"
        f"{profile_context_block}"
        f"{source_context_block}"
        f"{curriculum_boundary_block}"
        f"{level_instruction}\n\n"
        f"{code_policy}\n"
        f"{math_policy}\n"
        f"{authoring_rules}"
        f"12. MANDATORY: Generate notes completely through to the end of the final section ({required_last_section}). Never truncate.\n\n"
        f"{section_structure}"
    )

    note_system_prompt = None
    if study_profile:
        note_system_prompt = (
            f"You are an expert university tutor for the approved subject family {study_profile.get('subject_family')}. "
            "Treat uploaded notes and quoted evidence as the sole factual scope. Do not infer content from course codes, exams, or generic conventions. "
            + ("Do not use equations, mathematical symbols, LaTeX, or code because the approved notes contain none. " if not allows_math and not allows_code else "")
            + ("Include code only where the approved topic notes support it. " if allows_code else "Do not include code or pseudocode. ")
            + ("Use mathematical notation only where the approved notes support it. " if allows_math else "Do not include mathematical notation or equations. ")
            + "Follow the supplied note structure exactly and return only the notes."
        )

    p_hash = compute_prompt_hash(course_code, topic_title, level, prompt)
    result = route_math_request(
        prompt,
        course_code,
        topic_label=topic_title,
        is_complex_proof=False,
        system_prompt=note_system_prompt,
    )

    if result.get("success"):
        content = normalize_math_delimiters(result["content"])

        # Continue boundedly until all required sections and delimiters are complete.
        # This protects against responses that contain the final heading but stop
        # before its body, which the old heading-only check accepted.
        for continuation_attempt in range(2):
            completion_issues = _note_completion_issues(content, topic_title, **validation_options)
            if not completion_issues:
                break
            needs_continuation = any(
                issue.startswith("missing section")
                or issue in {
                    "unclosed display-math block",
                    "unclosed fenced code block",
                    "content ends at an escape delimiter",
                    "final section has insufficient content",
                }
                for issue in completion_issues
            )
            if not needs_continuation:
                break

            cont_messages = [
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": content},
                {
                    "role": "user",
                    "content": (
                        f"Continue directly from where you stopped and complete the notes through "
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
            if not cont_res.get("success") or not cont_res.get("content"):
                break
            content = content + "\n\n" + cont_res["content"].strip()
            result["usage"] = _merge_usage(result.get("usage", {}), cont_res.get("usage", {}))

        # Preserve the generated Markdown source. The browser renderer is the
        # single owner of Markdown and KaTeX interpretation.
        content = str(content).strip()
        completion_issues = _note_completion_issues(content, topic_title, **validation_options)
        if completion_issues:
            logger.error(
                "[Topic Notes] Refusing to cache incomplete notes for %s %s: %s",
                course_code,
                topic_title,
                "; ".join(completion_issues),
            )
            from prep.models import PrepContentCache

            # Quarantine fresh invalid output through the same targeted repair
            # path used for an invalid cache entry before requiring review.
            entry, _ = PrepContentCache.objects.get_or_create(
                cache_key=cache_key,
                defaults={
                    "content_type": "topic_notes",
                    "prompt_hash": p_hash,
                    "payload": {
                        "schema_version": 2,
                        "content": content,
                        "level": level,
                        "model": result.get("model_used", "deepseek-chat"),
                    },
                    "course": course_obj,
                    "topic": topic_obj,
                },
            )
            repaired = _repair_invalid_note_cache(
                topic_obj,
                level,
                cache_signature,
                cache_key,
                content,
                completion_issues,
            )
            if repaired:
                repaired["level"] = level
                repaired["regenerated_from_invalid_cache"] = regenerated_from_invalid_cache
                _clear_note_generation_guard(topic_obj, level, cache_signature)
                return repaired
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
            "study_profile_version": _course_study_profile_version(course_obj),
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

    # Parse valid JSON before applying legacy array-extraction heuristics;
    # LaTeX strings may contain square brackets inside otherwise valid objects.
    try:
        return json.loads(cleaned, strict=False)
    except Exception:
        pass

    if "[" in cleaned:
        start_idx = cleaned.find("[")
        cleaned = cleaned[start_idx:]
        if "]" in cleaned:
            end_idx = cleaned.rfind("]") + 1
            cleaned = cleaned[:end_idx]

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
        if re.search(r"\\infty\s+S\b", str(question or "")):
            issues.append(f"question {index}: possible infimum operator corrupted to infinity")
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

    # A shared generated set is immutable once verified. Reopening the control
    # must reuse it, never append paid variants because a later click selected
    # a larger count. A deliberate replacement workflow can be added separately
    # with tutor/admin review and an explicit archive step.
    if existing_qs:
        results = []
        for q in existing_qs:
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


def _question_solution_uses_nontechnical_format(course_obj=None, study_profile: dict | None = None) -> bool:
    """Return True when the course should be answered with explanatory analysis rather than proof-style math."""
    profile = study_profile if isinstance(study_profile, dict) else _course_study_profile(course_obj)
    family = str(profile.get("subject_family") or "").strip().lower()
    return family in {"social_science", "humanities", "business_economics", "general_science"}


def _nontechnical_solution_has_proof_scaffold(solution: str) -> bool:
    """Detect legacy math-proof scaffolding that should not be served for non-technical courses."""
    text = str(solution or "").lower()
    if any(marker in text for marker in (
        "problem statement & given conditions",
        "step-by-step rigorous proof / derivation",
        "final result / q.e.d.",
    )):
        return True
    return any(
        re.match(r"^\s*(?:#{1,6}\s+|\d+[.)]\s+|\*\*)", line)
        and re.search(r"\b(?:proof|derivation|theorem|q\.e\.d\.)\b", line)
        for line in text.splitlines()
    )


def get_or_generate_question_solution(question_latex: str, course_code: str, topic_label: str = "", question_obj=None) -> dict:
    """
    Retrieve a verified answer for a question.
    Non-technical subjects use explanatory, source-grounded answers rather than a mathematics proof template.
    """
    course_obj = None
    if question_obj:
        topic_obj = getattr(question_obj, "topic", None)
        if topic_obj:
            course_obj = getattr(topic_obj, "course", None)
        elif getattr(question_obj, "paper", None):
            course_obj = question_obj.paper.course
    study_profile = _course_study_profile(course_obj)
    is_nontechnical = _question_solution_uses_nontechnical_format(course_obj=course_obj, study_profile=study_profile)
    cache_key = compute_cache_key(
        "solution",
        course_code,
        question_latex[:50],
        f"profile-v{_course_study_profile_version(course_obj)}",
        "explanatory-v1" if is_nontechnical else "technical-v1",
    )
    cached = get_cached_content(cache_key)
    if cached:
        cached_solution = str(cached.get("solution") or "")
        if not is_nontechnical or not _nontechnical_solution_has_proof_scaffold(cached_solution):
            return {
                "solution": cached_solution,
                "reasoning": cached.get("reasoning", ""),
                "cached": True,
                "model": cached.get("model", "Cache"),
            }
        logger.warning("[Question Solution] Ignoring proof-style cached answer for non-technical course %s", course_code)

    # First attempt deterministic evaluation if algebraic
    sympy_res = evaluate_symbolic_math(question_latex)

    if is_nontechnical:
        prompt = (
            f"Provide a clear, academically rigorous explanatory answer for this question from course {course_code} "
            f"({topic_label}):\n\n"
            f"{question_latex}\n\n"
            "Structure your response:\n"
            "1. **Key Concept / Definition**\n"
            "2. **Explanation and Analysis**\n"
            "3. **Examples / Evidence / Application**\n"
            "4. **Conclusion / Main Point**\n\n"
            "Use definitions, theories, case examples, and clear academic reasoning. Do not convert it into a proof, derivation, or theorem exercise."
        )
        system_prompt = (
            "You are an expert university tutor in the social sciences and humanities. "
            "Answer with clear academic explanation, definitions, theories, case evidence, and examples. "
            "Do not rewrite the question as a mathematical proof or theorem derivation."
        )
        is_complex_proof = False
    else:
        prompt = (
            f"Provide a rigorous, step-by-step mathematical proof and solution for this examination question "
            f"from course {course_code} ({topic_label}):\n\n"
            f"$$\n{question_latex}\n$$\n\n"
            "Structure your response:\n"
            "1. **Problem Statement & Given Conditions**\n"
            "2. **Step-by-Step Rigorous Proof / Derivation** with complete intermediate steps (never chain equalities horizontally)\n"
            "3. **Final Result / Q.E.D.**"
        )
        system_prompt = None
        is_complex_proof = True

    p_hash = compute_prompt_hash(course_code, question_latex)
    result = route_math_request(prompt, course_code, topic_label=topic_label, is_complex_proof=is_complex_proof, system_prompt=system_prompt)

    if result.get("success"):
        solution_text = normalize_math_delimiters(result["content"])
        reasoning_text = result.get("reasoning_content", "")
        if is_nontechnical and _nontechnical_solution_has_proof_scaffold(solution_text):
            return {
                "solution": "",
                "cached": False,
                "error": "The generated answer used a mathematical proof format and was rejected. Please retry.",
            }

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
        "solution": "",
        "cached": False,
        "error": result.get("error") or "Solution derivation is unavailable. Please try again shortly.",
    }


def generate_adapted_past_question(question_obj) -> dict:
    """Reconstruct one unreadable past-paper question from its context.

    The result is an adapted question, never a claim that the OCR text was
    recovered exactly. It is validated structurally before the caller saves
    it to the shared topic question bank.
    """
    question_text = str(question_obj.question_latex or "").strip()
    topic = question_obj.topic
    course_code = question_obj.paper.course.code if question_obj.paper else topic.course.code
    topic_title = question_obj.topic_label or (topic.title if topic else "Mathematics")
    course_obj = question_obj.paper.course if question_obj.paper else topic.course
    topic_context = []
    if topic:
        if topic.summary.strip():
            topic_context.append("Approved topic summary:\n" + topic.summary.strip())
        subtopics = topic.subtopics if isinstance(topic.subtopics, list) else []
        if subtopics:
            topic_context.append("Approved topic subtopics:\n" + "\n".join(f"- {item}" for item in subtopics))
    source_context = _approved_course_source_context(course_obj, topic_title, limit=4000)
    if source_context:
        topic_context.append("Approved course material excerpts:\n" + source_context)
    topic_context_block = "\n\n".join(topic_context) or "No approved topic notes are available. Use only the explicit topic and source fragments."
    prompt = (
        f"Reconstruct one clear, original practice question closely matching an unreadable past-paper question "
        f"from {course_code}, topic '{topic_title}'.\n\n"
        f"Use this approved syllabus context to constrain the reconstruction:\n{topic_context_block}\n\n"
        f"Unreadable source extraction:\n{question_text}\n\n"
        f"Marks on the source: {question_obj.marks}.\n"
        "Use the approved topic context, visible fragments, source marks, and standard examination conventions. "
        "Do not introduce material outside the stated topic or pretend to reproduce the original wording. "
        "Create a mathematically coherent equivalent "
        "that tests the same likely skill. Include a complete step-by-step solution. Return only one JSON "
        "object with keys: marks, topic_label, question_latex, solution_latex, hint. Use Markdown and KaTeX "
        "delimiters exactly as requested, with no HTML and no code fences around the JSON."
    )
    system_prompt = (
        "You are a careful university mathematics examiner. Return only valid JSON. "
        "All LaTeX backslashes inside JSON strings must be escaped. Keep the adapted question at the same "
        "academic level and topic as the source."
    )
    usage = {}
    model = "deepseek-reasoner"
    last_error = "The adapted question could not be generated."
    for attempt in range(2):
        request_prompt = prompt
        if attempt:
            request_prompt += (
                "\n\nYour previous response failed structural validation: "
                f"{last_error}. Return one concise, complete JSON object only. "
                "The marks field must be a single integer, and every JSON string must be complete."
            )
        result = route_math_request(
            request_prompt,
            course_code,
            topic_label=topic_title,
            is_complex_proof=True,
            system_prompt=system_prompt,
        )
        model = result.get("model_used", model)
        usage = _merge_usage(usage, result.get("usage", {}))
        if not result.get("success"):
            last_error = result.get("error") or "The AI provider could not generate the adapted question."
            break

        try:
            item = robust_json_loads(str(result.get("content") or "").strip())
            if isinstance(item, list):
                item = item[0] if len(item) == 1 else None
            if not isinstance(item, dict):
                raise ValueError("response was not one question object")
            issues = _practice_question_issues([item], 1)
            if issues:
                raise ValueError("; ".join(issues))
            item["question_latex"] = normalize_math_delimiters(item["question_latex"])
            item["solution_latex"] = normalize_math_delimiters(item["solution_latex"])
            from services.prep_ingestion import assessment_question_rendering_issues

            source_issues = assessment_question_rendering_issues(item["question_latex"])
            if source_issues:
                raise ValueError("reconstructed question failed extraction validation: " + "; ".join(source_issues))
            return {"success": True, "question": item, "usage": usage, "model": model}
        except Exception as exc:
            last_error = str(exc)

    return {
        "success": False,
        "usage": usage,
        "model": model,
        "error": f"The adapted question did not pass validation: {last_error}",
    }
