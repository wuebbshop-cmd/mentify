import django, os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.development'
sys.path.insert(0, '.')
django.setup()

from prep.models import PrepTopic, PrepQuestion
from services.prep_export_service import _build_topic_notes_html, _render_html_with_playwright
from services.prep_ai_router import validated_question_solution
from django.db.models import Q
import fitz

topic = PrepTopic.objects.get(id=100)
course_code = topic.course.code
topic_title = topic.title

# Fetch notes from cache
from prep.models import PrepContentCache
cache_entry = PrepContentCache.objects.filter(topic=topic, content_type='topic_notes').order_by('-updated_at').first()
notes_content = cache_entry.payload.get('content', '') if cache_entry else 'Topic notes placeholder'

# Fetch authentic questions
q_filter = (
    Q(topic=topic)
    | (
        Q(topic__isnull=True)
        & Q(paper__course=topic.course)
        & Q(topic_label__icontains=topic_title)
    )
) & Q(
    question_type__in=["authentic", "adapted"],
    verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
)
authentic_qs = []
from services.prep_ingestion import learner_visible_assessment_questions

topic_questions = learner_visible_assessment_questions(
    PrepQuestion.objects.filter(q_filter, verification_status="verified")
    .select_related("paper")
    .order_by("paper", "number", "id")
)
for q in topic_questions:
    authentic_qs.append({
        "number": q.number,
        "marks": q.marks,
        "paper_title": q.paper.title if q.paper else f"{course_code} Examination",
        "year": q.paper.year if q.paper else "Official Examination",
        "question_latex": q.question_latex,
        "solution_latex": validated_question_solution(q),
    })

print(f'Building HTML with {len(authentic_qs)} authentic questions...')
html = _build_topic_notes_html(
    course_code=course_code,
    topic_title=topic_title,
    notes_content=notes_content,
    authentic_questions=authentic_qs,
    level='level_2'
)

with open('topic100_test.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('HTML written: ', len(html), 'chars')

print('Rendering PDF with Playwright...')
pdf_bytes = _render_html_with_playwright(html)
print('PDF rendered:', len(pdf_bytes), 'bytes')

with open('topic100_fixed.pdf', 'wb') as f:
    f.write(pdf_bytes)

doc = fitz.open('topic100_fixed.pdf')
print('Total pages in fixed PDF:', len(doc))

# Search for the coffee bean question
for page_num in range(len(doc)):
    text = doc[page_num].get_text()
    if 'Coffee Beans' in text or 'Substitute' in text and 'supply function' in text:
        print(f'Found Coffee Beans on page {page_num + 1}!')
        pix = doc[page_num].get_pixmap(dpi=150)
        pix.save(f'page_coffee_beans_{page_num+1}.png')
        print(f'Saved page_coffee_beans_{page_num+1}.png')
        print('Page text excerpt:')
        print(text[:800])
        break
