import io
import os
import sys
from collections import Counter
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
from services.prep_ingestion import assessment_question_rendering_issues  # noqa: E402

COURSE_ID = 8


def main() -> None:
    rows = list(
        PrepQuestion.objects.filter(
            Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID)
        )
        .select_related("paper", "topic")
        .order_by("id")
    )
    bad = [q for q in rows if assessment_question_rendering_issues(q.question_latex)]
    pairs = [q for q in rows if q.reconstructed_from_id is not None]
    print(f"rows={len(rows)} bad={len(bad)} reconstructions={len(pairs)} unmapped={sum(q.topic_id is None for q in rows)}")
    print("statuses:", dict(Counter(q.verification_status for q in rows)))
    print("issue frequency:", dict(Counter(
        issue.split(":")[0]
        for q in bad
        for issue in assessment_question_rendering_issues(q.question_latex)
    )))
    print("reconstruction pairs:")
    by_source = {q.reconstructed_from_id: q for q in pairs if q.reconstructed_from_id}
    for source_id, replacement in sorted(by_source.items()):
        source = next((q for q in rows if q.id == source_id), None)
        if source:
            print(
                f"  {source_id} [{source.verification_status}] -> {replacement.id} "
                f"[{replacement.verification_status}]"
            )
    print("bad rows:")
    for q in bad:
        text = " ".join((q.question_latex or "").split())
        print(
            f"  q{q.id} [{q.verification_status}] topic={q.topic_id} "
            f"paper={str(q.paper_id)[-8:]} issues={assessment_question_rendering_issues(q.question_latex)}"
        )
        print(f"    {text[:220]}")


if __name__ == "__main__":
    main()
