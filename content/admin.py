"""content/admin.py"""
from django.contrib import admin
from .models import Lesson, VideoAsset, Resource, LessonProgress


class VideoAssetInline(admin.StackedInline):
    model = VideoAsset
    extra = 0


class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 0


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["title", "cohort", "order", "is_published", "created_at"]
    list_filter = ["is_published", "cohort__course__track"]
    search_fields = ["title", "cohort__name", "cohort__course__title"]
    inlines = [VideoAssetInline, ResourceInline]
    ordering = ["cohort", "order"]


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ["title", "lesson", "resource_type", "uploaded_at"]
    list_filter = ["resource_type"]
    search_fields = ["title", "lesson__title"]


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ["learner", "lesson", "completed", "completed_at"]
    list_filter = ["completed"]
    raw_id_fields = ["learner", "lesson"]
