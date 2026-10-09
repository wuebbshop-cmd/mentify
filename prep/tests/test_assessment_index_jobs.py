from datetime import timedelta
from io import StringIO
from unittest.mock import patch

from django.contrib.admin.sites import AdminSite
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.test import RequestFactory, TestCase
from django.utils import timezone

from accounts.models import User
from prep.admin import PrepDocumentAdmin
from prep.models import (
    PrepAssessmentIndexJob,
    PrepCourse,
    PrepDocument,
    PrepPaper,
    PrepQuestion,
)
from prep.management.commands.run_prep_assessment_worker import Command
from services.prep_assessment_index import enqueue_assessment_index


class AssessmentIndexJobQueueTests(TestCase):
    def setUp(self):
        self.course = PrepCourse.objects.create(
            code="AIX 101",
            title="Assessment Index Jobs",
            slug="assessment-index-jobs",
        )
        self.document = PrepDocument.objects.create(
            course=self.course,
            doc_type="Final Examination Paper",
            file=SimpleUploadedFile("assessment.pdf", b"source PDF"),
            extracted_text=(
                "--- Page 1 ---\n"
                "1. Explain why every convergent sequence is bounded. (5 marks)"
            ),
            stage="stage_3",
        )
        self.paper = PrepPaper.objects.create(
            id="assessment-index-jobs-paper",
            course=self.course,
            title="Final Examination",
            year="2026",
            total_marks=5,
            source_document=self.document,
        )

    def test_enqueue_is_idempotent_for_the_same_source_and_creates_new_version(self):
        first, first_created = enqueue_assessment_index(self.paper)
        duplicate, duplicate_created = enqueue_assessment_index(self.paper)

        self.document.extracted_text += "\nAdditional source material."
        self.document.save(update_fields=["extracted_text"])
        updated, updated_created = enqueue_assessment_index(self.paper)

        self.assertTrue(first_created)
        self.assertFalse(duplicate_created)
        self.assertFalse(updated.pk == first.pk)
        self.assertEqual(duplicate.pk, first.pk)
        self.assertTrue(updated_created)
        self.assertEqual(
            PrepAssessmentIndexJob.objects.filter(paper=self.paper).count(),
            2,
        )

    def test_force_requeues_a_completed_source_version(self):
        job, _ = enqueue_assessment_index(self.paper)
        job.status = "complete"
        job.stage = "complete"
        job.completed_at = timezone.now()
        job.save(update_fields=["status", "stage", "completed_at"])

        requeued, created = enqueue_assessment_index(self.paper, force=True)

        self.assertTrue(created)
        self.assertEqual(requeued.pk, job.pk)
        self.assertEqual(requeued.status, "pending")
        self.assertEqual(requeued.attempts, 0)

    def test_enqueue_rejects_unapproved_or_unlinked_source(self):
        self.document.stage = "stage_2"
        self.document.save(update_fields=["stage"])

        with self.assertRaisesMessage(ValueError, "not approved for publication"):
            enqueue_assessment_index(self.paper)

        self.document.stage = "stage_3"
        self.document.save(update_fields=["stage"])
        self.paper.source_document = None
        self.paper.save(update_fields=["source_document"])

        with self.assertRaisesMessage(ValueError, "has no source document"):
            enqueue_assessment_index(self.paper)

    @patch.object(PrepDocumentAdmin, "message_user")
    @patch("services.prep_ingestion.index_assessment_questions")
    def test_admin_publication_queues_paper_instead_of_indexing_inline(
        self,
        index_questions,
        _message_user,
    ):
        user = User.objects.create_user(
            username="assessment-publisher",
            email="assessment-publisher@example.test",
            password="safe-test-password",
        )
        document = PrepDocument.objects.create(
            course=self.course,
            doc_type="Final Examination Paper",
            file=SimpleUploadedFile("published-assessment.pdf", b"source PDF"),
            extracted_text=(
                "1. Explain why every convergent sequence is bounded. (5 marks)"
            ),
            stage="stage_2",
        )
        request = RequestFactory().post("/admin/prep/prepdocument/")
        request.user = user
        model_admin = PrepDocumentAdmin(PrepDocument, AdminSite())

        model_admin.approve_stage_3_publish(
            request,
            PrepDocument.objects.filter(pk=document.pk),
        )

        document.refresh_from_db()
        paper = PrepPaper.objects.get(source_document=document)
        self.assertEqual(document.stage, "stage_3")
        self.assertTrue(
            PrepAssessmentIndexJob.objects.filter(
                paper=paper,
                status="pending",
            ).exists()
        )
        index_questions.assert_not_called()

    @patch("services.prep_ingestion.index_assessment_questions", return_value=2)
    def test_worker_completes_job_and_records_index_count(self, index_questions):
        job, _ = enqueue_assessment_index(self.paper)
        output = StringIO()

        call_command("run_prep_assessment_worker", once=True, stdout=output)

        job.refresh_from_db()
        self.assertEqual(job.status, "complete")
        self.assertEqual(job.stage, "complete")
        self.assertEqual(job.indexed_questions, 2)
        self.assertEqual(job.attempts, 1)
        index_questions.assert_called_once_with(
            self.document,
            self.paper,
            reconstruct_invalid=True,
        )

    @patch("services.prep_ingestion.index_assessment_questions")
    def test_manual_reindex_apply_queues_without_ai_reconstruction(self, index_questions):
        output = StringIO()

        call_command(
            "reindex_assessment_questions",
            course_codes=["AIX 101"],
            apply=True,
            stdout=output,
        )

        job = PrepAssessmentIndexJob.objects.get(paper=self.paper)
        self.assertEqual(job.status, "pending")
        self.assertFalse(job.reconstruct_invalid)
        self.assertIn("new indexing jobs queued: 1", output.getvalue())
        index_questions.assert_not_called()

    @patch(
        "services.prep_ingestion.index_assessment_questions",
        side_effect=RuntimeError("temporary provider outage"),
    )
    def test_worker_retries_failed_job_with_backoff_and_surfaces_error(self, _index_questions):
        job, _ = enqueue_assessment_index(self.paper)
        output = StringIO()
        errors = StringIO()

        call_command(
            "run_prep_assessment_worker",
            once=True,
            stdout=output,
            stderr=errors,
        )

        job.refresh_from_db()
        self.assertEqual(job.status, "pending")
        self.assertEqual(job.stage, "retry_wait")
        self.assertEqual(job.attempts, 1)
        self.assertIn("temporary provider outage", job.last_error)
        self.assertGreater(job.next_attempt_at, timezone.now())
        self.assertIn("attempt 1/3", errors.getvalue())

    @patch(
        "services.prep_ingestion.index_assessment_questions",
        side_effect=RuntimeError("permanent provider failure"),
    )
    def test_worker_marks_job_failed_after_bounded_retries(self, _index_questions):
        job, _ = enqueue_assessment_index(self.paper)
        job.attempts = 2
        job.next_attempt_at = timezone.now() - timedelta(seconds=1)
        job.save(update_fields=["attempts", "next_attempt_at"])

        call_command(
            "run_prep_assessment_worker",
            once=True,
            stdout=StringIO(),
            stderr=StringIO(),
        )

        job.refresh_from_db()
        self.assertEqual(job.status, "failed")
        self.assertEqual(job.stage, "failed")
        self.assertEqual(job.attempts, 3)
        self.assertIn("permanent provider failure", job.last_error)
        self.assertIsNotNone(job.completed_at)

    @patch("services.prep_ingestion.index_assessment_questions")
    def test_worker_supersedes_changed_source_and_queues_new_version(self, index_questions):
        job, _ = enqueue_assessment_index(self.paper)
        self.document.extracted_text += "\nThe source was revised."
        self.document.save(update_fields=["extracted_text"])

        Command()._process_job(job)

        job.refresh_from_db()
        self.assertEqual(job.status, "superseded")
        self.assertEqual(job.stage, "superseded")
        self.assertEqual(
            PrepAssessmentIndexJob.objects.filter(
                paper=self.paper,
                status="pending",
            ).count(),
            1,
        )
        index_questions.assert_not_called()

    def test_stale_job_exhausted_on_last_attempt_is_failed_not_retried(self):
        job, _ = enqueue_assessment_index(self.paper)
        job.status = "running"
        job.stage = "indexing"
        job.attempts = 3
        job.started_at = timezone.now() - timedelta(minutes=31)
        job.save(update_fields=["status", "stage", "attempts", "started_at"])

        Command()._recover_stale_jobs()

        job.refresh_from_db()
        self.assertEqual(job.status, "failed")
        self.assertEqual(job.stage, "failed")
        self.assertIsNotNone(job.completed_at)
        self.assertIn("exhausting the retry budget", job.last_error)

    @patch(
        "services.prep_ingestion.index_assessment_questions",
        side_effect=RuntimeError("indexing interrupted"),
    )
    def test_failed_job_does_not_remove_previously_published_questions(self, _index_questions):
        existing = PrepQuestion.objects.create(
            paper=self.paper,
            source_document=self.document,
            question_type="authentic",
            verification_status="auto_validated",
            number=1,
            marks=5,
            question_latex="Previously published valid source question text.",
        )
        enqueue_assessment_index(self.paper)

        call_command(
            "run_prep_assessment_worker",
            once=True,
            stdout=StringIO(),
            stderr=StringIO(),
        )

        self.assertTrue(
            PrepQuestion.objects.filter(
                pk=existing.pk,
                verification_status="auto_validated",
                question_latex="Previously published valid source question text.",
            ).exists()
        )
