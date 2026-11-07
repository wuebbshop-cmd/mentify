import io, json, sys
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
d = json.loads(Path("_pastpaper/cache_41.json").read_text(encoding="utf-8"))
rows = [q for q in d["questions"] if q["paper"] == "sma200-doc-776f3d92"]
print("rows:", len(rows))
for q in sorted(rows, key=lambda r: r["id"]):
    t = " ".join((q["text"] or "").split())
    print(f'q{q["id"]:5d} [{q["status"][:4]}] len={len(t):4d} :: {t[:150]}')
