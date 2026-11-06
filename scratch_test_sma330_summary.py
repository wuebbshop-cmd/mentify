import os, sys
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
import django
django.setup()
from prep.models import PrepCourse
from prep.views import _get_course_topics_summary

course = PrepCourse.objects.filter(code="SMA 330").first()
topics_data, total_q = _get_course_topics_summary(course)
for td in topics_data[:5]:
    print(f"Topic {td['id']} '{td['title']}': ready_levels={td['ready_levels']}, count={td['ready_levels_count']}")
