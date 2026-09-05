import json
import logging
import os
import re
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from courses.models import Course
from services.cdn_views import upload_to_github
from .models import Category, Post

logger = logging.getLogger(__name__)


def _is_tutor_or_admin(user):
    return user.is_authenticated and (user.role in ("tutor", "admin") or user.is_staff or user.is_superuser)


def blog_index(request):
    """Public Blog Hub: Hero featured post, search, category filter, article grid."""
    q = request.GET.get("q", "").strip()
    category_slug = request.GET.get("category", "").strip()

    posts = Post.objects.filter(is_published=True).select_related("author", "category")

    if q:
        posts = posts.filter(
            Q(title__icontains=q)
            | Q(excerpt__icontains=q)
            | Q(markdown_content__icontains=q)
            | Q(tags__icontains=q)
        )

    active_category = None
    if category_slug:
        active_category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=active_category)

    featured_post = None
    if not q and not category_slug:
        featured_post = posts.filter(is_featured=True).first()
        if not featured_post and posts.exists():
            featured_post = posts.first()
        if featured_post:
            posts = posts.exclude(pk=featured_post.pk)

    categories = Category.objects.all()

    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "featured_post": featured_post,
        "page_obj": page_obj,
        "categories": categories,
        "active_category": active_category,
        "search_query": q,
        "PLATFORM_NAME": getattr(settings, "PLATFORM_NAME", "Mentify"),
    }
    return render(request, "blog/index.html", context)


def post_detail(request, slug):
    """Single Blog Article Reader view."""
    post = get_object_or_404(Post, slug=slug)

    # If post is draft, only author or admin can view preview
    if not post.is_published:
        if not _is_tutor_or_admin(request.user) and request.user != post.author:
            return render(request, "404.html", status=404)

    # Increment view counter silently
    Post.objects.filter(pk=post.pk).update(views_count=models.F("views_count") + 1)
    post.refresh_from_db(fields=["views_count"])

    related_posts = (
        Post.objects.filter(is_published=True)
        .exclude(pk=post.pk)
        .select_related("category", "author")
    )
    if post.category:
        related_posts = related_posts.filter(category=post.category)[:3]
    else:
        related_posts = related_posts[:3]

    active_courses = Course.objects.filter(is_active=True)[:2]

    context = {
        "post": post,
        "related_posts": related_posts,
        "active_courses": active_courses,
        "PLATFORM_NAME": getattr(settings, "PLATFORM_NAME", "Mentify"),
    }
    return render(request, "blog/detail.html", context)


def category_detail(request, slug):
    """Articles archive for a specific Category."""
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, is_published=True).select_related("author")

    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    context = {
        "category": category,
        "page_obj": page_obj,
        "categories": categories,
        "PLATFORM_NAME": getattr(settings, "PLATFORM_NAME", "Mentify"),
    }
    return render(request, "blog/category.html", context)


@login_required
def tutor_blog_manage(request):
    """Tutor & Admin Blog Management Dashboard."""
    if not _is_tutor_or_admin(request.user):
        messages.error(request, "Access restricted to tutors and admins.")
        return redirect("accounts:dashboard")

    if request.user.role == "admin" or request.user.is_staff or request.user.is_superuser:
        posts = Post.objects.all().select_related("author", "category")
    else:
        posts = Post.objects.filter(author=request.user).select_related("category")

    context = {
        "posts": posts,
        "total_count": posts.count(),
        "published_count": posts.filter(is_published=True).count(),
        "draft_count": posts.filter(is_published=False).count(),
    }
    return render(request, "blog/manage.html", context)


@login_required
def tutor_blog_create(request):
    """Create a new blog post with live Markdown Editor & .md File Upload Importer."""
    if not _is_tutor_or_admin(request.user):
        messages.error(request, "Access restricted to tutors and admins.")
        return redirect("accounts:dashboard")

    categories = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        category_id = request.POST.get("category")
        excerpt = request.POST.get("excerpt", "").strip()
        markdown_content = request.POST.get("markdown_content", "").strip()
        featured_image_url = request.POST.get("featured_image_url", "").strip()
        tags = request.POST.get("tags", "").strip()
        is_published = request.POST.get("is_published") == "on"
        is_featured = request.POST.get("is_featured") == "on"

        # Check if a .md file was uploaded
        md_file = request.FILES.get("md_file")
        if md_file and md_file.name.endswith((".md", ".markdown", ".txt")):
            try:
                uploaded_text = md_file.read().decode("utf-8", errors="replace")
                if not markdown_content:
                    markdown_content = uploaded_text
                if not title:
                    # Extract title from first # heading if missing
                    match = re.search(r"^#\s+(.+)$", uploaded_text, re.MULTILINE)
                    if match:
                        title = match.group(1).strip()
                    else:
                        title = os.path.splitext(md_file.name)[0].replace("-", " ").replace("_", " ").title()
            except Exception as e:
                logger.error("Failed to parse uploaded .md file: %s", e)
                messages.warning(request, "Could not automatically read the uploaded .md file.")

        if not title:
            messages.error(request, "Article title is required.")
            return render(request, "blog/form.html", {"categories": categories})

        category = Category.objects.filter(pk=category_id).first() if category_id else None

        post = Post.objects.create(
            title=title,
            excerpt=excerpt,
            markdown_content=markdown_content,
            featured_image_url=featured_image_url,
            author=request.user,
            category=category,
            tags=tags,
            is_published=is_published,
            is_featured=is_featured,
            published_at=timezone.now(),
        )

        messages.success(request, f"Article '{post.title}' created successfully!")
        return redirect("blog:tutor_manage")

    context = {
        "categories": categories,
        "action": "Create",
    }
    return render(request, "blog/form.html", context)


@login_required
def tutor_blog_edit(request, post_id):
    """Edit existing blog post."""
    if not _is_tutor_or_admin(request.user):
        messages.error(request, "Access restricted to tutors and admins.")
        return redirect("accounts:dashboard")

    if request.user.role == "admin" or request.user.is_staff or request.user.is_superuser:
        post = get_object_or_404(Post, pk=post_id)
    else:
        post = get_object_or_404(Post, pk=post_id, author=request.user)

    categories = Category.objects.all()

    if request.method == "POST":
        post.title = request.POST.get("title", "").strip() or post.title
        category_id = request.POST.get("category")
        post.category = Category.objects.filter(pk=category_id).first() if category_id else None
        post.excerpt = request.POST.get("excerpt", "").strip()
        post.markdown_content = request.POST.get("markdown_content", "").strip()
        post.featured_image_url = request.POST.get("featured_image_url", "").strip()
        post.tags = request.POST.get("tags", "").strip()
        post.is_published = request.POST.get("is_published") == "on"
        post.is_featured = request.POST.get("is_featured") == "on"

        # Check if a replacement .md file was uploaded
        md_file = request.FILES.get("md_file")
        if md_file and md_file.name.endswith((".md", ".markdown", ".txt")):
            try:
                uploaded_text = md_file.read().decode("utf-8", errors="replace")
                post.markdown_content = uploaded_text
            except Exception as e:
                logger.error("Failed to parse uploaded .md file: %s", e)

        post.save()
        messages.success(request, f"Article '{post.title}' updated successfully!")
        return redirect("blog:tutor_manage")

    context = {
        "post": post,
        "categories": categories,
        "action": "Edit",
    }
    return render(request, "blog/form.html", context)


@login_required
def tutor_blog_delete(request, post_id):
    """Delete blog post."""
    if not _is_tutor_or_admin(request.user):
        messages.error(request, "Access restricted.")
        return redirect("accounts:dashboard")

    if request.user.role == "admin" or request.user.is_staff or request.user.is_superuser:
        post = get_object_or_404(Post, pk=post_id)
    else:
        post = get_object_or_404(Post, pk=post_id, author=request.user)

    if request.method == "POST":
        title = post.title
        post.delete()
        messages.success(request, f"Article '{title}' deleted successfully.")
        return redirect("blog:tutor_manage")

    return render(request, "blog/delete_confirm.html", {"post": post})


@login_required
def upload_blog_image(request):
    """AJAX endpoint for uploading images inside Markdown editor to GitHub CDN."""
    if not _is_tutor_or_admin(request.user):
        return JsonResponse({"error": "Unauthorized"}, status=403)

    if request.method == "POST" and request.FILES.get("image"):
        image_file = request.FILES["image"]
        filename = f"blog_{timezone.now().strftime('%Y%m%d_%H%M%S')}_{image_file.name}"
        cdn_url = upload_to_github(image_file, filename, folder="blog")

        if cdn_url:
            return JsonResponse({"success": True, "url": cdn_url})
        else:
            return JsonResponse({"error": "Failed to upload image to CDN"}, status=500)

    return JsonResponse({"error": "No image provided"}, status=400)
