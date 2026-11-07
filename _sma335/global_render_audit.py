"""Course-wide rendering audit: nothing hidden without a legitimate reason, nothing twice.

Run after the dedupe change in learner_visible_assessment_questions to confirm every
course still renders all of its distinct questions.
"""
from __future__ import annotations

import io
import os
import sys
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import django  # noqa: E402

django.setup()

from django.db.models import Q  # noqa: E402

from prep.models import PrepCourse, PrepQuestion, PrepTopic  # noqa: E402
from services.prep_ai_router import normalize_math_delimiters  # noqa: E402
from services.prep_ingestion import assessment_question_rendering_issues, learner_visible_assessment_questions  # noqa: E402


def norm(text: str) -> str:
    return " ".join(normalize_math_delimiters(text or "").split()).casefold()


def main() -> None:
    failures = 0
    for course in PrepCourse.objects.order_by("code"):
        topics = list(PrepTopic.objects.filter(course=course).order_by("id"))
        if not topics:
            continue
        course_fail = 0
        shown_total = 0
        for topic in topics:
            topic_match = Q(topic=topic) | (
                Q(topic__isnull=True) & Q(paper__course=course) & Q(topic_label__icontains=topic.title)
            )
            records = list(
                PrepQuestion.objects.filter(
                    topic_match, verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES
                )
                .filter(Q(paper__isnull=True) | Q(paper__is_published=True))
                .select_related("paper")
                .order_by("question_type", "paper__created_at", "number", "id")
            )
            rendered = learner_visible_assessment_questions(records)
            shown_total += len(rendered)
            shown = {norm(q.question_latex) for q in rendered}
            superseded = {q.reconstructed_from_id for q in records if q.reconstructed_from_id}
            unexplained = [
                q
                for q in records
                if q.id not in superseded
                and not assessment_question_rendering_issues(q.question_latex)
                and norm(q.question_latex) not in shown
            ]
            if unexplained:
                course_fail += 1
                print(f"  {course.code} / {topic.title[:40]}: {len(unexplained)} hidden")
                for q in unexplained[:2]:
                    same = [
                        r.id
                        for r in records
                        if r.paper_id == q.paper_id and r.number == q.number and r.id != q.id
                    ]
                    print(f"     q{q.id} n={q.number} same_paper_number_rows={same}")
        failures += course_fail
        print(f"{course.code:9} topics={len(topics):2d} rendered={shown_total:4d} failing_topics={course_fail}")
    print("FAILING TOPICS:", failures)


if __name__ == "__main__":
    main()
