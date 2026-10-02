import json
from io import StringIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.test import TestCase

from prep.models import PrepContentCache, PrepCourse, PrepDocument, PrepPaper, PrepQuestion, PrepTopic


class PipelineBackfillTests(TestCase):
    def setUp(self):
        self.course = PrepCourse.objects.create(
            code="BFL 101",
            title="Backfill Testing",
            slug="backfill-testing",
        )
        self.topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Sequences",
            slug="backfill-sequences",
        )
        self.document = PrepDocument.objects.create(
            course=self.course,
            doc_type="Lecture Notes",
            topic_name=self.topic.title,
            file=SimpleUploadedFile("backfill.pdf", b"pdf"),
            extracted_text="--- Page 4 ---\nSequences approach limits.",
            stage="stage_3",
        )
        self.paper = PrepPaper.objects.create(
            id="backfill-paper",
            course=self.course,
            title="Backfill Paper",
            year="2026",
            total_marks=10,
            source_document=self.document,
        )

    def test_dry_run_does_not_change_legacy_records(self):
        adapted = PrepQuestion.objects.create(
            paper=self.paper,
            topic=self.topic,
            question_type="adapted",
            verification_status="reconstructed",
            number=1,
            marks=5,
            question_latex="Legacy adapted question.",
            reconstruction_metadata={},
        )
        cache = PrepContentCache.objects.create(
            cache_key="backfill-legacy-note",
            course=self.course,
            topic=self.topic,
            content_type="topic_notes",
            prompt_hash="legacy",
            payload={"content": "## 1. One\n\nLegacy note."},
        )
        output = StringIO()

        call_command("backfill_pipeline_records", "--course-code", self.course.code, stdout=output)

        adapted.refresh_from_db()
        cache.refresh_from_db()
        self.assertEqual(adapted.verification_status, "reconstructed")
        self.assertEqual(adapted.reconstruction_metadata, {})
        self.assertEqual(cache.payload, {"content": "## 1. One\n\nLegacy note."})
        self.assertIn("DRY RUN", output.getvalue())

    def test_apply_writes_validation_and_quarantines_untraceable_adaptation(self):
        adapted = PrepQuestion.objects.create(
            paper=self.paper,
            topic=self.topic,
            question_type="adapted",
            verification_status="reconstructed",
            number=1,
            marks=5,
            question_latex="Legacy adapted question.",
            reconstruction_metadata={},
        )
        output = StringIO()

        call_command(
            "backfill_pipeline_records",
            "--course-code", self.course.code,
            "--apply",
            "--json",
            stdout=output,
        )

        report = json.loads(output.getvalue())
        self.document.refresh_from_db()
        adapted.refresh_from_db()
        self.assertEqual(self.document.validation_report["status"], "needs_review")
        self.assertEqual(adapted.verification_status, "pending")
        self.assertEqual(adapted.reconstruction_metadata["review_status"], "needs_review")
        self.assertGreaterEqual(report["adaptations_quarantined"], 1)
        self.assertEqual(report["provider_calls"], 0)
