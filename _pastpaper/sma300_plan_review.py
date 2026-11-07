import io
import json
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

from prep.models import PrepQuestion  # noqa: E402

plan = {
    row["id"]: row["targets"]
    for row in json.loads((BASE_DIR / "_pastpaper" / "topic_plan_8.json").read_text(encoding="utf-8"))
}
rows = PrepQuestion.objects.filter(pk__in=plan).order_by("id")
out = BASE_DIR / "_pastpaper" / "sma300_plan_review.txt"
with out.open("w", encoding="utf-8") as handle:
    for q in rows:
        text = " ".join((q.question_latex or "").split())
        handle.write(
            f"{q.id}\tcurrent={q.topic_id}\ttargets={','.join(map(str, plan[q.id]))}\t{text[:260]}\n"
        )
print(out, len(rows))
