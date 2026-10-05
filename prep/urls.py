from django.urls import path
from . import views

app_name = "prep"

urlpatterns = [
    # Public, crawlable Mentify Prep learning library. These read only approved
    # shared content and never invoke AI generation or student credit logic.
    path("library/", views.prep_public_library, name="public_library"),
    path("library/<slug:course_slug>/", views.prep_public_course, name="public_course"),
    path(
        "library/<slug:course_slug>/<int:topic_id>-<slug:topic_slug>/",
        views.prep_public_topic,
        name="public_topic",
    ),
    path("", views.prep_dashboard, name="dashboard"),
    path("courses/", views.prep_courses, name="courses"),
    path("courses/<int:course_id>/add/", views.prep_add_course, name="add_course"),
    path("courses/<int:course_id>/remove/", views.prep_remove_course, name="remove_course"),
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
    path("api/topic/<int:topic_id>/tutor/", views.prep_topic_tutor_api, name="api_topic_tutor"),
    path("api/generate-practice/", views.prep_generate_practice_api, name="api_generate_practice"),
    path("api/adapt-question/", views.prep_adapt_question_api, name="api_adapt_question"),
    # Live Student Notification Endpoints
    path("api/notifications/", views.prep_notifications_api, name="api_notifications"),
    path("api/notifications/read/", views.prep_mark_notification_read_api, name="api_notifications_read"),
    # Mentify Prep AI Assistant
    path("api/assistant/chat/", views.prep_assistant_chat_api, name="api_assistant_chat"),
]
