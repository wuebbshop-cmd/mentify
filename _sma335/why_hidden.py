"""Explain why a specific SMA 335 question does not reach a topic page."""
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

from prep.models import PrepQuestion, PrepTopic  # noqa: E402
from services.prep_ai_router import normalize_math_delimiters  # noqa: E402
from services.prep_ingestion import _normalise_document_text, learner_visible_assessment_questions  # noqa: E402

COURSE_ID = 57
TARGETS = {287: 1596, 288: 2500}


def norm(text: str) -> str:
    return _normalise_document_text(normalize_math_delimiters(text or ""))


def main() -> None:
    for topic_id, qid in TARGETS.items():
        topic = PrepTopic.objects.get(pk=topic_id)
        target = PrepQuestion.objects.get(pk=qid)
        print(f"\n== topic {topic_id} target q{qid} number={target.number} paper={target.paper_id} status={target.verification_status}")
        print(f"   {norm(target.question_latex)[:120]!r}")
        records = list(
            PrepQuestion.objects.filter(
                Q(topic=topic)
                | (Q(topic__isnull=True) & Q(paper__course_id=COURSE_ID) & Q(topic_label__icontains=topic.title)),
                verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
            )
            .filter(Q(paper__isnull=True) | Q(paper__is_published=True))
            .select_related("paper")
            .order_by("question_type", "paper__created_at", "number", "id")
        )
        shown = {q.id for q in learner_visible_assessment_questions(records)}
        superseded = {q.reconstructed_from_id for q in records if q.reconstructed_from_id}
        print(f"   in records: {qid in {q.id for q in records}}  shown: {qid in shown}  superseded: {qid in superseded}")
        same_number = [q for q in records if q.paper_id == target.paper_id and q.number == target.number]
        print(f"   same paper+number rows: {[(q.id, q.verification_status, 'copy' if (q.reconstruction_metadata or {}).get('cross_listed_from') else 'orig') for q in same_number]}")
        same_text = [q for q in records if norm(q.question_latex) == norm(target.question_latex)]
        print(f"   same text rows: {[(q.id, q.topic_id, q.paper_id[-6:], 'shown' if q.id in shown else 'dropped') for q in same_text]}")
        recon = [q for q in records if q.reconstructed_from_id == qid]
        print(f"   reconstructions of it: {[(q.id, q.verification_status) for q in recon]}")


if __name__ == "__main__":
    main()
