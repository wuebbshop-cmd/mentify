import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from prep.models import PrepTopic, PrepContentCache, PrepTopicNotesJob
from services.prep_ai_router import _cache_payload_as_dict, _note_completion_issues, _note_validation_options, NOTE_VALIDATION_STATE
from services.prep_blocks import parse_markdown_to_blocks, validate_structured_blocks


t = PrepTopic.objects.select_related('course').get(course__code='SST 401', title='Overview And Lesson Plans (Lessons 1–11)')
job = PrepTopicNotesJob.objects.filter(topic=t, level='level_2').order_by('-attempts', '-id').first()
entry = PrepContentCache.objects.filter(topic=t, content_type='topic_notes').order_by('-updated_at').first()
payload = _cache_payload_as_dict(entry.payload) or {}
content = str(payload.get('content') or '')
start = content.find('**Formulation without the rating organization.**')
if start < 0:
    raise RuntimeError('Target section not found')

replacement = '''**Formulation without the rating organization.** The decision alternatives are *extend credit* and *do not extend credit*. The states of nature are the actual credit record of the customer: poor, average, good. The payoff table, with prior probabilities attached, is:

| Alternative | Poor risk | Average risk | Good risk |
| --- | --- | --- | --- |
| Extend credit | $-\$15{,}000$ | $10{,}000$ | $20{,}000$ |
| Do not extend credit | $0$ | $0$ | $0$ |
| Prior probabilities | $0.2$ | $0.5$ | $0.3$ |

'''
new_content = content[:start] + replacement + content[content.find('This table is the canonical output of Lesson 1.', start):]

validation_options = _note_validation_options(t.course, t.title, t.summary, t.subtopics if isinstance(t.subtopics, list) else [], topic_obj=t)
issues = _note_completion_issues(new_content, t.title, **validation_options)
print('ISSUES', issues)
if not issues:
    payload['content'] = new_content
    payload['validation_state'] = NOTE_VALIDATION_STATE
    payload['validated_at'] = __import__('django.utils.timezone').utils.timezone.now().isoformat()
    payload['source_references'] = payload.get('source_references') or []
    entry.payload = payload
    entry.save(update_fields=['payload', 'updated_at'])
    if job:
        job.status = 'complete'
        job.completed_at = __import__('django.utils.timezone').utils.timezone.now()
        job.last_error = ''
        job.save(update_fields=['status', 'completed_at', 'last_error'])
    print('VALIDATED_AND_SAVED')
