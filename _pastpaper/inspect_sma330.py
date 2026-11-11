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

from django.db.models import Q  # noqa: E402
from prep.models import PrepQuestion  # noqa: E402

rows = (
    PrepQuestion.objects.filter(Q(topic__course_id=48) | Q(paper__course_id=48))
    .distinct()
    .select_related("paper", "topic")
    .order_by("verification_status", "id")
)

print("qid|status|topic_id|topic|paper|number|statement")
for q in rows:
    if q.verification_status not in {"flagged", "pending"} and q.topic_id is not None:
        continue
    text = " ".join((q.question_latex or "").split())
    topic = q.topic.title if q.topic_id else "None"
    print(f"{q.id}|{q.verification_status}|{q.topic_id}|{topic}|{q.paper_id}|{q.number}|{text[:260]}")

print("LINKS")
for q in rows.filter(reconstructed_from_id__isnull=False).order_by("id"):
    print(f"{q.id}|from={q.reconstructed_from_id}|status={q.verification_status}|topic={q.topic_id}|solution_chars={len(q.solution_latex or '')}")

from prep.models import PrepTopic  # noqa: E402

print("TOPICS")
for topic in PrepTopic.objects.filter(course_id=48).order_by("id"):
    print(f"{topic.id}|{topic.title}")

print("REPLACEMENT_PAIRS")
for replacement in rows.filter(reconstructed_from_id__isnull=False).select_related("topic").order_by("id"):
    source_id = replacement.reconstructed_from_id
    source = rows.filter(id=source_id).first()
    print(f"\nREPLACEMENT {replacement.id}|SOURCE {source_id}|STATUS {replacement.verification_status}|TOPIC {replacement.topic_id}|{replacement.topic.title if replacement.topic_id else 'None'}")
    print("SOURCE:", " ".join((source.question_latex or "").split())[:700] if source else "missing")
    print("CLEAN :", " ".join((replacement.question_latex or "").split())[:700])

print("\nUNMAPPED")
for q in rows.filter(topic__isnull=True).order_by("paper_id", "number", "id"):
    print(f"{q.id}|{q.verification_status}|{q.paper_id}|{q.number}|{' '.join((q.question_latex or '').split())[:260]}")
