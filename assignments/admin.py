"""assignments/admin.py"""
from django.contrib import admin
from .models import Assignment, RubricCriterion, Submission, Grade, CriterionScore


class RubricCriterionInline(admin.TabularInline):
    model = RubricCriterion
    extra = 1


class CriterionScoreInline(admin.TabularInline):
    model = CriterionScore
    extra = 0


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ["title", "lesson", "due_date", "max_score", "is_published"]
    list_filter = ["is_published"]
    search_fields = ["title", "lesson__title"]
    inlines = [RubricCriterionInline]


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ["learner", "assignment", "status", "submitted_at"]
    list_filter = ["status"]
    search_fields = ["learner__email", "assignment__title"]
    raw_id_fields = ["learner", "assignment"]


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ["submission", "total_score", "graded_by", "graded_at"]
    raw_id_fields = ["submission", "graded_by"]
    inlines = [CriterionScoreInline]
