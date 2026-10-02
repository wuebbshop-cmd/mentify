import re

from django.core.management.base import BaseCommand
from django.db.models import Q

from prep.models import PrepQuestion
from services.prep_ingestion import assessment_question_rendering_issues


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
    return None


class Command(BaseCommand):
    help = "Audit existing authentic questions and reconstruct flagged or malformed rows."

    def add_arguments(self, parser):
        parser.add_argument("--course-code", help="Limit the audit to one course code.")
        parser.add_argument("--limit", type=int, default=100, help="Maximum candidate rows to inspect (default: 100).")
        parser.add_argument("--apply", action="store_true", help="Call the AI and save validated adapted questions. Default is dry-run.")

    def handle(self, *args, **options):
        questions = PrepQuestion.objects.filter(question_type="authentic").select_related(
            "paper__course", "topic__course"
        ).order_by("id")
        course_code = options.get("course_code")
        if course_code:
            questions = questions.filter(
                Q(paper__course__code__iexact=course_code)
                | Q(topic__course__code__iexact=course_code)
            )

        candidates = []
        for question in questions.iterator():
            issues = assessment_question_rendering_issues(question.question_latex)
            if question.verification_status != "flagged" and not issues:
                continue
            course = question.paper.course if question.paper_id else (
                question.topic.course if question.topic_id else None
            )
            topic = _resolve_topic(question, course) if course else None
            candidates.append((question, course, topic, issues))

        limit = max(0, options["limit"])
        candidates = candidates[:limit]
        if not options["apply"]:
            self.stdout.write("DRY RUN: no questions changed and no AI calls made.")

        repaired = 0
        failed = 0
        skipped_without_topic = 0
        already_repaired = 0
        for question, course, topic, issues in candidates:
            code = course.code if course else "unlinked"
            topic_name = topic.title if topic else "unassigned"
            if not options["apply"]:
                self.stdout.write(
                    f"Q{question.number} id={question.id} course={code} topic={topic_name} "
                    f"status={question.verification_status} issues={'; '.join(issues) or 'manually flagged'}"
                )
                continue

            if question.verification_status != "flagged":
                question.verification_status = "flagged"
                question.verified_by = None
                question.save(update_fields=["verification_status", "verified_by"])
            if not topic:
                skipped_without_topic += 1
                self.stderr.write(f"Skipped Q{question.number} id={question.id}: no safe topic match; source remains hidden.")
                continue
            if question.topic_id != topic.id:
                question.topic = topic
                question.save(update_fields=["topic"])

            adapted_label = f"Adapted from Question {question.number}"
            existing = PrepQuestion.objects.filter(
                question_type="adapted",
                reconstructed_from=question,
            ).first()
            if existing is None:
                existing = PrepQuestion.objects.filter(
                    paper=question.paper,
                    topic=topic,
                    question_type="adapted",
                    topic_label=adapted_label,
                    verification_status__in=["pending", "verified"],
                ).first()
            if existing:
                already_repaired += 1
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

                PrepQuestion.objects.create(
                    paper=question.paper,
                    topic=topic,
                    source_document=question.source_document or (
                        question.paper.source_document if question.paper_id else None
                    ),
                    source_page_number=question.source_page_number,
                    extraction_confidence=question.extraction_confidence,
                    reconstructed_from=question,
                    reconstruction_metadata=result.get("reconstruction_metadata", {
                        "review_status": "pending",
                        "reason": "Adapted from a flagged source question.",
                        "source_question_id": str(question.pk),
                        "source_document_id": str(question.source_document_id) if question.source_document_id else None,
                        "source_page_number": question.source_page_number,
                        "original_transcription": question.question_latex,
                        "original_extraction_issues": issues,
                    }),
                    question_type="adapted",
                    number=question.number,
                    marks=int(item.get("marks") or question.marks),
                    topic_label=adapted_label,
                    question_latex=item["question_latex"],
                    solution_latex=item["solution_latex"],
                    verification_status="pending",
                )
                repaired += 1
            except Exception as exc:
                failed += 1
                self.stderr.write(f"Repair failed for Q{question.number} id={question.id}: {str(exc)[:300]}")

        mode = "Applied" if options["apply"] else "Would process"
        self.stdout.write(
            self.style.SUCCESS(
                f"{mode} {len(candidates)} candidate(s); repaired={repaired}, "
                f"already_repaired={already_repaired}, failed={failed}, "
                f"skipped_without_topic={skipped_without_topic}."
            )
        )