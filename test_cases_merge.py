import os, sys, re
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
import django; django.setup()

from prep.models import PrepQuestion

def fix_split_cases(text):
    # Pattern 1: $$\n$$f(x, ...) =$$\n\begin{cases}
    text = re.sub(
        r'\$\$\s*\n*\$\$([^\n$]+?=\s*)\$\$\s*\n*(\\begin\{cases\})',
        r'$$\n\1\n\2',
        text
    )
    # Pattern 2: $$f(x...) =$$\n\begin{cases}
    text = re.sub(
        r'\$\$([^\n$]+?=\s*)\$\$\s*\n*(\\begin\{cases\})',
        r'$$\n\1\n\2',
        text
    )
    # Pattern 3: f(x...) = \n\n$$\n\begin{cases} or f(x...) = $$\n\begin{cases}
    text = re.sub(
        r'(?<!\$)([a-zA-Z\\][a-zA-Z0-9_\\,\s\(\)]+?=\s*)\n*\$\$\s*\n*(\\begin\{cases\})',
        r'$$\n\1\n\2',
        text
    )
    # Pattern 4: any standalone $$ followed immediately by $$
    text = re.sub(r'\$\$\s*\n+\$\$', '$$', text)
    return text

q183 = PrepQuestion.objects.get(id=183)
fixed = fix_split_cases(q183.question_latex)
idx = fixed.find('(c)')
print(fixed[idx:idx+250])
