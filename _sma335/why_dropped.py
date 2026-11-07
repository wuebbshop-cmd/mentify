"""Explain each text the paper page drops: duplicate, prefix rule, or reconstruction suppression."""
from __future__ import annotations

import io
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import django  # noqa: E402

django.setup()

from prep.models import PrepQuestion  # noqa: E402
from services.prep_ai_router import normalize_math_delimiters  # noqa: E402
from services.prep_ingestion import (  # noqa: E402
    _normalise_document_text,
    assessment_question_rendering_issues,
    learner_visible_assessment_questions,
)

COURSE_ID = 57


def norm(text: str) -> str:
    return _normalise_document_text(normalize_math_delimiters(text or ""))


def main() -> None:
    rows = list(
        PrepQuestion.objects.filter(
            topic__course_id=COURSE_ID,
            paper__is_published=True,
        ).order_by("paper_id", "number", "id")
    )
    links = [(q.id, q.reconstructed_from_id) for q in rows if q.reconstructed_from_id]
    print("rows with reconstructed_from:", len(links), links[:10])

    papers = sorted({q.paper_id for q in rows})
    for paper_id in papers:
        qs = [q for q in rows if q.paper_id == paper_id]
        visible = [q for q in qs if q.verification_status in PrepQuestion.LEARNER_VISIBLE_STATUSES]
        rendered = learner_visible_assessment_questions(visible)
        shown = {norm(q.question_latex) for q in rendered}
        dropped = [q for q in visible if not assessment_question_rendering_issues(q.question_latex) and norm(q.question_latex) not in shown]
        if not dropped:
            continue
        print(f"\n{paper_id}: {len(dropped)} dropped")
        for q in dropped:
            source_of = [r.id for r in rows if r.reconstructed_from_id == q.id]
            same_text = [r.id for r in rows if r.paper_id == paper_id and norm(r.question_latex) == norm(q.question_latex)]
            print(
                f"  q{q.id} n={q.number} status={q.verification_status} "
                f"replaces={source_of} same_text_in_paper={same_text}"
            )
            print(f"     {' '.join(q.question_latex.split())[:100]}")


if __name__ == "__main__":
    main()
