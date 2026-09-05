import math
import os
import re
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


def table_name(base_name: str) -> str:
    prefix = os.getenv("DB_TABLE_PREFIX", "me_")
    suffix = os.getenv("DB_TABLE_SUFFIX", "_tbl")
    return f"{prefix}{base_name}{suffix}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True, help_text="Short summary of this category")
    icon_name = models.CharField(max_length=50, default="book-open", help_text="SVG icon key or name")
    color_hex = models.CharField(max_length=20, default="#0f766e", help_text="Theme accent color hex code")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = table_name("blog_category")
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    excerpt = models.TextField(
        max_length=500,
        blank=True,
        help_text="Short teaser summary displayed on cards and social share previews",
    )
    markdown_content = models.TextField(
        help_text="Full article body in Markdown format (# headings, **bold**, *italics*, code blocks, images)",
    )
    featured_image_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="URL of cover image (GitHub CDN or external URL)",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_posts",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
    )
    tags = models.CharField(
        max_length=255,
        blank=True,
        help_text="Comma-separated tags (e.g. Python, AI, Beginner)",
    )
    is_published = models.BooleanField(
        default=True,
        help_text="Whether this post is visible live on the site",
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Pin this article as a featured hero story on the blog home",
    )
    published_at = models.DateTimeField(default=timezone.now)
    views_count = models.PositiveIntegerField(default=0)
    reading_time_minutes = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = table_name("blog_post")
        ordering = ["-published_at", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or "article"
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        # Calculate estimated reading time (approx. 200 words per minute)
        words = len(re.findall(r"\w+", self.markdown_content or ""))
        self.reading_time_minutes = max(1, math.ceil(words / 200)) if words else 1

        super().save(*args, **kwargs)

    def get_tag_list(self):
        if not self.tags:
            return []
        return [t.strip() for t in self.tags.split(",") if t.strip()]

    def __str__(self):
        return self.title
