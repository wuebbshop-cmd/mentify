import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from django.utils import timezone
from prep.models import PrepTopicNotesJob
from services.prep_ai_router import _topic_notes_cache_signature
from services.prep_note_precompute import _has_current_topic_note_cache

updated = []
for job in PrepTopicNotesJob.objects.filter(status='failed').select_related('topic', 'topic__course'):
    topic = job.topic
    if not topic:
        continue
    current_sig = _topic_notes_cache_signature(
        topic.course,
        topic,
        topic.title,
        topic.subtopics if isinstance(topic.subtopics, list) else [],
    )
    if not _has_current_topic_note_cache(topic, job.level, current_sig):
        continue
    existing_current_sig = PrepTopicNotesJob.objects.filter(
        topic=topic,
        level=job.level,
        source_signature=current_sig,
    ).exclude(pk=job.pk).exists()
    update_fields = ['status', 'completed_at', 'last_error']
    if not existing_current_sig and job.source_signature != current_sig:
        job.source_signature = current_sig
        update_fields.insert(0, 'source_signature')
    job.status = 'complete'
    job.completed_at = timezone.now()
    job.last_error = ''
    job.save(update_fields=update_fields)
    updated.append((topic.course.code, topic.title, job.level, current_sig[:12]))

print(f'RECOVERED {len(updated)}')
for row in updated[:50]:
    print(row)
