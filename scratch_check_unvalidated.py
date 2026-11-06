import os, sys
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
import django
django.setup()
from prep.models import PrepContentCache, PrepTopic
from services.prep_ai_router import NOTE_VALIDATION_STATE

entries = PrepContentCache.objects.filter(content_type="topic_notes")
unvalidated_entries = []
for e in entries:
    p = e.payload if isinstance(e.payload, dict) else {}
    val = p.get("validation_state")
    rev = p.get("review_status")
    c = str(p.get("content") or p.get("notes") or "").strip()
    if val != NOTE_VALIDATION_STATE or rev == "skipped_no_source" or not c:
        unvalidated_entries.append((e.id, e.topic_id, e.cache_key, val, rev, len(c)))

print(f"Total unvalidated or skipped cache entries: {len(unvalidated_entries)}")
for ue in unvalidated_entries[:15]:
    t = PrepTopic.objects.filter(id=ue[1]).first()
    t_info = f"{t.course.code} Topic {t.id} '{t.title}'" if t else "No topic"
    print(" ", ue, t_info)
