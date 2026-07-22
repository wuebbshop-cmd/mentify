"""Authenticated proxy for GitHub-hosted public assets (images, etc.)."""
from __future__ import annotations

import base64
import mimetypes

import requests
from django.conf import settings
from django.http import Http404, HttpResponse
from urllib.parse import quote, unquote


def _guess_content_type(filepath: str, upstream_type: str | None = None) -> str:
    if upstream_type and upstream_type != "application/octet-stream":
        return upstream_type
    guessed, _ = mimetypes.guess_type(filepath)
    return guessed or "application/octet-stream"


def _fetch_github_asset(owner: str, repo: str, ref: str, filepath: str) -> tuple[bytes, str]:
    """
    Fetch a file from GitHub via raw URL, falling back to the Contents API.
    Mirrors BloodLink's /cdn/profile_pics/ proxy for private repositories.
    """
    filepath = unquote(filepath)
    encoded_path = quote(filepath, safe="/")
    raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{ref}/{encoded_path}"

    token = getattr(settings, "GITHUB_TOKEN", "").strip()
    headers: dict[str, str] = {}
    if token:
        headers["Authorization"] = f"token {token}"

    try:
        upstream = requests.get(raw_url, headers=headers, timeout=15)
    except requests.RequestException:
        upstream = None

    if upstream is not None and upstream.status_code == 200:
        return upstream.content, _guess_content_type(filepath, upstream.headers.get("Content-Type"))

    if not token:
        raise Http404("Asset not found")

    api_headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
    }
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{quote(filepath, safe='/')}"
    try:
        api_resp = requests.get(api_url, headers=api_headers, params={"ref": ref}, timeout=15)
    except requests.RequestException:
        raise Http404("Asset not found") from None

    if api_resp.status_code != 200:
        raise Http404("Asset not found")

    data = api_resp.json()
    if not isinstance(data, dict) or "content" not in data:
        raise Http404("Asset not found")

    content = base64.b64decode(data["content"].replace("\n", ""))
    return content, _guess_content_type(filepath)


def assets_proxy(request, filepath):
    """
    BloodLink-style proxy for files in the configured GitHub repo/branch.
    Example: /cdn/assets/mentify-uploads/course-cover.png
    """
    repo = getattr(settings, "GITHUB_REPO", "").strip()
    branch = getattr(settings, "GITHUB_BRANCH", "main").strip() or "main"
    if not repo or "/" not in repo:
        raise Http404("Asset not found")

    owner, repo_name = repo.split("/", 1)
    content, content_type = _fetch_github_asset(owner, repo_name, branch, filepath)
    response = HttpResponse(content, content_type=content_type)
    response["Cache-Control"] = "public, max-age=86400"
    return response


def github_asset_proxy(request, owner, repo, ref, filepath):
    """Stream a file from any GitHub repo/ref/path combination."""
    content, content_type = _fetch_github_asset(owner, repo, ref, filepath)
    response = HttpResponse(content, content_type=content_type)
    response["Cache-Control"] = "public, max-age=86400"
    return response
