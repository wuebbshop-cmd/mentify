import io
import json
from unittest.mock import patch

from django.core.management import call_command
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from accounts.models import User
from prep.models import PrepCourse, PrepPaper, PrepQuestion, PrepTopic
from services.prep_ai_router import _practice_question_issues
from services.prep_ingestion import assessment_question_rendering_issues


class GeneratedQuestionValidationTests(SimpleTestCase):
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
        PrepQuestion.objects.create(
            topic=self.real_functions,
            question_type="authentic",
            verification_status="flagged",
            number=2,
            marks=10,
            question_latex="Incomplete source question",
            solution_latex="",
        )

        response = self.client.get(
            reverse("prep:topic_study", kwargs={"topic_id": self.real_functions.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Incomplete source question")
        self.assertNotContains(response, "SOURCE NEEDS RECONSTRUCTION")


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

    @patch("services.prep_ai_router.route_math_request")
    def test_apply_reconstructs_malformed_question_with_topic_context(self, route_request):
        source = PrepQuestion.objects.create(
            paper=self.paper,
            topic=self.topic,
            question_type="authentic",
            number=1,
            marks=10,
            topic_label=self.topic.title,
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

        source.refresh_from_db()
        self.assertEqual(source.verification_status, "flagged")
        self.assertIsNone(source.verified_by)
        adapted = PrepQuestion.objects.get(
            paper=self.paper,
            topic=self.topic,
            question_type="adapted",
            verification_status="verified",
        )
        self.assertIn("AI_RECONSTRUCTED_MARKER", adapted.question_latex)
        prompt = route_request.call_args.args[0]
        self.assertIn(self.topic.summary, prompt)
        self.assertIn("Atomic vectors", prompt)
        self.assertIn("Type conversion", prompt)
        self.assertIn(source.question_latex, prompt)

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

        call_command("repair_past_questions", course_code="SST 301", stdout=io.StringIO())

        route_request.assert_not_called()
        source.refresh_from_db()
        self.assertEqual(source.verification_status, "verified")
