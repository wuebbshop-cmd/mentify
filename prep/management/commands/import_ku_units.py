"""
Import Kenyatta University unit codes and titles into the Prep course catalogue.

Marketing/retention purpose: every unit a student might search for should exist in
the public Study Library, even before any notes are uploaded. A course with no
topics shows a "Request course" button instead of an empty page.

Only two things are taken from the workbook: Unit code and Unit title. The
discipline category is derived from the code prefix (existing infer_course_category)
and, as a fallback, from the department name, so the library groups the unit under
the right heading and icon.

Usage:
    python manage.py import_ku_units --dry-run
    python manage.py import_ku_units
    python manage.py import_ku_units --source "C:\\path\\to\\file.xlsx"
"""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from django.core.cache import cache
from django.core.management.base import BaseCommand
from django.utils.text import slugify

DEFAULT_SOURCE = Path(r"C:\Users\adm\Documents\Comp Stats\KU_units_by_department_year_semester.xlsx")
SHEETS = ("Web additions", "All Units")

# Valid values for PrepCourse.category.
VALID_CATEGORIES = {
    "Mathematics",
    "Statistics",
    "Computing",
    "Engineering",
    "Chemistry",
    "Physics",
    "Social Sciences",
    "Humanities",
    "Business & Economics",
    "General Sciences",
    "Other",
}

# Fallback when the code prefix is not recognised by infer_course_category().
# Matched as lowercase substrings against the department/school name.
DEPARTMENT_KEYWORDS = (
    ("actuarial", "Statistics"),
    ("statistic", "Statistics"),
    ("economic", "Business & Economics"),
    ("accounting", "Business & Economics"),
    ("finance", "Business & Economics"),
    ("business", "Business & Economics"),
    ("commerce", "Business & Economics"),
    ("hospitality", "Business & Economics"),
    ("tourism", "Business & Economics"),
    ("agricultur", "Business & Economics"),
    ("enterprise", "Business & Economics"),
    ("engineer", "Engineering"),
    ("computing", "Computing"),
    ("computer", "Computing"),
    ("information technology", "Computing"),
    ("health", "General Sciences"),
    ("medical", "General Sciences"),
    ("nursing", "General Sciences"),
    ("pharmac", "General Sciences"),
    ("pure & applied", "General Sciences"),
    ("physical science", "General Sciences"),
    ("biological", "General Sciences"),
    ("environment", "General Sciences"),
    ("law", "Humanities"),
    ("education", "Social Sciences"),
    ("applied human", "Social Sciences"),
    ("humanities", "Humanities"),
    ("social science", "Humanities"),
    ("arts", "Humanities"),
)

CODE_RE = re.compile(r"^[A-Z]{2,6}\s?\d{2,4}[A-Z]?$")
LEVEL_RE = re.compile(r"level\s*(\d{3})", re.IGNORECASE)


def normalise_code(value) -> str:
    """'sma200 ' -> 'SMA 200'; returns '' when the value is not a unit code."""
    if value is None:
        return ""
    text = re.sub(r"\s+", " ", str(value)).strip().upper()
    if not text:
        return ""
    # Insert a space between the letter prefix and the number when missing.
    text = re.sub(r"^([A-Z]{2,6})(\d)", r"\1 \2", text)
    return text if CODE_RE.match(text) else ""


def normalise_title(value) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


# PrepCourse.title is CharField(max_length=200); a handful of rows in the
# workbook are longer (up to 342 chars) and would raise DataError on insert.
MAX_TITLE_LEN = 200


def truncate_title(title: str) -> str:
    """Clip to the column width at a word boundary rather than mid-word."""
    if len(title) <= MAX_TITLE_LEN:
        return title
    clipped = title[:MAX_TITLE_LEN]
    cut = clipped.rfind(" ")
    if cut > MAX_TITLE_LEN * 0.6:
        clipped = clipped[:cut]
    return clipped.rstrip(" ,.;:-–—")


def category_for(code: str, title: str, department: str) -> str:
    """Discipline category: code/title inference first, department name second."""
    from prep.views import infer_course_category

    inferred = infer_course_category(code, title)
    if inferred in VALID_CATEGORIES and inferred != "Other":
        return inferred

    dept = (department or "").lower()
    for needle, category in DEPARTMENT_KEYWORDS:
        if needle in dept:
            return category

    return inferred if inferred in VALID_CATEGORIES else "Other"


def level_for(year_value) -> str:
    match = LEVEL_RE.search(str(year_value or ""))
    return f"Level {match.group(1)}" if match else "Standard"


class Command(BaseCommand):
    help = "Import KU unit codes/titles into the Prep public course catalogue."

    def add_arguments(self, parser):
        parser.add_argument("--source", default=str(DEFAULT_SOURCE), help="Path to the workbook.")
        parser.add_argument("--dry-run", action="store_true", help="Report what would be created, write nothing.")

    def handle(self, *args, **options):
        import openpyxl

        from prep.models import PrepCourse

        source = Path(options["source"])
        if not source.is_file():
            raise SystemExit(f"Workbook not found: {source}")

        workbook = openpyxl.load_workbook(source, read_only=True, data_only=True)

        collected: dict[str, dict] = {}
        duplicates = 0
        rejected = 0
        truncated = 0

        for sheet_name in SHEETS:
            if sheet_name not in workbook.sheetnames:
                self.stdout.write(f"  ! sheet not found: {sheet_name}")
                continue

            rows = workbook[sheet_name].iter_rows(values_only=True)
            header = [str(h or "").strip().lower() for h in next(rows, [])]
            try:
                i_code = header.index("unit code")
                i_title = header.index("unit title")
            except ValueError:
                self.stdout.write(f"  ! missing 'Unit code'/'Unit title' header in {sheet_name}")
                continue
            i_dept = header.index("department") if "department" in header else None
            i_school = header.index("school") if "school" in header else None
            i_year = header.index("year / level") if "year / level" in header else None

            for row in rows:
                def cell(index):
                    return row[index] if index is not None and index < len(row) else None

                code = normalise_code(cell(i_code))
                title = normalise_title(cell(i_title))
                if not code or not title:
                    rejected += 1
                    continue
                if code in collected:
                    duplicates += 1
                    continue

                department = " ".join(
                    part for part in (cell(i_dept), cell(i_school)) if part
                ).strip()
                if len(title) > MAX_TITLE_LEN:
                    truncated += 1
                    title = truncate_title(title)
                collected[code] = {
                    "code": code,
                    "title": title,
                    "category": category_for(code, title, department),
                    "level": level_for(cell(i_year)),
                }

        existing = set(PrepCourse.objects.values_list("code", flat=True))
        new_units = [u for code, u in collected.items() if code not in existing]

        self.stdout.write(
            f"workbook rows parsed by code: {len(collected)} "
            f"(duplicates skipped: {duplicates}, rejected: {rejected}, "
            f"titles truncated to {MAX_TITLE_LEN}: {truncated})"
        )
        self.stdout.write(f"already in catalogue: {len(collected) - len(new_units)}")
        self.stdout.write(f"to create: {len(new_units)}")

        histogram = Counter(u["category"] for u in new_units)
        for category, count in histogram.most_common():
            self.stdout.write(f"    {category:<20} {count}")

        if options["dry_run"]:
            self.stdout.write(self.style.WARNING("dry run: nothing written"))
            for unit in new_units[:5]:
                self.stdout.write(
                    f"    e.g. {unit['code']:<10} {unit['title'][:50]:<52} {unit['category']:<20} {unit['level']}"
                )
            return

        # Bulk insert: one round-trip per batch instead of one per unit.
        rows = [
            PrepCourse(
                code=unit["code"],
                title=unit["title"],
                slug=slugify(unit["code"]),
                category=unit["category"],
                level=unit["level"],
            )
            for unit in new_units
        ]
        PrepCourse.objects.bulk_create(rows, batch_size=500, ignore_conflicts=True)

        # The library view caches its catalogue bundle; drop it so new units appear.
        for key in ("prep_pub_lib_courses_v3", "prep_pub_lib_courses"):
            cache.delete(key)

        self.stdout.write(
            self.style.SUCCESS(
                f"catalogue now holds {PrepCourse.objects.count()} courses "
                f"(attempted {len(rows)})"
            )
        )
