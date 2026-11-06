import os, sys
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
import django
django.setup()
from prep.models import PrepContentCache
from collections import Counter

entries = PrepContentCache.objects.filter(content_type="topic_notes")
val_states = Counter()
rev_statuses = Counter()
empty_content = 0

for e in entries:
    p = e.payload if isinstance(e.payload, dict) else {}
    val_states[p.get("validation_state")] += 1
    rev_statuses[p.get("review_status")] += 1
    c = str(p.get("content") or p.get("notes") or "").strip()
    if not c:
        empty_content += 1

print("Total topic_notes cache entries:", entries.count())
print("Validation states:", dict(val_states))
print("Review statuses:", dict(rev_statuses))
print("Empty content count:", empty_content)
