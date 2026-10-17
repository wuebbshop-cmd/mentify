"""
prep/tests/test_worker_delegation.py

Comprehensive test suite verifying the decoupled worker web service architecture (Option B):
1. Worker endpoint authorization with shared secret.
2. Rejection of unauthenticated or malformed requests.
3. Successful task queueing upon valid internal webhook.
4. Health check endpoint for UptimeRobot monitoring.
5. Remote dispatch helper behavior under success, timeout, and failure.
6. Seamless local fallback when remote worker is unreachable.
"""
from __future__ import annotations

import json
import uuid
from unittest.mock import MagicMock, patch

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from django.urls import reverse

from prep.models import PrepCourse, PrepDocument
from services.prep_ingestion import (
    dispatch_to_remote_worker,
    enqueue_prep_document_ingestion,
)

User = get_user_model()


class DedicatedWorkerServiceTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="worker_tester",
            email="worker_tester@example.com",
            password="testpass12345",
            role="learner",
        )
        self.course = PrepCourse.objects.create(
            code="PHY101",
            title="General Physics I",
            level="Standard",
            category="Other",
            is_active=True,
        )
        self.test_file = SimpleUploadedFile("physics_test.pdf", b"%PDF-1.4 test document content", content_type="application/pdf")
        self.doc = PrepDocument.objects.create(
            user=self.user,
            course=self.course,
            doc_type="past_paper",
            academic_year="2025/2026",
            file=self.test_file,
            file_size_bytes=len(b"%PDF-1.4 test document content"),
            file_sha256="testsha256hash12345",
            stage="stage_1",
        )
        self.secret = "test-internal-secret-token"
        self.worker_endpoint = reverse("internal_ingest_document")
        self.health_endpoint = reverse("internal_worker_health")

    def test_worker_health_endpoint_returns_ok(self):
        """UptimeRobot keep-alive endpoint must return 200 with healthy state."""
        response = self.client.get(self.health_endpoint)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "healthy")
        self.assertEqual(data["service"], "eduai-worker")
        self.assertTrue(data["db_connected"])

    @override_settings(INTERNAL_WORKER_SECRET="test-internal-secret-token")
    def test_ingest_endpoint_rejects_missing_secret(self):
        """Calls without X-Internal-Worker-Secret header must be rejected with 403 Forbidden."""
        response = self.client.post(
            self.worker_endpoint,
            data=json.dumps({"document_id": str(self.doc.pk)}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)
        self.assertFalse(response.json()["success"])
        self.assertIn("Unauthorized", response.json()["error"])

    @override_settings(INTERNAL_WORKER_SECRET="test-internal-secret-token")
    def test_ingest_endpoint_rejects_wrong_secret(self):
        """Calls with incorrect secret header must be rejected with 403 Forbidden."""
        response = self.client.post(
            self.worker_endpoint,
            data=json.dumps({"document_id": str(self.doc.pk)}),
            content_type="application/json",
            HTTP_X_INTERNAL_WORKER_SECRET="wrong-secret-token",
        )
        self.assertEqual(response.status_code, 403)
        self.assertFalse(response.json()["success"])

    @override_settings(INTERNAL_WORKER_SECRET="test-internal-secret-token")
    def test_ingest_endpoint_rejects_missing_document_id(self):
        """Valid secret with missing document_id must return 400 Bad Request."""
        response = self.client.post(
            self.worker_endpoint,
            data=json.dumps({}),
            content_type="application/json",
            HTTP_X_INTERNAL_WORKER_SECRET=self.secret,
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("Missing required field", response.json()["error"])

    @override_settings(INTERNAL_WORKER_SECRET="test-internal-secret-token")
    def test_ingest_endpoint_rejects_nonexistent_document(self):
        """Valid secret with non-existent UUID must return 404 Not Found."""
        random_uuid = str(uuid.uuid4())
        response = self.client.post(
            self.worker_endpoint,
            data=json.dumps({"document_id": random_uuid}),
            content_type="application/json",
            HTTP_X_INTERNAL_WORKER_SECRET=self.secret,
        )
        self.assertEqual(response.status_code, 404)
        self.assertIn("not found", response.json()["error"])

    @override_settings(INTERNAL_WORKER_SECRET="test-internal-secret-token")
    @patch("prep.internal_views._DOCUMENT_INGESTION_EXECUTOR.submit")
    def test_ingest_endpoint_accepts_valid_payload_and_queues(self, mock_submit):
        """Authorized call with valid document must submit to executor and return 200 immediately."""
        response = self.client.post(
            self.worker_endpoint,
            data=json.dumps({"document_id": str(self.doc.pk)}),
            content_type="application/json",
            HTTP_X_INTERNAL_WORKER_SECRET=self.secret,
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(data["status"], "queued")
        self.assertEqual(data["document_id"], str(self.doc.pk))
        mock_submit.assert_called_once()

    @override_settings(WORKER_SERVICE_URL="")
    def test_dispatch_skipped_when_no_worker_url(self):
        """When WORKER_SERVICE_URL is empty (local dev), dispatch_to_remote_worker returns False."""
        result = dispatch_to_remote_worker(str(self.doc.pk))
        self.assertFalse(result)

    @override_settings(
        WORKER_SERVICE_URL="https://eduai-worker.onrender.com",
        INTERNAL_WORKER_SECRET="test-internal-secret-token",
    )
    @patch("services.prep_ingestion.requests.post")
    def test_dispatch_success_to_remote_worker(self, mock_post):
        """When remote worker responds with 200 OK, dispatch_to_remote_worker returns True."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True, "status": "queued"}
        mock_post.return_value = mock_response

        result = dispatch_to_remote_worker(str(self.doc.pk))
        self.assertTrue(result)
        mock_post.assert_called_once_with(
            "https://eduai-worker.onrender.com/api/internal/ingest-document/",
            json={"document_id": str(self.doc.pk)},
            headers={
                "X-Internal-Worker-Secret": "test-internal-secret-token",
                "Content-Type": "application/json",
                "User-Agent": "Mentify-Main-App/1.0",
            },
            timeout=4.0,
        )

    @override_settings(
        WORKER_SERVICE_URL="https://eduai-worker.onrender.com",
        INTERNAL_WORKER_SECRET="test-internal-secret-token",
    )
    @patch("services.prep_ingestion.requests.post")
    def test_dispatch_fallback_when_remote_worker_times_out(self, mock_post):
        """When remote worker connection fails or times out, dispatch returns False cleanly."""
        import requests
        mock_post.side_effect = requests.exceptions.Timeout("Connection timed out")

        result = dispatch_to_remote_worker(str(self.doc.pk))
        self.assertFalse(result)

    @override_settings(WORKER_SERVICE_URL="")
    @patch("services.prep_ingestion._run_queued_document_ingestion")
    def test_enqueue_runs_locally_when_no_worker_configured(self, mock_run_local):
        """In local development (no worker URL), enqueue immediately runs the local ingestion runner."""
        future = enqueue_prep_document_ingestion(self.doc.pk)
        future.result(timeout=5)
        mock_run_local.assert_called_once_with(str(self.doc.pk))

    @override_settings(
        WORKER_SERVICE_URL="https://eduai-worker.onrender.com",
        INTERNAL_WORKER_SECRET="test-internal-secret-token",
    )
    @patch("services.prep_ingestion.dispatch_to_remote_worker", return_value=True)
    def test_enqueue_delegates_to_worker_when_configured(self, mock_dispatch):
        """When WORKER_SERVICE_URL is set, enqueue attempts remote dispatch asynchronously."""
        future = enqueue_prep_document_ingestion(self.doc.pk)
        result = future.result(timeout=5)
        self.assertTrue(result.get("success"))
        self.assertTrue(result.get("delegated"))
        mock_dispatch.assert_called_once_with(str(self.doc.pk))

    @override_settings(
        WORKER_SERVICE_URL="https://eduai-worker.onrender.com",
        INTERNAL_WORKER_SECRET="test-internal-secret-token",
    )
    @patch("services.prep_ingestion.dispatch_to_remote_worker", return_value=False)
    @patch("services.prep_ingestion._run_queued_document_ingestion")
    def test_enqueue_falls_back_to_local_when_worker_fails(self, mock_run_local, mock_dispatch):
        """When remote worker dispatch fails, execution automatically falls back to local runner."""
        mock_run_local.return_value = {"success": True, "local_fallback": True}
        future = enqueue_prep_document_ingestion(self.doc.pk)
        result = future.result(timeout=5)
        mock_dispatch.assert_called_once_with(str(self.doc.pk))
        mock_run_local.assert_called_once_with(str(self.doc.pk))
        self.assertTrue(result.get("local_fallback"))
