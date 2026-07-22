"""courses/admin.py"""
from django import forms
from django.contrib import admin
from django.conf import settings

from .models import Course, Cohort, Enrollment
from services.github_service import GitHubService, normalize_asset_reference


class CourseAdminForm(forms.ModelForm):
    cover_image_upload = forms.ImageField(
        required=False,
        label="Upload cover image",
        help_text="Uploads to the configured GitHub repo and uses it as the course banner.",
    )

    class Meta:
        model = Course
        fields = "__all__"


class CohortInline(admin.TabularInline):
    model = Cohort
    extra = 0
    show_change_link = True
    fields = ["name", "tutor", "start_date", "end_date", "price_kes", "status", "capacity"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ["title", "track", "level", "subject_area", "is_active", "created_at"]
    list_filter = ["track", "level", "is_active"]
    search_fields = ["title", "subject_area"]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [CohortInline]

    def save_model(self, request, obj, form, change):
        uploaded = form.cleaned_data.get("cover_image_upload")
        if uploaded:
            svc = GitHubService(
                settings.GITHUB_TOKEN,
                settings.GITHUB_REPO,
                settings.GITHUB_BRANCH,
                settings.GITHUB_UPLOAD_DIR,
            )
            result = svc.upload_file(uploaded, subdir=f"course-covers/{obj.slug or 'new-course'}")
            if result:
                obj.cover_image_url = result.stored_path
        elif obj.cover_image_url:
            obj.cover_image_url = normalize_asset_reference(
                obj.cover_image_url,
                repo_name=settings.GITHUB_REPO,
                branch=settings.GITHUB_BRANCH,
            )
        super().save_model(request, obj, form, change)


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
