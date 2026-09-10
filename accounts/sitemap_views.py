"""Sitemap and robots.txt views for SEO - Google Search Console integration"""

from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone
from django.views.decorators.cache import cache_page
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
    Includes:
    - Homepage & marketing pages (contact, terms, privacy, cookies)
    - Role registration pages & login
    - Course catalog & all active courses
    - Active cohorts
    - Public tutor profiles
    
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

    pages = static_pages + blog_hub + course_pages + blog_post_pages + cohort_pages + tutor_pages
    
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

> Mentify is an interactive online tutoring, cohort learning, and tech education platform founded and led by John Shivogo. It offers hands-on programming courses, machine learning & AI code auditing, live cohort mentorship, and career-focused technical articles.

## Core Offerings
- Live Online Cohorts: Interactive coding courses with live instruction, code reviews, and personal guidance.
- Course Catalog: Python, Machine Learning, Data Science, Web Development, and Computer Science.
- Technical Blog: Practical tutorials, career advice, and deep dives authored by John Shivogo.
- Code & Model Auditing: Machine learning code evaluation, model safety, and software quality assurance.

## Key Resources & Links
- Homepage: {base_url}/
- Blog Hub & Technical Articles: {base_url}/blog/
- Course Catalog: {base_url}/courses/
- Register Account: {base_url}/accounts/register/
- XML Sitemap: {base_url}/sitemap.xml

## Founder & Lead Educator
- Founder & Author: John Shivogo
- Platform Name: Mentify
- Domain: mlaudit.info
"""
    return HttpResponse(llms_content, content_type='text/markdown')

