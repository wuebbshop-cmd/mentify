"""
sessions/models.py

LiveSession — manually-entered meeting link, no Zoom API.
Attendance — manually marked by tutor after session.
MakeupSession — reuses LiveSession model with is_makeup=True + original_session FK.
"""
from django.db import models
from django.conf import settings
import os

def table_name(base_name: str) -> str:
    prefix = os.getenv("DB_TABLE_PREFIX", "me_")
    suffix = os.getenv("DB_TABLE_SUFFIX", "_tbl")
    return f"{prefix}{base_name}{suffix}"


class LiveSession(models.Model):
    cohort = models.ForeignKey(
        "courses.Cohort",
        on_delete=models.CASCADE,
        related_name="live_sessions",
    )
    title = models.CharField(max_length=255, help_text="e.g. 'Week 3: Functions in Python'")
    scheduled_at = models.DateTimeField(db_index=True)
    duration_minutes = models.PositiveIntegerField(default=120, help_text="Expected session duration")
    meeting_link = models.URLField(max_length=512, help_text="Paste Google Meet / Zoom link here")
    notes = models.TextField(blank=True, help_text="Any notes for learners before the session")
    is_makeup = models.BooleanField(
        default=False,
        help_text="True if this is a makeup session for a missed live session"
    )
    original_session = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="makeups",
        help_text="The original session this makeup replaces"
    )
    is_cancelled = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="sessions_created",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = table_name("live_sessions")
        app_label = "live_sessions"
        ordering = ["-scheduled_at"]

    def __str__(self):
        makeup_tag = " [MAKEUP]" if self.is_makeup else ""
        return f"{self.cohort.name} — {self.title}{makeup_tag} @ {self.scheduled_at.strftime('%d %b %Y %H:%M')}"

    @property
    def is_upcoming(self):
        from django.utils import timezone
        return self.scheduled_at > timezone.now() and not self.is_cancelled


class Attendance(models.Model):
    class AttendanceStatus(models.TextChoices):
        ATTENDED = "attended", "Attended"
        MISSED = "missed", "Missed"
        EXCUSED = "excused", "Excused"

    session = models.ForeignKey(LiveSession, on_delete=models.CASCADE, related_name="attendances")
    learner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="attendance_records",
        limit_choices_to={"role": "learner"},
    )
    status = models.CharField(
        max_length=20,
        choices=AttendanceStatus.choices,
        default=AttendanceStatus.MISSED,
    )
    marked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="attendance_marked",
    )
    marked_at = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = table_name("attendances")
        app_label = "live_sessions"
        unique_together = [("session", "learner")]

    def __str__(self):
        return f"{self.learner.get_full_name()} — {self.session.title} [{self.status}]"
