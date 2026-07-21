import re
import pathlib

base = pathlib.Path(r"C:\Users\adm\.vscode\Products\EduAI\templates")
pat = re.compile(r"(<aside class=\"sidebar\".*?</aside>)", re.S)

for rel in [
    "accounts/tutor_dashboard.html",
    "courses/tutor_cohorts.html",
    "payments/payment_list.html",
    "accounts/learner_dashboard.html",
    "content/lesson_list.html",
]:
    t = (base / rel).read_text(encoding="utf-8")
    m = pat.search(t)
    aside = m.group(1) if m else "NO ASIDE"
    profile = re.search(r"<div class=\"sidebar-profile\">.*?</div>\s*\n\s*<ul", aside, re.S)
    block = profile.group(0) if profile else "NO PROFILE"
    print("===", rel)
    print(block)
    print()
