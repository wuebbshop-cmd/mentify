"""
content/models.py

Lesson → VideoAsset (Bunny Stream) + Resource (PDF/link via GitHub)
"""
from django.db import models
from django.conf import settings
import os

def table_name(base_name: str) -> str:
    prefix = os.getenv("DB_TABLE_PREFIX", "me_")
    suffix = os.getenv("DB_TABLE_SUFFIX", "_tbl")
    return f"{prefix}{base_name}{suffix}"


class Lesson(models.Model):
    """A lesson belongs to a Cohort. Has an order for sequencing."""
    cohort = models.ForeignKey(
        "courses.Cohort",
        on_delete=models.CASCADE,
        related_name="lessons",
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order within the cohort")
    is_published = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="lessons_created",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = table_name("lessons")
        ordering = ["cohort", "order"]
        unique_together = [("cohort", "order")]

    def __str__(self):
        return f"[{self.cohort}] Lesson {self.order}: {self.title}"


class VideoAsset(models.Model):
    """
    Bunny Stream video linked to a Lesson.
    We only store the Bunny video ID - never serve raw video from Django.
    The embed/player URL is constructed from the library ID + video ID.
    """
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name="video")
    bunny_video_id = models.CharField(
        max_length=255,
        help_text="Bunny Stream video GUID (from your Bunny library)"
    )
    bunny_library_id = models.CharField(
        max_length=100,
        blank=True,
        help_text="Overrides settings.BUNNY_STREAM_LIBRARY_ID if set"
    )
    duration_seconds = models.PositiveIntegerField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = table_name("video_assets")

    def __str__(self):
        return f"Video for: {self.lesson.title}"

    def get_embed_url(self):
        library_id = self.bunny_library_id or settings.BUNNY_STREAM_LIBRARY_ID
        return f"https://iframe.mediadelivery.net/embed/{library_id}/{self.bunny_video_id}"

    def get_player_url(self):
        library_id = self.bunny_library_id or settings.BUNNY_STREAM_LIBRARY_ID
        return f"https://iframe.mediadelivery.net/play/{library_id}/{self.bunny_video_id}"


class Resource(models.Model):
    """
    A resource attached to a Lesson - PDF (stored on GitHub) or external link.
    """

    class ResourceType(models.TextChoices):
        PDF = "pdf", "PDF Document"
        LINK = "link", "External Link"
        OTHER = "other", "Other"

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="resources")
    title = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=20, choices=ResourceType.choices, default=ResourceType.PDF)
    # For PDFs: stored path in GitHub e.g. "github://owner/repo/main/uploads/notes.pdf"
    github_stored_path = models.CharField(max_length=512, blank=True)
    # For external links
    external_url = models.URLField(blank=True, max_length=512)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = table_name("resources")
        ordering = ["lesson", "resource_type", "title"]

    def __str__(self):
        return f"{self.title} [{self.get_resource_type_display()}] - {self.lesson.title}"

    def get_download_url(self):
        """Return the URL to access this resource."""
        if self.resource_type == self.ResourceType.LINK:
            return self.external_url
        if self.github_stored_path:
            # Serve via Django proxy view (avoids exposing raw GitHub token URLs)
            return f"/content/resource/{self.pk}/download/"
        return None


class LessonProgress(models.Model):
    """Tracks whether a learner has viewed a lesson."""
    learner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="lesson_progress",
    )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="progress_records")
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    first_viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = table_name("lesson_progress")
        unique_together = [("learner", "lesson")]

    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"{status} {self.learner.get_full_name()} - {self.lesson.title}"
