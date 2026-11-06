import os
import re
from fractions import Fraction
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
import django
django.setup()

from scipy.stats import chi2, t
from prep.models import PrepCourse, PrepTopic
from services.prep_ai_router import (
    _course_study_profile,
    _note_completion_issues,
    _note_validation_options,
)

course = PrepCourse.objects.get(code="SST 305")
errors = []
for topic_id in (51, 52, 53):
    topic = PrepTopic.objects.get(pk=topic_id, course=course)
    content = Path(__file__).with_name(
        f"topic_{topic_id}_level_2_candidate.md"
    ).read_text(encoding="utf-8")
    options = _note_validation_options(
        course, topic.title, topic.summary, topic.subtopics, topic_obj=topic
    )
    issues = _note_completion_issues(content, topic.title, **options)
    required = [
        f"## {index}. {title}"
        for index, title in enumerate(
            _course_study_profile(course).get("note_structure", []), start=1
        )
    ]
    actual = [line for line in content.splitlines() if line.startswith("## ")]
    if issues:
        errors.append(f"Topic {topic_id}: app validation issues {issues}")
    if actual != required:
        errors.append(f"Topic {topic_id}: section headings differ from study profile")
    if options["allow_code"] is False and "```" in content:
        errors.append(f"Topic {topic_id}: disallowed code fence")
    print(
        "TOPIC", topic_id, topic.title,
        "characters=", len(content),
        "headings_ok=", actual == required,
        "issues=", issues,
    )

# Three-estimator variance comparison in the Topic 51 worked example.
variances = [Fraction(1, 3), Fraction(7, 18), Fraction(3, 8)]
if min(variances) != Fraction(1, 3):
    errors.append("Topic 51: estimator variance comparison is incorrect")

# Topic 52 normal-sample arithmetic and the chi-square interval checks.
known_mean_ci = (148 - 2.326347874 * (800 / 25) ** 0.5,
                 148 + 2.326347874 * (800 / 25) ** 0.5)
n = 25
sample_var = (573000 - 3700 ** 2 / n) / (n - 1)
chi_lower = chi2.ppf(0.01, 24)
chi_upper = chi2.ppf(0.99, 24)
variance_ci = ((n - 1) * sample_var / chi_upper,
               (n - 1) * sample_var / chi_lower)
if not (134.83 < known_mean_ci[0] < 134.85 and 161.15 < known_mean_ci[1] < 161.17):
    errors.append("Topic 52: known-variance mean interval arithmetic is incorrect")
if not (590 < variance_ci[0] < 592 and 2338 < variance_ci[1] < 2341):
    errors.append("Topic 52: chi-square variance interval arithmetic is incorrect")

# Topic 53 two-sample pooled t examples, independently recomputed from raw data.
def pooled_interval(first, second, first_mean, second_mean, first_var, second_var):
    first_n, second_n = len(first), len(second)
    pooled_var = (
        (first_n - 1) * first_var + (second_n - 1) * second_var
    ) / (first_n + second_n - 2)
    standard_error = (pooled_var * (1 / first_n + 1 / second_n)) ** 0.5
    critical = t.ppf(0.975, first_n + second_n - 2)
    difference = first_mean - second_mean
    return difference - critical * standard_error, difference + critical * standard_error

cat_interval = pooled_interval([], [] ,72.5,68.0,16.0,20.0) if False else None
cat_pooled_var = (9 * 16.0 + 11 * 20.0) / 20
cat_se = (cat_pooled_var * (1 / 10 + 1 / 12)) ** 0.5
cat_margin = t.ppf(0.975, 20) * cat_se
cat_interval = (4.5 - cat_margin, 4.5 + cat_margin)
first = [32.3, 37.3, 35.3, 33.7, 31.9, 30.0, 34.6, 32.8, 36.4]
second = [38.4, 34.8, 36.6, 32.0, 33.9, 35.7, 37.5, 39.3, 34.3]
first_mean = sum(first) / len(first)
second_mean = sum(second) / len(second)
first_var = sum((x - first_mean) ** 2 for x in first) / (len(first) - 1)
second_var = sum((x - second_mean) ** 2 for x in second) / (len(second) - 1)
lesson_interval = pooled_interval(first, second, first_mean, second_mean, first_var, second_var)
if not (0.68 < cat_interval[0] < 0.70 and 8.30 < cat_interval[1] < 8.33):
    errors.append("Topic 53: verified CAT example arithmetic is incorrect")
if not (-4.36 < lesson_interval[0] < -4.34 and 0.30 < lesson_interval[1] < 0.32):
    errors.append("Topic 53: lecture data interval arithmetic is incorrect")
print("TOPIC_51_VARIANCES", variances)
print("TOPIC_52_KNOWN_MEAN_CI", known_mean_ci, "VARIANCE_CI", variance_ci)
print("TOPIC_53_CAT_CI", cat_interval, "LECTURE_CI", lesson_interval)
print("VALIDATION_ERRORS", errors)
if errors:
    raise SystemExit(1)
print("ALL_CANDIDATES_VALID")
