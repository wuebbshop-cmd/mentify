"""
accounts/models.py

Custom User model + Profile + Guardian.
All roles live on the User model itself for simple FK lookups.
Profile holds extended info. Guardian links parents to learners.
"""
import os
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

def table_name(base_name: str) -> str:
    prefix = os.getenv("DB_TABLE_PREFIX", "me_")
    suffix = os.getenv("DB_TABLE_SUFFIX", "_tbl")
    return f"{prefix}{base_name}{suffix}"



class User(AbstractUser):
    """
    Central user model. role field drives access control throughout the platform.
    """

    class Role(models.TextChoices):
        ADMIN = "admin", _("Admin")
        TUTOR = "tutor", _("Tutor")
        LEARNER = "learner", _("Learner")
        GUARDIAN = "guardian", _("Guardian")

    # Override email to be required and unique
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.LEARNER,
        db_index=True,
    )
    phone = models.CharField(max_length=20, blank=True, help_text="E.164 format, e.g. +254700000000")
    avatar_url = models.CharField(max_length=512, blank=True, help_text="GitHub-hosted or Bunny CDN URL")
    is_email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Make email the login field instead of username
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        db_table = table_name("users")
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.get_full_name()} ({self.email}) [{self.role}]"

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN or self.is_superuser

    @property
    def is_tutor(self):
        return self.role == self.Role.TUTOR

    @property
    def is_learner(self):
        return self.role == self.Role.LEARNER

    @property
    def is_guardian(self):
        return self.role == self.Role.GUARDIAN

    def get_dashboard_url(self):
        """Return the appropriate dashboard URL for this user's role."""
        from django.urls import reverse
        role_urls = {
            self.Role.ADMIN: "accounts:admin_dashboard",
            self.Role.TUTOR: "accounts:tutor_dashboard",
            self.Role.LEARNER: "accounts:learner_dashboard",
            self.Role.GUARDIAN: "accounts:guardian_dashboard",
        }
        url_name = role_urls.get(self.role, "accounts:learner_dashboard")
        return reverse(url_name)


class Profile(models.Model):
    """
    Extended profile info. Kept separate so User model stays lean.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    headline = models.CharField(max_length=160, blank=True)
    specialty = models.CharField(max_length=160, blank=True)
    bio = models.TextField(blank=True)
    experience_summary = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    county = models.CharField(max_length=100, blank=True, help_text="County, state, or region")
    school = models.CharField(max_length=255, blank=True)
    # For learners - school or experience level.
    class_level = models.CharField(
        max_length=20,
        blank=True,
        help_text="e.g. Primary, JSS, Senior School, Past Senior School, Adult Learner"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = table_name("profiles")

    def __str__(self):
        return f"Profile: {self.user.get_full_name()}"


class Guardian(models.Model):
    """
    Links a guardian (parent) user to one or more learner users.
    """
    class Relationship(models.TextChoices):
        PARENT = "parent", _("Parent")
        GUARDIAN = "guardian", _("Guardian")
        SIBLING = "sibling", _("Sibling")
        OTHER = "other", _("Other")

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="guardian_profile",
        limit_choices_to={"role": User.Role.GUARDIAN},
    )
    learners = models.ManyToManyField(
        User,
        related_name="guardians",
        limit_choices_to={"role": User.Role.LEARNER},
        blank=True,
    )
    relationship = models.CharField(
        max_length=20,
        choices=Relationship.choices,
        default=Relationship.PARENT,
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = table_name("guardians")

    def __str__(self):
        return f"Guardian: {self.user.get_full_name()}"


class GuardianLinkRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", _("Pending")
        ACCEPTED = "accepted", _("Accepted")
        REJECTED = "rejected", _("Rejected")
        CANCELLED = "cancelled", _("Cancelled")

    guardian = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="guardian_link_requests",
        limit_choices_to={"role": User.Role.GUARDIAN},
    )
    learner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="guardian_requests",
        limit_choices_to={"role": User.Role.LEARNER},
    )
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = table_name("guardian_link_requests")
        ordering = ["-created_at"]
        unique_together = [["guardian", "learner"]]

    def __str__(self):
        return f"Link request from {self.guardian.get_full_name()} to {self.learner.get_full_name()} ({self.status})"


class GuardianLinkRequestLog(models.Model):
    class Event(models.TextChoices):
        REQUESTED = "requested", _("Requested")
        ACCEPTED = "accepted", _("Accepted")
        REJECTED = "rejected", _("Rejected")
        CANCELLED = "cancelled", _("Cancelled")

    request = models.ForeignKey(
        GuardianLinkRequest,
        on_delete=models.CASCADE,
        related_name="logs",
    )
    event = models.CharField(max_length=20, choices=Event.choices)
    actor = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = table_name("guardian_link_request_logs")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.get_event_display()} for {self.request}"
