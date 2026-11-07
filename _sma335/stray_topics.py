"""Report SMA 335 rows whose topic does not belong to the course."""
from __future__ import annotations

import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django  # noqa: E402

django.setup()

from django.db.models import Q  # noqa: E402

from prep.models import PrepQuestion, PrepTopic  # noqa: E402

COURSE_ID = 57


def main() -> None:
    stray = PrepQuestion.objects.filter(Q(paper__course_id=COURSE_ID) | Q(topic__course_id=COURSE_ID)).exclude(
        Q(topic__isnull=True) | Q(topic__course_id=COURSE_ID)
    )
    print("rows with a topic from another course:", stray.count())
    topic_ids = sorted(set(stray.values_list("topic_id", flat=True)))
    for topic in PrepTopic.objects.filter(id__in=topic_ids).select_related("course"):
        n = stray.filter(topic=topic).count()
        print(f"  topic {topic.id} ({topic.course_id}: {topic.course.code if hasattr(topic.course, 'code') else topic.course_id}) {n} rows  {topic.title[:60]}")
    for q in stray.order_by("id")[:30]:
        print(f"  q{q.id} paper={q.paper_id} topic={q.topic_id} num={q.number} label={q.topic_label!r} :: {(q.question_latex or '')[:70]!r}")


if __name__ == "__main__":
    main()
