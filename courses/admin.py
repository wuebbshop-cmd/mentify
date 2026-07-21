"""courses/admin.py"""
from django.contrib import admin
from .models import Course, Cohort, Enrollment


class CohortInline(admin.TabularInline):
    model = Cohort
    extra = 0
    show_change_link = True
    fields = ["name", "tutor", "start_date", "end_date", "price_kes", "status", "capacity"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "track", "level", "subject_area", "is_active", "created_at"]
    list_filter = ["track", "level", "is_active"]
    search_fields = ["title", "subject_area"]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [CohortInline]


class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 0
    readonly_fields = ["enrolled_at"]
    raw_id_fields = ["learner"]


@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    list_display = ["name", "course", "tutor", "status", "start_date", "end_date", "price_kes", "enrolled_count", "capacity"]
    list_filter = ["status", "course__track"]
    search_fields = ["name", "course__title", "tutor__email"]
    raw_id_fields = ["tutor"]
    inlines = [EnrollmentInline]

    def enrolled_count(self, obj):
        return obj.enrolled_count
    enrolled_count.short_description = "Enrolled"


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["learner", "cohort", "status", "enrolled_at"]
    list_filter = ["status"]
    search_fields = ["learner__email", "cohort__name", "cohort__course__title"]
    raw_id_fields = ["learner", "cohort"]
