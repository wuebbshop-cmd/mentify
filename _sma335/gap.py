"""Explain the gap between SMA 335 row count and per-topic visible counts."""
from __future__ import annotations

import os
import sys
from collections import Counter
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


def main() -> None:
    allq = PrepQuestion.objects.filter(Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID))
    print("total:", allq.count())
    print("no paper:", allq.filter(paper__isnull=True).count())
    print(
        "unpublished paper:",
        allq.filter(paper__is_published=False).count(),
    )
    print("by paper published flag:", dict(Counter(allq.values_list("paper__is_published", flat=True))))
    print("visible statuses:", PrepQuestion.LEARNER_VISIBLE_STATUSES)
    print(
        "visible-status rows:",
        allq.filter(verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES).count(),
    )
    for row in allq.filter(paper__is_published=False).select_related("paper").order_by("paper_id", "number")[:30]:
        print(f"  q{row.id} paper={row.paper_id} pub={row.paper.is_published} topic={row.topic_id} num={row.number}")


if __name__ == "__main__":
    main()
