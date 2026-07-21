"""
courses/models.py

Course → Cohort → Enrollment hierarchy.
Course = subject template. Cohort = one running instance with a tutor and schedule.
Enrollment = learner signed up for a cohort.
"""
from django.db import models
from django.utils.text import slugify
from django.conf import settings
import os

def table_name(base_name: str) -> str:
    prefix = os.getenv("DB_TABLE_PREFIX", "me_")
    suffix = os.getenv("DB_TABLE_SUFFIX", "_tbl")
    return f"{prefix}{base_name}{suffix}"


class Course(models.Model):
    """
    A Course is a subject/template (e.g. "Intro to Python", "JSS1 Mathematics").
    Multiple cohorts can run from the same Course.
    """

    class Track(models.TextChoices):
        TECH = "tech", "Tech (Programming / ML / AI)"
        CBC = "cbc", "CBC Academic (Math, Science, etc.)"
        SPECIALIST = "specialist", "Specialist (Robotics, Cybersecurity, etc.)"

    class Level(models.TextChoices):
        JSS1 = "JSS1", "Junior Secondary School 1"
        JSS2 = "JSS2", "Junior Secondary School 2"
        JSS3 = "JSS3", "Junior Secondary School 3"
        FORM1 = "Form1", "Form 1"
        FORM2 = "Form2", "Form 2"
        FORM3 = "Form3", "Form 3"
        FORM4 = "Form4", "Form 4"
        OPEN = "open", "Open / All Levels"

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    track = models.CharField(max_length=20, choices=Track.choices, default=Track.TECH, db_index=True)
    subject_area = models.CharField(max_length=100, blank=True, help_text="e.g. Mathematics, Python, Robotics")
    level = models.CharField(max_length=20, choices=Level.choices, default=Level.OPEN)
    cover_image_url = models.CharField(max_length=512, blank=True, help_text="GitHub-hosted or CDN URL")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="courses_created",
        limit_choices_to={"role__in": ["admin", "tutor"]},
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = table_name("courses")
        ordering = ["track", "title"]

    def __str__(self):
        return f"{self.title} [{self.get_track_display()}]"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Cohort(models.Model):
    """
    A Cohort is one running instance of a Course — specific tutor, dates, price.
    """

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        ACTIVE = "active", "Active"
        COMPLETED = "completed", "Completed"
        ARCHIVED = "archived", "Archived"

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="cohorts")
    tutor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="cohorts_teaching",
        limit_choices_to={"role__in": ["admin", "tutor"]},
    )
    name = models.CharField(max_length=255, help_text="e.g. 'Batch 1 – Jan 2026' or 'Term 2 2026'")
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    schedule_description = models.CharField(
        max_length=255,
        blank=True,
        help_text="Human-readable schedule e.g. 'Saturdays 10am–12pm'",
    )
    capacity = models.PositiveIntegerField(default=30)
    price_kes = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        help_text="Monthly subscription price in KES"
    )
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = table_name("cohorts")
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.course.title} — {self.name}"

    @property
    def enrolled_count(self):
        return self.enrollments.filter(status="active").count()

    @property
    def is_full(self):
        return self.enrolled_count >= self.capacity


class Enrollment(models.Model):
    """
    Many-to-many join between a Learner and a Cohort, with status tracking.
    """

    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        PAUSED = "paused", "Paused"
        COMPLETED = "completed", "Completed"
        EXPIRED = "expired", "Expired (subscription lapsed)"
        CANCELLED = "cancelled", "Cancelled"

    learner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="enrollments",
        limit_choices_to={"role": "learner"},
    )
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name="enrollments")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE, db_index=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, help_text="Admin notes on this enrollment")

    class Meta:
        db_table = table_name("enrollments")
        unique_together = [("learner", "cohort")]
        ordering = ["-enrolled_at"]

    def __str__(self):
        return f"{self.learner.get_full_name()} → {self.cohort}"
