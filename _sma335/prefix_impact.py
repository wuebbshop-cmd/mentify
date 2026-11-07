"""Quantify what the 60-char prefix dedupe in learner_visible_assessment_questions hides."""
from __future__ import annotations

import io
import os
import sys
from collections import Counter, defaultdict
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
from services.prep_ingestion import _normalise_document_text, assessment_question_rendering_issues  # noqa: E402


def main() -> None:
    rows = list(
        PrepQuestion.objects.filter(
            verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
            paper__is_published=True,
        )
        .select_related("paper__course")
        .order_by("paper__course_id", "paper_id", "number", "id")
    )

    status_rank = {"verified": 3, "reconstructed": 2, "auto_validated": 1}
    per_paper = defaultdict(list)
    for q in rows:
        if assessment_question_rendering_issues(q.question_latex):
            continue
        per_paper[(q.paper.course.code if q.paper and q.paper.course else "?", q.paper_id)].append(q)

    hidden = Counter()
    samples = defaultdict(list)
    for (course, _paper), qs in per_paper.items():
        best = {}
        for q in qs:
            score = (status_rank.get(q.verification_status, 0), 1 if q.source_document_id else 0, q.pk)
            if q.number not in best or score > best[q.number][0]:
                best[q.number] = (score, q)
        survivors = sorted((v[1] for v in best.values()), key=lambda q: q.pk)
        seen_texts, seen_prefixes = set(), set()
        for q in survivors:
            norm = _normalise_document_text(normalize_math_delimiters(q.question_latex or ""))
            if norm and len(norm) > 25:
                prefix = norm[:60]
                if norm in seen_texts or (len(prefix) >= 50 and prefix in seen_prefixes):
                    hidden[course] += 1
                    if len(samples[course]) < 3:
                        samples[course].append((q.id, " ".join(q.question_latex.split())[:110]))
                    continue
                seen_texts.add(norm)
                if len(prefix) >= 50:
                    seen_prefixes.add(prefix)

    total = 0
    for course, count in sorted(hidden.items(), key=lambda kv: -kv[1]):
        total += count
        print(f"{course}: {count} questions hidden by the prefix rule")
        for qid, text in samples[course]:
            print(f"    q{qid}: {text}")
    print("TOTAL hidden by prefix rule:", total)


if __name__ == "__main__":
    main()
