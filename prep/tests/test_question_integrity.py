from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from accounts.models import User
from prep.models import PrepCourse, PrepPaper, PrepQuestion, PrepTopic
from services.prep_ai_router import _practice_question_issues


class GeneratedQuestionValidationTests(SimpleTestCase):
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
