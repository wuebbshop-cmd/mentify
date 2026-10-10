import re
from django.core.management.base import BaseCommand
from prep.models import PrepQuestion
from services.prep_ai_router import clean_latex_document_markup, normalize_math_delimiters
from services.prep_ingestion import assessment_question_rendering_issues


class Command(BaseCommand):
    help = (
        "Clean, normalize, and format all past paper and practice questions in the database, "
        "converting raw LaTeX document markup (enumerate, item, hfill, textbf) into clean Markdown + KaTeX."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--apply",
            action="store_true",
            help="Persist changes to the database. Defaults to dry-run.",
        )
        parser.add_argument(
            "--course",
            type=str,
            default=None,
            help="Optional course code filter (e.g. SMA 300).",
        )

    def handle(self, *args, **options):
        apply_changes = options.get("apply", False)
        course_filter = options.get("course")

        qs = PrepQuestion.objects.all().select_related("topic", "paper")
        if course_filter:
            qs = qs.filter(topic__course__code__iexact=course_filter)

        total_questions = qs.count()
        self.stdout.write(f"Found {total_questions} questions to check.")

        updated_count = 0
        issues_cleared_count = 0

        for q in qs.iterator():
            changed = False
            raw_q = q.question_latex or ""
            raw_sol = q.solution_latex or ""

            cleaned_q = clean_latex_document_markup(raw_q)
            if cleaned_q:
                cleaned_q = normalize_math_delimiters(cleaned_q)
            
            cleaned_sol = clean_latex_document_markup(raw_sol)
            if cleaned_sol:
                cleaned_sol = normalize_math_delimiters(cleaned_sol)

            update_fields = []
            if cleaned_q != raw_q:
                q.question_latex = cleaned_q
                update_fields.append("question_latex")
                changed = True

            if cleaned_sol != raw_sol:
                q.solution_latex = cleaned_sol
                update_fields.append("solution_latex")
                changed = True

            # If question had formatting issues before, check if they are now resolved
            prior_issues = assessment_question_rendering_issues(raw_q)
            new_issues = assessment_question_rendering_issues(cleaned_q)
            if prior_issues and not new_issues:
                issues_cleared_count += 1
                if q.verification_status == "flagged":
                    q.verification_status = "auto_validated"
                    update_fields.append("verification_status")
                    changed = True

            if changed:
                updated_count += 1
                if apply_changes:
                    q.save(update_fields=list(set(update_fields)))
                    self.stdout.write(
                        f"Updated Q{q.number} (id={q.id}, type={q.question_type}, fields={update_fields})"
                    )

        if apply_changes:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully formatted and saved {updated_count}/{total_questions} questions. "
                    f"Issues resolved for {issues_cleared_count} questions."
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    f"[DRY-RUN] {updated_count}/{total_questions} questions would be updated. "
                    f"Run with --apply to persist changes."
                )
            )
