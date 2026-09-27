"""
services/prep_ingestion.py

Mentify Prep Ingestion Pipeline & Storage Engine:
1. Local Digital Text PDF Extraction via `pdfplumber` ($0 LLM Token Cost).
2. Together.ai Vision OCR for Scanned / Handwritten CAT Examination Papers.
3. GitHub Permanent Storage Integration via GitHubService.
4. Stage 1 -> Stage 2 Tutor Review Gate automatic promotion and credit accounting.
"""
from __future__ import annotations

import base64
import hashlib
import io
import json
import logging
import os
import re
try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

try:
    import pdfplumber
except ImportError:
    pdfplumber = None
import requests
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

from services.github_service import GitHubService

logger = logging.getLogger(__name__)


def extract_text_docx(docx_source) -> tuple[str, bool, int]:
    """
    Extract structured text and tables from Word documents (.docx) at $0 cost.
    """
    try:
        import docx
        if isinstance(docx_source, bytes):
            stream = io.BytesIO(docx_source)
        elif hasattr(docx_source, "read"):
            try:
                docx_source.seek(0)
            except Exception:
                pass
            stream = io.BytesIO(docx_source.read())
        else:
            stream = docx_source

        doc = docx.Document(stream)
        paragraphs: list[str] = []
        for p in doc.paragraphs:
            text = p.text.strip()
            if text:
                paragraphs.append(text)

        # Extract tables if present
        for table in doc.tables:
            for row in table.rows:
                cells_text = [cell.text.strip() for cell in row.cells if cell.text.strip()]
                if cells_text:
                    paragraphs.append(" | ".join(cells_text))

        full_text = "\n\n".join(paragraphs).strip()
        page_est = max(1, len(doc.paragraphs) // 25)
        return full_text, True, page_est
    except Exception as e:
        logger.error(f"[DOCX Extraction] Error: {e}")
        return "", False, 0


def extract_text_markdown(md_source) -> tuple[str, bool, int]:
    """
    Extract text directly from Markdown (.md) or Text (.txt) files at $0 cost.
    """
    try:
        if isinstance(md_source, bytes):
            content = md_source.decode("utf-8", errors="replace")
        elif hasattr(md_source, "read"):
            try:
                md_source.seek(0)
            except Exception:
                pass
            raw = md_source.read()
            if isinstance(raw, bytes):
                content = raw.decode("utf-8", errors="replace")
            else:
                content = str(raw)
        else:
            with open(md_source, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()

        clean_text = content.strip()
        page_est = max(1, len(clean_text.splitlines()) // 40)
        return clean_text, True, page_est
    except Exception as e:
        logger.error(f"[Markdown Extraction] Error: {e}")
        return "", False, 0


def extract_text_pdfplumber(pdf_source) -> tuple[str, bool, int]:
    """
    Extract text from a digital PDF using local pdfplumber at zero API token cost.
    
    Args:
        pdf_source: file path (str), binary stream, or bytes.
        
    Returns:
        tuple (extracted_text: str, is_digital: bool, page_count: int)
    """
    extracted_pages: list[str] = []
    total_words = 0

    try:
        # Handle bytes vs file-like vs path
        if isinstance(pdf_source, bytes):
            pdf_file = io.BytesIO(pdf_source)
        elif hasattr(pdf_source, "read"):
            try:
                pdf_source.seek(0)
            except Exception:
                pass
            content = pdf_source.read()
            pdf_file = io.BytesIO(content)
        else:
            pdf_file = pdf_source

        with pdfplumber.open(pdf_file) as pdf:
            page_count = len(pdf.pages)
            for idx, page in enumerate(pdf.pages, start=1):
                page_text = page.extract_text(layout=True) or ""
                words = len(page_text.split())
                total_words += words

                # Also try to extract simple tables if text is sparse
                if words < 15:
                    tables = page.extract_tables()
                    for table in tables:
                        table_str = "\n".join([" | ".join([cell or "" for cell in row]) for row in table])
                        page_text += f"\n{table_str}\n"

                extracted_pages.append(f"--- Page {idx} ---\n{page_text.strip()}")

        full_text = "\n\n".join(extracted_pages).strip()
        avg_words_per_page = total_words / max(page_count, 1)

        # A digital PDF typically has more than 20-30 words per page
        is_digital = avg_words_per_page >= 25 and len(full_text) > 100

        return full_text, is_digital, page_count

    except Exception as e:
        logger.error(f"[pdfplumber] Extraction failed: {e}")
        return "", False, 0


def render_pdf_pages_to_images(pdf_source, max_pages: int = 15, dpi: int = 150) -> list[bytes]:
    """
    Render PDF pages to high-resolution JPEG images using PyMuPDF (fitz).
    Enforces maximum page cap to safeguard against excessive OCR token usage.
    """
    images_bytes: list[bytes] = []

    try:
        if isinstance(pdf_source, bytes):
            doc = fitz.open(stream=pdf_source, filetype="pdf")
        elif hasattr(pdf_source, "read"):
            try:
                pdf_source.seek(0)
            except Exception:
                pass
            doc = fitz.open(stream=pdf_source.read(), filetype="pdf")
        else:
            doc = fitz.open(pdf_source)

        num_pages = min(len(doc), max_pages)
        for i in range(num_pages):
            page = doc[i]
            pix = page.get_pixmap(dpi=dpi)
            img_data = pix.tobytes("jpeg")
            images_bytes.append(img_data)
        doc.close()

    except Exception as e:
        logger.error(f"[PyMuPDF] Failed to render PDF pages: {e}")

    return images_bytes


def extract_scanned_ocr_together(pdf_source, max_pages: int = 15) -> str:
    """
    Extract LaTeX/markdown from scanned handwritten or printed CAT papers using Together.ai Vision.
    Strictly bounded by max_pages to prevent runaway token bills.
    """
    api_key = getattr(settings, "TOGETHERAI_API", "") or os.environ.get("TOGETHERAI_API", "")
    vision_model = getattr(settings, "TOGETHER_VISION_MODEL", "deepseek-ai/DeepSeek-V4.1-Flash")

    if not api_key:
        logger.warning("[Together OCR] TOGETHERAI_API not configured in settings or .env")
        return ""

    # Render pages to JPEG bytes
    page_images = render_pdf_pages_to_images(pdf_source, max_pages=max_pages, dpi=150)
    if not page_images:
        logger.warning("[Together OCR] No pages rendered for OCR.")
        return ""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    url = "https://api.together.xyz/v1/chat/completions"
    page_transcriptions: list[str] = []

    system_instruction = (
        "You are an academic examination paper transcriber and OCR engine. "
        "Transcribe this exam or notes page precisely into clean LaTeX and markdown. "
        "Preserve question numbers (e.g. Q1(a)), allocated marks (e.g. [10 Marks]), "
        "and format all mathematical formulas in standard LaTeX ($...$ inline or $$...$$ display). "
        "Do not output conversational greetings, pleasantries, or apologies."
    )

    for idx, img_bytes in enumerate(page_images, start=1):
        try:
            b64_img = base64.b64encode(img_bytes).decode("utf-8")
            payload = {
                "model": vision_model,
                "messages": [
                    {
                        "role": "system",
                        "content": system_instruction,
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": f"Transcribe page {idx} of this examination / course document accurately into LaTeX:",
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{b64_img}"
                                },
                            },
                        ],
                    },
                ],
                "max_tokens": 1500,
                "temperature": 0.2,
            }

            resp = requests.post(url, headers=headers, json=payload, timeout=45)
            if resp.status_code == 200:
                result = resp.json()
                content = result["choices"][0]["message"]["content"].strip()
                page_transcriptions.append(f"--- Page {idx} (Vision OCR) ---\n{content}")
            else:
                logger.error(f"[Together OCR] Page {idx} failed with {resp.status_code}: {resp.text[:200]}")
                page_transcriptions.append(f"--- Page {idx} (OCR Error: HTTP {resp.status_code}) ---")

        except Exception as ex:
            logger.error(f"[Together OCR] Exception processing page {idx}: {ex}")
            page_transcriptions.append(f"--- Page {idx} (OCR Exception: {ex}) ---")

    return "\n\n".join(page_transcriptions).strip()


def upload_to_github_storage(file_obj, course_code: str) -> str:
    """
    Store uploaded document permanently in the configured GitHub repository.
    Returns the permanent raw reference or stored GitHub URL.
    """
    token = getattr(settings, "GITHUB_TOKEN", "") or os.environ.get("GITHUB_TOKEN", "")
    repo = getattr(settings, "GITHUB_REPO", "") or os.environ.get("GITHUB_REPO", "")
    branch = getattr(settings, "GITHUB_BRANCH", "main") or os.environ.get("GITHUB_BRANCH", "main")
    upload_dir = getattr(settings, "GITHUB_UPLOAD_DIR", "mentify-uploads")

    if not token or not repo:
        logger.warning("[GitHub Storage] GITHUB_TOKEN or GITHUB_REPO missing. Skipping GitHub upload.")
        return ""

    try:
        svc = GitHubService(token=token, repo_name=repo, branch=branch, upload_dir=upload_dir)
        clean_code = course_code.replace(" ", "_").upper()
        result = svc.upload_file(file_obj, subdir=f"prep-docs/{clean_code}")
        if result:
            # Build standard raw GitHub user content URL
            raw_url = f"https://raw.githubusercontent.com/{repo}/{branch}/{result.repo_path}"
            return raw_url
    except Exception as e:
        logger.error(f"[GitHub Storage] Upload failed: {e}")

    return ""


def extract_topic_candidates(text: str) -> list[dict]:
    """
    Extract candidate syllabus units/topics without changing the course graph.
    """
    if not text or len(text.strip()) < 50:
        return []

    topics = []

    # 1. First, check if text has Markdown table structure (e.g. Unit / Module tables)
    rows = text.splitlines()
    current_topic = None
    for line in rows:
        line = line.strip()
        if not line.startswith("|") or "---" in line or "Module / Main Unit" in line:
            continue
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) >= 2:
            unit_col = parts[0]
            topic_col = parts[1]
            desc_col = parts[2] if len(parts) >= 3 else ""

            # Match patterns like: **1. Matrices in R** or Unit 1: Matrices in R or 1. Matrices
            unit_match = re.search(r'(?:\*\*|#+)?(?:\bUnit\b|\bModule\b|\bChapter\b)?\s*(\d+)[\.:\)]\s*([^*#|]+)(?:\*\*)?', unit_col, re.IGNORECASE)
            if unit_match:
                num = int(unit_match.group(1))
                title = unit_match.group(2).strip()
                current_topic = {
                    "order": num,
                    "title": title,
                    "subtopics": [topic_col] if topic_col else [],
                    "summary": desc_col,
                }
                topics.append(current_topic)
            elif current_topic and topic_col:
                if topic_col not in current_topic["subtopics"]:
                    current_topic["subtopics"].append(topic_col)
                if desc_col:
                    current_topic["summary"] = (current_topic["summary"] + " " + desc_col).strip()

    # 2. Heading-based extraction (e.g. ### Module 1: ..., ## Unit 1: ..., # Chapter 1: ...)
    if len(topics) < 2:
        heading_pattern = re.compile(
            r'^(?:#{1,6}\s*(?:(?:\bUnit\b|\bModule\b|\bChapter\b|\bTopic\b)\s*)?|(?:\bUnit\b|\bModule\b|\bChapter\b|\bTopic\b)\s+)(\d+)[\.:\-\)]\s*([^\n\r]+)',
            re.MULTILINE | re.IGNORECASE
        )
        matches = list(heading_pattern.finditer(text))
        for i, m in enumerate(matches):
            num = int(m.group(1))
            title = m.group(2).strip().strip("#* ").strip()
            if len(title) > 2 and not any(t["order"] == num for t in topics):
                start_pos = m.end()
                end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(text)
                section_text = text[start_pos:end_pos]

                # Extract subtopics from bullet points like * **Subtopic**:
                subtopics = []
                sub_matches = re.findall(r'^\s*[\*\-]\s+\*\*([^*:]+)\*\*', section_text, re.MULTILINE)
                for sm in sub_matches:
                    clean_st = sm.strip()
                    if clean_st and clean_st not in subtopics:
                        subtopics.append(clean_st)

                # Extract summary from first meaningful paragraph
                para_match = re.search(r'^\s*([A-Za-z][^\n\r]+)', section_text, re.MULTILINE)
                summary = para_match.group(1).strip() if para_match else f"Syllabus coverage and foundational theorems for {title}."

                topics.append({
                    "order": num,
                    "title": title,
                    "subtopics": subtopics,
                    "summary": summary,
                })

    # 3. If still fewer than 2 topics and text is rich, call DeepSeek to extract structured syllabus topics
    if len(topics) < 2 and len(text) > 300:
        try:
            api_key = getattr(settings, "DEEPSEEK_API", "") or getattr(settings, "DEEPSEEK_API_KEY", "") or os.environ.get("DEEPSEEK_API", "") or os.environ.get("DEEPSEEK_API_KEY", "")
            base_url = (getattr(settings, "DEEPSEEK_BASE_URL", "https://api.deepseek.com") or "https://api.deepseek.com").rstrip("/")
            model_name = getattr(settings, "DEEPSEEK_CHAT_MODEL", "deepseek-chat") or "deepseek-chat"

            if api_key:
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                }
                sample_text = text[:4000]
                payload = {
                    "model": model_name,
                    "messages": [
                        {
                            "role": "system",
                            "content": (
                                "You are an academic course-content parser. Extract only distinct modules, units, "
                                "or topics explicitly evidenced in the provided university notes or assessment. "
                                "Do not infer unnamed topics or invent syllabus coverage. "
                                "Return ONLY a valid JSON list of objects with keys: "
                                "\"order\" (int), \"title\" (str), \"subtopics\" (list of str), \"summary\" (str). "
                                "Do not include markdown code fence formatting or explanations."
                            )
                        },
                        {
                            "role": "user",
                            "content": f"Extract explicitly evidenced course topics from this material:\n\n{sample_text}"
                        }
                    ],
                    "temperature": 0.1,
                    "max_tokens": 1500,
                }
                resp = requests.post(f"{base_url}/chat/completions", headers=headers, json=payload, timeout=25)
                if resp.status_code == 200:
                    raw_json = resp.json()["choices"][0]["message"]["content"].strip()
                    if raw_json.startswith("```"):
                        raw_json = re.sub(r"^```(?:json)?\s*", "", raw_json)
                        raw_json = re.sub(r"\s*```$", "", raw_json)
                    parsed = json.loads(raw_json)
                    if isinstance(parsed, list) and len(parsed) >= 2:
                        topics = parsed
        except Exception as ex:
            logger.warning(f"[Topic Extraction] LLM fallback exception: {ex}")

    return topics


def extract_and_index_topics(course, text: str, prep_doc=None) -> list:
    """Legacy explicit upsert helper retained for scripts and controlled admin use."""
    from prep.models import PrepTopic

    topics = extract_topic_candidates(text)
    created_topics = []
    for t in topics:
        order = t.get("order", 1)
        title = t.get("title", f"Unit {order}").strip()
        subtopics = t.get("subtopics", [])
        summary = t.get("summary", "")

        topic_slug = slugify(f"unit-{order}-{title[:30]}")
        topic_obj, created = PrepTopic.objects.get_or_create(
            course=course,
            order=order,
            defaults={
                "title": title,
                "slug": topic_slug,
                "subtopics": subtopics,
                "summary": summary,
            }
        )
        if not created:
            # Update subtopics or summary if new details found
            if subtopics and not topic_obj.subtopics:
                topic_obj.subtopics = subtopics
            if summary and not topic_obj.summary:
                topic_obj.summary = summary
            topic_obj.save()
        created_topics.append(topic_obj)

    return created_topics


def _normalise_for_comparison(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip()).casefold()


def _normalise_document_text(text: str) -> str:
    """Normalize only for duplicate detection; preserve original extracted text."""
    return _normalise_for_comparison(text)


_ASSESSMENT_QUESTION_START = re.compile(
    r"(?m)^\s*(?:question\s*)?(\d{1,2})\s*[\).:]\s+"
)
_ASSESSMENT_MARKS = re.compile(r"\(?\s*(\d{1,3})\s*(?:marks?|mks?)\s*\)?", re.IGNORECASE)
_TOPIC_STOP_WORDS = {
    "about", "after", "also", "answer", "assume", "below", "calculate", "course",
    "define", "find", "following", "from", "given", "have", "into", "marks", "paper",
    "prove", "question", "show", "that", "the", "then", "this", "using", "with", "write",
}


def extract_assessment_questions(text: str) -> list[dict]:
    """Split explicitly numbered assessment questions without inventing content."""
    if not text:
        return []

    cleaned = re.sub(r"(?m)^---\s*Page.*?---\s*$", "", text)
    matches = list(_ASSESSMENT_QUESTION_START.finditer(cleaned))
    questions = []
    for index, match in enumerate(matches):
        number = int(match.group(1))
        if number < 1 or number > 99:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(cleaned)
        prompt = cleaned[match.end():end].strip()
        prompt = re.sub(r"\\hfill", " ", prompt)
        prompt = re.sub(r"[ \t]+", " ", prompt)
        prompt = re.sub(r"\n{3,}", "\n\n", prompt).strip()
        if len(prompt) < 18:
            continue
        marks_match = _ASSESSMENT_MARKS.search(prompt)
        marks = int(marks_match.group(1)) if marks_match else 0
        if marks_match:
            prompt = (prompt[:marks_match.start()] + prompt[marks_match.end():]).strip()
        if len(prompt) < 12:
            continue
        questions.append({"number": number, "marks": marks, "question_latex": prompt})
    return questions


def _topic_match_for_question(course, question_text: str):
    """Map only evidence-backed keyword matches; leave uncertain questions unassigned."""
    question_words = {
        word.casefold()
        for word in re.findall(r"[A-Za-z]{3,}", question_text)
        if word.casefold() not in _TOPIC_STOP_WORDS
    }
    best_topic = None
    best_score = 0
    for topic in course.topics.all():
        labels = [topic.title] + list(topic.subtopics if isinstance(topic.subtopics, list) else [])
        topic_words = {
            word.casefold()
            for label in labels
            for word in re.findall(r"[A-Za-z]{3,}", str(label))
            if word.casefold() not in _TOPIC_STOP_WORDS
        }
        score = len(question_words & topic_words)
        if score > best_score:
            best_topic, best_score = topic, score
    return best_topic if best_score else None


def assessment_question_rendering_issues(question_text: str) -> list[str]:
    """Return deterministic extraction defects that must not reach learners.

    Private-use glyphs and replacement characters are evidence that PDF text
    extraction did not recover the mathematical notation. They are not valid
    question content and must be reviewed or re-OCRed before publication.
    """
    source = str(question_text or "")
    issues = []
    if re.search(r"[\ue000-\uf8ff]", source):
        issues.append("unreadable private-use glyphs from source extraction")
    if "\ufffd" in source:
        issues.append("unreadable replacement character from source extraction")
    return issues


def index_assessment_questions(prep_document, paper) -> int:
    """Create verified question-bank rows from an approved assessment exactly once."""
    from prep.models import PrepQuestion

    if PrepQuestion.objects.filter(paper=paper).exists() or not prep_document.extracted_text.strip():
        return 0

    parsed_questions = extract_assessment_questions(prep_document.extracted_text)
    if not parsed_questions:
        return 0

    created = 0
    for item in parsed_questions:
        topic = _topic_match_for_question(prep_document.course, item["question_latex"])
        issues = assessment_question_rendering_issues(item["question_latex"])
        PrepQuestion.objects.create(
            paper=paper,
            topic=topic,
            question_type="authentic",
            number=item["number"],
            marks=item["marks"],
            topic_label=topic.title if topic else "",
            question_latex=item["question_latex"],
            solution_latex="",
            verification_status=(
                "flagged" if issues else ("verified" if prep_document.stage == "stage_3" else "pending")
            ),
            verified_by=prep_document.reviewed_by if prep_document.stage == "stage_3" and not issues else None,
        )
        created += 1
    return created


def create_content_update_proposals(course, prep_document, candidates: list[dict]) -> list:
    """Create pending enrichment proposals without modifying approved topic data."""
    from prep.models import PrepContentUpdate, PrepTopic

    proposals = []
    for candidate in candidates:
        order = int(candidate.get("order") or 1)
        title = str(candidate.get("title") or f"Unit {order}").strip()
        if not title:
            continue
        candidate_subtopics = [
            str(item).strip()
            for item in candidate.get("subtopics", [])
            if str(item).strip()
        ]
        candidate_summary = str(candidate.get("summary") or "").strip()

        topic = PrepTopic.objects.filter(course=course, order=order).first()
        if not topic:
            topic = PrepTopic.objects.filter(course=course, title__iexact=title).first()

        if not topic:
            proposal = PrepContentUpdate.objects.create(
                document=prep_document,
                topic=None,
                update_type="new_topic",
                proposed_data={
                    "order": order,
                    "title": title,
                    "subtopics": candidate_subtopics,
                    "summary": candidate_summary,
                },
                rationale="The uploaded material contains a syllabus topic not present in the shared course graph.",
            )
            proposals.append(proposal)
            continue

        if _normalise_for_comparison(topic.title) != _normalise_for_comparison(title):
            proposal, created = PrepContentUpdate.objects.get_or_create(
                document=prep_document,
                topic=topic,
                update_type="topic_conflict",
                defaults={
                    "proposed_data": {"order": order, "title": title, "subtopics": candidate_subtopics, "summary": candidate_summary},
                    "rationale": "The uploaded material uses a different title for an existing unit number. No content was merged automatically.",
                },
            )
            if created:
                proposals.append(proposal)
            continue

        existing_subtopics = topic.subtopics if isinstance(topic.subtopics, list) else []
        existing_keys = {_normalise_for_comparison(item) for item in existing_subtopics}
        missing_subtopics = [
            item for item in candidate_subtopics
            if _normalise_for_comparison(item) not in existing_keys
        ]
        if missing_subtopics:
            proposal, created = PrepContentUpdate.objects.get_or_create(
                document=prep_document,
                topic=topic,
                update_type="add_subtopics",
                defaults={
                    "proposed_data": {"subtopics": missing_subtopics},
                    "rationale": "The uploaded material identifies subtopics absent from the current topic record.",
                },
            )
            if created:
                proposals.append(proposal)

        if candidate_summary and not topic.summary.strip():
            proposal, created = PrepContentUpdate.objects.get_or_create(
                document=prep_document,
                topic=topic,
                update_type="fill_summary",
                defaults={
                    "proposed_data": {"summary": candidate_summary},
                    "rationale": "The current topic has no summary and the uploaded material supplies one.",
                },
            )
            if created:
                proposals.append(proposal)
        elif candidate_summary and _normalise_for_comparison(candidate_summary) not in _normalise_for_comparison(topic.summary):
            proposal, created = PrepContentUpdate.objects.get_or_create(
                document=prep_document,
                topic=topic,
                update_type="summary_review",
                defaults={
                    "proposed_data": {"summary": candidate_summary},
                    "rationale": "Possible additional explanation found. It requires reviewer approval before changing the existing summary.",
                },
            )
            if created:
                proposals.append(proposal)

    return proposals


def process_prep_document(prep_document) -> dict:
    """
    Complete Step 3 Ingestion Pipeline:
    1. Reads PDF/Word/Markdown file from PrepDocument.
    2. Uploads to permanent GitHub storage.
    3. Executes local $0 text extraction (pdfplumber/docx/markdown).
    4. Falls back to Together.ai Vision OCR if text density is low or CAT paper is scanned.
    5. Deducts appropriate credit fee (2 for text, 5 for vision OCR).
    6. Automatically extracts syllabus topics and indexes them under the course.
    7. Creates live student notification.
    8. Promotes document to Stage 2: Tutor Review Gate.
    """
    from prep.models import PrepDocument, PrepWallet, PrepNotification
    from services.credit_service import (
        InsufficientCredits,
        PlanLimitExceeded,
        consume_credits,
        enforce_subscription_limit,
        get_available_credits,
    )

    if not prep_document.file:
        return {"success": False, "error": "No file attached to document."}

    file_content = prep_document.file.read()
    prep_document.file.seek(0)

    # Stop exact duplicates before storage, OCR, AI extraction, or credit use.
    prep_document.file_sha256 = hashlib.sha256(file_content).hexdigest()
    duplicate = (
        PrepDocument.objects.filter(
            course=prep_document.course,
            file_sha256=prep_document.file_sha256,
        )
        .exclude(pk=prep_document.pk)
        .order_by("created_at")
        .first()
    )
    if duplicate:
        prep_document.is_duplicate = True
        prep_document.duplicate_of = duplicate
        prep_document.stage = "stage_2"
        prep_document.save(update_fields=["file_sha256", "is_duplicate", "duplicate_of", "stage", "updated_at"])
        return {
            "success": True,
            "duplicate": True,
            "duplicate_of": str(duplicate.id),
            "stage": prep_document.stage,
            "credits_deducted": 0,
            "topics_indexed": 0,
            "updates_proposed": 0,
        }

    # 1. Format-Aware Extraction Engine ($0 LLM Token Cost for Digital)
    file_name = prep_document.file.name.lower() if prep_document.file.name else ""

    if file_name.endswith(".docx") or file_name.endswith(".doc"):
        text, is_digital, page_count = extract_text_docx(file_content)
        method_used = "digital_docx"
        credit_cost = 2
        action_type = "upload_text"
    elif file_name.endswith(".md") or file_name.endswith(".txt"):
        text, is_digital, page_count = extract_text_markdown(file_content)
        method_used = "digital_markdown"
        credit_cost = 2
        action_type = "upload_text"
    else:
        # Default PDF Handling: Local pdfplumber first ($0)
        text, is_digital, page_count = extract_text_pdfplumber(file_content)
        method_used = "digital_pdfplumber"
        credit_cost = 2
        action_type = "upload_text"

        requires_ocr = not is_digital or len(text.strip()) < 120 or "Scanned" in prep_document.doc_type
        if requires_ocr:
            method_used = "together_vision_ocr"
            credit_cost = 5
            action_type = "upload_ocr"

    # Enforce the plan allowance and available balance before any paid OCR or
    # downstream indexing work starts. Local text extraction above is free.
    wallet = PrepWallet.get_or_create_wallet(prep_document.user) if prep_document.user else None
    if wallet:
        quota_name = "scanned_uploads" if action_type == "upload_ocr" else "document_uploads"
        try:
            enforce_subscription_limit(wallet, quota_name)
        except PlanLimitExceeded as exc:
            return {"success": False, "error": str(exc), "credits_balance": get_available_credits(wallet)}
        if get_available_credits(wallet) < credit_cost:
            return {
                "success": False,
                "error": f"Insufficient credits. This upload requires {credit_cost} credits.",
                "credits_balance": wallet.credits_balance,
            }

    # 2. Permanent GitHub Storage only after the request is eligible to run.
    github_url = upload_to_github_storage(prep_document.file, prep_document.course.code)
    if github_url:
        prep_document.github_raw_url = github_url

    if action_type == "upload_ocr":
        logger.info(f"[Prep Ingestion] Low digital text detected for doc {prep_document.id}. Invoking Together Vision OCR...")
        max_pages = getattr(settings, "TOGETHER_MAX_PAGES_PER_RUN", 15)
        ocr_text = extract_scanned_ocr_together(file_content, max_pages=max_pages)
        if not ocr_text:
            return {
                "success": False,
                "error": "The scanned document could not be read. Please upload a clearer scan or a digital original.",
                "credits_balance": get_available_credits(wallet) if wallet else None,
            }
        text = ocr_text

    prep_document.extracted_text = text
    prep_document.text_sha256 = hashlib.sha256(_normalise_document_text(text).encode("utf-8")).hexdigest() if text.strip() else ""

    # Different files sometimes contain the same notes. Keep the source file for
    # review, but do not propose duplicate syllabus changes or charge a user for it.
    text_duplicate = None
    if prep_document.text_sha256:
        text_duplicate = (
            PrepDocument.objects.filter(
                course=prep_document.course,
                text_sha256=prep_document.text_sha256,
            )
            .exclude(pk=prep_document.pk)
            .order_by("created_at")
            .first()
        )
        if not text_duplicate:
            # Older documents predate text fingerprints. Compare their stored
            # extraction lazily so they are still protected without a bulk rewrite.
            for existing in (
                PrepDocument.objects.filter(course=prep_document.course)
                .exclude(pk=prep_document.pk)
                .exclude(extracted_text="")
                .only("id", "extracted_text")
                .iterator()
            ):
                existing_hash = hashlib.sha256(
                    _normalise_document_text(existing.extracted_text).encode("utf-8")
                ).hexdigest()
                if existing_hash == prep_document.text_sha256:
                    text_duplicate = existing
                    break
    if text_duplicate:
        prep_document.is_duplicate = True
        prep_document.duplicate_of = text_duplicate
        prep_document.stage = "stage_2"
        prep_document.save()
        return {
            "success": True,
            "duplicate": True,
            "duplicate_of": str(text_duplicate.id),
            "stage": prep_document.stage,
            "method_used": method_used,
            "credits_deducted": 0,
            "topics_indexed": 0,
            "updates_proposed": 0,
        }

    # 3. Reviewable course-content extraction. Notes and assessments can both
    # surface missing syllabus coverage, but nothing changes until tutor review.
    topic_candidates = []
    content_updates = []
    if prep_document.doc_type in [
        "Lecture Notes",
        "Revision Sheet",
        "Continuous Assessment Test (CAT)",
        "Final Examination Paper",
    ] or "outline" in file_name or "syllabus" in file_name:
        try:
            topic_candidates = extract_topic_candidates(text)
            content_updates = create_content_update_proposals(prep_document.course, prep_document, topic_candidates)
            logger.info(
                "[Prep Ingestion] Proposed %s content updates from %s topic candidates for %s",
                len(content_updates),
                len(topic_candidates),
                prep_document.course.code,
            )
        except Exception as e:
            logger.error(f"[Topic Extraction] Error extracting topics: {e}")

    # 4. Advance Pipeline to Stage 2: Tutor Review Gate
    prep_document.stage = "stage_2"
    prep_document.save()

    # 5. Atomic Credit Wallet Deduction
    if prep_document.user:
        try:
            consume_credits(
                wallet,
                credit_cost,
                action_type=action_type,
                description=f"Document Ingestion: {prep_document.course.code} ({method_used})",
                metadata={"method_used": method_used, "pages": page_count},
            )
        except InsufficientCredits:
            return {
                "success": False,
                "error": f"Insufficient credits. This upload requires {credit_cost} credits.",
                "credits_balance": get_available_credits(wallet),
            }

        # 6. Live Student Notification
        clean_filename = prep_document.file.name.split("/")[-1]
        topics_msg = f" Found {len(content_updates)} proposed course update(s) for review." if content_updates else ""
        course_slug = prep_document.course.slug or prep_document.course.code.replace(" ", "-")
        PrepNotification.objects.create(
            user=prep_document.user,
            title=f"Material Ingested: {clean_filename}",
            message=f"Document '{clean_filename}' successfully parsed via {method_used}.{topics_msg} Materials are now under Stage 2 Tutor Review.",
            category="review",
            url=reverse("prep:course_detail", kwargs={"course_code": course_slug}),
        )

    return {
        "success": True,
        "document_id": str(prep_document.id),
        "stage": prep_document.stage,
        "method_used": method_used,
        "credits_deducted": credit_cost,
        "pages": page_count,
        "extracted_length": len(text),
        "topics_indexed": len(topic_candidates),
        "updates_proposed": len(content_updates),
        "github_url": prep_document.github_raw_url,
    }
