"""Validation and resolution for approved, source-grounded content rules."""

from __future__ import annotations

from collections.abc import Mapping


CONTENT_RULES_SCHEMA_VERSION = 1
CONTENT_MODALITIES = (
    "text",
    "equations",
    "chemical_equations",
    "code",
    "graphs",
    "tables",
    "arrow_diagrams",
)
CONTENT_POLICIES = {"required", "allowed", "disallowed"}
CONTENT_COMPLEXITIES = {"basic", "source_level", "extended"}
_COMPLEXITY_ORDER = {"basic": 0, "source_level": 1, "extended": 2}


def validate_content_rule_set(
    rule_set: object,
    *,
    source_document_id: str | None = None,
) -> list[str]:
    """Return schema/provenance issues for a course or topic rule set."""
    if not isinstance(rule_set, Mapping):
        return ["rule set must be an object"]
    if rule_set.get("schema_version") != CONTENT_RULES_SCHEMA_VERSION:
        return [f"schema_version must be {CONTENT_RULES_SCHEMA_VERSION}"]

    modalities = rule_set.get("modalities")
    if not isinstance(modalities, Mapping):
        return ["modalities must be an object"]

    issues: list[str] = []
    for modality, rule in modalities.items():
        if modality not in CONTENT_MODALITIES:
            issues.append(f"unknown modality: {modality}")
            continue
        if not isinstance(rule, Mapping):
            issues.append(f"{modality} rule must be an object")
            continue
        policy = rule.get("policy")
        if policy not in CONTENT_POLICIES:
            issues.append(f"{modality} policy must be required, allowed, or disallowed")
        complexity = rule.get("max_complexity")
        if complexity is not None and complexity not in CONTENT_COMPLEXITIES:
            issues.append(f"{modality} max_complexity is invalid")

        evidence = rule.get("evidence", [])
        if not isinstance(evidence, list):
            issues.append(f"{modality} evidence must be a list")
            evidence = []
        valid_evidence = 0
        for item in evidence:
            if not isinstance(item, Mapping):
                issues.append(f"{modality} evidence entries must be objects")
                continue
            document_id = str(item.get("document_id") or "").strip()
            excerpt = str(item.get("excerpt") or "").strip()
            page = item.get("page")
            if not document_id or not excerpt:
                issues.append(f"{modality} evidence needs document_id and excerpt")
                continue
            if source_document_id and document_id != str(source_document_id):
                issues.append(f"{modality} evidence must reference the approved source document")
                continue
            if page is not None and (not isinstance(page, int) or page < 1):
                issues.append(f"{modality} evidence page must be a positive integer")
                continue
            valid_evidence += 1

        if (
            policy in {"required", "allowed"}
            and not valid_evidence
            and rule.get("evidence_required") is not True
        ):
            issues.append(f"{modality} {policy} rule needs source evidence")
        if policy == "disallowed" and not str(rule.get("rationale") or "").strip() and not valid_evidence:
            issues.append(f"{modality} disallowed rule needs a rationale or evidence")

    return issues


def legacy_course_rules(profile: Mapping | None) -> dict:
    """Build a conservative source-gated rules view for pre-schema profiles."""
    profile = profile if isinstance(profile, Mapping) else {}
    explicit = profile.get("content_rules")
    if isinstance(explicit, Mapping):
        return dict(explicit)

    capabilities = profile.get("capabilities")
    capabilities = capabilities if isinstance(capabilities, Mapping) else {}
    rules = {
        "text": {"policy": "required", "max_complexity": "source_level", "evidence_required": True},
        "equations": {"policy": "allowed", "max_complexity": "source_level", "evidence_required": True},
        "chemical_equations": {"policy": "allowed", "max_complexity": "source_level", "evidence_required": True},
        "code": {"policy": "allowed", "max_complexity": "source_level", "evidence_required": True},
        "graphs": {"policy": "allowed", "max_complexity": "source_level", "evidence_required": True},
        "tables": {"policy": "allowed", "max_complexity": "source_level", "evidence_required": True},
        "arrow_diagrams": {"policy": "allowed", "max_complexity": "source_level", "evidence_required": True},
    }
    # A legacy false flag means the classifier did not detect it; it is not
    # strong enough evidence to create a permanent course-level prohibition.
    for modality, capability in (
        ("equations", "math_notation"),
        ("chemical_equations", "chemical_equations"),
        ("code", "code"),
    ):
        rules[modality]["legacy_detected"] = bool(capabilities.get(capability))
    return {"schema_version": CONTENT_RULES_SCHEMA_VERSION, "modalities": rules}


def resolve_content_rules(course_rules: object, topic_rules: object | None = None) -> dict:
    """Combine a validated course maximum with topic rules that may only narrow it."""
    course_issues = validate_content_rule_set(course_rules)
    if course_issues:
        raise ValueError("Invalid course content rules: " + "; ".join(course_issues))
    if topic_rules:
        topic_issues = validate_content_rule_set(topic_rules)
        if topic_issues:
            raise ValueError("Invalid topic content rules: " + "; ".join(topic_issues))

    course_modalities = course_rules["modalities"]
    topic_modalities = topic_rules.get("modalities", {}) if isinstance(topic_rules, Mapping) else {}
    resolved = {}
    for modality in CONTENT_MODALITIES:
        course_rule = course_modalities.get(modality, {"policy": "disallowed"})
        topic_rule = topic_modalities.get(modality, {})
        course_policy = course_rule.get("policy", "disallowed")
        topic_policy = topic_rule.get("policy", course_policy)
        if course_policy == "disallowed" and topic_policy != "disallowed":
            raise ValueError(f"Topic rule cannot enable course-disallowed modality: {modality}")
        if course_policy == "required" and topic_policy == "disallowed":
            raise ValueError(f"Topic rule cannot disable course-required modality: {modality}")

        complexity_options = [
            value for value in (
                course_rule.get("max_complexity"),
                topic_rule.get("max_complexity"),
            ) if value in CONTENT_COMPLEXITIES
        ]
        maximum_complexity = min(complexity_options, key=_COMPLEXITY_ORDER.get) if complexity_options else None
        resolved[modality] = {
            "policy": "required" if "required" in {course_policy, topic_policy} else topic_policy,
            "max_complexity": maximum_complexity,
            "evidence_required": bool(
                course_rule.get("evidence_required", True)
                or topic_rule.get("evidence_required", True)
            ),
            "evidence": topic_rule.get("evidence") or course_rule.get("evidence", []),
        }
    return {"schema_version": CONTENT_RULES_SCHEMA_VERSION, "modalities": resolved}