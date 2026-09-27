"""
regenerate_benchmarks.py
─────────────────────────
Deletes the 3 benchmark PrepContentCache entries and regenerates them
through the locked-down AI router (new strict authoring format prompt).

Run from the EduAI project root:
    python regenerate_benchmarks.py

After regeneration, run benchmark_validate.py to verify.
"""

import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
django.setup()

from prep.models import PrepContentCache, PrepTopic, PrepCourse  # noqa: E402
from services.prep_ai_router import get_or_generate_topic_notes  # noqa: E402

# Exact cache keys to flush and regenerate
TARGETS = [
    "notes:sst_301_matrices_in_r_level_2",
    "notes:sst_301_differentiation_&_integration_of_univariate_functions_level_2",
    "notes:sma_300_the_real_number_system_level_2",
]

def run():
    print("=" * 72)
    print("BENCHMARK CACHE REGENERATION")
    print("=" * 72)

    for key in TARGETS:
        print(f"\n[FLUSH] {key}")
        deleted, _ = PrepContentCache.objects.filter(cache_key=key).delete()
        print(f"        Deleted {deleted} cache record(s)")

        # Parse cache key to find course_code, topic_title, level
        # Format: notes:{course_code_underscore}_{topic_title_underscore}_{level}
        # We strip the "notes:" prefix then extract level suffix
        raw = key.removeprefix("notes:")
        # Extract level
        for level_suffix in ("_level_1", "_level_2", "_level_3"):
            if raw.endswith(level_suffix):
                level = level_suffix.lstrip("_")  # e.g. "level_2"
                rest = raw[: -len(level_suffix)]  # e.g. "sst_301_matrices_in_r"
                break
        else:
            print(f"        [SKIP] Cannot parse level from key: {key}")
            continue

        # Find the PrepTopic matching this key fragment
        # Try to match topic by slug or by looking up via course
        topic = None
        course = None

        # Extract course code guess (first segment before topic part)
        # e.g. "sst_301_matrices_in_r" -> course might be SST 301
        #      "sma_300_the_real_number_system" -> course SMA 300
        for course_slug in ["sst-301", "sma-300"]:
            try:
                c = PrepCourse.objects.get(slug=course_slug)
                course_code_normalized = course_slug.replace("-", "_")
                if rest.startswith(course_code_normalized):
                    topic_slug_frag = rest[len(course_code_normalized):].lstrip("_")
                    # Try to find topic by slug containing the fragment
                    t = c.topics.filter(slug__icontains=topic_slug_frag[:20]).first()
                    if not t:
                        # Try title match
                        t = c.topics.filter(title__icontains=topic_slug_frag[:20].replace("_", " ")).first()
                    if t:
                        topic = t
                        course = c
                        break
            except PrepCourse.DoesNotExist:
                continue

        if not topic or not course:
            print(f"        [WARN] Could not resolve topic object — regenerating with name-only fallback")
            # Derive course code and topic title from the key as best guess
            # e.g. "sst_301" -> "SST 301", rest minus course prefix -> topic
            parts = rest.split("_")
            if len(parts) >= 2:
                course_code = (parts[0] + " " + parts[1]).upper()
                topic_title = " ".join(parts[2:]).replace("_", " ").title()
            else:
                course_code = "Unknown"
                topic_title = rest.replace("_", " ").title()
        else:
            course_code = course.code
            topic_title = topic.title
            print(f"        Course: {course_code}, Topic: {topic_title}, Level: {level}")

        print(f"        Regenerating: course={course_code!r}, topic={topic_title!r}, level={level!r}")

        result = get_or_generate_topic_notes(
            course_code=course_code,
            topic_title=topic_title,
            level=level,
            course_obj=course,
            topic_obj=topic,
        )

        if result.get("notes") and not result["notes"].startswith("Notes could not"):
            preview = result["notes"][:200].replace("\n", " ")
            print(f"        [OK] Regenerated ({len(result['notes']):,} chars). Preview: {preview!r}")
        else:
            print(f"        [FAIL] Regeneration failed: {result.get('error', 'unknown error')}")

    print()
    print("=" * 72)
    print("Done. Run: python benchmark_validate.py")
    print("=" * 72)


if __name__ == "__main__":
    run()
