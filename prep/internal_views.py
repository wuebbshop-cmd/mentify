"""
prep/internal_views.py

Internal Webhook API for the Dedicated Background Worker Web Service (Option B).
Allows the main web app (App 1) to delegate heavy, CPU-intensive document ingestion
and OCR extraction to the worker web app (App 2) via secure, private HTTP requests.
"""
from __future__ import annotations

import hmac
import json
import logging
import uuid

from django.conf import settings
from django.db import connection
from django.http import HttpRequest, JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from prep.models import PrepDocument
from services.prep_ingestion import (
    _DOCUMENT_INGESTION_EXECUTOR,
    _run_queued_document_ingestion,
)

logger = logging.getLogger(__name__)


def _is_authorized_internal_request(request: HttpRequest) -> bool:
    """Verify that the caller possesses the shared INTERNAL_WORKER_SECRET."""
    expected_secret = getattr(settings, "INTERNAL_WORKER_SECRET", "").strip()
    if not expected_secret:
        logger.error("[Worker Auth] INTERNAL_WORKER_SECRET is not configured in settings.")
        return False

    provided = (
        request.headers.get("X-Internal-Worker-Secret", "")
        or request.META.get("HTTP_X_INTERNAL_WORKER_SECRET", "")
    ).strip()

    # If not in header, allow checking Authorization: Bearer <secret>
    if not provided:
        auth_header = (request.headers.get("Authorization", "") or request.META.get("HTTP_AUTHORIZATION", "")).strip()
        if auth_header.startswith("Bearer "):
            provided = auth_header[7:].strip()

    if not provided:
        return False

    return hmac.compare_digest(provided, expected_secret)


@csrf_exempt
@require_POST
def internal_ingest_document_api(request: HttpRequest) -> JsonResponse:
    """
    Receive a document ingestion task dispatched from the main web application.
    Enqueues the job into the worker process's ThreadPoolExecutor and immediately
    returns HTTP 200 OK (< 50ms) to prevent HTTP connection timeouts.
    """
    if not _is_authorized_internal_request(request):
        logger.warning("[Worker Ingest] Unauthorized internal worker call attempted from %s", request.META.get("REMOTE_ADDR"))
        return JsonResponse(
            {"success": False, "error": "Unauthorized internal worker call."},
            status=403,
        )

    # Parse document_id from JSON payload or form body
    document_id_raw = None
    if request.body:
        try:
            payload = json.loads(request.body.decode("utf-8"))
            if isinstance(payload, dict):
                document_id_raw = payload.get("document_id")
        except (json.JSONDecodeError, UnicodeDecodeError):
            pass

    if not document_id_raw:
        document_id_raw = request.POST.get("document_id")

    if not document_id_raw:
        return JsonResponse(
            {"success": False, "error": "Missing required field 'document_id'."},
            status=400,
        )

    # Validate UUID format
    try:
        doc_uuid = uuid.UUID(str(document_id_raw).strip())
    except (ValueError, TypeError):
        return JsonResponse(
            {"success": False, "error": f"Invalid document_id format '{document_id_raw}'."},
            status=400,
        )

    # Verify document exists in shared database
    doc_exists = PrepDocument.objects.filter(pk=doc_uuid).exists()
    if not doc_exists:
        logger.warning("[Worker Ingest] Document %s not found in shared database.", doc_uuid)
        return JsonResponse(
            {"success": False, "error": f"Document '{doc_uuid}' not found."},
            status=404,
        )

    # Submit to local thread pool for background extraction (PyMuPDF, OCR, GitHub sync)
    _DOCUMENT_INGESTION_EXECUTOR.submit(_run_queued_document_ingestion, str(doc_uuid))
    logger.info("[Worker Ingest] Document %s queued for background processing on worker instance.", doc_uuid)

    return JsonResponse(
        {
            "success": True,
            "status": "queued",
            "document_id": str(doc_uuid),
            "enqueued_at": timezone.now().isoformat(),
        },
        status=200,
    )


@require_GET
def internal_worker_health_api(request: HttpRequest) -> JsonResponse:
    """
    Health check endpoint for the dedicated worker service.
    Verifies database connectivity and returns current worker state.
    Ideal for external ping monitors (UptimeRobot) to keep the free container awake.
    """
    db_healthy = False
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            row = cursor.fetchone()
            db_healthy = bool(row and row[0] == 1)
    except Exception as exc:
        logger.exception("[Worker Health] DB check failed: %s", exc)

    status_code = 200 if db_healthy else 503
    return JsonResponse(
        {
            "status": "healthy" if db_healthy else "unhealthy",
            "service": "eduai-worker",
            "db_connected": db_healthy,
            "is_worker_instance": getattr(settings, "IS_WORKER_INSTANCE", False),
            "timestamp": timezone.now().isoformat(),
        },
        status=status_code,
    )
