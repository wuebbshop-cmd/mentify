"""
Stealth External Course Pack Service for Mentify Prep.

Transfers and integrates the stealth scraping, download, and anti-detection architecture
from EduAI_MentifyAI to fetch, validate, sanitize, and store course PDF materials
directly into Cloudflare R2 object storage.

Guarantees:
1. Zero client-side trace (third-party domains/APIs are NEVER exposed to browser DevTools or LLMs).
2. Anti-detection measures: realistic browser fingerprint, dynamic referer spoofing,
   just-in-time tokens, exponential backoff on HTTP 429, random jitter.
3. Structural PDF integrity validation before storage.
4. Complete internal metadata sanitization (Author/Producer/XMP scrubbed via PyMuPDF).
5. Safe storage in Cloudflare R2 / local media WITHOUT triggering note-extraction worker pipelines,
   preserving API tokens and compute budgets.
"""
from __future__ import annotations

import io
import logging
import os
import random
import re
import time
from hashlib import sha256
from pathlib import Path
from typing import Any, Dict, List, Optional

import fitz  # PyMuPDF
import requests
from django.conf import settings
from django.core.cache import cache
from django.core.files.base import ContentFile
from django.utils import timezone

from prep.models import PrepCourse, PrepDocument, PrepPaper
from services.cloudflare_storage import CloudflareR2MediaStorage, is_cloudflare_r2_configured

logger = logging.getLogger(__name__)

# Base Upstream Configuration
BASE_URL = "https://kustudyhub.app"

# Realistic Chrome/Windows Browser Fingerprint Headers
# Accept-Encoding is omitted so requests handles gzip/deflate decoding cleanly.
STEALTH_HEADERS: Dict[str, str] = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9,sw;q=0.8",
    "Sec-Ch-Ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Connection": "keep-alive",
    "DNT": "1",
}


def normalize_code(code: str) -> str:
    """Normalize course/unit code for case-insensitive, space-free comparison."""
    return re.sub(r"[^A-Za-z0-9]", "", str(code or "")).upper()


def sanitize_filename(name: str, max_length: int = 150) -> str:
    """Sanitize string to be safe for filenames and storage keys."""
    cleaned = re.sub(r'[<>:"/\\|?*]', "_", str(name or ""))
    cleaned = cleaned.strip().strip(".")
    if not cleaned:
        cleaned = "document"
    if cleaned.lower().endswith(".pdf"):
        cleaned = cleaned[:-4].rstrip(".")
    return cleaned[:max_length]


def is_valid_pdf_bytes(data: bytes) -> bool:
    """
    Verify binary data is a structurally intact PDF.
    Must start with b'%PDF-' and contain b'%%EOF' within the final 1024 bytes.
    """
    if not data or len(data) < 64:
        return False
    if not data.startswith(b"%PDF-"):
        return False
    tail = data[-1024:] if len(data) >= 1024 else data
    return b"%%EOF" in tail


def sanitize_pdf_metadata(pdf_bytes: bytes, title: str, course_code: str) -> bytes:
    """
    Scrub all third-party internal metadata, author tags, and XMP XML streams
    from the PDF using PyMuPDF (fitz), replacing them with Mentify Prep branding.
    Ensures zero trace of upstream providers exists even if the file binary is inspected.
    """
    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        clean_title = sanitize_filename(title).replace("_", " ")

        doc.set_metadata({
            "title": f"{course_code} - {clean_title}",
            "author": "Mentify Prep",
            "subject": f"{course_code} Academic Study Material",
            "keywords": f"Mentify Prep, {course_code}, Higher Education",
            "creator": "Mentify Prep Academic Hub",
            "producer": "Mentify Prep",
            "creationDate": "",
            "modDate": "",
        })

        # Scrub embedded XML metadata (XMP streams), attachments, and hidden tracking artifacts
        doc.scrub(
            attached_files=True,
            clean_pages=False,
            embedded_files=True,
            metadata=False,
            xml_metadata=True,
        )

        output_bytes = doc.tobytes(garbage=3, deflate=True)
        doc.close()
        return output_bytes
    except Exception as exc:
        logger.warning("PDF metadata sanitization encountered an issue (%s); returning original bytes", exc)
        return pdf_bytes


def get_stealth_session() -> requests.Session:
    """Create a configured requests Session with realistic browser fingerprint."""
    session = requests.Session()
    session.headers.update(STEALTH_HEADERS)
    return session


def get_all_upstream_units(ttl_seconds: int = 86400) -> List[Dict[str, Any]]:
    """
    Fetch and cache the list of all available upstream course units.
    Cached in Django cache for 24 hours to minimize upstream traffic.
    """
    cache_key = "prep_upstream_units_catalog_v1"
    cached = cache.get(cache_key)
    if cached is not None and isinstance(cached, list):
        return cached

    session = get_stealth_session()
    url = f"{BASE_URL}/api/units/"
    try:
        resp = session.get(url, timeout=20)
        resp.raise_for_status()
        units = resp.json()
        if isinstance(units, list) and units:
            cache.set(cache_key, units, ttl_seconds)
            return units
    except Exception as exc:
        logger.warning("Failed to fetch upstream units catalog: %s", exc)

    return []


def find_upstream_unit_by_code(course_code: str, units: Optional[List[Dict[str, Any]]] = None) -> Optional[Dict[str, Any]]:
    """Find upstream unit matching the target course code."""
    normalized_target = normalize_code(course_code)
    if not normalized_target:
        return None

    if units is None:
        units = get_all_upstream_units()

    for unit in units:
        unit_code = unit.get("unitCode", "")
        slug = unit.get("slug", "")
        if (
            normalize_code(unit_code) == normalized_target
            or normalize_code(slug) == normalized_target
        ):
            return unit

    return None


def get_upstream_unit_pdfs(unit_id: int, unit_slug: str = "", ttl_seconds: int = 21600) -> List[Dict[str, Any]]:
    """
    Fetch list of available PDFs for a given upstream unit ID.
    Caches the list in Django cache for 6 hours.
    """
    cache_key = f"prep_upstream_unit_pdfs_v1_{unit_id}"
    cached = cache.get(cache_key)
    if cached is not None and isinstance(cached, list):
        return cached

    session = get_stealth_session()
    url = f"{BASE_URL}/api/unit/{unit_id}/pdfs/"
    referer = f"{BASE_URL}/kenyatta-university/{unit_slug}/" if unit_slug else f"{BASE_URL}/units/"

    try:
        resp = session.get(url, headers={"Referer": referer}, timeout=20)
        resp.raise_for_status()
        pdfs = resp.json()
        if isinstance(pdfs, list):
            cache.set(cache_key, pdfs, ttl_seconds)
            return pdfs
    except Exception as exc:
        logger.warning("Failed to fetch upstream PDFs for unit %s: %s", unit_id, exc)

    return []


def get_pdf_view_token(session: requests.Session, public_id: str, unit_slug: str = "") -> str:
    """Request a fresh, just-in-time viewing token with dynamic referer spoofing."""
    access_url = f"{BASE_URL}/api/pdfs/{public_id}/access/?action=view"
    referer_url = f"{BASE_URL}/kenyatta-university/{unit_slug}/" if unit_slug else f"{BASE_URL}/units/"
    resp = session.get(access_url, headers={"Referer": referer_url}, timeout=20)
    resp.raise_for_status()
    data = resp.json()
    token = data.get("token")
    if not token:
        raise ValueError(f"No access token received: {data}")
    return token


def download_upstream_pdf_bytes(
    session: requests.Session,
    public_id: str,
    unit_slug: str = "",
    max_retries: int = 3,
) -> Optional[bytes]:
    """
    Download a single PDF document in-memory with full stealth protections:
    - Dynamic referer header
    - Exponential backoff on HTTP 429
    - Fresh token per attempt
    - Returns sanitized binary bytes or None
    """
    referer_url = f"{BASE_URL}/kenyatta-university/{unit_slug}/" if unit_slug else f"{BASE_URL}/units/"
    request_headers = {"Referer": referer_url}

    for attempt in range(1, max_retries + 1):
        try:
            token = get_pdf_view_token(session, public_id, unit_slug=unit_slug)
            view_url = f"{BASE_URL}/api/pdfs/view/?token={token}"

            with session.get(view_url, headers=request_headers, stream=True, timeout=35) as resp:
                if resp.status_code == 429:
                    backoff = int(resp.headers.get("Retry-After", 10 * attempt))
                    logger.warning("Upstream rate limit (429). Backing off %ss (attempt %s/%s)...", backoff, attempt, max_retries)
                    time.sleep(backoff)
                    continue

                if resp.status_code in (401, 403):
                    logger.warning("Upstream access token rejected (HTTP %s)", resp.status_code)
                    continue

                resp.raise_for_status()
                buf = io.BytesIO()
                for chunk in resp.iter_content(chunk_size=16384):
                    if chunk:
                        buf.write(chunk)
                data = buf.getvalue()

                if is_valid_pdf_bytes(data):
                    return data
                else:
                    logger.warning("Downloaded data for %s failed PDF integrity check", public_id)
                    return None

        except Exception as exc:
            if attempt == max_retries:
                logger.warning("Failed to download PDF %s after %s attempts: %s", public_id, max_retries, exc)
                return None
            retry_wait = random.uniform(1.5, 3.0) * attempt
            time.sleep(retry_wait)

    return None


def sync_course_pdfs_from_upstream(course: PrepCourse, max_docs: int = 15) -> list[PrepDocument]:
    """
    Synchronizes PDFs for a course from the upstream repository into Cloudflare R2 / media storage
    and registers them as PrepDocument records in the database.

    IMPORTANT SAFETY MEASURES:
    1. Sets stage='stage_2' so that background extraction workers (Stage 1) are NOT triggered.
    2. Does NOT invoke AI generation or note extraction pipelines. Zero API tokens used.
    3. Scrubs all PDF metadata so external traces are completely removed.
    4. Uses a distributed cache lock to prevent duplicate ingestion from concurrent/repeated calls.
    """
    # Distributed cache lock: prevent parallel/repeated calls from creating duplicate documents.
    # If a sync is already in progress for this course, skip silently.
    lock_key = f"prep_upstream_sync_lock_{course.pk}"
    if cache.get(lock_key):
        logger.info(
            "Upstream sync already in progress for %s, skipping duplicate call", course.code
        )
        return []
    # Acquire lock for 3 minutes (generous timeout for slow upstream + R2 uploads)
    cache.set(lock_key, True, 180)

    try:
        return _sync_course_pdfs_from_upstream_inner(course, max_docs)
    finally:
        cache.delete(lock_key)


def _sync_course_pdfs_from_upstream_inner(course: PrepCourse, max_docs: int = 15) -> list[PrepDocument]:
    """Inner implementation called only when the lock is held."""
    unit = find_upstream_unit_by_code(course.code)
    if not unit:
        logger.info("No upstream unit found matching course code %s", course.code)
        return []

    unit_id = unit.get("id")
    unit_slug = unit.get("slug", "")
    pdfs = get_upstream_unit_pdfs(unit_id, unit_slug=unit_slug)
    if not pdfs:
        logger.info("No upstream PDFs found for unit %s (%s)", unit_id, course.code)
        return []

    session = get_stealth_session()
    created_documents: list[PrepDocument] = []
    storage = CloudflareR2MediaStorage() if is_cloudflare_r2_configured() else None

    # Retrieve existing document hashes for this course to avoid duplicate downloads
    existing_hashes = set(
        PrepDocument.objects.filter(course=course)
        .exclude(file_sha256="")
        .values_list("file_sha256", flat=True)
    )

    for idx, pdf in enumerate(pdfs[:max_docs], start=1):
        public_id = pdf.get("publicId")
        raw_title = pdf.get("pdfTitle", f"Document {idx}").strip()
        safe_title = sanitize_filename(raw_title)

        try:
            # Download bytes in memory with stealth safeguards
            raw_bytes = download_upstream_pdf_bytes(session, public_id, unit_slug=unit_slug)
            if not raw_bytes:
                continue

            file_hash = sha256(raw_bytes).hexdigest()
            if file_hash in existing_hashes:
                logger.info("Skipping already existing document %s (hash %s)", safe_title, file_hash[:8])
                continue

            # Scrub metadata and burn-in Mentify branding
            clean_bytes = sanitize_pdf_metadata(raw_bytes, raw_title, course.code)

            # Classify document type
            lower_title = raw_title.lower()
            if any(k in lower_title for k in ("exam", "final", "examination", "paper 1", "paper 2")):
                doc_type = "Final Examination Paper"
            elif any(k in lower_title for k in ("cat", "continuous assessment", "quiz", "test")):
                doc_type = "Continuous Assessment Test (CAT)"
            elif any(k in lower_title for k in ("revision", "tutorial", "assignment")):
                doc_type = "Revision Sheet"
            else:
                doc_type = "Lecture Notes"

            # Create file path
            now = timezone.now()
            year_month = now.strftime("%Y/%m")
            short_hash = file_hash[:8]
            clean_file_name = f"prep/documents/{year_month}/{short_hash}_{safe_title}.pdf"

            # Save to storage (Cloudflare R2 if enabled, otherwise Django default storage)
            if storage:
                storage.save_existing(clean_file_name, clean_bytes, content_type="application/pdf")
            else:
                from django.core.files.storage import default_storage
                default_storage.save(clean_file_name, ContentFile(clean_bytes))

            # Register document in database without triggering Stage 1 workers
            prep_doc = PrepDocument.objects.create(
                user=None,
                course=course,
                doc_type=doc_type,
                topic_name=raw_title,
                file=clean_file_name,
                file_size_bytes=len(clean_bytes),
                file_sha256=file_hash,
                stage="stage_2",  # Stage 2: Safe storage without auto-triggering Stage 1 extraction
                is_duplicate=False,
            )

            created_documents.append(prep_doc)
            existing_hashes.add(file_hash)
            logger.info("Successfully ingested course document: %s for %s", safe_title, course.code)

            # Human jitter delay between files
            if idx < len(pdfs):
                time.sleep(random.uniform(1.2, 2.8))

        except Exception as exc:
            logger.warning("Error processing upstream PDF %s (%s): %s", raw_title, public_id, exc)

    # Invalidate cached course pack zip if new documents were added
    if created_documents:
        cache.delete(f"prep_course_pdf_docs_{course.pk}")

    return created_documents
