import json

from django.core.management.base import BaseCommand, CommandError

from prep.models import PrepContentCache, PrepCourse, PrepDocument, PrepQuestion
from services.prep_ai_router import ANSWER_VALIDATION_VERSION, NOTE_VALIDATION_STATE


class Command(BaseCommand):
    help = "Report Phase 10 pilot readiness without changing data or calling providers."

    def add_arguments(self, parser):
        parser.add_argument(
            "--course-code",
            action="append",
            dest="course_codes",
            help="Limit the audit to one or more course codes; repeat the option for multiple courses.",
        )
        parser.add_argument("--json", action="store_true", help="Emit the report as JSON.")

    @staticmethod
    def _usage_total(payload):
        if not isinstance(payload, dict):
            return 0
        usage = payload.get("usage")
        if not isinstance(usage, dict):
            return 0
        return int(usage.get("total_tokens") or usage.get("prompt_tokens", 0) or 0) + int(
            usage.get("completion_tokens", 0) or 0
        ) if "total_tokens" not in usage else int(usage.get("total_tokens") or 0)

    def _course_report(self, course):
        documents = list(course.documents.all())
        questions = list(
            PrepQuestion.objects.filter(
                paper__course=course,
            ).select_related("source_document", "reconstructed_from")
        )
        questions += list(
            PrepQuestion.objects.filter(
                paper__isnull=True,
                topic__course=course,
            ).select_related("source_document", "reconstructed_from")
        )
        question_statuses = {}
        reconstruction = {"total": 0, "auto_validated": 0, "pending": 0, "with_original": 0, "missing_original": 0}
        question_risks = []
        observed_tokens = 0
        for question in questions:
            question_statuses[question.verification_status] = question_statuses.get(question.verification_status, 0) + 1
            if question.verification_status not in PrepQuestion.LEARNER_VISIBLE_STATUSES:
                question_risks.append(
                    f"question {question.pk} has non-learner-visible status {question.verification_status}"
                )
            if question.question_type == "adapted":
                reconstruction["total"] += 1
                if question.verification_status == "reconstructed":
                    reconstruction["auto_validated"] += 1
                if question.verification_status == "pending":
                    reconstruction["pending"] += 1
                metadata = question.reconstruction_metadata if isinstance(question.reconstruction_metadata, dict) else {}
                if metadata.get("original_transcription"):
                    reconstruction["with_original"] += 1
                else:
                    reconstruction["missing_original"] += 1
                    question_risks.append(f"adapted question {question.pk} has no original transcription metadata")
                observed_tokens += self._usage_total(metadata)

        document_reports = {
            "total": len(documents),
            "stage_3": sum(document.stage == "stage_3" for document in documents),
            "validation_passed": 0,
            "needs_review": 0,
            "missing_report": 0,
            "validation_issues": 0,
            "visual_candidates": 0,
            "approved_visuals": 0,
        }
        document_risks = []
        for document in documents:
            report = document.validation_report if isinstance(document.validation_report, dict) else {}
            if not report:
                document_reports["missing_report"] += 1
                document_risks.append(f"document {document.pk} has no validation report")
            elif report.get("status") == "passed":
                document_reports["validation_passed"] += 1
            else:
                document_reports["needs_review"] += 1
                document_reports["validation_issues"] += len(report.get("issues", []))
                document_risks.append(
                    f"document {document.pk} validation status is {report.get('status') or 'unknown'}"
                )
            visuals = list(document.visual_candidates.all())
            document_reports["visual_candidates"] += len(visuals)
            document_reports["approved_visuals"] += sum(visual.status == "approved" for visual in visuals)
            for visual in visuals:
                observed_tokens += self._usage_total(visual.vision_usage)
                if visual.status == "approved" and not visual.crop:
                    document_risks.append(f"visual {visual.pk} is approved without a crop")

        caches = list(PrepContentCache.objects.filter(course=course))
        cache_report = {
            "total": len(caches),
            "notes": sum(cache.content_type == "topic_notes" for cache in caches),
            "answers": sum(cache.content_type == "solution_derivation" for cache in caches),
            "practice_sets": sum(cache.content_type == "practice_set" for cache in caches),
            "invalid_or_unvalidated": 0,
        }
        cache_risks = []
        for cache in caches:
            payload = cache.payload if isinstance(cache.payload, dict) else {}
            is_valid = (
                cache.content_type == "topic_notes"
                and payload.get("validation_state") == NOTE_VALIDATION_STATE
                or cache.content_type == "solution_derivation"
                and payload.get("answer_validation_version") == ANSWER_VALIDATION_VERSION
                or cache.content_type == "practice_set"
                and payload.get("validation_version") == ANSWER_VALIDATION_VERSION
            )
            if cache.content_type in {"topic_notes", "solution_derivation", "practice_set"} and not is_valid:
                cache_report["invalid_or_unvalidated"] += 1
                cache_risks.append(f"{cache.content_type} cache {cache.pk} lacks current validation metadata")

        risks = document_risks + question_risks + cache_risks
        if not documents:
            risks.append("course has no uploaded source documents")
        if not questions:
            risks.append("course has no indexed questions")
        if reconstruction["missing_original"]:
            risks.append("one or more adaptations lack original-question provenance")
        return {
            "course_code": course.code,
            "course_title": course.title,
            "category": course.category,
            "study_profile_version": course.study_profile_version,
            "documents": document_reports,
            "questions": {"total": len(questions), "statuses": question_statuses},
            "reconstruction": reconstruction,
            "caches": cache_report,
            "observed_provider_tokens": observed_tokens,
            "risks": risks,
            "ready_for_expansion": not risks,
        }

    def handle(self, *args, **options):
        course_codes = options.get("course_codes") or []
        courses = PrepCourse.objects.all().order_by("code")
        if course_codes:
            courses = courses.filter(code__in=course_codes)
            found = set(courses.values_list("code", flat=True))
            missing = [code for code in course_codes if code not in found]
            if missing:
                raise CommandError(f"Course(s) not found: {', '.join(missing)}")

        reports = [self._course_report(course) for course in courses]
        report = {
            "schema_version": 1,
            "mode": "dry_run",
            "provider_calls": 0,
            "provider_tokens_spent": 0,
            "courses": reports,
            "ready_for_expansion": bool(reports) and all(item["ready_for_expansion"] for item in reports),
        }
        if options["json"]:
            self.stdout.write(json.dumps(report, ensure_ascii=True, sort_keys=True))
            return

        self.stdout.write("DRY RUN: no records changed and no provider calls made.")
        for item in reports:
            self.stdout.write(
                f"{item['course_code']}: ready={item['ready_for_expansion']} "
                f"documents={item['documents']['total']} questions={item['questions']['total']} "
                f"risks={len(item['risks'])} observed_tokens={item['observed_provider_tokens']}"
            )
        self.stdout.write(
            f"Audited {len(reports)} course(s); ready_for_expansion={report['ready_for_expansion']}."
        )
