import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from django.db import transaction
from django.utils import timezone

from prep.models import PrepContentCache, PrepTopic, PrepTopicNotesJob
from services.prep_ai_router import (
    _cache_payload_as_dict,
    _note_completion_issues,
    _note_validation_options,
    _repair_safe_math_text_issues,
    _topic_notes_cache_signature,
    NOTE_VALIDATION_STATE,
    normalize_math_delimiters,
)

failed_jobs = list(
    PrepTopicNotesJob.objects.filter(status='failed')
    .exclude(last_error__startswith='Superseded')
    .select_related('topic__course')
    .order_by('topic__course__code', 'topic__order', 'level')
)
seen = set()
count_saved = 0
count_left = 0

for job in failed_jobs:
    topic = job.topic
    key = (topic.pk, job.level, job.source_signature)
    if key in seen:
        continue
    seen.add(key)

    entry = PrepContentCache.objects.filter(
        topic=topic,
        content_type='topic_notes',
        cache_key__endswith=job.source_signature,
    ).order_by('-updated_at', '-id').first()
    if not entry:
        continue

    payload = _cache_payload_as_dict(entry.payload) or {}
    content = str(payload.get('content') or payload.get('notes') or '').strip()
    if not content:
        continue

    fixed = normalize_math_delimiters(content)
    fixed = _repair_safe_math_text_issues(fixed)
    validation_options = _note_validation_options(
        topic.course,
        topic.title,
        topic.summary,
        topic.subtopics if isinstance(topic.subtopics, list) else [],
        topic_obj=topic,
    )
    issues = _note_completion_issues(fixed, topic.title, **validation_options)

    if not issues:
        payload.update({
            'content': fixed,
            'validation_state': NOTE_VALIDATION_STATE,
            'validated_at': timezone.now().isoformat(),
            'level': job.level,
            'source_signature': job.source_signature,
            'source_references': validation_options.get('source_references') or payload.get('source_references') or [],
        })
        with transaction.atomic():
            entry = PrepContentCache.objects.select_for_update().get(pk=entry.pk)
            entry.payload = payload
            entry.save(update_fields=['payload', 'updated_at'])
            job = PrepTopicNotesJob.objects.select_for_update().get(pk=job.pk)
            job.status = 'complete'
            job.completed_at = timezone.now()
            job.last_error = ''
            job.save(update_fields=['status', 'completed_at', 'last_error'])
        count_saved += 1
        print(f'SAVED {topic.course.code} | {topic.title} | {job.level}')
    else:
        count_left += 1
        print(f'REMAINING {topic.course.code} | {topic.title} | {job.level} | {issues[:4]}')

print('SAVED_COUNT', count_saved)
print('REMAINING_COUNT', count_left)
