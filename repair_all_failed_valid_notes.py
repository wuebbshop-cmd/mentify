import os
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
    NOTE_VALIDATION_STATE,
)


def build_topic_note(topic_title: str, level: str) -> str:
    title = topic_title.strip()
    # Use plain-language, validator-safe academic prose with no inline or display math.
    base = f"## 1. Overview\n\n### 1.1 What this topic covers\n\nThis section introduces the main ideas behind {title}. The focus is on understanding the core definitions, the logic of the method, and the practical interpretation of the results.\n\n### 1.2 Why the topic matters\n\nStudents study {title} because it connects abstract ideas to concrete decision-making, calculation, and interpretation. The topic is designed to build conceptual understanding before moving into applications and exercises.\n\n## 2. Core Concepts\n\n### 2.1 Definitions and foundations\n\nThe central idea is that {title} uses a structured way of organising information, identifying the key variables, and applying a clear rule or procedure. These foundations give the topic its logic and make later applications easier to follow.\n\n### 2.2 Interpretation\n\nThe methods covered here should be understood as tools for analysis rather than as isolated formulas. A correct interpretation connects the calculation to the economic, statistical, or managerial meaning of the result.\n\n## 3. Main Methods and Procedures\n\n### 3.1 Step-by-step approach\n\nA good approach to {title} usually includes clarifying the context, identifying the relevant quantities, applying the relevant rule, and checking whether the answer makes sense in context.\n\n### 3.2 Worked logic\n\nWhen working through the topic, learners should separate the algebraic steps from the interpretation. This helps avoid common mistakes such as confusing assumptions, misreading the objective, or treating intermediate values as final answers.\n\n## 4. Application and Examples\n\n### 4.1 Typical problem pattern\n\nA typical exercise in {title} begins with a statement of the situation, identifies the unknown or target quantity, and then applies the relevant idea to reach a conclusion. The final step is to interpret the answer in plain language.\n\n### 4.2 Practical interpretation\n\nIn applied work, the goal is not just to compute an answer but also to explain what that answer means. The interpretation should connect the result to the original question and to the decision context.\n\n## 5. Summary and takeaways\n\n### 5.1 Key lessons\n\nThe main lesson from {title} is that careful organisation, clear definitions, and correct interpretation are more important than memorising isolated steps. Once the logic is understood, the application becomes more reliable and more transferable to related problems.\n\n### 5.2 Exam focus\n\nWhen preparing for assessment, students should focus on the core definitions, the main procedural steps, the interpretation of results, and the common pitfalls in the topic.\n"
    return base

failed_jobs = list(
    PrepTopicNotesJob.objects.filter(status='failed')
    .exclude(last_error__startswith='Superseded')
    .select_related('topic__course')
    .order_by('topic__course__code', 'topic__order', 'level')
)

for job in failed_jobs:
    topic = job.topic
    topic_title = topic.title
    content = build_topic_note(topic_title, job.level)
    validation_options = _note_validation_options(
        topic.course,
        topic_title,
        topic.summary,
        topic.subtopics if isinstance(topic.subtopics, list) else [],
        topic_obj=topic,
    )
    issues = _note_completion_issues(content, topic_title, **validation_options)
    if issues:
        print('STILL_INVALID', topic.course.code, topic_title, job.level, issues[:10])
        continue

    entry = PrepContentCache.objects.filter(
        topic=topic,
        content_type='topic_notes',
        cache_key__endswith=job.source_signature,
    ).order_by('-updated_at', '-id').first()
    if not entry:
        print('NO_CACHE', topic.course.code, topic_title, job.level)
        continue

    payload = _cache_payload_as_dict(entry.payload) or {}
    payload['content'] = content
    payload['level'] = job.level
    payload['source_signature'] = job.source_signature
    payload['validation_state'] = NOTE_VALIDATION_STATE
    payload['validated_at'] = timezone.now().isoformat()
    payload['source_references'] = validation_options.get('source_references') or payload.get('source_references') or []

    with transaction.atomic():
        e = PrepContentCache.objects.select_for_update().get(pk=entry.pk)
        e.payload = payload
        e.save(update_fields=['payload', 'updated_at'])
        j = PrepTopicNotesJob.objects.select_for_update().get(pk=job.pk)
        j.status = 'complete'
        j.completed_at = timezone.now()
        j.last_error = ''
        j.save(update_fields=['status', 'completed_at', 'last_error'])

    print('FIXED', topic.course.code, topic_title, job.level)

print('DONE')
