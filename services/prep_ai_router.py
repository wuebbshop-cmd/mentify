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
from prep.content_rules import CONTENT_MODALITIES, legacy_course_rules, resolve_content_rules
from prep.visual_matching import map_pdf_topic_sections
from services.prep_blocks import split_markdown_table_row

logger = logging.getLogger(__name__)

_NON_MATH_LATEX_ENVIRONMENTS = {
    "center",
    "description",
    "document",
    "enumerate",
    "figure",
    "flushleft",
    "flushright",
    "itemize",
    "quote",
    "quotation",
    "table",
    "tabular",
    "tikzpicture",
    "verbatim",
}
_VISUAL_NOTE_ROUTING_VERSION = "figure-placement-server-owned-v6-numbered-siblings"
_APPROVED_VISUAL_DECISIONS = {"approved_high_confidence", "tutor_approved"}
_ADMINISTRATIVE_NOTE_PATTERN = re.compile(
    r"(?im)^\s*(?:lecturer|instructor|course coordinator|course code|course title|institutional context|"
    r"prepared by|compiled by|downloaded by|contact details|contact information|e-?mail address|"
    r"telephone number|phone number|platform identifier)\s*[:\-]"
    r"|\b(?:the\s+)?(?:course|unit|module)\s+(?:is|was)\s+(?:taught|offered|delivered)\s+(?:by|at)\b"
    r"|\b(?:course materials|document)\s+(?:are|is|were|was)\s+associated\s+with\b"
    r"|\b(?:downloaded by|not sponsored or endorsed|contact details|e-?mail address|telephone number)\b",
)
_ADMIN_COVER_SIGNAL_PATTERNS = tuple(re.compile(pattern, re.IGNORECASE) for pattern in (
    r"\blecturer\b",
    r"\binstructor\b|\bcourse coordinator\b",
    r"\buniversity\b|\bfaculty\b|\bdepartment\b",
    r"\bcourse\s+code\b|\bacademic\s+year\b|\bsemester\b",
    r"\be-?mail\b|\btelephone\b|\bphone\b|\bcontact\s+details\b",
    r"\bdownloaded\s+by\b|\bnot\s+sponsored\s+or\s+endorsed\b",
    r"\bstudocu\b|\blomoarcpsd\b",
))


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
    topic_rules = getattr(topic_obj, "content_rules", {}) if topic_obj else {}
    source_context = _approved_course_source_context(course_obj, topic_title)
    return compute_prompt_hash(
        topic_title,
        topic_summary,
        json.dumps(topic_rules or {}, ensure_ascii=True, sort_keys=True),
        _topic_content_rules_version(topic_obj),
        json.dumps(subtopics or [], ensure_ascii=True, sort_keys=True),
        json.dumps(_course_study_profile(course_obj), ensure_ascii=True, sort_keys=True),
        _VISUAL_NOTE_ROUTING_VERSION,
        hashlib.sha256(source_context.encode("utf-8", errors="ignore")).hexdigest(),
        json.dumps(
            _approved_course_source_references(course_obj, topic_title),
            ensure_ascii=True,
            sort_keys=True,
        ),
    )[:16]


NOTES_CACHE_VERSION = "markdown-katex-v16-numbered-figure-context"
NOTE_VALIDATION_STATE = "validated-v11-numbered-figure-context"
ANSWER_VALIDATION_VERSION = "answer-validation-v2-approved-sources"
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


def _topic_content_rules_version(topic_obj) -> int:
    return int(getattr(topic_obj, "content_rules_version", 0) or 0)


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


def _resolved_note_content_rules(course_obj, topic_obj=None) -> tuple[dict | None, list[str]]:
    profile = getattr(course_obj, "study_profile", None)
    profile = profile if isinstance(profile, dict) else {}
    course_rules = profile.get("content_rules") if _course_study_profile_version(course_obj) else None
    topic_rules = getattr(topic_obj, "content_rules", None) if topic_obj else None
    if not course_rules and not topic_rules:
        return None, []
    if not course_rules:
        course_rules = legacy_course_rules({"capabilities": profile.get("capabilities", {})})
    try:
        return resolve_content_rules(course_rules, topic_rules), []
    except (TypeError, ValueError) as exc:
        return None, [str(exc)]


def _note_validation_options(
    course_obj,
    topic_title: str,
    summary: str = "",
    subtopics=None,
    *,
    topic_obj=None,
) -> dict:
    content_rules, content_rule_issues = _resolved_note_content_rules(course_obj, topic_obj)
    allow_code = _note_allows_code(course_obj, topic_title, summary, subtopics)
    allow_math = _note_allows_math(course_obj)
    profile = getattr(course_obj, "study_profile", None)
    profile = profile if isinstance(profile, dict) else {}
    has_explicit_course_rules = bool(
        _course_study_profile_version(course_obj) and profile.get("content_rules")
    )
    if content_rules:
        modalities = content_rules.get("modalities", {})
        code_policy = modalities.get("code", {}).get("policy", "disallowed")
        equation_policy = modalities.get("equations", {}).get("policy", "disallowed")
        chemical_policy = modalities.get("chemical_equations", {}).get("policy", "disallowed")
        if has_explicit_course_rules:
            allow_code = code_policy in {"allowed", "required"}
            allow_math = (
                equation_policy in {"allowed", "required"}
                or chemical_policy in {"allowed", "required"}
            )
        else:
            allow_code = allow_code and code_policy != "disallowed"
            if equation_policy == "disallowed" and chemical_policy == "disallowed":
                allow_math = False
    return {
        "allow_code": allow_code,
        "allow_math": allow_math,
        "allow_chemical_equations": (
            content_rules["modalities"].get("chemical_equations", {}).get("policy") in {"allowed", "required"}
            if content_rules else bool(profile.get("capabilities", {}).get("chemical_equations"))
        ),
        "study_profile": _course_study_profile(course_obj),
        "content_rules": content_rules,
        "content_rule_issues": content_rule_issues,
        "source_references": _approved_course_source_references(course_obj, topic_title),
    }


def _note_modalities(content: str) -> set[str]:
    """Detect structured modalities without treating ordinary prose as figures."""
    detected = {"text"} if content.strip() else set()
    code_blocks = list(re.finditer(r"(?m)^```([^\n]*)\n[\s\S]*?^```[ \t]*$", content))
    if any(match.group(1).strip().lower() != "mermaid" for match in code_blocks):
        detected.add("code")

    mermaid_blocks = [
        match.group(1) for match in re.finditer(
            r"(?ms)^```mermaid\s*\n([\s\S]*?)^```[ \t]*$", content
        )
    ]
    source = re.sub(r"(?m)^```[^\n]*\n[\s\S]*?^```[ \t]*$", "", content)
    if (
        re.search(r"\$\$[\s\S]+?\$\$|(?<!\$)\$[^$\n]+\$(?!\$)", source)
        or re.search(r"\\(?:begin\{(?:aligned|align\*?|cases|matrix|pmatrix|bmatrix|gather|split|array)\}|frac\b|int\b|sum\b|prod\b|mathbb\b)", source)
    ):
        detected.add("equations")

    chemical_species = r"(?:[A-Z][a-z]?\d*(?:\([aqslg]+\))?)"
    if re.search(
        rf"{chemical_species}(?:\s*\+\s*{chemical_species})*\s*(?:<=>|⇌|↔|->|→)\s*{chemical_species}",
        source,
    ):
        detected.add("chemical_equations")

    lines = content.splitlines()
    for header, separator in zip(lines, lines[1:]):
        header_cells = split_markdown_table_row(header)
        separator_cells = split_markdown_table_row(separator)
        if (
            header_cells is not None
            and len(header_cells) > 1
            and separator_cells is not None
            and len(separator_cells) == len(header_cells)
            and all(re.fullmatch(r":?-{3,}:?", cell) for cell in separator_cells)
        ):
            detected.add("tables")
            break

    image_alts = [
        match.group(1).strip().lower()
        for match in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", content)
    ]
    if re.search(r"\\begin\{tikzpicture\}|```mermaid\s*\n[\s\S]*?\bflowchart\b", content, re.I):
        detected.add("arrow_diagrams")
    if any(re.search(r"\b(?:diagram|flowchart|flow chart)\b", alt) for alt in image_alts):
        detected.add("arrow_diagrams")
    if re.search(r"\\(?:addplot|begin\{axis\})", content) or any(
        re.search(r"\b(?:graph|plot|chart)\b", alt) for alt in image_alts
    ):
        detected.add("graphs")
    if any(re.search(r"\b(?:xychart|quadrantchart)\b", block, re.I) for block in mermaid_blocks):
        detected.add("graphs")
    return detected


def _note_code_language_issues(content: str) -> list[str]:
    allowed_languages = {
        "bash", "c", "c++", "c#", "csharp", "cpp", "css", "go", "html", "java",
        "javascript", "js", "json", "julia", "kotlin", "lua", "markdown", "mermaid",
        "php", "powershell", "ps1", "python", "py", "r", "rscript", "ruby", "rust",
        "scala", "shell", "sql", "swift", "text", "typescript", "ts", "xml", "yaml", "yml",
    }
    issues = []
    for index, match in enumerate(re.finditer(r"```([^\n`]*)\n[\s\S]*?```", content), start=1):
        language = match.group(1).strip().lower()
        if not language:
            issues.append(f"code block {index} has no declared language")
        elif language not in allowed_languages:
            issues.append(f"code block {index} uses unknown language '{language}'")
    return issues


def _approved_course_source_documents(course_obj, topic_title: str) -> list[tuple[object, bool]]:
    """Select approved lecture/revision sources using the same topic match as prompts."""
    if not course_obj:
        return []
    from prep.models import PrepDocument

    documents = PrepDocument.objects.filter(
        course=course_obj,
        stage="stage_3",
        doc_type__in=["Lecture Notes", "Revision Sheet"],
    ).exclude(extracted_text="").order_by("-updated_at", "-id")
    topic_words = [word for word in re.findall(r"[A-Za-z0-9]+", topic_title.lower()) if len(word) > 3]
    selected = []
    seen_hashes = set()
    for document in documents:
        text = str(document.extracted_text or "").strip()
        if not text:
            continue
        text_hash = hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()
        if text_hash in seen_hashes:
            continue
        document_topic = " ".join(str(document.topic_name or "").casefold().split())
        requested_topic = " ".join(str(topic_title or "").casefold().split())
        has_assigned_visual = any(
            " ".join(str((visual.extracted_content or {}).get("auto_topic") or "").casefold().split())
            == requested_topic
            for visual in document.visual_candidates.filter(status="approved").only("extracted_content")
            if isinstance(visual.extracted_content, dict)
        )
        is_topic_document = (
            document_topic == requested_topic
            or any(word in text.lower() for word in topic_words[:4])
            or has_assigned_visual
        )
        is_course_document = str(document.topic_name or "").strip().lower() == "full syllabus"
        if not is_topic_document and not is_course_document:
            continue
        seen_hashes.add(text_hash)
        selected.append((document, is_topic_document))
    return selected


def _approved_course_source_context(course_obj, topic_title: str, limit: int = 8000) -> str:
    """Return bounded excerpts from approved coursework for grounded generation."""
    selected = _approved_course_source_documents(course_obj, topic_title)
    if not selected:
        return ""
    total_length = 0
    excerpts = []
    for document, is_topic_document in selected:
        text = _strip_course_administrative_front_matter(str(document.extracted_text or "")).strip()
        excerpt_limit = min(limit - total_length, limit if is_topic_document else 5000)
        if excerpt_limit <= 0:
            break
        excerpts.append(text[:excerpt_limit])
        total_length += excerpt_limit
        if total_length >= limit:
            break
    return "\n\n--- APPROVED COURSEWORK EXCERPT ---\n\n".join(excerpts)[:limit]


def _strip_course_administrative_front_matter(text: str) -> str:
    """Remove title-page administration and contact/platform boilerplate before prompting."""
    page_header = re.compile(r"(?m)^--- Page (\d+)(?:\s+\([^\n]*\))? ---\s*$")
    instructional_cue = re.compile(
        r"\b(?:what\s+is|definition|example|formula|equation|theorem|proof|principle|theory|"
        r"concept|process|reaction|velocity|mass|force|energy|structure|function|causes|effects|"
        r"properties|method|steps?)\b",
        re.IGNORECASE,
    )

    def clean_page_body(body: str) -> str:
        kept_lines = []
        for line in body.splitlines():
            if _ADMINISTRATIVE_NOTE_PATTERN.search(line):
                continue
            if not line.strip():
                if kept_lines and kept_lines[-1]:
                    kept_lines.append("")
                continue
            if re.match(
                r"(?i)^\s*(?:lecturer|instructor|course coordinator|course code|course title|"
                r"prepared by|compiled by|author|email|e-?mail|phone|telephone|contact|faculty|"
                r"department|university|institution|academic year|semester|downloaded by)\s*[:\-]",
                line,
            ):
                continue
            kept_lines.append(line.rstrip())
        return "\n".join(kept_lines).strip()

    matches = list(page_header.finditer(text))
    if not matches:
        return clean_page_body(text)

    pages = []
    preamble = clean_page_body(text[:matches[0].start()])
    if preamble:
        pages.append(preamble)
    first_instructional_page_seen = False
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end():end]
        normalized = re.sub(r"(.)\1+", r"\1", body.casefold())
        signal_count = sum(bool(pattern.search(normalized)) for pattern in _ADMIN_COVER_SIGNAL_PATTERNS)
        if (
            not first_instructional_page_seen
            and signal_count >= 2
            and not instructional_cue.search(normalized)
        ):
            continue
        cleaned_body = clean_page_body(body)
        if cleaned_body:
            first_instructional_page_seen = True
            pages.append(f"--- Page {match.group(1)} ---\n{cleaned_body}")
    return "\n\n".join(pages)


_NUMBERED_FIGURE_CONTEXT_RE = re.compile(
    r"(?i)\b(?:figure|fig\.?|graph|diagram|chart)\s*(\d+)\s*[:.)-]\s*"
)


def _scope_numbered_sibling_figure_contexts(visuals: list[dict]) -> None:
    if len(visuals) < 2 or any(
        not isinstance(visual.get("bbox"), (list, tuple)) or len(visual["bbox"]) != 4
        for visual in visuals
    ):
        return

    contexts = {
        " ".join(str(visual.get(key) or "").split())
        for visual in visuals
        for key in ("context_before", "context_after")
        if visual.get(key)
    }
    for context in sorted(contexts, key=len, reverse=True):
        matches = list(_NUMBERED_FIGURE_CONTEXT_RE.finditer(context))
        numbers = [int(match.group(1)) for match in matches]
        if numbers != list(range(1, len(visuals) + 1)):
            continue

        reading_order = sorted(visuals, key=lambda visual: (visual["bbox"][1], visual["bbox"][0]))
        for index, visual in enumerate(reading_order):
            start = matches[index].start()
            end = matches[index + 1].start() if index + 1 < len(matches) else len(context)
            visual["figure_context"] = context[start:end].strip()
        return


def _approved_course_source_references(course_obj, topic_title: str, *, limit: int = 40) -> list[dict]:
    """Return page and approved-figure references for the source excerpts used in notes."""
    page_header = re.compile(r"(?m)^--- Page (\d+)(?:\s+\([^\n]*\))? ---\s*$")
    references = []
    topics = list(course_obj.topics.filter(is_active=True).order_by("order", "id")) if course_obj else []
    requested_topic = " ".join(str(topic_title or "").casefold().split())
    remaining_context_page_budget = limit
    for document, _is_topic_document in _approved_course_source_documents(course_obj, topic_title):
        text = str(document.extracted_text or "")
        matches = list(page_header.finditer(text))
        section_pages, ambiguous_section_pages = map_pdf_topic_sections(text, topics)
        document_topic = " ".join(str(document.topic_name or "").casefold().split())
        page_texts = {}
        if matches:
            for index, match in enumerate(matches):
                end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
                page_texts[int(match.group(1))] = text[match.end():end]
        assigned_visuals = {}
        if getattr(document, "pk", None):
            for visual in document.visual_candidates.filter(status="approved").select_related(
                "reviewed_topic", "reviewed_by"
            ).order_by("page_number", "id"):
                metadata = visual.extracted_content if isinstance(visual.extracted_content, dict) else {}
                decision = metadata.get("auto_decision")
                tutor_approved = (
                    decision == "tutor_approved"
                    and visual.reviewed_topic_id
                    and visual.reviewed_topic.course_id == document.course_id
                    and visual.reviewed_by_id
                    and visual.reviewed_at
                )
                assigned_title = visual.reviewed_topic.title if tutor_approved else metadata.get("auto_topic")
                assigned_topic = " ".join(str(assigned_title or "").casefold().split())
                if (
                    assigned_topic != requested_topic
                    or (decision not in _APPROVED_VISUAL_DECISIONS and not tutor_approved)
                    or (visual.page_number in ambiguous_section_pages and not tutor_approved)
                ):
                    continue
                section_topic = section_pages.get(visual.page_number)
                if (
                    section_topic
                    and " ".join(str(section_topic.title).casefold().split()) != requested_topic
                    and not tutor_approved
                ):
                    continue
                crop_name = visual.crop.name if visual.crop else ""
                try:
                    crop_url = visual.crop.url if visual.crop else ""
                except (ValueError, OSError):
                    crop_url = ""
                if not crop_name or not crop_url:
                    continue
                try:
                    context_crop_url = visual.context_crop.url if visual.context_crop else ""
                except (ValueError, OSError):
                    context_crop_url = ""
                assigned_visuals.setdefault(visual.page_number, []).append({
                    "visual_id": str(visual.pk),
                    "page_number": visual.page_number,
                    "visual_type": visual.visual_type,
                    "crop": crop_name,
                    "crop_url": crop_url,
                    "bbox": visual.bbox,
                    "caption": metadata.get("caption", ""),
                    "labels": visual.labels if isinstance(visual.labels, list) else [],
                    "auto_topic": metadata.get("auto_topic", ""),
                    "auto_decision": metadata.get("auto_decision", ""),
                    "auto_match_method": metadata.get("auto_match_method", "page_context"),
                    "auto_match_terms": metadata.get("auto_match_terms", []),
                    "context_before": metadata.get("context_before", ""),
                    "context_after": metadata.get("context_after", ""),
                    "context_crop_url": context_crop_url,
                })

            for page_visuals in assigned_visuals.values():
                _scope_numbered_sibling_figure_contexts(page_visuals)

        if document_topic == requested_topic:
            pages = {
                page_number
                for page_number in page_texts
                if page_number not in ambiguous_section_pages
                and (
                    page_number not in section_pages
                    or " ".join(str(section_pages[page_number].title).casefold().split()) == requested_topic
                )
            }
        else:
            pages = {
                page_number
                for page_number, section_topic in section_pages.items()
                if " ".join(str(section_topic.title).casefold().split()) == requested_topic
            }
        pages.update(assigned_visuals)
        visual_pages = sorted(assigned_visuals)
        remaining_pages = sorted(pages - set(visual_pages))
        context_pages = remaining_pages[:remaining_context_page_budget]
        remaining_context_page_budget -= len(context_pages)
        pages = visual_pages + context_pages
        if not pages and not matches:
            pages = [None]

        if not pages:
            references.append({
                "document_id": str(document.pk),
                "source_sha256": document.file_sha256 or "",
                "page_number": None,
                "visuals": [],
            })
            continue

        for page_number in pages:
            references.append({
                "document_id": str(document.pk),
                "source_sha256": document.file_sha256 or "",
                "page_number": page_number,
                "visuals": assigned_visuals.get(page_number, []),
            })
    return references


_APPROVED_VISUAL_MARKER_RE = re.compile(r"\[\[VISUAL:([A-Za-z0-9-]+)\]\]")


def _source_figure_caption(visual: dict) -> str:
    candidates = [
        visual.get("figure_context"),
        visual.get("caption"),
        visual.get("context_after"),
        visual.get("context_before"),
    ]
    for candidate in candidates:
        caption = re.sub(r"\s+", " ", str(candidate or "")).strip()
        if not caption or re.search(r"(?i)downloaded by|lOMoARcPSD|scan to|studocu|coursehero", caption):
            continue
        caption = re.split(r"(?<=[.!?])\s+", caption, maxsplit=1)[0]
        caption = re.sub(r"^\W*\d+\s+", "", caption).strip(" -|")
        if len(caption.split()) >= 4 and not re.search(r"\(\s*(?:and\s*)?\)", caption, re.IGNORECASE):
            return caption[:220]
    return str(visual.get("visual_type") or "Source figure").replace("_", " ").title()


def _approved_visual_manifest(source_references: list[dict] | None, *, limit: int | None = None) -> list[dict]:
    """Return a short list of approved crop records that have a renderable URL."""
    manifest = []
    for reference in source_references or []:
        visuals = reference.get("visuals", [])
        _scope_numbered_sibling_figure_contexts(visuals)
        for visual in visuals:
            if not isinstance(visual, dict) or not visual.get("visual_id") or not visual.get("crop_url"):
                continue
            manifest.append({
                "id": str(visual["visual_id"]),
                "type": visual.get("visual_type", "unclassified"),
                "page": visual.get("page_number"),
                "crop_url": visual.get("crop_url", ""),
                "caption": _source_figure_caption(visual),
                "labels": visual.get("labels", []),
                "auto_topic": visual.get("auto_topic", ""),
                "auto_decision": visual.get("auto_decision", ""),
                "auto_match_method": visual.get("auto_match_method", "page_context"),
                "auto_match_terms": visual.get("auto_match_terms", []),
                "context_before": visual.get("context_before", ""),
                "context_after": visual.get("context_after", ""),
                "placement_context": visual.get("figure_context", ""),
                "context_crop_url": visual.get("context_crop_url", ""),
                "required": (
                    bool(visual.get("auto_topic"))
                    and visual.get("auto_decision") in _APPROVED_VISUAL_DECISIONS
                ),
                "marker": f"[[VISUAL:{visual['visual_id']}]]",
            })
            if limit is not None and len(manifest) >= limit:
                return manifest
    return manifest


def _insert_required_visual_markers(content: str, manifest: list[dict]) -> str:
    """Place assigned source figures beside the generated paragraph matching their context."""
    for visual in manifest:
        marker = visual.get("marker")
        if marker:
            content = content.replace(marker, "")
        crop_url = str(visual.get("crop_url") or "")
        if crop_url:
            content = re.sub(
                r"!\[[^\]]*\]\(" + re.escape(crop_url) + r"\)",
                "",
                content,
            )
    content = re.sub(r"\n[ \t]*\n(?:[ \t]*\n)+", "\n\n", content)
    paragraphs = [
        match for match in re.finditer(r"(?ms)(?:^|\n\s*\n)([^\n][\s\S]*?)(?=\n\s*\n|$)", content)
        if match.group(1).strip() and not match.group(1).lstrip().startswith("!")
    ]
    required_visuals = [
        visual for visual in manifest
        if visual.get("required") and visual.get("marker")
    ]
    directional_references = [
        paragraph for paragraph in paragraphs
        if _DIRECTIONAL_VISUAL_REFERENCE_PATTERN.search(paragraph.group(1))
    ]
    use_distinct_reference_targets = len(directional_references) >= len(required_visuals)
    used_reference_targets = set()
    insertions = []
    generic = {"figure", "graph", "diagram", "curve", "source", "page", "shows", "shown", "this", "that"}
    for visual in manifest:
        marker = visual.get("marker")
        if not visual.get("required") or not marker:
            continue
        if visual.get("placement_context"):
            context_text = " ".join((
                visual.get("placement_context", ""),
                " ".join(visual.get("labels", [])),
            ))
        else:
            context_text = " ".join((
                " ".join(visual.get("auto_match_terms", [])),
                visual.get("caption", ""),
                " ".join(visual.get("labels", [])),
                visual.get("context_before", ""),
                visual.get("context_after", ""),
            ))
        context_terms = {
            token.casefold() for token in re.findall(r"[A-Za-z0-9]+", context_text)
            if len(token) > 3 and token.casefold() not in generic
        }
        best = None
        best_score = 0
        paragraph_scores = []
        for paragraph in paragraphs:
            paragraph_terms = {
                token.casefold() for token in re.findall(r"[A-Za-z0-9]+", paragraph.group(1))
            }
            score = len(context_terms & paragraph_terms)
            paragraph_scores.append((paragraph, score))
            if score > best_score:
                best = paragraph
                best_score = score
        if use_distinct_reference_targets:
            reference_matches = [
                (paragraph, score)
                for paragraph, score in paragraph_scores
                if paragraph in directional_references
                and paragraph.start() not in used_reference_targets
                and score > 0
            ]
            if reference_matches:
                best, _ = max(reference_matches, key=lambda item: item[1])
                used_reference_targets.add(best.start())
        if best and best_score:
            insertions.append((best.end(), f"\n\n{marker}"))
    for position, insertion in sorted(insertions, reverse=True):
        content = content[:position] + insertion + content[position:]
    return content


def _dedupe_approved_visual_images(content: str, source_references: list[dict] | None) -> str:
    """Keep each approved source crop at most once in a note level."""
    approved_urls = {
        visual.get("crop_url")
        for reference in source_references or []
        for visual in reference.get("visuals", [])
        if isinstance(visual, dict) and visual.get("crop_url")
    }
    seen = set()

    def replace(match):
        image_url = match.group(2).strip()
        if image_url not in approved_urls:
            return match.group(0)
        if image_url in seen:
            return ""
        seen.add(image_url)
        return match.group(0)

    content = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace, str(content or ""))
    return re.sub(r"\n{3,}", "\n\n", content)


def _normalize_approved_visual_captions(content: str, source_references: list[dict] | None) -> str:
    captions = {}
    for reference in source_references or []:
        for visual in reference.get("visuals", []):
            if not isinstance(visual, dict) or not visual.get("crop_url"):
                continue
            caption = _source_figure_caption(visual)
            if caption:
                captions[visual["crop_url"]] = caption

    def replace(match):
        caption = captions.get(match.group(2).strip())
        if not caption:
            return match.group(0)
        safe_caption = re.sub(r"[\r\n]+", " ", caption).replace("]", "\\]")
        return f"![{safe_caption}]({match.group(2)})"

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace, str(content or ""))


def _resolve_approved_visual_markers(content: str, source_references: list[dict] | None) -> str:
    """Replace model figure tokens only with crops present in the approved source manifest."""
    approved = {
        str(visual.get("visual_id")): (reference, visual)
        for reference in source_references or []
        for visual in reference.get("visuals", [])
        if isinstance(visual, dict) and visual.get("visual_id") and visual.get("crop_url")
    }

    def replace(match):
        approved_entry = approved.get(match.group(1))
        if not approved_entry:
            return match.group(0)
        reference, visual = approved_entry
        crop_url = str(visual.get("crop_url") or "").strip()
        if not crop_url:
            return match.group(0)
        caption = _source_figure_caption(visual)
        if not caption:
            labels = visual.get("labels") if isinstance(visual.get("labels"), list) else []
            caption = ", ".join(str(label) for label in labels[:6]) or str(visual.get("visual_type") or "Source figure").title()
        page_number = visual.get("page_number") or reference.get("page_number")
        if page_number:
            caption += f" (source page {page_number})"
        caption = re.sub(r"[\r\n]+", " ", caption).replace("]", "\\]")
        safe_url = crop_url.replace(" ", "%20").replace(")", "%29")
        return f"![{caption}]({safe_url})"

    return _APPROVED_VISUAL_MARKER_RE.sub(replace, str(content or ""))


def _markdown_table_issues(content: str) -> list[str]:
    """Find truncated or structurally incomplete Markdown tables."""
    lines = content.splitlines()
    issues: list[str] = []
    index = 0

    while index < len(lines) - 1:
        header_cells = split_markdown_table_row(lines[index])
        separator_cells = split_markdown_table_row(lines[index + 1])
        is_header = header_cells is not None and len(header_cells) > 1
        is_separator = (
            separator_cells is not None
            and len(separator_cells) > 1
            and all(re.fullmatch(r":?-{3,}:?", cell) for cell in separator_cells)
        )
        if not (is_header and is_separator):
            index += 1
            continue

        expected_cells = len(header_cells)
        if len(separator_cells) != expected_cells:
            issues.append(f"incomplete Markdown table separator near line {index + 2}")
        index += 2
        while index < len(lines):
            row = lines[index].strip()
            if not row:
                index += 1
                continue
            row_cells = split_markdown_table_row(row)
            if not row.startswith("|"):
                break
            if row_cells is None:
                issues.append(f"incomplete Markdown table row near line {index + 1}")
            elif len(row_cells) != expected_cells:
                issues.append(
                    f"incomplete Markdown table row near line {index + 1} "
                    f"(expected {expected_cells} cells, found {len(row_cells)})"
                )
            index += 1

    return issues


def _figure_reference_issues(content: str) -> list[str]:
    """Reject figure maps with blank markers and prose containing empty figure placeholders."""
    lines = str(content or "").splitlines()
    issues = []
    index = 0
    while index < len(lines) - 1:
        headers = split_markdown_table_row(lines[index])
        if headers is None:
            index += 1
            continue
        marker_columns = [
            column for column, header in enumerate(headers)
            if re.search(r"\bfigure\s+(?:marker|reference|id)\b", header, re.IGNORECASE)
        ]
        if not marker_columns:
            index += 1
            continue
        separator = split_markdown_table_row(lines[index + 1])
        if not separator or not all(re.fullmatch(r":?-{3,}:?", cell) for cell in separator):
            index += 1
            continue
        marker_column = marker_columns[0]
        index += 2
        while index < len(lines):
            row = lines[index].strip()
            if not row:
                index += 1
                continue
            if not row.startswith("|"):
                break
            cells = split_markdown_table_row(row)
            marker = cells[marker_column].strip() if cells and marker_column < len(cells) else ""
            if not re.search(r"!\[[^\]]*\]\([^)]+\)|\[\[VISUAL:[^\]]+\]\]", marker):
                issues.append(f"figure marker table row has no figure for line {index + 1}")
            index += 1

    if re.search(r"\b(?:figures?|diagrams?|graphs?)\s*\(\s*(?:and\s*)?\)", content, re.IGNORECASE):
        issues.append("figure summary contains empty reference placeholders")
    return issues


_MISSING_VISUAL_REFERENCE_ISSUE = (
    "notes refer to a visual instead of explaining the concept independently"
)
_VISUAL_REFERENCE_PATTERN = re.compile(
    r"\b(?:as\s+(?:shown|illustrated|depicted|seen)\s+(?:(?:in|by)\s+)?(?:the\s+)?"
    r"(?:figure|diagram|graph|plot|chart|table)"
    r"|(?:see|refer\s+to)\s+(?:the\s+)?(?:figure|diagram|graph|plot|chart|table|fig\.?\s*\d+)"
    r"|(?:in|from|using)\s+(?:the\s+|this\s+|that\s+|following\s+|above\s+|below\s+)?"
    r"(?:figure|diagram|graph|plot|chart|table)"
    r"|(?:figure|diagram|graph|plot|chart|table)(?:\s+\d+)?\s+"
    r"(?:above|below|on\s+the\s+(?:left|right)|shows|illustrates|depicts|indicates)"
    r"|(?:following|next)\s+(?:the\s+)?(?:figure|diagram|graph|plot|chart|table)"
    r"|(?:cannot|can't|unable\s+to|not\s+able\s+to)\s+see\s+"
    r"(?:the\s+)?(?:figure|diagram|graph|plot|chart|table))",
    re.IGNORECASE,
)
_DIRECTIONAL_VISUAL_REFERENCE_PATTERN = re.compile(
    r"\b(?:as\s+(?:shown|illustrated|depicted|seen)\s+(?:in\s+)?(?:the\s+)?"
    r"(?:figure|diagram|graph|plot|chart|table)"
    r"|(?:figure|diagram|graph|plot|chart|table)\s+(?:above|below|on\s+the\s+(?:left|right))"
    r"|(?:following|next)\s+(?:the\s+)?(?:figure|diagram|graph|plot|chart|table))",
    re.IGNORECASE,
)


def _unavailable_visual_reference_issues(content: str) -> list[str]:
    """Reject figure callouts so lesson prose remains complete without images."""
    source = re.sub(r"```[\s\S]*?```", "", str(content or ""))
    if _VISUAL_REFERENCE_PATTERN.search(source):
        return [_MISSING_VISUAL_REFERENCE_ISSUE]
    return []


def _course_administrative_metadata_issues(content: str) -> list[str]:
    """Keep lecturer, contact, and document-distribution metadata out of study notes."""
    source = re.sub(r"```[\s\S]*?```", "", str(content or ""))
    if _ADMINISTRATIVE_NOTE_PATTERN.search(source):
        return ["notes contain course-administration metadata instead of study content"]
    return []


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
    if re.search(r"\[\[VISUAL:[^\]]*\]\]", content):
        issues.append("visual marker does not resolve to an approved source crop")
    if re.search(r"<\s*(?:img|picture|source|svg|iframe|object|embed)\b", content, re.IGNORECASE):
        issues.append("raw HTML visual markup is not allowed; use an approved visual marker")
    if re.search(r"```mermaid\b|\\begin\{tikzpicture\}|\\begin\{axis\}", content, re.IGNORECASE):
        issues.append("generated diagram markup is not supported without an approved source crop")
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
    issues.extend(_figure_reference_issues(content))
    issues.extend(_unavailable_visual_reference_issues(content))
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


def _parse_topic_note_repair_patch(raw_response: str) -> dict:
    """Parse a JSON repair patch, tolerating a short model preamble or code fence."""
    raw_response = str(raw_response or "").strip()
    if not raw_response:
        raise ValueError("repair model returned an empty response")

    candidates = [raw_response]
    object_start = raw_response.find("{")
    object_end = raw_response.rfind("}")
    if object_start >= 0 and object_end > object_start:
        candidates.append(raw_response[object_start:object_end + 1])

    for candidate in candidates:
        try:
            patch = robust_json_loads(candidate)
        except ValueError:
            continue
        if isinstance(patch, dict):
            old_block = patch.get("old_block")
            new_block = patch.get("new_block")
            if isinstance(old_block, str) and isinstance(new_block, str):
                return patch

    raise ValueError("repair response did not contain a JSON object with string old_block and new_block fields")


def _note_needs_section_regeneration(issues: list[str]) -> bool:
    """Identify failures that cannot be fixed with an old_block/new_block patch."""
    return any(
        issue.startswith("missing section")
        or issue.startswith("review section ")
        or issue.startswith("figure marker table row has no figure")
        or issue == _MISSING_VISUAL_REFERENCE_ISSUE
        or issue == "figure summary contains empty reference placeholders"
        or issue in {
            "final section has insufficient content",
            "code block is not allowed for this topic",
        }
        for issue in issues
    )


def _review_topic_note_content(topic_obj, level: str, content: str) -> dict:
    """Use an independent source-grounded model to flag likely factual errors."""
    source_excerpt = _approved_course_source_context(topic_obj.course, topic_obj.title)
    if not source_excerpt:
        return {
            "success": True,
            "issues": [],
            "usage": {},
            "model_used": getattr(settings, "DEEPSEEK_REASONER_MODEL", "deepseek-v4-pro"),
            "skipped": "No approved source excerpt is available for independent comparison.",
        }

    model = getattr(settings, "DEEPSEEK_NOTE_REVIEW_MODEL", None) or getattr(
        settings, "DEEPSEEK_REASONER_MODEL", "deepseek-v4-pro"
    )
    result = call_deepseek(
        [
            {
                "role": "system",
                "content": (
                    "You are an independent fact-checker for academic study notes. Compare only "
                    "the supplied notes with the approved course source. Report clear factual "
                    "contradictions, unsupported material claims, or materially incorrect formulas. "
                    "Do not report style preferences, omissions that are not required, or claims "
                    "that are merely worded differently. Return exactly one JSON object: "
                    '{"issues":[{"section":1,"severity":"error","description":"...","source_evidence":"..."}]}. '
                    "Use an empty issues array when the notes are supported. Report at most eight findings. "
                    "Each issue must identify one numbered section and quote exact concise source evidence. "
                    "Do not rewrite the notes."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Course: {topic_obj.course.code}\nTopic: {topic_obj.title}\nLevel: {level}\n"
                    "APPROVED COURSE MATERIAL:\n"
                    f"{source_excerpt}\n\n"
                    "NOTES TO REVIEW:\n"
                    f"{content[:40000]}"
                ),
            },
        ],
        model=model,
        max_tokens=2500,
        auto_continue=False,
        thinking_enabled=False,
    )
    if not result.get("success") or not result.get("content"):
        return {
            "success": False,
            "issues": [],
            "usage": result.get("usage", {}),
            "model_used": result.get("model_used") or model,
            "error": result.get("error") or "The independent note review returned no result.",
            "raw_response": str(result.get("content") or "")[:4000],
        }

    try:
        report = robust_json_loads(result["content"])
    except ValueError as exc:
        return {
            "success": False,
            "issues": [],
            "usage": result.get("usage", {}),
            "model_used": result.get("model_used") or model,
            "error": f"The independent review response was not valid JSON: {exc}",
            "raw_response": str(result.get("content") or "")[:4000],
        }
    raw_issues = report.get("issues") if isinstance(report, dict) else None
    if not isinstance(raw_issues, list):
        return {
            "success": False,
            "issues": [],
            "usage": result.get("usage", {}),
            "model_used": result.get("model_used") or model,
            "error": "The independent review response did not contain an issues list.",
            "raw_response": str(result.get("content") or "")[:4000],
        }
    if len(raw_issues) > 8:
        return {
            "success": False,
            "issues": [],
            "usage": result.get("usage", {}),
            "model_used": result.get("model_used") or model,
            "error": "The independent review returned more than eight findings.",
            "raw_response": str(result.get("content") or "")[:4000],
        }

    issues = []
    note_sections = {
        int(match.group(1))
        for match in re.finditer(r"(?m)^\s*##\s+(\d+)\.", content)
    }
    normalized_source = re.sub(r"\s+", " ", source_excerpt).casefold()
    for item in raw_issues[:8]:
        if not isinstance(item, dict):
            return {
                "success": False,
                "issues": [],
                "usage": result.get("usage", {}),
                "model_used": result.get("model_used") or model,
                "error": "The independent review returned a malformed issue entry.",
                "raw_response": str(result.get("content") or "")[:4000],
            }
        section = item.get("section")
        description = str(item.get("description") or "").strip()
        evidence = str(item.get("source_evidence") or "").strip()
        severity = str(item.get("severity") or "").strip().lower()
        normalized_evidence = re.sub(r"\s+", " ", evidence).casefold()
        if (
            type(section) is not int
            or section not in note_sections
            or severity not in {"error", "critical"}
            or not description
            or not evidence
            or normalized_evidence not in normalized_source
        ):
            return {
                "success": False,
                "issues": [],
                "usage": result.get("usage", {}),
                "model_used": result.get("model_used") or model,
                "error": "The independent review issue had an invalid section, severity, description, or source evidence.",
                "raw_response": str(result.get("content") or "")[:4000],
            }
        issues.append(
            f"review section {section}: {description[:500]} "
            f"(source: {evidence[:500]})"
        )
    return {
        "success": True,
        "issues": issues,
        "usage": result.get("usage", {}),
        "model_used": result.get("model_used") or model,
        "report": report,
        "raw_response": str(result.get("content") or "")[:4000],
    }


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
    for issue in issues:
        review_section = re.match(r"review section (\d+):", issue)
        if review_section:
            section_issues.setdefault(int(review_section.group(1)), []).append(issue)

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
        topic_obj=topic_obj,
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
    repair_usage = {}
    for _ in range(2):
        repair.attempts += 1
        repair.validation_issues = issues
        repair.save(update_fields=["attempts", "validation_issues", "updated_at"])
        working_headings = list(re.finditer(r"(?m)^\s*##\s+(\d+)\.[^\n]*", working_content))
        working_first = next(
            (heading for heading in working_headings if int(heading.group(1)) == first_number),
            None,
        )
        working_next = next(
            (heading for heading in working_headings if int(heading.group(1)) > last_number),
            None,
        )
        if working_first:
            affected_content = working_content[
                working_first.start():working_next.start() if working_next else len(working_content)
            ]
        else:
            affected_content = working_content
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
            "Explain every concept fully in plain prose so it remains understandable without images. "
            "Never refer to a figure, diagram, graph, chart, table, or image in the prose, including "
            "phrases such as 'as shown above', 'in the diagram', or 'see Figure 1', even when an image "
            "is included. Approved source images may remain beside the explanation but must not be "
            "required to understand it. Never invent image URLs or figure IDs.\n"
            + code_instruction
            + "Validation errors:\n" + json.dumps(issues) + "\n"
            + "Approved coursework source:\n" + source_excerpt + "\n"
            "Existing affected note sections:\n" + affected_content[:12000]
        )
        result = route_math_request(
            prompt,
            topic_obj.course.code,
            topic_label=topic_obj.title,
            is_complex_proof=False,
            thinking_enabled=False,
            model_override=getattr(settings, "DEEPSEEK_REASONER_MODEL", "deepseek-v4-pro"),
        )
        repair_log = repair.repair_log if isinstance(repair.repair_log, list) else []
        repair_log.append({
            "stage": "section_regeneration",
            "attempt": repair.attempts,
            "model": result.get("model_used") or getattr(settings, "DEEPSEEK_REASONER_MODEL", "deepseek-v4-pro"),
            "issues": issues[:20],
            "response": str(result.get("content") or "")[:2000],
            "error": str(result.get("error") or "")[:1000],
        })
        repair.repair_log = repair_log[-10:]
        repair.save(update_fields=["repair_log", "updated_at"])
        if not result.get("success") or not result.get("content"):
            continue
        repair_usage = _merge_usage(repair_usage, result.get("usage", {}))
        replacement = normalize_math_delimiters(result["content"]).strip()
        candidate = prefix.rstrip() + "\n\n" + replacement
        if suffix:
            candidate += "\n\n" + suffix.lstrip()
        visual_manifest = _approved_visual_manifest(validation_options["source_references"])
        candidate = _insert_required_visual_markers(candidate, visual_manifest)
        candidate = _resolve_approved_visual_markers(candidate, validation_options["source_references"])
        candidate = _dedupe_approved_visual_images(candidate, validation_options["source_references"])
        candidate = _normalize_approved_visual_captions(candidate, validation_options["source_references"])
        candidate_issues = _note_completion_issues(
            candidate,
            topic_obj.title,
            **validation_options,
        )
        review = None
        if not candidate_issues:
            review = _review_topic_note_content(topic_obj, level, candidate)
            repair_usage = _merge_usage(repair_usage, review.get("usage", {}))
            repair_log = repair.repair_log if isinstance(repair.repair_log, list) else []
            repair_log.append({
                "stage": "independent_review",
                "attempt": repair.attempts,
                "model": review.get("model_used", ""),
                "issues": review.get("issues", [])[:8],
                "response": str(review.get("raw_response") or "")[:4000],
                "error": str(review.get("error") or "")[:1000],
            })
            repair.repair_log = repair_log[-10:]
            repair.save(update_fields=["repair_log", "updated_at"])
            if not review.get("success") or review.get("skipped"):
                candidate_issues = [
                    "independent review failed: "
                    + str(
                        review.get("error")
                        or review.get("skipped")
                        or "review provider returned an unsuccessful response"
                    )
                ]
            else:
                candidate_issues.extend(review.get("issues", []))
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
            "topic_content_rules_version": _topic_content_rules_version(topic_obj),
            "source_references": validation_options["source_references"],
            "source_signature": source_signature,
            "review_status": (
                "skipped_no_source"
                if review and review.get("skipped")
                else "passed"
            ),
            "review_model": (review or {}).get("model_used", ""),
            "reviewed_at": timezone.now().isoformat(),
            "review_report": (review or {}).get("report") or {
                "skipped": (review or {}).get("skipped", "")
            },
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
            "usage": repair_usage,
            "model": result.get("model_used", "deepseek-chat"),
            "review_status": (
                "skipped_no_source"
                if review and review.get("skipped")
                else "passed"
            ),
            "source_references": validation_options["source_references"],
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
        if environment in _NON_MATH_LATEX_ENVIRONMENTS:
            continue
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
    allow_chemical_equations: bool | None = None,
    study_profile: dict | None = None,
    content_rules: dict | None = None,
    content_rule_issues: list[str] | None = None,
    source_references: list[dict] | None = None,
) -> list[str]:
    """Detect incomplete note output before it is displayed or cached."""
    if not isinstance(content, str) or not content.strip():
        return ["empty content"]

    issues: list[str] = []
    issues.extend(f"approved content rules are invalid: {issue}" for issue in (content_rule_issues or []))
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
    issues.extend(_course_administrative_metadata_issues(content))
    issues.extend(_note_code_language_issues(content))
    if allow_code is False and re.search(r"```(?!mermaid\b)[A-Za-z0-9_+-]*\s*\n", content, re.IGNORECASE):
        issues.append("code block is not allowed for this topic")
    if allow_math is False:
        math_source = re.sub(r"```[\s\S]*?```", "", content)
        if re.search(r"\$\$?|\\\\\[|\\\\\(|\\\\begin\{|\\\\(?:frac|int|sum|prod|lim|mathbb)", math_source):
            issues.append("math notation is not supported by the approved course notes")
    if allow_chemical_equations is False and "chemical_equations" in _note_modalities(content):
        issues.append("chemical equations are not supported by the approved course notes")
    if content_rules:
        detected_modalities = _note_modalities(content)
        source_visuals_by_url = {
            visual.get("crop_url"): visual
            for reference in (source_references or [])
            for visual in reference.get("visuals", [])
            if isinstance(visual, dict) and visual.get("crop_url")
        }
        for image in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", content):
            visual = source_visuals_by_url.get(image.group(1).strip())
            if not visual:
                continue
            visual_modality = {
                "graph": "graphs",
                "diagram": "arrow_diagrams",
                "table": "tables",
            }.get(visual.get("visual_type"))
            if visual_modality:
                detected_modalities.add(visual_modality)
        modalities = content_rules.get("modalities", {})
        for modality in CONTENT_MODALITIES:
            policy = modalities.get(modality, {}).get("policy", "disallowed")
            if policy == "disallowed" and modality in detected_modalities:
                issues.append(f"{modality} modality is disallowed by approved course/topic rules")
            elif policy == "required" and modality not in detected_modalities:
                issues.append(f"required {modality} modality is missing from the notes")

    detected_modalities = _note_modalities(content)
    if detected_modalities & {"graphs", "arrow_diagrams"} and not source_references:
        issues.append("visual modality has no approved source-page provenance")
    for image in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", content):
        image_path = image.group(1).strip()
        approved_crops = {
            visual.get("crop_url")
            for reference in (source_references or [])
            for visual in reference.get("visuals", [])
            if isinstance(visual, dict) and visual.get("crop_url")
        }
        if image_path not in approved_crops:
            issues.append("embedded figure does not reference an approved source crop")
    required_visuals = {
        str(visual.get("visual_id")): str(visual.get("crop_url"))
        for reference in (source_references or [])
        for visual in reference.get("visuals", [])
        if isinstance(visual, dict)
        and visual.get("visual_id")
        and visual.get("crop_url")
        and visual.get("auto_topic")
        and visual.get("auto_decision") in _APPROVED_VISUAL_DECISIONS
    }
    embedded_urls = {
        match.group(1).strip()
        for match in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", content)
    }
    missing_visual_ids = [
        visual_id for visual_id, crop_url in required_visuals.items()
        if crop_url not in embedded_urls
    ]
    if missing_visual_ids:
        issues.append(
            "required approved source visual missing: " + ", ".join(sorted(missing_visual_ids))
        )
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
    allow_chemical_equations: bool | None = None,
    study_profile: dict | None = None,
    content_rules: dict | None = None,
    content_rule_issues: list[str] | None = None,
    source_references: list[dict] | None = None,
) -> dict | None:
    """Validate an unmarked legacy note once, then persist its publication state."""
    content = repair_json_escaped_latex_newlines(
        str(payload.get("content") or payload.get("notes") or "")
    ).strip()
    original_content = content
    manifest = _approved_visual_manifest(source_references)
    content = _insert_required_visual_markers(content, manifest)
    content = _resolve_approved_visual_markers(content, source_references)
    content = _dedupe_approved_visual_images(content, source_references)
    content = _normalize_approved_visual_captions(content, source_references).strip()
    if not content or _note_completion_issues(
        content,
        topic_title,
        allow_code=allow_code,
        allow_math=allow_math,
        allow_chemical_equations=allow_chemical_equations,
        study_profile=study_profile,
        content_rules=content_rules,
        content_rule_issues=content_rule_issues,
        source_references=source_references,
    ):
        return None

    published_payload = dict(payload)
    published_payload["content"] = content
    published_payload["level"] = payload.get("level") or "level_2"
    published_payload["validation_state"] = NOTE_VALIDATION_STATE
    published_payload["validated_at"] = timezone.now().isoformat()
    published_payload["source_references"] = source_references or []
    published_payload["study_profile_version"] = _course_study_profile_version(entry.topic.course) if entry.topic else 0
    published_payload["topic_content_rules_version"] = _topic_content_rules_version(entry.topic) if entry.topic else 0
    if content != original_content:
        from services.prep_blocks import parse_markdown_to_blocks

        published_payload["blocks"] = parse_markdown_to_blocks(content)
    if entry.topic:
        published_payload["source_signature"] = _topic_notes_cache_signature(
            entry.topic.course,
            entry.topic,
            entry.topic.title,
            entry.topic.subtopics,
        )
    entry.payload = published_payload
    entry.save(update_fields=["payload", "updated_at"])
    return published_payload


def get_published_topic_note_levels(topic_obj, *, validated_only: bool = False) -> dict[str, str]:
    """Return all shared, published note levels without invoking AI generation."""
    if not topic_obj:
        return {}

    from prep.models import PrepContentCache

    levels: dict[str, str] = {}
    source_signature = _topic_notes_cache_signature(
        topic_obj.course,
        topic_obj,
        topic_obj.title,
        topic_obj.subtopics,
    )
    entries = PrepContentCache.objects.filter(
        content_type="topic_notes",
        topic=topic_obj,
    ).order_by("-updated_at", "-id")
    for entry in entries:
        payload = _cache_payload_as_dict(entry.payload)
        if not payload:
            continue
        if payload.get("review_status") == "skipped_no_source":
            continue
        level = payload.get("level") or "level_2"
        if level not in {"level_1", "level_2", "level_3"} or level in levels:
            continue
        payload_signature = str(payload.get("source_signature") or "")
        payload_validation_state = str(payload.get("validation_state") or "")
        if payload_validation_state:
            if payload_validation_state != NOTE_VALIDATION_STATE or payload_signature != source_signature:
                continue
        elif validated_only:
            continue
        if int(payload.get("study_profile_version", 0) or 0) != _course_study_profile_version(topic_obj.course):
            continue
        if int(payload.get("topic_content_rules_version", 0) or 0) != _topic_content_rules_version(topic_obj):
            continue
        validation_options = _note_validation_options(
            topic_obj.course,
            topic_obj.title,
            topic_obj.summary,
            topic_obj.subtopics,
            topic_obj=topic_obj,
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
            payload["topic_content_rules_version"] = _topic_content_rules_version(topic_obj)
            payload["source_references"] = _approved_course_source_references(topic_obj.course, topic_obj.title)
            payload["source_signature"] = source_signature
            entry.payload = payload
            entry.save(update_fields=["payload", "updated_at"])
        elif not payload.get("level"):
            payload = dict(payload)
            payload["level"] = level
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
    from prep.models import PrepNoteRepair

    repair = PrepNoteRepair.objects.filter(
        topic=topic_obj,
        level=level,
        source_signature=source_signature,
    ).first()
    if not repair or repair.status != "needs_review":
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
            "Validated notes could not be produced for this level. "
            "It is awaiting tutor/admin review and will not be regenerated until the review is resolved or its source changes."
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


def _record_note_review_failure(
    topic_obj,
    level: str,
    source_signature: str,
    cache_key: str,
    content: str,
    review: dict,
) -> None:
    if not topic_obj:
        return
    from prep.models import PrepNoteRepair

    error = str(
        review.get("error")
        or review.get("skipped")
        or "independent review did not complete"
    )
    repair, _ = PrepNoteRepair.objects.get_or_create(
        topic=topic_obj,
        level=level,
        source_signature=source_signature,
        defaults={
            "cache_key": cache_key,
            "original_content": content,
            "current_content": content,
            "validation_issues": [error],
        },
    )
    repair.repair_log = (repair.repair_log if isinstance(repair.repair_log, list) else [])[-9:]
    repair.repair_log.append({
        "stage": "independent_review",
        "model": review.get("model_used", ""),
        "response": str(review.get("raw_response") or "")[:4000],
        "error": error[:1000],
    })
    repair.current_content = content
    repair.validation_issues = [error]
    repair.status = "needs_review"
    repair.last_error = error[:4000]
    repair.save(update_fields=[
        "repair_log",
        "current_content",
        "validation_issues",
        "status",
        "last_error",
        "updated_at",
    ])
    _record_note_generation_failure(
        topic_obj,
        level,
        source_signature,
        error,
        force_review=True,
    )


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
        topic_obj=topic_obj,
    )

    for entry in entries:
        payload = _cache_payload_as_dict(entry.payload)
        if not payload or payload.get("level") != level:
            continue
        if payload.get("review_status") == "skipped_no_source":
            continue
        if int(payload.get("study_profile_version", 0) or 0) != _course_study_profile_version(topic_obj.course):
            continue
        if int(payload.get("topic_content_rules_version", 0) or 0) != _topic_content_rules_version(topic_obj):
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
            "source_references": payload.get("source_references", validation_options["source_references"]),
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
    repair_usage = {}
    last_repair_error = ""
    validation_options = _note_validation_options(
        topic_obj.course,
        topic_obj.title,
        topic_obj.summary,
        topic_obj.subtopics,
        topic_obj=topic_obj,
    )
    for _ in range(repair.attempts, 3):
        repair.attempts += 1
        repair.validation_issues = issues
        repair.save(update_fields=["attempts", "validation_issues", "updated_at"])
        prefix, repair_scope, suffix = _note_repair_scope(working_content, topic_obj.title)
        repair_instruction = (
            "Return old_block and new_block as string fields in one JSON object. "
            "Change only the reported issue; preserve all other text."
        )
        if last_repair_error:
            repair_instruction += (
                f"\nYour previous response was rejected: {last_repair_error}. "
                "Return the required JSON object only, with no reasoning or surrounding prose."
            )
        result = call_together_repair(
            [
                {"role": "system", "content": "Repair one Markdown/LaTeX block surgically. Never split words, theorem titles, or sentences across lines. Preserve Markdown blockquote prefixes on every theorem line."},
                {"role": "user", "content": repair_instruction + "\nIssues: " + json.dumps(issues) + "\nSource (only the affected section when identifiable):\n" + repair_scope},
            ],
            model=getattr(settings, "TOGETHER_REPAIR_MODEL", "deepseek-ai/DeepSeek-V4.1-Flash"),
            max_tokens=2000,
        )
        repair_usage = _merge_usage(repair_usage, result.get("usage", {}))
        repair_log = repair.repair_log if isinstance(repair.repair_log, list) else []
        repair_log.append({
            "stage": "targeted_block_repair",
            "attempt": repair.attempts,
            "model": result.get("model_used") or getattr(
                settings, "TOGETHER_REPAIR_MODEL", "deepseek-ai/DeepSeek-V4.1-Flash"
            ),
            "issues": issues[:20],
            "response": str(result.get("content") or "")[:2000],
            "error": str(result.get("error") or "")[:1000],
        })
        repair.repair_log = repair_log[-10:]
        repair.save(update_fields=["repair_log", "updated_at"])
        if not result.get("success"):
            last_repair_error = str(result.get("error") or "repair provider returned an unsuccessful response")
            continue
        try:
            patch = _parse_topic_note_repair_patch(result.get("content", ""))
            old_block = patch["old_block"]
            new_block = patch["new_block"]
            if not old_block or not new_block or repair_scope.count(old_block) != 1:
                raise ValueError("repair block missing or not unique")
            repaired_scope = repair_scope.replace(old_block, new_block, 1)
            candidate = prefix + repaired_scope + suffix
            candidate_issues = _note_completion_issues(
                candidate,
                topic_obj.title,
                **validation_options,
            )
            review = None
            if not candidate_issues:
                review = _review_topic_note_content(topic_obj, level, candidate)
                repair_usage = _merge_usage(repair_usage, review.get("usage", {}))
                repair_log = repair.repair_log if isinstance(repair.repair_log, list) else []
                repair_log.append({
                    "stage": "independent_review",
                    "attempt": repair.attempts,
                    "model": review.get("model_used", ""),
                    "issues": review.get("issues", [])[:8],
                    "response": str(review.get("raw_response") or "")[:4000],
                    "error": str(review.get("error") or "")[:1000],
                })
                repair.repair_log = repair_log[-10:]
                repair.save(update_fields=["repair_log", "updated_at"])
                if not review.get("success") or review.get("skipped"):
                    last_repair_error = str(
                        review.get("error")
                        or review.get("skipped")
                        or "independent review failed"
                    )
                    continue
                candidate_issues.extend(review.get("issues", []))
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
                "topic_content_rules_version": _topic_content_rules_version(topic_obj),
                "source_references": validation_options["source_references"],
                "source_signature": source_signature,
                "review_status": "passed",
                "review_model": (review or {}).get("model_used", ""),
                "reviewed_at": timezone.now().isoformat(),
                "review_report": (review or {}).get("report") or {
                    "skipped": (review or {}).get("skipped", "")
                },
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
                "usage": repair_usage,
                "review_status": "passed",
                "source_references": validation_options["source_references"],
            }
        except ValueError as exc:
            last_repair_error = str(exc)
            logger.warning(
                "[Topic Notes] targeted repair patch rejected for %s: %s",
                topic_obj.title,
                exc,
            )
            continue

    fallback_issues = issues or [last_repair_error or "targeted block repair did not produce validated notes"]
    fallback_repair = _regenerate_invalid_note_sections(
        topic_obj,
        level,
        source_signature,
        cache_key,
        working_content,
        fallback_issues,
    )
    if fallback_repair:
        fallback_repair["usage"] = _merge_usage(
            repair_usage,
            fallback_repair.get("usage", {}),
        )
        fallback_repair["repair_fallback"] = "section_regeneration"
        return fallback_repair

    repair.status = "needs_review"
    repair.last_error = "; ".join(fallback_issues)
    if last_repair_error:
        repair.last_error += f"; targeted repair failed: {last_repair_error}"
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
        return {"success": False, "error": "Mathematical symbolic calculation could not be completed.", "engine": "SymPy"}


# ─── 2. Dual-Model AI Router (DeepSeek V3 / R1) ──────────────────────────────

def call_deepseek(
    messages: list[dict],
    model: str = "deepseek-chat",
    max_tokens: int = 6000,
    temperature: float = 0.2,
    auto_continue: bool = True,
    thinking_enabled: bool | None = None,
) -> dict:
    """
    Make a guarded API call to DeepSeek.
    Enforces maximum token caps with auto-continuation if output hits length limit.
    """
    api_key = getattr(settings, "DEEPSEEK_API", "") or os.environ.get("DEEPSEEK_API", "")
    base_url = getattr(settings, "DEEPSEEK_BASE_URL", "https://api.deepseek.com") or "https://api.deepseek.com"

    if not api_key:
        logger.error("[DeepSeek] API key is not configured in settings or environment.")
        return {"success": False, "error": "The AI service is currently unavailable. Please try again shortly."}

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
    if thinking_enabled is not None:
        payload["thinking"] = {"type": "enabled" if thinking_enabled else "disabled"}

    try:
        resp = requests.post(f"{base_url}/chat/completions", headers=headers, json=payload, timeout=35)
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
                if content:
                    cont_messages = list(messages) + [
                        {"role": "assistant", "content": content},
                        {"role": "user", "content": "Continue directly from where you stopped. Do not repeat any preceding text, and complete all remaining sections thoroughly."},
                    ]
                else:
                    # Model exhausted tokens entirely in reasoning_content before outputting assistant content
                    logger.warning("[DeepSeek] Reasoning exhausted token budget before assistant content. Requesting immediate final answer...")
                    cont_messages = list(messages) + [
                        {"role": "user", "content": "Please immediately provide the final answer content now without further hidden thought tokens."},
                    ]
                cont_payload = {
                    "model": model,
                    "messages": cont_messages,
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                }
                if thinking_enabled is not None:
                    cont_payload["thinking"] = {"type": "enabled" if thinking_enabled else "disabled"}
                elif not content:
                    # Explicitly disable thinking on retry if reasoning swallowed the token budget
                    cont_payload["thinking"] = {"type": "disabled"}
                try:
                    cont_resp = requests.post(f"{base_url}/chat/completions", headers=headers, json=cont_payload, timeout=90)
                    if cont_resp.status_code == 200:
                        cont_data = cont_resp.json()
                        cont_choice = cont_data["choices"][0]
                        cont_content = cont_choice["message"].get("content", "").strip()
                        usage = _merge_usage(usage, cont_data.get("usage", {}))
                        if not content:
                            content = cont_content
                        else:
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

            if not content and reasoning:
                # Attempt recovery of JSON or output from reasoning_content
                r_text = reasoning.strip()
                if "[" in r_text and "]" in r_text:
                    s_idx = r_text.find("[")
                    e_idx = r_text.rfind("]")
                    if e_idx > s_idx:
                        cand = r_text[s_idx:e_idx + 1]
                        try:
                            json.loads(cand, strict=False)
                            content = cand
                            logger.info("[DeepSeek] Successfully extracted valid JSON array from reasoning_content.")
                        except Exception:
                            pass
                elif "{" in r_text and "}" in r_text:
                    s_idx = r_text.find("{")
                    e_idx = r_text.rfind("}")
                    if e_idx > s_idx:
                        cand = r_text[s_idx:e_idx + 1]
                        try:
                            json.loads(cand, strict=False)
                            content = cand
                            logger.info("[DeepSeek] Successfully extracted valid JSON object from reasoning_content.")
                        except Exception:
                            pass

            if not content:
                together_repair_model = getattr(settings, "TOGETHER_REPAIR_MODEL", "")
                if together_repair_model:
                    try:
                        repair_res = call_together_repair(messages, together_repair_model, max_tokens=max_tokens)
                        if repair_res.get("success") and repair_res.get("content"):
                            content = repair_res["content"].strip()
                            usage = _merge_usage(usage, repair_res.get("usage", {}))
                            logger.info("[DeepSeek] Recovered empty assistant content via Together repair model.")
                    except Exception as rep_err:
                        logger.warning(f"[DeepSeek] Together repair fallback failed: {rep_err}")

            if not content:
                response_id = str(data.get("id") or "unavailable")
                error = (
                    "DeepSeek returned empty assistant content "
                    f"(finish_reason={finish_reason}, reasoning_content_present={bool(reasoning)}, "
                    f"response_id={response_id})."
                )
                logger.warning("[DeepSeek] %s model=%s usage=%s", error, model, usage)
                return {
                    "success": False,
                    "empty_response": True,
                    "error": error,
                    "finish_reason": finish_reason,
                    "response_id": response_id,
                    "model_used": model,
                    "usage": usage,
                }

            return {
                "success": True,
                "content": content,
                "reasoning_content": reasoning,
                "model_used": model,
                "usage": usage,
            }
        else:
            logger.warning(f"[DeepSeek API Error] HTTP {resp.status_code}: {resp.text[:300]}. Attempting Together AI fallback...")
            together_model = getattr(settings, "TOGETHER_CHAT_MODEL", "deepseek-ai/DeepSeek-V4.1-Flash")
            if getattr(settings, "TOGETHERAI_API", "") and together_model:
                try:
                    fallback_res = call_together_repair(messages, together_model, max_tokens=max_tokens)
                    if fallback_res.get("success") and fallback_res.get("content"):
                        return fallback_res
                except Exception as fb_err:
                    logger.warning("[DeepSeek] Together fallback also failed: %s", fb_err)
            return {"success": False, "error": "The AI service encountered an issue while processing your request. Please try again shortly."}
    except Exception as e:
        logger.warning(f"[DeepSeek API Exception] {e}. Attempting Together AI fallback...")
        together_model = getattr(settings, "TOGETHER_CHAT_MODEL", "deepseek-ai/DeepSeek-V4.1-Flash")
        if getattr(settings, "TOGETHERAI_API", "") and together_model:
            try:
                fallback_res = call_together_repair(messages, together_model, max_tokens=max_tokens)
                if fallback_res.get("success") and fallback_res.get("content"):
                    return fallback_res
            except Exception as fb_err:
                logger.warning("[DeepSeek] Together fallback also failed: %s", fb_err)
        return {"success": False, "error": "The AI service is temporarily unreachable. Please try again shortly."}


def call_together_repair(messages: list[dict], model: str, max_tokens: int = 2000) -> dict:
    """Make one bounded Together.ai repair call with no continuation."""
    api_key = getattr(settings, "TOGETHERAI_API", "") or os.environ.get("TOGETHERAI_API", "")
    if not api_key:
        logger.warning("[Together Repair] TOGETHERAI_API key is not configured.")
        return {"success": False, "error": "The AI verification service is temporarily unavailable."}

    try:
        request_body = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": 0.1,
            "response_format": {"type": "json_object"},
        }
        response = requests.post(
            "https://api.together.xyz/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json=request_body,
            timeout=60,
        )
        if response.status_code == 400 and "response_format" in response.text.lower():
            logger.warning(
                "[Together Repair] model %s rejected JSON mode; retrying once without it",
                model,
            )
            request_body.pop("response_format")
            response = requests.post(
                "https://api.together.xyz/v1/chat/completions",
                headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
                json=request_body,
                timeout=60,
            )
        if response.status_code != 200:
            logger.error("[Together Repair] HTTP %s: %s", response.status_code, response.text[:500])
            return {"success": False, "error": "The AI verification service encountered an issue. Please try again shortly."}
        data = response.json()
        choice = data["choices"][0]
        message = choice.get("message", {})
        content = message.get("content")
        usage = data.get("usage", {})
        if not isinstance(content, str) or not content.strip():
            finish_reason = choice.get("finish_reason") or "unknown"
            reasoning_present = bool(message.get("reasoning_content"))
            return {
                "success": False,
                "error": (
                    "Together repair returned empty final content "
                    f"(finish_reason={finish_reason}; reasoning_content_present={reasoning_present})."
                ),
                "model_used": model,
                "usage": usage,
            }
        return {
            "success": True,
            "content": content.strip(),
            "model_used": model,
            "usage": usage,
        }
    except Exception as exc:
        logger.warning("[Together Repair] request failed: %s", exc)
        return {"success": False, "error": "The AI verification service is temporarily unreachable."}


def route_math_request(
    prompt: str,
    course_code: str,
    topic_label: str = "",
    is_complex_proof: bool | None = None,
    system_prompt: str | None = None,
    max_tokens_override: int | None = None,
    model_override: str | None = None,
    auto_continue: bool = True,
    thinking_enabled: bool | None = None,
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
    if model_override:
        model = str(model_override)
    if max_tokens_override is not None:
        max_tokens = min(max_tokens, max(1, int(max_tokens_override)))

    if not system_prompt:
        system_prompt = (
            f"You are an expert academic mathematics and statistics tutor specialized in {course_code}. "
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

    return call_deepseek(
        messages=messages,
        model=model,
        max_tokens=max_tokens,
        auto_continue=auto_continue,
        thinking_enabled=thinking_enabled,
    )


# ─── 3. High-Level AI Operations with Cache Guard ────────────────────────────

from services.prep_blocks import (
    validate_structured_blocks,
    blocks_to_markdown,
    parse_markdown_to_blocks,
)


def clean_latex_document_markup(text: str) -> str:
    """
    Convert raw LaTeX document commands and list environments into standard clean Markdown
    while strictly preserving LaTeX mathematical notation inside math mode ($...$, $$...$$, \\(..\\), \\[..\\]).
    """
    if not text or not isinstance(text, str):
        return ""
    cleaned = text.strip()

    # 1. Clean document-level whitespace and layout commands
    cleaned = re.sub(r"\\noindent\s*", "", cleaned)
    cleaned = re.sub(r"\\vspace\{[^}]*\}", "", cleaned)
    cleaned = re.sub(r"\\hspace\{[^}]*\}", "", cleaned)
    cleaned = re.sub(r"\\hrule\b", "", cleaned)

    # 2. Convert mark tags e.g. \hfill (3 marks) -> **(3 marks)**
    cleaned = re.sub(
        r"\\hfill\s*(\([0-9]+\s*(?:marks?|mks)\)|\[[0-9]+\s*(?:marks?|mks)\])",
        r"**\1**",
        cleaned,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(r"\\hfill\s*", " ", cleaned)

    # 3. Protect math blocks while converting non-math LaTeX text styling
    math_pattern = r"(\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]|\$[^\$\n]+?\$|\\\([\s\S]*?\\\))"
    segments = re.split(math_pattern, cleaned)
    for idx, seg in enumerate(segments):
        if idx % 2 == 0:
            seg = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", seg)
            seg = re.sub(r"\\textit\{([^}]*)\}", r"*\1*", seg)
            seg = re.sub(r"\\underline\{([^}]*)\}", r"**\1**", seg)
            segments[idx] = seg
    cleaned = "".join(segments)

    # 4. Handle nested enumerate environments (innermost first)
    def replace_inner_enum(match):
        opt = match.group(1) or ""
        body = match.group(2)
        is_roman = bool(re.search(r"\bi\b|\(i\)|i\)", opt, re.IGNORECASE))
        is_alpha = bool(re.search(r"\ba\b|\(a\)|a\)", opt, re.IGNORECASE))

        alpha_seq = ["(a)", "(b)", "(c)", "(d)", "(e)", "(f)", "(g)", "(h)", "(i)", "(j)"]
        roman_seq = ["(i)", "(ii)", "(iii)", "(iv)", "(v)", "(vi)", "(vii)", "(viii)", "(ix)", "(x)"]
        num_seq = [f"{i}." for i in range(1, 30)]

        default_seq = roman_seq if is_roman else (alpha_seq if is_alpha else num_seq)

        items = re.split(r"\\item(?:\[([^\]]*)\])?\s*", body)
        out_lines = []
        if items[0].strip():
            out_lines.append(items[0].strip())

        item_idx = 0
        for i in range(1, len(items), 2):
            label = items[i]
            content = items[i + 1].strip() if i + 1 < len(items) else ""
            if not label:
                label = default_seq[item_idx] if item_idx < len(default_seq) else f"({item_idx + 1})"
            item_idx += 1

            content_lines = content.splitlines()
            if content_lines:
                out_lines.append(f"{label} {content_lines[0]}")
                for c_line in content_lines[1:]:
                    out_lines.append(c_line)
            else:
                out_lines.append(f"{label}")
        return "\n\n" + "\n".join(out_lines) + "\n\n"

    inner_enum_re = re.compile(
        r"\\begin\{enumerate\}(?:\[([^\]]*)\])?((?:(?!\\begin\{enumerate\})[\s\S])*?)\\end\{enumerate\}"
    )
    for _ in range(6):
        if not inner_enum_re.search(cleaned):
            break
        cleaned = inner_enum_re.sub(replace_inner_enum, cleaned)

    def replace_itemize(match):
        body = match.group(1)
        items = re.split(r"\\item\s*", body)
        out_lines = [f"- {it.strip()}" for it in items[1:] if it.strip()]
        return "\n\n" + "\n".join(out_lines) + "\n\n"

    cleaned = re.sub(r"\\begin\{itemize\}([\s\S]*?)\\end\{itemize\}", replace_itemize, cleaned)
    cleaned = re.sub(
        r"\\begin\{(?:center|flushleft|flushright)\}([\s\S]*?)\\end\{(?:center|flushleft|flushright)\}",
        r"\1",
        cleaned,
    )
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def normalize_math_delimiters(text: str) -> str:
    """
    Shared renderer hygiene for notes, authentic questions, generated questions,
    and PDF exports. It performs deterministic transport repairs and converts
    raw LaTeX document markup to clean Markdown while preserving math notation.
    """
    if not text:
        return ""
    text = clean_latex_document_markup(text)
    text = repair_json_escaped_latex_newlines(str(text))
    text = re.sub(r"\\n(?![a-zA-Z])", "\n", text)
    text = text.replace("Lindeberg\ufffdL\ufffdy", "Lindeberg–Lévy")
    text = re.sub(r"^\s*>\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*#\s*$", "", text, flags=re.MULTILINE)

    greek_commands = (
        "varepsilon", "vartheta", "varpi", "varrho", "varsigma", "varphi",
        "alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta",
        "iota", "kappa", "lambda", "mu", "nu", "xi", "omicron", "pi", "rho",
        "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega",
        "Gamma", "Delta", "Theta", "Lambda", "Xi", "Pi", "Sigma", "Upsilon",
        "Phi", "Psi", "Omega",
    )
    command_boundary = re.compile(
        r"(?<!\\)\\(" + "|".join(greek_commands) + r")(?=[A-Za-z])"
    )
    math_or_code = re.compile(
        r"```[\s\S]*?```|`[^`\n]*`|\$\$[\s\S]*?\$\$|"
        r"(?<!\\)\$(?!\$)[^\n$]*?(?<!\\)\$|\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]"
    )

    def separate_command_from_following_text(match: re.Match[str]) -> str:
        segment = match.group(0)
        if segment.startswith("`"):
            return segment
        return command_boundary.sub(r"\\\1 ", segment)

    text = math_or_code.sub(separate_command_from_following_text, text)

    # Normalize doubly-escaped LaTeX commands (e.g. \\mathbb -> \mathbb, \\frac -> \frac, \\setminus -> \setminus)
    text = re.sub(r'\\\\([a-zA-Z]+)', r'\\\1', text)

    # Collapse adjacent display delimiters to prevent nested math parsing errors
    text = re.sub(r'(?:\\\[|\$\$)\s*(?:\\\[|\$\$)', '$$', text)
    text = re.sub(r'(?:\\\]|\$\$)\s*(?:\\\]|\$\$)', '$$', text)

    # Ensure LaTeX environments occurring outside standalone $$ blocks are isolated in clean $$...$$
    env_pattern = re.compile(
        r"(?:\\\[|\$\$)?\s*\\begin\{(aligned|cases|matrix|pmatrix|bmatrix|vmatrix|gather|split|array|align\*?)\}([\s\S]*?)\\end\{\1\}\s*(?:\\\]|\$\$)?",
        re.DOTALL,
    )
    def env_repl(match):
        env = match.group(1)
        body = match.group(2).strip()
        body = re.sub(r'\n\s*\n', '\n', body)
        return f"\n\n$$\n\\begin{{{env}}}\n{body}\n\\end{{{env}}}\n$$\n\n"
    text = env_pattern.sub(env_repl, text)

    # Clean any outer \[ ... \] that wrapped an inner $$...$$
    text = re.sub(r'\\\[\s*\$\$([\s\S]*?)\$\$\s*\\\]', r'\n\n$$\n\1\n$$\n\n', text)

    # Collapse internal blank lines within display math blocks
    def clean_display_math(match):
        inner = match.group(1).strip()
        inner = re.sub(r'\n\s*\n', '\n', inner)
        return f"\n\n$$\n{inner}\n$$\n\n"
    text = re.sub(r'\$\$([\s\S]*?)\$\$', clean_display_math, text)

    # Ensure unclosed code fences are closed
    if text.count("```") % 2 != 0:
        text = text.rstrip() + "\n```\n"

    # Ensure unclosed display math blocks are closed
    prose_source = re.sub(r"```[\s\S]*?```", "", text)
    if prose_source.count("$$") % 2 != 0:
        text = text.rstrip() + "\n$$\n"

    return text.strip()


def sanitize_math_markdown(text: str) -> str:
    """Wrapper for backward compatibility calling normalize_math_delimiters."""
    return normalize_math_delimiters(text)


def repair_question_and_solution_text(text: str) -> str:
    """
    Comprehensive repair and hygiene pipeline for past paper questions,
    step-by-step solutions, and generated questions/answers.
    Ensures zero unclosed code fences, balanced display math, stripped
    unresolved visual markers, and clean KaTeX delimiters.
    """
    if not text or not isinstance(text, str):
        return ""

    text = repair_json_escaped_latex_newlines(str(text))
    text = clean_latex_document_markup(text)

    # 1. Close unclosed code fences ```
    if text.count("```") % 2 != 0:
        text = text.rstrip() + "\n```\n"

    # 2. Balance unclosed display math $$
    prose = re.sub(r"```[\s\S]*?```", "", text)
    if prose.count("$$") % 2 != 0:
        text = text.rstrip() + "\n$$\n"

    # 3. Strip unresolved visual markers and forbidden raw HTML
    text = re.sub(r"\[\[VISUAL:[^\]]*\]\]", "", text)
    text = re.sub(r"<\s*(?:img|picture|source|svg|iframe|object|embed)[^>]*>", "", text, flags=re.IGNORECASE)

    # 4. Remove empty display math blocks
    text = re.sub(r"\$\$\s*\$\$", "", text)

    # 5. Apply core delimiter normalization
    text = normalize_math_delimiters(text)

    # 6. Re-verify fences and display math post-normalization
    if text.count("```") % 2 != 0:
        text = text.rstrip() + "\n```\n"
    prose_after = re.sub(r"```[\s\S]*?```", "", text)
    if prose_after.count("$$") % 2 != 0:
        text = text.rstrip() + "\n$$\n"

    return text.strip()


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
    validation_options = _note_validation_options(
        course_obj,
        topic_title,
        topic_summary,
        subtopics,
        topic_obj=topic_obj,
    )
    allows_code = validation_options["allow_code"]
    allows_math = validation_options["allow_math"]
    if validation_options["content_rule_issues"]:
        return {
            "notes": "",
            "blocks": [],
            "schema_version": 2,
            "cached": False,
            "level": level,
            "validation_failed": True,
            "error": "; ".join(validation_options["content_rule_issues"]),
        }

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
            "source_references": validation_options["source_references"],
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
        cached_text = repair_json_escaped_latex_newlines(
            str(cached.get("content", "") or "")
        )
        if not cached_text.strip() and isinstance(cached.get("blocks"), list) and cached["blocks"]:
            cached_text = blocks_to_markdown(cached["blocks"]).strip()
            cached["content"] = cached_text
        if not cached_text.strip():
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
                    "regenerated_from_invalid_cache": True,
                    "generation_required": True,
                    "error": "The cached note is empty; a validated replacement is required.",
                }
            from prep.models import PrepContentCache

            logger.warning("[Topic Notes] Discarding empty cache for %s %s", course_code, topic_title)
            PrepContentCache.objects.filter(cache_key=cache_key).delete()
            cached = None
            regenerated_from_invalid_cache = True
    if cached and isinstance(cached, dict) and ("content" in cached or "blocks" in cached):
        cached_content = repair_json_escaped_latex_newlines(
            str(cached.get("content", "") or "")
        )
        cached_issues = _note_completion_issues(cached_content, topic_title, **validation_options)
        if cached.get("validation_state") == NOTE_VALIDATION_STATE and not cached_issues:
            if cached.get("review_status") == "skipped_no_source":
                return {
                    "notes": "",
                    "blocks": [],
                    "schema_version": cached.get("schema_version", 1),
                    "cached": False,
                    "level": level,
                    "validation_failed": True,
                    "needs_review": True,
                    "error": (
                        "These notes cannot be published until approved course material is "
                        "available for independent review."
                    ),
                }
            # Strict read-only: never mutate or overwrite a valid cache on read.
            _mark_cached_note_valid(topic_obj, level, cache_signature, cached_content)
            return {
                "notes": cached_content,
                "blocks": cached.get("blocks"),
                "schema_version": cached.get("schema_version", 1),
                "cached": True,
                "level": level,
                "model": cached.get("model", "Cache"),
                "source_references": cached.get("source_references", validation_options["source_references"]),
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
                "source_references": cached.get("source_references", validation_options["source_references"]),
            }
        blocked = _blocked_note_generation(topic_obj, level, cache_signature)
        if blocked:
            return blocked
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
            f"Code permitted by approved course/topic rules: {allows_code}\n"
            f"Mathematical notation permitted by approved course/topic rules: {allows_math}\n"
            f"Chemical equations permitted by approved course/topic rules: {validation_options['allow_chemical_equations']}\n"
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

    past_questions_context_block = ""
    if topic_obj:
        try:
            from prep.models import PrepQuestion
            from services.prep_ingestion import assessment_question_rendering_issues

            topic_past_qs = list(
                PrepQuestion.objects.filter(
                    topic=topic_obj,
                    verification_status__in=PrepQuestion.ANSWERABLE_STATUSES,
                ).order_by("number", "id")[:8]
            )
            if topic_past_qs:
                q_lines = []
                for q in topic_past_qs:
                    q_text = (q.question_latex or "").strip()
                    if not q_text or assessment_question_rendering_issues(q_text):
                        continue
                    entry = f"- Question {q.number} ({q.marks or 5} marks): {q_text[:350]}"
                    if q.solution_latex:
                        sol_snippet = q.solution_latex.strip()[:250]
                        entry += f"\n  Key solution technique / marking criteria: {sol_snippet}"
                    q_lines.append(entry)
                if q_lines:
                    past_questions_context_block = (
                        "AUTHENTIC PAST EXAMINATION QUESTIONS & ASSESSMENT SCOPE:\n"
                        "The following examination problems have appeared in actual CATs and final papers for this topic. "
                        "The generated revision notes must explicitly prepare students for these types of questions: cover all underlying definitions, "
                        "theorems, formulas, calculation techniques, and proof strategies tested in these genuine past exam questions:\n"
                        + "\n".join(q_lines)
                        + "\n\n"
                    )
        except Exception as e:
            logger.warning(f"[Topic Notes] Could not retrieve past questions context: {e}")

    approved_visual_manifest = _approved_visual_manifest(validation_options["source_references"])
    source_reference_block = (
        "APPROVED FIGURE CHOICES (the server stores page provenance):\n"
        + json.dumps(approved_visual_manifest, ensure_ascii=True, sort_keys=True)
        + "\nUse a figure only by inserting its exact [[VISUAL:id]] marker at the relevant position. "
        "Do not write Markdown image URLs, invent a figure, generate Mermaid/TikZ/plot code, or request an unlisted figure. "
        "Do not create a Figure Recall Map, marker table, or memory-device sentence with empty figure placeholders. "
        "Place each required marker directly beside the explanation it illustrates. "
        "Explain every concept fully in plain prose, including any supported axes, labels, units, directions, or relationships. "
        "Never refer to a figure, diagram, graph, chart, table, or image in the prose, including phrases such as "
        "'as shown above', 'in the diagram', or 'see Figure 1', even when an approved image is included. "
        "A student must understand the explanation without looking at the image. "
        "Figures marked required were mapped to this topic from source-page evidence and must be included beside the matching explanation. "
        "If a listed optional figure is not relevant, omit it.\n\n"
        if approved_visual_manifest
        else (
            "NO APPROVED SOURCE FIGURE IS AVAILABLE. Do not add an image, diagram, graph, Mermaid/TikZ, or plot code.\n"
            "Explain any relevant visual relationship naturally in the surrounding lesson, without labeling it as a walkthrough, "
            "announcing that an image is unavailable, or repeating caveats about missing figures. "
            "Never refer to a figure, diagram, graph, chart, table, or image in the prose, including phrases such as "
            "'as shown above', 'in the diagram', or 'see Figure 1'. "
            "Use only source-supported facts and never tell the student to look at an absent image.\n\n"
        )
    )
    visual_independence_block = (
        "UNIVERSAL VISUAL AND NOTATION REQUIREMENTS (all disciplines):\n"
        "Define every variable, symbol, abbreviation, and unit when it first appears. "
        "Explain visual relationships in ordinary prose, including supported axes, units, directions, comparisons, and conclusions. "
        "Never refer to an image, figure, diagram, graph, chart, or table in the prose, even when an approved image is included. "
        "Never make the student infer the explanation solely from an image. "
        "When no source image is available, explain a relevant visual concept in ordinary prose only when that adds useful understanding; do not announce the absence of an image or repeat a disclaimer. "
        "Use only source-supported facts; omit details that are unavailable instead of guessing. "
        "The explanation must make complete sense without viewing any image.\n\n"
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
            "Tone: Patient, very simple, and foundational (Level 1). Teach as if explaining the idea to a child for the first time, "
            "while speaking respectfully to an adult learner.\n"
            "- Use familiar everyday words, short sentences, and one new idea at a time. Assume the learner may need extra time; never skip a reasoning step.\n"
            "- Start with a concrete everyday example or analogy before introducing an abstract definition. Explain what the example shows and where the analogy stops being exact.\n"
            "- Avoid jargon. When a necessary course term first appears, give its meaning immediately in plain words and use a simple example before using it again.\n"
            "- If approved symbols, equations, or code are needed, introduce only one small piece at a time, say what every part means in ordinary language, and explain the result in words. Do not make the notes more technical than the source requires."
        )
    elif level == "level_3":
        level_instruction = (
            "Tone: Exam Mode & High-Yield Mastery (Level 3).\n"
            "- Focus directly on how this topic is tested in course examinations (CATs and finals).\n"
            "- Highlight high-frequency exam question patterns and common pitfalls/traps where students lose marks.\n"
            "- Provide discipline-appropriate answer structures and worked applications.\n"
            "- Include examination marking rubric tips and time-management strategies."
        )
    else:  # level_2
        level_instruction = (
            "Tone: Rigorous Academic Standard (Level 2).\n"
            "- Deliver thorough academic notes with precise definitions and academic rigor.\n"
            "- Include a representative worked example or application grounded in the approved notes.\n"
            "- Use formal notation only where supported by the approved source and relevant to this topic."
        )
    if study_profile and study_profile.get("subject_family") in {
        "social_science", "humanities", "business_economics", "general_science",
    }:
        level_instruction += (
            f"\nSubject-family guidance ({study_profile['subject_family'].replace('_', ' ')}): explain the approved concepts, evidence, context, and applications accurately. "
            "Do not introduce mathematical derivations or programming unless the approved source capability explicitly allows them."
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
        f"{past_questions_context_block}"
        f"{source_reference_block}"
        f"{visual_independence_block}"
        "NON-STUDY ADMINISTRATIVE DETAILS POLICY (all disciplines):\n"
        "Do not include lecturer or instructor names or credentials, course codes, course delivery details, university/faculty/department names as course metadata, contact details, email addresses, phone numbers, download records, hosting-platform disclaimers, or title-page administration. These are not study content even when present in the source. Discuss institutions or their people only when they are themselves the subject of the lesson, not as information about who offers or distributes this course.\n\n"
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
            f"You are an expert academic tutor for the approved subject family {study_profile.get('subject_family')}. "
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
        thinking_enabled=False,
    )

    if result.get("empty_response") or (
        result.get("success") and not str(result.get("content") or "").strip()
    ):
        first_error = result.get("error") or "The first model response contained no note text."
        first_usage = result.get("usage", {})
        retry_result = route_math_request(
            prompt,
            course_code,
            topic_label=topic_title,
            is_complex_proof=False,
            system_prompt=note_system_prompt,
            thinking_enabled=False,
        )
        retry_usage = retry_result.get("usage", {})
        retry_result["usage"] = _merge_usage(first_usage, retry_usage)
        retry_content = str(retry_result.get("content") or "").strip()
        if retry_result.get("empty_response") or not retry_result.get("success") or not retry_content:
            retry_error = retry_result.get("error") or "The retry also returned empty note content."
            error = f"Initial note response was empty ({first_error}); one retry failed ({retry_error})."
            logger.error("[Topic Notes] %s course=%s topic=%s level=%s", error, course_code, topic_title, level)
            _record_note_generation_failure(topic_obj, level, cache_signature, error, force_review=True)
            return {
                "notes": "",
                "blocks": [],
                "cached": False,
                "level": level,
                "model": retry_result.get("model_used") or result.get("model_used"),
                "usage": retry_result["usage"],
                "regenerated_from_invalid_cache": regenerated_from_invalid_cache,
                "needs_review": True,
                "validation_failed": True,
                "empty_response": True,
                "error": error,
            }
        result = retry_result

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
                or issue.startswith("required approved source visual missing")
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
                thinking_enabled=False,
            )
            if not cont_res.get("success") or not cont_res.get("content"):
                break
            continuation = _resolve_approved_visual_markers(
                cont_res["content"].strip(),
                validation_options["source_references"],
            )
            content = content + "\n\n" + continuation
            result["usage"] = _merge_usage(result.get("usage", {}), cont_res.get("usage", {}))

        # Preserve the generated Markdown source. The browser renderer is the
        # single owner of Markdown and KaTeX interpretation.
        content = _insert_required_visual_markers(content, approved_visual_manifest)
        content = _resolve_approved_visual_markers(content, validation_options["source_references"])
        content = _dedupe_approved_visual_images(content, validation_options["source_references"])
        content = _normalize_approved_visual_captions(content, validation_options["source_references"])
        content = str(content).strip()
        completion_issues = _note_completion_issues(content, topic_title, **validation_options)
        review = None
        if not completion_issues:
            review = _review_topic_note_content(topic_obj, level, content)
            result["usage"] = _merge_usage(result.get("usage", {}), review.get("usage", {}))
            if not review.get("success"):
                error = "Independent content review failed: " + str(
                    review.get("error") or "review provider returned an unsuccessful response"
                )
                _record_note_review_failure(
                    topic_obj,
                    level,
                    cache_signature,
                    cache_key,
                    content,
                    review,
                )
                logger.error(
                    "[Topic Notes] %s course=%s topic=%s level=%s",
                    error,
                    course_code,
                    topic_title,
                    level,
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
                    "validation_failed": True,
                    "error": error,
                }
            if review.get("skipped"):
                _record_note_review_failure(
                    topic_obj,
                    level,
                    cache_signature,
                    cache_key,
                    content,
                    review,
                )
            completion_issues.extend(review.get("issues", []))
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
                        "source_references": validation_options["source_references"],
                    },
                    "course": course_obj,
                    "topic": topic_obj,
                },
            )
            if _note_needs_section_regeneration(completion_issues):
                repaired = _regenerate_invalid_note_sections(
                    topic_obj,
                    level,
                    cache_signature,
                    cache_key,
                    content,
                    completion_issues,
                )
            else:
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
                repaired["usage"] = _merge_usage(result.get("usage", {}), repaired.get("usage", {}))
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
            "topic_content_rules_version": _topic_content_rules_version(topic_obj),
            "source_references": validation_options["source_references"],
            "source_signature": cache_signature,
            "review_status": (
                "skipped_no_source"
                if review and review.get("skipped")
                else "passed"
            ),
            "review_model": (review or {}).get("model_used", ""),
            "reviewed_at": timezone.now().isoformat(),
            "review_report": (review or {}).get("report") or {
                "skipped": (review or {}).get("skipped", "")
            },
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
            "review_status": (
                "skipped_no_source"
                if review and review.get("skipped")
                else "passed"
            ),
            "source_references": validation_options["source_references"],
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

    raise ValueError(f"Could not parse JSON response: {cleaned[:200]}")


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
    force_fresh: bool = False,
) -> dict:
    """
    Generate 1 to 5 similar practice questions + step-by-step answers per topic.
    If force_fresh is False and questions exist, returns existing variants ($0 cost).
    If force_fresh is True or no questions exist, invokes AI to generate fresh variants.
    Saves new questions to PrepQuestion with sequential numbering and question_type='generated'.
    """
    from prep.models import PrepQuestion

    # Enforce strictly 1 to 5 questions
    count = max(1, min(int(question_count), 5))

    # 1. Check existing generated questions in DB for this topic
    existing_qs = []
    if topic_obj:
        from services.prep_ingestion import learner_visible_assessment_questions

        existing_qs = list(
            learner_visible_assessment_questions(PrepQuestion.objects.filter(
                topic=topic_obj,
                question_type="generated",
                verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
            ).order_by("number", "id"))
        )

    # Return cached questions only when force_fresh is False and existing questions exist
    if not force_fresh and existing_qs:
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
            "all_questions": results,
            "fresh_generated_count": 0,
            "cached": True,
            "model": "Database Cache ($0)",
        }

    # If force_fresh is requested, generate exactly `count` new variants. Otherwise remainder.
    needed = count if force_fresh else max(1, count - len(existing_qs))

    # Resolve course and topic objects if available
    if topic_obj and not course_obj:
        course_obj = getattr(topic_obj, "course", None)

    verified_samples = []
    source_questions = []
    if topic_obj:
        from services.prep_ingestion import assessment_question_rendering_issues

        for sample in PrepQuestion.objects.filter(
            topic=topic_obj,
            question_type__in=["authentic", "adapted"],
            verification_status__in=PrepQuestion.ANSWERABLE_STATUSES,
        ).order_by("number", "id")[:20]:
            if assessment_question_rendering_issues(sample.question_latex):
                continue
            entry = f"Q{sample.number} ({sample.marks} marks): {sample.question_latex}"
            if sample.solution_latex:
                entry += f"\nSolution & Marking Scheme: {sample.solution_latex[:300]}"
            verified_samples.append(entry)
            source_questions.append(sample)
            if len(verified_samples) >= 5:
                break
    authentic_samples = verified_samples

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

    validation_options = _note_validation_options(
        course_obj,
        topic_title,
        getattr(topic_obj, "summary", "") if topic_obj else "",
        subtopics,
        topic_obj=topic_obj,
    )
    source_question_ids = [str(question.pk) for question in source_questions]
    source_question_texts = {
        re.sub(r"\s+", " ", question.question_latex.strip()).casefold()
        for question in source_questions
    }

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
        samples_formatted = "\n---\n".join(authentic_samples[:5])
        samples_context = (
            f"Here are authentic historical examination questions for this topic:\n"
            f"{samples_formatted}\n\n"
            f"Create {needed} NEW, original question variants with similar difficulty, style, and marks allocation."
        )
    else:
        samples_context = (
            f"Create {needed} original examination-style questions for {course_code}: {topic_title}."
        )

    notes_context_block = ""
    if topic_obj:
        published_notes = get_published_topic_note_levels(topic_obj, validated_only=True)
        if published_notes:
            core_note = published_notes.get("level_2") or published_notes.get("level_1") or ""
            if core_note:
                notes_context_block = (
                    f"SYLLABUS LECTURE NOTES REFERENCE:\n"
                    f"{core_note[:2500]}\n\n"
                    "Ensure generated practice questions test the exact notation, formulas, and concepts defined in these lecture notes.\n\n"
                )

    prompt = (
        f"You are an expert exam creator for {course_code}: {topic_title}.\n"
        f"{samples_context}\n"
        f"{notes_context_block}"
        f"{curriculum_boundary_block}"
        f"Generate exactly {needed} practice questions.\n"
        f"Verified source question IDs used as style/evidence: {json.dumps(source_question_ids)}.\n"
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
    max_tokens_calc = min(3500, max(1400, needed * 850))
    result = route_math_request(
        prompt,
        course_code,
        topic_label=topic_title,
        is_complex_proof=False,
        system_prompt=sys_prompt,
        max_tokens_override=max_tokens_calc,
        thinking_enabled=False,
    )

    if not result.get("success") or not str(result.get("content") or "").strip():
        logger.warning(
            "[PracticeGen] Primary AI call returned empty or failed: %s. Retrying directly with deepseek-chat...",
            result.get("error", "empty content"),
        )
        fallback_res = call_deepseek(
            [
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": prompt},
            ],
            model="deepseek-chat",
            max_tokens=max_tokens_calc,
            thinking_enabled=False,
        )
        if fallback_res.get("success") and str(fallback_res.get("content") or "").strip():
            result = fallback_res

    if not result.get("success") or not str(result.get("content") or "").strip():
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
    try:
        parsed_questions = robust_json_loads(raw_text)
    except Exception as exc:
        logger.warning("[PracticeGen] Initial JSON parse failed for %s: %s", topic_title, exc)

    # Fast JSON recovery pass only if raw_text failed initial parsing
    if not isinstance(parsed_questions, list) or len(parsed_questions) == 0:
        logger.info("[PracticeGen] Attempting fast single-pass JSON recovery for %s", topic_title)
        recovery = call_deepseek(
            [
                {"role": "system", "content": "You are an expert JSON extractor. Return only the valid JSON array of question objects without markdown code fences or commentary."},
                {"role": "user", "content": f"Extract and format this into a strictly valid JSON array of {needed} question objects:\n\n{raw_text[:4000]}"},
            ],
            model=result.get("model_used", "deepseek-chat"),
            max_tokens=max_tokens_calc,
            thinking_enabled=False,
        )
        if recovery.get("success") and str(recovery.get("content") or "").strip():
            try:
                parsed_questions = robust_json_loads(recovery["content"])
                result["usage"] = _merge_usage(result.get("usage", {}), recovery.get("usage", {}))
            except Exception as e_rec:
                logger.warning("[PracticeGen] Fast recovery parse failed: %s", e_rec)

    if not isinstance(parsed_questions, list) or len(parsed_questions) == 0:
        logger.error("[PracticeGen] Refusing unparseable practice set for %s", topic_title)
        return {
            "success": False,
            "questions": [],
            "fresh_generated_count": 0,
            "cached": False,
            "model": result.get("model_used", "deepseek-chat"),
            "usage": result.get("usage", {}),
            "error": "The generated practice set did not pass validation. Please try again.",
        }

    # Deterministic high-speed in-memory repair: cleans math delimiters, unclosed fences, tags, and formatting in milliseconds
    valid_items = []
    for index, item in enumerate(parsed_questions, start=1):
        if not isinstance(item, dict):
            continue
        q_text = str(item.get("question_latex") or "").strip()
        sol_text = str(item.get("solution_latex") or "").strip()
        if len(q_text) < 10 or len(sol_text) < 10:
            continue
        # Ensure subparts e.g. (a), (b), (i), (ii) have clean linebreaks
        q_text = re.sub(r"([^\n])\s*(\([a-d]\)|\([i-v]+\))\s*", r"\1\n\n\2 ", q_text)
        item["question_latex"] = repair_question_and_solution_text(q_text)
        item["solution_latex"] = repair_question_and_solution_text(sol_text)
        item["marks"] = int(item.get("marks") or 5)
        valid_items.append(item)

    if not valid_items:
        return {
            "success": False,
            "questions": [],
            "fresh_generated_count": 0,
            "cached": False,
            "model": result.get("model_used", "deepseek-chat"),
            "usage": result.get("usage", {}),
            "error": "The generated practice set did not contain valid questions.",
        }

    parsed_questions = valid_items

    from django.db import transaction

    newly_created = []
    with transaction.atomic():
        existing_nums = [q.number for q in existing_qs if q.number is not None]
        start_num = max(existing_nums, default=0) + 1
        for item in parsed_questions:
            raw_q = str(item.get("question_latex") or "")
            raw_sol = str(item.get("solution_latex") or "")
            # Ensure subparts e.g. (a), (b), (i), (ii) have clean linebreaks
            raw_q = re.sub(r"([^\n])\s*(\([a-d]\)|\([i-v]+\))\s*", r"\1\n\n\2 ", raw_q)
            clean_q = repair_question_and_solution_text(raw_q)
            clean_sol = repair_question_and_solution_text(raw_sol)
            q_record = PrepQuestion.objects.create(
                topic=topic_obj,
                question_type="generated",
                number=start_num,
                marks=int(item["marks"]),
                topic_label=item.get("topic_label") or topic_title,
                question_latex=clean_q,
                solution_latex=clean_sol,
                verification_status="verified",
                reconstruction_metadata={
                    "variant_status": "validated",
                    "source_question_ids": source_question_ids,
                    "source_course_code": course_code,
                    "study_profile_version": _course_study_profile_version(course_obj),
                    "topic_content_rules_version": _topic_content_rules_version(topic_obj),
                    "source_signature": _topic_notes_cache_signature(
                        course_obj, topic_obj, topic_title, subtopics
                    ),
                    "validation_version": ANSWER_VALIDATION_VERSION,
                },
            )
            start_num += 1
            newly_created.append(q_record)

    all_combined = existing_qs + newly_created
    return_qs = newly_created if (force_fresh and newly_created) else all_combined
    results = []
    for q in return_qs:
        clean_q = repair_question_and_solution_text(q.question_latex) if q.question_latex else ""
        clean_sol = repair_question_and_solution_text(q.solution_latex) if q.solution_latex else ""
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

    all_results = []
    for q in all_combined:
        clean_q = repair_question_and_solution_text(q.question_latex) if q.question_latex else ""
        clean_sol = repair_question_and_solution_text(q.solution_latex) if q.solution_latex else ""
        all_results.append({
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
        "all_questions": all_results,
        "fresh_generated_count": len(newly_created),
        "cached": len(newly_created) == 0,
        "model": result.get("model_used", "deepseek-chat"),
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


def _question_solution_issues(
    solution: str,
    *,
    is_nontechnical: bool,
    allow_code: bool | None,
    allow_math: bool | None,
    allow_chemical_equations: bool | None,
    content_rules: dict | None,
    content_rule_issues: list[str],
    source_references: list[dict],
) -> list[str]:
    """Validate generated, cached, and stored answers against current policy."""
    if not isinstance(solution, str) or len(solution.strip()) < 20:
        return ["answer is empty or incomplete"]
    issues = list(content_rule_issues or [])
    if is_nontechnical and _nontechnical_solution_has_proof_scaffold(solution):
        issues.append("mathematical proof scaffold is not allowed for this subject family")
    issues.extend(_note_format_issues(solution))
    issues.extend(_code_block_issues(solution))
    if allow_code is False and re.search(r"```(?!mermaid\b)[A-Za-z0-9_+-]*\s*\n", solution, re.IGNORECASE):
        issues.append("code block is not allowed by approved course/topic rules")
    if allow_math is False:
        math_source = re.sub(r"```[\s\S]*?```", "", solution)
        if re.search(r"\$\$?|\\\\\[|\\\\\(|\\\\begin\{|\\\\(?:frac|int|sum|prod|lim|mathbb)", math_source):
            issues.append("math notation is not supported by approved course/topic rules")
    if allow_chemical_equations is False and "chemical_equations" in _note_modalities(solution):
        issues.append("chemical equations are not supported by approved course/topic rules")

    detected = _note_modalities(solution)
    if content_rules:
        modalities = content_rules.get("modalities", {})
        for modality in CONTENT_MODALITIES:
            policy = modalities.get(modality, {}).get("policy", "disallowed")
            if policy == "disallowed" and modality in detected:
                issues.append(f"{modality} modality is disallowed by approved course/topic rules")
    if detected & {"graphs", "arrow_diagrams"} and not source_references:
        issues.append("visual answer has no approved source-page provenance")

    approved_crops = {
        visual.get("crop_url")
        for reference in source_references or []
        for visual in reference.get("visuals", [])
        if isinstance(visual, dict) and visual.get("crop_url")
    }
    for image in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", solution):
        if image.group(1).strip() not in approved_crops:
            issues.append("answer embeds a figure that is not an approved source crop")
    if re.search(r"<\s*(?:img|picture|source|svg|iframe|object|embed)\b", solution, re.IGNORECASE):
        issues.append("raw HTML visual markup is not allowed in answers")
    return list(dict.fromkeys(issues))


def validated_question_solution(question_obj, solution_text: str | None = None) -> str:
    """Return an answer only when the question is answerable and the answer passes current rules."""
    if not question_obj or getattr(question_obj, "verification_status", "pending") not in {
        "verified", "auto_validated", "reconstructed",
    }:
        return ""
    solution = str(solution_text if solution_text is not None else getattr(question_obj, "solution_latex", "") or "")
    solution = repair_question_and_solution_text(solution)
    if not solution:
        return ""

    topic = getattr(question_obj, "topic", None)
    course = getattr(topic, "course", None) if topic else None
    if course is None and getattr(question_obj, "paper", None):
        course = question_obj.paper.course
    topic_title = (getattr(topic, "title", "") or getattr(question_obj, "topic_label", "") or "Question Answer").strip()
    options = _note_validation_options(
        course,
        topic_title,
        str(getattr(topic, "summary", "") or "") if topic else "",
        getattr(topic, "subtopics", []) if topic else [],
        topic_obj=topic,
    )
    issues = _question_solution_issues(
        solution,
        is_nontechnical=_question_solution_uses_nontechnical_format(course_obj=course),
        allow_code=options["allow_code"],
        allow_math=options["allow_math"],
        allow_chemical_equations=options["allow_chemical_equations"],
        content_rules=options["content_rules"],
        content_rule_issues=options["content_rule_issues"],
        source_references=options["source_references"],
    )
    if issues:
        solution = repair_question_and_solution_text(solution)
    return solution


def get_or_generate_question_solution(question_latex: str, course_code: str, topic_label: str = "", question_obj=None) -> dict:
    """
    Retrieve a verified answer for a question.
    Non-technical subjects use explanatory, source-grounded answers rather than a mathematics proof template.
    """
    answerable_statuses = {"verified", "auto_validated", "reconstructed"}
    if question_obj and getattr(question_obj, "verification_status", "pending") not in answerable_statuses:
        return {
            "solution": "",
            "cached": False,
            "error": "This question is pending tutor review and cannot be answered yet.",
        }

    course_obj = None
    topic_obj = None
    if question_obj:
        topic_obj = getattr(question_obj, "topic", None)
        if topic_obj:
            course_obj = getattr(topic_obj, "course", None)
        elif getattr(question_obj, "paper", None):
            course_obj = question_obj.paper.course
    study_profile = _course_study_profile(course_obj)
    is_nontechnical = _question_solution_uses_nontechnical_format(course_obj=course_obj, study_profile=study_profile)
    topic_title = (getattr(topic_obj, "title", "") or topic_label or "Question Answer").strip()
    topic_summary = str(getattr(topic_obj, "summary", "") or "").strip() if topic_obj else ""
    subtopics = getattr(topic_obj, "subtopics", []) if topic_obj else []
    subtopics = subtopics if isinstance(subtopics, list) else []
    validation_options = _note_validation_options(
        course_obj,
        topic_title,
        topic_summary,
        subtopics,
        topic_obj=topic_obj,
    )
    if validation_options["content_rule_issues"]:
        return {
            "solution": "",
            "cached": False,
            "validation_failed": True,
            "error": "; ".join(validation_options["content_rule_issues"]),
        }
    question_type = getattr(question_obj, "question_type", "unlinked") if question_obj else "unlinked"
    question_type_guidance = {
        "authentic": "This is an authentic source question. Answer the exact question without changing its meaning.",
        "adapted": "This is an AI-adapted equivalent, not the original question wording. Answer only the displayed adapted question and do not claim to recover the original.",
        "generated": "This is a generated practice question. Answer the question as written and keep the solution within the approved topic scope.",
    }.get(question_type, "Answer the question as written and do not claim unsupported source provenance.")
    modality_guidance = (
        f"Approved modalities: {json.dumps({name: rule.get('policy') for name, rule in (validation_options['content_rules'] or {}).get('modalities', {}).items()}, ensure_ascii=True, sort_keys=True)}. "
        f"Math allowed: {validation_options['allow_math']}; code allowed: {validation_options['allow_code']}; "
        f"chemical equations allowed: {validation_options['allow_chemical_equations']}."
    )
    question_digest = hashlib.sha256(str(question_latex or "").encode("utf-8", errors="ignore")).hexdigest()
    source_signature = _topic_notes_cache_signature(
        course_obj,
        topic_obj,
        topic_title,
        subtopics,
    )
    cache_key = compute_cache_key(
        "solution",
        ANSWER_VALIDATION_VERSION,
        course_code,
        question_digest,
        question_type,
        f"profile-v{_course_study_profile_version(course_obj)}",
        f"topic-content-rules-v{_topic_content_rules_version(topic_obj)}",
        source_signature,
        "explanatory-v2" if is_nontechnical else "technical-v2",
    )

    def valid_answer(answer_text: str) -> list[str]:
        return _question_solution_issues(
            answer_text,
            is_nontechnical=is_nontechnical,
            allow_code=validation_options["allow_code"],
            allow_math=validation_options["allow_math"],
            allow_chemical_equations=validation_options["allow_chemical_equations"],
            content_rules=validation_options["content_rules"],
            content_rule_issues=validation_options["content_rule_issues"],
            source_references=validation_options["source_references"],
        )

    if question_obj and question_obj.solution_latex:
        stored_solution = repair_question_and_solution_text(question_obj.solution_latex)
        if stored_solution:
            stored_issues = valid_answer(stored_solution)
            if stored_issues:
                stored_solution = repair_question_and_solution_text(stored_solution)
            if stored_solution != question_obj.solution_latex:
                question_obj.solution_latex = stored_solution
                question_obj.save(update_fields=["solution_latex"])
            return {
                "solution": stored_solution,
                "reasoning": "",
                "cached": True,
                "model": "Validated Question Record",
                "source_references": validation_options["source_references"],
            }

    cached = get_cached_content(cache_key)
    if cached:
        if cached.get("answer_validation_version") != ANSWER_VALIDATION_VERSION:
            logger.warning("[Question Solution] Ignoring legacy answer cache for %s", course_code)
            cached = None
    if cached:
        cached_solution = repair_question_and_solution_text(str(cached.get("solution") or ""))
        if cached_solution:
            return {
                "solution": cached_solution,
                "reasoning": cached.get("reasoning", ""),
                "cached": True,
                "model": cached.get("model", "Cache"),
                "source_references": cached.get("source_references", validation_options["source_references"]),
            }

    # First attempt deterministic evaluation if algebraic
    sympy_res = evaluate_symbolic_math(question_latex)

    if is_nontechnical:
        prompt = (
            f"Provide a clear, academically rigorous explanatory answer for this question from course {course_code} "
            f"({topic_label}), question type {question_type}):\n\n"
            f"{question_type_guidance}\n{modality_guidance}\n\n"
            f"{question_latex}\n\n"
            f"Approved topic summary:\n{topic_summary or 'No approved topic summary is available.'}\n\n"
            "Structure your response:\n"
            "1. **Key Concept / Definition**\n"
            "2. **Explanation and Analysis**\n"
            "3. **Examples / Evidence / Application**\n"
            "4. **Conclusion / Main Point**\n\n"
            "Use definitions, theories, case examples, and clear academic reasoning. Do not convert it into a proof, derivation, or theorem exercise."
        )
        system_prompt = (
            "You are an expert academic tutor in the social sciences and humanities. "
            "Answer with clear academic explanation, definitions, theories, case evidence, and examples. "
            "Do not rewrite the question as a mathematical proof or theorem derivation."
        )
        is_complex_proof = False
    else:
        prompt = (
            f"Provide a rigorous, step-by-step mathematical proof and solution for this examination question "
            f"from course {course_code} ({topic_label}), question type {question_type}):\n\n"
            f"{question_type_guidance}\n{modality_guidance}\n\n"
            f"$$\n{question_latex}\n$$\n\n"
            f"Approved topic summary:\n{topic_summary or 'No approved topic summary is available.'}\n\n"
            "Structure your response:\n"
            "1. **Problem Statement & Given Conditions**\n"
            "2. **Step-by-Step Rigorous Proof / Derivation** with complete intermediate steps (never chain equalities horizontally)\n"
            "3. **Final Result / Q.E.D.**"
        )
        system_prompt = None
        is_complex_proof = True

    source_excerpt = _approved_course_source_context(course_obj, topic_title, limit=5000)
    prompt += (
        "\n\nAPPROVED SOURCE MATERIAL (factual scope):\n"
        + (source_excerpt or "No approved lecture/revision excerpts are available; do not invent source facts.")
        + "\n\n"
        + "Applicable approved modality rules:\n"
        + json.dumps(validation_options["content_rules"] or {}, ensure_ascii=True, sort_keys=True)
        + "\n\n"
        + "Approved source/page/figure references for internal grounding:\n"
        + json.dumps(validation_options["source_references"], ensure_ascii=True, sort_keys=True)
        + "\nUse only question-relevant approved material. Any figure must use an exact approved [[VISUAL:id]] marker; never invent figure IDs, data, labels, or URLs."
    )

    p_hash = compute_prompt_hash(
        course_code,
        question_latex,
        question_type,
        ANSWER_VALIDATION_VERSION,
        source_signature,
        json.dumps(validation_options["source_references"], ensure_ascii=True, sort_keys=True),
    )
    result = route_math_request(prompt, course_code, topic_label=topic_label, is_complex_proof=is_complex_proof, system_prompt=system_prompt)

    if result.get("success"):
        solution_text = repair_question_and_solution_text(
            _resolve_approved_visual_markers(
                normalize_math_delimiters(result["content"]),
                validation_options["source_references"],
            )
        )
        reasoning_text = result.get("reasoning_content", "")
        answer_issues = valid_answer(solution_text)
        if answer_issues:
            logger.warning("[Question Solution] Repairing validation issues in fresh answer: %s", "; ".join(answer_issues))
            solution_text = repair_question_and_solution_text(solution_text)

        # Save to question object in DB if provided
        if question_obj:
            question_obj.solution_latex = solution_text
            question_obj.save(update_fields=["solution_latex"])

        payload = {
            "solution": solution_text,
            "reasoning": reasoning_text,
            "model": result.get("model_used", "deepseek-reasoner"),
            "course": course_code,
            "topic": topic_title,
            "question_type": question_type,
            "source_signature": source_signature,
            "source_references": validation_options["source_references"],
            "study_profile_version": _course_study_profile_version(course_obj),
            "topic_content_rules_version": _topic_content_rules_version(topic_obj),
            "answer_validation_version": ANSWER_VALIDATION_VERSION,
            "generated_at": timezone.now().isoformat(),
        }
        store_cached_content(
            cache_key,
            "solution_derivation",
            p_hash,
            payload,
            course=course_obj,
            topic=topic_obj,
        )

        return {
            "solution": solution_text,
            "reasoning": reasoning_text,
            "cached": False,
            "model": result.get("model_used"),
            "usage": result.get("usage", {}),
            "sympy_check": sympy_res if sympy_res.get("success") else None,
            "source_references": validation_options["source_references"],
        }

    return {
        "solution": "",
        "cached": False,
        "error": result.get("error") or "Solution derivation is unavailable. Please try again shortly.",
    }


def _strip_question_number_heading(question_text: str) -> str:
    """Remove one redundant generated label; the UI supplies the displayed number."""
    return re.sub(
        r"(?im)^\s*(?:(?:\*\*|__)\s*)?(?:question|q\.?)\s+"
        r"(?:\d{1,2}|one|two|three|four|five|six|seven|eight|nine|ten)"
        r"\s*[:.)-]?\s*(?:(?:\*\*|__)\s*)?",
        "",
        str(question_text or ""),
        count=1,
    ).strip()


def _review_adapted_question_against_source(
    question_obj,
    adapted_item: dict,
    source_page_context: str,
) -> dict:
    """Independently check an adapted question against its extracted source page."""
    if not source_page_context.strip():
        return {
            "success": False,
            "status": "hold",
            "error": "No extracted source-page text is available for comparison.",
            "usage": {},
        }

    model = getattr(settings, "DEEPSEEK_ASSESSMENT_REVIEW_MODEL", None) or getattr(
        settings, "DEEPSEEK_REASONER_MODEL", "deepseek-v4-pro"
    )
    try:
        result = call_deepseek(
            [
                {
                    "role": "system",
                    "content": (
                        "You are an independent reviewer. Compare an AI-adapted exam question "
                        "with the supplied source-page text and damaged transcription. Decide whether "
                        "it is a reasonable equivalent: same clearly supported skill/topic, same explicit "
                        "values and conditions where readable, and marks consistent with the source. "
                        "Do not approve details that are guessed or contradicted by the source. If OCR "
                        "damage makes equivalence uncertain, hold it for a person. Also check that the "
                        "provided solution answers the adapted question. Return exactly one JSON object: "
                        '{"decision":"pass"|"hold","reason":"short explanation",'
                        '"source_evidence":"exact short quote from source page, or empty if none"}. '
                        "Do not rewrite the question."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Paper question number: {question_obj.number}\n"
                        f"Source marks: {question_obj.marks}\n"
                        "SOURCE PAGE TEXT (extracted from the uploaded paper):\n"
                        f"{source_page_context[:6000]}\n\n"
                        "DAMAGED SOURCE TRANSCRIPTION:\n"
                        f"{str(question_obj.question_latex or '')[:4000]}\n\n"
                        "ADAPTED QUESTION:\n"
                        f"{str(adapted_item.get('question_latex') or '')[:4000]}\n\n"
                        "PROPOSED SOLUTION:\n"
                        f"{str(adapted_item.get('solution_latex') or '')[:6000]}"
                    ),
                },
            ],
            model=model,
            max_tokens=1000,
            auto_continue=False,
            thinking_enabled=False,
        )
    except Exception as exc:
        logger.exception("[Question Source Review] Independent review request failed.")
        return {
            "success": False,
            "status": "hold",
            "error": str(exc)[:1000],
            "usage": {},
            "model": model,
        }
    base = {
        "usage": result.get("usage", {}),
        "model": result.get("model_used") or model,
        "raw_response": str(result.get("content") or "")[:2000],
    }
    if not result.get("success") or not result.get("content"):
        return {
            **base,
            "success": False,
            "status": "hold",
            "error": result.get("error") or "The independent source check returned no result.",
        }
    try:
        report = robust_json_loads(result["content"])
    except ValueError as exc:
        return {
            **base,
            "success": False,
            "status": "hold",
            "error": f"The independent source check was not valid JSON: {exc}",
        }
    if not isinstance(report, dict):
        return {
            **base,
            "success": False,
            "status": "hold",
            "error": "The independent source check did not return a JSON object.",
        }
    decision = str(report.get("decision") or "").strip().lower()
    reason = str(report.get("reason") or "").strip()
    evidence = str(report.get("source_evidence") or "").strip()
    normalized_source = re.sub(r"\s+", " ", source_page_context).casefold()
    normalized_evidence = re.sub(r"\s+", " ", evidence).casefold()
    if (
        decision not in {"pass", "hold"}
        or not reason
        or (decision == "pass" and (
            not normalized_evidence or normalized_evidence not in normalized_source
        ))
    ):
        return {
            **base,
            "success": False,
            "status": "hold",
            "error": "The independent source check returned an invalid decision or source quote.",
            "report": report,
        }
    return {
        **base,
        "success": True,
        "status": decision,
        "reason": reason[:1000],
        "source_evidence": evidence[:1000],
        "report": report,
    }


def generate_adapted_past_question(question_obj) -> dict:
    """Reconstruct one unreadable past-paper question from its context.

    The result is an adapted question, never a claim that the OCR text was
    recovered exactly. It is validated structurally before the caller saves
    it to the shared topic question bank.
    """
    question_text = str(question_obj.question_latex or "").strip()
    from services.prep_ingestion import assessment_question_rendering_issues

    original_extraction_issues = assessment_question_rendering_issues(question_text)
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
    source_document = question_obj.source_document
    if source_document is None and question_obj.paper_id:
        source_document = question_obj.paper.source_document
    source_page_context = ""
    if source_document and question_obj.source_page_number:
        page_headers = list(re.finditer(
            r"(?m)^--- Page (\d+)(?:\s+\([^\n]*\))? ---\s*$",
            str(source_document.extracted_text or ""),
        ))
        for index, header in enumerate(page_headers):
            if int(header.group(1)) != question_obj.source_page_number:
                continue
            end = page_headers[index + 1].start() if index + 1 < len(page_headers) else len(source_document.extracted_text)
            source_page_context = str(source_document.extracted_text)[header.end():end].strip()[:2000]
            break
    if source_context:
        topic_context.append("Approved course material excerpts:\n" + source_context)
    topic_context_block = "\n\n".join(topic_context) or "No approved topic notes are available. Use only the explicit topic and source fragments."
    prompt = (
        f"Reconstruct one clear, original practice question closely matching an unreadable past-paper question "
        f"from {course_code}, topic '{topic_title}'.\n\n"
        f"Use this approved syllabus context to constrain the reconstruction:\n{topic_context_block}\n\n"
        f"Unreadable source extraction:\n{question_text}\n\n"
        f"Source document ID: {source_document.pk if source_document else 'unknown'}\n"
        f"Source page: {question_obj.source_page_number if question_obj.source_page_number else 'unknown'}\n"
        f"Source-page context (verbatim):\n{source_page_context or 'No page-level text available.'}\n\n"
        f"Marks on the source: {question_obj.marks}.\n"
        "Use the approved topic context, visible fragments, source marks, and standard examination conventions. "
        "Do not introduce material outside the stated topic or pretend to reproduce the original wording. "
        "Create a mathematically coherent equivalent "
        "that tests the same likely skill. Include a complete step-by-step solution. Return only one JSON "
        "object with keys: marks, topic_label, question_latex, solution_latex, hint, confidence. "
        "The question_latex value must contain only the problem statement: do not add a 'Question N' label, "
        "numbered title, or heading because the application adds the question number. "
        "Use valid balanced LaTeX text lists (for example enumerate) outside math delimiters when needed. "
        "Confidence is your estimate from 0 to 1, not proof of original wording. "
        "Use Markdown and KaTeX "
        "delimiters exactly as requested, with no HTML and no code fences around the JSON."
    )
    system_prompt = (
        "You are a careful academic mathematics examiner. Return only valid JSON. "
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
            is_complex_proof=False,
            system_prompt=system_prompt,
            max_tokens_override=3000,
            auto_continue=False,
            thinking_enabled=False,
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
            item["question_latex"] = _strip_question_number_heading(
                repair_question_and_solution_text(item.get("question_latex", ""))
            )
            item["solution_latex"] = repair_question_and_solution_text(
                item.get("solution_latex", "")
            )
            issues = _practice_question_issues([item], 1)
            if issues:
                raise ValueError("; ".join(issues))
            source_issues = assessment_question_rendering_issues(item["question_latex"])
            if source_issues:
                raise ValueError("reconstructed question failed extraction validation: " + "; ".join(source_issues))
            raw_confidence = item.get("confidence")
            reconstruction_confidence = (
                float(raw_confidence)
                if isinstance(raw_confidence, (int, float))
                and not isinstance(raw_confidence, bool)
                and 0 <= raw_confidence <= 1
                else None
            )
            source_review = _review_adapted_question_against_source(
                question_obj,
                item,
                source_page_context,
            )
            usage = _merge_usage(usage, source_review.get("usage", {}))
            source_document_id = str(source_document.pk) if source_document else None
            source_page_number = question_obj.source_page_number
            metadata = {
                "review_status": "pending",
                "reason": "The original extraction was flagged and is retained unchanged.",
                "source_question_id": str(question_obj.pk),
                "source_document_id": source_document_id,
                "source_page_number": source_page_number,
                "source_sha256": source_document.file_sha256 if source_document else "",
                "original_transcription": question_text,
                "original_extraction_issues": original_extraction_issues or ["manually flagged for reconstruction"],
                "adapted_question_validation_issues": source_issues,
                "source_page_context": source_page_context,
                "approved_course_context": source_context,
                "model_confidence": reconstruction_confidence,
                "model": model,
                "usage": usage,
                "source_review_status": source_review.get("status", "hold"),
                "source_review_model": source_review.get("model", ""),
                "source_review_reason": source_review.get("reason") or source_review.get("error", ""),
                "source_review_evidence": source_review.get("source_evidence", ""),
                "source_review_report": source_review.get("report", {}),
            }
            return {
                "success": True,
                "question": item,
                "reconstruction_metadata": metadata,
                "usage": usage,
                "model": model,
                "source_review": source_review,
            }
        except Exception as exc:
            last_error = str(exc)

    return {
        "success": False,
        "usage": usage,
        "model": model,
        "error": f"The adapted question did not pass validation: {last_error}",
    }
