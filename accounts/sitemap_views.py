"""Sitemap and robots.txt views for SEO - Google Search Console integration"""

from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.db.models import Q
from xml.sax.saxutils import escape

def get_base_url(request):
    """Dynamically resolve canonical base URL for SEO outputs."""
    configured = getattr(settings, "BASE_URL", "").strip().rstrip("/")
    if configured and "127.0.0.1" not in configured and "localhost" not in configured:
        return configured
    return request.build_absolute_uri("/").rstrip("/")


@cache_page(60 * 15)
def sitemap(request):
    """
    Generate XML sitemap for Google Search Console.
    Includes public Mentify marketing, catalog, blog, and Mentify Prep library
    resources. Logged-in workspaces, exports, and APIs are intentionally excluded.
    
    Returns: XML formatted as application/xml
    """
    from accounts.models import User
    from courses.models import Course, Cohort

    base_url = get_base_url(request)
    today = timezone.now().date().isoformat()
    
    # Static public pages
    static_pages = [
        {'loc': f"{base_url}/", 'lastmod': today, 'changefreq': 'weekly', 'priority': '1.0'},
        {'loc': f"{base_url}/courses/", 'lastmod': today, 'changefreq': 'daily', 'priority': '0.9'},
        {'loc': f"{base_url}/accounts/register/", 'lastmod': today, 'changefreq': 'monthly', 'priority': '0.8'},
        {'loc': f"{base_url}/accounts/register/learner/", 'lastmod': today, 'changefreq': 'monthly', 'priority': '0.8'},
        {'loc': f"{base_url}/accounts/register/guardian/", 'lastmod': today, 'changefreq': 'monthly', 'priority': '0.8'},
        {'loc': f"{base_url}/accounts/register/tutor/", 'lastmod': today, 'changefreq': 'monthly', 'priority': '0.8'},
        {'loc': f"{base_url}/accounts/login/", 'lastmod': today, 'changefreq': 'monthly', 'priority': '0.7'},
        {'loc': f"{base_url}/accounts/contact/", 'lastmod': today, 'changefreq': 'monthly', 'priority': '0.6'},
        {'loc': f"{base_url}/accounts/privacy-policy/", 'lastmod': today, 'changefreq': 'monthly', 'priority': '0.5'},
        {'loc': f"{base_url}/accounts/terms-of-service/", 'lastmod': today, 'changefreq': 'monthly', 'priority': '0.5'},
        {'loc': f"{base_url}/accounts/cookies/", 'lastmod': today, 'changefreq': 'monthly', 'priority': '0.5'},
    ]

    # Active Courses
    course_pages = []
    for course in Course.objects.filter(is_active=True).only("slug", "updated_at"):
        course_pages.append({
            "loc": f"{base_url}/courses/{course.slug}/",
            "lastmod": course.updated_at.date().isoformat(),
            "changefreq": "weekly",
            "priority": "0.8",
        })

    # Mentify Prep public course and topic study resources. These URLs are
    # anonymous, server-rendered, canonical pages, unlike the logged-in Prep
    # workspace routes under /prep/courses/ and /prep/topic/.
    prep_pages = []
    try:
        from prep.models import PrepContentCache, PrepCourse, PrepQuestion, PrepTopic
        from services.prep_ai_router import _note_completion_issues

        # Mentify Prep public marketing and footer pages
        prep_pages.extend([
            {"loc": f"{base_url}/prep/", "lastmod": today, "changefreq": "daily", "priority": "0.9"},
            {"loc": f"{base_url}/prep/library/", "lastmod": today, "changefreq": "daily", "priority": "0.9"},
            {"loc": f"{base_url}/prep/billing/", "lastmod": today, "changefreq": "weekly", "priority": "0.8"},
            {"loc": f"{base_url}/prep/upload/", "lastmod": today, "changefreq": "weekly", "priority": "0.8"},
            {"loc": f"{base_url}/prep/terms/", "lastmod": today, "changefreq": "monthly", "priority": "0.6"},
            {"loc": f"{base_url}/prep/privacy/", "lastmod": today, "changefreq": "monthly", "priority": "0.6"},
        ])
        for prep_course in PrepCourse.objects.filter(is_active=True).only("slug", "updated_at"):
            prep_pages.append({
                "loc": f"{base_url}/prep/library/{prep_course.slug}/",
                "lastmod": prep_course.updated_at.date().isoformat(),
                "changefreq": "weekly",
                "priority": "0.8",
            })

        notes_dates = {}
        for topic_id, topic_title, updated_at, payload in PrepContentCache.objects.filter(
                content_type="topic_notes",
                topic__course__is_active=True,
            ).order_by("topic_id", "updated_at").values_list("topic_id", "topic__title", "updated_at", "payload"):
            content = str((payload or {}).get("content", "") or "")
            if content and not _note_completion_issues(content, topic_title):
                notes_dates[topic_id] = updated_at

        for topic in PrepTopic.objects.filter(course__is_active=True).select_related("course").only(
            "id", "slug", "created_at", "course__slug"
        ):
            has_verified_questions = PrepQuestion.objects.filter(
                topic=topic,
                verification_status="verified",
            ).filter(Q(paper__isnull=True) | Q(paper__is_published=True)).exists()
            if topic.id not in notes_dates and not has_verified_questions:
                continue
            lastmod = notes_dates.get(topic.id, topic.created_at).date().isoformat()
            prep_pages.append({
                "loc": f"{base_url}/prep/library/{topic.course.slug}/{topic.id}-{topic.slug}/",
                "lastmod": lastmod,
                "changefreq": "weekly",
                "priority": "0.7",
            })
    except Exception:
        # A sitemap should remain available even if Prep migrations are pending.
        prep_pages = []

    # Blog Hub Page
    blog_hub = [{'loc': f"{base_url}/blog/", 'lastmod': today, 'changefreq': 'daily', 'priority': '0.9'}]

    # Published Blog Posts
    blog_post_pages = []
    try:
        from blog.models import Post, Category
        for post in Post.objects.filter(is_published=True).only("slug", "updated_at"):
            blog_post_pages.append({
                "loc": f"{base_url}/blog/{post.slug}/",
                "lastmod": post.updated_at.date().isoformat(),
                "changefreq": "weekly",
                "priority": "0.8",
            })
        for cat in Category.objects.all().only("slug"):
            blog_post_pages.append({
                "loc": f"{base_url}/blog/category/{cat.slug}/",
                "lastmod": today,
                "changefreq": "weekly",
                "priority": "0.7",
            })
    except Exception:
        pass

    # Active Cohorts
    cohort_pages = []
    for cohort in Cohort.objects.filter(status="active").only("id", "updated_at"):
        cohort_pages.append({
            "loc": f"{base_url}/courses/cohort/{cohort.id}/",
            "lastmod": cohort.updated_at.date().isoformat(),
            "changefreq": "weekly",
            "priority": "0.7",
        })

    # Public Tutor Profiles
    tutor_pages = []
    for tutor in User.objects.filter(role__in=["tutor", "admin"]).only("id", "updated_at"):
        tutor_pages.append({
            "loc": f"{base_url}/accounts/profile/{tutor.id}/",
            "lastmod": tutor.updated_at.date().isoformat() if tutor.updated_at else today,
            "changefreq": "monthly",
            "priority": "0.6",
        })

    pages = static_pages + blog_hub + course_pages + prep_pages + blog_post_pages + cohort_pages + tutor_pages
    
    xml_output = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
    
    for page in pages:
        xml_output += f"""  <url>
    <loc>{escape(page['loc'])}</loc>
    <lastmod>{page['lastmod']}</lastmod>
    <changefreq>{page['changefreq']}</changefreq>
    <priority>{page['priority']}</priority>
  </url>
"""
    
    xml_output += """</urlset>"""
    
    return HttpResponse(xml_output, content_type='application/xml')


@cache_page(60 * 60 * 24)
def robots_txt(request):
    """
    Generate robots.txt for search engine & AI crawlers.
    Directs crawlers to sitemap and llms.txt, specifying disallowed private paths.
    """
    base_url = get_base_url(request)
    sitemap_url = f"{base_url}/sitemap.xml"
    llms_url = f"{base_url}/llms.txt"
    
    robots_content = f"""# robots.txt - Mentify Web Crawler Directives

User-agent: *
Allow: /
Allow: /blog/
Allow: /courses/
Allow: /prep/
Allow: /prep/library/
Allow: /prep/billing/
Allow: /prep/upload/
Allow: /prep/terms/
Allow: /prep/privacy/
Allow: /llms.txt

# Explicitly allow AI Search Engines & LLM Crawlers
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

# Disallow private dashboards and internal endpoints
Disallow: /admin/
Disallow: /accounts/dashboard/
Disallow: /content/video/
Disallow: /content/resource/
Disallow: /payments/
Disallow: /prep/api/
Disallow: /prep/export/
Disallow: /prep/history/
Disallow: /prep/practice/

# XML Sitemap & LLMs Index
Sitemap: {sitemap_url}
# LLMs.txt for Generative Engine Optimization (GEO)
# Location: {llms_url}
"""
    
    return HttpResponse(robots_content, content_type='text/plain')


@cache_page(60 * 60 * 24)
def llms_txt(request):
    """
    Generate llms.txt for AI Search Engines (ChatGPT, Perplexity, Gemini, Claude).
    Provides structured, markdown summary of Mentify platform and author John Shivogo.
    """
    base_url = get_base_url(request)
    
    llms_content = f"""# Mentify ({base_url})

> Mentify is an interactive online tutoring, cohort learning, and tech education platform for students and adults. It offers hands-on programming courses, machine learning & AI code auditing, live cohort mentorship, robotics, math, science, and career-focused technical articles. Mentify Prep is the specialized course-anchored exam readiness and past-paper revision engine for university students.

## Core Offerings
- Live Online Cohorts: Interactive coding courses with live instruction, code reviews, and personal guidance.
- Course Catalog: Python, Machine Learning, Data Science, Web Development, and Computer Science.
- Technical Blog: Practical tutorials, career advice, and deep dives authored by John Shivogo.
- Code & Model Auditing: Machine learning code evaluation, model safety, and software quality assurance.
- Mentify Prep Exam Engine: Course-anchored university past papers, CAT revision, syllabus modules, verified step-by-step mathematical proofs, and document ingestion.

## Key Resources & Links
- Homepage: {base_url}/
- Blog Hub & Technical Articles: {base_url}/blog/
- Course Catalog: {base_url}/courses/
- Mentify Prep Workspace: {base_url}/prep/
- Mentify Prep Public Study Library: {base_url}/prep/library/
- Mentify Prep Credit Rules & Plans: {base_url}/prep/billing/
- Mentify Prep Upload & Verification Guidelines: {base_url}/prep/upload/
- Mentify Prep Terms of Service: {base_url}/prep/terms/
- Mentify Prep Privacy Policy: {base_url}/prep/privacy/
- Register Account: {base_url}/accounts/register/
- XML Sitemap: {base_url}/sitemap.xml

## Founder & Lead Educator
- Founder & Author: John Shivogo
- Platform Name: Mentify
- Domain: mlaudit.info
"""
    return HttpResponse(llms_content, content_type='text/markdown')
