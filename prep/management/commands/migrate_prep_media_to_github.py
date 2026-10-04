from pathlib import Path

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import OperationalError, close_old_connections

from prep.models import PrepContentCache, PrepDocument, PrepDocumentVisual
from services.github_media_storage import GitHubMediaStorage


class Command(BaseCommand):
    help = "Move existing Prep documents, visual crops, and cached note URLs to durable GitHub media storage."

    def handle(self, *args, **options):
        storage = GitHubMediaStorage()
        replacements = {}
        migrated = 0
        durable_prefix = f"{settings.GITHUB_UPLOAD_DIR.strip('/')}/prep-media/"

        document_ids = list(PrepDocument.objects.exclude(file="").values_list("pk", flat=True))
        for document_id in document_ids:
            close_old_connections()
            document = PrepDocument.objects.get(pk=document_id)
            old_name = document.file.name
            if old_name.startswith(durable_prefix):
                continue
            local_path = Path(settings.MEDIA_ROOT) / old_name
            if not local_path.is_file():
                self.stderr.write(f"Skipping missing document file: {old_name}")
                continue
            try:
                new_name = storage.save_existing(old_name, local_path.read_bytes())
            except Exception as exc:
                self.stderr.write(f"Skipping document upload {old_name}: {exc}")
                continue
            document.file.name = new_name
            self._save_with_retry(document, ["file", "updated_at"])
            replacements[f"{settings.MEDIA_URL}{old_name}"] = storage.url(new_name)
            migrated += 1

        visual_ids = list(PrepDocumentVisual.objects.values_list("pk", flat=True))
        for visual_id in visual_ids:
            close_old_connections()
            visual = PrepDocumentVisual.objects.get(pk=visual_id)
            for field_name in ("crop", "context_crop"):
                field = getattr(visual, field_name)
                if not field:
                    continue
                old_name = field.name
                if old_name.startswith(durable_prefix):
                    if "." not in Path(old_name).name:
                        try:
                            with storage._open(old_name, "rb") as source:
                                content_bytes = source.read()
                            new_name = storage.save_existing(f"visual-{visual.pk}-{field_name}.jpg", content_bytes)
                            replacements[f"/cdn/assets/{old_name.lstrip('/')}"] = f"/cdn/assets/{new_name}"
                            field.name = new_name
                            migrated += 1
                        except Exception as exc:
                            self.stderr.write(f"Could not add image extension to {old_name}: {exc}")
                    continue
                local_path = Path(settings.MEDIA_ROOT) / old_name
                if not local_path.is_file():
                    self.stderr.write(f"Skipping missing visual file: {old_name}")
                    continue
                try:
                    new_name = storage.save_existing(old_name, local_path.read_bytes())
                except Exception as exc:
                    self.stderr.write(f"Skipping visual upload {old_name}: {exc}")
                    continue
                field.name = new_name
                replacements[f"{settings.MEDIA_URL}{old_name}"] = storage.url(new_name)
                migrated += 1
            self._save_with_retry(visual, ["crop", "context_crop", "updated_at"])

        updated_caches = 0
        cache_ids = list(PrepContentCache.objects.filter(content_type="topic_notes").values_list("pk", flat=True))
        for cache_id in cache_ids:
            close_old_connections()
            cache = PrepContentCache.objects.get(pk=cache_id)
            self._add_cached_visual_replacements(cache.payload, replacements, storage)
            payload = self._replace(cache.payload, replacements)
            if payload != cache.payload:
                try:
                    cache.payload = payload
                    cache.save(update_fields=["payload", "updated_at"])
                    updated_caches += 1
                except OperationalError as exc:
                    self.stderr.write(f"Could not update note cache {cache_id}: {exc}")

        self.stdout.write(self.style.SUCCESS(
            f"Migrated {migrated} Prep media files and updated {updated_caches} note caches."
        ))

    def _add_cached_visual_replacements(self, value, replacements, storage):
        if isinstance(value, list):
            for item in value:
                self._add_cached_visual_replacements(item, replacements, storage)
            return
        if not isinstance(value, dict):
            return
        visual_id = value.get("visual_id")
        if visual_id:
            visual = PrepDocumentVisual.objects.filter(pk=visual_id).first()
            if visual and visual.crop:
                new_url = f"/cdn/assets/{visual.crop.name.lstrip('/')}"
                old_crop = str(value.get("crop") or "")
                old_url = str(value.get("crop_url") or "")
                if old_crop:
                    replacements[f"{settings.MEDIA_URL}{old_crop.lstrip('/')}"] = new_url
                if old_url:
                    replacements[old_url] = new_url
            if visual and visual.context_crop:
                new_context_url = f"/cdn/assets/{visual.context_crop.name.lstrip('/')}"
                old_context_url = str(value.get("context_crop_url") or "")
                if old_context_url:
                    replacements[old_context_url] = new_context_url
        for item in value.values():
            self._add_cached_visual_replacements(item, replacements, storage)

    def _save_with_retry(self, instance, update_fields):
        try:
            instance.save(update_fields=update_fields)
        except OperationalError:
            close_old_connections()
            instance.save(update_fields=update_fields)

    def _replace(self, value, replacements):
        if isinstance(value, str):
            for old, new in replacements.items():
                value = value.replace(old, new)
            return value
        if isinstance(value, list):
            return [self._replace(item, replacements) for item in value]
        if isinstance(value, dict):
            return {key: self._replace(item, replacements) for key, item in value.items()}
        return value
