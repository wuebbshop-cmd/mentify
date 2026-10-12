from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from django.urls import reverse
from django.utils import timezone

from prep.models import PrepNotification, PrepWallet
from services.credit_service import expire_wallet_credits, grant_freemium_monthly


class Command(BaseCommand):
    help = "Expire dated Prep credit lots, transition expired trials to Freemium, and refresh Freemium monthly grants."

    def handle(self, *args, **options):
        now = timezone.now()
        expired_wallets = 0
        trials_to_freemium = 0
        freemium_refreshed = 0
        reminders = 0

        for wallet in PrepWallet.objects.select_related("user").iterator():
            expired = expire_wallet_credits(wallet)
            wallet.refresh_from_db(fields=["current_plan", "plan_expires_at", "updated_at"])
            if expired:
                expired_wallets += 1

            # 1. Trial timer expired -> auto-transition to Freemium with 20 fresh credits
            if wallet.current_plan == "trial" and wallet.plan_expires_at and wallet.plan_expires_at <= now:
                grant_freemium_monthly(wallet)
                trials_to_freemium += 1
                wallet.refresh_from_db(fields=["current_plan", "plan_expires_at", "updated_at"])

            # 2. Freemium 30-day cycle expired -> grant next monthly batch of 20 credits
            elif wallet.current_plan == "freemium" and wallet.plan_expires_at and wallet.plan_expires_at <= now:
                grant_freemium_monthly(wallet)
                freemium_refreshed += 1
                wallet.refresh_from_db(fields=["current_plan", "plan_expires_at", "updated_at"])

            # 3. Active trial reminders
            elif wallet.current_plan == "trial" and wallet.plan_expires_at and wallet.plan_expires_at > now:
                remaining = wallet.plan_expires_at - now
                reminder_window = None
                if remaining <= timedelta(hours=3):
                    reminder_window = "3 hours"
                elif remaining <= timedelta(hours=24):
                    reminder_window = "24 hours"
                elif remaining <= timedelta(days=2) and remaining > timedelta(hours=47):
                    reminder_window = "2 days"

                if reminder_window:
                    title = f"Free trial ends in {reminder_window}"
                    exists = PrepNotification.objects.filter(
                        user=wallet.user,
                        title=title,
                        created_at__gte=now - timedelta(hours=20),
                    ).exists()
                    if not exists:
                        PrepNotification.objects.create(
                            user=wallet.user,
                            title=title,
                            message=(
                                f"Your 100-credit free trial ends in {reminder_window}. "
                                "After your trial, you will automatically move to our Free Plan (20 credits/mo), "
                                "or subscribe to Basic/Plus/Pro for full access."
                            ),
                            category="general",
                            url=reverse("prep:billing"),
                        )
                        reminders += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Processed Prep wallets: {expired_wallets} with expired lots; "
                f"{trials_to_freemium} trial(s) moved to Freemium; "
                f"{freemium_refreshed} Freemium cycle(s) refreshed; "
                f"{reminders} trial reminder(s) created."
            )
        )
