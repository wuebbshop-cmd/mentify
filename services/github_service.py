"""
services/github_service.py

Adapted from ml101/github_ops.py (GitHubOps).
Framework-agnostic - handles PDF/file uploads to a GitHub repo.
"""
from __future__ import annotations

import base64
import uuid
from dataclasses import dataclass
from typing import Optional
from urllib.parse import quote, unquote, urlparse

import requests


@dataclass(slots=True)
class GitHubUploadResult:
    repo_path: str          # e.g. "uploads/cohort_3/lesson_1/abc123_notes.pdf"
    stored_path: str        # e.g. "github://owner/repo/main/uploads/..."


class GitHubService:
    """Uploads and deletes files in a GitHub repository via the Contents API."""

    def __init__(self, token: str, repo_name: str, branch: str = "main", upload_dir: str = "uploads") -> None:
        if not token or not repo_name:
            raise ValueError("GITHUB_TOKEN and GITHUB_REPO are required.")
        self.repo_name = repo_name
        self.branch = branch
        self.upload_dir = upload_dir.strip("/")
        self.base_url = "https://api.github.com"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json",
        })

    def _get_file_sha(self, path: str) -> Optional[str]:
        """Get the SHA of an existing file (needed for updates)."""
        resp = self.session.get(
            f"{self.base_url}/repos/{self.repo_name}/contents/{path}",
            params={"ref": self.branch},
        )
        if resp.status_code >= 300:
            return None
        data = resp.json()
        if isinstance(data, dict):
            return data.get("sha")
        return None

    def _commit_file(self, path: str, content: bytes, message: str) -> None:
        """Create or update a file in the repo."""
        encoded = base64.b64encode(content).decode("utf-8")
        payload: dict = {
            "message": message,
            "content": encoded,
            "branch": self.branch,
        }
        sha = self._get_file_sha(path)
        if sha:
            payload["sha"] = sha

        resp = self.session.put(
            f"{self.base_url}/repos/{self.repo_name}/contents/{path}",
            json=payload,
            timeout=30,
        )
        if resp.status_code >= 300:
            raise RuntimeError(f"GitHub upload failed: {resp.status_code} {resp.text}")

    def upload_file(self, file_obj, subdir: str | None = None) -> GitHubUploadResult | None:
        """
        Upload a file-like object to GitHub.
        file_obj can be a Django InMemoryUploadedFile or similar.
        Returns a GitHubUploadResult or None if file is empty.
        """
        if not file_obj:
            return None

        filename = getattr(file_obj, "name", "file") or "file"
        # Sanitize filename
        safe_name = "".join(c if c.isalnum() or c in "._-" else "_" for c in filename)
        unique_name = f"{uuid.uuid4().hex[:8]}_{safe_name}"

        base_dir = self.upload_dir
        if subdir:
            base_dir = f"{base_dir}/{subdir.strip('/')}"
        repo_path = f"{base_dir}/{unique_name}"

        # Read content
        try:
            if hasattr(file_obj, "seek"):
                file_obj.seek(0)
        except Exception:
            pass
        content = file_obj.read() if hasattr(file_obj, "read") else bytes(file_obj)
        if not content:
            return None

        self._commit_file(repo_path, content, f"[Mentify] Upload {unique_name}")
        stored_path = f"github://{self.repo_name}/{self.branch}/{repo_path}"
        return GitHubUploadResult(repo_path=repo_path, stored_path=stored_path)

    def download_file(self, stored_path: str) -> bytes:
        """
        Download a file from GitHub using the stored_path.
        Returns raw bytes. Raises RuntimeError on failure.
        """
        repo_path = self.repo_path_from_stored(stored_path)
        if not repo_path:
            raise RuntimeError(f"Invalid stored_path: {stored_path}")

        resp = self.session.get(
            f"{self.base_url}/repos/{self.repo_name}/contents/{repo_path}",
            params={"ref": self.branch},
        )
        if resp.status_code >= 300:
            raise RuntimeError(f"GitHub download failed: {resp.status_code}")

        data = resp.json()
        if not isinstance(data, dict) or "content" not in data:
            raise RuntimeError("Unexpected GitHub API response.")

        content_b64 = data["content"].replace("\n", "")
        return base64.b64decode(content_b64)

    def delete_file(self, stored_path: str) -> bool:
        """Delete a file from GitHub by its stored_path."""
        repo_path = self.repo_path_from_stored(stored_path)
        if not repo_path:
            return False
        sha = self._get_file_sha(repo_path)
        if not sha:
            return False

        payload = {
            "message": f"[Mentify] Delete {repo_path}",
            "sha": sha,
            "branch": self.branch,
        }
        resp = self.session.delete(
            f"{self.base_url}/repos/{self.repo_name}/contents/{repo_path}",
            json=payload,
            timeout=30,
        )
        return resp.status_code < 300

    @staticmethod
    def repo_path_from_stored(stored_path: str) -> Optional[str]:
        """Extract the repo-relative path from a stored_path string."""
        if not stored_path or not stored_path.startswith("github://"):
            return None
        # github://owner/repo/branch/path/to/file
        rest = stored_path[len("github://"):]
        parts = rest.split("/", 3)  # owner, repo, branch, path
        if len(parts) < 4:
            return None
        return parts[3]


def clean_asset_reference(value: str | None) -> str:
    """Strip whitespace and trailing punctuation from pasted asset URLs."""
    if not value:
        return ""
    return value.strip().rstrip(";,").strip()


def assets_cdn_url(repo_path: str) -> str:
    """Build a BloodLink-style local proxy URL for a repo-relative file path."""
    return f"/cdn/assets/{quote(repo_path.lstrip('/'), safe='/')}"


def github_cdn_url(owner: str, repo: str, ref: str, repo_path: str) -> str:
    """Build a local proxy URL for a GitHub-hosted asset."""
    return f"/cdn/github/{owner}/{repo}/{ref}/{quote(repo_path.lstrip('/'), safe='/')}"


def parse_raw_github_url(url: str) -> tuple[str, str, str, str] | None:
    """Return (owner, repo, ref, path) from a raw.githubusercontent.com URL."""
    parsed = urlparse(clean_asset_reference(url))
    if parsed.netloc != "raw.githubusercontent.com":
        return None

    parts = parsed.path.lstrip("/").split("/", 3)
    if len(parts) < 4:
        return None

    owner, repo, ref, repo_path = parts
    return owner, repo, ref, unquote(repo_path)


def _repo_matches(full_repo: str, configured_repo: str) -> bool:
    return bool(configured_repo) and full_repo.lower() == configured_repo.lower()


def normalize_asset_reference(
    value: str | None,
    *,
    repo_name: str = "",
    branch: str = "main",
) -> str:
    """
    Normalize pasted links into a stable github:// stored reference.
    Raw commit URLs for the configured repo are rewritten to use the branch ref.
    """
    value = clean_asset_reference(value)
    if not value:
        return ""

    if value.startswith("github://"):
        return value

    if value.startswith("/cdn/assets/"):
        repo_path = unquote(value[len("/cdn/assets/"):].lstrip("/"))
        if repo_name and repo_path:
            return f"github://{repo_name}/{branch}/{repo_path}"
        return value

    parsed = parse_raw_github_url(value)
    if parsed:
        owner, repo, _ref, repo_path = parsed
        full_repo = f"{owner}/{repo}"
        if _repo_matches(full_repo, repo_name):
            return f"github://{repo_name}/{branch}/{repo_path}"
        return value

    if value.startswith(("http://", "https://")):
        return value

    if repo_name and not value.startswith("/"):
        return f"github://{repo_name}/{branch}/{value.lstrip('/')}"

    return value


def github_public_url(
    stored_path: str | None,
    *,
    repo_name: str = "",
    branch: str = "main",
) -> str | None:
    """Return a browser-usable URL for a stored GitHub path or ordinary URL."""
    stored_path = clean_asset_reference(stored_path)
    if not stored_path:
        return None

    if stored_path.startswith("/cdn/assets/") or stored_path.startswith("/cdn/github/"):
        return stored_path

    parsed = parse_raw_github_url(stored_path)
    if parsed:
        owner, repo, ref, repo_path = parsed
        full_repo = f"{owner}/{repo}"
        if _repo_matches(full_repo, repo_name):
            return assets_cdn_url(repo_path)
        return github_cdn_url(owner, repo, ref, repo_path)

    if stored_path.startswith(("http://", "https://")):
        return stored_path

    if stored_path.startswith("github://"):
        rest = stored_path[len("github://"):]
        parts = rest.split("/", 3)
        if len(parts) < 4:
            return None
        owner, repo, stored_branch, repo_path = parts
        full_repo = f"{owner}/{repo}"
        if _repo_matches(full_repo, repo_name):
            return assets_cdn_url(repo_path)
        return github_cdn_url(owner, repo, stored_branch, repo_path)

    if repo_name:
        return assets_cdn_url(stored_path)

    return None
