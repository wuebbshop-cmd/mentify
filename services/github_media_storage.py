from __future__ import annotations

import hashlib
import os
from io import BytesIO
from urllib.parse import quote

import requests
from django.conf import settings
from django.core.files.base import File
from django.core.files.storage import Storage

from services.github_service import GitHubService


class GitHubMediaStorage(Storage):
    """Durable Django storage for uploaded prep media on the configured GitHub repo."""

    def _service(self) -> GitHubService:
        token = getattr(settings, "GITHUB_TOKEN", "")
        repo = getattr(settings, "GITHUB_REPO", "")
        branch = getattr(settings, "GITHUB_BRANCH", "main") or "main"
        upload_dir = getattr(settings, "GITHUB_UPLOAD_DIR", "mentify-uploads")
        return GitHubService(token=token, repo_name=repo, branch=branch, upload_dir=upload_dir)

    def _save(self, name, content):
        content_bytes = content.read()
        return self._upload_compact(name, content_bytes)

    def save_existing(self, name, content_bytes: bytes) -> str:
        """Upload an existing local file to a deterministic path for resumable migration."""
        return self._upload_compact(name, content_bytes)

    def _upload_compact(self, name, content_bytes: bytes) -> str:
        safe_name = "".join(char if char.isalnum() or char in "._-" else "_" for char in os.path.basename(name))
        digest = hashlib.sha256(content_bytes).hexdigest()[:16]
        safe_name = safe_name[:40]
        repo_path = f"{self._service().upload_dir}/prep-media/{digest}-{safe_name}"
        self._service()._commit_file(repo_path, content_bytes, f"[Mentify] Migrate {safe_name}")
        return repo_path

    def _open(self, name, mode="rb"):
        if "b" not in mode:
            raise ValueError("GitHubMediaStorage only supports binary reads.")
        repo = getattr(settings, "GITHUB_REPO", "")
        branch = getattr(settings, "GITHUB_BRANCH", "main") or "main"
        owner, repo_name = repo.split("/", 1)
        path = str(name).lstrip("/")
        response = requests.get(
            f"https://raw.githubusercontent.com/{owner}/{repo_name}/{branch}/{quote(path, safe='/')}",
            headers={"Authorization": f"token {settings.GITHUB_TOKEN}"} if settings.GITHUB_TOKEN else {},
            timeout=30,
        )
        response.raise_for_status()
        return File(BytesIO(response.content), name=path)

    def delete(self, name):
        if not name:
            return
        self._service().delete_file(f"github://{settings.GITHUB_REPO}/{settings.GITHUB_BRANCH}/{str(name).lstrip('/')}")

    def exists(self, name):
        # GitHubService generates a unique filename for every upload.
        return False

    def url(self, name):
        if not name:
            return ""
        value = str(name)
        if value.startswith(("http://", "https://", "/cdn/")):
            return value
        return f"/cdn/assets/{quote(value.lstrip('/'), safe='/')}"

    def size(self, name):
        with self._open(name, "rb") as file_obj:
            file_obj.seek(0, 2)
            return file_obj.tell()
