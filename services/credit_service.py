"""Atomic credit grants, expiry, and usage-based deductions for Mentify Prep."""

from __future__ import annotations

import math
import re
from datetime import timedelta

from django.conf import settings
from django.db import transaction
from django.utils import timezone


TRIAL_CREDITS = 30
TRIAL_DURATION = timedelta(hours=72)
PURCHASED_CREDIT_DURATION = timedelta(days=30)

# These are the server-side counterparts of the limits shown on the billing
# page. Credits pay for model use; these caps bound plan volume independently.
SUBSCRIPTION_USAGE_LIMITS = {
    "basic": {"document_uploads": 10, "scanned_uploads": 5, "practice_questions": 100},
    "plus": {"document_uploads": 20, "scanned_uploads": 15, "practice_questions": 200},
    "pro": {"document_uploads": 40, "scanned_uploads": 30, "practice_questions": 350},
}


class CreditError(Exception):
    """Base error for credit operations."""


class InsufficientCredits(CreditError):
    """Raised when a wallet cannot cover an operation."""


class PlanLimitExceeded(CreditError):
    """Raised when an active subscription has reached an advertised usage cap."""


def _sync_balance_locked(wallet):
    from prep.models import PrepCreditGrant
    from django.db.models import Q

    total = (
        PrepCreditGrant.objects.filter(wallet=wallet, remaining_credits__gt=0)
        .filter(Q(expires_at__isnull=True) | Q(expires_at__gt=timezone.now()))
    )
    balance = sum(grant.remaining_credits for grant in total)
    if wallet.credits_balance != balance:
        wallet.credits_balance = balance
        wallet.save(update_fields=["credits_balance", "updated_at"])
    return balance


def _expire_locked(wallet, now=None):
    """Expire dated lots while the wallet row is locked."""
    from prep.models import PrepTransaction
    from django.db.models import Q

    now = now or timezone.now()
    expiry_filter = Q(expires_at__isnull=False, expires_at__lte=now)
    if wallet.current_plan == "trial" and wallet.plan_expires_at and wallet.plan_expires_at <= now:
        expiry_filter |= Q(source="trial")
    expired = list(wallet.credit_grants.select_for_update().filter(remaining_credits__gt=0).filter(expiry_filter))
    for grant in expired:
        amount = grant.remaining_credits
        grant.remaining_credits = 0
        grant.save(update_fields=["remaining_credits"])
        PrepTransaction.objects.create(
            wallet=wallet,
            credit_grant=grant,
            amount=-amount,
            action_type="credit_expiry",
            description=f"Expired {grant.source} credits",
            reference_code=grant.reference_code,
        )

    if expired:
        _sync_balance_locked(wallet)
    return len(expired)


def _ensure_grant_locked(wallet, now=None):
    """Backfill one lot for old wallets created before credit lots existed."""
    from prep.models import PrepCreditGrant, PrepTransaction

    if wallet.credit_grants.exists():
        return

    now = now or timezone.now()
    legacy_balance = int(wallet.credits_balance or 0)
    if legacy_balance <= 0:
        return

    source = "trial" if wallet.current_plan == "trial" else "legacy"
    grant = PrepCreditGrant.objects.create(
        wallet=wallet,
        source=source,
        granted_credits=legacy_balance,
        remaining_credits=legacy_balance,
        granted_at=wallet.created_at or now,
        expires_at=wallet.plan_expires_at if source == "trial" else None,
    )
    if not wallet.transactions.filter(action_type="trial_grant").exists() and source == "trial":
        PrepTransaction.objects.create(
            wallet=wallet,
            credit_grant=grant,
            amount=legacy_balance,
            action_type="trial_grant",
            description="Welcome Grant: 3-Day Free Trial (30 Credits)",
        )


def ensure_wallet_credit_state(wallet, initialize_trial: bool = False):
    """Initialize new wallets and backfill old aggregate-only wallets safely."""
    from prep.models import PrepCreditGrant, PrepNotification, PrepTransaction

    with transaction.atomic():
        locked = wallet.__class__.objects.select_for_update().get(pk=wallet.pk)
        now = timezone.now()
        _ensure_grant_locked(locked, now)
        if initialize_trial and not locked.credit_grants.exists() and locked.current_plan == "trial":
            expires_at = locked.plan_expires_at or (now + TRIAL_DURATION)
            grant = PrepCreditGrant.objects.create(
                wallet=locked,
                source="trial",
                granted_credits=TRIAL_CREDITS,
                remaining_credits=TRIAL_CREDITS,
                granted_at=now,
                expires_at=expires_at,
            )
            PrepTransaction.objects.create(
                wallet=locked,
                credit_grant=grant,
                amount=TRIAL_CREDITS,
                action_type="trial_grant",
                description="Welcome Grant: 3-Day Free Trial (30 Credits)",
            )
            PrepNotification.objects.create(
                user=locked.user,
                title="Your 3-day free trial has started",
                message=(
                    "You received 30 free credits. They expire exactly 72 hours after account creation. "
                    "Subscribe before the expiry time to continue using Mentify Prep."
                ),
                category="general",
                url="/prep/billing/",
            )
        _expire_locked(locked, now)
        if locked.plan_expires_at and locked.plan_expires_at <= now:
            if locked.current_plan in {"trial", "basic", "plus", "pro"}:
                locked.current_plan = "expired"
                locked.save(update_fields=["current_plan", "updated_at"])
        _sync_balance_locked(locked)


def grant_credits(
    wallet,
    amount: int,
    source: str,
    expires_at=None,
    action_type="monthly_grant",
    description="Credit grant",
    reference_code="",
):
    """Create a dated credit lot and update the compatibility balance."""
    from prep.models import PrepCreditGrant, PrepTransaction

    amount = int(amount)
    if amount <= 0:
        raise ValueError("Credit grant amount must be positive")

    with transaction.atomic():
        locked = wallet.__class__.objects.select_for_update().get(pk=wallet.pk)
        _expire_locked(locked)
        now = timezone.now()
        grant = PrepCreditGrant.objects.create(
            wallet=locked,
            source=source,
            granted_credits=amount,
            remaining_credits=amount,
            granted_at=now,
            expires_at=expires_at,
            reference_code=reference_code or "",
        )
        locked.credits_balance = _sync_balance_locked(locked)
        locked.save(update_fields=["credits_balance", "updated_at"])
        PrepTransaction.objects.create(
            wallet=locked,
            credit_grant=grant,
            amount=amount,
            action_type=action_type,
            reference_code=reference_code or "",
            description=description,
        )
        return grant


def expire_wallet_credits(wallet):
    with transaction.atomic():
        locked = wallet.__class__.objects.select_for_update().get(pk=wallet.pk)
        now = timezone.now()
        count = _expire_locked(locked, now)
        if locked.plan_expires_at and locked.plan_expires_at <= now:
            if locked.current_plan in {"trial", "basic", "plus", "pro"}:
                locked.current_plan = "expired"
                locked.save(update_fields=["current_plan", "updated_at"])
        _sync_balance_locked(locked)
        return count


def get_available_credits(wallet):
    ensure_wallet_credit_state(wallet)
    wallet.refresh_from_db(fields=["credits_balance", "current_plan", "plan_expires_at", "updated_at"])
    from prep.models import PrepCreditReservation

    held = sum(
        PrepCreditReservation.objects.filter(
            wallet=wallet,
            status="reserved",
        ).values_list("remaining_reserved_credits", flat=True)
    )
    return max(0, wallet.credits_balance - held)


def has_active_subscription(wallet, now=None):
    now = now or timezone.now()
    return wallet.current_plan in {"basic", "plus", "pro"} and bool(wallet.plan_expires_at and wallet.plan_expires_at > now)


def subscription_usage(wallet) -> dict:
    """Return current-plan usage derived from the immutable credit ledger."""
    from prep.models import PrepTransaction

    limits = SUBSCRIPTION_USAGE_LIMITS.get(wallet.current_plan)
    if not limits or not has_active_subscription(wallet):
        return {}

    # Every subscription allocation lasts 30 days and plan replacement creates
    # a new allocation, so this window is the current plan cycle only.
    cycle_start = wallet.plan_expires_at - timedelta(days=30)
    transactions = PrepTransaction.objects.filter(wallet=wallet, created_at__gte=cycle_start)
    practice_questions = 0
    for entry in transactions.filter(action_type="ai_practice_gen").only("amount", "description", "metadata"):
        metadata = entry.metadata if isinstance(entry.metadata, dict) else {}
        count = metadata.get("question_count")
        if isinstance(count, int) and count > 0:
            practice_questions += count
            continue
        # Preserve accurate counting for transactions created before the
        # question_count metadata field was introduced.
        match = re.search(r"Generated\s+(\d+)\s+Practice Questions", entry.description or "", re.IGNORECASE)
        if match:
            practice_questions += int(match.group(1))

    return {
        "document_uploads": transactions.filter(action_type="upload_text").count(),
        "scanned_uploads": transactions.filter(action_type="upload_ocr").count(),
        "practice_questions": practice_questions,
    }


def enforce_subscription_limit(wallet, limit_name: str, requested: int = 1) -> dict:
    """Reject paid-plan work that would exceed its published per-cycle cap."""
    requested = max(0, int(requested))
    limits = SUBSCRIPTION_USAGE_LIMITS.get(wallet.current_plan)
    if not limits or not has_active_subscription(wallet):
        # Trial access is governed by its dated 30-credit grant. Expired plans
        # have no active tier whose monthly quota can be applied.
        return {}
    if limit_name not in limits:
        raise ValueError(f"Unknown subscription limit: {limit_name}")

    usage = subscription_usage(wallet)
    used = usage.get(limit_name, 0)
    limit = limits[limit_name]
    if used + requested > limit:
        label = limit_name.replace("_", " ")
        raise PlanLimitExceeded(
            f"Your {wallet.current_plan.title()} plan includes {limit} {label} per 30-day plan period. "
            f"You have used {used}; this request needs {requested} more."
        )
    return {"used": used, "limit": limit, "remaining": limit - used}


def grant_subscription(wallet, plan_id: str, amount: int, reference_code: str = ""):
    """
    Assign new subscription plan and credit allocation.
    When a student upgrades (e.g. basic -> pro) or switches tiers, existing credit lots
    from prior subscriptions remain intact and each expires at its originally scheduled date,
    while the active plan tier and badge update immediately to the latest subscription.
    """
    if plan_id not in {"basic", "plus", "pro"}:
        raise ValueError("Invalid subscription plan")
    with transaction.atomic():
        locked = wallet.__class__.objects.select_for_update().get(pk=wallet.pk)
        now = timezone.now()
        _expire_locked(locked, now)
        # Previous subscription credit grants are preserved with their original
        # expiration dates so that the user does not lose unused credits upon upgrade.
        # FIFO consumption will naturally draw from earlier-expiring lots first.
        locked.current_plan = plan_id
        locked.plan_expires_at = now + timedelta(days=30)
        locked.save(update_fields=["current_plan", "plan_expires_at", "updated_at"])
        return grant_credits(
            locked,
            amount,
            source="subscription",
            expires_at=locked.plan_expires_at,
            action_type="monthly_grant",
            description=f"{plan_id.title()} subscription allocation (30 days)",
            reference_code=reference_code,
        )


def grant_purchased_topup(wallet, amount: int, reference_code: str, description: str):
    wallet.refresh_from_db(fields=["current_plan", "plan_expires_at", "updated_at"])
    if not has_active_subscription(wallet):
        raise CreditError("An active subscription is required to purchase credit top-ups.")
    return grant_credits(
        wallet,
        amount,
        source="purchased",
        expires_at=timezone.now() + PURCHASED_CREDIT_DURATION,
        action_type="topup_purchase",
        description=f"{description} (valid for 30 days)",
        reference_code=reference_code,
    )


def consume_credits(wallet, amount: int, action_type: str, description: str, usage=None, model_name="", metadata=None):
    """Consume credits atomically, preferring expiring trial/subscription lots before top-ups."""
    from prep.models import PrepTransaction

    amount = int(amount)
    if amount <= 0:
        return 0

    with transaction.atomic():
        locked = wallet.__class__.objects.select_for_update().get(pk=wallet.pk)
        _ensure_grant_locked(locked)
        _expire_locked(locked)
        now = timezone.now()
        grants = list(
            locked.credit_grants.select_for_update().filter(remaining_credits__gt=0)
        )
        priority = {"trial": 0, "subscription": 1, "purchased": 2, "admin": 3, "legacy": 4}
        grants.sort(key=lambda grant: (priority.get(grant.source, 9), grant.expires_at or now + timedelta(days=36500), grant.created_at))
        from prep.models import PrepCreditReservation

        reserved = sum(
            PrepCreditReservation.objects.filter(
                wallet=locked,
                status="reserved",
            ).values_list("remaining_reserved_credits", flat=True)
        )
        if sum(grant.remaining_credits for grant in grants) - reserved < amount:
            _sync_balance_locked(locked)
            raise InsufficientCredits(f"Insufficient credits. Required: {amount}.")

        remaining = amount
        usage = usage or {}
        input_tokens = int(usage.get("prompt_tokens") or usage.get("input_tokens") or 0)
        output_tokens = int(usage.get("completion_tokens") or usage.get("output_tokens") or 0)
        total_tokens = int(usage.get("total_tokens") or input_tokens + output_tokens)
        metadata = metadata or {}
        for grant in grants:
            if remaining <= 0:
                break
            used = min(grant.remaining_credits, remaining)
            grant.remaining_credits -= used
            grant.save(update_fields=["remaining_credits"])
            PrepTransaction.objects.create(
                wallet=locked,
                credit_grant=grant,
                amount=-used,
                action_type=action_type,
                description=description,
                model_name=model_name or "",
                input_tokens=input_tokens or None,
                output_tokens=output_tokens or None,
                total_tokens=total_tokens or None,
                metadata={**metadata, "credit_source": grant.source},
            )
            remaining -= used

        _sync_balance_locked(locked)
        return amount


def reserve_credits(wallet, amount: int, *, purpose: str, metadata=None):
    """Atomically hold spendable credits without debiting them during provider latency."""
    from prep.models import PrepCreditReservation

    amount = max(0, int(amount))
    if amount <= 0:
        raise ValueError("Credit reservation must be positive.")

    ensure_wallet_credit_state(wallet)
    with transaction.atomic():
        locked = wallet.__class__.objects.select_for_update().get(pk=wallet.pk)
        _ensure_grant_locked(locked)
        _expire_locked(locked)
        balance = _sync_balance_locked(locked)
        held = sum(
            PrepCreditReservation.objects.filter(
                wallet=locked,
                status="reserved",
            ).values_list("remaining_reserved_credits", flat=True)
        )
        available = max(0, balance - held)
        if available < amount:
            raise InsufficientCredits(
                f"Insufficient credits. Required reservation: {amount}; available: {available}."
            )
        return PrepCreditReservation.objects.create(
            wallet=locked,
            purpose=str(purpose)[:50],
            reserved_credits=amount,
            remaining_reserved_credits=amount,
            metadata=metadata or {},
        )


def settle_credit_reservation(
    reservation,
    amount: int,
    *,
    release_reserved: int | None = None,
    action_type: str,
    description: str,
    usage=None,
    model_name: str = "",
    metadata=None,
):
    """Settle one completed provider stage while retaining any later-stage hold."""
    from prep.models import PrepCreditReservation

    amount = max(0, int(amount))
    with transaction.atomic():
        locked = reservation.wallet.__class__.objects.select_for_update().get(
            pk=reservation.wallet_id
        )
        held = PrepCreditReservation.objects.select_for_update().get(pk=reservation.pk)
        if held.status != "reserved":
            if amount == 0 and held.status in {"settled", "released"}:
                return 0
            raise ValueError("Credit reservation is no longer active.")

        release_amount = (
            held.remaining_reserved_credits
            if release_reserved is None
            else max(0, int(release_reserved))
        )
        if release_amount > held.remaining_reserved_credits:
            raise ValueError("Cannot release more credits than the active reservation.")

        held.remaining_reserved_credits -= release_amount
        held.charged_credits += amount
        if held.remaining_reserved_credits == 0:
            held.status = "settled"
        held.metadata = {
            **(held.metadata if isinstance(held.metadata, dict) else {}),
            **(metadata or {}),
        }
        held.save(update_fields=[
            "remaining_reserved_credits",
            "charged_credits",
            "status",
            "metadata",
            "updated_at",
        ])

        charged = consume_credits(
            locked,
            amount,
            action_type=action_type,
            description=description,
            usage=usage,
            model_name=model_name,
            metadata={
                **(metadata or {}),
                "credit_reservation_id": held.pk,
                "reserved_credits": held.reserved_credits,
            },
        ) if amount else 0
        return charged


def release_credit_reservation(reservation, *, reason: str = "") -> int:
    """Release unused held credits after a request finishes or fails."""
    from prep.models import PrepCreditReservation

    with transaction.atomic():
        reservation.wallet.__class__.objects.select_for_update().get(
            pk=reservation.wallet_id
        )
        held = PrepCreditReservation.objects.select_for_update().get(pk=reservation.pk)
        if held.status != "reserved":
            return 0
        released = held.remaining_reserved_credits
        held.remaining_reserved_credits = 0
        held.status = "released" if held.charged_credits == 0 else "settled"
        if reason:
            held.metadata = {
                **(held.metadata if isinstance(held.metadata, dict) else {}),
                "release_reason": str(reason)[:500],
            }
        held.save(update_fields=[
            "remaining_reserved_credits",
            "status",
            "metadata",
            "updated_at",
        ])
        return released


def credits_for_usage(usage, minimum: int = 1) -> int:
    """Convert provider usage into internal credits with a predictable minimum."""
    usage = usage or {}
    total = int(usage.get("total_tokens") or 0)
    if not total:
        total = int(usage.get("prompt_tokens") or usage.get("input_tokens") or 0)
        total += int(usage.get("completion_tokens") or usage.get("output_tokens") or 0)
    unit = max(1, int(getattr(settings, "PREP_CREDIT_TOKEN_UNIT", 1000)))
    return max(int(minimum), math.ceil(total / unit)) if total else int(minimum)


def estimated_generation_credits(minimum: int = 1) -> int:
    """Minimum balance required before an uncached model generation starts."""
    output_cap = max(
        int(getattr(settings, "MAX_TOKENS_EXPLANATION", 8000)),
        int(getattr(settings, "MAX_TOKENS_REASONING", 8000)),
    )
    prompt_buffer = int(getattr(settings, "PREP_CREDIT_PROMPT_BUFFER", 2000))
    return credits_for_usage({"total_tokens": output_cap + prompt_buffer}, minimum=minimum)
