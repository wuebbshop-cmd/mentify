"""
Cloudflare R2 Object Storage Backend for Mentify Prep.

Handles:
- Uploaded course and document PDFs (PrepDocument)
- Extracted visual crops and diagrams (PrepDocumentVisual)
- Generated topic notes and questions PDFs (PrepTopicPdfArtifact)

Provides high-performance, S3-compatible cloud storage using Cloudflare R2
with zero egress fees and global edge delivery.
"""
from __future__ import annotations

import logging
import mimetypes
import os
from io import BytesIO
from urllib.parse import quote, urlparse
from typing import Optional

import boto3
from botocore.config import Config
from botocore.exceptions import ClientError
from django.conf import settings
from django.core.files.base import File
from django.core.files.storage import Storage

logger = logging.getLogger(__name__)


def get_cloudflare_r2_config() -> dict[str, str]:
    """Resolve Cloudflare R2 configuration from Django settings or environment variables."""
    access_key = (
        getattr(settings, "CF_ACCESS_KEY_ID", "")
        or os.environ.get("CF_Access_Key_ID")
        or os.environ.get("CF_ACCESS_KEY_ID")
        or os.environ.get("CD_Access_Key_ID")
        or os.environ.get("CD_ACCESS_KEY_ID")
        or ""
    ).strip()

    secret_key = (
        getattr(settings, "CF_SECRET_ACCESS_KEY", "")
        or os.environ.get("CF_Secret_Access_Key")
        or os.environ.get("CF_SECRET_ACCESS_KEY")
        or os.environ.get("CD_Secret_Access_Key")
        or os.environ.get("CD_SECRET_ACCESS_KEY")
        or ""
    ).strip()

    raw_endpoint = (
        getattr(settings, "CF_ENDPOINT", "")
        or os.environ.get("CF_Endpoint")
        or os.environ.get("CF_ENDPOINT")
        or os.environ.get("CD_Endpoint")
        or os.environ.get("CD_ENDPOINT")
        or ""
    ).strip()

    bucket_name = (
        getattr(settings, "CF_BUCKET_NAME", "")
        or os.environ.get("CF_BUCKET_NAME")
        or os.environ.get("CF_Bucket")
        or os.environ.get("CD_BUCKET_NAME")
        or os.environ.get("CD_Bucket")
        or ""
    ).strip()

    public_url = (
        getattr(settings, "CF_PUBLIC_URL", "")
        or os.environ.get("CF_PUBLIC_URL")
        or os.environ.get("CD_PUBLIC_URL")
        or ""
    ).strip().rstrip("/")

    # Parse endpoint URL and bucket if bucket was embedded in endpoint path
    # e.g., https://<account_id>.r2.cloudflarestorage.com/mentify
    endpoint_url = raw_endpoint
    if raw_endpoint:
        parsed = urlparse(raw_endpoint)
        endpoint_url = f"{parsed.scheme}://{parsed.netloc}"
        if not bucket_name and parsed.path.strip("/"):
            bucket_name = parsed.path.strip("/")

    if not bucket_name:
        bucket_name = "mentify"

    return {
        "access_key": access_key,
        "secret_key": secret_key,
        "endpoint_url": endpoint_url,
        "bucket_name": bucket_name,
        "public_url": public_url,
    }


def is_cloudflare_r2_configured() -> bool:
    """Return True if required Cloudflare R2 credentials are present."""
    cfg = get_cloudflare_r2_config()
    return bool(cfg["access_key"] and cfg["secret_key"] and cfg["endpoint_url"])


class CloudflareR2MediaStorage(Storage):
    """
    Django Storage backend for Cloudflare R2 S3-compatible Object Storage.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config = get_cloudflare_r2_config()
        self.bucket = self.config["bucket_name"]
        self.endpoint_url = self.config["endpoint_url"]
        self.public_url = self.config["public_url"]
        self._s3_client = None

    def _get_client(self):
        if self._s3_client is None:
            if not self.config["access_key"] or not self.config["secret_key"]:
                raise RuntimeError(
                    "Cloudflare R2 credentials are not configured. Check CF_Access_Key_ID and CF_Secret_Access_Key."
                )
            self._s3_client = boto3.client(
                "s3",
                endpoint_url=self.endpoint_url,
                aws_access_key_id=self.config["access_key"],
                aws_secret_access_key=self.config["secret_key"],
                region_name="auto",
                config=Config(
                    signature_version="s3v4",
                    retries={"max_attempts": 5, "mode": "standard"},
                    connect_timeout=15,
                    read_timeout=60,
                ),
            )
        return self._s3_client

    def _clean_key(self, name: str) -> str:
        """Sanitize and normalize storage key path."""
        if not name:
            return ""
        clean = str(name).replace("\\", "/").strip("/")
        # Strip common local prefixes if present
        for prefix in ("media/", "cdn/cloudflare/", "cdn/assets/"):
            if clean.startswith(prefix):
                clean = clean[len(prefix):]
        return clean

    def _guess_content_type(self, name: str) -> str:
        content_type, _ = mimetypes.guess_type(name)
        return content_type or "application/octet-stream"

    def _save(self, name: str, content) -> str:
        key = self._clean_key(name)
        content_bytes = content.read() if hasattr(content, "read") else content
        content_type = self._guess_content_type(key)

        client = self._get_client()
        client.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=content_bytes,
            ContentType=content_type,
        )
        logger.info("Uploaded to Cloudflare R2: %s (size: %s bytes)", key, len(content_bytes))
        return key

    def save_existing(self, name: str, content_bytes: bytes, content_type: Optional[str] = None) -> str:
        """Upload raw bytes to a specific key in R2."""
        key = self._clean_key(name)
        ct = content_type or self._guess_content_type(key)
        client = self._get_client()
        client.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=content_bytes,
            ContentType=ct,
        )
        return key

    def _open(self, name: str, mode: str = "rb") -> File:
        if "b" not in mode:
            raise ValueError("CloudflareR2MediaStorage only supports binary reads.")
        key = self._clean_key(name)
        client = self._get_client()
        try:
            response = client.get_object(Bucket=self.bucket, Key=key)
            body = response["Body"].read()
            return File(BytesIO(body), name=key)
        except ClientError as exc:
            code = exc.response.get("Error", {}).get("Code", "")
            if code in ("NoSuchKey", "404"):
                raise FileNotFoundError(f"File not found in Cloudflare R2: {key}") from exc
            raise

    def download_bytes(self, name: str) -> bytes:
        """Read and return full binary content of an object."""
        key = self._clean_key(name)
        client = self._get_client()
        response = client.get_object(Bucket=self.bucket, Key=key)
        return response["Body"].read()

    def upload_bytes(self, name: str, content_bytes: bytes, content_type: Optional[str] = None) -> str:
        """Upload binary content and return the key."""
        return self.save_existing(name, content_bytes, content_type)

    def delete(self, name: str) -> None:
        if not name:
            return
        key = self._clean_key(name)
        client = self._get_client()
        try:
            client.delete_object(Bucket=self.bucket, Key=key)
            logger.info("Deleted from Cloudflare R2: %s", key)
        except ClientError as exc:
            logger.warning("Failed to delete %s from Cloudflare R2: %s", key, exc)

    def exists(self, name: str) -> bool:
        if not name:
            return False
        key = self._clean_key(name)
        client = self._get_client()
        try:
            client.head_object(Bucket=self.bucket, Key=key)
            return True
        except ClientError as exc:
            code = exc.response.get("Error", {}).get("Code", "")
            if code in ("NoSuchKey", "404"):
                return False
            raise

    def size(self, name: str) -> int:
        key = self._clean_key(name)
        client = self._get_client()
        response = client.head_object(Bucket=self.bucket, Key=key)
        return int(response.get("ContentLength", 0))

    def url(self, name: str) -> str:
        """
        Return public access URL for this object.
        If a custom public domain or R2 public dev URL is configured, use it directly.
        Otherwise, route through the high-performance cached proxy view `/cdn/cloudflare/<filepath>`.
        """
        if not name:
            return ""
        value = str(name)
        if value.startswith(("http://", "https://")):
            return value

        clean_key = self._clean_key(value)
        if self.public_url:
            return f"{self.public_url}/{quote(clean_key, safe='/')}"

        return f"/cdn/cloudflare/{quote(clean_key, safe='/')}"

    def get_presigned_url(self, name: str, expires_in: int = 3600) -> str:
        """Generate a presigned GET URL valid for `expires_in` seconds."""
        key = self._clean_key(name)
        client = self._get_client()
        return client.generate_presigned_url(
            "get_object",
            Params={"Bucket": self.bucket, "Key": key},
            ExpiresIn=expires_in,
        )
