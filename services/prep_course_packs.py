"""
Course PDF Pack Service for Mentify Prep.

Handles:
- Aggregating all verified course lecture notes and past examination PDFs from Cloudflare R2.
- Generating structured, high-speed ZIP packages of course PDF materials.
- Edge caching compiled ZIP archives in Cloudflare R2 for instant zero-latency downloads.
- Seamless fallback to stealth upstream fetch when local documents are not yet present.
"""
from __future__ import annotations

import io
import logging
import os
import re
import time
import zipfile
from pathlib import Path
from typing import Any

from django.conf import settings
from django.urls import reverse
from django.utils import timezone

from prep.models import PrepCourse, PrepDocument, PrepPaper
from services.cloudflare_storage import CloudflareR2MediaStorage, is_cloudflare_r2_configured

logger = logging.getLogger(__name__)


def clean_pdf_display_name(doc: PrepDocument, paper: PrepPaper | None = None) -> str:
    """Generate a clean, student-friendly display title for a course PDF."""
    if paper and paper.title:
        year_suffix = f" ({paper.year})" if paper.year and str(paper.year) not in paper.title else ""
        return f"{paper.title}{year_suffix}".strip()

    if doc.topic_name and doc.topic_name.lower() not in ("full syllabus", "notes", "lecture notes"):
        return doc.topic_name.strip()

    raw_file = doc.file.name if doc.file else ""
    base_name = Path(raw_file).name
    # Strip random sha hash prefix e.g. "c7bf382a02e4f3ee-344bdca8_file"
    clean_base = re.sub(r"^[a-f0-9]{16}-", "", base_name)
    clean_base = clean_base.replace("_file", "").replace(".pdf", "").replace("_", " ").strip()

    if clean_base and len(clean_base) >= 3 and not re.match(r"^[a-f0-9]{8}$", clean_base):
        return clean_base

    year_str = f" ({doc.academic_year})" if doc.academic_year else ""
    return f"{doc.course.code} {doc.doc_type}{year_str}".strip()


def get_course_pdf_documents(course: PrepCourse) -> list[dict[str, Any]]:
    """
    Retrieve all available original PDF documents for a course.
    Returns a structured list with clean titles, categories, sizes, and stealth download URLs.
    If no documents exist in DB yet, checks upstream catalog so the download button is visible.
    """
    docs = list(
        PrepDocument.objects.filter(course=course)
        .exclude(file="")
        .defer("extracted_text", "page_evidence", "validation_report")
        .order_by("doc_type", "created_at")
    )

    # If documents exist in DB, build stealth response items
    if docs:
        papers = PrepPaper.objects.filter(course=course, source_document__isnull=False).select_related("source_document")
        papers_by_doc_id = {p.source_document_id: p for p in papers}
        storage = CloudflareR2MediaStorage() if is_cloudflare_r2_configured() else None

        results = []
        for d in docs:
            raw_name = d.file.name if d.file else ""
            if not raw_name:
                continue

            clean_key = storage._clean_key(raw_name) if storage else raw_name.replace("\\", "/").strip("/")
            cdn_url = storage.url(clean_key) if storage else f"{settings.MEDIA_URL}{clean_key}"

            paper = papers_by_doc_id.get(d.id)
            display_title = clean_pdf_display_name(d, paper)

            doc_type_lower = (d.doc_type or "").lower()
            is_note = "note" in doc_type_lower
            is_paper = any(w in doc_type_lower for w in ["exam", "paper", "cat", "quiz"])

            # Determine download filename
            safe_stem = re.sub(r'[\\/*?:"<>|]', "", display_title).strip().replace(" ", "_")
            download_filename = f"{safe_stem}.pdf" if not safe_stem.lower().endswith(".pdf") else safe_stem

            try:
                download_url = reverse("prep:download_document", kwargs={"doc_id": str(d.id)})
            except Exception:
                download_url = cdn_url

            results.append({
                "id": str(d.id),
                "title": display_title,
                "doc_type": d.doc_type,
                "academic_year": d.academic_year or (paper.year if paper else ""),
                "key": clean_key,
                "cdn_url": cdn_url,
                "download_url": download_url,
                "download_filename": download_filename,
                "file_size_bytes": d.file_size_bytes,
                "is_note": is_note,
                "is_paper": is_paper,
                "is_upstream": False,
            })

        return results

    # Fallback: check upstream catalog if no DB documents exist yet
    try:
        from services.prep_external_pack_service import find_upstream_unit_by_code, get_upstream_unit_pdfs
        unit = find_upstream_unit_by_code(course.code)
        if unit:
            upstream_pdfs = get_upstream_unit_pdfs(unit.get("id"), unit_slug=unit.get("slug", ""))
            if upstream_pdfs:
                pack_url = reverse("prep:download_course_pack", kwargs={"course_code": course.code})
                upstream_results = []
                for idx, pdf in enumerate(upstream_pdfs, start=1):
                    raw_title = pdf.get("pdfTitle", f"Document {idx}").strip()
                    lower_title = raw_title.lower()
                    is_paper = any(k in lower_title for k in ("exam", "final", "examination", "cat", "quiz", "test", "paper"))
                    is_note = not is_paper
                    doc_type = "Continuous Assessment Test (CAT)" if "cat" in lower_title else ("Final Examination Paper" if is_paper else "Lecture Notes")
                    safe_stem = re.sub(r'[\\/*?:"<>|]', "", raw_title).strip().replace(" ", "_")
                    upstream_results.append({
                        "id": f"upstream_{idx}",
                        "title": raw_title,
                        "doc_type": doc_type,
                        "academic_year": "",
                        "key": "",
                        "cdn_url": pack_url,
                        "download_url": pack_url,
                        "download_filename": f"{safe_stem}.pdf",
                        "file_size_bytes": 0,
                        "is_note": is_note,
                        "is_paper": is_paper,
                        "is_upstream": True,
                    })
                return upstream_results
    except Exception as exc:
        logger.warning("Could not query upstream catalog for %s: %s", course.code, exc)

    return []


def build_or_get_course_pdf_pack(course: PrepCourse) -> tuple[bytes, str]:
    """
    Produce a complete, categorized ZIP archive of all course PDFs.
    Uses Cloudflare R2 as both source and zero-cost edge cache.
    Automatically fetches upstream materials if none are present in DB yet.
    Returns (zip_bytes, zip_filename).
    """
    docs = list(
        PrepDocument.objects.filter(course=course)
        .exclude(file="")
        .defer("extracted_text", "page_evidence", "validation_report")
        .order_by("doc_type", "created_at")
    )

    # If no documents exist, attempt stealth on-demand fetch from upstream
    if not docs:
        try:
            from services.prep_external_pack_service import sync_course_pdfs_from_upstream
            logger.info("No documents in DB for %s; initiating on-demand stealth fetch...", course.code)
            created_docs = sync_course_pdfs_from_upstream(course)
            if created_docs:
                docs = list(
                    PrepDocument.objects.filter(course=course)
                    .exclude(file="")
                    .order_by("doc_type", "created_at")
                )
        except Exception as exc:
            logger.warning("Stealth upstream sync failed for %s: %s", course.code, exc)

    if not docs:
        raise ValueError(f"No PDF documents available for course {course.code}")

    storage = CloudflareR2MediaStorage() if is_cloudflare_r2_configured() else None

    safe_course_code = re.sub(r"[^a-zA-Z0-9_-]", "_", course.code.strip())
    zip_filename = f"{safe_course_code}_PDF_Pack.zip"

    # Signature for cache validation
    sig_raw = "".join(f"{d.id}:{d.updated_at.isoformat() if d.updated_at else ''}" for d in docs)
    from hashlib import sha256
    cache_sig = sha256(sig_raw.encode("utf-8")).hexdigest()[:12]
    cache_key = f"prep-packs/{safe_course_code}_PDF_Pack_{cache_sig}.zip"

    # 1. Check Cloudflare R2 cache first
    if storage:
        try:
            if storage.exists(cache_key):
                logger.info("Serving cached course PDF pack from Cloudflare R2: %s", cache_key)
                return storage.download_bytes(cache_key), zip_filename
        except Exception as exc:
            logger.warning("Could not check R2 cache for %s: %s", cache_key, exc)

    # 2. Build ZIP archive
    logger.info("Building new course PDF pack for %s (%s documents)...", course.code, len(docs))
    doc_metadata_list = get_course_pdf_documents(course)

    buf = io.BytesIO()
    seen_entries = set()
    added_count = 0

    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for item in doc_metadata_list:
            if item.get("is_upstream"):
                continue

            clean_key = item["key"]
            file_bytes = None

            # Fetch from Cloudflare R2
            if storage and clean_key:
                try:
                    file_bytes = storage.download_bytes(clean_key)
                except Exception as exc:
                    logger.warning("Failed to fetch %s from R2: %s", clean_key, exc)

            # Fallback to local MEDIA_ROOT if absent from R2
            if not file_bytes and clean_key:
                local_path = Path(settings.MEDIA_ROOT) / clean_key
                if local_path.is_file():
                    file_bytes = local_path.read_bytes()

            if not file_bytes:
                logger.error("Could not obtain file bytes for document key: %s", clean_key)
                continue

            # Determine folder inside zip
            if item["is_note"]:
                folder = "01_Lecture_Notes"
            elif item["is_paper"]:
                folder = "02_Past_Papers_and_CATs"
            else:
                folder = "03_Reference_Materials"

            filename = item["download_filename"]
            entry_path = f"{folder}/{filename}"
            idx = 1
            while entry_path in seen_entries:
                stem = filename[:-4] if filename.lower().endswith(".pdf") else filename
                entry_path = f"{folder}/{stem}_{idx}.pdf"
                idx += 1

            seen_entries.add(entry_path)
            zf.writestr(entry_path, file_bytes)
            added_count += 1

        # Add README
        now_str = timezone.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        notes_count = sum(1 for m in doc_metadata_list if m["is_note"])
        papers_count = sum(1 for m in doc_metadata_list if m["is_paper"])
        readme_text = (
            f"===========================================================\n"
            f"{course.code} — {course.title}\n"
            f"Official Course PDF Pack (Lecture Notes & Past Examination Papers)\n"
            f"Delivered via Mentify Prep Academic Engine\n"
            f"===========================================================\n\n"
            f"Course Code:      {course.code}\n"
            f"Course Title:     {course.title}\n"
            f"Generated At:     {now_str}\n"
            f"Total Documents:  {added_count}\n"
            f"  - Lecture Notes: {notes_count}\n"
            f"  - Past Papers & CATs: {papers_count}\n\n"
            f"Folders Included:\n"
            f"  /01_Lecture_Notes       Original course modules and lecture notes\n"
            f"  /02_Past_Papers_and_CATs Past university examination papers & CATs\n"
            f"  /03_Reference_Materials Additional course revision guides & syllabi\n\n"
            f"For interactive AI tutoring, step-by-step problem solutions, and\n"
            f"spaced repetition recall decks, visit Mentify Prep.\n"
            f"===========================================================\n"
        )
        zf.writestr("README.txt", readme_text)

    zip_bytes = buf.getvalue()

    # 3. Cache compiled ZIP in Cloudflare R2
    if storage and added_count > 0:
        try:
            storage.save_existing(cache_key, zip_bytes, content_type="application/zip")
            logger.info("Successfully cached course PDF pack in Cloudflare R2: %s", cache_key)
        except Exception as exc:
            logger.warning("Failed to store course pack cache in R2: %s", exc)

    return zip_bytes, zip_filename
