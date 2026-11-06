import os
import re
from fractions import Fraction
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
import django
django.setup()

from prep.models import PrepCourse, PrepTopic
from services.prep_ai_router import (
    _note_completion_issues,
    _note_validation_options,
    _required_note_sections,
    _course_study_profile,
)

course = PrepCourse.objects.get(code="SST 305")
topic = PrepTopic.objects.get(pk=50, course=course)
content = Path(__file__).with_name("topic_50_level_2_candidate.md").read_text(encoding="utf-8")
profile = _course_study_profile(course)
options = _note_validation_options(
    course, topic.title, topic.summary, topic.subtopics, topic_obj=topic
)
issues = _note_completion_issues(content, topic.title, **options)
required_sections = [
    f"## {index}. {title}"
    for index, title in enumerate(profile.get("note_structure", []), start=1)
]
actual_sections = [line for line in content.splitlines() if line.startswith("## ")]

x_values = [6, -4, 10, 8, 4, 13, 2]
y_values = [20, 18, 6, 2, 13, 22, 5]
sum_x = sum(x_values)
sum_y = sum(y_values)
sum_x_squared = sum(value * value for value in x_values)
sum_xy = sum(x * y for x, y in zip(x_values, y_values))
determinant = len(x_values) * sum_x_squared - sum_x * sum_x
slope = Fraction(len(x_values) * sum_xy - sum_x * sum_y, determinant)
intercept = Fraction(sum_y - slope * sum_x, len(x_values))

errors = list(issues)
if actual_sections != required_sections:
    errors.append("section headings do not match the approved study profile")
if options["allow_code"] is False and "```" in content:
    errors.append("code block is disallowed for this topic")
if (sum_x, sum_y, sum_x_squared, sum_xy) != (39, 86, 405, 472):
    errors.append("seven-point question totals do not match the raw data")
if (intercept, slope) != (Fraction(2737, 219), Fraction(-25, 657)):
    errors.append("seven-point least-squares estimates do not match exact arithmetic")
if re.search(r"445|436|13\.3413|0\.1895", content):
    errors.append("candidate contains superseded incorrect CAT results")
if re.search(r"\\\\[A-Za-z]", content):
    errors.append("a matrix row separator is immediately followed by a LaTeX command")

print("CONTENT_LENGTH", len(content))
print("LINE_COUNT", len(content.splitlines()))
print("APPROVED_SECTIONS", actual_sections)
print("MATH_ALLOWED", options["allow_math"], "CODE_ALLOWED", options["allow_code"])
print("CAT_TOTALS", sum_x, sum_y, sum_x_squared, sum_xy)
print("CAT_ESTIMATES", "alpha=", intercept, float(intercept), "beta=", slope, float(slope))
print("VALIDATION_ISSUES", errors)
if errors:
    raise SystemExit(1)
print("VALIDATION_PASSED")
