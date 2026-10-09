import re
from collections import Counter

from django.core.management.base import BaseCommand
from django.db.models import Q

from prep.models import PrepQuestion
from services.prep_ingestion import (
    _AUTO_RECONSTRUCTION_CONFIDENCE_THRESHOLD,
    _strip_assessment_document_footers,
    _strip_safe_question_extraction_artifacts,
    assessment_question_rendering_issues,
    extract_assessment_questions,
)


def _normalise_label(value):
    return " ".join(re.findall(r"[a-z0-9]+", str(value or "").casefold()))


def _resolve_topic(question, course):
    if question.topic_id and question.topic.course_id == course.id:
        return question.topic

    label = _normalise_label(question.topic_label)
    if not label:
        return None

    for topic in course.topics.all():
        labels = [topic.title]
        if isinstance(topic.subtopics, list):
            labels.extend(topic.subtopics)
        if any(_normalise_label(item) == label for item in labels):
            return topic
    from services.prep_ingestion import _topic_match_for_question

    return _topic_match_for_question(course, question.question_latex)


def _clean_indexed_duplicate(question):
    """Find a clean same-page question that already covers a damaged duplicate."""
    source_document = question.source_document or (
        question.paper.source_document if question.paper_id else None
    )
    if source_document is None or question.source_page_number is None or question.paper_id is None:
        return None

    source_questions = [
        item
        for item in extract_assessment_questions(source_document.extracted_text or "")
        if item["number"] == question.number
        and item["source_page_number"] == question.source_page_number
    ]
    source_token_counters = [
        Counter(re.findall(r"[a-z0-9]+", item["question_latex"].casefold()))
        for item in source_questions
    ]
    if not source_token_counters:
        return None

    candidates = PrepQuestion.objects.filter(
        paper_id=question.paper_id,
        source_document=source_document,
        source_page_number=question.source_page_number,
        question_type="authentic",
        number=question.number,
        verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
    ).exclude(pk=question.pk)
    for candidate in candidates:
        candidate_text = _strip_assessment_document_footers(candidate.question_latex)
        if assessment_question_rendering_issues(candidate_text):
            continue
        candidate_tokens = Counter(re.findall(r"[a-z0-9]+", candidate_text.casefold()))
        candidate_token_count = sum(candidate_tokens.values())
        if candidate_token_count < 30:
            continue
        for source_tokens in source_token_counters:
            if sum(source_tokens.values()) == 0:
                continue
            overlap = sum((candidate_tokens & source_tokens).values())
            if overlap / candidate_token_count >= 0.95:
                return candidate
    return None


class Command(BaseCommand):
    help = "Audit existing authentic questions and reconstruct flagged or malformed rows."

    def add_arguments(self, parser):
        parser.add_argument("--course-code", help="Limit the audit to one course code.")
        parser.add_argument("--question-id", type=int, help="Limit repair to one question record ID.")
        parser.add_argument(
            "--limit",
            type=int,
            default=0,
            help="Maximum candidate rows to inspect; 0 processes all candidates (default: 0).",
        )
        parser.add_argument(
            "--apply",
            action="store_true",
            help="Use the AI to reconstruct flagged items and publish only validated, high-confidence results.",
        )
        parser.add_argument(
            "--retry-pending",
            action="store_true",
            help="Make one deliberate AI retry for valid existing adaptations below the confidence threshold.",
        )
        parser.add_argument(
            "--deterministic-only",
            action="store_true",
            help="Remove only unambiguous extraction debris and flag other invalid visible rows; never call AI.",
        )

    def handle(self, *args, **options):
        deterministic_only = options["deterministic_only"]
        question_types = ("authentic", "adapted") if deterministic_only else ("authentic",)
        questions = PrepQuestion.objects.filter(question_type__in=question_types).select_related(
            "paper__course", "topic__course"
        ).order_by("id")
        course_code = options.get("course_code")
        if course_code:
            questions = questions.filter(
                Q(paper__course__code__iexact=course_code)
                | Q(topic__course__code__iexact=course_code)
            )
        question_id = options.get("question_id")
        if question_id:
            questions = questions.filter(pk=question_id)

        candidates = []
        for question in questions.iterator():
            if deterministic_only and question.verification_status not in PrepQuestion.LEARNER_VISIBLE_STATUSES:
                continue
            issues = assessment_question_rendering_issues(question.question_latex)
            if question.verification_status != "flagged" and not issues:
                continue
            course = question.paper.course if question.paper_id else (
                question.topic.course if question.topic_id else None
            )
            topic = _resolve_topic(question, course) if course else None
            candidates.append((question, course, topic, issues))

        limit = max(0, options["limit"])
        if limit:
            candidates = candidates[:limit]
        if not options["apply"]:
            self.stdout.write(
                f"DRY RUN: no questions changed and no AI calls made. "
                f"Candidate limit: {limit or 'all'}."
            )

        repaired = 0
        safely_cleaned = 0
        hidden_invalid = 0
        failed = 0
        skipped_without_context = 0
        already_repaired = 0
        awaiting_review = 0
        covered_by_clean_duplicate = 0
        for question, course, topic, issues in candidates:
            code = course.code if course else "unlinked"
            topic_name = topic.title if topic else "unassigned"
            if not options["apply"]:
                self.stdout.write(
                    f"Q{question.number} id={question.id} course={code} topic={topic_name} "
                    f"status={question.verification_status} issues={'; '.join(issues) or 'manually flagged'}"
                )
                continue

            if deterministic_only:
                original_text = question.question_latex
                cleaned_text = _strip_safe_question_extraction_artifacts(original_text)
                cleaned_issues = assessment_question_rendering_issues(cleaned_text)
                metadata = (
                    question.reconstruction_metadata
                    if isinstance(question.reconstruction_metadata, dict)
                    else {}
                )
                metadata = dict(metadata)
                if cleaned_text != original_text and not cleaned_issues:
                    metadata.setdefault("original_transcription", original_text)
                    metadata.update({
                        "review_status": "deterministically_repaired",
                        "reason": (
                            "Only unambiguous leading extraction debris or a following paper header was removed."
                        ),
                        "deterministic_repair_issues": issues,
                    })
                    question.question_latex = cleaned_text
                    question.reconstruction_metadata = metadata
                    question.save(update_fields=["question_latex", "reconstruction_metadata"])
                    safely_cleaned += 1
                    self.stdout.write(
                        f"Cleaned Q{question.number} id={question.id} course={code}; "
                        "retained only after validation passed."
                    )
                else:
                    metadata.setdefault("original_transcription", original_text)
                    metadata.update({
                        "review_status": "source_flagged",
                        "reason": "The question has extraction defects that cannot be repaired without guessing.",
                        "original_extraction_issues": issues,
                    })
                    question.verification_status = "flagged"
                    question.verified_by = None
                    question.reconstruction_metadata = metadata
                    question.save(update_fields=[
                        "verification_status",
                        "verified_by",
                        "reconstruction_metadata",
                    ])
                    hidden_invalid += 1
                    self.stderr.write(
                        f"Flagged Q{question.number} id={question.id} course={code}: "
                        f"{'; '.join(issues)}"
                    )
                continue

            if question.verification_status != "flagged":
                question.verification_status = "flagged"
                question.verified_by = None
                question.save(update_fields=["verification_status", "verified_by"])
            if question.topic_id != (topic.id if topic else None):
                question.topic = topic
                question.save(update_fields=["topic"])
            if course is None:
                skipped_without_context += 1
                self.stderr.write(
                    f"Skipped Q{question.number} id={question.id}: no course context is available."
                )
                continue

            duplicate = _clean_indexed_duplicate(question)
            if duplicate:
                covered_by_clean_duplicate += 1
                self.stderr.write(
                    f"Skipped Q{question.number} id={question.id}: clean indexed question "
                    f"id={duplicate.id} on the same source page already covers this damaged duplicate."
                )
                continue

            adapted_label = f"Adapted from Question {question.number}"
            existing = PrepQuestion.objects.filter(
                question_type="adapted",
                reconstructed_from=question,
            ).first()
            if (
                existing
                and existing.verification_status in PrepQuestion.LEARNER_VISIBLE_STATUSES
                and not assessment_question_rendering_issues(existing.question_latex)
            ):
                already_repaired += 1
                continue
            if (
                existing
                and existing.verification_status == "pending"
                and not assessment_question_rendering_issues(existing.question_latex)
            ):
                metadata = (
                    existing.reconstruction_metadata
                    if isinstance(existing.reconstruction_metadata, dict)
                    else {}
                )
                confidence = metadata.get("model_confidence")
                if (
                    metadata.get("source_review_status") == "pass"
                    and isinstance(confidence, (int, float))
                    and not isinstance(confidence, bool)
                    and _AUTO_RECONSTRUCTION_CONFIDENCE_THRESHOLD <= confidence <= 1
                    and not metadata.get("adapted_question_validation_issues")
                ):
                    existing.verification_status = "reconstructed"
                    metadata["review_status"] = "auto_validated"
                    metadata["reason"] = (
                        "Previously generated adaptation passed deterministic validation, "
                        "independent source review, and the confidence threshold."
                    )
                    existing.reconstruction_metadata = metadata
                    existing.save(update_fields=["verification_status", "reconstruction_metadata"])
                    repaired += 1
                    continue
                elif not options["retry_pending"]:
                    awaiting_review += 1
                    self.stderr.write(
                        f"Q{question.number} id={question.id} already has a structurally valid "
                        "adaptation without a passing source review and confidence evidence; "
                        "not spending credits on an automatic retry."
                    )
                    continue

            try:
                from services.prep_ai_router import generate_adapted_past_question

                result = generate_adapted_past_question(question)
                if not result.get("success"):
                    failed += 1
                    self.stderr.write(
                        f"Repair failed for Q{question.number} id={question.id}: "
                        f"{result.get('error', 'AI reconstruction failed')[:300]}"
                    )
                    continue

                item = result["question"]
                item_issues = assessment_question_rendering_issues(item.get("question_latex", ""))
                if item_issues:
                    failed += 1
                    self.stderr.write(
                        f"Repair failed validation for Q{question.number} id={question.id}: "
                        f"{'; '.join(item_issues)}"
                    )
                    continue

                metadata = result.get("reconstruction_metadata")
                metadata = dict(metadata) if isinstance(metadata, dict) else {}
                confidence = metadata.get("model_confidence")
                auto_approved = (
                    not item_issues
                    and metadata.get("source_review_status") == "pass"
                    and isinstance(confidence, (int, float))
                    and not isinstance(confidence, bool)
                    and _AUTO_RECONSTRUCTION_CONFIDENCE_THRESHOLD <= confidence <= 1
                )
                try:
                    repair_attempts = int(existing.reconstruction_metadata.get("repair_attempts", 0)) + 1 if (
                        existing and isinstance(existing.reconstruction_metadata, dict)
                    ) else 1
                except (TypeError, ValueError):
                    repair_attempts = 1
                metadata.update({
                    "review_status": "auto_validated" if auto_approved else "pending",
                    "reason": (
                        "AI reconstruction passed deterministic validation, source review, and the confidence threshold."
                        if auto_approved
                        else "AI reconstruction requires review because source review failed or confidence was below threshold or unavailable."
                    ),
                    "auto_validation_threshold": _AUTO_RECONSTRUCTION_CONFIDENCE_THRESHOLD,
                    "source_question_id": str(question.pk),
                    "source_document_id": (
                        str(question.source_document_id) if question.source_document_id else None
                    ),
                    "source_page_number": question.source_page_number,
                    "original_transcription": question.question_latex,
                    "original_extraction_issues": issues or ["manually flagged for reconstruction"],
                    "adapted_question_validation_issues": item_issues,
                    "repair_attempts": repair_attempts,
                })
                if existing is None:
                    existing = PrepQuestion(
                        paper=question.paper,
                        reconstructed_from=question,
                        question_type="adapted",
                        number=question.number,
                    )
                existing.topic = topic
                existing.source_document = question.source_document or (
                    question.paper.source_document if question.paper_id else None
                )
                existing.source_page_number = question.source_page_number
                existing.extraction_confidence = question.extraction_confidence
                existing.marks = int(item.get("marks") or question.marks)
                existing.topic_label = adapted_label
                existing.question_latex = item["question_latex"]
                existing.solution_latex = item["solution_latex"]
                existing.verification_status = "reconstructed" if auto_approved else "pending"
                existing.verified_by = None
                existing.reconstruction_metadata = metadata
                existing.save()
                if auto_approved:
                    repaired += 1
                else:
                    awaiting_review += 1
                    self.stderr.write(
                        f"Q{question.number} id={question.id} reconstructed but held for review: "
                        f"confidence={confidence!r}, threshold={_AUTO_RECONSTRUCTION_CONFIDENCE_THRESHOLD}."
                    )
            except Exception as exc:
                failed += 1
                self.stderr.write(f"Repair failed for Q{question.number} id={question.id}: {str(exc)[:300]}")

        mode = "Applied" if options["apply"] else "Would process"
        self.stdout.write(
            self.style.SUCCESS(
                f"{mode} {len(candidates)} candidate(s); repaired={repaired}, "
                f"deterministically_cleaned={safely_cleaned}, hidden_invalid={hidden_invalid}, "
                f"already_repaired={already_repaired}, failed={failed}, "
                f"awaiting_review={awaiting_review}, "
                f"covered_by_clean_duplicate={covered_by_clean_duplicate}, "
                f"skipped_without_context={skipped_without_context}."
            )
        )