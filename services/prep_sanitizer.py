"""
Deterministic Institutional & Lecturer Sanitizer for Mentify Prep.
Purges and generalizes all university names, institution names, lecturer names,
and institutional degree/department levels from notes, questions, syllabus,
and prompts across the entire platform.
"""

from __future__ import annotations

import copy
import logging
import re
from typing import Any

from django.db.models import Q

logger = logging.getLogger(__name__)

# ─── 1. Specific & Generic University / Institution Patterns ─────────────────

_SPECIFIC_UNIVERSITIES = (
    r"Kenyatta\s+University"
    r"|University\s+of\s+Nairobi"
    r"|Jomo\s+Kenyatta\s+University(?:\s+of\s+Agriculture\s+and\s+Technology)?"
    r"|JKUAT"
    r"|Moi\s+University"
    r"|Egerton\s+University"
    r"|Strathmore\s+University"
    r"|Maseno\s+University"
    r"|Chuka\s+University"
    r"|Kisii\s+University"
    r"|Masinde\s+Muliro\s+University(?:\s+of\s+Science\s+and\s+Technology)?"
    r"|MMUST"
    r"|Dedan\s+Kimathi\s+University(?:\s+of\s+Technology)?"
    r"|DKUT"
    r"|Mount\s+Kenya\s+University"
    r"|MKU"
    r"|Technical\s+University\s+of\s+(?:Kenya|Mombasa)"
    r"|TUK|TUM"
    r"|KCA\s+University|KCAU"
    r"|United\s+States\s+International\s+University(?:-Africa)?"
    r"|USIU(?:-Africa)?"
    r"|Catholic\s+University\s+of\s+Eastern\s+Africa|CUEA"
    r"|Daystar\s+University"
    r"|Riara\s+University"
    r"|Kabarak\s+University"
    r"|Multimedia\s+University(?:\s+of\s+Kenya)?"
    r"|University\s+of\s+Kabianga"
    r"|University\s+of\s+Embu"
    r"|University\s+of\s+Eldoret"
    r"|Machakos\s+University"
    r"|Murang'?a\s+University(?:\s+of\s+Technology)?"
    r"|Pwani\s+University"
    r"|Taita\s+Taveta\s+University"
    r"|South\s+Eastern\s+Kenya\s+University|SEKU"
    r"|Kirinyaga\s+University"
    r"|Cooperative\s+University(?:\s+of\s+Kenya)?"
    r"|Africa\s+Nazarene\s+University"
    r"|Zetech\s+University"
    r"|Gretsa\s+University"
    r"|Kenya\s+Methodist\s+University|KeMU"
    r"|St\.?\s*Paul'?s?\s+University"
    r"|Scott\s+Christian\s+University"
    r"|Great\s+Lakes\s+University(?:\s+of\s+Kisumu)?"
    r"|Rongo\s+University"
    r"|Garissa\s+University"
)

# Contextual illustrative example patterns (e.g. "Using Kenyatta University as an illustrative example...")
_EXAMPLE_INSTITUTION_RE = re.compile(
    rf"(?i)\b(?:using|consider(?:ing)?|application\s+to|at|in|such\s+as)\s+(?:the\s+)?(?:{_SPECIFIC_UNIVERSITIES})\s*(?:as\s+(?:an?\s+)?(?:illustrative\s+)?example)?\b"
)

# Header patterns with institution name (e.g. "Social Structure at Kenyatta University")
_HEADING_INSTITUTION_RE = re.compile(
    rf"(?i)(#+\s*|\*\*)(?:(?:Worked\s+)?Application\s*:\s*)?(?:Social\s+(?:Order|Structure)\s+(?:at|in))\s+(?:{_SPECIFIC_UNIVERSITIES})(\*\*)?"
)

# Direct standalone institution mentions
_STANDALONE_INSTITUTION_RE = re.compile(
    rf"(?i)\b(?:{_SPECIFIC_UNIVERSITIES})\b"
)

# ─── 2. Watermarks, Scraped Headers & Download Boilerplate ───────────────────

_WATERMARK_PATTERNS = [
    re.compile(r"(?i)\bDownloaded\s+by\s+[^\n\(\)]*(?:\([^\)]*@?[^\)]*\))?", re.MULTILINE),
    re.compile(r"(?i)\blOMoARcPSD(?:\|\d+)?", re.MULTILINE),
    re.compile(r"(?i)\b(?:Studocu|Course\s*Hero|Scribd)\b[^\n]*", re.MULTILINE),
    re.compile(r"(?i)\bScan(?:ned)?\s+(?:to|with|by)\s+[^\n]+", re.MULTILINE),
    re.compile(r"(?i)\bnot\s+sponsored\s+or\s+endorsed\s+by\s+[^\n]+", re.MULTILINE),
    re.compile(r"(?i)\bKU/ACAD/SOP/[^\s]+", re.MULTILINE),
    re.compile(r"(?i)\b(?:ISO\s*9001(?::\d+)?|Quality\s+Management\s+System)\b[^\n]*", re.MULTILINE),
    re.compile(r"(?i)\bRef\.?\s*:\s*[A-Z0-9\/\.\-]+", re.MULTILINE),
    re.compile(r"(?i)\bVer\.?\s*:\s*\d+(?:\.\d+)?", re.MULTILINE),
]

# ─── 3. Lecturer / Instructor / Author Patterns ──────────────────────────────

_LECTURER_PATTERNS = [
    re.compile(r"(?i)(?:^|[\n;]|\b)\s*(?:lecturer|instructor|course\s+coordinator|examiner|moderator)\s*[:\-]\s*(?:(?:Dr|Prof|Professor|Mr|Mrs|Ms)\.?\s*)?[A-Za-z\s]*?(?=[;\n]|\.\s+[A-Z]|\.|$)", re.MULTILINE),
    re.compile(r"(?i)(?:^|[\n;]|\b)\s*(?:prepared\s+by|compiled\s+by|taught\s+by|author|written\s+by)\s*[:\-]\s*(?:(?:Dr|Prof|Professor|Mr|Mrs|Ms)\.?\s*)?[A-Za-z\s]*?(?=[;\n]|\.\s+[A-Z]|\.|$)", re.MULTILINE),
    re.compile(r"(?i)\b(?:prepared\s+by|compiled\s+by|taught\s+by)\s+(?:Dr\.|Prof\.|Professor|Mr\.|Mrs\.|Ms\.)\s+[A-Za-z]+(?:\s+[A-Za-z]+)?\b"),
    re.compile(r"(?i)\b(?:by\s+Nduta|Nduta)\b", re.MULTILINE),
]

# ─── 4. Institutional Levels, Degree Programs, Department Headers ────────────

_INSTITUTIONAL_LEVEL_PATTERNS = [
    re.compile(r"(?i)^\s*\\textbf\{[^\}]*(?:UNIVERSITY|EXAMINATION|DEGREE|FACULTY|SCHOOL|DEPARTMENT)[^\}]*\}\s*(?:\\\\)?\s*$", re.MULTILINE),
    re.compile(r"(?i)^\s*\\begin\{center\}\s*\\textbf\{[^\}]*\}\s*\\\\\s*\\end\{center\}\s*$", re.MULTILINE),
    re.compile(r"(?i)\bEXAMINATION\s+(?:FOR\s+THE\s+DEGREE\s+OF|PAPER|SESSION)[^\n]*", re.MULTILINE),
    re.compile(r"(?i)\b(?:DEPARTMENT\s+OF\s+[A-Za-z\s]{3,40}|SCHOOL\s+OF\s+[A-Za-z\s]{3,40}|FACULTY\s+OF\s+[A-Za-z\s]{3,40}|COLLEGE\s+OF\s+[A-Za-z\s]{3,40})\b", re.MULTILINE),
    re.compile(r"(?i)\b(?:DEGREE\s+OF\s+BACHELOR\s+OF\s+[A-Za-z\s]{3,40}|BACHELOR\s+OF\s+SCIENCE(?:\s+IN\s+[A-Za-z\s]{3,40})?|BACHELOR\s+OF\s+ARTS(?:\s+IN\s+[A-Za-z\s]{3,40})?|B\.?SC\.?(?:\s+IN\s+[A-Za-z\s]{3,40})?|B\.?A\.?(?:\s+IN\s+[A-Za-z\s]{3,40})?|MASTER\s+OF\s+SCIENCE|MASTER\s+OF\s+ARTS)\b", re.MULTILINE),
    re.compile(r"(?i)\b(?:FIRST|SECOND|THIRD|FOURTH)\s+YEAR\s+(?:FIRST|SECOND)\s+SEMESTER\s+(?:EXAMINATION|EXAM)\b", re.MULTILINE),
    re.compile(r"(?i)\bACADEMIC\s+YEAR\s+\d{4}\s*[/–-]\s*\d{4}\b", re.MULTILINE),
    re.compile(r"(?i)\bEND\s+OF\s+SEMESTER\s+(?:EXAMINATIONS?|EXAMS?)\b", re.MULTILINE),
]


def purge_institutional_metadata(text: str) -> str:
    """
    Deterministic sanitizer that removes or abstracts:
    - Specific and generic university and college names
    - Lecturer, instructor, and author attributions
    - Watermarks (Studocu, lOMoARcPSD, Downloaded by...)
    - Institutional headers, faculties, departments, and degree programs
    """
    if not text or not isinstance(text, str):
        return ""

    cleaned = text

    # 1. Clean watermarks and scrapers
    for pat in _WATERMARK_PATTERNS:
        cleaned = pat.sub("", cleaned)

    # 2. Clean lecturer / author lines
    for pat in _LECTURER_PATTERNS:
        cleaned = pat.sub("", cleaned)

    # 3. Clean institutional level and exam headers
    for pat in _INSTITUTIONAL_LEVEL_PATTERNS:
        cleaned = pat.sub("", cleaned)

    # 4. Contextual headings (e.g. "### 4.3 Worked Application: Social Order at Kenyatta University")
    def _replace_heading(match):
        prefix = match.group(1) or ""
        suffix = match.group(2) or ""
        return f"{prefix}Social Structure in a University Setting{suffix}"

    cleaned = _HEADING_INSTITUTION_RE.sub(_replace_heading, cleaned)

    # 5. Contextual illustrative examples:
    # "Using Kenyatta University as an illustrative example, explain..." -> "Using a higher education institution as an illustrative example, explain..."
    # "at Kenyatta University" -> "in an academic institution"
    # "Application to Kenyatta University:" -> "Application to a Higher Education Institution:"
    def _replace_example(match):
        matched_str = match.group(0)
        lower = matched_str.lower()
        if "using" in lower:
            return "using a higher education institution as an illustrative example"
        elif "application to" in lower:
            return "Application to a Higher Education Institution:"
        elif "consider" in lower:
            return "Consider how social order is established through structure in a university setting"
        elif "at" in lower or "in" in lower:
            return "in a higher education institution"
        return "a higher education institution"

    cleaned = _EXAMPLE_INSTITUTION_RE.sub(_replace_example, cleaned)

    # 6. Standalone institution names
    # Replace remaining mentions with generic academic terms
    cleaned = _STANDALONE_INSTITUTION_RE.sub("a higher education institution", cleaned)

    # 7. Generic University names: "Baraton University" -> "an academic institution"
    cleaned = re.sub(
        r"(?i)\b(?:at|in|of)\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?\s+University\b",
        "in an academic institution",
        cleaned,
    )

    # 8. Clean leftover punctuation or awkward artifacts
    cleaned = re.sub(r":{2,}", ":", cleaned)
    cleaned = re.sub(r"(?i)\binstitution([A-Za-z])", r"institution \1", cleaned)
    cleaned = re.sub(r"(?i)\ba a higher education institution\b", "a higher education institution", cleaned)
    cleaned = re.sub(r"(?i)\ban a higher education institution\b", "a higher education institution", cleaned)
    cleaned = re.sub(r"(?i)\ba an academic institution\b", "an academic institution", cleaned)
    cleaned = re.sub(r"(?i)\bin in an academic institution\b", "in an academic institution", cleaned)
    cleaned = re.sub(r"(?i)\bin in a higher education institution\b", "in a higher education institution", cleaned)
    cleaned = re.sub(r"(?m)^using a higher education institution", "Using a higher education institution", cleaned)
    cleaned = re.sub(r"(?<=\.\s)using a higher education institution", "Using a higher education institution", cleaned)
    cleaned = re.sub(r"\s*\.\s*(?:\.\s*)+", ". ", cleaned)
    cleaned = re.sub(r"\s+([.,;:!?])", r"\1", cleaned)
    cleaned = re.sub(r"[ \t]+", " ", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    cleaned = re.sub(r"(?m)^\s*[-*]\s*$", "", cleaned)

    return cleaned.strip()


def sanitize_notes_blocks(blocks: list) -> list:
    """Recursively sanitize all text fields in note block dictionaries."""
    if not isinstance(blocks, list):
        return []

    cleaned_blocks = []
    for block in blocks:
        if not isinstance(block, dict):
            continue
        b = copy.deepcopy(block)
        if "text" in b and isinstance(b["text"], str):
            b["text"] = purge_institutional_metadata(b["text"])
        if "title" in b and isinstance(b["title"], str):
            b["title"] = purge_institutional_metadata(b["title"])
        if "items" in b and isinstance(b["items"], list):
            b["items"] = [
                purge_institutional_metadata(item) if isinstance(item, str) else item
                for item in b["items"]
            ]
        if "rows" in b and isinstance(b["rows"], list):
            cleaned_rows = []
            for row in b["rows"]:
                if isinstance(row, list):
                    cleaned_rows.append([
                        purge_institutional_metadata(cell) if isinstance(cell, str) else cell
                        for cell in row
                    ])
                else:
                    cleaned_rows.append(row)
            b["rows"] = cleaned_rows
        cleaned_blocks.append(b)
    return cleaned_blocks


def sanitize_data_structure(data: Any) -> Any:
    """Recursively sanitize any nested dict, list, or string structure."""
    if isinstance(data, str):
        return purge_institutional_metadata(data)
    elif isinstance(data, list):
        return [sanitize_data_structure(item) for item in data]
    elif isinstance(data, dict):
        return {k: sanitize_data_structure(v) for k, v in data.items()}
    return data


def sanitize_notes_payload(payload: dict) -> dict:
    """Sanitize entire topic notes payload dictionary recursively."""
    if not isinstance(payload, dict):
        return payload
    return sanitize_data_structure(payload)


def purge_all_institutional_metadata_from_db() -> dict:
    """
    Sweeps the database and purges all institution names, lecturer names,
    and degree/department levels across all relevant tables.
    Uses chunked iteration to prevent MySQL connection timeouts.
    Safe to call repeatedly (idempotent).
    """
    from prep.models import (
        PrepContentCache,
        PrepContentUpdate,
        PrepCourse,
        PrepDocument,
        PrepDocumentVisual,
        PrepQuestion,
        PrepTopic,
        PrepTopicChatMessage,
        PrepTopicQuizQuestion,
    )

    stats = {
        "content_cache": 0,
        "questions": 0,
        "topics": 0,
        "courses": 0,
        "chat_messages": 0,
        "content_updates": 0,
        "document_visuals": 0,
        "quiz_questions": 0,
        "documents": 0,
    }

    # 1. Sweep PrepContentCache
    for cache_obj in PrepContentCache.objects.all().iterator(chunk_size=50):
        if not isinstance(cache_obj.payload, dict):
            continue
        cleaned_payload = sanitize_notes_payload(cache_obj.payload)
        if cleaned_payload != cache_obj.payload:
            cache_obj.payload = cleaned_payload
            cache_obj.save(update_fields=["payload"])
            stats["content_cache"] += 1

    # 2. Sweep PrepQuestion
    for q in PrepQuestion.objects.all().iterator(chunk_size=100):
        changed = False
        update_fields = []
        if q.question_latex:
            cleaned_q = purge_institutional_metadata(q.question_latex)
            if cleaned_q != q.question_latex:
                q.question_latex = cleaned_q
                update_fields.append("question_latex")
                changed = True
        if q.solution_latex:
            cleaned_s = purge_institutional_metadata(q.solution_latex)
            if cleaned_s != q.solution_latex:
                q.solution_latex = cleaned_s
                update_fields.append("solution_latex")
                changed = True
        if q.topic_label:
            cleaned_tl = purge_institutional_metadata(q.topic_label)
            if cleaned_tl != q.topic_label:
                q.topic_label = cleaned_tl
                update_fields.append("topic_label")
                changed = True
        if isinstance(q.reconstruction_metadata, dict):
            orig_meta = copy.deepcopy(q.reconstruction_metadata)
            cleaned_meta = {}
            for k, val in orig_meta.items():
                if isinstance(val, str):
                    cleaned_meta[k] = purge_institutional_metadata(val)
                else:
                    cleaned_meta[k] = val
            if cleaned_meta != orig_meta:
                q.reconstruction_metadata = cleaned_meta
                update_fields.append("reconstruction_metadata")
                changed = True
        if changed:
            q.save(update_fields=update_fields)
            stats["questions"] += 1

    # 3. Sweep PrepTopic
    for t in PrepTopic.objects.all().iterator(chunk_size=100):
        changed = False
        update_fields = []
        if t.title:
            cleaned_title = purge_institutional_metadata(t.title)
            if cleaned_title != t.title:
                t.title = cleaned_title
                update_fields.append("title")
                changed = True
        if t.summary:
            cleaned_summary = purge_institutional_metadata(t.summary)
            if cleaned_summary != t.summary:
                t.summary = cleaned_summary
                update_fields.append("summary")
                changed = True
        if isinstance(t.subtopics, list):
            cleaned_subtopics = [
                purge_institutional_metadata(st) if isinstance(st, str) else st
                for st in t.subtopics
            ]
            if cleaned_subtopics != t.subtopics:
                t.subtopics = cleaned_subtopics
                update_fields.append("subtopics")
                changed = True
        if changed:
            t.save(update_fields=update_fields)
            stats["topics"] += 1

    # 4. Sweep PrepCourse
    for c in PrepCourse.objects.all().iterator(chunk_size=100):
        changed = False
        update_fields = []
        if c.title:
            cleaned_ct = purge_institutional_metadata(c.title)
            if cleaned_ct != c.title:
                c.title = cleaned_ct
                update_fields.append("title")
                changed = True
        if c.description:
            cleaned_cd = purge_institutional_metadata(c.description)
            if cleaned_cd != c.description:
                c.description = cleaned_cd
                update_fields.append("description")
                changed = True
        if changed:
            c.save(update_fields=update_fields)
            stats["courses"] += 1

    # 5. Sweep PrepTopicChatMessage
    for msg in PrepTopicChatMessage.objects.all().iterator(chunk_size=100):
        if msg.content:
            cleaned_msg = purge_institutional_metadata(msg.content)
            if cleaned_msg != msg.content:
                msg.content = cleaned_msg
                msg.save(update_fields=["content"])
                stats["chat_messages"] += 1

    # 6. Sweep PrepContentUpdate
    for cu in PrepContentUpdate.objects.all().iterator(chunk_size=100):
        if isinstance(cu.proposed_data, dict):
            cleaned_pd = {}
            for k, v in cu.proposed_data.items():
                if isinstance(v, str):
                    cleaned_pd[k] = purge_institutional_metadata(v)
                elif isinstance(v, list):
                    cleaned_pd[k] = [
                        purge_institutional_metadata(item) if isinstance(item, str) else item
                        for item in v
                    ]
                else:
                    cleaned_pd[k] = v
            if cleaned_pd != cu.proposed_data:
                cu.proposed_data = cleaned_pd
                cu.save(update_fields=["proposed_data"])
                stats["content_updates"] += 1

    # 7. Sweep PrepDocumentVisual (targeted to rows with metadata cues)
    inst_cue = (
        Q(context_text__icontains="university")
        | Q(context_text__icontains="downloaded by")
        | Q(context_text__icontains="lomoar")
        | Q(context_text__icontains="studocu")
        | Q(context_text__icontains="lecturer")
        | Q(context_text__icontains="bachelor of")
        | Q(context_text__icontains="school of")
        | Q(context_text__icontains="department of")
        | Q(context_text__icontains="ku/acad")
    )
    for dv in PrepDocumentVisual.objects.filter(inst_cue).iterator(chunk_size=50):
        changed = False
        update_fields = []
        if dv.context_text:
            ct = purge_institutional_metadata(dv.context_text)
            if ct != dv.context_text:
                dv.context_text = ct
                update_fields.append("context_text")
                changed = True
        if isinstance(dv.extracted_content, dict):
            cleaned_ec = {}
            for k, v in dv.extracted_content.items():
                if isinstance(v, str):
                    cleaned_ec[k] = purge_institutional_metadata(v)
                else:
                    cleaned_ec[k] = v
            if cleaned_ec != dv.extracted_content:
                dv.extracted_content = cleaned_ec
                update_fields.append("extracted_content")
                changed = True
        if changed:
            dv.save(update_fields=update_fields)
            stats["document_visuals"] += 1

    # 8. Sweep PrepTopicQuizQuestion
    for qq in PrepTopicQuizQuestion.objects.all().iterator(chunk_size=100):
        changed = False
        update_fields = []
        if qq.question_text:
            c_qt = purge_institutional_metadata(qq.question_text)
            if c_qt != qq.question_text:
                qq.question_text = c_qt
                update_fields.append("question_text")
                changed = True
        if qq.explanation:
            c_exp = purge_institutional_metadata(qq.explanation)
            if c_exp != qq.explanation:
                qq.explanation = c_exp
                update_fields.append("explanation")
                changed = True
        if isinstance(qq.options, list):
            c_opt = [
                purge_institutional_metadata(opt) if isinstance(opt, str) else opt
                for opt in qq.options
            ]
            if c_opt != qq.options:
                qq.options = c_opt
                update_fields.append("options")
                changed = True
        if changed:
            qq.save(update_fields=update_fields)
            stats["quiz_questions"] += 1

    # 9. Sweep PrepDocument extracted_text
    doc_cue = (
        Q(extracted_text__icontains="university")
        | Q(extracted_text__icontains="downloaded by")
        | Q(extracted_text__icontains="lomoar")
        | Q(extracted_text__icontains="studocu")
        | Q(extracted_text__icontains="lecturer")
        | Q(extracted_text__icontains="bachelor of")
        | Q(extracted_text__icontains="school of")
        | Q(extracted_text__icontains="department of")
        | Q(extracted_text__icontains="ku/acad")
    )
    for doc in PrepDocument.objects.filter(doc_cue).iterator(chunk_size=50):
        if doc.extracted_text:
            c_dt = purge_institutional_metadata(doc.extracted_text)
            if c_dt != doc.extracted_text:
                doc.extracted_text = c_dt
                doc.save(update_fields=["extracted_text"])
                stats["documents"] += 1

    logger.info("Institutional metadata purge complete: %s", stats)
    return stats
