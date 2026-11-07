"""Final sweep of SMA 335: rescue one stub, retire the rest of the dead rows.

* Row 1027 (Question One of the 2010/2011 paper) failed extraction and is empty, but
  it is the only row that would carry Question One (a). It is rebuilt from the
  document text and mapped, so nothing is lost.
* The other nine empty stubs carry no text at all - their content is already covered
  by the rows that follow them in the same paper - so they are retired.
* The twelve ``Adapted from Question N`` rows were never attached to a topic (their
  ``topic_label`` is a provenance note, not a topic title) and duplicate questions
  that are already visible, so they are retired.
* ``sma335-doc-f2677f37`` is a second extraction of the same 2010/2011 paper as
  ``sma335-doc-14688bc6``; it is unpublished so the paper is listed once.

Everything is backed up before deletion.
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

from prep.models import PrepPaper, PrepQuestion  # noqa: E402
from services.prep_ingestion import assessment_question_rendering_issues  # noqa: E402

COURSE_ID = 57

Q_1027 = r"""a) i) Differentiate between a primitive equation and a differential equation. **(3 marks)**

ii) Form the differential equation from the equation

$$
y = c_{1}\cos bx + c_{2}\sin bx,
$$

by eliminating the arbitrary constants $c_{1}$ and $c_{2}$, where $b$ is a parameter. **(5 marks)**"""

EMPTY_STUBS = [1032, 1035, 1038, 1041, 1084, 1089, 1092, 1095, 1098]
ADAPTED_DUPLICATES = [1335, 1336, 1337, 1338, 1339, 1340, 1341, 1348, 1349, 1350, 1351, 1352]
DUPLICATE_PAPER = "sma335-doc-f2677f37"


def main() -> None:
    apply = "--apply" in sys.argv

    issues = assessment_question_rendering_issues(Q_1027)
    if issues:
        raise SystemExit(f"1027 fails the validator: {issues}")

    stubs = list(PrepQuestion.objects.filter(pk__in=EMPTY_STUBS))
    for q in stubs:
        if (q.question_latex or "").strip():
            raise SystemExit(f"row {q.id} is not empty; refusing to delete")
    adapted = list(PrepQuestion.objects.filter(pk__in=ADAPTED_DUPLICATES))
    print(f"rescue 1027 | delete {len(stubs)} empty stubs | delete {len(adapted)} adapted duplicates")

    if not apply:
        print("DRY RUN - nothing written.")
        return

    out = Path(__file__).resolve().parent / "final_sweep_backup.json"
    out.write_text(
        json.dumps(
            {
                "rescued": {"id": 1027, "question_latex": PrepQuestion.objects.get(pk=1027).question_latex},
                "deleted": [
                    {
                        "id": q.id,
                        "paper_id": q.paper_id,
                        "verification_status": q.verification_status,
                        "topic_label": q.topic_label,
                        "question_latex": q.question_latex,
                        "solution_latex": q.solution_latex,
                    }
                    for q in stubs + adapted
                ],
            },
            indent=1,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print("backup written:", out)

    row = PrepQuestion.objects.get(pk=1027)
    metadata = dict(row.reconstruction_metadata or {})
    metadata["reason"] = "Extraction produced no text; question rebuilt from the document text of the same PDF."
    row.question_latex = Q_1027
    row.topic_id = 171
    row.topic_label = ""
    row.verification_status = "reconstructed"
    row.reconstruction_metadata = metadata
    row.save(update_fields=["question_latex", "topic", "topic_label", "verification_status", "reconstruction_metadata"])
    print("rescued 1027")

    deleted = PrepQuestion.objects.filter(pk__in=EMPTY_STUBS + ADAPTED_DUPLICATES).delete()
    print("deleted:", deleted)

    dup = PrepPaper.objects.filter(pk=DUPLICATE_PAPER).first()
    if dup and dup.is_published:
        dup.is_published = False
        dup.save(update_fields=["is_published"])
        print("unpublished duplicate paper", DUPLICATE_PAPER)


if __name__ == "__main__":
    main()
