from __future__ import annotations

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
        result = self._service().upload_file(content, subdir="prep-media")
        if not result:
            raise OSError("GitHub media upload returned no path.")
        return result.repo_path

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
