import json
from playwright.sync_api import sync_playwright

test_md = """
> **✓ Step-by-Step Verified Solution & Marking Rubric:**
>
> 1. **Substitute $p_c = 0.8$ into the supply function:**
>
> $$
> Q_s = 3.15 + 0.1p - 0.5(0.8) = 3.15 + 0.1p - 0.40 = 2.75 + 0.1p.
> $$
"""

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    page = browser.new_page()
    page.goto('file:///' + r'c:/Users/adm/.vscode/Products/EduAI/temp_test.html'.replace('\\', '/'))
    html = page.evaluate('(md) => renderMarkdownWithKaTeX(md, document.getElementById("content"))', test_md)
    with open("test_output.html", "w", encoding="utf-8") as out:
        out.write(html)
    print("SAVED TO test_output.html, length:", len(html))
    browser.close()
