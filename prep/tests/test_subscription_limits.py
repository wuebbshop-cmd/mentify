from unittest.mock import patch
from io import StringIO

from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from accounts.models import User
from prep.models import PrepCourse, PrepQuestion, PrepTopic, PrepTransaction, PrepWallet
from services.credit_service import (
    InsufficientCredits,
    PlanLimitExceeded,
    enforce_subscription_limit,
    get_available_credits,
    get_free_credit_entitlement,
    get_remaining_practice_question_allowance,
    grant_freemium_monthly,
    grant_subscription,
    is_student_email,
    notify_standard_account_credit_limit,
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


class FreeCreditEntitlementTests(TestCase):
    def create_user_and_wallet(self, email):
        user = User.objects.create_user(
            username=email.replace("@", "_").replace(".", "_"),
            email=email,
            password="Valid123",
        )
        return user, PrepWallet.get_or_create_wallet(user)

    def test_student_subdomain_receives_standard_trial_and_freemium_allowances(self):
        user, wallet = self.create_user_and_wallet("5507.2022@students.ku.ac.ke")

        entitlement = get_free_credit_entitlement(user)
        self.assertTrue(entitlement["is_student"])
        self.assertEqual(entitlement["trial_credits"], 100)
        self.assertEqual(entitlement["freemium_credits"], 20)
        self.assertEqual(wallet.credit_grants.get(source="trial").granted_credits, 100)

        grant_freemium_monthly(wallet)
        self.assertEqual(
            wallet.credit_grants.filter(source="subscription").latest("id").granted_credits,
            20,
        )

    def test_personal_address_receives_reduced_trial_and_freemium_allowances(self):
        user, wallet = self.create_user_and_wallet("learner.personal@gmail.com")

        entitlement = get_free_credit_entitlement(user)
        self.assertFalse(entitlement["is_student"])
        self.assertEqual(entitlement["trial_credits"], 10)
        self.assertEqual(entitlement["freemium_credits"], 10)
        self.assertEqual(wallet.credit_grants.get(source="trial").granted_credits, 10)

        grant_freemium_monthly(wallet)
        self.assertEqual(
            wallet.credit_grants.filter(source="subscription").latest("id").granted_credits,
            10,
        )

    def test_student_detection_does_not_accept_all_kenyan_or_institutional_domains(self):
        self.assertTrue(is_student_email("student@students.uonbi.ac.ke"))
        self.assertTrue(is_student_email("student@students.jkuat.ac.ke"))
        self.assertTrue(is_student_email("student@students.must.ac.ke"))
        self.assertTrue(is_student_email("student@college.edu"))
        self.assertFalse(is_student_email("staff@ku.ac.ke"))
        self.assertFalse(is_student_email("person@company.co.ke"))

    def test_standard_email_receives_one_explanatory_credit_notification(self):
        user, _wallet = self.create_user_and_wallet("standard.notice@gmail.com")

        self.assertTrue(notify_standard_account_credit_limit(user))
        self.assertFalse(notify_standard_account_credit_limit(user))

        notification = user.prep_notifications.get(
            title="Use your student email for the full free allowance"
        )
        self.assertIn("10 trial credits", notification.message)
        self.assertIn("10 free credits every 30 days", notification.message)
        self.assertIn("100-credit trial", notification.message)

    def test_student_email_does_not_receive_the_standard_email_notification(self):
        user, _wallet = self.create_user_and_wallet("notice@students.ku.ac.ke")

        self.assertFalse(notify_standard_account_credit_limit(user))
        self.assertFalse(user.prep_notifications.filter(
            title="Use your student email for the full free allowance"
        ).exists())

    def test_backfill_command_notifies_existing_standard_accounts_once(self):
        standard_user, _wallet = self.create_user_and_wallet("existing.standard@gmail.com")
        student_user, _wallet = self.create_user_and_wallet("existing@students.ku.ac.ke")

        output = StringIO()
        call_command("backfill_standard_email_credit_notices", stdout=output)
        call_command("backfill_standard_email_credit_notices", stdout=output)

        title = "Use your student email for the full free allowance"
        self.assertEqual(standard_user.prep_notifications.filter(title=title).count(), 1)
        self.assertFalse(student_user.prep_notifications.filter(title=title).exists())
        self.assertIn("created", output.getvalue())
