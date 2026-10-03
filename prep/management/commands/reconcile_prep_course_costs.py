import re

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from prep.models import (
    PrepCourse,
    PrepCourseCostShare,
    PrepCourseSharedCost,
    PrepDocument,
    PrepTransaction,
)
from services.prep_course_billing import settle_course_cost_share


class Command(BaseCommand):
    help = "Backfill shared course costs from existing upload and topic-note credit transactions."

    def add_arguments(self, parser):
        parser.add_argument("--course", help="Limit reconciliation to a course code.")
        parser.add_argument(
            "--enqueue-published",
            action="store_true",
            help="Queue Level 2 precomputation for courses with published lecture materials.",
        )

    def handle(self, *args, **options):
        courses = PrepCourse.objects.all()
        if options.get("course"):
            courses = courses.filter(code__iexact=options["course"])
        total = 0
        queued = 0

        for course in courses.iterator():
            total += self._reconcile_course(course)
            if options["enqueue_published"] and PrepDocument.objects.filter(
                course=course,
                stage="stage_3",
                doc_type__in=["Lecture Notes", "Revision Sheet"],
            ).exists():
                from services.prep_note_precompute import enqueue_course_level_two_precompute

                _, was_queued = enqueue_course_level_two_precompute(course)
                queued += int(was_queued)
        self.stdout.write(self.style.SUCCESS(
            f"Reconciled {total} historical shared costs and queued {queued} published course(s)."
        ))

    def _reconcile_course(self, course):
        count = 0
        prefix = f"Document Ingestion: {course.code} ("
        transactions = PrepTransaction.objects.filter(
            action_type__in=["upload_text", "upload_ocr", "topic_notes"],
            description__icontains=course.code,
        ).select_related("wallet__user").order_by("-created_at", "-pk")
        reconciled_note_keys = set()

        for entry in transactions.iterator():
            if (entry.metadata or {}).get("shared_course_cost_id"):
                continue
            if entry.action_type in {"upload_text", "upload_ocr"}:
                if not entry.description.startswith(prefix):
                    continue
                cost_type = "upload"
                topic = None
                level = ""
            else:
                match = re.match(
                    r"^AI Topic Notes \((level_[123])\):\s*(.+?)\s+-\s+(.+)$",
                    entry.description,
                )
                if not match or match.group(2).strip().casefold() != course.code.casefold():
                    continue
                level = match.group(1)
                topic = course.topics.filter(title__iexact=match.group(3).strip()).first()
                if not topic:
                    continue
                note_key = (topic.pk, level)
                if note_key in reconciled_note_keys:
                    continue
                reconciled_note_keys.add(note_key)
                cost_type = "topic_notes"

            cost, created = PrepCourseSharedCost.objects.get_or_create(
                source_key=(
                    f"legacy-upload-transaction:{entry.pk}"
                    if cost_type == "upload"
                    else f"legacy-topic-notes:{topic.pk}:{level}"
                ),
                defaults={
                    "course": course,
                    "cost_type": cost_type,
                    "document": None,
                    "topic": topic,
                    "level": level,
                    "source_transaction": entry,
                    "total_credits": abs(entry.amount),
                    "per_student_credits": 0,
                    "member_count_at_creation": 0,
                    "usage": {
                        "prompt_tokens": entry.input_tokens or 0,
                        "completion_tokens": entry.output_tokens or 0,
                        "total_tokens": entry.total_tokens or 0,
                    },
                    "model_name": entry.model_name,
                },
            )
            if not created:
                continue

            # Use the current course catalog as the roster snapshot for legacy costs.
            members = list(course.enrollments.filter(user__role="learner").values_list("user_id", flat=True))
            cost.member_count_at_creation = len(members)
            cost.per_student_credits = cost.total_credits
            cost.save(update_fields=["member_count_at_creation", "per_student_credits"])
            PrepCourseCostShare.objects.bulk_create([
                PrepCourseCostShare(
                    cost=cost,
                    user_id=user_id,
                    required_credits=cost.total_credits,
                )
                for user_id in members
            ])
            payer_share = cost.shares.filter(user=entry.wallet.user).first()
            if payer_share:
                payer_share.paid_credits = min(payer_share.required_credits, abs(entry.amount))
                if payer_share.paid_credits >= payer_share.required_credits:
                    payer_share.settled_at = entry.created_at or timezone.now()
                payer_share.save(update_fields=["paid_credits", "settled_at"])
            for share in cost.shares.exclude(user=entry.wallet.user).select_related("user", "cost"):
                settle_course_cost_share(share)
            count += 1
        return count
