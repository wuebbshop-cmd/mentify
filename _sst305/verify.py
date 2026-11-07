"""Full verification of SST 305 after the repair campaign."""
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
from repair import is_acceptable, repair_text  # noqa: E402
from services.prep_ingestion import (  # noqa: E402
    assessment_question_rendering_issues,
    learner_visible_assessment_questions,
)

COURSE_ID = 27
FURNITURE = re.compile(
    r"INVOLVEMENT|IRREGULARITY|MALPRACTICE|CamScanner|Page \d+ of|"
    r"higher education institution|University Logo|VISIT US FOR|documentclass|usepackage",
    re.IGNORECASE,
)


def main() -> None:
    allq = PrepQuestion.objects.filter(Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID)).distinct()
    visible_statuses = PrepQuestion.LEARNER_VISIBLE_STATUSES
    visible = [
        q
        for q in allq
        if q.verification_status in visible_statuses
        and (q.paper_id is None or (q.paper and q.paper.is_published))
        and q.topic_id
    ]
    print(f"course total: {allq.count()}")
    print("statuses:", dict(Counter(allq.values_list("verification_status", flat=True))))
    print(f"VISIBLE (mapped + published): {len(visible)}")
    print("flagged:", [q.id for q in allq if q.verification_status == "flagged"])
    print("pending:", [q.id for q in allq if q.verification_status == "pending"])
    print("unmapped:", [q.id for q in allq if q.topic_id is None])
    print("blank questions:", [q.id for q in allq if not (q.question_latex or "").strip()])
    print("render issues:", [q.id for q in allq if assessment_question_rendering_issues(q.question_latex or "")])
    print("needs repair:", [q.id for q in allq if repair_text(q.question_latex or "")[0] != (q.question_latex or "")])
    print("furniture residue:", [q.id for q in allq if FURNITURE.search(q.question_latex or "")])
    print("odd dollars:", [q.id for q in allq if (q.question_latex or "").count("$") % 2])
    print("blank solutions:", sum(1 for q in allq if not (q.solution_latex or "").strip()))

    papers = PrepPaper.objects.filter(course_id=COURSE_ID)
    print("papers:", papers.count(), "published:", papers.filter(is_published=True).count())

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


if __name__ == "__main__":
    main()
