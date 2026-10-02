"""Evidence-gated specifications for reconstructing approved source visuals."""

from __future__ import annotations

from collections.abc import Mapping
from math import isfinite


MIN_RECONSTRUCTION_CONFIDENCE = 0.8


def _value(source, name, default=None):
    if isinstance(source, Mapping):
        return source.get(name, default)
    return getattr(source, name, default)


def _source_provenance(candidate) -> dict:
    document = _value(candidate, "document")
    crop = _value(candidate, "crop")
    bbox = _value(candidate, "bbox", [])
    document_id = _value(document, "pk") or _value(document, "id")
    page_number = _value(candidate, "page_number")
    crop_name = _value(crop, "name") or (crop if isinstance(crop, str) else "")
    bbox_is_valid = (
        isinstance(bbox, (list, tuple))
        and len(bbox) == 4
        and all(isinstance(value, (int, float)) and not isinstance(value, bool) and isfinite(value) for value in bbox)
    )
    return {
        "visual_candidate_id": _value(candidate, "pk") or _value(candidate, "id"),
        "source_document_id": str(document_id) if document_id is not None else "",
        "source_page_number": page_number,
        "source_bbox": list(bbox) if bbox_is_valid else None,
        "source_crop": crop_name,
        "source_file_sha256": _value(document, "file_sha256", ""),
    }


def _decision(status: str, reason: str, source: dict, spec: dict | None = None) -> dict:
    return {"status": status, "reason": reason, "source": source, "spec": spec}


def build_visual_reconstruction_spec(candidate) -> dict:
    """Build a reconstruction spec only from tutor-approved, traceable evidence.

    The policy is subject-agnostic. It preserves source values and relationships
    without inventing labels, units, numeric data, or diagram topology.
    """
    source = _source_provenance(candidate)
    if _value(candidate, "status") != "approved":
        return _decision("blocked", "visual evidence is not tutor-approved", source)

    if (
        not source["source_document_id"]
        or not isinstance(source["source_page_number"], int)
        or source["source_page_number"] < 1
        or not source["source_crop"]
        or source["source_bbox"] is None
    ):
        return _decision("needs_review", "source page and crop provenance are incomplete", source)

    content = _value(candidate, "extracted_content", {})
    if not isinstance(content, Mapping):
        return _decision("needs_review", "inspected visual content is not an object", source)

    visual_type = str(content.get("visual_type") or _value(candidate, "visual_type") or "unclassified").lower()
    candidate_type = str(_value(candidate, "visual_type") or "unclassified").lower()
    if candidate_type != "unclassified" and visual_type != candidate_type:
        return _decision("needs_review", "approved visual type conflicts with the extracted classification", source)

    confidence_values = [
        value for value in (content.get("confidence"), _value(candidate, "confidence"))
        if value is not None
    ]
    if not confidence_values or any(
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not isfinite(value)
        or not 0 <= value <= 1
        for value in confidence_values
    ):
        return _decision("needs_review", "visual confidence is missing or invalid", source)
    confidence = min(confidence_values)
    if confidence < MIN_RECONSTRUCTION_CONFIDENCE:
        return _decision("needs_review", "visual confidence is below the reconstruction threshold", source)

    uncertainties = content.get("uncertainties", [])
    if not isinstance(uncertainties, list) or any(not isinstance(item, str) for item in uncertainties):
        return _decision("needs_review", "visual uncertainties are malformed", source)
    if uncertainties:
        return _decision("needs_review", "source visual has unresolved uncertainties", source)

    labels = content.get("visible_labels", _value(candidate, "labels", []))
    if not isinstance(labels, list) or any(not isinstance(label, str) for label in labels):
        return _decision("needs_review", "visible labels are malformed", source)

    axes = content.get("axes")
    if axes is not None and not isinstance(axes, Mapping):
        return _decision("needs_review", "graph axes are malformed", source)

    numeric_values = content.get("data_points", content.get("visible_numeric_values", []))
    if not isinstance(numeric_values, list):
        return _decision("needs_review", "visible numeric values are malformed", source)

    qualitative_relationships = content.get("qualitative_relationships")
    source_relationships = content.get("relationships", [])
    if (
        (qualitative_relationships is not None and not isinstance(qualitative_relationships, list))
        or not isinstance(source_relationships, list)
    ):
        return _decision("needs_review", "visual relationships are malformed", source)
    relationships = qualitative_relationships or source_relationships
    if any(
        not isinstance(item, str)
        and not (
            isinstance(item, (list, tuple))
            and len(item) == 3
            and all(isinstance(part, str) and part.strip() for part in item)
        )
        for item in relationships
    ):
        return _decision("needs_review", "visual relationships are malformed", source)
    supporting_source_text = _value(candidate, "context_text", "")
    if not isinstance(supporting_source_text, str):
        return _decision("needs_review", "nearby source text is malformed", source)

    base_spec = {
        "visual_type": visual_type,
        "labels": list(labels),
        "axes": dict(axes) if isinstance(axes, Mapping) else None,
        "numeric_values": list(numeric_values),
        "relationships": relationships,
        "confidence": confidence,
        "supporting_source_text": supporting_source_text.strip(),
        "is_reconstruction": True,
        "source_exact": False,
        "requires_source_crop_link": True,
    }

    if visual_type == "graph":
        if numeric_values:
            base_spec["representation"] = "labelled_graph"
            return _decision("ready", "uses only visible source values and labels", source, base_spec)
        if not relationships and not str(content.get("qualitative_summary") or "").strip():
            return _decision("needs_review", "graph has no supported values or qualitative relationships", source)
        base_spec["representation"] = "qualitative_graph"
        base_spec["numeric_values"] = []
        base_spec["schematic"] = True
        return _decision("ready", "qualitative reconstruction uses source-supported relationships only", source, base_spec)

    if visual_type == "diagram":
        is_arrow_triples = bool(relationships) and all(
            isinstance(item, (list, tuple))
            and len(item) == 3
            and all(isinstance(part, str) and part.strip() for part in item)
            for item in relationships
        )
        if not is_arrow_triples:
            return _decision("needs_review", "diagram relationships do not define unambiguous labelled arrows", source)
        base_spec["representation"] = "arrow_diagram"
        base_spec["arrows"] = [list(item) for item in relationships]
        return _decision("ready", "arrow topology is explicit in approved source relationships", source, base_spec)

    if visual_type == "table":
        rows = content.get("table_rows")
        if not isinstance(rows, list) or not rows or any(not isinstance(row, list) for row in rows):
            return _decision("needs_review", "table cell relationships are not structured in the source evidence", source)
        base_spec["representation"] = "source_table"
        base_spec["rows"] = rows
        return _decision("ready", "table rows preserve the approved source cell relationships", source, base_spec)

    return _decision("needs_review", "visual type has no reconstruction policy", source)


def store_visual_reconstruction_proposal(candidate) -> dict:
    """Persist a reviewable reconstruction decision without changing approval state."""
    proposal = build_visual_reconstruction_spec(candidate)
    candidate.reconstruction_proposal = proposal
    candidate.save(update_fields=["reconstruction_proposal", "updated_at"])
    return proposal