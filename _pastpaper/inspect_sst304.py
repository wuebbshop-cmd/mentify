"""Inspect SST 304 past-paper rows and reconstruction pairs."""

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
from prep.models import PrepQuestion, PrepTopic  # noqa: E402

COURSE_ID = 3635
rows = list(
    PrepQuestion.objects.filter(Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID))
    .distinct()
    .select_related("paper", "topic")
    .order_by("paper_id", "number", "id")
)

print("TOPICS")
for topic in PrepTopic.objects.filter(course_id=COURSE_ID).order_by("id"):
    print(f"{topic.id}|{topic.title}")

print("ROWS")
for q in rows:
    text = " ".join((q.question_latex or "").split())
    print(f"{q.id}|{q.verification_status}|topic={q.topic_id}|paper={q.paper_id}|number={q.number}|from={q.reconstructed_from_id}|{text[:260]}")

print("REPLACEMENT_PAIRS")
for replacement in [q for q in rows if q.reconstructed_from_id]:
    source = next((q for q in rows if q.id == replacement.reconstructed_from_id), None)
    print(f"\nREPLACEMENT {replacement.id}|SOURCE {replacement.reconstructed_from_id}|STATUS {replacement.verification_status}|TOPIC {replacement.topic_id}")
    print("SOURCE:", " ".join((source.question_latex or "").split())[:600] if source else "missing")
    print("CLEAN :", " ".join((replacement.question_latex or "").split())[:700])

print("\nUNMAPPED")
for q in [q for q in rows if q.topic_id is None]:
    print(f"{q.id}|{q.verification_status}|{q.paper_id}|{q.number}|{' '.join((q.question_latex or '').split())[:260]}")
