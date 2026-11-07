"""Verify SMA 335 topic distribution and rendering after cross-listing."""
from __future__ import annotations

import os
import re
import sys
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django  # noqa: E402

django.setup()

from django.db.models import Q  # noqa: E402

from prep.models import PrepPaper, PrepQuestion, PrepTopic  # noqa: E402
from services.prep_ingestion import (  # noqa: E402
    assessment_question_rendering_issues,
    learner_visible_assessment_questions,
)

COURSE_ID = 57


def main() -> None:
    allq = PrepQuestion.objects.filter(Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID)).distinct()
    visible_statuses = PrepQuestion.LEARNER_VISIBLE_STATUSES
    print("course total rows:", allq.count())
    print("statuses:", dict(Counter(allq.values_list("verification_status", flat=True))))
    print("unmapped:", allq.filter(topic__isnull=True).count())
    print("flagged:", allq.filter(verification_status="flagged").count())
    print("pending:", allq.filter(verification_status="pending").count())
    print("render issues:", [q.id for q in allq if assessment_question_rendering_issues(q.question_latex or "")][:10])

    print()
    print("per-topic visible counts")
    for topic in PrepTopic.objects.filter(course_id=COURSE_ID).order_by("id"):
        n = allq.filter(topic=topic).filter(
            verification_status__in=visible_statuses
        ).filter(Q(paper__isnull=True) | Q(paper__is_published=True)).count()
        print(f"  {topic.id}  {n:3d}  {topic.title}")

    print()
    rendered, errors = 0, []
    for topic in PrepTopic.objects.filter(course_id=COURSE_ID).order_by("id"):
        records = (
            PrepQuestion.objects.filter(
                Q(topic=topic)
                | (
                    Q(topic__isnull=True)
                    & Q(paper__course_id=COURSE_ID)
                    & Q(topic_label__icontains=topic.title)
                ),
                verification_status__in=visible_statuses,
            )
            .filter(Q(paper__isnull=True) | Q(paper__is_published=True))
            .select_related("paper")
            .order_by("question_type", "paper__created_at", "number", "id")
        )
        try:
            rendered += len(learner_visible_assessment_questions(records))
        except Exception as exc:  # noqa: BLE001
            errors.append((topic.id, type(exc).__name__, str(exc)[:80]))
    print(f"topic render smoke test: {rendered} questions, errors: {errors}")

    # duplicate guard: same paper + topic + text appearing twice
    seen: Counter[tuple[str, int, str]] = Counter()
    for q in allq:
        if q.topic_id:
            seen[(q.paper_id or "", q.topic_id, " ".join((q.question_latex or "").split()))] += 1
    dupes = {k: v for k, v in seen.items() if v > 1}
    print("duplicate rows within one paper+topic:", len(dupes))


if __name__ == "__main__":
    main()
