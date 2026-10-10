import time
from django.core.management.base import BaseCommand
from prep.models import PrepCourse, PrepPaper, PrepQuestion
from services.prep_ingestion import learner_visible_assessment_questions
from services.prep_solution_precompute import (
    precompute_solution_for_question,
    precompute_solutions_for_questions,
)
from services.prep_ai_router import validated_question_solution


class Command(BaseCommand):
    help = (
        "Precompute and verify step-by-step solutions for past paper questions in the background, "
        "ensuring they are vetted, validated, and formatted before learners view or export them."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--course",
            type=str,
            default=None,
            help="Filter by course code (e.g. SMA 300).",
        )
        parser.add_argument(
            "--paper-id",
            type=int,
            default=None,
            help="Filter by specific PrepPaper ID.",
        )
        parser.add_argument(
            "--limit",
            type=int,
            default=None,
            help="Maximum number of solutions to generate in this run.",
        )
        parser.add_argument(
            "--sleep-seconds",
            type=float,
            default=1.0,
            help="Pacing sleep between generations (default 1.0s) to avoid rate limits or CPU contention.",
        )

    def handle(self, *args, **options):
        course_code = options.get("course")
        paper_id = options.get("paper_id")
        limit = options.get("limit")
        sleep_seconds = options.get("sleep_seconds", 1.0)

        qs = PrepQuestion.objects.filter(
            verification_status__in=PrepQuestion.ANSWERABLE_STATUSES
        ).select_related("topic", "paper", "paper__course", "topic__course").order_by("paper", "number", "id")

        if paper_id:
            qs = qs.filter(paper_id=paper_id)
        if course_code:
            qs = qs.filter(
                topic__course__code__iexact=course_code
            ) | qs.filter(
                paper__course__code__iexact=course_code
            )

        visible_questions = learner_visible_assessment_questions(qs)
        missing_solutions = [q for q in visible_questions if not validated_question_solution(q)]

        self.stdout.write(
            f"Found {len(visible_questions)} visible questions. "
            f"{len(missing_solutions)} questions currently need verified solutions."
        )

        if not missing_solutions:
            self.stdout.write(self.style.SUCCESS("All visible questions already have verified solutions!"))
            return

        to_process = missing_solutions[:limit] if limit else missing_solutions
        self.stdout.write(f"Precomputing solutions for {len(to_process)} question(s)...")

        def progress(idx, total, q, status):
            c_code = getattr(getattr(q.topic, "course", None), "code", "") or getattr(getattr(q.paper, "course", None), "code", "Math")
            if status == "completed":
                self.stdout.write(self.style.SUCCESS(f"[{idx}/{total}] Q{q.number} (id={q.id}, {c_code}): Verified solution generated."))
            elif status == "failed":
                self.stdout.write(self.style.WARNING(f"[{idx}/{total}] Q{q.number} (id={q.id}, {c_code}): Generation or validation failed."))
            elif status == "already_valid":
                self.stdout.write(f"[{idx}/{total}] Q{q.number} (id={q.id}, {c_code}): Already verified.")

        stats = precompute_solutions_for_questions(
            to_process,
            sleep_seconds=sleep_seconds,
            progress_callback=progress,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Finished! Completed: {stats['completed']} | Already valid: {stats['already_valid']} | "
                f"Failed: {stats['failed']} | Total: {stats['total']}"
            )
        )
