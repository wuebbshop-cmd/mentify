import io
import json
from unittest.mock import patch

from django.contrib import admin
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.test import RequestFactory, SimpleTestCase, TestCase
from django.urls import reverse

from accounts.models import User
from prep.models import PrepCourse, PrepDocument, PrepPaper, PrepQuestion, PrepTopic
from prep.admin import PrepQuestionAdmin
from services.prep_ai_router import _practice_question_issues
from services.prep_ingestion import (
    assessment_question_rendering_issues,
    extract_assessment_questions,
    index_assessment_questions,
    learner_visible_assessment_questions,
)


class GeneratedQuestionValidationTests(SimpleTestCase):
    def test_question_splitter_retains_start_page_and_removes_page_headers(self):
        source = (
            "--- Page 4 ---\n"
            "1. Explain how a sequence approaches its limit. (5 marks)\n"
            "--- Page 5 ---\n"
            "Use one example to support your explanation.\n"
            "2. Define a bounded sequence and give a relevant property."
        )

        questions = extract_assessment_questions(source)

        self.assertEqual(len(questions), 2)
        self.assertEqual(questions[0]["source_page_number"], 4)
        self.assertEqual(questions[0]["marks"], 5)
        self.assertIn("Use one example", questions[0]["question_latex"])
        self.assertNotIn("--- Page 5 ---", questions[0]["question_latex"])
        self.assertEqual(questions[1]["source_page_number"], 5)
        self.assertIsNone(questions[0]["extraction_confidence"])

    def test_question_splitter_recognizes_word_number_markdown_and_latex_headings(self):
        source = (
            "**QUESTION ONE** Explain why a convergent sequence is bounded.\n"
            "\\section*{Question Three (6 marks)}\n"
            "Show that the limit is unique."
        )

        questions = extract_assessment_questions(source)

        self.assertEqual([question["number"] for question in questions], [1, 3])
        self.assertIn("Explain why a convergent sequence", questions[0]["question_latex"])
        self.assertIn("Show that the limit is unique", questions[1]["question_latex"])

    def test_question_splitter_removes_scan_and_page_footers(self):
        source = (
            "--- Page 8 ---\n"
            "3. Find the derived set of the integers and decide whether it is closed.\n"
            "Page 3 of 5\n"
            "INVOLVEMENT IN ANY EXAMINATION IRREGULARITY SHALL LEAD TO DISCONTINUATION\n"
            "Scanned with CamScanner\n"
            "4. Prove that every convergent sequence is Cauchy."
        )

        questions = extract_assessment_questions(source)

        self.assertEqual(len(questions), 2)
        self.assertNotIn("Page 3 of 5", questions[0]["question_latex"])
        self.assertNotIn("INVOLVEMENT IN ANY EXAMINATION IRREGULARITY", questions[0]["question_latex"])
        self.assertNotIn("Scanned with CamScanner", questions[0]["question_latex"])
        self.assertIn("Prove that every convergent sequence", questions[1]["question_latex"])

    def test_flags_page_footer_in_existing_question_text(self):
        issues = assessment_question_rendering_issues(
            "Find the derived set of the integers.\n"
            "Page 3 of 5\n"
            "INVOLVEMENT IN ANY EXAMINATION IRREGULARITY SHALL LEAD TO DISCONTINUATION"
        )

        self.assertIn("question text contains document page or scan footer", issues)

    def test_flags_question_content_that_contains_the_following_question_heading(self):
        content = "Part (e): Prove the intersection is open.\n\n**Question Three (20 marks)**"

        self.assertIn(
            "question text contains a following question heading",
            assessment_question_rendering_issues(content),
        )

    def test_flags_document_download_metadata_in_question_text(self):
        content = "Show that the irrational numbers are uncountable. Downloaded by user@example.test"

        self.assertIn(
            "question text contains document download metadata",
            assessment_question_rendering_issues(content),
        )

    def test_flags_infinity_used_instead_of_infimum_before_set(self):
        content = r"Find \sup S and \infty S."

        self.assertIn(
            "question text may have a corrupted infimum operator before S",
            assessment_question_rendering_issues(content),
        )

    def test_flags_observed_pdf_glyph_empty_placeholder_and_detached_index_corruption(self):
        examples = (
            "Explain the estimate (cid:40) and its role in this calculation.",
            r"Estimate the parameter using this model and report the result [].",
            "For a, b, c, .... n, describe the sequence and its convergence.",
        )
        expected_issues = (
            "unreadable PDF character-map placeholder",
            "question text contains an empty extraction placeholder",
            "question text contains a corrupted ellipsis or detached indices",
        )

        for example, expected_issue in zip(examples, expected_issues):
            with self.subTest(example=example):
                self.assertIn(expected_issue, assessment_question_rendering_issues(example))

    def test_flags_unbalanced_latex_in_questions_before_display(self):
        issues = assessment_question_rendering_issues(
            r"Evaluate this expression and explain the result: $$\frac{1}{2$$."
        )

        self.assertTrue(any("unmatched braces" in issue for issue in issues), issues)

    def test_allows_balanced_list_environment_in_latex_question_text(self):
        issues = assessment_question_rendering_issues(
            r"Choose the correct result: \begin{enumerate}\item first option\end{enumerate}"
        )

        self.assertFalse(any("outside display math" in issue for issue in issues), issues)

    def test_rejects_corrupted_r_boolean_operator(self):
        issues = _practice_question_issues([
            {
                "number": 1,
                "marks": 10,
                "topic_label": "Simulation",
                "question_latex": "Write an R function.",
                "solution_latex": "```R\nif (!is.numeric(N) |\n| length(N) != 1) {}\n```",
            },
        ], 1)

        self.assertTrue(any("duplicated boolean operator" in issue for issue in issues))

    def test_rejects_inline_math_split_across_lines(self):
        issues = _practice_question_issues([
            {
                "number": 1,
                "marks": 5,
                "topic_label": "Series",
                "question_latex": "Find the limit.",
                "solution_latex": "Since $\\lim a_n = 1\neq 0$, the series diverges.",
            },
        ], 1)

        self.assertTrue(any("inline-math expression crosses" in issue for issue in issues))

    def test_rejects_corrupted_infimum_in_ai_generated_question(self):
        issues = _practice_question_issues([
            {
                "number": 1,
                "marks": 5,
                "topic_label": "Real Analysis",
                "question_latex": r"Find \sup S and \infty S.",
                "solution_latex": "The supremum is 1.",
            },
        ], 1)

        self.assertTrue(any("infimum operator corrupted" in issue for issue in issues))


class TopicQuestionCourseIsolationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="question_isolation_user",
            email="question-isolation@example.test",
            password="Valid123",
        )
        self.client.force_login(self.user)
        self.real_analysis = PrepCourse.objects.create(
            code="SMA 300",
            title="Real Analysis I",
            slug="sma-300",
        )
        self.real_functions = PrepTopic.objects.create(
            course=self.real_analysis,
            order=1,
            title="Functions",
            slug="real-functions",
        )
        statistics = PrepCourse.objects.create(
            code="SST 301",
            title="Statistical Programming",
            slug="sst-301",
        )
        statistics_topic = PrepTopic.objects.create(
            course=statistics,
            order=1,
            title="User-Defined Functions",
            slug="user-defined-functions",
        )
        paper = PrepPaper.objects.create(
            id="sst-functions-paper",
            course=statistics,
            title="Final Examination",
            year="2026",
            total_marks=14,
        )
        PrepQuestion.objects.create(
            paper=paper,
            topic=statistics_topic,
            question_type="authentic",
            number=1,
            marks=14,
            topic_label="User-Defined Functions",
            question_latex="Write monte_carlo_pi in R.",
            solution_latex="R solution",
        )

    def test_other_course_question_with_similar_topic_label_is_not_displayed(self):
        response = self.client.get(
            reverse("prep:topic_study", kwargs={"topic_id": self.real_functions.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "monte_carlo_pi")

    def test_flagged_source_question_is_not_displayed_before_adaptation(self):
        source = PrepQuestion.objects.create(
            topic=self.real_functions,
            question_type="authentic",
            verification_status="flagged",
            number=2,
            marks=10,
            question_latex="Incomplete source question",
            solution_latex="",
        )
        PrepQuestion.objects.create(
            topic=self.real_functions,
            question_type="adapted",
            reconstructed_from=source,
            verification_status="pending",
            number=2,
            marks=10,
            question_latex="PENDING_ADAPTATION_MARKER: equivalent problem awaiting tutor review.",
            solution_latex="Pending solution awaiting tutor review.",
            reconstruction_metadata={
                "review_status": "pending",
                "original_transcription": source.question_latex,
            },
        )

        response = self.client.get(
            reverse("prep:topic_study", kwargs={"topic_id": self.real_functions.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Incomplete source question")
        self.assertNotContains(response, "PENDING_ADAPTATION_MARKER")
        self.assertNotContains(response, "SOURCE NEEDS RECONSTRUCTION")

    def test_verified_but_corrupted_question_is_not_learner_visible(self):
        corrupted = PrepQuestion.objects.create(
            topic=self.real_functions,
            question_type="authentic",
            verification_status="verified",
            number=3,
            marks=5,
            question_latex="Explain this estimate (cid:40) using the supplied data.",
        )

        self.assertEqual(learner_visible_assessment_questions([corrupted]), [])


class ExistingPastQuestionRepairTests(TestCase):
    def setUp(self):
        self.course = PrepCourse.objects.create(
            code="SST 301",
            title="Programming Language for Statistics 1",
            slug="sst-301-repair-test",
            category="Statistics",
        )
        self.topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Data Types",
            slug="data-types",
            summary="Numeric, character, and logical data types in R.",
            subtopics=["Atomic vectors", "Type conversion"],
        )
        self.paper = PrepPaper.objects.create(
            id="sst301-repair-test-paper",
            course=self.course,
            title="Final Examination",
            year="2026",
            total_marks=20,
        )
        self.source_document = PrepDocument.objects.create(
            course=self.course,
            doc_type="Final Examination Paper",
            file=SimpleUploadedFile("repair-source.pdf", b"source PDF"),
            extracted_text=(
                "--- Page 9 ---\n"
                "R notes explain atomic vectors, their storage modes, and type conversion."
            ),
            stage="stage_3",
        )
        self.paper.source_document = self.source_document
        self.paper.save(update_fields=["source_document"])


    @patch("services.prep_ai_router.route_math_request")
    def test_apply_reconstructs_malformed_question_with_topic_context(self, route_request):
        source = PrepQuestion.objects.create(
            paper=self.paper,
            topic=self.topic,
            question_type="authentic",
            number=1,
            marks=10,
            topic_label=self.topic.title,
            source_document=self.source_document,
            source_page_number=9,
            extraction_confidence=0.35,
            question_latex="BAD_SOURCE_MARKER \ue000: Explain this R data type problem.",
            verification_status="verified",
        )
        route_request.return_value = {
            "success": True,
            "content": json.dumps({
                "marks": 10,
                "topic_label": self.topic.title,
                "question_latex": "AI_RECONSTRUCTED_MARKER: Explain how atomic vectors store numeric values in R.",
                "solution_latex": "Use a numeric vector and check its type with typeof().",
                "hint": "Consider the vector's underlying storage type.",
            }),
            "model_used": "test-model",
            "usage": {},
        }

        call_command(
            "repair_past_questions",
            course_code="SST 301",
            apply=True,
            stdout=io.StringIO(),
        )
        call_command(
            "repair_past_questions",
            course_code="SST 301",
            apply=True,
            stdout=io.StringIO(),
        )

        source.refresh_from_db()
        self.assertEqual(source.verification_status, "flagged")
        self.assertIsNone(source.verified_by)
        adapted = PrepQuestion.objects.get(
            paper=self.paper,
            topic=self.topic,
            question_type="adapted",
            reconstructed_from=source,
        )
        self.assertIn("AI_RECONSTRUCTED_MARKER", adapted.question_latex)
        self.assertEqual(adapted.verification_status, "pending")
        self.assertNotEqual(adapted.question_latex, source.question_latex)
        self.assertEqual(adapted.reconstruction_metadata["review_status"], "pending")
        self.assertEqual(adapted.reconstruction_metadata["original_transcription"], source.question_latex)
        self.assertEqual(adapted.source_document, self.source_document)
        self.assertEqual(adapted.source_page_number, 9)
        self.assertEqual(adapted.extraction_confidence, 0.35)
        self.assertEqual(adapted.reconstruction_metadata["source_document_id"], str(self.source_document.pk))
        self.assertEqual(adapted.reconstruction_metadata["source_page_number"], 9)
        self.assertIn("unreadable private-use glyph", " ".join(adapted.reconstruction_metadata["original_extraction_issues"]))
        self.assertIsNone(adapted.reconstruction_metadata["model_confidence"])
        self.assertEqual(PrepQuestion.objects.filter(reconstructed_from=source).count(), 1)
        self.assertEqual(route_request.call_count, 1)
        self.assertFalse(route_request.call_args.kwargs["is_complex_proof"])
        self.assertEqual(route_request.call_args.kwargs["max_tokens_override"], 3000)
        self.assertFalse(route_request.call_args.kwargs["thinking_enabled"])
        prompt = route_request.call_args.args[0]
        self.assertIn(self.topic.summary, prompt)
        self.assertIn("Atomic vectors", prompt)
        self.assertIn("Type conversion", prompt)
        self.assertIn(source.question_latex, prompt)
        self.assertIn("Source page: 9", prompt)
        self.assertIn("Source-page context (verbatim)", prompt)
        self.assertIn("R notes explain atomic vectors", prompt)

    @patch("services.prep_ai_router.route_math_request")
    def test_high_confidence_reconstruction_is_auto_published_after_validation(self, route_request):
        source = PrepQuestion.objects.create(
            paper=self.paper,
            topic=self.topic,
            question_type="authentic",
            number=4,
            marks=10,
            topic_label=self.topic.title,
            source_document=self.source_document,
            question_latex="BAD_SOURCE_MARKER \ue000: Explain this R data type problem.",
            verification_status="verified",
        )
        route_request.return_value = {
            "success": True,
            "content": json.dumps({
                "marks": 10,
                "topic_label": self.topic.title,
                "question_latex": (
                    "Question 4: Explain how an atomic vector stores values of one basic type in R.\n"
                    "\\begin{enumerate}\\item State what typeof() reports.\\end{enumerate}"
                ),
                "solution_latex": (
                    "An atomic vector stores values of one underlying type. "
                    "The `typeof()` function reports that storage type."
                ),
                "hint": "Check the storage mode.",
                "confidence": 0.94,
            }),
            "model_used": "test-model",
            "usage": {},
        }

        call_command(
            "repair_past_questions",
            course_code="SST 301",
            apply=True,
            stdout=io.StringIO(),
        )
        adapted = PrepQuestion.objects.get(reconstructed_from=source)

        self.assertEqual(adapted.verification_status, "reconstructed")
        self.assertEqual(adapted.reconstruction_metadata["review_status"], "auto_validated")
        self.assertEqual(adapted.reconstruction_metadata["model_confidence"], 0.94)
        self.assertNotIn("Question 4:", adapted.question_latex)
        self.assertIn("\\begin{enumerate}", adapted.question_latex)
        self.assertFalse(assessment_question_rendering_issues(adapted.question_latex))
        self.assertEqual(route_request.call_count, 1)

    @patch("services.prep_ai_router.route_math_request")
    def test_failed_reconstruction_leaves_source_flagged_and_creates_no_replacement(self, route_request):
        source = PrepQuestion.objects.create(
            paper=self.paper,
            topic=self.topic,
            question_type="authentic",
            number=2,
            marks=10,
            topic_label=self.topic.title,
            question_latex="BAD_SOURCE_MARKER \ue000: Explain this R data type problem.",
            verification_status="verified",
        )
        route_request.return_value = {"success": False, "error": "provider unavailable"}

        call_command(
            "repair_past_questions",
            course_code="SST 301",
            apply=True,
            stdout=io.StringIO(),
            stderr=io.StringIO(),
        )

        source.refresh_from_db()
        self.assertEqual(source.verification_status, "flagged")
        self.assertFalse(
            PrepQuestion.objects.filter(
                paper=self.paper,
                topic=self.topic,
                question_type="adapted",
                number=source.number,
                verification_status="verified",
            ).exists()
        )

    @patch("services.prep_ai_router.route_math_request")
    def test_default_dry_run_does_not_call_ai_or_change_source(self, route_request):
        source = PrepQuestion.objects.create(
            paper=self.paper,
            topic=self.topic,
            question_type="authentic",
            number=3,
            marks=10,
            topic_label=self.topic.title,
            question_latex="BAD_SOURCE_MARKER \ue000: Explain this R data type problem.",
            verification_status="verified",
        )

        output = io.StringIO()
        call_command("repair_past_questions", course_code="SST 301", stdout=output)

        route_request.assert_not_called()
        source.refresh_from_db()
        self.assertEqual(source.verification_status, "verified")
        self.assertIn("Candidate limit: all", output.getvalue())

    @patch("services.prep_ai_router.route_math_request")
    def test_damaged_duplicate_is_not_reconstructed_when_clean_copy_covers_source(self, route_request):
        source_text = (
            "(a) Determine the derived set of the integers and state whether it is closed.\n"
            "(b) Prove that every convergent sequence in the real numbers is Cauchy.\n"
            "(c) Find the limit superior and limit inferior of an alternating sequence."
        )
        self.source_document.extracted_text = (
            "--- Page 9 ---\n"
            "3. " + source_text + "\nPage 3 of 5\n"
            "INVOLVEMENT IN ANY EXAMINATION IRREGULARITY SHALL LEAD TO DISCONTINUATION"
        )
        self.source_document.save(update_fields=["extracted_text"])
        source = PrepQuestion.objects.create(
            paper=self.paper,
            topic=self.topic,
            question_type="authentic",
            number=3,
            marks=10,
            topic_label=self.topic.title,
            source_document=self.source_document,
            source_page_number=9,
            question_latex="**",
            verification_status="flagged",
        )
        clean_copy = PrepQuestion.objects.create(
            paper=self.paper,
            topic=self.topic,
            question_type="authentic",
            number=3,
            marks=10,
            topic_label=self.topic.title,
            source_document=self.source_document,
            source_page_number=9,
            question_latex=source_text,
            verification_status="auto_validated",
        )
        output = io.StringIO()
        errors = io.StringIO()

        call_command(
            "repair_past_questions",
            course_code="SST 301",
            apply=True,
            stdout=output,
            stderr=errors,
        )

        route_request.assert_not_called()
        self.assertFalse(PrepQuestion.objects.filter(reconstructed_from=source).exists())
        self.assertIn(f"clean indexed question id={clean_copy.id}", errors.getvalue())
        self.assertIn("covered_by_clean_duplicate=1", output.getvalue())


class QuestionIndexProvenanceTests(TestCase):
    @patch("services.prep_ai_router.route_math_request")
    def test_indexed_question_keeps_document_page_and_auto_validates_clean_source(self, route_request):
        course = PrepCourse.objects.create(
            code="QPX 101",
            title="Question Provenance Testing",
            slug="question-provenance-testing",
        )
        document = PrepDocument.objects.create(
            course=course,
            doc_type="Final Examination Paper",
            file=SimpleUploadedFile("questions.pdf", b"source PDF"),
            extracted_text=(
                "--- Page 8 ---\n"
                "1. Explain why every convergent sequence is bounded and give a supporting example. (6 marks)"
            ),
            stage="stage_3",
        )
        paper = PrepPaper.objects.create(
            id="question-provenance-paper",
            course=course,
            title="Final Examination",
            year="2026",
            total_marks=6,
            source_document=document,
        )

        created = index_assessment_questions(document, paper)

        question = PrepQuestion.objects.get(paper=paper, number=1, question_type="authentic")
        self.assertEqual(created, 1)
        self.assertEqual(question.source_document, document)
        self.assertEqual(question.source_page_number, 8)
        self.assertIsNone(question.extraction_confidence)
        self.assertEqual(question.verification_status, "auto_validated")
        self.assertIn("Explain why every convergent sequence", question.question_latex)
        self.assertEqual(question.reconstruction_metadata, {})
        route_request.assert_not_called()

    @patch("services.prep_ai_router.route_math_request")
    def test_reindex_preserves_distinct_repeated_number_instances(self, route_request):
        course = PrepCourse.objects.create(
            code="QPX 105",
            title="Repeated Question Index Testing",
            slug="repeated-question-index-testing",
        )
        document = PrepDocument.objects.create(
            course=course,
            doc_type="Final Examination Paper",
            file=SimpleUploadedFile("repeated-questions.pdf", b"source PDF"),
            extracted_text=(
                "**QUESTION ONE** Explain why every convergent sequence is bounded.\n"
                "**QUESTION ONE** Give a separate example showing boundedness does not imply convergence."
            ),
            stage="stage_3",
        )
        paper = PrepPaper.objects.create(
            id="repeated-question-index-paper",
            course=course,
            title="Final Examination",
            year="2026",
            total_marks=10,
            source_document=document,
        )

        created_first_run = index_assessment_questions(document, paper, reconstruct_invalid=False)
        created_second_run = index_assessment_questions(document, paper, reconstruct_invalid=False)
        questions = list(
            PrepQuestion.objects.filter(paper=paper, question_type="authentic").order_by("id")
        )

        self.assertEqual(created_first_run, 2)
        self.assertEqual(created_second_run, 0)
        self.assertEqual(len(questions), 2)
        self.assertNotEqual(questions[0].question_latex, questions[1].question_latex)
        self.assertTrue(all(question.number == 1 for question in questions))
        route_request.assert_not_called()

    @patch("services.prep_ai_router.route_math_request")
    def test_reindex_does_not_overwrite_clean_tutor_verified_question(self, route_request):
        course = PrepCourse.objects.create(
            code="QPX 107",
            title="Tutor Verified Reindex Testing",
            slug="tutor-verified-reindex-testing",
        )
        document = PrepDocument.objects.create(
            course=course,
            doc_type="Final Examination Paper",
            file=SimpleUploadedFile("verified-question.pdf", b"source PDF"),
            extracted_text=(
                "1. Explain why every convergent sequence is bounded and include a clear example."
            ),
            stage="stage_3",
        )
        paper = PrepPaper.objects.create(
            id="tutor-verified-reindex-paper",
            course=course,
            title="Final Examination",
            year="2026",
            total_marks=5,
            source_document=document,
        )
        reviewer = User.objects.create_user(
            username="reindex-reviewer",
            email="reindex-reviewer@example.test",
            password="test-password",
        )
        original_text = "Tutor-approved: prove that a convergent sequence is bounded."
        PrepQuestion.objects.create(
            paper=paper,
            source_document=document,
            question_type="authentic",
            verification_status="verified",
            verified_by=reviewer,
            number=1,
            marks=5,
            question_latex=original_text,
        )

        created = index_assessment_questions(document, paper, reconstruct_invalid=False)

        self.assertEqual(created, 0)
        self.assertEqual(
            PrepQuestion.objects.filter(paper=paper, question_type="authentic").count(),
            1,
        )
        self.assertEqual(
            PrepQuestion.objects.get(paper=paper, question_type="authentic").question_latex,
            original_text,
        )
        route_request.assert_not_called()

    @patch("prep.management.commands.reindex_assessment_questions.index_assessment_questions")
    def test_reindex_command_dry_run_does_not_write_or_call_ai(self, index_questions):
        course = PrepCourse.objects.create(
            code="QPX 106",
            title="Assessment Command Testing",
            slug="assessment-command-testing",
        )
        document = PrepDocument.objects.create(
            course=course,
            doc_type="Final Examination Paper",
            file=SimpleUploadedFile("assessment.pdf", b"source PDF"),
            extracted_text="1. Explain why every convergent sequence is bounded.",
            stage="stage_3",
        )
        PrepPaper.objects.create(
            id="assessment-command-paper",
            course=course,
            title="Final Examination",
            year="2026",
            total_marks=5,
            source_document=document,
        )
        self.assertEqual(
            PrepDocument.objects.filter(
                pk=document.pk,
                stage="stage_3",
                doc_type__in=["Continuous Assessment Test (CAT)", "Final Examination Paper"],
            ).count(),
            1,
        )
        self.assertEqual(document.derived_papers.count(), 1)
        output = io.StringIO()

        call_command(
            "reindex_assessment_questions",
            course_codes=["QPX 106"],
            stdout=output,
        )

        self.assertIn("DRY RUN", output.getvalue())
        self.assertIn("parsed_questions=1", output.getvalue())
        index_questions.assert_not_called()

    @patch("services.prep_ai_router.route_math_request")
    def test_damaged_question_is_flagged_with_page_and_never_auto_reconstructed(self, route_request):
        course = PrepCourse.objects.create(
            code="QPX 103",
            title="Damaged Question Index Testing",
            slug="damaged-question-index-testing",
        )
        document = PrepDocument.objects.create(
            course=course,
            doc_type="Final Examination Paper",
            file=SimpleUploadedFile("damaged-questions.pdf", b"source PDF"),
            extracted_text=(
                "--- Page 11 ---\n"
                "1. Find the limit of BAD_SOURCE_MARKER \ue000 for the sequence and justify your result."
            ),
            stage="stage_3",
        )
        paper = PrepPaper.objects.create(
            id="damaged-question-index-paper",
            course=course,
            title="Final Examination",
            year="2026",
            total_marks=5,
            source_document=document,
        )

        index_assessment_questions(document, paper)

        question = PrepQuestion.objects.get(paper=paper, number=1, question_type="authentic")
        self.assertEqual(question.verification_status, "flagged")
        self.assertEqual(question.source_document, document)
        self.assertEqual(question.source_page_number, 11)
        self.assertIn("BAD_SOURCE_MARKER", question.question_latex)
        self.assertFalse(PrepQuestion.objects.filter(reconstructed_from=question).exists())
        route_request.assert_not_called()

    @patch("services.prep_ai_router.route_math_request")
    def test_indexing_automatically_reconstructs_damaged_question_with_topic_evidence(self, route_request):
        course = PrepCourse.objects.create(
            code="QPX 104",
            title="Automatic Reconstruction Testing",
            slug="automatic-reconstruction-testing",
        )
        topic = PrepTopic.objects.create(
            course=course,
            order=1,
            title="Atomic Vectors",
            slug="atomic-vectors",
            summary="Atomic vectors store values of one basic data type in R.",
            subtopics=["Vector storage", "Type conversion"],
        )
        document = PrepDocument.objects.create(
            course=course,
            doc_type="Final Examination Paper",
            file=SimpleUploadedFile("automatic-repair.pdf", b"source PDF"),
            extracted_text=(
                "--- Page 6 ---\n"
                "1. BAD_SOURCE_MARKER \ue000: Explain how atomic vectors store values in R. (5 marks)"
            ),
            stage="stage_3",
        )
        paper = PrepPaper.objects.create(
            id="automatic-reconstruction-paper",
            course=course,
            title="Final Examination",
            year="2026",
            total_marks=5,
            source_document=document,
        )
        route_request.return_value = {
            "success": True,
            "content": json.dumps({
                "marks": 5,
                "topic_label": topic.title,
                "question_latex": "Explain how an atomic vector stores values of one data type in R.",
                "solution_latex": "An atomic vector stores values of a single type. Use typeof(x) to inspect the underlying type.",
                "hint": "Consider the vector's storage mode.",
                "confidence": 0.93,
            }),
            "model_used": "test-model",
            "usage": {"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30},
        }

        index_assessment_questions(document, paper)

        source = PrepQuestion.objects.get(paper=paper, question_type="authentic", number=1)
        adapted = PrepQuestion.objects.get(paper=paper, question_type="adapted", reconstructed_from=source)
        self.assertEqual(source.verification_status, "flagged")
        self.assertIn("BAD_SOURCE_MARKER", source.question_latex)
        self.assertEqual(source.source_page_number, 6)
        self.assertEqual(source.reconstruction_metadata["original_transcription"], source.question_latex)
        self.assertIn("unreadable private-use glyph", " ".join(source.reconstruction_metadata["original_extraction_issues"]))
        self.assertEqual(adapted.verification_status, "reconstructed")
        self.assertEqual(adapted.source_document, document)
        self.assertEqual(adapted.source_page_number, 6)
        self.assertEqual(adapted.reconstruction_metadata["review_status"], "auto_validated")
        self.assertEqual(adapted.reconstruction_metadata["model_confidence"], 0.93)
        self.assertIn("Approved topic summary", route_request.call_args.args[0])
        self.assertIn("Source page: 6", route_request.call_args.args[0])
        self.assertEqual(route_request.call_args.kwargs["max_tokens_override"], 3000)
        self.assertFalse(route_request.call_args.kwargs["auto_continue"])
        route_request.assert_called_once()

        index_assessment_questions(document, paper)

        self.assertEqual(route_request.call_count, 1)
        self.assertEqual(PrepQuestion.objects.filter(reconstructed_from=source).count(), 1)

    @patch("services.prep_ai_router.route_math_request")
    def test_low_confidence_automatic_reconstruction_stays_pending(self, route_request):
        course = PrepCourse.objects.create(
            code="QPX 105",
            title="Low Confidence Reconstruction Testing",
            slug="low-confidence-reconstruction-testing",
        )
        topic = PrepTopic.objects.create(
            course=course,
            order=1,
            title="Atomic Vectors",
            slug="low-confidence-atomic-vectors",
            summary="Atomic vectors store values of one basic data type in R.",
        )
        document = PrepDocument.objects.create(
            course=course,
            doc_type="Final Examination Paper",
            file=SimpleUploadedFile("low-confidence.pdf", b"source PDF"),
            extracted_text=(
                "--- Page 3 ---\n"
                "1. BAD_SOURCE_MARKER \ue000: Explain how atomic vectors store values in R."
            ),
            stage="stage_3",
        )
        paper = PrepPaper.objects.create(
            id="low-confidence-question-paper",
            course=course,
            title="Final Examination",
            year="2026",
            total_marks=5,
            source_document=document,
        )
        route_request.return_value = {
            "success": True,
            "content": json.dumps({
                "marks": 5,
                "topic_label": topic.title,
                "question_latex": "Explain how an atomic vector stores values of one data type in R.",
                "solution_latex": "An atomic vector stores values of one underlying type.",
                "hint": "Consider storage mode.",
                "confidence": 0.55,
            }),
            "model_used": "test-model",
            "usage": {},
        }

        index_assessment_questions(document, paper)

        source = PrepQuestion.objects.get(paper=paper, question_type="authentic", number=1)
        adapted = PrepQuestion.objects.get(reconstructed_from=source)
        self.assertEqual(source.verification_status, "flagged")
        self.assertEqual(adapted.verification_status, "pending")
        self.assertEqual(adapted.reconstruction_metadata["review_status"], "pending")
        self.assertEqual(adapted.reconstruction_metadata["model_confidence"], 0.55)

    @patch.object(PrepQuestionAdmin, "message_user")
    def test_adapted_question_is_verified_only_by_explicit_tutor_action(self, _message_user):
        user = User.objects.create_user(username="question-reviewer", password="Valid123")
        course = PrepCourse.objects.create(
            code="QPX 102",
            title="Reconstruction Review Testing",
            slug="reconstruction-review-testing",
        )
        source = PrepDocument.objects.create(
            course=course,
            doc_type="Final Examination Paper",
            file=SimpleUploadedFile("review-source.pdf", b"pdf"),
            extracted_text="--- Page 2 ---\nOriginal unreadable source transcription.",
        )
        paper = PrepPaper.objects.create(
            id="reconstruction-review-paper",
            course=course,
            title="Final Examination",
            year="2026",
            total_marks=5,
            source_document=source,
        )
        original = PrepQuestion.objects.create(
            paper=paper,
            source_document=source,
            source_page_number=2,
            question_type="authentic",
            number=1,
            marks=5,
            question_latex="BAD_SOURCE_MARKER: Original transcription remains here.",
            verification_status="flagged",
        )
        adapted = PrepQuestion.objects.create(
            paper=paper,
            source_document=source,
            source_page_number=2,
            reconstructed_from=original,
            question_type="adapted",
            number=1,
            marks=5,
            question_latex="A newly worded equivalent question.",
            verification_status="pending",
            reconstruction_metadata={
                "review_status": "pending",
                "original_transcription": original.question_latex,
                "source_page_number": 2,
            },
        )
        request = RequestFactory().post("/admin/prep/prepquestion/")
        request.user = user
        model_admin = PrepQuestionAdmin(PrepQuestion, admin.site)

        model_admin.verify_questions(request, PrepQuestion.objects.filter(pk=adapted.pk))

        original.refresh_from_db()
        adapted.refresh_from_db()
        self.assertEqual(original.verification_status, "flagged")
        self.assertEqual(original.question_latex, "BAD_SOURCE_MARKER: Original transcription remains here.")
        self.assertEqual(adapted.verification_status, "verified")
        self.assertEqual(adapted.verified_by, user)
        self.assertEqual(adapted.reconstruction_metadata["review_status"], "approved")
        self.assertEqual(adapted.reconstruction_metadata["reviewed_by"], str(user.pk))
        self.assertEqual(adapted.reconstructed_from, original)
