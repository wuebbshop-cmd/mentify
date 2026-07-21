"""payments/admin.py"""
from django.contrib import admin
from .models import Subscription, Payment


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0
    readonly_fields = ["reference", "method", "amount_kes", "status", "paid_at", "recorded_by"]
    show_change_link = True


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["learner", "cohort", "status", "paid_until", "is_access_valid"]
    list_filter = ["status"]
    search_fields = ["learner__email", "learner__first_name", "cohort__name"]
    raw_id_fields = ["learner", "cohort"]
    inlines = [PaymentInline]

    def is_access_valid(self, obj):
        return obj.is_access_valid
    is_access_valid.boolean = True
    is_access_valid.short_description = "Access OK?"


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["get_learner", "get_cohort", "method", "amount_kes", "status", "paid_at", "recorded_by"]
    list_filter = ["method", "status"]
    search_fields = ["reference", "subscription__learner__email", "subscription__cohort__name"]
    readonly_fields = ["reference", "created_at"]
    raw_id_fields = ["subscription", "recorded_by"]

    def get_learner(self, obj):
        return obj.subscription.learner.get_full_name()
    get_learner.short_description = "Learner"

    def get_cohort(self, obj):
        return str(obj.subscription.cohort)
    get_cohort.short_description = "Cohort"
