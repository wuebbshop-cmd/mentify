from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from accounts.models import User
from prep.models import PrepWallet


class CreditExpiryTests(TestCase):
    def test_dashboard_expires_trial_balance_after_72_hours(self):
        user = User.objects.create_user(
            username="expired-trial",
            email="expired-trial@example.test",
            password="Valid123",
        )
        wallet = PrepWallet.get_or_create_wallet(user)
        expired_at = timezone.now() - timedelta(days=1)
        wallet.plan_expires_at = expired_at
        wallet.save(update_fields=["plan_expires_at"])
        wallet.credit_grants.update(expires_at=expired_at)
        self.client.force_login(user)

        response = self.client.get(reverse("prep:dashboard"))

        self.assertEqual(response.status_code, 200)
        wallet.refresh_from_db()
        self.assertEqual(wallet.credits_balance, 0)
        self.assertEqual(wallet.current_plan, "expired")
        self.assertEqual(response.context["user_credits"], 0)
