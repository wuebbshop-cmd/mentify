import os, sys
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
import django
django.setup()
from prep.models import PrepContentCache

entries = PrepContentCache.objects.filter(content_type="topic_notes").order_by('-updated_at')[:10]
for e in entries:
    p = e.payload if isinstance(e.payload, dict) else {}
    print("---")
    print("ID:", e.id, "Topic:", e.topic_id, "Key:", e.cache_key[:60])
    print("  level:", p.get("level"))
    print("  validation_state:", p.get("validation_state"))
    print("  review_status:", p.get("review_status"))
    print("  is_valid:", p.get("is_valid"))
    print("  content length:", len(str(p.get("content") or p.get("notes") or "")))
    print("  keys in payload:", list(p.keys()))
