import io, os, sys
sys.path.insert(0, ".")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
import django; django.setup()
from django.db.models import Q
from prep.models import PrepQuestion
from services.prep_ingestion import assessment_question_rendering_issues
rows = PrepQuestion.objects.filter(Q(topic__course_id=41)|Q(paper__course_id=41), verification_status="flagged").exclude(paper_id="sma200-doc-776f3d92").order_by("id")
print("flagged outside textbook paper:", rows.count())
for q in rows:
    t = " ".join((q.question_latex or "").split())
    print(f"\nq{q.id} p={str(q.paper_id)[-8:]} issues={assessment_question_rendering_issues(q.question_latex)}")
    print("  HEAD:", t[:90])
    print("  TAIL:", t[-160:])
