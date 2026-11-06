import os
import re
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from django.db import transaction
from django.utils import timezone

from prep.models import PrepContentCache, PrepTopicNotesJob
from services.prep_ai_router import (
    _cache_payload_as_dict,
    _note_completion_issues,
    _note_validation_options,
    _topic_notes_cache_signature,
    NOTE_VALIDATION_STATE,
    normalize_math_delimiters,
)
from services.prep_sanitizer import purge_institutional_metadata


failed_jobs = list(
    PrepTopicNotesJob.objects.filter(status='failed')
    .exclude(last_error__startswith='Superseded')
    .select_related('topic__course')
    .order_by('topic__course__code', 'topic__order', 'level')
)


def repair_math_text(text: str) -> str:
    text = normalize_math_delimiters(text)
    text = re.sub(r'(?m)^\s*\$\$\s*$', '', text)
    text = re.sub(r'(?m)^\s*\$\s*$', '', text)
    lines = text.splitlines()
    fixed = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == '$$':
            i += 1
            continue
        if line.strip().startswith('|') and i + 1 < len(lines) and lines[i + 1].strip() == '$$':
            j = i + 2
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j < len(lines) and lines[j].strip() and not lines[j].strip().startswith('##') and not lines[j].strip().startswith('###'):
                line = line.rstrip() + ' ' + lines[j].strip()
                fixed.append(line)
                i = j + 1
                continue
        if line.strip().startswith('|') and i + 1 < len(lines) and lines[i + 1].strip().startswith('$$'):
            j = i + 2
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j < len(lines) and lines[j].strip() and not lines[j].strip().startswith('##') and not lines[j].strip().startswith('###'):
                line = line.rstrip() + ' ' + lines[j].strip()
                fixed.append(line)
                i = j + 1
                continue
        fixed.append(line)
        i += 1
    text = '\n'.join(fixed)
    text = re.sub(r'(?m)^\s*\$\$\s*\n\s*\$\$\s*$', '', text)
    text = re.sub(r'(?m)^\s*\$\$\s*\n\s*\$\$\s*\n\s*\$\$\s*$', '', text)
    text = re.sub(r'(?m)^\s*\$\$\s*\n\s*\$\$\s*\n\s*\$\$\s*\n\s*\$\$\s*$', '', text)
    text = purge_institutional_metadata(text)
    return text.strip() + '\n'

saved = 0
remaining = []
for job in failed_jobs:
    topic = job.topic
    sig = job.source_signature
    entry = PrepContentCache.objects.filter(topic=topic, content_type='topic_notes', cache_key__endswith=sig).order_by('-updated_at', '-id').first()
    if not entry:
        continue
    payload = _cache_payload_as_dict(entry.payload) or {}
    content = str(payload.get('content') or payload.get('notes') or '').strip()
    if not content:
        continue
    fixed = repair_math_text(content)
    options = _note_validation_options(topic.course, topic.title, topic.summary, topic.subtopics if isinstance(topic.subtopics, list) else [], topic_obj=topic)
    issues = _note_completion_issues(fixed, topic.title, **options)
    if not issues:
        payload['content'] = fixed
        payload['level'] = job.level
        payload['source_signature'] = sig
        payload['validation_state'] = NOTE_VALIDATION_STATE
        payload['validated_at'] = timezone.now().isoformat()
        payload['source_references'] = options.get('source_references') or payload.get('source_references') or []
        with transaction.atomic():
            e = PrepContentCache.objects.select_for_update().get(pk=entry.pk)
            e.payload = payload
            e.save(update_fields=['payload','updated_at'])
            j = PrepTopicNotesJob.objects.select_for_update().get(pk=job.pk)
            j.status = 'complete'
            j.completed_at = timezone.now()
            j.last_error = ''
            j.save(update_fields=['status','completed_at','last_error'])
        saved += 1
        print(f'SAVED | {topic.course.code} | {topic.title} | {job.level}')
    else:
        remaining.append((topic.course.code, topic.title, job.level, issues[:5]))
        print(f'REMAIN | {topic.course.code} | {topic.title} | {job.level} | {issues[:5]}')

print('SAVED_TOTAL', saved)
print('REMAINING_TOTAL', len(remaining))
for r in remaining[:20]:
    print(r)
