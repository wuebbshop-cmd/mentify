"""Bunny Stream upload helper."""
from __future__ import annotations

from dataclasses import dataclass

import requests


@dataclass(slots=True)
class BunnyVideoUploadResult:
    video_id: str
    library_id: str


class BunnyStreamService:
    """Create Bunny Stream videos and upload binary content."""

    base_url = "https://video.bunnycdn.com"

    def __init__(self, library_id: str, api_key: str) -> None:
        self.library_id = str(library_id or "").strip()
        self.api_key = (api_key or "").strip()
        if not self.library_id or not self.api_key:
            raise ValueError("BUNNY_STREAM_LIBRARY_ID and BUNNY_STREAM_API_KEY are required.")

    @property
    def headers(self) -> dict[str, str]:
        return {"AccessKey": self.api_key}

    def create_video(self, title: str) -> str:
        response = requests.post(
            f"{self.base_url}/library/{self.library_id}/videos",
            headers={**self.headers, "Content-Type": "application/json"},
            json={"title": title or "Lesson video"},
            timeout=30,
        )
        if response.status_code >= 300:
            raise RuntimeError(f"Bunny video creation failed: {response.status_code} {response.text}")
        video_id = response.json().get("guid")
        if not video_id:
            raise RuntimeError("Bunny video creation did not return a video GUID.")
        return video_id

    def upload_video_file(self, video_id: str, file_obj) -> None:
        try:
            file_obj.seek(0)
        except Exception:
            pass
        response = requests.put(
            f"{self.base_url}/library/{self.library_id}/videos/{video_id}",
            headers={**self.headers, "Content-Type": "application/octet-stream"},
            data=file_obj.chunks() if hasattr(file_obj, "chunks") else file_obj,
            timeout=600,
        )
        if response.status_code >= 300:
            raise RuntimeError(f"Bunny video upload failed: {response.status_code} {response.text}")

    def upload(self, title: str, file_obj) -> BunnyVideoUploadResult:
        video_id = self.create_video(title)
        self.upload_video_file(video_id, file_obj)
        return BunnyVideoUploadResult(video_id=video_id, library_id=self.library_id)
