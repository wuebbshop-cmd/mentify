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

qs = list(PrepQuestion.objects.exclude(question_latex='').only('id', 'topic_id', 'question_latex'))
print(f'Checking {len(qs)} questions...')

updated = 0
for q in qs:
    new_latex = fix_split_cases(q.question_latex)
    if new_latex != q.question_latex:
        updated += 1
        q.question_latex = new_latex
        q.save(update_fields=['question_latex'])
        print(f'Updated split cases in Q{q.id} [Topic {q.topic_id}]')

print(f'\nTotal questions fixed: {updated}')
