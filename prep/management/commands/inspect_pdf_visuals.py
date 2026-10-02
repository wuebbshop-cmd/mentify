from django.core.management.base import BaseCommand, CommandError

from prep.models import PrepDocument, PrepDocumentVisual


class Command(BaseCommand):
    help = "Review or explicitly inspect captured PDF visual crops with the configured vision model."

    def add_arguments(self, parser):
        parser.add_argument("--document-id", required=True, help="PrepDocument UUID to inspect.")
        parser.add_argument("--execute", action="store_true", help="Call the paid vision API for the selected crops.")
        parser.add_argument("--max-candidates", type=int, default=3, help="Maximum crops to inspect (1-20).")

    def handle(self, *args, **options):
        max_candidates = options["max_candidates"]
        if not 1 <= max_candidates <= 20:
            raise CommandError("--max-candidates must be between 1 and 20.")
        try:
            document = PrepDocument.objects.get(pk=options["document_id"])
        except PrepDocument.DoesNotExist as exc:
            raise CommandError("PrepDocument was not found.") from exc

        candidates = list(
            PrepDocumentVisual.objects.filter(
                document=document,
                status__in=["candidate", "error"],
            ).order_by("page_number", "id")
        )
        candidates.sort(key=lambda item: (item.visual_type == "unclassified", item.page_number, item.id))
        candidates = candidates[:max_candidates]
        if not candidates:
            self.stdout.write("No uninspected visual candidates found.")
            return

        for candidate in candidates:
            self.stdout.write(
                f"page={candidate.page_number} type={candidate.visual_type} "
                f"bbox={candidate.bbox} status={candidate.status}"
            )
        if not options["execute"]:
            self.stdout.write(self.style.WARNING("Dry run only; no vision API call was made. Pass --execute to inspect these crops."))
            return

        from services.prep_ingestion import inspect_visual_candidate_with_vision

        completed = 0
        needs_review = 0
        for candidate in candidates:
            result = inspect_visual_candidate_with_vision(candidate)
            if result.get("success"):
                completed += 1
                if result.get("status") == "needs_review":
                    needs_review += 1
                    conflicts = "; ".join(result.get("source_conflicts", []))
                    self.stdout.write(self.style.WARNING(
                        f"Needs review on page {candidate.page_number}: {result['visual_type']} "
                        f"(confidence {result['confidence']:.2f}). {conflicts}"
                    ))
                else:
                    self.stdout.write(self.style.SUCCESS(
                        f"Inspected page {candidate.page_number}: {result['visual_type']} "
                        f"(confidence {result['confidence']:.2f})."
                    ))
            else:
                self.stderr.write(self.style.ERROR(
                    f"Page {candidate.page_number} inspection failed: {result.get('error')}"
                ))
        self.stdout.write(
            f"Completed {completed}/{len(candidates)} vision inspection(s); "
            f"{needs_review} require tutor review."
        )