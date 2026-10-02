from django.core.management.base import BaseCommand, CommandError

from prep.models import PrepDocument, PrepDocumentVisual
from prep.visual_reconstruction import (
    build_visual_reconstruction_spec,
    store_visual_reconstruction_proposal,
)


class Command(BaseCommand):
    help = "Prepare provenance-linked reconstruction proposals from tutor-approved visuals."

    def add_arguments(self, parser):
        parser.add_argument("--document-id", required=True, help="PrepDocument ID to process.")
        parser.add_argument("--execute", action="store_true", help="Persist proposals; defaults to dry run.")
        parser.add_argument("--max-candidates", type=int, default=20, help="Maximum approved visuals to process (1-200).")

    def handle(self, *args, **options):
        max_candidates = options["max_candidates"]
        if not 1 <= max_candidates <= 200:
            raise CommandError("--max-candidates must be between 1 and 200.")
        try:
            document = PrepDocument.objects.get(pk=options["document_id"])
        except PrepDocument.DoesNotExist as exc:
            raise CommandError("PrepDocument was not found.") from exc

        candidates = list(
            PrepDocumentVisual.objects.filter(document=document, status="approved")
            .order_by("page_number", "id")[:max_candidates]
        )
        if not candidates:
            self.stdout.write("No tutor-approved visual candidates found.")
            return

        execute = options["execute"]
        for candidate in candidates:
            proposal = (
                store_visual_reconstruction_proposal(candidate)
                if execute
                else build_visual_reconstruction_spec(candidate)
            )
            message = (
                f"page={candidate.page_number} type={candidate.visual_type} "
                f"decision={proposal['status']} reason={proposal['reason']}"
            )
            if proposal["status"] == "ready":
                self.stdout.write(self.style.SUCCESS(message))
            else:
                self.stdout.write(self.style.WARNING(message))

        if not execute:
            self.stdout.write(self.style.WARNING("Dry run only; no proposal was saved. Pass --execute to persist decisions."))