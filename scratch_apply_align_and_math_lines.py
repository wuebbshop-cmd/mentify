"""
Update database questions:
1. Replace \begin{align*} / \begin{align} with \begin{aligned} and \end{align*} / \end{align} with \end{aligned}
2. Wrap standalone equation lines (such as t_1 = \frac..., Q_1 = ..., \frac{x^2}{...} = 1, etc.) in $$...$$
"""
import os, sys, re
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
import django; django.setup()

from prep.models import PrepQuestion

def is_standalone_math_line(s):
    s = s.strip()
    if not s:
        return False
    if any(d in s for d in ['$', '$$', r'\(', r'\)', r'\[', r'\]', '```', '`']):
        return False
    if s.startswith(('#', '>', '|', '- ', '* ')):
        return False
    if re.match(r'^\d+\.\s+[A-Za-z]', s):
        return False
    if re.match(r'^\([a-z0-9]+\)\s+[A-Za-z]', s):
        return False
        
    has_math_cmd = bool(re.search(r'\\(?:frac|sum|int|sqrt|prod|alpha|beta|gamma|theta|mu|sigma|lambda|pi|partial|cdot|times|pm|le|ge|neq|equiv|approx|in|to|infty|lim|sin|cos|tan|log|ln|exp|quad|qquad)\b', s))
    has_math_eq = bool(re.search(r'[=<>≤≥]\s*\\', s) or re.search(r'\\\w+\s*[=<>≤≥]', s) or re.search(r'^[a-zA-Z](?:_\d+|\([a-zA-Z0-9,\s\\]+\))?\s*=', s))
    
    if not (has_math_cmd and (has_math_eq or s.startswith(r'\frac') or s.startswith(r'\sum') or s.startswith(r'\int'))):
        return False

    words = re.findall(r'\b[A-Za-z]{3,}\b', s)
    math_words = {'frac', 'sqrt', 'quad', 'qquad', 'text', 'and', 'sum', 'sin', 'cos', 'tan', 'exp', 'log', 'ln', 'lim', 'det', 'max', 'min', 'var', 'cov', 'where', 'for', 'giving', 'details', 'marks', 'mks'}
    real_english = [w.lower() for w in words if w.lower() not in math_words]
    
    return len(real_english) <= 3

qs = list(PrepQuestion.objects.exclude(question_latex='').only('id', 'topic_id', 'question_latex'))
print(f'Total questions: {len(qs)}')

updated_count = 0
align_fixed = 0
math_lines_wrapped = 0

for q in qs:
    latex = q.question_latex
    orig = latex
    changes = []
    
    # 1. Normalize align/align* to aligned
    if r'\begin{align' in latex:
        new_latex = re.sub(r'\\begin\{align\*?\}', r'\\begin{aligned}', latex)
        new_latex = re.sub(r'\\end\{align\*?\}', r'\\end{aligned}', new_latex)
        if new_latex != latex:
            changes.append('align_to_aligned')
            align_fixed += 1
            latex = new_latex

    # 2. Wrap standalone math lines in $$...$$
    lines = latex.split('\n')
    new_lines = []
    wrapped_in_q = 0
    for line in lines:
        if is_standalone_math_line(line):
            line = f'$${line.strip()}$$'
            wrapped_in_q += 1
        new_lines.append(line)
        
    if wrapped_in_q > 0:
        changes.append(f'wrapped_{wrapped_in_q}_math_lines')
        math_lines_wrapped += wrapped_in_q
        latex = '\n'.join(new_lines)

    if latex != orig:
        updated_count += 1
        q.question_latex = latex
        q.save(update_fields=['question_latex'])
        print(f'Updated Q{q.id} [Topic {q.topic_id}]: {changes}')

print(f'\nTotal questions updated: {updated_count}')
print(f'align->aligned conversions: {align_fixed}')
print(f'standalone math lines wrapped: {math_lines_wrapped}')
