import os
import sys
import django
import re

BASE_DIR = r"C:\Users\adm\.vscode\Products\EduAI"
sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
django.setup()

from prep.models import PrepContentCache
from benchmark_validate import (
    extract_text,
    check_no_backslash_brackets,
    check_no_raw_html,
    check_display_math_on_own_line,
    check_no_naked_environments,
    check_balanced_display_math,
    check_balanced_inline_math_per_paragraph,
    check_table_column_consistency,
    check_no_replacement_chars,
)
from services.prep_ai_router import normalize_math_delimiters

benchmarks = [
    ("Topic 8", "notes:sst_301_matrices_in_r_level_2"),
    ("Topic 9", "notes:sst_301_differentiation_&_integration_of_univariate_functions_level_2"),
    ("Topic 19", "notes:sma_300_the_real_number_system_level_2"),
]

for label, key in benchmarks:
    entry = PrepContentCache.objects.filter(cache_key=key).first()
    if not entry:
        print(f"{label}: NOT FOUND")
        continue
    raw = extract_text(entry)
    norm = normalize_math_delimiters(raw)
    
    checks = [
        ("No \\[ or \\(", check_no_backslash_brackets(norm)),
        ("No raw HTML", check_no_raw_html(norm)),
        ("$$ own line", check_display_math_on_own_line(norm)),
        ("No naked env", check_no_naked_environments(norm)),
        ("$$ balanced", check_balanced_display_math(norm)),
        ("$ balanced", check_balanced_inline_math_per_paragraph(norm)),
        ("Table cols", check_table_column_consistency(norm)),
        ("No replacement", check_no_replacement_chars(norm)),
    ]
    
    print(f"=== {label} ({key}) ===")
    failed = False
    for name, issues in checks:
        if issues:
            failed = True
            print(f"  [FAIL] {name}: {issues[:2]}")
        else:
            print(f"  [PASS] {name}")
    print(f"Result: {'FAILED' if failed else 'ALL PASSED'}\n")
