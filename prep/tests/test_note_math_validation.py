import json
from unittest.mock import patch

from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from accounts.models import User
from prep.models import PrepContentCache, PrepCourse, PrepQuestion, PrepTopic, PrepWallet
from services.prep_ai_router import (
    NOTES_CACHE_VERSION,
    _display_math_issues,
    _latex_syntax_issues,
    _note_completion_issues,
    _topic_notes_cache_signature,
    compute_cache_key,
    generate_similar_practice_questions,
    get_or_generate_topic_notes,
)


class NoteMathValidationTests(SimpleTestCase):
    def test_valid_display_math_is_accepted(self):
        content = """## 1. One

Text.

## 2. Two

Text.

## 3. Three

Text.

## 4. Four

Text.

## 5. Five

This final section has enough explanatory material to meet the completion threshold. It explains the
result, gives a useful exam reminder, and ends the notes with substantial instructional content.

$$
\\left\\lvert a_m-a_n\\right\\rvert \\leq \\varepsilon
$$
"""
        self.assertEqual(_display_math_issues(content), [])
        self.assertEqual(_note_completion_issues(content, "Sequences"), [])

    def test_split_right_delimiter_is_rejected(self):
        content = """$$
\\lvert a_m-a_n \\rvert = \\left\\lvert x-y \\right

\\right\\rvert
$$"""
        issues = _display_math_issues(content)
        self.assertTrue(any("blank structural break" in issue for issue in issues))
        self.assertTrue(any("split \\left or \\right delimiter" in issue for issue in issues))

    def test_unmatched_left_right_is_rejected(self):
        issues = _display_math_issues("$$\\left( x + y$$")
        self.assertTrue(any("unmatched \\left/\\right" in issue for issue in issues))

    def test_unmatched_grouping_and_inline_math_are_rejected(self):
        issues = _latex_syntax_issues("A broken inline expression $x + 1 and $$\\frac{1}{2$$")
        self.assertIn("unmatched inline-math delimiter", issues)
        self.assertTrue(any("unmatched braces" in issue for issue in issues))

    def test_balanced_latex_grouping_is_accepted(self):
        content = """The identity $x^2 + y^2$ is useful.

$$
\\sqrt[2]{x^2 + y^2} = \\left\\lvert z \\right\\rvert
$$"""
        self.assertEqual(_latex_syntax_issues(content), [])

    def test_code_block_dollar_signs_are_not_math_validation_errors(self):
        content = """```R
result <- frame$column
$$ not mathematical output
```"""
        self.assertEqual(_display_math_issues(content), [])
        self.assertEqual(_note_completion_issues(content, "Sequences"), [
            "missing section ## 1.",
            "missing section ## 2.",
            "missing section ## 3.",
            "missing section ## 4.",
            "missing section ## 5.",
        ])


class InvalidCachedNoteRecoveryTests(TestCase):
    valid_notes = """## 1. One

Text.

## 2. Two

Text.

## 3. Three

Text.

## 4. Four

Text.

## 5. Five

This final section has enough explanatory material to meet the completion threshold. It explains the
result, gives a useful exam reminder, and ends the notes with substantial instructional content.

$$
\\left\\lvert a_m-a_n\\right\\rvert \\leq \\varepsilon
$$
"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="note_validation_user",
            email="note-validation@example.test",
            password="Valid123",
        )
        self.course = PrepCourse.objects.create(
            code="VAL 101",
            title="Validation Testing",
            slug="validation-testing",
        )
        self.topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Sequences",
            slug="sequences",
        )

    @patch("services.prep_ai_router.route_math_request")
    def test_invalid_cache_is_replaced_and_marked_as_free_recovery(self, route_request):
        signature = _topic_notes_cache_signature(
            self.course, self.topic, self.topic.title, self.topic.subtopics
        )
        cache_key = compute_cache_key(
            "notes", NOTES_CACHE_VERSION, self.course.code, self.topic.title, "level_2", signature
        )
        PrepContentCache.objects.create(
            cache_key=cache_key,
            content_type="topic_notes",
            prompt_hash="old",
            payload={"content": "$$\\left( x \\right\n\n\\right)$$"},
            course=self.course,
            topic=self.topic,
        )
        route_request.return_value = {
            "success": True,
            "content": self.valid_notes,
            "model_used": "test-model",
            "usage": {"total_tokens": 0},
        }

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_2",
            course_obj=self.course,
            topic_obj=self.topic,
        )

        self.assertFalse(result["cached"])
        self.assertTrue(result["regenerated_from_invalid_cache"])
        self.assertEqual(
            PrepContentCache.objects.get(cache_key=cache_key).payload["content"], self.valid_notes.strip()
        )

    def test_cache_only_read_keeps_invalid_entry_for_free_recovery(self):
        signature = _topic_notes_cache_signature(
            self.course, self.topic, self.topic.title, self.topic.subtopics
        )
        cache_key = compute_cache_key(
            "notes", NOTES_CACHE_VERSION, self.course.code, self.topic.title, "level_2", signature
        )
        PrepContentCache.objects.create(
            cache_key=cache_key,
            content_type="topic_notes",
            prompt_hash="old",
            payload={"content": "$$\\left( x \\right\n\n\\right)$$"},
            course=self.course,
            topic=self.topic,
        )

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_2",
            course_obj=self.course,
            topic_obj=self.topic,
            generate_if_missing=False,
        )

        self.assertTrue(result["regenerated_from_invalid_cache"])
        self.assertTrue(PrepContentCache.objects.filter(cache_key=cache_key).exists())

    @patch("prep.views.get_or_generate_topic_notes")
    def test_invalid_cache_recovery_does_not_deduct_student_credits(self, generate_notes):
        wallet = PrepWallet.get_or_create_wallet(self.user)
        before = wallet.credits_balance
        generate_notes.return_value = {
            "notes": self.valid_notes,
            "cached": False,
            "regenerated_from_invalid_cache": True,
            "level": "level_2",
            "model": "test-model",
            "usage": {"total_tokens": 100},
        }
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("prep:api_topic_notes"),
            data='{ "topic_id": "%s", "level": "level_2" }' % self.topic.id,
            content_type="application/json",
        )

        wallet.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["credits_deducted"], 0)
        self.assertEqual(wallet.credits_balance, before)

    @patch("services.prep_ai_router.route_math_request")
    def test_prior_valid_shared_notes_are_served_when_the_current_generation_fails(self, route_request):
        PrepContentCache.objects.create(
            cache_key="notes:legacy:validation-testing:sequences:level_2",
            content_type="topic_notes",
            prompt_hash="previous-version",
            payload={
                "content": self.valid_notes,
                "level": "level_2",
                "model": "previous-model",
            },
            course=self.course,
            topic=self.topic,
        )
        route_request.return_value = {"success": False, "error": "Provider unavailable"}

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_2",
            course_obj=self.course,
            topic_obj=self.topic,
        )

        self.assertTrue(result["cached"])
        self.assertTrue(result["stale"])
        self.assertEqual(result["notes"], self.valid_notes.strip())


class SharedPracticeQuestionTests(TestCase):
    def setUp(self):
        self.course = PrepCourse.objects.create(
            code="PRA 101",
            title="Practice Sharing",
            slug="practice-sharing",
        )
        self.topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Sequences",
            slug="practice-sequences",
        )

    @patch("services.prep_ai_router.route_math_request")
    def test_complete_valid_practice_set_is_saved_once_and_reused_globally(self, route_request):
        route_request.return_value = {
            "success": True,
            "content": json.dumps([
                {
                    "number": 1,
                    "marks": 5,
                    "topic_label": "Arithmetic sequences",
                    "question_latex": "Find the next term of $1, 3, 5, \ldots$.",
                    "solution_latex": "The common difference is $2$, so the next term is $7$.",
                    "hint": "Find the common difference.",
                },
                {
                    "number": 2,
                    "marks": 5,
                    "topic_label": "Geometric sequences",
                    "question_latex": "Find the next term of $2, 6, 18, \ldots$.",
                    "solution_latex": "The common ratio is $3$, so the next term is $54$.",
                    "hint": "Find the common ratio.",
                },
            ]),
            "model_used": "test-model",
            "usage": {"total_tokens": 10},
        }

        first = generate_similar_practice_questions(
            self.course.code,
            self.topic.title,
            question_count=2,
            topic_obj=self.topic,
            course_obj=self.course,
        )
        second = generate_similar_practice_questions(
            self.course.code,
            self.topic.title,
            question_count=2,
            topic_obj=self.topic,
            course_obj=self.course,
        )

        self.assertTrue(first["success"])
        self.assertEqual(first["fresh_generated_count"], 2)
        self.assertEqual(
            PrepQuestion.objects.filter(topic=self.topic, question_type="generated").count(), 2
        )
        self.assertTrue(second["success"])
        self.assertTrue(second["cached"])
        self.assertEqual(second["fresh_generated_count"], 0)
        route_request.assert_called_once()

    @patch("services.prep_ai_router.call_deepseek")
    @patch("services.prep_ai_router.route_math_request")
    def test_incomplete_practice_set_is_not_saved(self, route_request, continue_request):
        route_request.return_value = {
            "success": True,
            "content": json.dumps([
                {
                    "number": 1,
                    "marks": 5,
                    "topic_label": "Arithmetic sequences",
                    "question_latex": "Find the next term of $1, 3, 5, \ldots$.",
                    "solution_latex": "The common difference is $2$.",
                },
            ]),
            "model_used": "test-model",
            "usage": {"total_tokens": 10},
        }
        continue_request.return_value = {"success": False, "error": "Provider unavailable"}

        result = generate_similar_practice_questions(
            self.course.code,
            self.topic.title,
            question_count=2,
            topic_obj=self.topic,
            course_obj=self.course,
        )

        self.assertFalse(result["success"])
        self.assertIn("did not pass validation", result["error"])
        self.assertFalse(PrepQuestion.objects.filter(topic=self.topic, question_type="generated").exists())
        continue_request.assert_called_once()


class TopicStudyQuestionRenderingTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="topic_render_user",
            email="topic-render@example.test",
            password="Valid123",
        )
        self.client.force_login(self.user)
        self.course = PrepCourse.objects.create(
            code="TOP 101",
            title="Topic Rendering",
            slug="topic-rendering",
        )
        self.topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Generated Only",
            slug="generated-only",
        )
        PrepQuestion.objects.create(
            topic=self.topic,
            question_type="generated",
            verification_status="verified",
            number=1,
            marks=5,
            question_latex="Find $x$.",
            solution_latex="$x = 1$.",
        )

    @patch("services.prep_ai_router.get_or_generate_topic_notes")
    def test_topic_page_renders_generated_questions_without_authentic_questions(self, generate_notes):
        generate_notes.return_value = {"notes": "## 1. Valid Notes", "cached": True}

        response = self.client.get(
            reverse("prep:topic_study", kwargs={"topic_id": self.topic.id}) + "?tab=notes"
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Find")

    @patch("services.prep_ai_router.call_deepseek")
    @patch("services.prep_ai_router.route_math_request")
    def test_invalid_practice_set_is_corrected_before_it_is_saved(self, route_request, continue_request):
        incomplete_set = [
            {
                "number": 1,
                "marks": 5,
                "topic_label": "Arithmetic sequences",
                "question_latex": "Find the next term of $1, 3, 5, \\ldots$.",
                "solution_latex": "The common difference is $2$.",
            },
        ]
        corrected_set = incomplete_set + [
            {
                "number": 2,
                "marks": 5,
                "topic_label": "Geometric sequences",
                "question_latex": "Find the next term of $2, 6, 18, \\ldots$.",
                "solution_latex": "The common ratio is $3$, so the next term is $54$.",
            },
        ]
        route_request.return_value = {
            "success": True,
            "content": json.dumps(incomplete_set),
            "model_used": "test-model",
            "usage": {"total_tokens": 10},
        }
        continue_request.return_value = {
            "success": True,
            "content": json.dumps(corrected_set),
            "usage": {"total_tokens": 10},
        }

        result = generate_similar_practice_questions(
            self.course.code,
            self.topic.title,
            question_count=2,
            topic_obj=self.topic,
            course_obj=self.course,
        )

        self.assertTrue(result["success"])
        self.assertEqual(result["fresh_generated_count"], 2)
        self.assertEqual(
            PrepQuestion.objects.filter(topic=self.topic, question_type="generated").count(), 2
        )
        continue_request.assert_called_once()
