"""Find published SMA 335 rows where two different questions share a paper+number.

learner_visible_assessment_questions keeps only one row per (paper, number), so if a paper
has two distinct questions with the same number and cross-listing put them in the same
topic, one of them disappears from that topic page.
"""
from __future__ import annotations

import os
import sys
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django  # noqa: E402

django.setup()

from django.db.models import Q  # noqa: E402

from prep.models import PrepQuestion  # noqa: E402

COURSE_ID = 57


def norm(text: str) -> str:
    return " ".join((text or "").split())


def main() -> None:
    rows = PrepQuestion.objects.filter(
        Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID),
        paper__is_published=True,
    ).select_related("paper")
    groups: dict[tuple, list] = defaultdict(list)
    for q in rows:
        groups[(q.paper_id, q.number)].append(q)

    clashes = {k: v for k, v in groups.items() if len({norm(q.question_latex) for q in v}) > 1}
    print("paper+number groups with more than one distinct question:", len(clashes))
    hidden = 0
    for (paper, number), qs in sorted(clashes.items()):
        by_topic = defaultdict(set)
        for q in qs:
            by_topic[q.topic_id].add(norm(q.question_latex))
        for topic, texts in by_topic.items():
            if len(texts) > 1:
                hidden += len(texts) - 1
                print(f"  paper={paper} num={number} topic={topic}: {len(texts)} distinct questions -> {len(texts) - 1} hidden")
                for q in qs:
                    if q.topic_id == topic:
                        print(f"    q{q.id} :: {norm(q.question_latex)[:90]!r}")
    print("questions hidden by the paper+number dedupe:", hidden)


if __name__ == "__main__":
    main()
