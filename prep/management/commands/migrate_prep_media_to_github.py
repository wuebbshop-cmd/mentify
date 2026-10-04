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

        for document in PrepDocument.objects.exclude(file="").iterator():
            old_name = document.file.name
            if old_name.startswith(durable_prefix):
                continue
            local_path = Path(settings.MEDIA_ROOT) / old_name
            if not local_path.is_file():
                self.stderr.write(f"Skipping missing document file: {old_name}")
                continue
            new_name = storage.save(old_name, ContentFile(local_path.read_bytes()))
            document.file.name = new_name
            self._save_with_retry(document, ["file", "updated_at"])
            replacements[f"{settings.MEDIA_URL}{old_name}"] = storage.url(new_name)
            migrated += 1

        for visual in PrepDocumentVisual.objects.all().iterator():
            for field_name in ("crop", "context_crop"):
                field = getattr(visual, field_name)
                if not field:
                    continue
                old_name = field.name
                if old_name.startswith(durable_prefix):
                    continue
                local_path = Path(settings.MEDIA_ROOT) / old_name
                if not local_path.is_file():
                    self.stderr.write(f"Skipping missing visual file: {old_name}")
                    continue
                new_name = storage.save(old_name, ContentFile(local_path.read_bytes()))
                field.name = new_name
                replacements[f"{settings.MEDIA_URL}{old_name}"] = storage.url(new_name)
                migrated += 1
            self._save_with_retry(visual, ["crop", "context_crop", "updated_at"])

        updated_caches = 0
        for cache in PrepContentCache.objects.filter(content_type="topic_notes").iterator():
            payload = self._replace(cache.payload, replacements)
            if payload != cache.payload:
                cache.payload = payload
                cache.save(update_fields=["payload", "updated_at"])
                updated_caches += 1

        self.stdout.write(self.style.SUCCESS(
            f"Migrated {migrated} Prep media files and updated {updated_caches} note caches."
        ))

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
