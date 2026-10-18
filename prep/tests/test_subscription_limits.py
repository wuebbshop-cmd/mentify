from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from accounts.models import User
from prep.models import PrepCourse, PrepQuestion, PrepTopic, PrepTransaction, PrepWallet
from services.credit_service import (
    InsufficientCredits,
    PlanLimitExceeded,
    enforce_subscription_limit,
    get_available_credits,
    get_remaining_practice_question_allowance,
    grant_subscription,
)


class SubscriptionLimitTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tier_limit_user",
            email="tier-limit@example.test",
            password="Valid123",
        )
        self.wallet = PrepWallet.get_or_create_wallet(self.user)
        grant_subscription(self.wallet, "basic", 250, reference_code="TEST-BASIC")
        self.wallet.refresh_from_db()

    def test_basic_plan_document_upload_cap_is_enforced_from_the_ledger(self):
        # Basic plan has 20 document uploads limit
        for _ in range(20):
            PrepTransaction.objects.create(
                wallet=self.wallet,
                amount=0,
                action_type="upload_text",
                description="Document Ingestion: TEST 101 (digital_pdfplumber)",
            )

        # When credits are 0, exceeding the plan limit raises PlanLimitExceeded
        self.wallet.credit_grants.all().delete()
        self.wallet.credits_balance = 0
        self.wallet.save(update_fields=["credits_balance"])

        with self.assertRaises(PlanLimitExceeded):
            enforce_subscription_limit(self.wallet, "document_uploads")

    def test_basic_plan_document_upload_falls_back_to_credits_when_allowance_exhausted(self):
        for _ in range(20):
            PrepTransaction.objects.create(
                wallet=self.wallet,
                amount=0,
                action_type="upload_text",
                description="Document Ingestion: TEST 101 (digital_pdfplumber)",
            )

        # With credits available, it reports not covered by plan without raising PlanLimitExceeded
        result = enforce_subscription_limit(self.wallet, "document_uploads", required_credits=2)
        self.assertFalse(result["covered_by_plan"])
        self.assertEqual(result["used"], 20)

    def test_practice_endpoint_rejects_before_the_model_when_allowance_exhausted_and_no_credits(self):
        course = PrepCourse.objects.create(
            code="LIM 101",
            title="Limits",
            slug="limits",
        )
        topic = PrepTopic.objects.create(
            course=course,
            order=1,
            title="Limits Topic",
            slug="limits-topic",
        )
        PrepTransaction.objects.create(
            wallet=self.wallet,
            amount=0,
            action_type="ai_practice_gen",
            description="Generated 100 Practice Questions: LIM 101 - Limits Topic",
            metadata={"question_count": 100},
        )
        # Clear credits so fallback is impossible
        self.wallet.credit_grants.all().delete()
        self.wallet.credits_balance = 0
        self.wallet.save(update_fields=["credits_balance"])
        self.client.force_login(self.user)

        with patch("prep.views.generate_similar_practice_questions") as generate_practice:
            response = self.client.post(
                reverse("prep:api_generate_practice"),
                data={"topic_id": topic.id, "count": 1},
            )

        self.assertEqual(response.status_code, 402)
        self.assertIn("used your monthly plan question allowance", response.json()["error"])
        generate_practice.assert_not_called()

    def test_practice_endpoint_deducts_zero_credits_while_within_plan_allowance(self):
        course = PrepCourse.objects.create(
            code="PRAC 101",
            title="Practice Course",
            slug="prac-course",
        )
        topic = PrepTopic.objects.create(
            course=course,
            order=1,
            title="Calculus",
            slug="calculus",
        )
        q1 = PrepQuestion.objects.create(topic=topic, question_type="generated", verification_status="approved", question_latex="Q1", solution_latex="S1")
        q2 = PrepQuestion.objects.create(topic=topic, question_type="generated", verification_status="approved", question_latex="Q2", solution_latex="S2")
        q3 = PrepQuestion.objects.create(topic=topic, question_type="generated", verification_status="approved", question_latex="Q3", solution_latex="S3")

        self.client.force_login(self.user)

        with patch("prep.views.generate_similar_practice_questions") as generate_practice:
            generate_practice.return_value = {
                "success": True,
                "fresh_generated_count": 3,
                "questions": [
                    {"id": q1.id, "question_latex": "Q1", "solution_latex": "S1"},
                    {"id": q2.id, "question_latex": "Q2", "solution_latex": "S2"},
                    {"id": q3.id, "question_latex": "Q3", "solution_latex": "S3"},
                ],
                "usage": {"input_tokens": 100, "output_tokens": 100, "total_tokens": 200},
                "model": "deepseek-chat",
            }
            initial_balance = get_available_credits(self.wallet)
            response = self.client.post(
                reverse("prep:api_generate_practice"),
                data={"topic_id": topic.id, "count": 3, "force_fresh": True},
            )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(data["credits_deducted"], 0)
        self.assertEqual(data["credits_balance"], initial_balance)

    def test_active_recall_drill_deducts_zero_credits_while_within_plan_allowance(self):
        course = PrepCourse.objects.create(
            code="REC 101",
            title="Recall Course",
            slug="recall-course",
        )
        topic = PrepTopic.objects.create(
            course=course,
            order=1,
            title="Recall Topic",
            slug="recall-topic",
        )
        self.client.force_login(self.user)

        with patch("services.prep_topic_quiz.get_or_create_topic_quiz") as mock_quiz:
            mock_quiz.return_value = [
                type("QuizQ", (), {"id": i, "question_text": f"Q{i}", "options": ["A", "B", "C", "D"], "difficulty": "medium"})()
                for i in range(1, 6)
            ]
            initial_balance = get_available_credits(self.wallet)
            response = self.client.get(reverse("prep:api_topic_quiz", kwargs={"topic_id": topic.id}))

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(data["credits_deducted"], 0)
        self.assertEqual(data["credits_balance"], initial_balance)

    @patch("services.prep_ai_router.route_math_request")
    def test_topic_get_does_not_generate_missing_notes(self, route_math_request):
        course = PrepCourse.objects.create(
            code="GET 101",
            title="Read Only Topic",
            slug="read-only-topic",
        )
        topic = PrepTopic.objects.create(
            course=course,
            order=1,
            title="Missing Notes",
            slug="missing-notes",
        )
        self.client.force_login(self.user)

        response = self.client.get(reverse("prep:topic_study", kwargs={"topic_id": topic.id}))

        self.assertEqual(response.status_code, 200)
        route_math_request.assert_not_called()
