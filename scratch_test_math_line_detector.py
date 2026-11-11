import os, sys, re
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
import django; django.setup()

from prep.models import PrepQuestion

def is_standalone_math_line(s):
    s = s.strip()
    if not s:
        return False
    # Must not already contain math delimiters or code fences
    if any(d in s for d in ['$', '$$', r'\(', r'\)', r'\[', r'\]', '```', '`']):
        return False
    # Must not be markdown syntax
    if s.startswith(('#', '>', '|', '- ', '* ')):
        return False
    if re.match(r'^\d+\.\s+[A-Za-z]', s): # numbered list item with prose
        return False
    if re.match(r'^\([a-z0-9]+\)\s+[A-Za-z]', s): # e.g. (a) Let X be...
        return False
        
    # Must have LaTeX math commands or symbols
    has_math_cmd = bool(re.search(r'\\(?:frac|sum|int|sqrt|prod|alpha|beta|gamma|theta|mu|sigma|lambda|pi|partial|cdot|times|pm|le|ge|neq|equiv|approx|in|to|infty|lim|sin|cos|tan|log|ln|exp|quad|qquad)\b', s))
    has_math_eq = bool(re.search(r'[=<>≤≥]\s*\\', s) or re.search(r'\\\w+\s*[=<>≤≥]', s) or re.search(r'^[a-zA-Z](?:_\d+|\([a-zA-Z0-9,\s\\]+\))?\s*=', s))
    
    if not (has_math_cmd and (has_math_eq or s.startswith(r'\frac') or s.startswith(r'\sum') or s.startswith(r'\int'))):
        return False

    # English words check
    words = re.findall(r'\b[A-Za-z]{3,}\b', s)
    math_words = {'frac', 'sqrt', 'quad', 'qquad', 'text', 'and', 'sum', 'sin', 'cos', 'tan', 'exp', 'log', 'ln', 'lim', 'det', 'max', 'min', 'var', 'cov', 'where', 'for', 'giving', 'details', 'marks', 'mks'}
    real_english = [w.lower() for w in words if w.lower() not in math_words]
    
    return len(real_english) <= 3

qs = list(PrepQuestion.objects.exclude(question_latex='').values_list('id', 'topic_id', 'question_latex'))

matched = []
for qid, tid, latex in qs:
    for line in latex.split('\n'):
        if is_standalone_math_line(line):
            matched.append((qid, tid, line.strip()))

print(f'Total matched standalone math lines: {len(matched)}')
for qid, tid, line in matched[:30]:
    print(f'Q{qid} (Topic {tid}): {repr(line)}')
