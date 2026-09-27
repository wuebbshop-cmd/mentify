from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from django.urls import reverse
from django.utils import timezone

from prep.models import PrepNotification, PrepWallet
from services.credit_service import expire_wallet_credits


class Command(BaseCommand):
    help = "Expire dated Prep credit lots and notify users about approaching trial expiry."

    def handle(self, *args, **options):
        now = timezone.now()
        expired_wallets = 0
        reminders = 0

        for wallet in PrepWallet.objects.select_related("user").iterator():
            expired = expire_wallet_credits(wallet)
            wallet.refresh_from_db(fields=["current_plan", "plan_expires_at", "updated_at"])
            if expired:
                expired_wallets += 1

            if wallet.current_plan == "trial" and wallet.plan_expires_at:
                if wallet.plan_expires_at <= now:
                    PrepWallet.objects.filter(pk=wallet.pk, current_plan="trial").update(
                        current_plan="expired",
                        updated_at=now,
                    )
                else:
                    remaining = wallet.plan_expires_at - now
                    reminder_window = "24 hours" if remaining <= timedelta(hours=24) else None
                    if remaining <= timedelta(hours=3):
                        reminder_window = "3 hours"
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
                                    f"Your 30-credit free trial ends in {reminder_window}. "
                                    "Subscribe before the expiry time to continue using Mentify Prep."
                                ),
                                category="general",
                                url=reverse("prep:billing"),
                            )
                            reminders += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Processed Prep wallets. Expired lots for {expired_wallets} wallet(s); "
                f"created {reminders} trial reminder(s)."
            )
        )
