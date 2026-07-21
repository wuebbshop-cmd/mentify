"""
assignments/models.py

Rubric-based grading system.
Assignment → RubricCriterion → Submission → Grade → CriterionScore
"""
from django.db import models
from django.conf import settings
import os

def table_name(base_name: str) -> str:
    prefix = os.getenv("DB_TABLE_PREFIX", "me_")
    suffix = os.getenv("DB_TABLE_SUFFIX", "_tbl")
    return f"{prefix}{base_name}{suffix}"


class Assignment(models.Model):
    lesson = models.ForeignKey(
        "content.Lesson",
        on_delete=models.CASCADE,
        related_name="assignments",
    )
    title = models.CharField(max_length=255)
    description = models.TextField(help_text="Assignment brief - what learners need to do")
    due_date = models.DateField(null=True, blank=True)
    github_stored_path = models.CharField(
        max_length=512, blank=True,
        help_text="Optional PDF brief stored on GitHub"
    )
    max_score = models.PositiveIntegerField(default=100)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = table_name("assignments")
        ordering = ["lesson", "due_date"]

    def __str__(self):
        return f"{self.title} - {self.lesson.title}"

    def total_rubric_weight(self):
        return sum(c.weight for c in self.criteria.all())


class RubricCriterion(models.Model):
    """One scoring dimension for an assignment rubric."""
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="criteria")
    label = models.CharField(max_length=255, help_text="e.g. 'Code correctness', 'Presentation'")
    weight = models.PositiveIntegerField(help_text="Weight in points (criteria weights should sum to max_score)")
    description = models.TextField(blank=True, help_text="What does full marks look like?")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = table_name("rubric_criteria")
        ordering = ["assignment", "order"]

    def __str__(self):
        return f"{self.label} ({self.weight}pts) - {self.assignment.title}"


class Submission(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        SUBMITTED = "submitted", "Submitted"
        GRADED = "graded", "Graded"

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    learner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="submissions",
        limit_choices_to={"role": "learner"},
    )
    github_stored_path = models.CharField(
        max_length=512, blank=True,
        help_text="Submitted file stored on GitHub"
    )
    text_response = models.TextField(blank=True, help_text="Typed/pasted response")
    submitted_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = table_name("submissions")
        unique_together = [("assignment", "learner")]
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.learner.get_full_name()} → {self.assignment.title} ({self.status})"


class Grade(models.Model):
    """Overall grade for a Submission."""
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE, related_name="grade")
    graded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="grades_given",
    )
    total_score = models.DecimalField(max_digits=6, decimal_places=2)
    tutor_comment = models.TextField(blank=True)
    graded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = table_name("grades")

    def __str__(self):
        return f"Grade: {self.total_score}/{self.submission.assignment.max_score} - {self.submission}"

    @property
    def percentage(self):
        if self.submission.assignment.max_score:
            return round((float(self.total_score) / self.submission.assignment.max_score) * 100, 1)
        return 0


class CriterionScore(models.Model):
    """Per-criterion score within a Grade."""
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="criterion_scores")
    criterion = models.ForeignKey(RubricCriterion, on_delete=models.CASCADE, related_name="scores")
    score = models.DecimalField(max_digits=6, decimal_places=2)
    comment = models.TextField(blank=True)

    class Meta:
        db_table = table_name("criterion_scores")
        unique_together = [("grade", "criterion")]

    def __str__(self):
        return f"{self.criterion.label}: {self.score}/{self.criterion.weight}"
