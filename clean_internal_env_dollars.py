import os, sys
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
import django; django.setup()

from prep.models import PrepQuestion

def strip_dollars_in_env(text):
    for env in ['aligned', 'cases', 'matrix', 'pmatrix', 'bmatrix', 'vmatrix', 'gather', 'split', 'array']:
        start_tag = f'\\begin{{{env}}}'
        end_tag = f'\\end{{{env}}}'
        pos = 0
        while True:
            idx1 = text.find(start_tag, pos)
            if idx1 == -1:
                break
            idx2 = text.find(end_tag, idx1 + len(start_tag))
            if idx2 == -1:
                break
            body = text[idx1 + len(start_tag):idx2]
            body_clean = body.replace('$$', '').replace('$', '')
            text = text[:idx1 + len(start_tag)] + body_clean + text[idx2:]
            pos = idx1 + len(start_tag) + len(body_clean) + len(end_tag)
    return text

qs = list(PrepQuestion.objects.exclude(question_latex='').only('id', 'topic_id', 'question_latex'))
print(f'Total questions to check: {len(qs)}')

cleaned_count = 0

for q in qs:
    cleaned = strip_dollars_in_env(q.question_latex)
    if cleaned != q.question_latex:
        cleaned_count += 1
        q.question_latex = cleaned
        q.save(update_fields=['question_latex'])
        print(f'Cleaned env dollars in Q{q.id} [Topic {q.topic_id}]')

print(f'\nTotal questions cleaned of internal env dollars: {cleaned_count}')
