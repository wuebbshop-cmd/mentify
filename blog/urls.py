from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # Public views
    path("", views.blog_index, name="index"),
    path("<slug:slug>/", views.post_detail, name="detail"),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),

    # Tutor & Admin management
    path("manage/dashboard/", views.tutor_blog_manage, name="tutor_manage"),
    path("manage/create/", views.tutor_blog_create, name="tutor_create"),
    path("manage/edit/<int:post_id>/", views.tutor_blog_edit, name="tutor_edit"),
    path("manage/delete/<int:post_id>/", views.tutor_blog_delete, name="tutor_delete"),
    path("manage/upload-image/", views.upload_blog_image, name="upload_image"),
]
