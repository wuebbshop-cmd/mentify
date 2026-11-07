"""Finish SST 305: fix row 218's trapped table and publish the 9 valid pending rows.

* Row 218 passes the validator but its data table is wrapped in display dollars, so
  it would render as a line of pipes and backslashes. The table is unwrapped and the
  leftover ``Page 1 of`` footer removed.
* The 9 pending rows are complete, valid, already attached to the right topic and
  each carries a worked solution. Their ``reconstructed_from`` link is unreliable
  (six of them are not the question they point at), so they are published as their
  own reconstruction rather than deleted - deleting would throw away the solution.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django  # noqa: E402

django.setup()

from prep.models import PrepQuestion  # noqa: E402
from services.prep_ingestion import assessment_question_rendering_issues  # noqa: E402

COURSE_ID = 27

Q_218_TAIL = r"""e) Use matrix notation to fit a straight line to the 5 sample units given below by the method of least squares. **(6 marks)**

$$
\begin{array}{c|ccccc}
x & -2 & -1 & 0 & 1 & 2 \\ \hline
y & 0 & 0 & 1 & 1 & 3
\end{array}
$$"""

PENDING = [1168, 1169, 1170, 1171, 1173, 1174, 1175, 1182, 1184]

PENDING_REASON = (
    "Repair of AI-reconstructed question: the extraction it was adapted from was "
    "flagged, so it was never published. It is complete, valid and topically mapped, "
    "and carries a worked solution."
)


def main() -> None:
    apply = "--apply" in sys.argv

    row = PrepQuestion.objects.get(pk=218)
    text = row.question_latex or ""
    head, _, _tail = text.partition("e) Use matrix notation")
    new_218 = head.rstrip() + "\n\n" + Q_218_TAIL
    issues = assessment_question_rendering_issues(new_218)
    if issues:
        raise SystemExit(f"218 fails the validator: {issues}")

    pending = list(PrepQuestion.objects.filter(pk__in=PENDING))
    for q in pending:
        if q.verification_status != "pending":
            raise SystemExit(f"{q.id} is no longer pending ({q.verification_status})")
        problems = assessment_question_rendering_issues(q.question_latex or "")
        if problems:
            raise SystemExit(f"{q.id} fails the validator: {problems}")
        if q.topic_id is None:
            raise SystemExit(f"{q.id} has no topic")

    print(f"rebuild 218 ({len(text)} -> {len(new_218)} chars)")
    print(f"publish pending: {sorted(PENDING)}")
    if not apply:
        print("DRY RUN - nothing written.")
        return

    out = Path(__file__).resolve().parent / "finish_backup.json"
    out.write_text(
        json.dumps(
            {
                "218": {"question_latex": text},
                "pending": {
                    str(q.id): {"question_latex": q.question_latex, "verification_status": q.verification_status}
                    for q in pending
                },
            },
            indent=1,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print("backup written:", out)

    row.question_latex = new_218
    row.save(update_fields=["question_latex"])
    print("rebuilt 218")

    for q in pending:
        metadata = dict(q.reconstruction_metadata or {})
        metadata["reason"] = PENDING_REASON
        q.verification_status = "reconstructed"
        q.reconstruction_metadata = metadata
        q.save(update_fields=["verification_status", "reconstruction_metadata"])
    print(f"published {len(pending)} pending rows")


if __name__ == "__main__":
    main()
