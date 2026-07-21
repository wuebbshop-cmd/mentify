"""Sitemap and robots.txt views for SEO - Google Search Console integration"""

from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone
from django.views.decorators.cache import cache_page
from xml.sax.saxutils import escape

from courses.models import Course


@cache_page(60 * 15)
def sitemap(request):
    """
    Generate XML sitemap for Google Search Console.
    Includes:
    - Public pages (home, login, register)
    - Course browsing (catalog)
    - About/Help pages (if any)
    
    Returns: XML formatted as application/xml
    """
    base_url = settings.BASE_URL.rstrip("/")
    today = timezone.now().date().isoformat()
    
    # List of static pages with priority and change frequency
    static_pages = [
        {
            'loc': f"{base_url}/",
            'lastmod': today,
            'changefreq': 'weekly',
            'priority': '1.0',
        },
        {
            'loc': f"{base_url}/accounts/login/",
            'lastmod': today,
            'changefreq': 'monthly',
            'priority': '0.8',
        },
        {
            'loc': f"{base_url}/accounts/register/",
            'lastmod': today,
            'changefreq': 'monthly',
            'priority': '0.8',
        },
        {
            'loc': f"{base_url}/courses/",
            'lastmod': today,
            'changefreq': 'daily',
            'priority': '0.9',
        },
    ]

    course_pages = []
    for course in Course.objects.filter(is_active=True).only("slug", "updated_at"):
        course_pages.append({
            "loc": f"{base_url}/courses/{course.slug}/",
            "lastmod": course.updated_at.date().isoformat(),
            "changefreq": "weekly",
            "priority": "0.8",
        })

    pages = static_pages + course_pages
    
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
    Generate robots.txt for search engine crawlers.
    Directs crawlers to sitemap and specifies disallowed paths.
    
    Returns: Plain text formatted as text/plain
    """
    base_url = settings.BASE_URL.rstrip('/')
    sitemap_url = f"{base_url}/sitemap.xml"
    
    robots_content = f"""# robots.txt - Web crawler directives and sitemap location
# Tells search engines which pages to crawl and where sitemap is located

# Allow all crawlers (no restrictions)
User-agent: *
Allow: /

# Disallow private/admin areas
Disallow: /admin/
Disallow: /accounts/admin-*
Disallow: /dashboard/admin*

# Sitemap location for Google Search Console and other search engines
Sitemap: {sitemap_url}

# Optional: Add more sitemaps if you have additional ones later
# Sitemap: {base_url}/courses-sitemap.xml
# Sitemap: {base_url}/content-sitemap.xml
"""
    
    return HttpResponse(robots_content, content_type='text/plain')

