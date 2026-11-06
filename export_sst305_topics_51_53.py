import json
import os
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
import django
django.setup()

from prep.models import (
    PrepContentCache,
    PrepCourse,
    PrepNoteGenerationGuard,
    PrepNoteRepair,
    PrepQuestion,
    PrepTopic,
    PrepTopicNotesJob,
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

for topic_id in (51, 52, 53):
    topic = PrepTopic.objects.get(pk=topic_id, course=course)
    level = "level_2"
    profile = _course_study_profile(course)
    options = _note_validation_options(
        course, topic.title, topic.summary, topic.subtopics, topic_obj=topic
    )
    signature = _topic_notes_cache_signature(
        course, topic, topic.title, topic.subtopics
    )
    cache_key = compute_cache_key(
        "notes", NOTES_CACHE_VERSION, course.code, topic.title, level, signature
    )

    questions = []
    for question in PrepQuestion.objects.filter(
        topic=topic,
        verification_status__in=PrepQuestion.ANSWERABLE_STATUSES,
    ).order_by("number", "id")[:8]:
        questions.append({
            "number": question.number,
            "marks": question.marks,
            "verification_status": question.verification_status,
            "question": question.question_latex,
            "solution": question.solution_latex,
        })

    rows = []
    current_content = ""
    for entry in PrepContentCache.objects.filter(
        topic=topic, content_type="topic_notes"
    ).order_by("-updated_at"):
        payload = entry.payload if isinstance(entry.payload, dict) else {}
        content = str(payload.get("content") or payload.get("notes") or "")
        if entry.cache_key == cache_key:
            current_content = content
        rows.append({
            "cache_key": entry.cache_key,
            "level": payload.get("level"),
            "model": payload.get("model"),
            "validation_state": payload.get("validation_state"),
            "source_signature": payload.get("source_signature"),
            "characters": len(content),
            "is_current_key": entry.cache_key == cache_key,
        })

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
        "current_level_2_content": current_content,
        "relevant_verified_questions": questions,
        "curriculum_prior_topics": list(
            course.topics.filter(order__lt=topic.order)
            .order_by("order").values_list("title", flat=True)
        ),
        "curriculum_future_topics": list(
            course.topics.filter(order__gt=topic.order)
            .order_by("order").values_list("title", flat=True)
        ),
        "notes_cache_version": NOTES_CACHE_VERSION,
        "source_signature": signature,
        "current_cache_key": cache_key,
        "cache_rows": rows,
        "repair_records": list(PrepNoteRepair.objects.filter(topic=topic).values(
            "level", "status", "validation_issues", "cache_key", "last_error"
        )),
        "generation_guards": list(PrepNoteGenerationGuard.objects.filter(topic=topic).values(
            "level", "status", "failed_attempts", "last_error", "source_signature"
        )),
        "generation_jobs": list(PrepTopicNotesJob.objects.filter(
            topic=topic, level=level, source_signature=signature
        ).values("status", "attempts", "model_name", "last_error", "queued_at", "completed_at")),
    }

    output_path = Path(__file__).with_name(f"topic_{topic_id}_prompt_data.json")
    output_path.write_text(json.dumps(export, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        "EXPORTED", topic_id, topic.title,
        "source_chars=", len(export["approved_source_excerpt"]),
        "questions=", len(questions),
        "cache_rows=", len(rows),
        "repairs=", len(export["repair_records"]),
        "guards=", len(export["generation_guards"]),
        "jobs=", len(export["generation_jobs"]),
    )
