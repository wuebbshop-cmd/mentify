import sys
from django.core.management.base import BaseCommand
from django.db import transaction

from prep.models import PrepQuestion


class Command(BaseCommand):
    help = "Safely purge orphaned unlinked legacy questions created during earlier pre-Stage 3 testing."

    def add_arguments(self, parser):
        parser.add_argument(
            "--apply",
            action="store_true",
            help="Commit changes to the database. Defaults to dry-run.",
        )

    def handle(self, *args, **options):
        apply = options["apply"]

        orphaned_ids = list(
            PrepQuestion.objects.filter(
                source_document__isnull=True,
                question_type__in=["authentic", "adapted"],
            )
            .exclude(verification_status="verified")
            .values_list("id", flat=True)
        )
        orphaned_count = len(orphaned_ids)

        referencing_children = PrepQuestion.objects.filter(
            reconstructed_from_id__in=orphaned_ids
        )
        child_count = referencing_children.count()

        sys.stdout.write(
            f"Found {orphaned_count} unlinked legacy question(s) without source documents.\n"
        )
        sys.stdout.write(
            f"Found {child_count} active question(s) with provenance pointing to these legacy rows.\n"
        )
        sys.stdout.flush()

        if not apply:
            sys.stdout.write("DRY RUN: No database changes applied. Use --apply to execute.\n")
            sys.stdout.flush()
            return

        with transaction.atomic():
            if child_count > 0:
                referencing_children.update(reconstructed_from=None)
                sys.stdout.write(f"Safely detached provenance for {child_count} child question(s).\n")
                sys.stdout.flush()

            deleted_count, _ = PrepQuestion.objects.filter(id__in=orphaned_ids).delete()
            sys.stdout.write(
                f"Successfully purged {deleted_count} orphaned legacy question record(s).\n"
            )
            sys.stdout.flush()
