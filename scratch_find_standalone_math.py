import os, sys, re
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
import django; django.setup()

from prep.models import PrepQuestion

qs = list(PrepQuestion.objects.exclude(question_latex='').values_list('id', 'topic_id', 'question_latex'))

standalone_math_lines = []

for qid, tid, latex in qs:
    # Check lines
    for line in latex.split('\n'):
        s = line.strip()
        if not s:
            continue
        # Does it have $ or $$ or \( or \) or \[ or \] ?
        if any(delm in s for delm in ['$', '$$', r'\(', r'\)', r'\[', r'\]', '```']):
            continue
        # Does it contain math commands?
        if any(cmd in s for cmd in [r'\frac{', r'\sum_', r'\int_', r'\sqrt{', r'\cdot', r'\times', r'\pm', r'\quad']):
            # Filter out lines that are full English sentences (e.g. starting with "Show that", "Find", "Evaluate", etc.)
            # unless the line is overwhelmingly math
            words = re.findall(r'[a-zA-Z]{3,}', s)
            # Math keywords that can appear in math formulas
            math_words = {'frac', 'sqrt', 'quad', 'qquad', 'text', 'and', 'sum', 'sin', 'cos', 'tan', 'exp', 'log', 'ln', 'lim', 'det', 'max', 'min', 'var', 'cov'}
            english_words = [w.lower() for w in words if w.lower() not in math_words]
            if len(english_words) <= 3:
                standalone_math_lines.append((qid, tid, s))

print(f'Total standalone un-delimited math lines: {len(standalone_math_lines)}')
for qid, tid, s in standalone_math_lines[:35]:
    print(f'Q{qid} (Topic {tid}): {repr(s)}')
