from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "color_hex", "created_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "description")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "author",
        "is_published",
        "is_featured",
        "views_count",
        "published_at",
    )
    list_filter = ("is_published", "is_featured", "category", "created_at")
    search_fields = ("title", "markdown_content", "tags", "excerpt")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    ordering = ("-published_at",)
