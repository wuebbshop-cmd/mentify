import io, json, re, sys
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
d = json.loads(Path("_pastpaper/cache_41.json").read_text(encoding="utf-8"))
rows = [q for q in d["questions"] if q["paper"] == "sma200-doc-776f3d92"]
ASK = re.compile(r"\b(find|evaluate|calculate|determine|show that|prove|obtain|compute|use|estimate|interpret|verify|sketch|plot)\b", re.I)
BOOK = re.compile(r"you have learnt|summary|further reading|chapter|exercise\s*\d|solution|example|by j\.|wiley|heinemann|longman|pure mathematics|advanced calculus|additional pure", re.I)
good, bad = [], []
for q in rows:
    t = " ".join((q["text"] or "").split())
    if ASK.search(t) and 40 <= len(t) <= 700 and not BOOK.search(t):
        good.append(q)
    else:
        bad.append(q)
print(f"textbook rows={len(rows)} question-like={len(good)} junk={len(bad)}")
print("\n--- QUESTION-LIKE ---")
for q in good:
    print(f'q{q["id"]:5d} [{q["status"][:4]}] len={len(" ".join(q["text"].split())):4d} :: {" ".join(q["text"].split())[:140]}')
