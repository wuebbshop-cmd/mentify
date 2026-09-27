import os, sys, django
sys.path.insert(0, '.')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.development'
django.setup()

from prep.models import PrepCourse
from services.prep_ai_router import get_or_generate_topic_notes
from benchmark_validate import extract_text, CHECKS

course = PrepCourse.objects.get(slug='sma-300')

tasks = [
    ('The Real Number System', 'level_3'),
    ('Topology of the Real Numbers', 'level_2'),
    ('Topology of the Real Numbers', 'level_3'),
]

for title, level in tasks:
    topic = course.topics.filter(title__iexact=title).first()
    print(f"\n==========================================")
    print(f"Generating {course.code} - {title} ({level})...")
    res = get_or_generate_topic_notes(course.code, title, level=level, course_obj=course, topic_obj=topic)
    notes = res.get('notes', '')
    print(f"Generated: {len(notes)} chars")

    all_pass = True
    for name, fn in CHECKS:
        issues = fn(notes)
        status = 'PASS' if not issues else 'FAIL'
        if issues:
            all_pass = False
            clean_iss = issues[0].encode('ascii', 'replace').decode('ascii')
            print(f"  [{status}] {name} -> {clean_iss[:70]}")
        else:
            print(f"  [{status}] {name}")
    print(f"RESULT: {'ALL CHECKS PASSED' if all_pass else 'CHECKS FAILED'}")

print("\nDone with regeneration and validation!")
