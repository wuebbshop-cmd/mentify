"""Source-linked format and modality validation for extracted course documents."""

from __future__ import annotations

from collections.abc import Mapping
import re

from prep.content_rules import resolve_content_rules
from services.prep_blocks import split_markdown_table_row


_PAGE_HEADER_RE = re.compile(r"(?m)^--- Page (\d+)(?:\s+\([^\n]*\))? ---\s*$")
_CODE_FENCE_RE = re.compile(r"(?m)^```([^\n]*)\n([\s\S]*?)^```[ \t]*$")
_CODE_LANGUAGES = {
    "bash", "c", "c++", "c#", "csharp", "cpp", "csharp", "css", "go", "html",
    "java", "javascript", "js", "json", "julia", "kotlin", "lua", "markdown", "php",
    "powershell", "ps1", "python", "py", "r", "rscript", "ruby", "rust", "scala",
    "scheme", "shell", "sql", "swift", "text", "typescript", "ts", "xml", "yaml", "yml",
}
_VISUAL_REFERENCE_RE = re.compile(r"(?i)\b(?:figure|fig\.?|graph|plot|diagram|flow[\s-]*chart)\b")
_CHEMICAL_ARROW_RE = re.compile(r"<=>|⇌|↔|->|→")
_CHEMICAL_SPECIES_RE = re.compile(r"(?<![A-Za-z])[A-Z][a-z]?\d*(?:\([aqslg]+\))?")
_MATH_ENVIRONMENT_RE = re.compile(
    r"\\begin\{(?:aligned|align\*?|cases|matrix|pmatrix|bmatrix|vmatrix|gather|split|array)\}"
)


def _attribute(value, name, default=None):
    if isinstance(value, Mapping):
        return value.get(name, default)
    return getattr(value, name, default)


def _split_document_pages(text: str) -> dict[int, str]:
    matches = list(_PAGE_HEADER_RE.finditer(text))
    if not matches:
        return {1: text} if text else {}
    pages = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        pages[int(match.group(1))] = text[match.end():end].strip()
    return pages


def _has_markdown_table(page_text: str) -> bool:
    lines = page_text.splitlines()
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
            return True
    return False


def _has_equations(page_text: str) -> bool:
    without_code = _CODE_FENCE_RE.sub("", page_text)
    return bool(
        re.search(r"\$\$[\s\S]+?\$\$|(?<!\$)\$[^$\n]+\$(?!\$)", without_code)
        or _MATH_ENVIRONMENT_RE.search(without_code)
        or re.search(r"\\(?:frac\b|int\b|sum\b|prod\b|mathbb\b|alpha\b|beta\b)", without_code)
    )


def _chemical_equation_findings(page_text: str) -> tuple[bool, list[str]]:
    without_code = _CODE_FENCE_RE.sub("", page_text)
    found_equation = False
    issues = []
    for match in _CHEMICAL_ARROW_RE.finditer(without_code):
        line_start = without_code.rfind("\n", 0, match.start()) + 1
        line_end = without_code.find("\n", match.end())
        if line_end < 0:
            line_end = len(without_code)
        left = without_code[line_start:match.start()]
        right = without_code[match.end():line_end]
        if _CHEMICAL_SPECIES_RE.search(left) and _CHEMICAL_SPECIES_RE.search(right):
            found_equation = True
        else:
            issues.append("chemical reaction arrow is missing a recognizable formula on one side")
    return found_equation, issues


def _provenance(document, page_number=None, candidate=None) -> dict:
    candidate_id = _attribute(candidate, "pk") or _attribute(candidate, "id")
    bbox = _attribute(candidate, "bbox")
    crop = _attribute(candidate, "crop")
    crop_name = _attribute(crop, "name") or (crop if isinstance(crop, str) else "")
    return {
        "document_id": str(_attribute(document, "pk") or _attribute(document, "id") or ""),
        "source_sha256": _attribute(document, "file_sha256", "") or "",
        "page_number": _attribute(candidate, "page_number") or page_number,
        "visual_candidate_id": str(candidate_id) if candidate_id is not None else None,
        "bbox": bbox if isinstance(bbox, list) else None,
        "crop": crop_name,
    }


def build_document_validation_report(
    document,
    extracted_text: str,
    *,
    visual_candidates=(),
    course_rules=None,
    topic_rules=None,
) -> dict:
    """Inspect extracted content without rewriting it or approving it."""
    from services.prep_ai_router import _note_format_issues

    text = str(extracted_text or "")
    pages = _split_document_pages(text)
    candidates = list(visual_candidates or [])
    issues = []
    detected = set()
    evidence_locations = {}

    def mark_detected(modality, page_number=None, candidate=None):
        detected.add(modality)
        evidence_locations.setdefault(modality, []).append((page_number, candidate))

    def add_issue(code, message, *, page_number=None, candidate=None, modality=None, severity="review"):
        issues.append({
            "code": code,
            "message": message,
            "modality": modality,
            "severity": severity,
            "provenance": _provenance(document, page_number, candidate),
        })

    if not text.strip():
        add_issue("empty_extraction", "No extracted text is available to validate.")

    for page_number, page_text in pages.items():
        if page_text.strip():
            mark_detected("text", page_number)
        if "\ufffd" in page_text:
            add_issue(
                "unreadable_replacement_character",
                "Text contains an unknown replacement character; preserve the source and review the original page.",
                page_number=page_number,
            )

        if _has_equations(page_text):
            mark_detected("equations", page_number)
        if re.search(r"\\begin\{tikzpicture\}", page_text):
            mark_detected("arrow_diagrams", page_number)
            if not any(
                _attribute(candidate, "page_number") == page_number
                and _attribute(candidate, "status") != "rejected"
                for candidate in candidates
            ):
                add_issue(
                    "diagram_markup_unlinked",
                    "TikZ diagram markup has no captured source crop linked to this page.",
                    page_number=page_number,
                    modality="arrow_diagrams",
                )
        chemical_found, chemical_issues = _chemical_equation_findings(page_text)
        if chemical_found:
            mark_detected("chemical_equations", page_number)
        for message in chemical_issues:
            add_issue("malformed_chemical_equation", message, page_number=page_number, modality="chemical_equations")

        code_blocks = list(_CODE_FENCE_RE.finditer(page_text))
        if code_blocks:
            mark_detected("code", page_number)
            for index, match in enumerate(code_blocks, start=1):
                language = match.group(1).strip().lower()
                if not language:
                    add_issue(
                        "code_language_missing",
                        f"Code block {index} has no declared language.",
                        page_number=page_number,
                        modality="code",
                    )
                elif language not in _CODE_LANGUAGES:
                    add_issue(
                        "code_language_unknown",
                        f"Code block {index} uses unknown language '{language}'.",
                        page_number=page_number,
                        modality="code",
                    )

        if _has_markdown_table(page_text):
            mark_detected("tables", page_number)
        if any(line.lstrip().startswith("|") for line in page_text.splitlines()):
            from services.prep_ai_router import _markdown_table_issues

            for message in _markdown_table_issues(page_text):
                add_issue("malformed_markdown_table", message, page_number=page_number, modality="tables")

        has_format_markup = any(token in page_text for token in ("$", "```", "\\begin{", "\\[", "\\("))
        has_latex_command = bool(
            re.search(r"\\(?:frac\b|int\b|sum\b|prod\b|mathbb\b|alpha\b|beta\b)", page_text)
        )
        if has_format_markup or has_latex_command:
            for message in _note_format_issues(page_text):
                code = "format_validation"
                if "fenced code" in message:
                    modality = "code"
                elif "math" in message.lower() or "latex" in message.lower() or "escape delimiter" in message:
                    modality = "equations"
                elif "table" in message.lower():
                    modality = "tables"
                else:
                    modality = None
                add_issue(code, message, page_number=page_number, modality=modality)

        if _VISUAL_REFERENCE_RE.search(page_text) and not any(
            _attribute(candidate, "page_number") == page_number
            and _attribute(candidate, "status") != "rejected"
            for candidate in candidates
        ):
            add_issue(
                "visual_reference_unlinked",
                "Page references a visual but has no captured visual crop linked to this page.",
                page_number=page_number,
            )

    for candidate in candidates:
        visual_type = str(_attribute(candidate, "visual_type", "unclassified") or "unclassified").lower()
        status = str(_attribute(candidate, "status", "candidate") or "candidate")
        modality = {"graph": "graphs", "diagram": "arrow_diagrams", "table": "tables"}.get(visual_type)
        if modality:
            mark_detected(modality, candidate=candidate)
        content = _attribute(candidate, "extracted_content", {})
        content = content if isinstance(content, Mapping) else {}

        if visual_type == "unclassified" or status in {"candidate", "needs_review", "error"}:
            add_issue(
                "visual_classification_unresolved",
                "Visual candidate has not been reliably classified; retain its source crop for review.",
                candidate=candidate,
                modality=modality,
            )
        confidence = content.get("confidence", _attribute(candidate, "confidence"))
        if status in {"inspected", "approved"} and (
            isinstance(confidence, bool)
            or not isinstance(confidence, (int, float))
            or not 0.8 <= confidence <= 1
        ):
            add_issue(
                "visual_confidence_below_threshold",
                "Visual confidence is missing, invalid, or below 0.8; retain the crop for tutor review.",
                candidate=candidate,
                modality=modality,
            )
        if visual_type == "graph":
            axes = content.get("axes")
            x_label = axes.get("x_label") or axes.get("x") if isinstance(axes, Mapping) else None
            y_label = axes.get("y_label") or axes.get("y") if isinstance(axes, Mapping) else None
            if not x_label or not y_label:
                add_issue(
                    "graph_axis_labels_missing",
                    "Graph axis labels are missing or unverified; do not infer labels from subject context.",
                    candidate=candidate,
                    modality="graphs",
                )
            units = axes.get("units") if isinstance(axes, Mapping) else None
            if units is not None and not (
                isinstance(units, str)
                or isinstance(units, Mapping) and all(isinstance(value, str) for value in units.values())
            ):
                add_issue(
                    "graph_units_malformed",
                    "Graph units must be source-transcribed text or an axis-to-unit object.",
                    candidate=candidate,
                    modality="graphs",
                )

    rules_status = "missing"
    resolved_rules = None
    if course_rules is not None:
        try:
            resolved_rules = resolve_content_rules(course_rules, topic_rules)
            rules_status = "valid"
        except (TypeError, ValueError) as exc:
            rules_status = "invalid"
            add_issue("content_rules_invalid", str(exc), severity="error")
    else:
        add_issue(
            "approved_content_rules_missing",
            "No approved course modality rules are available; permissions cannot be inferred from the course name or classifier output.",
        )

    if resolved_rules:
        for modality in sorted(detected):
            policy = resolved_rules["modalities"].get(modality, {}).get("policy", "disallowed")
            if policy == "disallowed":
                for page_number, candidate in evidence_locations.get(modality, [(None, None)]):
                    add_issue(
                        "modality_disallowed",
                        f"Detected {modality} content is disallowed by the approved course/topic rules.",
                        page_number=page_number,
                        candidate=candidate,
                        modality=modality,
                        severity="error",
                    )

    status = "needs_review" if issues or rules_status != "valid" else "passed"
    return {
        "schema_version": 1,
        "status": status,
        "rules_status": rules_status,
        "detected_modalities": sorted(detected),
        "source": _provenance(document),
        "issues": issues,
    }


def validate_prep_document(document, extracted_text: str | None = None) -> dict:
    """Validate current document text against only applied course/topic rules."""
    course = _attribute(document, "course")
    profile = _attribute(course, "study_profile", {})
    profile = profile if isinstance(profile, Mapping) else {}
    course_rules = profile.get("content_rules") if _attribute(course, "study_profile_version", 0) else None
    topic_rules = None
    topic_name = str(_attribute(document, "topic_name", "") or "").strip()
    if course_rules and topic_name and course is not None:
        topic = course.topics.filter(title__iexact=topic_name).first()
        topic_rules = topic.content_rules if topic else None
    text = _attribute(document, "extracted_text", "") if extracted_text is None else extracted_text
    visuals = _attribute(document, "visual_candidates", ())
    if hasattr(visuals, "all"):
        visuals = visuals.all()
    return build_document_validation_report(
        document,
        text,
        visual_candidates=visuals,
        course_rules=course_rules,
        topic_rules=topic_rules,
    )