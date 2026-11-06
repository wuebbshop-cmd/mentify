import json
from pathlib import Path

import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
django.setup()

from django.db import close_old_connections
from prep.models import (
    PrepContentCache,
    PrepCourse,
    PrepDocument,
    PrepNoteGenerationGuard,
    PrepNoteRepair,
    PrepQuestion,
    PrepTopicNotesJob,
    PrepTopic,
)
from services.prep_ai_router import (
    NOTES_CACHE_VERSION,
    _approved_course_source_context,
    _course_study_profile,
    _note_validation_options,
    _required_note_sections,
    _topic_notes_cache_signature,
    compute_cache_key,
)

course = PrepCourse.objects.get(code="SST 305")
topic = PrepTopic.objects.get(pk=50, course=course)
level = "level_2"
profile = _course_study_profile(course)
options = _note_validation_options(
    course, topic.title, topic.summary, topic.subtopics, topic_obj=topic
)
source_signature = _topic_notes_cache_signature(
    course, topic, topic.title, topic.subtopics
)
cache_key = compute_cache_key(
    "notes", NOTES_CACHE_VERSION, course.code, topic.title, level, source_signature
)
current_entry = PrepContentCache.objects.filter(
    cache_key=cache_key, topic=topic, content_type="topic_notes"
).first()
current_payload = (
    current_entry.payload
    if current_entry and isinstance(current_entry.payload, dict)
    else {}
)

source_lesson = ""
for document in PrepDocument.objects.filter(
    course=course, doc_type="Lecture Notes", stage="stage_3"
).order_by("created_at"):
    text = str(document.extracted_text or "")
    start = text.find("LESSON SIX")
    end = text.find("LESSON SEVEN", start + 1) if start >= 0 else -1
    if start >= 0:
        source_lesson = text[start:end] if end > start else text[start:start + 12000]
        break

past_questions = []
for question in PrepQuestion.objects.filter(
    topic=topic,
    verification_status__in=PrepQuestion.ANSWERABLE_STATUSES,
).order_by("number", "id")[:8]:
    past_questions.append({
        "number": question.number,
        "marks": question.marks,
        "verification_status": question.verification_status,
        "question": question.question_latex,
        "solution": question.solution_latex,
    })

cache_rows = []
for entry in PrepContentCache.objects.filter(
    topic=topic, content_type="topic_notes"
).order_by("-updated_at"):
    payload = entry.payload if isinstance(entry.payload, dict) else {}
    cache_rows.append({
        "cache_key": entry.cache_key,
        "level": payload.get("level"),
        "model": payload.get("model"),
        "validation_state": payload.get("validation_state"),
        "source_signature": payload.get("source_signature"),
        "characters": len(str(payload.get("content") or "")),
        "is_current_key": entry.cache_key == cache_key,
    })

repairs = list(PrepNoteRepair.objects.filter(topic=topic).values(
    "level", "status", "validation_issues", "cache_key", "last_error"
))
guards = list(PrepNoteGenerationGuard.objects.filter(topic=topic).values(
    "level", "status", "failed_attempts", "last_error", "source_signature"
))
jobs = list(PrepTopicNotesJob.objects.filter(
    topic=topic, level=level, source_signature=source_signature
).values("status", "attempts", "model_name", "last_error", "queued_at", "completed_at"))

previous_topics = list(
    course.topics.filter(order__lt=topic.order).order_by("order").values_list("title", flat=True)
)
future_topics = list(
    course.topics.filter(order__gt=topic.order).order_by("order").values_list("title", flat=True)
)

export = {
    "course": {"code": course.code, "title": course.title},
    "topic": {
        "id": topic.pk,
        "title": topic.title,
        "summary": topic.summary,
        "subtopics": topic.subtopics,
        "content_rules": topic.content_rules,
    },
    "level": level,
    "course_study_profile": profile,
    "required_note_sections": _required_note_sections(topic.title, profile),
    "level_2_instruction": (
        "Rigorous academic standard: use precise definitions and appropriate academic rigor; "
        "include representative worked examples grounded in approved notes; use formal notation "
        "only when supported by approved sources."
    ),
    "validation_options": {
        "allow_math": options["allow_math"],
        "allow_code": options["allow_code"],
        "allow_chemical_equations": options["allow_chemical_equations"],
        "content_rules": options["content_rules"],
        "content_rule_issues": options["content_rule_issues"],
        "source_references": options["source_references"],
    },
    "approved_source_excerpt": _approved_course_source_context(
        course, topic.title, limit=12000
    ),
    "approved_topic_lesson_source": source_lesson,
    "current_level_2_content": str(
        current_payload.get("content") or current_payload.get("notes") or ""
    ),
    "relevant_verified_questions": past_questions,
    "curriculum_prior_topics": previous_topics,
    "curriculum_future_topics": future_topics,
    "notes_cache_version": NOTES_CACHE_VERSION,
    "source_signature": source_signature,
    "current_cache_key": cache_key,
    "cache_rows": cache_rows,
    "repair_records": repairs,
    "generation_guards": guards,
    "generation_jobs": jobs,
}

output_path = Path(__file__).with_name("topic_50_prompt_data.json")
output_path.write_text(json.dumps(export, ensure_ascii=False, indent=2), encoding="utf-8")
print("EXPORTED", output_path.name, "lesson_source_chars=", len(source_lesson))
print("PROFILE_SECTIONS", profile.get("note_structure", []))
print("REQUIRED_HEADINGS", export["required_note_sections"])
print("VALIDATION", export["validation_options"]["content_rule_issues"])
print("QUESTIONS", len(past_questions), "CACHE_ROWS", len(cache_rows), "REPAIRS", len(repairs), "GUARDS", len(guards), "JOBS", len(jobs))
