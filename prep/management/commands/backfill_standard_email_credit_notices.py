from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from prep.models import PrepNotification
from services.credit_service import get_free_credit_entitlement


class Command(BaseCommand):
    help = "Create the one-time free-credit allowance notice for existing standard-email accounts."

    def handle(self, *args, **options):
        title = "Use your student email for the full free allowance"
        users = list(get_user_model().objects.all())
        existing_user_ids = set(
            PrepNotification.objects.filter(title=title).values_list("user_id", flat=True)
        )
        pending_users = [
            user
            for user in users
            if not user.is_staff
            and not user.is_superuser
            and not get_free_credit_entitlement(user)["is_student"]
            and user.pk not in existing_user_ids
        ]

        PrepNotification.objects.bulk_create([
            PrepNotification(
                user=user,
                title=title,
                message=(
                    "This account uses a standard email address, so it receives "
                    "10 trial credits and 10 free credits every 30 days. "
                    "Sign in or register with your institution-issued student email "
                    "to receive the full 100-credit trial and 20-credit monthly allowance."
                ),
                category="general",
                url="/prep/billing/",
            )
            for user in pending_users
        ])

        created = len(pending_users)
        already_present = len(users) - created

        self.stdout.write(
            self.style.SUCCESS(
                f"Standard-email credit notices: {created} created, {already_present} skipped."
            )
        )
