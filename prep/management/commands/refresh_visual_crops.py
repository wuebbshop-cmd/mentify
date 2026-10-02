from pathlib import Path

import fitz
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.core.management.base import BaseCommand, CommandError

from prep.models import PrepDocument, PrepDocumentVisual
from services.prep_ingestion import VISUAL_CROP_VERSION, inspect_pdf_visual_candidates


class Command(BaseCommand):
    help = "Refresh stored vector-figure crops so labels outside drawn strokes remain visible."

    def add_arguments(self, parser):
        target = parser.add_mutually_exclusive_group(required=True)
        target.add_argument("--course-code", help="Refresh crops for every source document in this course.")
        target.add_argument("--document-id", help="Refresh crops for one PrepDocument UUID.")
        parser.add_argument("--apply", action="store_true", help="Write refreshed crop files; otherwise report a dry run.")

    def handle(self, *args, **options):
        documents = PrepDocument.objects.filter(visual_candidates__isnull=False)
        if options.get("course_code"):
            documents = documents.filter(course__code=options["course_code"])
        else:
            documents = documents.filter(pk=options["document_id"])
        documents = documents.distinct().order_by("course__code", "id")
        if not documents.exists():
            raise CommandError("No documents with visual candidates matched the requested target.")

        refreshed = 0
        skipped = 0
        for document in documents:
            try:
                with document.file.open("rb") as source_file:
                    pdf_bytes = source_file.read()
                _, extracted_candidates = inspect_pdf_visual_candidates(pdf_bytes)
            except Exception as exc:
                raise CommandError(f"Could not open source PDF for document {document.pk}: {exc}") from exc

            current_by_page = {}
            for visual in PrepDocumentVisual.objects.filter(document=document).exclude(crop="").order_by("page_number", "id"):
                if "vector_drawing_cluster" in (visual.candidate_reasons or []):
                    current_by_page.setdefault(visual.page_number, []).append(visual)
            source_by_page = {}
            for candidate in extracted_candidates:
                if "vector_drawing_cluster" in (candidate.get("candidate_reasons") or []):
                    source_by_page.setdefault(candidate["page_number"], []).append(candidate)

            for page_number, visuals in current_by_page.items():
                source_candidates = source_by_page.get(page_number, [])
                if len(visuals) != len(source_candidates):
                    skipped += len(visuals)
                    self.stderr.write(self.style.WARNING(
                        f"{document.course.code} page {page_number}: current/source figure counts differ "
                        f"({len(visuals)} vs {len(source_candidates)}); skipped to preserve assignments."
                    ))
                    continue

                visuals.sort(key=lambda item: (item.bbox[1], item.bbox[0], item.pk))
                source_candidates.sort(key=lambda item: (item["bbox"][1], item["bbox"][0]))

                for visual, candidate in zip(visuals, source_candidates):
                    metadata = dict(visual.extracted_content) if isinstance(visual.extracted_content, dict) else {}
                    if metadata.get("crop_refinement_version") == VISUAL_CROP_VERSION:
                        skipped += 1
                        continue
                    crop_bytes = candidate["crop_bytes"]
                    context_crop_bytes = candidate.get("context_crop_bytes")
                    metadata["crop_refinement_version"] = VISUAL_CROP_VERSION
                    metadata["context_before"] = candidate.get("context_before", "")
                    metadata["context_after"] = candidate.get("context_after", "")

                    if options["apply"]:
                        storage = visual.crop.storage
                        if isinstance(storage, FileSystemStorage):
                            with storage.open(visual.crop.name, "wb") as destination:
                                destination.write(crop_bytes)
                        else:
                            refined_name = f"{Path(visual.crop.name).stem}-{VISUAL_CROP_VERSION}.jpg"
                            visual.crop.save(refined_name, ContentFile(crop_bytes), save=False)
                        if context_crop_bytes:
                            context_storage = visual.context_crop.storage if visual.context_crop else storage
                            if visual.context_crop and isinstance(context_storage, FileSystemStorage):
                                with context_storage.open(visual.context_crop.name, "wb") as destination:
                                    destination.write(context_crop_bytes)
                            else:
                                context_name = f"{Path(visual.context_crop.name or visual.crop.name).stem}-{VISUAL_CROP_VERSION}-context.jpg"
                                visual.context_crop.save(context_name, ContentFile(context_crop_bytes), save=False)
                        visual.bbox = candidate["bbox"]
                        visual.context_text = candidate.get("context_text", visual.context_text)
                        visual.extracted_content = metadata
                        visual.save(update_fields=["crop", "context_crop", "bbox", "context_text", "extracted_content", "updated_at"])
                    refreshed += 1
                    self.stdout.write(
                        f"{document.course.code} page {visual.page_number}: "
                        f"{'refreshed' if options['apply'] else 'would refresh'}"
                    )

        action = "Refreshed" if options["apply"] else "Would refresh"
        self.stdout.write(f"{action} {refreshed} vector crops; skipped {skipped}.")