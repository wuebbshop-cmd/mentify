"""accounts/admin.py — Django admin registration for accounts."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, Profile, Guardian, GuardianLinkRequest, GuardianLinkRequestLog


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["email", "first_name", "last_name", "role", "is_active", "is_email_verified", "created_at"]
    list_filter = ["role", "is_active", "is_email_verified", "is_staff"]
    search_fields = ["email", "first_name", "last_name", "username"]
    ordering = ["-created_at"]

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "phone", "avatar_url")}),
        (_("Role & Status"), {"fields": ("role", "is_email_verified")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "first_name", "last_name", "role", "password1", "password2"),
        }),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "county", "school", "class_level"]
    search_fields = ["user__email", "user__first_name", "user__last_name"]
    raw_id_fields = ["user"]


@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ["user", "relationship", "created_at"]
    filter_horizontal = ["learners"]
    raw_id_fields = ["user"]
    search_fields = ["user__email", "user__first_name"]


@admin.register(GuardianLinkRequest)
class GuardianLinkRequestAdmin(admin.ModelAdmin):
    list_display = ["guardian", "learner", "status", "created_at", "responded_at"]
    list_filter = ["status", "created_at"]
    search_fields = ["guardian__email", "learner__email", "guardian__first_name", "learner__first_name"]
    raw_id_fields = ["guardian", "learner"]


@admin.register(GuardianLinkRequestLog)
class GuardianLinkRequestLogAdmin(admin.ModelAdmin):
    list_display = ["request", "event", "actor", "created_at"]
    list_filter = ["event", "created_at"]
    search_fields = ["actor__email", "request__guardian__email", "request__learner__email"]
    raw_id_fields = ["actor", "request"]
