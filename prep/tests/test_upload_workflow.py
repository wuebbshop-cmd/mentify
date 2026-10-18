import tempfile
from unittest.mock import patch

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from accounts.models import User
from prep.models import (
    PrepCourse,
    PrepCourseEnrollment,
    PrepCreditGrant,
    PrepDocument,
    PrepNoteGenerationGuard,
    PrepTopic,
    PrepWallet,
)
from services.email_service import send_prep_note_generation_failure_email


class PrepUploadWorkflowTests(TestCase):
    def setUp(self):
        self.media_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.media_directory.cleanup)
        self.media_settings = override_settings(MEDIA_ROOT=self.media_directory.name)
        self.media_settings.enable()
        self.addCleanup(self.media_settings.disable)

        self.user = User.objects.create_user(
            username="upload_workflow_user",
            email="upload-workflow@example.test",
            password="Valid123",
        )
        self.client.force_login(self.user)
        self.course = PrepCourse.objects.create(
            code="SMA 101",
            title="Foundations of Analysis",
            slug="upload-sma-101",
        )

    @staticmethod
    def _pdf(name):
        return SimpleUploadedFile(name, b"%PDF-1.4 test upload", content_type="application/pdf")

    @patch("services.prep_ingestion.process_prep_document")
    def test_existing_course_accepts_a_group_of_documents_without_search(self, process_document):
        process_document.return_value = {
            "success": True,
            "method_used": "digital_pdfplumber",
            "updates_proposed": 0,
            "credits_deducted": 2,
        }

        response = self.client.post(
            reverse("prep:upload"),
            {
                "course_id": str(self.course.pk),
                "doc_type": "Final Examination Paper",
                "academic_year": "2025/2026",
                "topic_name": "",
                "files": [self._pdf("final-2024.pdf"), self._pdf("final-2025.pdf")],
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], f"{reverse('prep:upload')}?course_id={self.course.pk}")
        self.assertEqual(process_document.call_count, 2)
        self.assertEqual(
            PrepDocument.objects.filter(course=self.course, user=self.user).count(),
            2,
        )
        self.assertTrue(PrepCourseEnrollment.objects.filter(user=self.user, course=self.course).exists())

        page = self.client.get(reverse("prep:upload"), {"course_id": self.course.pk})
        self.assertEqual(page.status_code, 200)
        self.assertContains(page, f'<option value="{self.course.pk}" selected>', html=False)
        self.assertContains(page, 'name="files"', html=False)
        self.assertContains(page, "multiple", html=False)

    @patch("services.prep_ingestion.process_prep_document")
    def test_one_document_failure_does_not_stop_the_rest_of_the_group(self, process_document):
        process_document.side_effect = [
            {"success": True, "method_used": "digital_pdfplumber", "updates_proposed": 0},
            RuntimeError("OCR provider unavailable"),
        ]

        response = self.client.post(
            reverse("prep:upload"),
            {
                "course_id": str(self.course.pk),
                "doc_type": "Lecture Notes",
                "academic_year": "2025/2026",
                "topic_name": "",
                "files": [self._pdf("notes-a.pdf"), self._pdf("notes-b.pdf")],
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(process_document.call_count, 2)
        documents = {
            document.file.name.rsplit("/", 1)[-1]: document
            for document in PrepDocument.objects.filter(course=self.course, user=self.user)
        }
        self.assertEqual(set(documents), {"notes-a.pdf", "notes-b.pdf"})
        self.assertEqual(documents["notes-a.pdf"].tutor_review_notes, "")
        self.assertIn("OCR provider unavailable", documents["notes-b.pdf"].tutor_review_notes)

    @patch("services.prep_ingestion.process_prep_document")
    def test_new_course_upload_remains_supported(self, process_document):
        process_document.return_value = {
            "success": True,
            "method_used": "digital_pdfplumber",
            "updates_proposed": 0,
            "credits_deducted": 2,
        }

        response = self.client.post(
            reverse("prep:upload"),
            {
                "course_id": "",
                "course_name": "SST 210 - Introductory Statistics",
                "doc_type": "Lecture Notes",
                "academic_year": "2025/2026",
                "files": [self._pdf("statistics-notes.pdf")],
            },
        )

        self.assertEqual(response.status_code, 302)
        course = PrepCourse.objects.get(code="SST 210")
        self.assertTrue(PrepDocument.objects.filter(course=course, user=self.user).exists())

    @patch("services.prep_ingestion.enqueue_prep_document_ingestion")
    def test_async_xhr_upload_returns_202_immediately_and_polls_status(self, enqueue_ingestion):
        response = self.client.post(
            reverse("prep:upload"),
            {
                "course_id": str(self.course.pk),
                "doc_type": "Lecture Notes",
                "academic_year": "2025/2026",
                "topic_name": "Metric Spaces",
                "files": [
                    SimpleUploadedFile("lecture-1.pdf", b"%PDF-1.4 unique-a", content_type="application/pdf"),
                    SimpleUploadedFile("lecture-2.pdf", b"%PDF-1.4 unique-b", content_type="application/pdf"),
                ],
            },
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        self.assertEqual(response.status_code, 202)
        payload = response.json()
        self.assertTrue(payload["success"])
        self.assertEqual(payload["queued_count"], 2)
        self.assertEqual(payload["duplicate_count"], 0)
        self.assertEqual(len(payload["documents"]), 2)
        self.assertEqual(enqueue_ingestion.call_count, 2)

        doc_ids = [doc["id"] for doc in payload["documents"]]
        status_res = self.client.get(
            reverse("prep:api_document_upload_status"),
            {"ids": ",".join(doc_ids)},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(status_res.status_code, 200)
        status_payload = status_res.json()
        self.assertTrue(status_payload["has_processing"])
        self.assertEqual(len(status_payload["documents"]), 2)

        # Simulate background worker completing one document
        PrepDocument.objects.filter(pk=doc_ids[0]).update(stage="stage_2")
        PrepDocument.objects.filter(pk=doc_ids[1]).update(stage="stage_2")
        status_res_done = self.client.get(
            reverse("prep:api_document_upload_status"),
            {"ids": ",".join(doc_ids)},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertFalse(status_res_done.json()["has_processing"])

    @patch("services.prep_ingestion.enqueue_prep_document_ingestion")
    def test_async_xhr_upload_detects_exact_duplicate_instantly_without_queuing(self, enqueue_ingestion):
        first_res = self.client.post(
            reverse("prep:upload"),
            {
                "course_id": str(self.course.pk),
                "doc_type": "Lecture Notes",
                "academic_year": "2025/2026",
                "files": [SimpleUploadedFile("notes-v1.pdf", b"%PDF-1.4 identical-bytes", content_type="application/pdf")],
            },
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(first_res.status_code, 202)
        self.assertEqual(enqueue_ingestion.call_count, 1)

        dup_res = self.client.post(
            reverse("prep:upload"),
            {
                "course_id": str(self.course.pk),
                "doc_type": "Lecture Notes",
                "academic_year": "2025/2026",
                "files": [SimpleUploadedFile("notes-copy.pdf", b"%PDF-1.4 identical-bytes", content_type="application/pdf")],
            },
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(dup_res.status_code, 200)
        dup_payload = dup_res.json()
        self.assertTrue(dup_payload["success"])
        self.assertEqual(dup_payload["queued_count"], 0)
        self.assertEqual(dup_payload["duplicate_count"], 1)
        # Background worker must not be called again for an exact duplicate
        self.assertEqual(enqueue_ingestion.call_count, 1)

    @patch("services.prep_ingestion.enqueue_prep_document_ingestion")
    def test_freemium_user_with_credits_can_upload_and_credits_are_deducted(self, enqueue_ingestion):
        from services.credit_service import grant_purchased_topup
        wallet = PrepWallet.get_or_create_wallet(self.user)
        wallet.credit_grants.all().delete()
        wallet.credits_balance = 0
        wallet.current_plan = "freemium"
        wallet.save()

        grant_purchased_topup(wallet, 20, "TEST-TOPUP-20", "20 Credit Topup")
        wallet.refresh_from_db()

        response = self.client.post(
            reverse("prep:upload"),
            {
                "course_id": str(self.course.pk),
                "doc_type": "Lecture Notes",
                "academic_year": "2025/2026",
                "files": [SimpleUploadedFile("digital_notes.pdf", b"%PDF-1.4 digital content", content_type="application/pdf")],
            },
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(response.status_code, 202)
        payload = response.json()
        self.assertTrue(payload["success"])
        self.assertEqual(payload["credits_deducted"], 2)
        self.assertEqual(payload["credits_balance"], 18)
        self.assertEqual(enqueue_ingestion.call_count, 1)

    @patch("services.prep_ingestion.enqueue_prep_document_ingestion")
    def test_freemium_user_with_zero_credits_is_prompted_to_top_up(self, enqueue_ingestion):
        wallet = PrepWallet.get_or_create_wallet(self.user)
        wallet.credit_grants.all().delete()
        wallet.current_plan = "freemium"
        wallet.credits_balance = 0
        wallet.save()

        response = self.client.post(
            reverse("prep:upload"),
            {
                "course_id": str(self.course.pk),
                "doc_type": "Lecture Notes",
                "academic_year": "2025/2026",
                "files": [SimpleUploadedFile("notes_blocked.pdf", b"%PDF-1.4 notes blocked", content_type="application/pdf")],
            },
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(response.status_code, 402)
        payload = response.json()
        self.assertFalse(payload["success"])
        self.assertTrue(payload.get("upgrade_required"))
        self.assertIn("2 credits", payload["error"])
        enqueue_ingestion.assert_not_called()

    @patch("services.prep_ingestion.enqueue_prep_document_ingestion")
    def test_basic_plan_uses_allowance_first_then_deducts_credits_when_exhausted(self, enqueue_ingestion):
        from services.credit_service import grant_subscription
        wallet = PrepWallet.get_or_create_wallet(self.user)
        wallet.credit_grants.all().delete()
        wallet.credits_balance = 0
        wallet.save()

        grant_subscription(wallet, "basic", 250, reference_code="TEST-BASIC-ALLOWANCE")
        wallet.refresh_from_db()
        self.assertEqual(wallet.pdf_uploads_this_month, 0)
        self.assertEqual(wallet.credits_balance, 250)

        # 1. First upload: uses allowance, 0 credits deducted
        res1 = self.client.post(
            reverse("prep:upload"),
            {
                "course_id": str(self.course.pk),
                "doc_type": "Lecture Notes",
                "academic_year": "2025/2026",
                "files": [SimpleUploadedFile("doc1.pdf", b"%PDF-1.4 doc 1 content", content_type="application/pdf")],
            },
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(res1.status_code, 202)
        payload1 = res1.json()
        self.assertEqual(payload1["credits_deducted"], 0)
        wallet.refresh_from_db()
        self.assertEqual(wallet.pdf_uploads_this_month, 1)

        # 2. Simulate allowance exhausted (20 used out of 20 limit)
        wallet.pdf_uploads_this_month = 20
        wallet.save()

        # 3. Next upload: allowance exhausted, falls back to credit deduction (2 credits)
        res2 = self.client.post(
            reverse("prep:upload"),
            {
                "course_id": str(self.course.pk),
                "doc_type": "Lecture Notes",
                "academic_year": "2025/2026",
                "files": [SimpleUploadedFile("doc2.pdf", b"%PDF-1.4 doc 2 content", content_type="application/pdf")],
            },
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(res2.status_code, 202)
        payload2 = res2.json()
        self.assertEqual(payload2["credits_deducted"], 2)
        self.assertEqual(payload2["credits_balance"], 248)


class PrepFailureNotificationRecipientTests(TestCase):
    @override_settings(
        ADMIN_EMAILS=["admins@example.test"],
        ADMIN_EMAILS_NOTIFICATIONS=["alerts@example.test"],
        BASE_URL="https://prep.example.test",
    )
    @patch("services.email_service.send_email_notification", return_value=True)
    def test_note_failure_uses_notification_recipients_only(self, send_email):
        course = PrepCourse.objects.create(
            code="SMA 201",
            title="Real Analysis",
            slug="notification-sma-201",
        )
        topic = PrepTopic.objects.create(
            course=course,
            order=1,
            title="Sequences",
            slug="notification-sequences",
        )
        guard = PrepNoteGenerationGuard.objects.create(
            topic=topic,
            level="level_2",
            source_signature="a" * 64,
            failed_attempts=2,
            status="needs_review",
            last_error="test validation failure",
        )

        self.assertTrue(send_prep_note_generation_failure_email(guard))
        self.assertEqual(send_email.call_count, 1)
        self.assertEqual(send_email.call_args.args[1], "alerts@example.test")