import logging
from django.core.management.base import BaseCommand
from services.blog_generator import run_daily_blog_batch, _get_target_db

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generate daily high-impact technical blog posts using live web headlines and DeepSeek synthesis into substitute DB."

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=4,
            help="Number of blog posts to generate (default: 4)",
        )
        parser.add_argument(
            "--database",
            type=str,
            default="",
            help="Target database alias (default: substitute if configured, else default)",
        )

    def handle(self, *args, **options):
        count = options["count"]
        db_alias = options["database"] or _get_target_db()

        self.stdout.write(self.style.NOTICE(f"Starting daily blog generation batch (target: {count} posts, db: {db_alias})..."))

        posts = run_daily_blog_batch(target_count=count, db_alias=db_alias)

        self.stdout.write(self.style.SUCCESS(f"\nSuccessfully published {len(posts)} new posts to {db_alias}:"))
        for p in posts:
            self.stdout.write(f" - [{p.category.name if p.category else 'No Category'}] {p.title} (slug: {p.slug})")
