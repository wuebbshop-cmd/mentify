"""
Management command: migrate_prep_media_to_r2

Migrates all existing Prep uploaded PDFs, visual crops, and PDF artifacts
from local disk / GitHub to Cloudflare R2.

Safe to run repeatedly - already-migrated files (keys starting with
`prep-pdfs/` or `prep-media/`) are skipped.

Usage:
    python manage.py migrate_prep_media_to_r2
    python manage.py migrate_prep_media_to_r2 --dry-run
"""
from __future__ import annotations

import hashlib
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import close_old_connections, OperationalError

from prep.models import PrepContentCache, PrepDocument, PrepDocumentVisual, PrepTopicPdfArtifact
from services.cloudflare_storage import CloudflareR2MediaStorage, is_cloudflare_r2_configured


class Command(BaseCommand):
    help = "Migrate existing Prep media and PDF artifacts from local disk / GitHub to Cloudflare R2."

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Scan what would be migrated without uploading or saving anything.",
        )

    def handle(self, *args, **options):
        dry_run = options["dry_run"]

        if not is_cloudflare_r2_configured():
            self.stderr.write(self.style.ERROR(
                "Cloudflare R2 is not configured. Set CF_Access_Key_ID, CF_Secret_Access_Key, "
                "and CF_Endpoint in your .env file."
            ))
            return

        if dry_run:
            self.stdout.write(self.style.WARNING("DRY RUN -- no files will be uploaded or records changed."))

        storage = CloudflareR2MediaStorage()
        migrated = 0
        skipped = 0
        errors = 0
        replacements: dict[str, str] = {}

        # --- 1. PrepDocument uploaded PDFs ------------------------------------
        self.stdout.write("\n[1/4] Migrating PrepDocument uploaded PDFs...")
        doc_ids = list(PrepDocument.objects.exclude(file="").values_list("pk", flat=True))
        for doc_id in doc_ids:
            close_old_connections()
            doc = PrepDocument.objects.get(pk=doc_id)
            old_name = doc.file.name
            if not old_name:
                continue

            # Already in R2 (key has no local path structure)
            if self._is_r2_key(old_name):
                skipped += 1
                continue

            local_path = Path(settings.MEDIA_ROOT) / old_name
            raw_bytes = None
            if local_path.is_file():
                raw_bytes = local_path.read_bytes()
            else:
                try:
                    from services.github_service import GitHubService
                    token = getattr(settings, "GITHUB_TOKEN", "").strip()
                    repo = getattr(settings, "GITHUB_REPO", "").strip()
                    branch = getattr(settings, "GITHUB_BRANCH", "main").strip() or "main"
                    if token and repo:
                        stored_path = f"github://{repo}/{branch}/{old_name.lstrip('/')}"
                        raw_bytes = GitHubService(token=token, repo_name=repo, branch=branch).download_file(stored_path)
                except Exception:
                    pass

            if not raw_bytes:
                self.stderr.write(f"  Skipping missing doc file: {old_name}")
                errors += 1
                continue

            base_name = Path(old_name).name
            safe_name = f"prep-media/{hashlib.sha256(raw_bytes).hexdigest()[:16]}-{base_name}"
            self.stdout.write(f"  Document {doc_id}: {old_name} -> {safe_name}")

            if not dry_run:
                try:
                    storage.save_existing(safe_name, raw_bytes)
                    old_url = f"{settings.MEDIA_URL}{old_name}"
                    replacements[old_url] = storage.url(safe_name)
                    doc.file.name = safe_name
                    doc.save(update_fields=["file"])
                    migrated += 1
                except Exception as exc:
                    self.stderr.write(f"  ERROR on doc {doc_id}: {exc}")
                    errors += 1
            else:
                migrated += 1

        # --- 2. PrepDocumentVisual crops --------------------------------------
        self.stdout.write("\n[2/4] Migrating PrepDocumentVisual image crops...")
        visual_ids = list(PrepDocumentVisual.objects.values_list("pk", flat=True))
        for visual_id in visual_ids:
            close_old_connections()
            visual = PrepDocumentVisual.objects.get(pk=visual_id)
            changed = False
            for field_name in ("crop", "context_crop"):
                field = getattr(visual, field_name)
                if not field or not field.name:
                    continue
                old_name = field.name
                if self._is_r2_key(old_name):
                    skipped += 1
                    continue

                local_path = Path(settings.MEDIA_ROOT) / old_name
                raw_bytes = None
                if local_path.is_file():
                    raw_bytes = local_path.read_bytes()
                else:
                    try:
                        from services.github_service import GitHubService
                        token = getattr(settings, "GITHUB_TOKEN", "").strip()
                        repo = getattr(settings, "GITHUB_REPO", "").strip()
                        branch = getattr(settings, "GITHUB_BRANCH", "main").strip() or "main"
                        if token and repo:
                            stored_path = f"github://{repo}/{branch}/{old_name.lstrip('/')}"
                            raw_bytes = GitHubService(token=token, repo_name=repo, branch=branch).download_file(stored_path)
                    except Exception:
                        pass

                if not raw_bytes:
                    self.stderr.write(f"  Skipping missing visual file: {old_name}")
                    errors += 1
                    continue

                ext = Path(old_name).suffix or ".jpg"
                safe_name = f"prep-media/{hashlib.sha256(raw_bytes).hexdigest()[:16]}-visual-{visual_id}-{field_name}{ext}"
                self.stdout.write(f"  Visual {visual_id} ({field_name}): {old_name} -> {safe_name}")

                if not dry_run:
                    try:
                        storage.save_existing(safe_name, raw_bytes)
                        old_url = f"{settings.MEDIA_URL}{old_name}"
                        replacements[old_url] = storage.url(safe_name)
                        field.name = safe_name
                        changed = True
                        migrated += 1
                    except Exception as exc:
                        self.stderr.write(f"  ERROR on visual {visual_id} {field_name}: {exc}")
                        errors += 1
                else:
                    migrated += 1

            if changed and not dry_run:
                try:
                    visual.save(update_fields=["crop", "context_crop"])
                except OperationalError as exc:
                    self.stderr.write(f"  Could not save visual {visual_id}: {exc}")

        # --- 3. PrepTopicPdfArtifact (ready) -- migrate GitHub paths -----------
        self.stdout.write("\n[3/4] Migrating ready PDF artifacts from GitHub to R2...")
        artifact_ids = list(
            PrepTopicPdfArtifact.objects.filter(status="ready")
            .exclude(github_path="")
            .values_list("pk", flat=True)
        )
        for art_id in artifact_ids:
            close_old_connections()
            artifact = PrepTopicPdfArtifact.objects.get(pk=art_id)
            old_path = artifact.github_path
            if not old_path:
                continue
            if self._is_r2_key(old_path):
                skipped += 1
                continue

            self.stdout.write(f"  Artifact {art_id}: {old_path}")

            if not dry_run:
                try:
                    from services.github_service import GitHubService
                    token = getattr(settings, "GITHUB_TOKEN", "").strip()
                    repo = getattr(settings, "GITHUB_REPO", "").strip()
                    branch = getattr(settings, "GITHUB_BRANCH", "main").strip() or "main"
                    if not token or not repo:
                        self.stderr.write(f"  No GitHub token; skipping artifact {art_id}")
                        errors += 1
                        continue
                    stored_path = f"github://{repo}/{branch}/{old_path.lstrip('/')}"
                    pdf_bytes = GitHubService(token=token, repo_name=repo, branch=branch).download_file(stored_path)
                    if not pdf_bytes or not pdf_bytes[:4] == b"%PDF":
                        self.stderr.write(f"  Invalid PDF from GitHub for artifact {art_id}; skipping.")
                        errors += 1
                        continue

                    # Store at same key without the upload_dir prefix
                    r2_key = old_path
                    for strip_prefix in ("mentify-uploads/", "uploads/"):
                        if r2_key.startswith(strip_prefix):
                            r2_key = r2_key[len(strip_prefix):]
                            break

                    storage.save_existing(r2_key, pdf_bytes, content_type="application/pdf")
                    artifact.github_path = r2_key
                    artifact.save(update_fields=["github_path"])
                    migrated += 1
                except Exception as exc:
                    self.stderr.write(f"  ERROR on artifact {art_id}: {exc}")
                    errors += 1
            else:
                migrated += 1

        # --- 4. Update note cache URL references ------------------------------
        if replacements and not dry_run:
            self.stdout.write(f"\n[4/4] Updating {len(replacements)} URL references in note caches...")
            cache_ids = list(PrepContentCache.objects.filter(content_type="topic_notes").values_list("pk", flat=True))
            updated_caches = 0
            for cache_id in cache_ids:
                close_old_connections()
                cache_entry = PrepContentCache.objects.get(pk=cache_id)
                new_payload = self._replace_in_dict(cache_entry.payload, replacements)
                if new_payload != cache_entry.payload:
                    try:
                        cache_entry.payload = new_payload
                        cache_entry.save(update_fields=["payload"])
                        updated_caches += 1
                    except OperationalError as exc:
                        self.stderr.write(f"  Could not update cache {cache_id}: {exc}")
            self.stdout.write(f"  Updated {updated_caches} note caches.")
        else:
            self.stdout.write("\n[4/4] Skipping cache URL update (no replacements or dry run).")

        self.stdout.write(self.style.SUCCESS(
            f"\n{'[DRY RUN] Would migrate' if dry_run else 'Migrated'} {migrated} files, "
            f"skipped {skipped} already-migrated, {errors} errors."
        ))

    def _is_r2_key(self, name: str) -> bool:
        """
        Return True if this path is already an R2 key (no local disk-path prefix).
        Local paths: `prep/documents/...`, `prep/visual-crops/...`
        GitHub legacy: `mentify-uploads/...`, `uploads/...`
        R2 keys: `prep-media/...`, `prep-pdfs/...`
        """
        for r2_prefix in ("prep-media/", "prep-pdfs/"):
            if name.startswith(r2_prefix):
                return True
        return False

    def _replace_in_dict(self, value, replacements: dict):
        if isinstance(value, dict):
            return {k: self._replace_in_dict(v, replacements) for k, v in value.items()}
        if isinstance(value, list):
            return [self._replace_in_dict(item, replacements) for item in value]
        if isinstance(value, str):
            for old, new in replacements.items():
                value = value.replace(old, new)
            return value
        return value
