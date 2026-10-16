import logging
from django.conf import settings
from django.http import HttpResponsePermanentRedirect

logger = logging.getLogger(__name__)


class DomainRedirectMiddleware:
    """
    HTTP 301 Permanent Redirect middleware for SEO authority and brand domain migration.

    Redirects legacy domains (mlaudit.info, www.mlaudit.info, and www.mentify.study)
    to the canonical primary domain (mentify.study), preserving the exact request path
    and query parameters so that Google SEO rankings, search index, and backlinks
    seamlessly transfer to the new domain.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        primary_domain = getattr(settings, "PRIMARY_DOMAIN", "mentify.study")
        redirect_domains = getattr(
            settings,
            "REDIRECT_DOMAINS",
            {"mlaudit.info", "www.mlaudit.info", "www.mentify.study"},
        )

        host = request.get_host().split(":")[0].lower()
        if host in redirect_domains and host != primary_domain:
            redirect_url = f"https://{primary_domain}{request.get_full_path()}"
            logger.info(
                "301 Permanent Redirect from legacy domain %s to %s for path %s",
                host,
                redirect_url,
                request.path,
            )
            return HttpResponsePermanentRedirect(redirect_url)

        return self.get_response(request)
