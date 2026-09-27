from django.urls import path
from . import views

app_name = "prep"

urlpatterns = [
    path("", views.prep_dashboard, name="dashboard"),
    path("courses/", views.prep_courses, name="courses"),
    path("courses/<int:course_id>/add/", views.prep_add_course, name="add_course"),
    path("courses/<str:course_code>/", views.prep_course_detail, name="course_detail"),
    path("topic/<str:topic_id>/", views.prep_topic_study, name="topic_study"),
    path("papers/", views.prep_past_papers, name="past_papers"),
    path("papers/<str:course_code>/<str:paper_id>/", views.prep_paper_detail, name="paper_detail"),
    path("practice/<str:topic_id>/", views.prep_practice, name="practice"),
    path("upload/", views.prep_upload, name="upload"),
    path("history/", views.prep_history, name="history"),
    path("billing/", views.prep_billing, name="billing"),
    path("billing/initiate/", views.prep_initiate_payment, name="initiate_payment"),
    path("billing/callback/", views.prep_payment_callback, name="payment_callback"),
    path("terms/", views.prep_terms, name="terms"),
    path("privacy/", views.prep_privacy, name="privacy"),
    # Export Endpoints (PDF & DOCX)
    path("export/topic/<str:topic_id>/<str:fmt>/", views.prep_export_topic, name="export_topic"),
    path("export/paper/<str:course_code>/<str:paper_id>/<str:fmt>/", views.prep_export_paper, name="export_paper"),
    # AI Router & Zero-Cost Cache Endpoints
    path("api/solve-question/", views.prep_solve_question_api, name="api_solve_question"),
    path("api/topic-notes/", views.prep_topic_notes_api, name="api_topic_notes"),
    path("api/generate-practice/", views.prep_generate_practice_api, name="api_generate_practice"),
    # Live Student Notification Endpoints
    path("api/notifications/", views.prep_notifications_api, name="api_notifications"),
    path("api/notifications/read/", views.prep_mark_notification_read_api, name="api_notifications_read"),
    # Mentify Prep AI Assistant
    path("api/assistant/chat/", views.prep_assistant_chat_api, name="api_assistant_chat"),
]
