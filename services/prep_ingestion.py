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
from PIL import Image, ImageDraw
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

from services.github_service import GitHubService
from prep.visual_matching import map_pdf_topic_sections, score_topic_context

logger = logging.getLogger(__name__)
VISUAL_CROP_VERSION = "figure-sibling-label-ownership-v9"


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


_VISUAL_REFERENCE_RE = re.compile(
    r"(?i)\b(?:flow[\s-]*chart|figure|fig\.?|graph|plot|diagram|chart)\s*(?:\d+[a-z]?)?"
)
_VISUAL_INSPECTION_VERSION = "visual-candidates-v1"


def _pdf_page_document(pdf_source):
    if fitz is None:
        return None
    if isinstance(pdf_source, bytes):
        return fitz.open(stream=pdf_source, filetype="pdf")
    if hasattr(pdf_source, "read"):
        try:
            pdf_source.seek(0)
        except Exception:
            pass
        return fitz.open(stream=pdf_source.read(), filetype="pdf")
    return fitz.open(pdf_source)


def _union_pdf_rect(first, second):
    return fitz.Rect(
        min(first.x0, second.x0),
        min(first.y0, second.y0),
        max(first.x1, second.x1),
        max(first.y1, second.y1),
    )


def _visual_crop_rect(
    page,
    rect,
    reasons,
    *,
    existing_padding: float = 0,
    sibling_rects=(),
    excluded_labels=None,
):
    rect = fitz.Rect(rect)
    vector_crop = "vector_drawing_cluster" in reasons
    def remove_old_padding(box):
        box = fitz.Rect(box)
        if not existing_padding:
            return box
        return fitz.Rect(
            min(box.x1, box.x0 + existing_padding),
            min(box.y1, box.y0 + existing_padding),
            max(box.x0, box.x1 - existing_padding),
            max(box.y0, box.y1 - existing_padding),
        )

    region = remove_old_padding(rect)
    siblings = [remove_old_padding(box) for box in sibling_rects]
    crop_padding = 2 if vector_crop else 6
    crop_rect = fitz.Rect(
        max(page.rect.x0, region.x0 - crop_padding),
        max(page.rect.y0, region.y0 - crop_padding),
        min(page.rect.x1, region.x1 + crop_padding),
        min(page.rect.y1, region.y1 + crop_padding),
    )
    if not vector_crop:
        return crop_rect

    for sibling in siblings:
        vertical_overlap = min(region.y1, sibling.y1) - max(region.y0, sibling.y0)
        horizontal_overlap = min(region.x1, sibling.x1) - max(region.x0, sibling.x0)
        if vertical_overlap > 0 and sibling.x0 >= region.x1:
            crop_rect.x1 = min(crop_rect.x1, region.x1)
        elif vertical_overlap > 0 and sibling.x1 <= region.x0:
            crop_rect.x0 = max(crop_rect.x0, (sibling.x1 + region.x0) / 2)
        if horizontal_overlap > 0 and sibling.y0 >= region.y1:
            crop_rect.y1 = min(crop_rect.y1, (region.y1 + sibling.y0) / 2)
        elif horizontal_overlap > 0 and sibling.y1 <= region.y0:
            crop_rect.y0 = max(crop_rect.y0, (sibling.y1 + region.y0) / 2)

    label_halo = fitz.Rect(
        max(page.rect.x0, region.x0 - min(100, max(36, region.width * 0.42))),
        max(page.rect.y0, region.y0 - min(56, max(20, region.height * 0.20))),
        min(page.rect.x1, region.x1 + min(100, max(36, region.width * 0.42))),
        min(page.rect.y1, region.y1 + min(56, max(20, region.height * 0.20))),
    )
    text_lines = {}
    for word in page.get_text("words"):
        text_lines.setdefault((word[5], word[6]), []).append(word)
    for words in text_lines.values():
        line_text = " ".join(str(word[4]) for word in words).strip()
        if not line_text or len(line_text) > 36 or len(words) > 5:
            continue
        if line_text.isupper() and sum(char.isalpha() for char in line_text) >= 8:
            continue
        if re.search(r"[!?;:]", line_text) or ("." in line_text and "(" not in line_text):
            continue
        line_rect = fitz.Rect(words[0][:4])
        for word in words[1:]:
            line_rect |= fitz.Rect(word[:4])
        if "=" in line_text and not region.intersects(line_rect):
            continue
        line_center = fitz.Point((line_rect.x0 + line_rect.x1) / 2, (line_rect.y0 + line_rect.y1) / 2)
        if any(
            sibling.x0 >= region.x1
            and region.y0 <= line_center.y <= region.y1
            and region.x1 < line_center.x < sibling.x0
            for sibling in siblings
        ):
            if excluded_labels is not None:
                excluded_labels.append(line_rect)
            continue
        if any(
            sibling.x1 <= region.x0
            and region.y0 <= line_center.y <= region.y1
            and sibling.x1 < line_center.x < region.x0
            for sibling in siblings
        ):
            crop_rect |= line_rect
            continue
        own_distance = max(region.x0 - line_center.x, 0, line_center.x - region.x1) ** 2
        own_distance += max(region.y0 - line_center.y, 0, line_center.y - region.y1) ** 2
        sibling_distances = [
            max(sibling.x0 - line_center.x, 0, line_center.x - sibling.x1) ** 2
            + max(sibling.y0 - line_center.y, 0, line_center.y - sibling.y1) ** 2
            for sibling in siblings
        ]
        if sibling_distances and min(sibling_distances) < own_distance:
            if excluded_labels is not None:
                excluded_labels.append(line_rect)
            continue
        if label_halo.intersects(line_rect):
            crop_rect |= line_rect
    return fitz.Rect(
        max(page.rect.x0, crop_rect.x0 - 2),
        max(page.rect.y0, crop_rect.y0 - 2),
        min(page.rect.x1, crop_rect.x1 + 2),
        min(page.rect.y1, crop_rect.y1 + 2),
    )


def _mask_excluded_visual_labels(crop_bytes, crop_rect, excluded_labels):
    image = Image.open(io.BytesIO(crop_bytes)).convert("RGB")
    draw = ImageDraw.Draw(image)
    for label_rect in excluded_labels:
        overlap = fitz.Rect(label_rect) & crop_rect
        if overlap.width <= 0 or overlap.height <= 0:
            continue
        left = max(0, int((overlap.x0 - crop_rect.x0) * 2) - 1)
        top = max(0, int((overlap.y0 - crop_rect.y0) * 2) - 1)
        right = min(image.width, int((overlap.x1 - crop_rect.x0) * 2) + 1)
        bottom = min(image.height, int((overlap.y1 - crop_rect.y0) * 2) + 1)
        if left < right and top < bottom:
            draw.rectangle((left, top, right - 1, bottom - 1), fill="white")
    output = io.BytesIO()
    image.save(output, format="JPEG", quality=90)
    return output.getvalue()


def _rects_near(first, second, gap: float = 20) -> bool:
    return not (
        first.x1 + gap < second.x0
        or second.x1 + gap < first.x0
        or first.y1 + gap < second.y0
        or second.y1 + gap < first.y0
    )


def _cluster_visual_rects(rectangles, *, gap: float = 20):
    clusters = []
    for rectangle in rectangles:
        rect = fitz.Rect(rectangle)
        index = 0
        while index < len(clusters):
            if _rects_near(rect, clusters[index], gap):
                rect = _union_pdf_rect(rect, clusters.pop(index))
                index = 0
            else:
                index += 1
        clusters.append(rect)
    return clusters


def _page_context(text: str, limit: int = 1800) -> str:
    if not text:
        return ""
    snippets = []
    for match in list(_VISUAL_REFERENCE_RE.finditer(text))[:4]:
        start = max(0, match.start() - 280)
        end = min(len(text), match.end() + 520)
        snippets.append(text[start:end].strip())
    if not snippets:
        return re.sub(r"\s+", " ", text).strip()[:limit]
    return "\n...\n".join(dict.fromkeys(snippets))[:limit]


def _text_near_visual_region(page, rect, padding: float = 140) -> str:
    expanded = fitz.Rect(
        max(page.rect.x0, rect.x0 - padding),
        max(page.rect.y0, rect.y0 - padding),
        min(page.rect.x1, rect.x1 + padding),
        min(page.rect.y1, rect.y1 + padding),
    )
    nearby = [word for word in page.get_text("words") if fitz.Rect(word[:4]).intersects(expanded)]
    nearby.sort(key=lambda word: (round(word[1] / 6), word[0]))
    return " ".join(word[4] for word in nearby)


def _visual_neighbor_text(page, rect, padding: float = 140) -> tuple[str, str]:
    before = []
    after = []
    for word in page.get_text("words"):
        word_rect = fitz.Rect(word[:4])
        if word_rect.x0 > page.rect.width * 0.94 or word_rect.x1 < page.rect.width * 0.06:
            continue
        if word_rect.y1 <= rect.y0 and rect.y0 - word_rect.y1 <= padding:
            before.append(word)
        elif word_rect.y0 >= rect.y1 and word_rect.y0 - rect.y1 <= padding:
            after.append(word)
    before.sort(key=lambda word: (round(word[1] / 6), word[0]))
    after.sort(key=lambda word: (round(word[1] / 6), word[0]))
    return " ".join(word[4] for word in before), " ".join(word[4] for word in after)


def inspect_pdf_visual_candidates(pdf_source, *, max_candidates: int = 100) -> tuple[list[dict], list[dict]]:
    """Collect page metrics and crops for likely non-text PDF visuals locally."""
    if fitz is None:
        return [], []
    try:
        document = _pdf_page_document(pdf_source)
    except Exception as exc:
        logger.warning("[PDF Visuals] Could not open PDF for page inspection: %s", exc)
        return [], []
    if document is None:
        return [], []

    source_identity = hashlib.sha256(pdf_source).hexdigest() if isinstance(pdf_source, bytes) else ""
    page_evidence = []
    visual_candidates = []
    try:
        for page_index, page in enumerate(document, start=1):
            text = page.get_text("text") or ""
            references = [match.group(0) for match in _VISUAL_REFERENCE_RE.finditer(text)][:12]
            image_rectangles = []
            images = page.get_images(full=True)
            for image in images:
                for image_rect in page.get_image_rects(image[0]):
                    rect = fitz.Rect(image_rect)
                    coverage = rect.get_area() / max(page.rect.get_area(), 1)
                    if (
                        rect.y0 < page.rect.height * 0.9
                        and rect.width >= page.rect.width * 0.12
                        and rect.height >= page.rect.height * 0.05
                        and coverage >= 0.003
                    ):
                        image_rectangles.append(rect)

            drawing_rectangles = []
            drawings = page.get_drawings()
            for drawing in drawings:
                rect = fitz.Rect(drawing.get("rect", (0, 0, 0, 0)))
                if rect.width >= 3 or rect.height >= 3:
                    drawing_rectangles.append(rect)
            clusters = _cluster_visual_rects(drawing_rectangles)
            vector_candidates = [
                rect for rect in clusters
                if rect.width >= page.rect.width * 0.16
                and rect.height >= page.rect.height * 0.055
                and (bool(references) or rect.get_area() >= page.rect.get_area() * 0.012)
            ]

            regions = [(rect, ["embedded_image_region"]) for rect in image_rectangles]
            regions.extend((rect, ["vector_drawing_cluster"]) for rect in vector_candidates)
            merged_regions = []
            for rect, reasons in regions:
                for existing in merged_regions:
                    if _rects_near(rect, existing[0], gap=12):
                        existing[0] = _union_pdf_rect(rect, existing[0])
                        existing[1].extend(reason for reason in reasons if reason not in existing[1])
                        break
                else:
                    merged_regions.append([rect, list(reasons)])

            page_evidence.append({
                "page_number": page_index,
                "text_chars": len(text),
                "word_count": len(text.split()),
                "image_count": len(images),
                "drawing_count": len(drawings),
                "visual_references": references,
                "candidate_region_count": len(merged_regions),
            })

            for rect, reasons in merged_regions:
                if len(visual_candidates) >= max(0, max_candidates):
                    continue
                sibling_rects = [other[0] for other in merged_regions if other[0] is not rect]
                excluded_labels = []
                crop_rect = _visual_crop_rect(
                    page,
                    rect,
                    reasons,
                    sibling_rects=sibling_rects,
                    excluded_labels=excluded_labels,
                )
                if crop_rect.width < 20 or crop_rect.height < 20:
                    continue
                try:
                    pixmap = page.get_pixmap(
                        matrix=fitz.Matrix(2, 2),
                        clip=crop_rect,
                        alpha=False,
                    )
                    crop_bytes = pixmap.tobytes("jpeg")
                    if excluded_labels:
                        crop_bytes = _mask_excluded_visual_labels(crop_bytes, crop_rect, excluded_labels)
                except Exception as exc:
                    logger.warning("[PDF Visuals] Could not crop page %s: %s", page_index, exc)
                    continue

                box = [round(crop_rect.x0, 2), round(crop_rect.y0, 2), round(crop_rect.x1, 2), round(crop_rect.y1, 2)]
                key_input = (
                    f"{_VISUAL_INSPECTION_VERSION}|{source_identity}|{page_index}|{box}|"
                    f"{hashlib.sha256(crop_bytes).hexdigest()}"
                )
                region_context = _text_near_visual_region(page, crop_rect)
                context_before, context_after = _visual_neighbor_text(page, crop_rect)
                region_references = [
                    match.group(0) for match in _VISUAL_REFERENCE_RE.finditer(region_context)
                ]
                page_references = " ".join(region_references).lower()
                has_flowchart_ref = bool(re.search(r"\bflow[\s-]*chart\b", page_references))
                has_diagram_ref = has_flowchart_ref or bool(re.search(r"\bdiagram\b", page_references))
                has_graph_ref = bool(re.search(r"\b(?:graph|plot)\b", page_references)) or (
                    not has_flowchart_ref and bool(re.search(r"\bchart\b", page_references))
                )
                visual_type = (
                    "graph" if has_graph_ref and not has_diagram_ref
                    else "diagram" if has_diagram_ref and not has_graph_ref
                    else "unclassified"
                )
                visual_candidates.append({
                    "candidate_key": hashlib.sha256(key_input.encode("utf-8")).hexdigest(),
                    "page_number": page_index,
                    "bbox": box,
                    "candidate_reasons": reasons,
                    "context_text": _page_context(region_context or text),
                    "context_before": context_before,
                    "context_after": context_after,
                    "context_crop_bytes": page.get_pixmap(
                        matrix=fitz.Matrix(1.5, 1.5),
                        clip=fitz.Rect(
                            page.rect.x0,
                            max(page.rect.y0, crop_rect.y0 - 140),
                            page.rect.x1,
                            min(page.rect.y1, crop_rect.y1 + 140),
                        ),
                        alpha=False,
                    ).tobytes("jpeg"),
                    "visual_type": visual_type,
                    "crop_bytes": crop_bytes,
                })
    except Exception as exc:
        logger.warning("[PDF Visuals] Page inspection stopped: %s", exc)
    finally:
        document.close()
    return page_evidence, visual_candidates


def store_pdf_visual_candidates(prep_document, pdf_source, *, max_candidates: int = 100) -> int:
    """Persist page evidence and source crops without invoking vision services."""
    from django.core.files.base import ContentFile
    from prep.models import PrepDocumentVisual

    page_evidence, candidates = inspect_pdf_visual_candidates(
        pdf_source,
        max_candidates=max_candidates,
    )
    prep_document.page_evidence = page_evidence
    prep_document.save(update_fields=["page_evidence", "updated_at"])
    for candidate in candidates:
        visual, created = PrepDocumentVisual.objects.get_or_create(
            candidate_key=candidate["candidate_key"],
            defaults={
                "document": prep_document,
                "page_number": candidate["page_number"],
                "bbox": candidate["bbox"],
                "candidate_reasons": candidate["candidate_reasons"],
                "context_text": candidate["context_text"],
                "visual_type": candidate["visual_type"],
            },
        )
        if created:
            visual.crop.save(
                f"document-{prep_document.pk}-page-{candidate['page_number']}-{candidate['candidate_key'][:8]}.jpg",
                ContentFile(candidate["crop_bytes"]),
                save=True,
            )
        if candidate.get("context_crop_bytes") and not visual.context_crop:
            visual.context_crop.save(
                f"document-{prep_document.pk}-page-{candidate['page_number']}-{candidate['candidate_key'][:8]}-context.jpg",
                ContentFile(candidate["context_crop_bytes"]),
                save=True,
            )
        metadata = dict(visual.extracted_content) if isinstance(visual.extracted_content, dict) else {}
        metadata.update({
            "context_before": candidate.get("context_before", ""),
            "context_after": candidate.get("context_after", ""),
        })
        if metadata != (visual.extracted_content or {}):
            visual.extracted_content = metadata
            visual.save(update_fields=["extracted_content", "updated_at"])
    return len(candidates)


def assign_visuals_to_topics(prep_document, topics, *, allow_auto_approval: bool | None = None) -> dict[str, int]:
    """Assign source visuals only when page evidence clearly identifies a syllabus topic."""
    from prep.models import PrepDocumentVisual

    if allow_auto_approval is None:
        allow_auto_approval = prep_document.stage == "stage_3"

    text = str(prep_document.extracted_text or "")
    page_header = re.compile(r"(?m)^--- Page (\d+)(?:\s+\([^\n]*\))? ---\s*$")
    matches = list(page_header.finditer(text))
    page_texts = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_texts[int(match.group(1))] = text[match.end():end]
    section_topics, ambiguous_section_pages = map_pdf_topic_sections(text, topics)

    counts = {"approved": 0, "review": 0, "rejected": 0}
    candidates = PrepDocumentVisual.objects.filter(document=prep_document)
    for visual in candidates:
        if visual.status not in {"candidate", "approved", "needs_review", "rejected"}:
            continue
        if visual.reviewed_at and visual.status in {"approved", "rejected"}:
            continue
        metadata = dict(visual.extracted_content) if isinstance(visual.extracted_content, dict) else {}
        if visual.status != "candidate" and not metadata.get("auto_decision"):
            continue
        context = "\n".join((page_texts.get(visual.page_number, ""), visual.context_text or ""))
        topic, score, margin, evidence = score_topic_context(context, topics)
        section_topic = section_topics.get(visual.page_number)
        if visual.page_number in ambiguous_section_pages:
            topic, score, margin, evidence = None, 0, 0, []
            match_method = "ambiguous_pdf_topic_section_boundary"
        elif section_topic:
            context_topic, score, margin, evidence = score_topic_context(context, topics)
            topic = section_topic
            section_title = str(getattr(section_topic, "title", "")).casefold()
            context_title = str(getattr(context_topic, "title", "")).casefold() if context_topic else ""
            match_method = (
                "pdf_topic_section_and_context"
                if context_title == section_title and score >= 6 and margin >= 3 and len(evidence) >= 2
                else "pdf_topic_section_context_needs_review"
            )
        else:
            match_method = "page_context"
        metadata.update({
            "auto_topic": str(topic.get("title", "") if isinstance(topic, dict) else getattr(topic, "title", "")) if topic else "",
            "auto_topic_score": score,
            "auto_topic_margin": margin,
            "auto_match_terms": evidence,
            "auto_match_method": match_method,
        })
        confident = topic is not None and score >= 6 and margin >= 3 and len(evidence) >= 2
        if match_method == "pdf_topic_section_context_needs_review":
            visual.status = "needs_review"
            metadata["auto_decision"] = "needs_review_ambiguous_section_context"
            counts["review"] += 1
        elif confident and allow_auto_approval:
            visual.status = "approved"
            metadata["auto_decision"] = "approved_high_confidence"
            counts["approved"] += 1
        elif confident:
            visual.status = "needs_review"
            metadata["auto_decision"] = "suggested_high_confidence_pending_source_approval"
            counts["review"] += 1
        elif visual.page_number in ambiguous_section_pages:
            visual.status = "needs_review"
            metadata["auto_decision"] = "needs_review_ambiguous_section_boundary"
            counts["review"] += 1
        elif visual.page_number <= 1:
            visual.status = "rejected"
            metadata["auto_decision"] = "rejected_unmatched_cover_page"
            counts["rejected"] += 1
        else:
            visual.status = "needs_review"
            metadata["auto_decision"] = "needs_review_ambiguous_context"
            counts["review"] += 1
        visual.extracted_content = metadata
        visual.save(update_fields=["status", "extracted_content", "updated_at"])
    return counts


def _visual_source_conflicts(analysis: dict, source_context: str, visual_type: str) -> list[str]:
    """Find direct source contradictions that invalidate confidence-only acceptance."""
    conflicts = []
    source_text = str(source_context or "").upper()
    normalized_context = re.sub(r"\s+", "", source_text)
    source_identifiers = {
        re.sub(r"\s+", "", match.group(0))
        for match in re.finditer(r"(?<![A-Z0-9])[A-Z]{1,3}\s*\d+[A-Z]?(?![A-Z0-9])", source_text)
    }
    labels = analysis.get("visible_labels", [])
    for label in labels if isinstance(labels, list) else []:
        normalized_label = re.sub(r"\s+", "", label).upper() if isinstance(label, str) else ""
        if not re.fullmatch(r"[A-Z]{1,3}\d+[A-Z]?", normalized_label):
            continue
        if normalized_label in normalized_context:
            continue
        suffix = re.search(r"\d+[A-Z]?$", normalized_label)
        alternatives = sorted(
            identifier for identifier in source_identifiers
            if suffix and identifier.endswith(suffix.group(0))
        )
        if alternatives:
            conflicts.append(
                f"Model label {label!r} conflicts with source-page identifier(s): {', '.join(alternatives)}."
            )

    if visual_type == "graph":
        claims = " ".join(str(analysis.get(key) or "") for key in (
            "caption", "elements", "relationships", "qualitative_summary",
        )).lower()
        context = str(source_context or "").lower()
        if re.search(r"\bkink(?:ed)?\b", context) and not re.search(r"\bkink(?:ed)?\b", claims):
            conflicts.append("Source text explicitly describes a kinked graph, but the model did not report the kink.")
        source_explains_mr_discontinuity = (
            re.search(r"\b(?:mr|marginal revenue)\b", context)
            and re.search(r"\bdiscontinu\w*", context)
        )
        if source_explains_mr_discontinuity and not re.search(r"\bdiscontinu\w*", claims):
            conflicts.append("Source text explicitly describes discontinuous marginal revenue, but the model omitted it.")
    return conflicts


def inspect_visual_candidate_with_vision(visual_candidate) -> dict:
    """Inspect one stored crop with vision and persist structured, reviewable evidence."""
    api_key = getattr(settings, "TOGETHERAI_API", "") or os.environ.get("TOGETHERAI_API", "")
    if not api_key:
        return {"success": False, "error": "TOGETHERAI_API is not configured."}
    inspection_image = visual_candidate.context_crop or visual_candidate.crop
    if not inspection_image:
        return {"success": False, "error": "Visual candidate has no stored crop."}

    vision_model = getattr(settings, "TOGETHER_VISION_MODEL", "deepseek-ai/DeepSeek-V4.1-Flash")
    try:
        inspection_image.open("rb")
        image_bytes = inspection_image.read()
    except Exception as exc:
        visual_candidate.status = "error"
        visual_candidate.inspection_error = str(exc)[:2000]
        visual_candidate.save(update_fields=["status", "inspection_error", "updated_at"])
        return {"success": False, "error": visual_candidate.inspection_error}
    finally:
        try:
            inspection_image.close()
        except Exception:
            pass
    if not image_bytes:
        return {"success": False, "error": "Stored visual crop is empty."}

    prompt = (
        "Inspect this figure with its neighboring source-page text from a university course document. "
        "Use the surrounding text before and after the figure to determine which concept and note section it supports. "
        "Transcribe only visible evidence; use nearby text only to interpret labels, never to invent pixels or numeric values. "
        "Classify flowcharts as diagrams, not graphs. For a graph, copy numeric values only when visibly printed; "
        "otherwise describe supported qualitative relationships and leave data_points empty. "
        "Return JSON only with keys: visual_type (graph, diagram, table, illustration, unclassified), caption, "
        "visible_labels (array), axes (object with x_label, y_label, units), elements (array of visible elements), "
        "relationships (array), data_points (array of visibly printed numeric values only), "
        "qualitative_summary, uncertainties (array), confidence (number 0..1).\n\n"
        f"Text immediately before the figure:\n{(visual_candidate.extracted_content or {}).get('context_before', '')[:600]}\n\n"
        f"Text immediately after the figure:\n{(visual_candidate.extracted_content or {}).get('context_after', '')[:600]}\n\n"
        f"Additional page context:\n{visual_candidate.context_text[:1200]}"
    )
    payload = {
        "model": vision_model,
        "messages": [
            {"role": "system", "content": "Return one valid JSON object only. Do not infer exact data that is not visible."},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64.b64encode(image_bytes).decode('ascii')}"},
                    },
                ],
            },
        ],
        "temperature": 0,
        "max_tokens": 1200,
        "reasoning": {"enabled": False},
    }
    usage = {}
    try:
        response = requests.post(
            "https://api.together.xyz/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json=payload,
            timeout=60,
        )
        response.raise_for_status()
        body = response.json()
        usage = body.get("usage") if isinstance(body.get("usage"), dict) else {}
        choice = (body.get("choices") or [{}])[0]
        message = choice.get("message") if isinstance(choice.get("message"), dict) else {}
        raw_content = message.get("content")
        if not raw_content:
            finish_reason = str(choice.get("finish_reason") or "unknown")
            visual_candidate.status = "error"
            visual_candidate.vision_model = vision_model
            visual_candidate.vision_usage = usage
            visual_candidate.inspection_error = (
                f"Vision response contained no final content (finish_reason={finish_reason})."
            )
            visual_candidate.save(update_fields=[
                "status", "vision_model", "vision_usage", "inspection_error", "updated_at",
            ])
            return {"success": False, "error": visual_candidate.inspection_error, "usage": usage}

        raw = str(raw_content).strip()
        raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw, flags=re.IGNORECASE)
        analysis = json.loads(raw)
        if not isinstance(analysis, dict):
            raise ValueError("vision response was not a JSON object")
        visual_type = str(analysis.get("visual_type") or "unclassified").lower()
        valid_types = {choice[0] for choice in visual_candidate.VISUAL_TYPES}
        if visual_type not in valid_types:
            raise ValueError(f"unsupported visual_type: {visual_type}")
        confidence = float(analysis.get("confidence", 0))
        if not 0 <= confidence <= 1:
            raise ValueError("confidence must be between 0 and 1")
        labels = analysis.get("visible_labels", [])
        if not isinstance(labels, list) or any(not isinstance(label, str) for label in labels):
            raise ValueError("visible_labels must be an array of strings")

        source_conflicts = _visual_source_conflicts(
            analysis,
            visual_candidate.context_text,
            visual_type,
        )
        if source_conflicts:
            analysis["source_conflicts"] = source_conflicts

        visual_candidate.visual_type = visual_type
        visual_candidate.labels = labels
        visual_candidate.extracted_content = analysis
        visual_candidate.confidence = confidence
        visual_candidate.status = (
            "needs_review"
            if source_conflicts or confidence < 0.8
            else "inspected"
        )
        visual_candidate.vision_model = vision_model
        visual_candidate.vision_usage = usage
        visual_candidate.inspection_error = ""
        visual_candidate.save(update_fields=[
            "visual_type", "labels", "extracted_content", "confidence", "status",
            "vision_model", "vision_usage", "inspection_error", "updated_at",
        ])
        return {
            "success": True,
            "visual_type": visual_type,
            "confidence": confidence,
            "status": visual_candidate.status,
            "source_conflicts": source_conflicts,
            "usage": usage,
        }
    except Exception as exc:
        visual_candidate.status = "error"
        visual_candidate.vision_model = vision_model
        visual_candidate.vision_usage = usage
        visual_candidate.inspection_error = str(exc)[:2000]
        visual_candidate.save(update_fields=[
            "status", "vision_model", "vision_usage", "inspection_error", "updated_at",
        ])
        return {"success": False, "error": visual_candidate.inspection_error, "usage": usage}


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
                "reasoning": {"enabled": False},
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


_PAGE_TEXT_HEADER_RE = re.compile(r"(?m)^--- Page (\d+)(?: \([^\n]*\))? ---\s*$")
_ASSESSMENT_PAGE_FOOTER_RE = re.compile(r"(?im)^[ \t]*Page\s+\d+\s+of\s+\d+[ \t]*$\r?\n?")
_ASSESSMENT_EXAM_FOOTER_RE = re.compile(
    r"(?im)^[ \t]*INVOLVEMENT IN ANY EXAMINATION IRREGULARITY "
    r"SHALL LEAD TO DISCONTINUATION[ \t]*$\r?\n?"
)
_ASSESSMENT_SCANNER_FOOTER_RE = re.compile(r"(?im)^[ \t]*Scanned with CamScanner[ \t]*$\r?\n?")
_ASSESSMENT_ADVERTISEMENT_RE = re.compile(r"(?im)^[ \t]*VISIT US FOR\s*:")
_ASSESSMENT_PAPER_HEADER_RE = re.compile(
    r"(?is)\\begin\{center\}\s*"
    r"\\textbf\{[^{}]*(?:UNIVERSITY|COLLEGE|INSTITUTE)[^{}]*\}"
    r"[\s\S]{0,600}?\\textbf\{EXAMINATION\b[\s\S]{0,600}?"
    r"\\end\{center\}\s*\\noindent\s*\\textbf\{INSTRUCTIONS:"
)


def _strip_assessment_document_footers(text: str) -> str:
    """Remove recurring scan/page footers from extracted question text."""
    cleaned = _ASSESSMENT_PAGE_FOOTER_RE.sub("", str(text or ""))
    cleaned = _ASSESSMENT_EXAM_FOOTER_RE.sub("", cleaned)
    cleaned = _ASSESSMENT_SCANNER_FOOTER_RE.sub("", cleaned)
    return re.sub(r"\n{3,}", "\n\n", cleaned).strip()


def _strip_safe_question_extraction_artifacts(text: str) -> str:
    """Remove only known extraction debris whose boundaries are unambiguous."""
    cleaned = re.sub(r"^\s*\}+", "", str(text or ""), count=1).lstrip()
    header = _ASSESSMENT_PAPER_HEADER_RE.search(cleaned)
    if header:
        cleaned = cleaned[:header.start()].rstrip()
    advertisement = _ASSESSMENT_ADVERTISEMENT_RE.search(cleaned)
    if advertisement and re.search(
        r"(?i)\b(?:key cutting|past papers|setbooks|binding|handouts)\b",
        cleaned[advertisement.end():],
    ):
        cleaned = cleaned[:advertisement.start()].rstrip()
    return cleaned


def _split_page_transcriptions(text: str) -> dict[int, str]:
    matches = list(_PAGE_TEXT_HEADER_RE.finditer(str(text or "")))
    if not matches:
        clean = str(text or "").strip()
        return {1: clean} if clean else {}
    pages = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.end():end].strip()
        if page_text.startswith("(OCR Error:") or page_text.startswith("(OCR Exception:"):
            page_text = ""
        pages[int(match.group(1))] = page_text
    return pages


def merge_local_and_ocr_pages(local_text: str, ocr_text: str, *, minimum_local_words: int = 25) -> str:
    """Use OCR only to supplement pages whose local PDF text is weak."""
    local_pages = _split_page_transcriptions(local_text)
    ocr_pages = _split_page_transcriptions(ocr_text)
    if not local_pages and not ocr_pages:
        return ""

    merged = []
    for page_number in sorted(set(local_pages) | set(ocr_pages)):
        local_page = local_pages.get(page_number, "").strip()
        ocr_page = ocr_pages.get(page_number, "").strip()
        local_is_weak = len(local_page.split()) < minimum_local_words
        if ocr_page and (not local_page or (local_is_weak and len(ocr_page.split()) > len(local_page.split()))):
            page_content = ocr_page
            source_label = "Vision OCR supplement"
        else:
            page_content = local_page
            source_label = "Local extraction"
        if page_content:
            merged.append(f"--- Page {page_number} ({source_label}) ---\n{page_content}")
    return "\n\n".join(merged)


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
    # Prefer explicit syllabus headings over cover-page table rows. Some PDFs
    # put course metadata in a table-shaped cover block that looks like units.
    if text:
        heading_pattern = re.compile(
            r'^(?:#{1,6}\s*(?:(?:\bUnit\b|\bModule\b|\bChapter\b|\bTopic\b)\s*)?|(?:\bUnit\b|\bModule\b|\bChapter\b|\bTopic\b)\s+)(\d+)[\.:\-\)]\s*([^\n\r]+)',
            re.MULTILINE | re.IGNORECASE
        )
        matches = list(heading_pattern.finditer(text))
        bare_topic_pattern = re.compile(r'^\s*(\d+)\:\s*([^\n\r]+)', re.MULTILINE)
        first_explicit_heading = min((match.start() for match in matches), default=len(text))
        matches += [
            match for match in bare_topic_pattern.finditer(text)
            if match.start() < first_explicit_heading
        ]
        matches.sort(key=lambda match: match.start())
        heading_topics = {}
        for i, m in enumerate(matches):
            num = int(m.group(1))
            title = m.group(2).strip().strip("#* ").strip()
            if len(title) > 2 and num not in heading_topics:
                start_pos = m.end()
                end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(text)
                section_text = text[start_pos:end_pos]

                # Extract subtopics from bullet points like * **Subtopic**:
                subtopics = []
                started_bullets = False
                for line in section_text.splitlines():
                    clean_line = line.strip()
                    bullet_match = re.match(
                        r'^(?:[\*\-•])\s+(?:\*\*)?([^*:\n]+?)(?:\*\*)?\s*$',
                        clean_line,
                    )
                    if bullet_match:
                        started_bullets = True
                        clean_st = bullet_match.group(1).strip()
                        if clean_st and clean_st not in subtopics:
                            subtopics.append(clean_st)
                    elif started_bullets and clean_line:
                        break

                # Extract summary from first meaningful paragraph
                summary = ""
                summary_source = section_text.split("•", 1)[0]
                for line in summary_source.splitlines():
                    clean_line = line.strip()
                    if (
                        len(clean_line) >= 20
                        and re.match(r"[A-Za-z]", clean_line)
                        and not re.match(r"(?i)(downloaded by|lomoar|scan to|studocu)", clean_line)
                    ):
                        summary = clean_line
                        break
                summary = summary or f"Syllabus coverage and foundational theorems for {title}."

                heading_topics[num] = {
                    "order": num,
                    "title": title,
                    "subtopics": subtopics,
                    "summary": summary,
                }
        if heading_topics:
            topics = [topic for topic in topics if topic["order"] not in heading_topics]
            topics.extend(heading_topics.values())
            topics.sort(key=lambda topic: topic["order"])

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


COURSE_STUDY_FAMILIES = {
    "mathematics": {
        "category": "Mathematics",
        "note_structure": [
            "Conceptual Overview",
            "Definitions and Notation",
            "Theorems and Core Results",
            "Worked Examples",
            "Revision Summary and Common Errors",
        ],
    },
    "statistics": {
        "category": "Statistics",
        "note_structure": [
            "Purpose and Statistical Context",
            "Definitions and Assumptions",
            "Methods and Interpretation",
            "Worked Applications",
            "Revision Summary and Common Errors",
        ],
    },
    "computing": {
        "category": "Computing",
        "note_structure": [
            "Concept and Use Case",
            "Data, Syntax, and Core Concepts",
            "Methods and Operations",
            "Worked Implementation from the Notes",
            "Testing, Interpretation, and Common Errors",
        ],
    },
    "engineering": {
        "category": "Engineering",
        "note_structure": [
            "Engineering Context and System",
            "Principles and Assumptions",
            "Methods and Design Decisions",
            "Worked Application from the Notes",
            "Safety, Limitations, and Revision Summary",
        ],
    },
    "chemistry": {
        "category": "Chemistry",
        "note_structure": [
            "Chemical Context and Key Concepts",
            "Species, Properties, and Principles",
            "Reactions and Mechanisms",
            "Worked Applications from the Notes",
            "Safety, Conditions, and Revision Summary",
        ],
    },
    "physics": {
        "category": "Physics",
        "note_structure": [
            "Physical Context and Models",
            "Principles and Assumptions",
            "Laws and Relationships",
            "Worked Applications from the Notes",
            "Units, Limitations, and Revision Summary",
        ],
    },
    "social_science": {
        "category": "Social Sciences",
        "note_structure": [
            "Core Concepts and Context",
            "Theories and Key Thinkers",
            "Social Processes and Evidence",
            "Applications and Case Studies",
            "Revision Summary and Critical Questions",
        ],
    },
    "humanities": {
        "category": "Humanities",
        "note_structure": [
            "Historical and Cultural Context",
            "Key Ideas, Texts, and Terms",
            "Interpretations and Evidence",
            "Examples and Critical Analysis",
            "Revision Summary and Questions",
        ],
    },
    "business_economics": {
        "category": "Business & Economics",
        "note_structure": [
            "Context and Key Concepts",
            "Principles and Frameworks",
            "Processes and Evidence",
            "Worked Applications from the Notes",
            "Limitations and Revision Summary",
        ],
    },
    "general_science": {
        "category": "General Sciences",
        "note_structure": [
            "Context and Core Concepts",
            "Terms and Principles",
            "Processes and Evidence",
            "Applications from the Notes",
            "Limitations and Revision Summary",
        ],
    },
}


def _source_capabilities(text: str) -> dict[str, bool]:
    """Detect notation and code actually present in source notes."""
    source = str(text or "")
    code = bool(
        re.search(r"(?is)```(?:r|python|sql|javascript|java|c\+\+|bash)\s*\n", source)
        or re.search(r"(?m)^\s*[A-Za-z_][\w.]*\s*(?:<-|:=)\s*\S+", source)
        or re.search(r"(?m)^\s*(?:def|class)\s+[A-Za-z_]\w*\s*\(", source)
    )
    math = bool(
        re.search(r"\$\$|\$[^$\n]+\$|\\(?:frac|int|sum|prod|lim|mathbb|begin\{)|\\\(|\\\[", source)
    )
    chemical_equations = bool(
        re.search(
            r"(?:\d*\s*[A-Z][a-z]?\d*\s*)+(?:->|→|⇌|⟶)\s*(?:\d*\s*[A-Z][a-z]?\d*\s*)+",
            source,
        )
    )
    return {"code": code, "math_notation": math, "chemical_equations": chemical_equations}


def extract_course_study_profile(course, notes_text: str, source_document=None) -> dict | None:
    """Ask the configured model to classify course notes using verbatim evidence.

    The returned profile is a proposal only. Subject family uses verbatim model
    evidence; notation and code capabilities are detected deterministically.
    """
    source = str(notes_text or "").strip()
    if len(source) < 120:
        return None
    api_key = getattr(settings, "DEEPSEEK_API", "") or os.environ.get("DEEPSEEK_API", "")
    if not api_key:
        return None

    allowed_families = ", ".join(COURSE_STUDY_FAMILIES)
    prompt = (
        "Classify the subject family of this university lecture-note/syllabus source. "
        "The uploaded notes are the source of truth; do not infer discipline from the course code. "
        "Choose one family from: " + allowed_families + ". Return JSON only with keys: "
        "subject_family, confidence (0..1), evidence_quotes (1-3 exact verbatim excerpts). "
        "Do not treat a subject name in a proposed topic as evidence if the notes do not discuss it.\n\n"
        f"Course label for reference only: {course.code} - {course.title}\n\n"
        "SOURCE NOTES:\n" + source[:12000]
    )
    try:
        response = requests.post(
            f"{getattr(settings, 'DEEPSEEK_BASE_URL', 'https://api.deepseek.com').rstrip('/')}/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": getattr(settings, "DEEPSEEK_CHAT_MODEL", "deepseek-chat"),
                "messages": [
                    {"role": "system", "content": "Return one valid JSON object only. Do not invent evidence."},
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0,
                "max_tokens": 900,
            },
            timeout=30,
        )
        response.raise_for_status()
        raw = str(response.json()["choices"][0]["message"]["content"]).strip()
        raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw, flags=re.IGNORECASE)
        result = json.loads(raw)
        family = str(result.get("subject_family") or "").strip().lower()
        confidence = float(result.get("confidence", 0))
        evidence = [str(item).strip() for item in result.get("evidence_quotes", []) if str(item).strip()]
        source_folded = source.casefold()
        if family not in COURSE_STUDY_FAMILIES or not 0 <= confidence <= 1 or not evidence:
            return None
        if any(quote.casefold() not in source_folded for quote in evidence):
            logger.warning("[Course Profile] Rejected ungrounded classifier evidence for %s", course.code)
            return None

        detected = _source_capabilities(source)
        # Capabilities are deterministic source facts; a classifier's false
        # negative must not suppress notation or code visibly present in notes.
        capabilities = detected
        profile_template = COURSE_STUDY_FAMILIES[family]
        return {
            "schema_version": 1,
            "subject_family": family,
            "category": profile_template["category"],
            "confidence": confidence,
            "evidence_quotes": evidence,
            "source_sha256": hashlib.sha256(source.encode("utf-8", errors="ignore")).hexdigest(),
            "capabilities": capabilities,
            "note_structure": profile_template["note_structure"],
            "source_document_id": str(getattr(source_document, "id", "")),
            "rules": {
                "authority": "uploaded lecture notes and syllabus only",
                "code": "may be generated only when source notes contain code evidence",
                "math_notation": "may be generated only when source notes contain notation evidence",
                "chemical_equations": "may be generated only when source notes contain reaction evidence",
            },
        }
    except Exception as exc:
        logger.warning("[Course Profile] Classification failed for %s: %s", course.code, exc)
        return None


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


_ASSESSMENT_QUESTION_NUMBER = r"(?:\d{1,2}|one|two|three|four|five|six|seven|eight|nine|ten)"
_ASSESSMENT_QUESTION_START = re.compile(
    r"(?im)^[ \t]*(?:(?:\\noindent\s*)|(?:\\(?:section\*?|subsection\*?|textbf|underline)\s*\{\s*)|(?:\*\*|__|#{1,6}\s*))*"
    r"(?:(?:question\s+|q\.?\s*)(?P<explicit_number>" + _ASSESSMENT_QUESTION_NUMBER + r")\b"
    r"(?!\s+and\s+any\s+other\b)|(?P<bare_number>\d{1,2})\s*[\).:]\s+)"
)
_ASSESSMENT_QUESTION_NUMBER_WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
}
_ASSESSMENT_MARKS = re.compile(r"\(?\s*(\d{1,3})\s*(?:marks?|mks?)\s*\)?", re.IGNORECASE)
_AUTO_RECONSTRUCTION_CONFIDENCE_THRESHOLD = 0.8
_TOPIC_STOP_WORDS = {
    "about", "after", "also", "answer", "assume", "below", "calculate", "course",
    "define", "find", "following", "from", "given", "have", "into", "marks", "paper",
    "prove", "question", "show", "that", "the", "then", "this", "using", "with", "write",
}


def extract_assessment_questions(text: str) -> list[dict]:
    """Split numbered questions while retaining their original source page."""
    if not text:
        return []

    page_headers = list(_PAGE_TEXT_HEADER_RE.finditer(text))
    matches = list(_ASSESSMENT_QUESTION_START.finditer(text))
    questions = []
    for index, match in enumerate(matches):
        raw_number = match.group("explicit_number") or match.group("bare_number")
        number = _ASSESSMENT_QUESTION_NUMBER_WORDS.get(raw_number.casefold())
        if number is None:
            number = int(raw_number)
        if number < 1 or number > 99:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        prompt = _strip_assessment_document_footers(
            _PAGE_TEXT_HEADER_RE.sub("", text[match.end():end])
        )
        prompt = re.sub(r"\\hfill", " ", prompt)
        prompt = re.sub(r"[ \t]+", " ", prompt)
        prompt = re.sub(r"\n{3,}", "\n\n", prompt).strip()
        marks_match = _ASSESSMENT_MARKS.search(prompt)
        marks = int(marks_match.group(1)) if marks_match else 0
        if marks_match:
            prompt = (prompt[:marks_match.start()] + prompt[marks_match.end():]).strip()
        source_page = next(
            (int(header.group(1)) for header in reversed(page_headers) if header.start() < match.start()),
            None,
        )
        questions.append({
            "number": number,
            "marks": marks,
            "question_latex": prompt,
            "source_page_number": source_page,
            "extraction_confidence": None,
        })
    return questions


def learner_visible_assessment_questions(question_records):
    """Return only published-status questions that pass current rendering checks."""
    from prep.models import PrepQuestion

    return [
        question
        for question in question_records
        if question.verification_status in PrepQuestion.LEARNER_VISIBLE_STATUSES
        and not assessment_question_rendering_issues(question.question_latex)
    ]


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
    from services.prep_ai_router import _display_math_issues, _latex_syntax_issues

    source = str(question_text or "")
    issues = []
    if re.match(r"^\s*\}+", source):
        issues.append("question text begins with stray closing LaTeX braces")
    if source.count("**") % 2:
        issues.append("question text contains an unmatched Markdown bold marker")
    if _ASSESSMENT_PAPER_HEADER_RE.search(source):
        issues.append("question text contains the next examination paper header")
    if re.search(r"[\ue000-\uf8ff]", source):
        issues.append("unreadable private-use glyphs from source extraction")
    if "\ufffd" in source:
        issues.append("unreadable replacement character from source extraction")
    if re.search(r"(?i)\(\s*(?:cid|glyph|char)\s*:\s*\d+\s*\)", source):
        issues.append("unreadable PDF character-map placeholder")
    if len(re.sub(r"\s+", " ", source).strip()) < 18:
        issues.append("question text is too short to be a complete assessment item")
    if re.search(r"(?<!\\)\[\s*\]", source):
        issues.append("question text contains an empty extraction placeholder")
    if re.search(r"\b[A-Za-z]\s*,\s*[A-Za-z]\s*,\s*[A-Za-z]\s*,\s*\.{4,}\s*[A-Za-z]\b", source):
        issues.append("question text contains a corrupted ellipsis or detached indices")
    if source.count("$$") % 2:
        issues.append("unclosed display-math delimiter")
    if source.count("\\(") != source.count("\\)"):
        issues.append("unclosed inline-math delimiter")
    if len(re.findall(r"\\begin\{([^{}]+)\}", source)) != len(re.findall(r"\\end\{([^{}]+)\}", source)):
        issues.append("unclosed LaTeX environment")
    if re.search(
        r"(?im)^\s*(?:\*\*|\\textbf\{\s*)?question\s+"
        r"(?:one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b",
        source,
    ):
        issues.append("question text contains a following question heading")
    if re.search(r"(?i)\bdownloaded\s+by\b", source):
        issues.append("question text contains document download metadata")
    if (
        _ASSESSMENT_PAGE_FOOTER_RE.search(source)
        or _ASSESSMENT_EXAM_FOOTER_RE.search(source)
        or _ASSESSMENT_SCANNER_FOOTER_RE.search(source)
    ):
        issues.append("question text contains document page or scan footer")
    if re.search(r"\\infty\s+S\b", source):
        issues.append("question text may have a corrupted infimum operator before S")
    if source.rstrip().endswith(("\\", "=", ":", "|")):
        issues.append("question text appears truncated")
    has_included_table_or_visual = (
        re.search(r"(?i)\\begin\{(?:table|tabular|figure)\}|\\includegraphics\b", source)
        or re.search(r"(?m)^\s*\|[^|\n]+\|", source)
    )
    if (
        re.search(r"(?i)\b(?:following|below)\s+(?:table|figure|diagram)\b", source)
        and not has_included_table_or_visual
    ):
        issues.append("question refers to a following table or visual that is missing")
    if _ASSESSMENT_ADVERTISEMENT_RE.search(source):
        issues.append("question text contains an advertisement footer")
    issues.extend(_display_math_issues(source))
    issues.extend(
        issue
        for issue in _latex_syntax_issues(source)
        if " is outside display math" not in issue
    )
    return issues


def index_assessment_questions(prep_document, paper, *, reconstruct_invalid: bool = True) -> int:
    """Index source questions and automatically reconstruct flagged rows safely."""
    from prep.models import PrepQuestion

    if not prep_document.extracted_text.strip():
        return 0

    parsed_questions = extract_assessment_questions(prep_document.extracted_text)
    if not parsed_questions:
        return 0

    occurrences_by_number = {}
    for item in parsed_questions:
        occurrences_by_number[item["number"]] = occurrences_by_number.get(item["number"], 0) + 1

    used_question_ids = set()
    created = 0
    for item in parsed_questions:
        topic = _topic_match_for_question(prep_document.course, item["question_latex"])
        issues = assessment_question_rendering_issues(item["question_latex"])
        status = "flagged" if issues else "auto_validated"
        candidates = list(PrepQuestion.objects.filter(
            paper=paper,
            question_type="authentic",
            number=item["number"],
        ).order_by("id"))
        normalized_text = _normalise_document_text(item["question_latex"])
        question = next(
            (
                candidate
                for candidate in candidates
                if candidate.pk not in used_question_ids
                and _normalise_document_text(candidate.question_latex) == normalized_text
            ),
            None,
        )
        if question is None and occurrences_by_number[item["number"]] == 1:
            manually_verified = next(
                (
                    candidate
                    for candidate in candidates
                    if candidate.pk not in used_question_ids
                    and candidate.verification_status == "verified"
                    and candidate.verified_by_id
                ),
                None,
            )
            if manually_verified and not assessment_question_rendering_issues(
                manually_verified.question_latex
            ):
                used_question_ids.add(manually_verified.pk)
                continue
        if question is None:
            question = next(
                (
                    candidate
                    for candidate in candidates
                    if candidate.pk not in used_question_ids
                    and candidate.source_document_id == prep_document.pk
                    and not (
                        candidate.verification_status == "verified"
                        and candidate.verified_by_id
                    )
                ),
                None,
            )
        if question is None and occurrences_by_number[item["number"]] == 1:
            question = next(
                (
                    candidate
                    for candidate in candidates
                    if candidate.pk not in used_question_ids
                    and candidate.source_document_id is None
                    and not (
                        candidate.verification_status == "verified"
                        and candidate.verified_by_id
                    )
                ),
                None,
            )
        if question is None:
            question = PrepQuestion(
                paper=paper,
                question_type="authentic",
                number=item["number"],
            )
            created += 1
        elif question.verification_status == "verified" and question.verified_by_id and not issues:
            status = "verified"
        elif question.verification_status == "flagged" and not issues:
            status = "flagged"
        question.topic = topic
        question.marks = item["marks"]
        question.topic_label = topic.title if topic else ""
        question.source_document = prep_document
        question.source_page_number = item.get("source_page_number")
        question.extraction_confidence = item.get("extraction_confidence")
        question.question_latex = item["question_latex"]
        question.verification_status = status
        if issues:
            prior_metadata = question.reconstruction_metadata if isinstance(question.reconstruction_metadata, dict) else {}
            question.reconstruction_metadata = {
                **prior_metadata,
                "review_status": "source_flagged",
                "reason": "Automatic source extraction failed deterministic integrity checks.",
                "source_document_id": str(prep_document.pk),
                "source_page_number": item.get("source_page_number"),
                "original_transcription": item["question_latex"],
                "original_extraction_issues": issues,
            }
        question.verified_by = (
            question.verified_by
            if status == "verified"
            else None
        )
        question.save()
        used_question_ids.add(question.pk)

        if not reconstruct_invalid or not issues or not topic:
            continue

        existing_adaptation = PrepQuestion.objects.filter(reconstructed_from=question).first()
        if existing_adaptation:
            continue

        try:
            from services.prep_ai_router import generate_adapted_past_question

            adapted_result = generate_adapted_past_question(question)
            if not adapted_result.get("success"):
                logger.warning(
                    "[Question Index] Automatic reconstruction failed for %s Q%s: %s",
                    prep_document.course.code,
                    question.number,
                    adapted_result.get("error", "unknown error"),
                )
                continue

            adapted_item = adapted_result["question"]
            adapted_issues = assessment_question_rendering_issues(adapted_item.get("question_latex", ""))
            metadata = adapted_result.get("reconstruction_metadata")
            metadata = dict(metadata) if isinstance(metadata, dict) else {}
            confidence = metadata.get("model_confidence")
            accepted = (
                not adapted_issues
                and isinstance(confidence, (int, float))
                and not isinstance(confidence, bool)
                and _AUTO_RECONSTRUCTION_CONFIDENCE_THRESHOLD <= confidence <= 1
            )
            metadata.update({
                "review_status": "auto_validated" if accepted else "pending",
                "auto_validation_threshold": _AUTO_RECONSTRUCTION_CONFIDENCE_THRESHOLD,
                "adapted_question_validation_issues": adapted_issues,
            })
            PrepQuestion.objects.create(
                paper=paper,
                topic=topic,
                source_document=prep_document,
                source_page_number=item.get("source_page_number"),
                extraction_confidence=item.get("extraction_confidence"),
                reconstructed_from=question,
                question_type="adapted",
                number=question.number,
                marks=int(adapted_item.get("marks") or question.marks),
                topic_label=f"Reconstructed from Question {question.number}",
                question_latex=adapted_item["question_latex"],
                solution_latex=adapted_item["solution_latex"],
                verification_status="reconstructed" if accepted else "pending",
                reconstruction_metadata=metadata,
            )
        except Exception:
            logger.exception(
                "[Question Index] Automatic reconstruction raised for %s Q%s",
                prep_document.course.code,
                question.number,
            )
    return created


def create_content_update_proposals(
    course,
    prep_document,
    candidates: list[dict],
    course_profile: dict | None = None,
) -> list:
    """Create pending enrichment proposals without modifying approved topic data."""
    from prep.models import PrepContentUpdate, PrepTopic

    proposals = []
    if course_profile and prep_document.doc_type in {"Lecture Notes", "Revision Sheet"}:
        course_profile = dict(course_profile)
        course_profile["covers_full_syllabus"] = (
            str(prep_document.topic_name or "").strip().casefold() == "full syllabus"
        )
        course_profile["topic_outline"] = [
            {
                "order": int(candidate.get("order") or 1),
                "title": str(candidate.get("title") or "").strip(),
                "subtopics": candidate.get("subtopics") if isinstance(candidate.get("subtopics"), list) else [],
                "summary": str(candidate.get("summary") or "").strip(),
            }
            for candidate in candidates
            if str(candidate.get("title") or "").strip()
        ]
        existing_profile = PrepContentUpdate.objects.filter(
            document=prep_document,
            update_type="course_profile",
        ).first()
        if not existing_profile and course_profile.get("source_sha256") != (
            (course.study_profile or {}).get("source_sha256") if isinstance(course.study_profile, dict) else None
        ):
            proposals.append(PrepContentUpdate.objects.create(
                document=prep_document,
                topic=None,
                update_type="course_profile",
                proposed_data=course_profile,
                rationale=(
                    f"AI classified the uploaded notes as {course_profile['subject_family']} "
                    f"(confidence {course_profile['confidence']:.2f}) using quoted source evidence. "
                    "Review before applying the subject profile to the shared course."
                ),
            ))

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
        PlanLimitExceeded,
        enforce_subscription_limit,
        get_available_credits,
    )

    if not prep_document.file:
        return {"success": False, "error": "No file attached to document."}

    with prep_document.file.open("rb") as uploaded_file:
        file_content = uploaded_file.read()

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
    is_pdf = file_name.endswith(".pdf")

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

    # Enforce plan quotas before any paid OCR or downstream indexing work.
    # Upload credits are shared course costs and are settled per catalog member.
    wallet = PrepWallet.get_or_create_wallet(prep_document.user) if prep_document.user else None
    uploader_upload_credits = 0
    if wallet:
        quota_name = "scanned_uploads" if action_type == "upload_ocr" else "document_uploads"
        try:
            enforce_subscription_limit(wallet, quota_name)
        except PlanLimitExceeded as exc:
            return {"success": False, "error": str(exc), "credits_balance": get_available_credits(wallet)}

    # 2. Permanent GitHub Storage only after the request is eligible to run.
    with prep_document.file.open("rb") as uploaded_file:
        github_url = upload_to_github_storage(uploaded_file, prep_document.course.code)
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
        text = merge_local_and_ocr_pages(text, ocr_text)

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

    visual_candidate_count = 0
    if is_pdf:
        visual_candidate_count = store_pdf_visual_candidates(prep_document, file_content)

    # 3. Only lecture notes/revision sheets define course identity and syllabus.
    # Assessment papers are question sources, never course-profile/topic sources.
    topic_candidates = []
    content_updates = []
    visual_topic_assignments = {"approved": 0, "review": 0, "rejected": 0}
    if prep_document.doc_type in {"Lecture Notes", "Revision Sheet"}:
        try:
            topic_candidates = extract_topic_candidates(text)
            if visual_candidate_count and topic_candidates:
                visual_topic_assignments = assign_visuals_to_topics(prep_document, topic_candidates)
            course_profile = extract_course_study_profile(
                prep_document.course,
                text,
                source_document=prep_document,
            )
            content_updates = create_content_update_proposals(
                prep_document.course,
                prep_document,
                topic_candidates,
                course_profile=course_profile,
            )
            logger.info(
                "[Prep Ingestion] Proposed %s content updates from %s topic candidates for %s",
                len(content_updates),
                len(topic_candidates),
                prep_document.course.code,
            )
        except Exception as e:
            logger.error(f"[Topic Extraction] Error extracting topics: {e}")

    from prep.document_validation import validate_prep_document

    prep_document.validation_report = validate_prep_document(prep_document, text)

    # 4. Advance Pipeline to Stage 2: Tutor Review Gate
    prep_document.stage = "stage_2"
    prep_document.save()

    # 5. Record and settle the shared course upload cost.
    if prep_document.user:
        from services.prep_course_billing import create_shared_course_cost, settle_course_cost_share

        shared_cost = create_shared_course_cost(
            course=prep_document.course,
            cost_type="upload",
            total_credits=credit_cost,
            source_key=f"upload:{prep_document.pk}",
            document=prep_document,
            usage={"total_tokens": 0, "upload_credits": credit_cost},
            model_name=method_used,
        )
        uploader_share = shared_cost.shares.filter(user=prep_document.user).first()
        uploader_paid_before = uploader_share.paid_credits if uploader_share else 0
        for share in shared_cost.shares.select_related("user", "cost").all():
            settle_course_cost_share(share)
        if uploader_share:
            uploader_share.refresh_from_db(fields=["paid_credits"])
            uploader_upload_credits = uploader_share.paid_credits - uploader_paid_before

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
        "credits_deducted": uploader_upload_credits,
        "shared_credits_created": credit_cost,
        "pages": page_count,
        "extracted_length": len(text),
        "visual_candidates": visual_candidate_count,
        "visual_topic_assignments": visual_topic_assignments,
        "validation_status": prep_document.validation_report.get("status"),
        "validation_issue_count": len(prep_document.validation_report.get("issues", [])),
        "topics_indexed": len(topic_candidates),
        "updates_proposed": len(content_updates),
        "github_url": prep_document.github_raw_url,
    }
