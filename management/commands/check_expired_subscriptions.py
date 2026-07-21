"""
management/commands/check_expired_subscriptions.py

Daily management command to flag/suspend expired subscriptions.
Run via cron at 1:00 AM Nairobi time:
    python manage.py check_expired_subscriptions

Configured in settings.py CRONJOBS for django-crontab.
"""
from django.core.management.base import BaseCommand
from django.utils import timezone

from payments.models import Subscription
from courses.models import Enrollment


class Command(BaseCommand):
    help = "Flag subscriptions where paid_until has passed and update enrollment status."

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Show what would be updated without making changes.",
        )

    def handle(self, *args, **options):
        dry_run = options["dry_run"]
        today = timezone.now().date()

        # Find subscriptions that were active but have now lapsed
        expired_subs = Subscription.objects.filter(
            status=Subscription.Status.ACTIVE,
            paid_until__lt=today,
        ).select_related("learner", "cohort")

        count = expired_subs.count()
        self.stdout.write(f"Found {count} subscription(s) to expire.")

        if dry_run:
            for sub in expired_subs:
                self.stdout.write(
                    f"  [DRY RUN] Would expire: {sub.learner.email} → {sub.cohort} (paid_until={sub.paid_until})"
                )
            return

        expired_ids = list(expired_subs.values_list("id", flat=True))

        # Bulk update subscriptions to expired
        Subscription.objects.filter(id__in=expired_ids).update(status=Subscription.Status.EXPIRED)

        # Also suspend their enrollments
        for sub_id in expired_ids:
            sub = Subscription.objects.get(id=sub_id)
            Enrollment.objects.filter(
                learner=sub.learner,
                cohort=sub.cohort,
                status=Enrollment.Status.ACTIVE,
            ).update(status=Enrollment.Status.EXPIRED)

        self.stdout.write(
            self.style.SUCCESS(f"Expired {count} subscription(s) and suspended their enrollments.")
        )

        # Also re-activate any that were expired but have since been renewed
        renewed_subs = Subscription.objects.filter(
            status=Subscription.Status.EXPIRED,
            paid_until__gte=today,
        ).select_related("learner", "cohort")

        renewed_count = renewed_subs.count()
        if renewed_count:
            renewed_ids = list(renewed_subs.values_list("id", flat=True))
            Subscription.objects.filter(id__in=renewed_ids).update(status=Subscription.Status.ACTIVE)
            for sub_id in renewed_ids:
                sub = Subscription.objects.get(id=sub_id)
                Enrollment.objects.filter(
                    learner=sub.learner,
                    cohort=sub.cohort,
                ).update(status=Enrollment.Status.ACTIVE)
            self.stdout.write(
                self.style.SUCCESS(f"Re-activated {renewed_count} renewed subscription(s).")
            )
