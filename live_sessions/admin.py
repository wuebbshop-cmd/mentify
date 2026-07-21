"""sessions/admin.py"""
from django.contrib import admin
from .models import LiveSession, Attendance


class AttendanceInline(admin.TabularInline):
    model = Attendance
    extra = 0
    raw_id_fields = ["learner", "marked_by"]


@admin.register(LiveSession)
class LiveSessionAdmin(admin.ModelAdmin):
    list_display = ["title", "cohort", "scheduled_at", "is_makeup", "is_cancelled", "is_upcoming"]
    list_filter = ["is_makeup", "is_cancelled", "cohort__course__track"]
    search_fields = ["title", "cohort__name"]
    raw_id_fields = ["cohort", "created_by", "original_session"]
    inlines = [AttendanceInline]

    def is_upcoming(self, obj):
        return obj.is_upcoming
    is_upcoming.boolean = True
    is_upcoming.short_description = "Upcoming?"


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["learner", "session", "status", "marked_at"]
    list_filter = ["status"]
    raw_id_fields = ["learner", "session", "marked_by"]
