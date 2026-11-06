import os, sys
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
import django
django.setup()
from prep.models import PrepTopic, PrepCourse, PrepContentCache
from services.prep_ai_router import get_published_topic_note_levels

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Sample some courses that have notes, e.g. SMA 200, SMA 330, SST 305
for code in ['SMA 200', 'SMA 330', 'SST 305', 'SMA 230']:
    course = PrepCourse.objects.filter(code=code).first()
    if not course:
        continue
    print(f"\n=== Course {code} ===")
    for topic in course.topics.all()[:5]:
        v_true = get_published_topic_note_levels(topic, validated_only=True)
        v_false = get_published_topic_note_levels(topic, validated_only=False)
        print(f"Topic [{topic.id}] '{topic.title}':")
        print(f"   validated_only=True:  {list(v_true.keys())}")
        print(f"   validated_only=False: {list(v_false.keys())}")
