import os, sys
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
import django; django.setup()

from prep.models import PrepCourse
from prep.views import _get_course_topics_summary
from django.core.cache import cache

# Clear any old cache so we get fresh results
cache.clear()

for code in ['SMA 330', 'SST 101', 'SST 202', 'SST 304']:
    c = PrepCourse.objects.filter(code=code).first()
    if not c:
        print(f"{code}: NOT FOUND")
        continue
    data, _ = _get_course_topics_summary(c)
    print(f"\n=== {code} ===")
    for td in data:
        print(f"  Topic {td['id']} '{td['title']}': dots={td['ready_levels_count']}  levels={[l['key'] for l in td.get('ready_levels_list', [])]}")
