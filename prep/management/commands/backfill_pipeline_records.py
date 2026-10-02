import json

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone

from prep.document_validation import validate_prep_document
from prep.models import PrepContentCache, PrepCourse, PrepDocument, PrepQuestion
from services.prep_ai_router import (
    ANSWER_VALIDATION_VERSION,
    NOTE_VALIDATION_STATE,
    _approved_course_source_references,
    _note_completion_issues,
    _note_validation_options,
    _topic_notes_cache_signature,
)


class Command(BaseCommand):
    help = "Safely backfill legacy validation/provenance records without provider calls."

    def add_arguments(self, parser):
        parser.add_argument("--course-code", action="append", dest="course_codes")
        parser.add_argument("--apply", action="store_true", help="Persist deterministic repairs; defaults to dry run.")
        parser.add_argument("--json", action="store_true", help="Emit the result as JSON.")

    def _courses(self, codes):
        courses = PrepCourse.objects.all().order_by("code")
        if codes:
            courses = courses.filter(code__in=codes)
            found = set(courses.values_list("code", flat=True))
            missing = [code for code in codes if code not in found]
            if missing:
                raise CommandError(f"Course(s) not found: {', '.join(missing)}")
        return courses

    def handle(self, *args, **options):
        apply = options["apply"]
        report = {
            "schema_version": 1,
            "mode": "apply" if apply else "dry_run",
            "provider_calls": 0,
            "documents_validated": 0,
            "document_reports_written": 0,
            "adaptations_enriched": 0,
            "adaptations_quarantined": 0,
            "note_caches_validated": 0,
            "note_caches_quarantined": 0,
            "answer_caches_quarantined": 0,
            "risks": [],
        }

        for course in self._courses(options.get("course_codes") or []):
            documents = list(course.documents.all())
            questions = list(
                PrepQuestion.objects.filter(paper__course=course).select_related(
                    "paper__source_document", "source_document", "reconstructed_from"
                )
            )
            questions += list(
                PrepQuestion.objects.filter(paper__isnull=True, topic__course=course).select_related(
                    "source_document", "reconstructed_from"
                )
            )

            for document in documents:
                report["documents_validated"] += 1
                validation = validate_prep_document(document)
                if not document.validation_report:
                    report["document_reports_written"] += 1
                if apply:
                    document.validation_report = validation
                    document.save(update_fields=["validation_report", "updated_at"])

            for question in questions:
                if question.question_type != "adapted":
                    continue
                metadata = question.reconstruction_metadata if isinstance(question.reconstruction_metadata, dict) else {}
                original = question.reconstructed_from
                source_document = question.source_document
                source_page = question.source_page_number
                if original:
                    source_document = source_document or original.source_document
                    source_page = source_page or original.source_page_number
                    enriched = {
                        **metadata,
                        "source_question_id": str(original.pk),
                        "source_document_id": str(source_document.pk) if source_document else None,
                        "source_page_number": source_page,
                        "original_transcription": metadata.get("original_transcription") or original.question_latex,
                        "review_status": metadata.get("review_status") or "pending",
                    }
                    needs_write = (
                        question.source_document_id != (source_document.pk if source_document else None)
                        or question.source_page_number != source_page
                        or enriched != metadata
                    )
                    if needs_write:
                        report["adaptations_enriched"] += 1
                        if apply:
                            question.source_document = source_document
                            question.source_page_number = source_page
                            question.reconstruction_metadata = enriched
                            question.save(update_fields=[
                                "source_document", "source_page_number", "reconstruction_metadata", "updated_at",
                            ])
                elif question.verification_status in PrepQuestion.LEARNER_VISIBLE_STATUSES:
                    report["adaptations_quarantined"] += 1
                    if apply:
                        question.verification_status = "pending"
                        question.reconstruction_metadata = {
                            **metadata,
                            "review_status": "needs_review",
                            "reason": "Legacy adapted question has no source-question link; provenance cannot be inferred safely.",
                        }
                        question.save(update_fields=["verification_status", "reconstruction_metadata"])

            caches = PrepContentCache.objects.filter(course=course).select_related("topic")
            for cache in caches:
                payload = cache.payload if isinstance(cache.payload, dict) else {}
                if cache.content_type == "topic_notes" and cache.topic:
                    options = _note_validation_options(
                        course,
                        cache.topic.title,
                        cache.topic.summary,
                        cache.topic.subtopics,
                        topic_obj=cache.topic,
                    )
                    issues = _note_completion_issues(
                        str(payload.get("content") or ""),
                        cache.topic.title,
                        **options,
                    )
                    updated = dict(payload)
                    if not issues:
                        updated.update({
                            "validation_state": NOTE_VALIDATION_STATE,
                            "validated_at": timezone.now().isoformat(),
                            "source_references": options["source_references"],
                            "source_signature": _topic_notes_cache_signature(
                                course, cache.topic, cache.topic.title, cache.topic.subtopics
                            ),
                        })
                        report["note_caches_validated"] += 1
                    else:
                        updated.update({"validation_state": "needs_review", "validation_issues": issues})
                        report["note_caches_quarantined"] += 1
                    if apply and updated != payload:
                        cache.payload = updated
                        cache.save(update_fields=["payload", "updated_at"])
                elif cache.content_type == "solution_derivation":
                    if payload.get("answer_validation_version") != ANSWER_VALIDATION_VERSION:
                        report["answer_caches_quarantined"] += 1
                        if apply:
                            updated = dict(payload)
                            updated["validation_state"] = "needs_review"
                            updated["validation_issues"] = ["Legacy answer cache lacks current provenance/validator metadata."]
                            cache.payload = updated
                            cache.save(update_fields=["payload", "updated_at"])

        if options.get("json", False):
            self.stdout.write(json.dumps(report, ensure_ascii=True, sort_keys=True))
            return
        if not apply:
            self.stdout.write("DRY RUN: no records changed and no provider calls made.")
        self.stdout.write(json.dumps(report, ensure_ascii=True, sort_keys=True))
