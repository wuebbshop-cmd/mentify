"""
payments/views.py

Paystack checkout, callback, webhook + admin cash recording.
"""
import hashlib
import hmac
import json
import uuid
import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from accounts.decorators import role_required
from accounts.models import User, Profile
from courses.models import Cohort, Enrollment
from .models import Payment, Subscription
from services.paystack_service import PaystackService

logger = logging.getLogger(__name__)


# ─── Paystack Checkout ────────────────────────────────────────────────────────

@login_required
@role_required("learner")
def initiate_payment(request, cohort_id):
    """
    Initiate Paystack checkout for a cohort subscription.
    Creates a pending Payment record, then redirects learner to Paystack.
    """
    cohort = get_object_or_404(Cohort, id=cohort_id, status="active")

    # Ensure enrollment exists as PENDING until payment confirms
    enrollment, _ = Enrollment.objects.get_or_create(
        learner=request.user,
        cohort=cohort,
        defaults={"status": "pending"},
    )
    # Don't downgrade an already-active enrollment (re-paying for renewal)
    if enrollment.status not in ("active",):
        enrollment.status = "pending"
        enrollment.save()

    # Get or create subscription
    subscription, _ = Subscription.objects.get_or_create(
        learner=request.user,
        cohort=cohort,
    )

    reference = f"MENTIFY-{uuid.uuid4().hex[:16].upper()}"
    amount_kes = cohort.price_kes
    amount_cents = int(amount_kes * 100)  # Paystack uses smallest currency unit

    ps = PaystackService(
        secret_key=settings.PAYSTACK_SECRET_KEY,
        public_key=settings.PAYSTACK_PUBLIC_KEY,
        currency=settings.PAYSTACK_CURRENCY,
    )

    callback_url = request.build_absolute_uri(f"/payments/callback/?ref={reference}")

    status_code, body = ps.initialize(
        email=request.user.email,
        amount_cents=amount_cents,
        reference=reference,
        callback_url=callback_url,
        metadata={
            "subscription_id": subscription.id,
            "cohort_id": cohort.id,
            "learner_id": request.user.id,
        },
    )

    if status_code != 200 or not body.get("status"):
        error_msg = body.get("message", "Payment initialization failed. Please try again.")
        messages.error(request, error_msg)
        return redirect("courses:cohort_detail", cohort_id=cohort.id)

    # Create pending payment record
    Payment.objects.create(
        subscription=subscription,
        method=Payment.Method.PAYSTACK,
        amount_kes=amount_kes,
        reference=reference,
        status=Payment.Status.PENDING,
    )

    authorization_url = body["data"]["authorization_url"]
    return redirect(authorization_url)


def payment_callback(request):
    """
    Paystack redirects here after payment attempt.
    We verify the transaction via API (not just trusting the redirect).
    """
    reference = request.GET.get("ref") or request.GET.get("reference")
    if not reference:
        messages.error(request, "Invalid payment reference.")
        return redirect("home")

    payment = get_object_or_404(Payment, reference=reference)

    if payment.status == Payment.Status.SUCCESS:
        messages.info(request, "This payment has already been processed.")
        return redirect("accounts:learner_dashboard")

    ps = PaystackService(
        secret_key=settings.PAYSTACK_SECRET_KEY,
        public_key=settings.PAYSTACK_PUBLIC_KEY,
        currency=settings.PAYSTACK_CURRENCY,
    )
    status_code, body = ps.verify(reference)

    if status_code == 200 and body.get("data", {}).get("status") == "success":
        _confirm_payment(payment, body["data"].get("id", ""))
        messages.success(
            request,
            f"Payment successful! Your access to '{payment.subscription.cohort}' has been activated."
        )
        return redirect("accounts:learner_dashboard")
    else:
        payment.status = Payment.Status.FAILED
        payment.save()
        # Revert enrollment to pending if it hasn't been confirmed by another payment
        sub = payment.subscription
        has_successful = sub.payments.filter(status=Payment.Status.SUCCESS).exists()
        if not has_successful:
            Enrollment.objects.filter(
                learner=sub.learner, cohort=sub.cohort
            ).update(status="pending")
        messages.error(request, "Payment could not be verified. Please contact support if you were charged.")
        return redirect("courses:cohort_detail", cohort_id=payment.subscription.cohort_id)


@csrf_exempt
@require_POST
def paystack_webhook(request):
    """
    Paystack webhook handler — the authoritative payment confirmation path.
    Verifies HMAC-SHA512 signature, then extends subscription paid_until.
    """
    signature = request.headers.get("X-Paystack-Signature", "")
    raw_body = request.body

    secret = settings.PAYSTACK_WEBHOOK_SECRET or settings.PAYSTACK_SECRET_KEY
    if not secret:
        logger.error("Paystack webhook: no secret configured.")
        return HttpResponseBadRequest("No webhook secret configured.")

    expected = hmac.new(
        secret.encode("utf-8"),
        raw_body,
        hashlib.sha512,
    ).hexdigest()

    if not hmac.compare_digest(expected, signature):
        logger.warning("Paystack webhook: invalid signature.")
        return HttpResponse(status=401)

    try:
        payload = json.loads(raw_body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON.")

    event = payload.get("event")
    data = payload.get("data", {})

    if event == "charge.success":
        reference = data.get("reference")
        if not reference:
            return HttpResponse("ok")
        try:
            payment = Payment.objects.get(reference=reference)
            if payment.status != Payment.Status.SUCCESS:
                _confirm_payment(payment, str(data.get("id", "")))
                logger.info("Webhook: confirmed payment %s", reference)
        except Payment.DoesNotExist:
            logger.warning("Webhook: payment %s not found.", reference)

    return HttpResponse("ok")


def _confirm_payment(payment: Payment, transaction_id: str):
    """Shared logic: mark payment successful and extend subscription."""
    payment.status = Payment.Status.SUCCESS
    payment.paystack_transaction_id = transaction_id
    payment.paid_at = timezone.now()
    payment.save()

    sub = payment.subscription
    sub.extend_by_one_month()

    # Ensure enrollment is active
    Enrollment.objects.filter(
        learner=sub.learner, cohort=sub.cohort
    ).update(status="active")


# ─── Admin: Manual Cash Payment ───────────────────────────────────────────────

@login_required
@role_required("admin")
def record_cash_payment(request):
    """
    Admin-only: record a cash payment for a learner.
    Supports inline learner account creation if learner doesn't exist.
    """
    from .forms import CashPaymentForm, InlineLearnerCreationForm

    learner_form = InlineLearnerCreationForm()
    payment_form = CashPaymentForm()
    created_learner = None

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "create_learner":
            learner_form = InlineLearnerCreationForm(request.POST)
            if learner_form.is_valid():
                created_learner = learner_form.save()
                messages.success(request, f"Account created for {created_learner.get_full_name()}.")
                # Pre-fill the payment form with this learner
                payment_form = CashPaymentForm(initial={"learner": created_learner.id})

        elif action == "record_payment":
            payment_form = CashPaymentForm(request.POST)
            if payment_form.is_valid():
                learner = payment_form.cleaned_data["learner"]
                cohort = payment_form.cleaned_data["cohort"]
                amount = payment_form.cleaned_data["amount_kes"]
                note = payment_form.cleaned_data.get("note", "")

                # Get or create subscription
                sub, _ = Subscription.objects.get_or_create(
                    learner=learner, cohort=cohort
                )

                # Get or create enrollment
                Enrollment.objects.get_or_create(
                    learner=learner, cohort=cohort,
                    defaults={"status": "active"}
                )

                reference = f"CASH-{uuid.uuid4().hex[:12].upper()}"

                payment = Payment.objects.create(
                    subscription=sub,
                    method=Payment.Method.CASH,
                    amount_kes=amount,
                    reference=reference,
                    recorded_by=request.user,
                    note=note,
                    status=Payment.Status.SUCCESS,
                    paid_at=timezone.now(),
                )

                sub.extend_by_one_month()

                # Ensure enrollment active
                Enrollment.objects.filter(learner=learner, cohort=cohort).update(status="active")

                messages.success(
                    request,
                    f"Cash payment of KES {amount} recorded for {learner.get_full_name()} "
                    f"in '{cohort}'. Access extended until {sub.paid_until}."
                )
                return redirect("accounts:admin_dashboard")

    return render(request, "payments/record_cash.html", {
        "learner_form": learner_form,
        "payment_form": payment_form,
        "created_learner": created_learner,
    })


@login_required
@role_required("admin")
def payment_list(request):
    """Admin: view all payments with filtering."""
    payments = (
        Payment.objects.all()
        .select_related("subscription__learner", "subscription__cohort__course", "recorded_by")
        .order_by("-paid_at")
    )

    method_filter = request.GET.get("method", "")
    if method_filter:
        payments = payments.filter(method=method_filter)

    return render(request, "payments/payment_list.html", {
        "payments": payments,
        "method_filter": method_filter,
    })


@login_required
@role_required("learner")
def learner_payment_history(request):
    """Learner views their own subscription + payment history."""
    subs = (
        Subscription.objects.filter(learner=request.user)
        .select_related("cohort__course")
        .prefetch_related("payments")
        .order_by("-updated_at")
    )
    return render(request, "payments/learner_history.html", {"subscriptions": subs})
