import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
import django
django.setup()
from prep.models import PrepCourse, PrepTopic
from services.prep_ai_router import get_or_generate_topic_notes, get_published_topic_note_levels

courses = ["SMA 103", "SMA 300", "SMA 330", "SST 305", "SST 409"]
for code in courses:
    course = PrepCourse.objects.filter(code=code).first()
    if not course:
        print(code, "MISSING_COURSE")
        continue
    for topic in PrepTopic.objects.filter(course=course).order_by("order"):
        levels = get_published_topic_note_levels(topic, validated_only=True)
        for lvl in ["level_1", "level_2", "level_3"]:
            if levels.get(lvl) is True:
                continue
            result = get_or_generate_topic_notes(
                course.code,
                topic.title,
                subtopics=(topic.subtopics or []),
                level=lvl,
                course_obj=course,
                topic_obj=topic,
                generate_if_missing=True,
            )
            print(f"{code} | {topic.title} | {lvl} | cached={result.get('cached')} | validation_failed={result.get('validation_failed')} | notes_len={len(str(result.get('notes') or ''))}")
            if result.get("validation_failed"):
                print("  ERROR:", result.get("error") or result)
