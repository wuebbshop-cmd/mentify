import logging
from django.core.management.base import BaseCommand
from prep.models import PrepCourse, PrepTopic, PrepTopicQuizQuestion
from services.prep_topic_quiz import generate_topic_quiz_questions

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Pre-generate high-quality multiple-choice questions for course topics so students get instant drill access."

    def add_arguments(self, parser):
        parser.add_argument(
            "--course",
            type=str,
            help="Filter by specific course code (e.g., 'SMA 103', 'UCU 110', 'SMA 190')",
        )
        parser.add_argument(
            "--topic-id",
            type=int,
            help="Pre-generate for a specific topic ID",
        )
        parser.add_argument(
            "--count",
            type=int,
            default=5,
            help="Target number of active quiz questions per topic (default: 5)",
        )
        parser.add_argument(
            "--overwrite",
            action="store_true",
            help="Regenerate questions even if the topic already has questions",
        )

    def handle(self, *args, **options):
        course_code = options.get("course")
        topic_id = options.get("topic_id")
        target_count = options.get("count") or 5
        overwrite = options.get("overwrite", False)

        topics_qs = PrepTopic.objects.filter(is_active=True).select_related("course")

        if topic_id:
            topics_qs = topics_qs.filter(id=topic_id)
        elif course_code:
            topics_qs = topics_qs.filter(course__code__icontains=course_code.strip())
        else:
            topics_qs = topics_qs.filter(course__is_active=True)

        topics = list(topics_qs.order_by("course__code", "order", "id"))
        if not topics:
            self.stdout.write(self.style.WARNING("No matching active topics found."))
            return

        self.stdout.write(
            self.style.MIGRATE_HEADING(
                f"Starting quiz question seeding for {len(topics)} topic(s)... (Target: {target_count} MCQs/topic)"
            )
        )

        total_created = 0
        total_skipped = 0
        total_failed = 0

        for idx, topic in enumerate(topics, 1):
            existing_count = PrepTopicQuizQuestion.objects.filter(topic=topic, is_active=True).count()
            if existing_count >= target_count and not overwrite:
                self.stdout.write(
                    f"[{idx}/{len(topics)}] {topic.course.code} - {topic.title}: already has {existing_count} questions. Skipping."
                )
                total_skipped += 1
                continue

            needed = target_count if overwrite else (target_count - existing_count)
            self.stdout.write(
                f"[{idx}/{len(topics)}] Generating {needed} questions for {topic.course.code} - {topic.title}..."
            )

            try:
                new_questions = generate_topic_quiz_questions(topic=topic, count=needed)
                if new_questions:
                    total_created += len(new_questions)
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"  -> Successfully generated and saved {len(new_questions)} questions."
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f"  -> Generator returned 0 questions for topic {topic.id}."
                        )
                    )
            except Exception as e:
                total_failed += 1
                self.stdout.write(
                    self.style.ERROR(
                        f"  -> Failed to generate questions for topic {topic.id} ({topic.title}): {e}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"\nSeeding complete! Total generated: {total_created}, Skipped: {total_skipped}, Failed: {total_failed}."
            )
        )
