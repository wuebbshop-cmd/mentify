import json
from io import StringIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.test import TestCase

from prep.models import PrepContentCache, PrepCourse, PrepDocument, PrepPaper, PrepQuestion
from services.prep_ai_router import NOTE_VALIDATION_STATE


class PilotPipelineAuditTests(TestCase):
    def test_audit_is_dry_run_and_reports_risks_as_json(self):
        course = PrepCourse.objects.create(
            code="PIL 101",
            title="Pilot Testing",
            slug="pilot-testing",
        )
        document = PrepDocument.objects.create(
            course=course,
            doc_type="Final Examination Paper",
            file=SimpleUploadedFile("pilot.pdf", b"pdf"),
            stage="stage_3",
            validation_report={
                "status": "needs_review",
                "issues": [{"code": "review_needed"}],
            },
        )
        paper = PrepPaper.objects.create(
            id="pilot-paper",
            course=course,
            title="Pilot Paper",
            year="2026",
            total_marks=10,
            source_document=document,
        )
        PrepQuestion.objects.create(
            paper=paper,
            source_document=document,
            source_page_number=2,
            question_type="authentic",
            verification_status="auto_validated",
            number=1,
            marks=10,
            question_latex="A clean source question.",
        )
        PrepQuestion.objects.create(
            paper=paper,
            source_document=document,
            source_page_number=2,
            question_type="adapted",
            verification_status="pending",
            number=1,
            marks=10,
            question_latex="Pending adaptation.",
            reconstruction_metadata={"review_status": "pending"},
        )
        PrepContentCache.objects.create(
            cache_key="pilot-note-cache",
            content_type="topic_notes",
            prompt_hash="pilot",
            course=course,
            payload={"content": "notes", "validation_state": "validated-v3-source-modalities"},
        )
        before_documents = PrepDocument.objects.count()
        before_questions = PrepQuestion.objects.count()
        output = StringIO()

        call_command("pilot_pipeline_audit", "--course-code", "PIL 101", "--json", stdout=output)

        report = json.loads(output.getvalue())
        self.assertEqual(report["mode"], "dry_run")
        self.assertEqual(report["provider_calls"], 0)
        self.assertFalse(report["ready_for_expansion"])
        self.assertEqual(report["courses"][0]["documents"]["needs_review"], 1)
        self.assertGreater(report["courses"][0]["risks"].__len__(), 0)
        self.assertEqual(PrepDocument.objects.count(), before_documents)
        self.assertEqual(PrepQuestion.objects.count(), before_questions)

    def test_default_output_advertises_no_provider_or_write_activity(self):
        course = PrepCourse.objects.create(
            code="PIL 102",
            title="Empty Pilot Testing",
            slug="empty-pilot-testing",
        )
        output = StringIO()

        call_command("pilot_pipeline_audit", "--course-code", course.code, stdout=output)

        self.assertIn("DRY RUN: no records changed and no provider calls made.", output.getvalue())
        self.assertIn("ready=False", output.getvalue())

    def test_unresolved_documents_questions_and_caches_block_readiness(self):
        course = PrepCourse.objects.create(
            code="PIL 103",
            title="Blocked Pilot Testing",
            slug="blocked-pilot-testing",
        )
        document = PrepDocument.objects.create(
            course=course,
            doc_type="Final Examination Paper",
            file=SimpleUploadedFile("blocked.pdf", b"pdf"),
            stage="stage_3",
            validation_report={"status": "needs_review", "issues": [{"code": "review_needed"}]},
        )
        paper = PrepPaper.objects.create(
            id="blocked-paper",
            course=course,
            title="Blocked Paper",
            year="2026",
            total_marks=10,
            source_document=document,
        )
        PrepQuestion.objects.create(
            paper=paper,
            question_type="authentic",
            verification_status="flagged",
            number=1,
            marks=10,
            question_latex="Question requiring review.",
        )
        PrepContentCache.objects.create(
            cache_key="blocked-note-cache",
            content_type="topic_notes",
            prompt_hash="blocked",
            course=course,
            payload={"content": "Unvalidated notes."},
        )
        output = StringIO()

        call_command("pilot_pipeline_audit", "--course-code", course.code, "--json", stdout=output)

        course_report = json.loads(output.getvalue())["courses"][0]
        self.assertFalse(course_report["ready_for_expansion"])
        self.assertEqual(course_report["caches"]["invalid_or_unvalidated"], 1)
        self.assertTrue(any("validation status is needs_review" in risk for risk in course_report["risks"]))
        self.assertTrue(any("non-learner-visible status flagged" in risk for risk in course_report["risks"]))
        self.assertTrue(any("lacks current validation metadata" in risk for risk in course_report["risks"]))

    def test_fully_validated_course_can_pass_readiness_gate(self):
        course = PrepCourse.objects.create(
            code="PIL 104",
            title="Ready Pilot Testing",
            slug="ready-pilot-testing",
        )
        document = PrepDocument.objects.create(
            course=course,
            doc_type="Final Examination Paper",
            file=SimpleUploadedFile("ready.pdf", b"pdf"),
            stage="stage_3",
            validation_report={"status": "passed", "issues": []},
        )
        paper = PrepPaper.objects.create(
            id="ready-paper",
            course=course,
            title="Ready Paper",
            year="2026",
            total_marks=10,
            source_document=document,
        )
        PrepQuestion.objects.create(
            paper=paper,
            question_type="authentic",
            verification_status="verified",
            number=1,
            marks=10,
            question_latex="A verified source question.",
        )
        PrepContentCache.objects.create(
            cache_key="ready-note-cache",
            content_type="topic_notes",
            prompt_hash="ready",
            course=course,
            payload={"content": "Validated notes.", "validation_state": NOTE_VALIDATION_STATE},
        )
        output = StringIO()

        call_command("pilot_pipeline_audit", "--course-code", course.code, "--json", stdout=output)

        course_report = json.loads(output.getvalue())["courses"][0]
        self.assertTrue(course_report["ready_for_expansion"])
        self.assertEqual(course_report["risks"], [])
