"""List every question the 60-char prefix rule hides, with the row that shadows it."""
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

from prep.models import PrepQuestion  # noqa: E402
from services.prep_ai_router import normalize_math_delimiters  # noqa: E402
from services.prep_ingestion import _normalise_document_text, assessment_question_rendering_issues  # noqa: E402


def norm(text: str) -> str:
    return _normalise_document_text(normalize_math_delimiters(text or ""))


def main() -> None:
    rows = list(
        PrepQuestion.objects.filter(
            verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
            paper__is_published=True,
        )
        .select_related("paper__course")
        .order_by("paper_id", "number", "id")
    )
    status_rank = {"verified": 3, "reconstructed": 2, "auto_validated": 1}

    by_paper: dict[str, list] = {}
    for q in rows:
        if assessment_question_rendering_issues(q.question_latex):
            continue
        by_paper.setdefault(q.paper_id, []).append(q)

    total = 0
    near = []
    for paper_id, qs in by_paper.items():
        best = {}
        for q in qs:
            score = (status_rank.get(q.verification_status, 0), 1 if q.source_document_id else 0, q.pk)
            if q.number not in best or score > best[q.number][0]:
                best[q.number] = (score, q)
        survivors = sorted((v[1] for v in best.values()), key=lambda q: q.pk)
        seen_texts, seen_prefixes = {}, {}
        for q in survivors:
            text = norm(q.question_latex)
            if text and len(text) > 25:
                prefix = text[:60]
                if text in seen_texts:
                    continue
                owner = seen_prefixes.get(prefix) if len(prefix) >= 50 else None
                if owner is not None:
                    ratio = SequenceMatcher(None, text, norm(owner.question_latex)).ratio()
                    if ratio >= 0.99:
                        near.append((ratio, q, owner))
                    continue
                seen_texts[text] = q
                if len(prefix) >= 50:
                    seen_prefixes[prefix] = q
    print("\npairs suppressed by the prefix rule that are near-identical (ratio >= 0.99):", len(near))
    for ratio, q, owner in sorted(near, key=lambda p: -p[0])[:25]:
        print(f"  {ratio:.4f} q{q.id} / q{owner.id} :: {' '.join(q.question_latex.split())[:90]}")
        print(f"           other   :: {' '.join(owner.question_latex.split())[:90]}")
    print("\nnon-identical questions hidden by the prefix rule:", total)



if __name__ == "__main__":
    main()
