from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from accounts.models import User
from prep.models import PrepCourse, PrepQuestion, PrepTopic, PrepTransaction, PrepWallet
from services.credit_service import PlanLimitExceeded, enforce_subscription_limit, grant_subscription


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
        for _ in range(10):
            PrepTransaction.objects.create(
                wallet=self.wallet,
                amount=-2,
                action_type="upload_text",
                description="Document Ingestion: TEST 101 (digital_pdfplumber)",
            )

        with self.assertRaises(PlanLimitExceeded):
            enforce_subscription_limit(self.wallet, "document_uploads")

    def test_practice_endpoint_rejects_before_the_model_at_the_plan_cap(self):
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
            amount=-100,
            action_type="ai_practice_gen",
            description="Generated 100 Practice Questions: LIM 101 - Limits Topic",
            metadata={"question_count": 100},
        )
        self.client.force_login(self.user)

        with patch("prep.views.generate_similar_practice_questions") as generate_practice:
            response = self.client.post(
                reverse("prep:api_generate_practice"),
                data={"topic_id": topic.id, "count": 1},
            )

        self.assertEqual(response.status_code, 403)
        self.assertIn("includes 100 practice questions", response.json()["error"])
        generate_practice.assert_not_called()

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
