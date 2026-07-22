from django import template
from django.conf import settings

from services.github_service import github_public_url

register = template.Library()


@register.filter
def public_asset_url(value):
    return github_public_url(
        value,
        repo_name=getattr(settings, "GITHUB_REPO", ""),
        branch=getattr(settings, "GITHUB_BRANCH", "main"),
    ) or ""
