"""Measure text similarity between SMA 335 questions to choose a safe dedupe rule."""
from __future__ import annotations

import io
import os
import re
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

from django.db.models import Q  # noqa: E402

from prep.models import PrepQuestion  # noqa: E402
from services.prep_ai_router import normalize_math_delimiters  # noqa: E402
from services.prep_ingestion import _normalise_document_text, assessment_question_rendering_issues  # noqa: E402

COURSE_ID = 57
_NOISE = re.compile(r"[\\${}^_\s]+")


def plain(text: str) -> str:
    """Compare on words and maths stripped of LaTeX decoration."""
    s = normalize_math_delimiters(text or "")
    s = s.replace("\\dfrac", "\\frac").replace("\\left", "").replace("\\right", "")
    s = _NOISE.sub(" ", s)
    return _normalise_document_text(s)


def main() -> None:
    rows = list(
        PrepQuestion.objects.filter(
            Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID),
            paper__is_published=True,
        )
        .order_by("paper_id", "number")
    )
    sources = [q for q in rows if not (q.reconstruction_metadata or {}).get("cross_listed_from")]
    by_paper: dict[str, list] = {}
    for q in sources:
        by_paper.setdefault(q.paper_id, []).append(q)

    buckets = {0.6: [], 0.7: [], 0.8: [], 0.9: []}
    for paper_id, qs in by_paper.items():
        for i, a in enumerate(qs):
            for b in qs[i + 1 :]:
                ta, tb = plain(a.question_latex), plain(b.question_latex)
                if not ta or not tb:
                    continue
                ratio = SequenceMatcher(None, ta, tb).ratio()
                for cut in buckets:
                    if ratio >= cut:
                        buckets[cut].append((ratio, paper_id, a, b))

    for cut in sorted(buckets):
        pairs = buckets[cut]
        print(f"\nratio >= {cut}: {len(pairs)} pairs")
        for ratio, paper_id, a, b in sorted(pairs, key=lambda p: -p[0])[:8]:
            print(f"  {ratio:.3f} q{a.id}(n{a.number}) / q{b.id}(n{b.number}) {paper_id[-6:]}")
            print(f"     A: {' '.join((a.question_latex or '').split())[:110]}")
            print(f"     B: {' '.join((b.question_latex or '').split())[:110]}")


if __name__ == "__main__":
    main()
