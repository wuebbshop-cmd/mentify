"""payments/urls.py"""
from django.urls import path
from . import views

app_name = "payments"

urlpatterns = [
    path("pay/<int:cohort_id>/", views.initiate_payment, name="initiate"),
    path("callback/", views.payment_callback, name="callback"),
    path("webhook/paystack/", views.paystack_webhook, name="paystack_webhook"),
    # Admin
    path("cash/record/", views.record_cash_payment, name="record_cash"),
    path("admin/list/", views.payment_list, name="payment_list"),
    # Learner
    path("history/", views.learner_payment_history, name="learner_history"),
]
