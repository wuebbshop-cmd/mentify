import io, os, sys
sys.path.insert(0, ".")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
import django; django.setup()
from django.db.models import Q
from prep.models import PrepQuestion
from services.prep_ingestion import assessment_question_rendering_issues
rows = PrepQuestion.objects.filter(Q(topic__course_id=41)|Q(paper__course_id=41)).exclude(paper_id="sma200-doc-776f3d92").select_related("paper").order_by("paper_id","id")
print("rows:", rows.count())
for q in rows:
    issues = assessment_question_rendering_issues(q.question_latex)
    t = " ".join((q.question_latex or "").split())
    print(f'q{q.id:5d} p={str(q.paper_id)[-8:]} [{q.verification_status[:6]}] ref={q.reconstructed_from_id} sol={len((q.solution_latex or "").strip()):4d} iss={len(issues)} :: {t[:110]}')
