"""
payments/models.py

Subscription: learner <-> cohort, with paid_until for access gating.
Payment: unified record for both Paystack and manual cash payments.
Both methods update paid_until the same way.
"""
from django.db import models
from django.conf import settings
from django.utils import timezone
from dateutil.relativedelta import relativedelta
import os

def table_name(base_name: str) -> str:
    prefix = os.getenv("DB_TABLE_PREFIX", "me_")
    suffix = os.getenv("DB_TABLE_SUFFIX", "_tbl")
    return f"{prefix}{base_name}{suffix}"


class Subscription(models.Model):
    """
    A learner's subscription to a cohort. The paid_until date is the access gate.
    """

    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        PAUSED = "paused", "Paused"
        EXPIRED = "expired", "Expired"
        CANCELLED = "cancelled", "Cancelled"

    learner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="subscriptions",
        limit_choices_to={"role": "learner"},
    )
    cohort = models.ForeignKey(
        "courses.Cohort",
        on_delete=models.CASCADE,
        related_name="subscriptions",
    )
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE, db_index=True)
    paid_until = models.DateField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = table_name("subscriptions")
        unique_together = [("learner", "cohort")]
        ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.learner.get_full_name()} → {self.cohort} (until {self.paid_until})"

    @property
    def is_access_valid(self):
        if not self.paid_until:
            return False
        return self.paid_until >= timezone.now().date()

    def extend_by_one_month(self):
        """
        Extend paid_until by one calendar month.
        If already lapsed, extend from today. Otherwise extend from current paid_until.
        """
        today = timezone.now().date()
        base = max(self.paid_until, today) if self.paid_until else today
        self.paid_until = base + relativedelta(months=1)
        self.status = self.Status.ACTIVE
        self.save()


class Payment(models.Model):
    """
    Unified payment record. Both Paystack and cash write here.
    recorded_by is set for cash payments (the admin who recorded it).
    """

    class Method(models.TextChoices):
        PAYSTACK = "paystack", "Paystack (Card / M-Pesa)"
        CASH = "cash", "Cash (Manual)"

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        SUCCESS = "success", "Success"
        FAILED = "failed", "Failed"

    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name="payments")
    method = models.CharField(max_length=20, choices=Method.choices)
    amount_kes = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=255, unique=True, help_text="Paystack ref or manual note ref")
    paystack_transaction_id = models.CharField(max_length=255, blank=True)
    # Set for cash payments
    recorded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="payments_recorded",
        limit_choices_to={"role__in": ["admin"]},
    )
    note = models.TextField(blank=True, help_text="Cash payment note or any additional info")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING, db_index=True)
    paid_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = table_name("payments")
        ordering = ["-paid_at"]

    def __str__(self):
        return f"[{self.method}] {self.subscription.learner.get_full_name()} - KES {self.amount_kes} ({self.status})"
