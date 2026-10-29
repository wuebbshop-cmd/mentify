"""
HTTP View for serving Cloudflare R2 stored media and PDF assets with edge caching.
"""
from __future__ import annotations

import mimetypes
import os
from pathlib import Path
from urllib.parse import unquote

from django.conf import settings
from django.http import Http404, HttpResponse, StreamingHttpResponse
from django.views.decorators.http import condition

from services.cloudflare_storage import CloudflareR2MediaStorage, is_cloudflare_r2_configured


def _guess_content_type(filepath: str) -> str:
    content_type, _ = mimetypes.guess_type(filepath)
    return content_type or "application/octet-stream"


def cloudflare_asset_proxy(request, filepath: str):
    """
    High-performance CDN proxy view for Cloudflare R2 media files.
    Serves images, PDFs, and media assets with 7-day browser & edge caching.
    
    Fallback chain:
    1. Cloudflare R2 bucket
    2. Local MEDIA_ROOT (and auto-promotes to R2)
    3. GitHub media store (for legacy mentify-uploads paths)
    """
    clean_path = unquote(filepath).replace("\\", "/").strip("/")
    if not clean_path or ".." in clean_path:
        raise Http404("Invalid asset path")

    content_type = _guess_content_type(clean_path)

    # 1. Attempt Cloudflare R2
    if is_cloudflare_r2_configured():
        storage = CloudflareR2MediaStorage()
        try:
            content_bytes = storage.download_bytes(clean_path)
            response = HttpResponse(content_bytes, content_type=content_type)
            response["Cache-Control"] = "public, max-age=604800, immutable"
            return response
        except Exception:
            # File might not yet be migrated to R2; fallback below
            pass

    # 2. Fallback to local MEDIA_ROOT
    local_file = Path(settings.MEDIA_ROOT) / clean_path
    if local_file.is_file():
        try:
            content_bytes = local_file.read_bytes()
            # If R2 is configured, asynchronously/lazily promote this file to R2
            if is_cloudflare_r2_configured():
                try:
                    storage = CloudflareR2MediaStorage()
                    storage.save_existing(clean_path, content_bytes, content_type=content_type)
                except Exception:
                    pass
            response = HttpResponse(content_bytes, content_type=content_type)
            response["Cache-Control"] = "public, max-age=86400"
            return response
        except Exception:
            pass

    # 3. Fallback to GitHub for legacy paths
    from services.cdn_views import _fetch_github_asset
    repo = getattr(settings, "GITHUB_REPO", "").strip()
    branch = getattr(settings, "GITHUB_BRANCH", "main").strip() or "main"
    if repo and "/" in repo:
        try:
            owner, repo_name = repo.split("/", 1)
            content, g_content_type = _fetch_github_asset(owner, repo_name, branch, clean_path)
            if content:
                # Promote to R2
                if is_cloudflare_r2_configured():
                    try:
                        storage = CloudflareR2MediaStorage()
                        storage.save_existing(clean_path, content, content_type=g_content_type or content_type)
                    except Exception:
                        pass
                response = HttpResponse(content, content_type=g_content_type or content_type)
                response["Cache-Control"] = "public, max-age=86400"
                return response
        except Exception:
            pass

    raise Http404("Asset not found in Cloudflare R2, local media, or repository.")
