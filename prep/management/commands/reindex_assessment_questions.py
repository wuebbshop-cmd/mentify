from collections import Counter

from django.core.management.base import BaseCommand, CommandError

from prep.models import PrepDocument
from services.prep_ingestion import (
    assessment_question_rendering_issues,
    extract_assessment_questions,
)
from services.prep_assessment_index import enqueue_assessment_index


class Command(BaseCommand):
    help = "Audit published assessment papers or queue them for background reindexing."

    def add_arguments(self, parser):
        parser.add_argument("--course-code", action="append", dest="course_codes")
        parser.add_argument(
            "--apply",
            action="store_true",
            help="Queue linked stage_3 papers for the dedicated background assessment worker.",
        )

    def handle(self, *args, **options):
        documents = PrepDocument.objects.filter(
            stage="stage_3",
            doc_type__in=[
                "Continuous Assessment Test (CAT)",
                "Final Examination Paper",
            ],
        ).exclude(extracted_text="").select_related("course").prefetch_related("derived_papers")
        course_codes = options.get("course_codes") or []
        if course_codes:
            documents = documents.filter(course__code__in=course_codes)

        candidates = []
        flag_reasons = Counter()
        unlinked_count = 0
        for document in documents.order_by("course__code", "created_at", "id"):
            papers = list(document.derived_papers.all())
            if not papers:
                unlinked_count += 1
                self.stderr.write(
                    f"Skipped {document.course.code} document {document.pk}: "
                    "no paper is linked by source_document."
                )
                continue
            parsed_questions = extract_assessment_questions(document.extracted_text)
            parsed_issues = [
                assessment_question_rendering_issues(item["question_latex"])
                for item in parsed_questions
            ]
            flagged_count = sum(bool(issues) for issues in parsed_issues)
            for issues in parsed_issues:
                flag_reasons.update(set(issues))
            candidates.extend(
                (document, paper, len(parsed_questions), flagged_count)
                for paper in papers
            )

        if not candidates:
            if unlinked_count:
                raise CommandError(
                    f"No linked stage_3 assessment papers to reindex; {unlinked_count} "
                    "source document(s) need linking."
                )
            self.stdout.write("No published assessment papers with extracted text were found.")
            return

        if not options["apply"]:
            self.stdout.write("DRY RUN: no questions changed and no AI calls made.")
        total_parsed = 0
        queued_jobs = 0
        for document, paper, parsed_count, flagged_count in candidates:
            total_parsed += parsed_count
            self.stdout.write(
                f"{'Would reindex' if not options['apply'] else 'Reindexing'} "
                f"{document.course.code} | paper={paper.pk} ({paper.title}) "
                f"| source={document.pk} "
                f"| existing_authentic={paper.questions.filter(question_type='authentic').count()} "
                f"| parsed_questions={parsed_count} | extraction_flags={flagged_count}"
            )
            if options["apply"]:
                _, created = enqueue_assessment_index(
                    paper,
                    reconstruct_invalid=False,
                    force=True,
                )
                queued_jobs += int(created)
                self.stdout.write(
                    f"  {'queued new job' if created else 'job already exists'}"
                )

        self.stdout.write(
            f"Assessment documents: {len(candidates)}; parsed question instances: {total_parsed}; "
            f"new indexing jobs queued: {queued_jobs}; "
            f"unlinked source documents: {unlinked_count}."
        )
        if flag_reasons:
            self.stdout.write("Extraction flag summary:")
            for reason, count in flag_reasons.most_common():
                self.stdout.write(f"- {reason}: {count}")
