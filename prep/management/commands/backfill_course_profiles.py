from django.core.management.base import BaseCommand

from prep.models import PrepCourse, PrepDocument
from services.prep_ingestion import COURSE_STUDY_FAMILIES, extract_course_study_profile


class Command(BaseCommand):
    help = "Backfill approved study profiles for existing courses using their uploaded lecture notes and revision sheets."

    def add_arguments(self, parser):
        parser.add_argument("--course-code", help="Limit the backfill to one course code.")
        parser.add_argument("--dry-run", action="store_true", help="Preview the courses that would receive profiles without changing them.")

    def handle(self, *args, **options):
        queryset = PrepCourse.objects.all().order_by("code")
        if options.get("course_code"):
            queryset = queryset.filter(code__iexact=options["course_code"])

        updated = 0
        skipped = 0
        for course in queryset:
            documents = (
                PrepDocument.objects.filter(
                    course=course,
                    doc_type__in=["Lecture Notes", "Revision Sheet"],
                )
                .exclude(extracted_text="")
                .order_by("-updated_at", "-created_at")
            )
            chosen = None
            for doc in documents:
                profile = extract_course_study_profile(course, doc.extracted_text, source_document=doc)
                if profile:
                    chosen = (doc, profile)
                    break

            if not chosen:
                skipped += 1
                self.stdout.write(self.style.WARNING(f"Skipped {course.code}: no grounded profile could be extracted."))
                continue

            document, profile = chosen
            family = str(profile.get("subject_family") or "").strip().lower()
            family_config = COURSE_STUDY_FAMILIES.get(family)
            if not family_config:
                skipped += 1
                self.stdout.write(self.style.WARNING(f"Skipped {course.code}: family '{family}' is not recognised."))
                continue

            if options["dry_run"]:
                self.stdout.write(
                    self.style.HTTP_INFO(
                        f"Would apply {family} profile to {course.code} from {document.doc_type} ({document.id})."
                    )
                )
                continue

            course.category = family_config["category"]
            course.study_profile = {**profile, "version": (course.study_profile_version or 0) + 1}
            course.study_profile_version = (course.study_profile_version or 0) + 1
            course.save(update_fields=["category", "study_profile", "study_profile_version", "updated_at"])
            updated += 1
            self.stdout.write(
                self.style.SUCCESS(
                    f"Applied {family} profile to {course.code} using {document.doc_type} ({document.id})."
                )
            )

        mode = "Would update" if options["dry_run"] else "Updated"
        self.stdout.write(
            self.style.SUCCESS(f"{mode} {updated} course(s); skipped {skipped} course(s).")
        )
