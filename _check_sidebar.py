import re, hashlib, glob, os

base = r"C:\Users\adm\.vscode\Products\EduAI\templates"
files = glob.glob(os.path.join(base, "**", "*.html"), recursive=True)
pat = re.compile(
    r'<div class="sidebar-profile">.*?</div>\s*\n\s*<ul class="sidebar-nav">',
    re.S,
)
blocks = {}
for f in files:
    txt = open(f, encoding="utf-8").read()
    m = pat.search(txt)
    if m:
        block = re.sub(r"\s+", " ", m.group(0)).strip()
        h = hashlib.md5(block.encode()).hexdigest()[:8]
        rel = os.path.relpath(f, base)
        blocks.setdefault(h, []).append(rel)

for h, flist in sorted(blocks.items(), key=lambda x: -len(x[1])):
    print(f"{h}: {len(flist)} files")
    for rel in flist:
        print(f"  {rel}")
