"""Show which rendered row shadows each dropped SMA 335 question, and how alike they are."""
from __future__ import annotations

import io
import os
import sys
from difflib import SequenceMatcher
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import django  # noqa: E402

django.setup()

from prep.models import PrepPaper, PrepQuestion  # noqa: E402
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
    for paper in PrepPaper.objects.filter(course_id=COURSE_ID, is_published=True).order_by("id"):
        records = list(
            paper.questions.filter(verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES).order_by("number", "id")
        )
        rendered = learner_visible_assessment_questions(records)
        shown_ids = {q.id for q in rendered}
        by_prefix = {}
        for q in rendered:
            by_prefix.setdefault(norm(q.question_latex)[:60], q)
        for q in records:
            if q.id in shown_ids or assessment_question_rendering_issues(q.question_latex):
                continue
            text = norm(q.question_latex)
            owner = by_prefix.get(text[:60]) or next((r for r in rendered if norm(r.question_latex) == text), None)
            if owner is None:
                continue
            ratio = SequenceMatcher(None, text, norm(owner.question_latex)).ratio()
            if ratio >= 0.99:
                continue
            print(f"\nq{q.id} (n{q.number}) shadowed by q{owner.id} (n{owner.number}) ratio={ratio:.3f} paper={paper.id[-6:]}")
            print(f"  dropped : {' '.join(q.question_latex.split())[:150]}")
            print(f"  rendered: {' '.join(owner.question_latex.split())[:150]}")


if __name__ == "__main__":
    main()
