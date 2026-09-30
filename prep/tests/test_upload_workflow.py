import tempfile
from unittest.mock import patch

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from accounts.models import User
from prep.models import (
    PrepCourse,
    PrepCourseEnrollment,
    PrepDocument,
    PrepNoteGenerationGuard,
    PrepTopic,
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