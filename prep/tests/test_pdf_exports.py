from unittest.mock import patch

import fitz
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from accounts.models import User
from prep.models import PrepCourse, PrepPaper, PrepQuestion, PrepTopic
from services.prep_export_service import (
    _build_topic_notes_html,
    export_paper_questions_pdf,
    export_topic_notes_pdf,
)


class PrepPdfExportTests(SimpleTestCase):
    """Keep PDF exports aligned with the validated note source and renderer."""

    notes_source = """# Export Sentinel Heading

| Concept | Value |
|---|---|
| Export Table Sentinel | $x^2$ |

```R
export_code_sentinel <- 1
```

$$
x^2 = 4
$$
"""

    questions = [
        {
            "number": 1,
            "marks": 10,
            "topic": "Export Topic",
            "question_latex": "QUESTION_SENTINEL: Solve $x^2=4$.",
            "solution_latex": "ANSWER_SENTINEL: $x=2$ or $x=-2$.",
        }
    ]

    @staticmethod
    def _pdf_text(pdf_bytes):
        document = fitz.open(stream=pdf_bytes, filetype="pdf")
        try:
            return "".join(page.get_text() for page in document)
        finally:
            document.close()

    @patch("services.prep_export_service._render_html_with_playwright", return_value=b"")
    def test_notes_pdf_preserves_validated_source_and_uses_shared_renderer(self, _render_pdf):
        html = _build_topic_notes_html("TST 101", "Export Topic", self.notes_source)
        self.assertIn("normalizeLegacyMathBlocks", html)
        self.assertIn("Export Sentinel Heading", html)

        pdf_bytes = export_topic_notes_pdf("TST 101", "Export Topic", self.notes_source, level="level_2")
        pdf_text = self._pdf_text(pdf_bytes)

        self.assertTrue(pdf_bytes.startswith(b"%PDF"))
        self.assertGreater(len(pdf_bytes), 1000)
        self.assertIn("Export Sentinel Heading", pdf_text)
        self.assertIn("Export Table Sentinel", pdf_text)

    @patch("services.prep_export_service._render_html_with_playwright", return_value=b"")
    def test_paper_questions_and_answers_export_separately(self, _render_pdf):
        questions_pdf = export_paper_questions_pdf(
            "TST 101",
            "CAT Export",
            "2026",
            10,
            self.questions,
            include_questions=True,
            include_answers=False,
        )
        answers_pdf = export_paper_questions_pdf(
            "TST 101",
            "CAT Export",
            "2026",
            10,
            self.questions,
            include_questions=False,
            include_answers=True,
        )

        questions_text = self._pdf_text(questions_pdf)
        answers_text = self._pdf_text(answers_pdf)

        self.assertIn("QUESTION_SENTINEL", questions_text)
        self.assertNotIn("ANSWER_SENTINEL", questions_text)
        self.assertIn("ANSWER_SENTINEL", answers_text)
        self.assertNotIn("QUESTION_SENTINEL", answers_text)

    def test_paper_export_requires_content_selection(self):
        with self.assertRaises(ValueError):
            export_paper_questions_pdf(
                "TST 101",
                "CAT Export",
                "2026",
                10,
                self.questions,
                include_questions=False,
                include_answers=False,
            )


class PrepPdfExportEndpointTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="pdf_export_user",
            email="pdf-export@example.test",
            password="Valid123",
        )
        self.client.force_login(self.user)
        self.course = PrepCourse.objects.create(
            code="PDF 101",
            title="PDF Export Testing",
            slug="pdf-export-testing",
        )
        self.paper = PrepPaper.objects.create(
            id="pdf-export-cat-1",
            course=self.course,
            title="CAT 1",
            year="2026",
            total_marks=10,
        )
        PrepQuestion.objects.create(
            paper=self.paper,
            number=1,
            marks=10,
            topic_label="Export Topic",
            question_latex="Question source",
            solution_latex="Answer source",
        )

    @patch("prep.views.export_paper_questions_pdf", return_value=b"%PDF-test")
    def test_export_endpoint_selects_questions_or_answers(self, exporter):
        url = reverse(
            "prep:export_paper",
            kwargs={"course_code": "PDF-101", "paper_id": self.paper.id, "fmt": "pdf"},
        )

        questions_response = self.client.get(f"{url}?section=questions")
        self.assertEqual(questions_response.status_code, 200)
        self.assertEqual(questions_response["Content-Type"], "application/pdf")
        self.assertIn("_questions.pdf", questions_response["Content-Disposition"])
        self.assertTrue(exporter.call_args.kwargs["include_questions"])
        self.assertFalse(exporter.call_args.kwargs["include_answers"])

        answers_response = self.client.get(f"{url}?section=answers")
        self.assertEqual(answers_response.status_code, 200)
        self.assertIn("_answers.pdf", answers_response["Content-Disposition"])
        self.assertFalse(exporter.call_args.kwargs["include_questions"])
        self.assertTrue(exporter.call_args.kwargs["include_answers"])

    @patch("prep.views.export_paper_questions_pdf", return_value=b"%PDF-test")
    def test_topic_questions_and_answers_export_combines_authentic_and_generated(self, exporter):
        topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Topic Export",
            slug="topic-export",
        )
        PrepQuestion.objects.create(
            topic=topic,
            question_type="authentic",
            number=1,
            marks=8,
            topic_label=topic.title,
            question_latex="Authentic question source",
            solution_latex="Authentic answer source",
        )
        PrepQuestion.objects.create(
            topic=topic,
            question_type="generated",
            verification_status="verified",
            number=1,
            marks=6,
            topic_label=topic.title,
            question_latex="Generated question source",
            solution_latex="Generated answer source",
        )

        url = reverse(
            "prep:export_topic",
            kwargs={"topic_id": topic.id, "fmt": "pdf"},
        )
        response = self.client.get(f"{url}?section=questions_answers")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/pdf")
        self.assertIn("_questions_answers.pdf", response["Content-Disposition"])
        self.assertEqual(exporter.call_args.args[3], 14)
        self.assertEqual(len(exporter.call_args.args[4]), 2)
        self.assertEqual(exporter.call_args.args[4][0]["question_latex"], "Authentic question source")
        self.assertEqual(exporter.call_args.args[4][1]["question_latex"], "Generated question source")
        self.assertTrue(exporter.call_args.kwargs["include_questions"])
        self.assertTrue(exporter.call_args.kwargs["include_answers"])
