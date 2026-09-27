import os
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.db.models import Count, Q
from .models import (
    PrepCourse,
    PrepTopic,
    PrepDocument,
    PrepPaper,
    PrepQuestion,
    PrepWallet,
    PrepCourseEnrollment,
    PrepTransaction,
    PrepHistory,
    PrepNotification,
)
from services.credit_service import (
    InsufficientCredits,
    PlanLimitExceeded,
    consume_credits,
    credits_for_usage,
    enforce_subscription_limit,
    estimated_generation_credits,
    get_available_credits,
    grant_purchased_topup,
    grant_subscription,
    has_active_subscription,
)


def parse_course_code_and_title(raw_name: str) -> tuple[str, str]:
    """Robustly parse course input into standard (code, title) avoiding duplication."""
    raw_name = raw_name.strip()
    match = re.match(r"^([A-Za-z]{2,5}\s*\d{3,4}[A-Za-z]?)(?:[\s:\-\–—]+(.*))?$", raw_name)
    if match:
        code_part = match.group(1).strip().upper()
        code_clean = re.sub(r"^([A-Z]+)\s*(\d+.*)$", r"\1 \2", code_part)
        title_part = match.group(2).strip() if match.group(2) else ""
        if not title_part:
            title_part = code_clean
        # Remove repeated code inside title if present
        title_part = re.sub(r"^" + re.escape(code_part) + r"[\s:\-\–—]*", "", title_part, flags=re.IGNORECASE).strip()
        if not title_part:
            title_part = code_clean
        return code_clean, title_part

    if ":" in raw_name:
        parts = raw_name.split(":", 1)
        return parts[0].strip().upper(), parts[1].strip()
    elif "-" in raw_name:
        parts = raw_name.split("-", 1)
        return parts[0].strip().upper(), parts[1].strip()

    return raw_name.upper(), raw_name


def clean_tag_label(label: str) -> str:
    """Robustly clean topic/subtopic tag labels so no equations, mathematical notations, or symbols belong to tags."""
    if not label or not isinstance(label, str):
        return ""
    text = label
    # Common ordinals like $n^{\text{th}}$, $n^{\\text{th}}$, n^{th}, n^th -> nth
    text = re.sub(r"\$?([a-zA-Z0-9]+)\^\{?\\*(?:text\{)?([a-zA-Z]+)\}?\}?\$?", r"\1\2", text)
    # Strip any remaining \text{...} -> ...
    text = re.sub(r"\\*text\{([^}]+)\}", r"\1", text)
    # Strip LaTeX command sequences like \alpha, \frac, etc.
    text = re.sub(r"\\[a-zA-Z]+", "", text)
    # Remove math mode and formatting characters: $, {, }, ^, _, `, \
    for ch in ("$", "{", "}", "^", "_", "`", "\\"):
        text = text.replace(ch, "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


@login_required
def prep_dashboard(request):
    """Mentify Prep Hub Main Landing Page with real database metrics."""
    wallet = PrepWallet.get_or_create_wallet(request.user)

    courses_qs = PrepCourse.objects.filter(is_active=True).annotate(
        topics_count=Count("topics", distinct=True),
        papers_count=Count("papers", distinct=True),
    )

    enrolled_courses = PrepCourse.objects.filter(
        enrollments__user=request.user,
    ).annotate(
        topics_count=Count("topics", distinct=True),
        papers_count=Count("papers", distinct=True),
    ).order_by("-enrollments__created_at")

    recent_courses = []
    for c in enrolled_courses[:3]:
        clean_title = c.title
        if c.code and c.code in clean_title:
            clean_title = re.sub(r"^" + re.escape(c.code) + r"[\s:\-\–—]*", "", clean_title, flags=re.IGNORECASE).strip()
            if not clean_title:
                clean_title = c.title
        recent_courses.append({
            "code": c.code,
            "slug": c.slug or c.code.replace(" ", "-"),
            "title": clean_title,
            "level": c.level,
            "topics_count": c.topics_count,
            "papers_count": c.papers_count,
        })

    # Recent activity from database
    history_qs = PrepHistory.objects.filter(user=request.user).order_by("-created_at")[:5]
    recent_activity = []
    for h in history_qs:
        recent_activity.append({
            "title": h.title,
            "course": h.course_code,
            "time": h.created_at.strftime("%b %d, %H:%M"),
            "type": h.item_type,
        })

    total_papers = PrepPaper.objects.filter(is_published=True).count()
    total_topics = PrepTopic.objects.count()
    total_questions = PrepQuestion.objects.count()

    featured_topics = []
    for t in PrepTopic.objects.select_related("course")[:4]:
        auth_cnt = PrepQuestion.objects.filter(
            Q(topic=t) | Q(topic_label__icontains=t.title),
            question_type="authentic"
        ).count()
        featured_topics.append({
            "id": t.id,
            "title": t.title,
            "course_code": t.course.code,
            "course_title": t.course.title,
            "authentic_count": auth_cnt,
        })

    # Latest study item for "Resume Study" hero banner
    latest_study_item = None
    latest_h = history_qs.first()
    if latest_h and latest_h.url:
        latest_study_item = {
            "title": latest_h.title,
            "course_code": latest_h.course_code,
            "url": latest_h.url,
            "type": latest_h.item_type or "Syllabus Revision",
        }
    elif featured_topics:
        ft0 = featured_topics[0]
        from django.urls import reverse
        latest_study_item = {
            "title": ft0["title"],
            "course_code": ft0["course_code"],
            "url": reverse("prep:topic_study", kwargs={"topic_id": str(ft0["id"])}),
            "type": "Syllabus Notes",
        }

    recent_credit_transactions = wallet.transactions.all()[:10]

    context = {
        "active_tab": "dashboard",
        "user_credits": wallet.credits_balance,
        "recent_courses": recent_courses,
        "recent_activity": recent_activity,
        "recent_credit_transactions": recent_credit_transactions,
        "total_active_courses": enrolled_courses.count(),
        "total_papers": total_papers,
        "total_topics": total_topics,
        "total_questions": total_questions,
        "featured_topics": featured_topics,
        "latest_study_item": latest_study_item,
    }
    return render(request, "prep/dashboard.html", context)


@login_required
def prep_courses(request):
    """Personal course list with search across the shared course catalogue."""
    wallet = PrepWallet.get_or_create_wallet(request.user)
    query = request.GET.get("q", "").strip()
    enrolled_course_ids = set(
        PrepCourseEnrollment.objects.filter(user=request.user).values_list("course_id", flat=True)
    )

    personal_courses_qs = PrepCourse.objects.filter(
        id__in=enrolled_course_ids,
        is_active=True,
    ).annotate(
        topics_count=Count("topics", distinct=True),
        papers_count=Count("papers", distinct=True),
    ).order_by("code")

    courses_data = []
    for c in personal_courses_qs:
        clean_title = c.title
        if c.code and c.code in clean_title:
            clean_title = re.sub(r"^" + re.escape(c.code) + r"[\s:\-\–—]*", "", clean_title, flags=re.IGNORECASE).strip()
            if not clean_title:
                clean_title = c.title
        courses_data.append({
            "code": c.code,
            "slug": c.slug or c.code.replace(" ", "-"),
            "title": clean_title,
            "level": c.level,
            "category": c.category,
            "topics": c.topics_count,
            "papers": c.papers_count,
        })

    search_results = []
    already_added_matches = []
    if query:
        matches = (
            PrepCourse.objects.filter(is_active=True)
            .filter(Q(code__icontains=query) | Q(title__icontains=query))
            .annotate(
                topics_count=Count("topics", distinct=True),
                papers_count=Count("papers", distinct=True),
            )
            .order_by("code")[:12]
        )
        for course in matches:
            title = re.sub(
                r"^" + re.escape(course.code) + r"[\s:\-\â€“\â€”]*",
                "",
                course.title,
                flags=re.IGNORECASE,
            ).strip() or course.title
            result = {
                "id": course.id,
                "code": course.code,
                "title": title,
                "level": course.level,
                "category": course.category,
                "topics": course.topics_count,
                "papers": course.papers_count,
            }
            if course.id in enrolled_course_ids:
                already_added_matches.append(result)
            else:
                search_results.append(result)

    context = {
        "active_tab": "courses",
        "user_credits": wallet.credits_balance,
        "courses": courses_data,
        "search_query": query,
        "search_results": search_results,
        "already_added_matches": already_added_matches,
    }
    return render(request, "prep/courses.html", context)


@login_required
def prep_add_course(request, course_id):
    """Add a public catalogue course to the requesting user's course list."""
    if request.method != "POST":
        return redirect("prep:courses")

    course = get_object_or_404(PrepCourse, pk=course_id, is_active=True)
    enrollment, created = PrepCourseEnrollment.objects.get_or_create(
        user=request.user,
        course=course,
        defaults={"source": "catalog"},
    )
    if created:
        messages.success(request, f"{course.code} was added to your courses.")
    else:
        messages.info(request, f"{course.code} is already in your courses.")

    return redirect("prep:courses")


@login_required
def prep_course_detail(request, course_code):
    """Syllabus Topics & Paper Breakdown for a Course."""
    clean_code = course_code.replace("-", " ").strip().upper()
    wallet = PrepWallet.get_or_create_wallet(request.user)

    course = PrepCourse.objects.filter(code__iexact=clean_code).first()
    if not course:
        course = PrepCourse.objects.filter(slug__iexact=course_code).first()
    if not course:
        # Try finding by slug or code starts
        course = PrepCourse.objects.filter(code__icontains=clean_code.split()[0]).first()

    if not course:
        messages.info(request, f"Course '{clean_code}' has not been added yet. Upload documents to index this course.")
        return redirect("prep:courses")

    topics_data = []
    course_papers = []
    total_questions_count = 0
    topics_qs = course.topics.all().order_by("order")
    for t in topics_qs:
        auth_count = PrepQuestion.objects.filter(
            Q(topic=t) | Q(topic_label__icontains=t.title),
            question_type="authentic"
        ).count()
        total_questions_count += auth_count
        raw_subtopics = t.subtopics if isinstance(t.subtopics, list) else []
        clean_subtopics = [clean_tag_label(str(st)) for st in raw_subtopics if clean_tag_label(str(st))]
        topics_data.append({
            "id": str(t.id),
            "num": t.order,
            "title": clean_tag_label(t.title),
            "subtopics": clean_subtopics,
            "authentic_count": auth_count,
        })

    for p in course.papers.filter(is_published=True).prefetch_related("questions"):
        course_papers.append({
            "id": p.id,
            "title": p.title,
            "year": p.year,
            "marks": p.total_marks,
            "questions_count": p.questions.count(),
        })

    pending_documents = []
    for d in course.documents.filter(stage__in=["stage_1", "stage_2"]).order_by("-created_at"):
        pending_documents.append({
            "id": str(d.id),
            "filename": d.file.name.split("/")[-1] if d.file else "Document",
            "doc_type": d.doc_type,
            "stage": d.stage,
            "stage_display": d.get_stage_display(),
            "academic_year": d.academic_year,
            "topic_name": d.topic_name,
            "created_at": d.created_at.strftime("%b %d, %Y"),
        })
    pending_review_count = len(pending_documents)

    # Clean display title to avoid duplication
    display_title = course.title
    if course.code and course.code in display_title:
        display_title = re.sub(r"^" + re.escape(course.code) + r"[\s:\-\–—]*", "", display_title, flags=re.IGNORECASE).strip()
        if not display_title:
            display_title = course.title

    course_obj = {
        "code": course.code,
        "title": display_title,
        "level": course.level,
        "description": course.description or "Canonical syllabus units, structured theorems, lecture notes, and past examination problems.",
    }

    context = {
        "active_tab": "courses",
        "user_credits": wallet.credits_balance,
        "course": course_obj,
        "topics": topics_data,
        "total_questions_count": total_questions_count,
        "course_papers": course_papers,
        "course_documents": pending_documents,
        "pending_documents": pending_documents,
        "pending_review_count": pending_review_count,
    }
    return render(request, "prep/course_detail.html", context)


@login_required
def prep_topic_study(request, topic_id):
    """
    Topic Study Engine:
    1. Toned Notes (Level 1 Intuition, Level 2 Standard, Level 3 Exam Mode)
    2. Authentic Past Examination Questions tagged to this syllabus topic
    3. Practice & Variant Generator (1 to 5 questions per run)
    """
    wallet = PrepWallet.get_or_create_wallet(request.user)
    from_tab = request.GET.get("from")
    active_subtab = request.GET.get("tab", "notes")  # 'notes', 'past_questions', 'practice'

    topic = None
    if str(topic_id).isdigit():
        topic = PrepTopic.objects.filter(id=int(topic_id)).select_related("course").first()

    if not topic:
        messages.info(request, "The requested syllabus topic was not found.")
        return redirect("prep:courses")

    course_code = topic.course.code
    course_title = topic.course.title
    topic_title = clean_tag_label(topic.title)
    raw_subtopics = topic.subtopics if isinstance(topic.subtopics, list) else []
    subtopics = [clean_tag_label(str(st)) for st in raw_subtopics if clean_tag_label(str(st))]

    # Log to revision history
    PrepHistory.objects.get_or_create(
        user=request.user,
        title=topic.title,
        course_code=topic.course.code,
        item_type="Lecture Notes",
        defaults={"url": reverse("prep:topic_study", kwargs={"topic_id": topic_id}) + "?from=history"},
    )

    # 1. Authentic KU CAT Questions for this topic
    from services.prep_ai_router import normalize_math_delimiters

    authentic_qs = []
    q_filter = (
        Q(topic=topic)
        | (
            Q(topic__isnull=True)
            & Q(paper__course=topic.course)
            & Q(topic_label__icontains=topic.title)
        )
    ) & Q(question_type="authentic")
    authentic_records = PrepQuestion.objects.filter(q_filter).select_related("paper")

    for q in authentic_records[:15]:
        paper_label = q.paper.title if q.paper else f"{course_code} Examination"
        year_label = q.paper.year if q.paper else "Official Examination"
        clean_q = normalize_math_delimiters(q.question_latex) if q.question_latex else ""
        clean_sol = normalize_math_delimiters(q.solution_latex) if q.solution_latex else ""
        authentic_qs.append({
            "id": q.id,
            "number": q.number,
            "marks": q.marks,
            "paper_title": paper_label,
            "year": year_label,
            "topic_label": q.topic_label or topic_title,
            "question_latex": clean_q,
            "solution_latex": clean_sol,
            "has_solution": bool(clean_sol),
        })

    # 2. Existing Practice Variants in DB
    generated_qs = []
    gen_records = PrepQuestion.objects.filter(
        topic=topic,
        question_type="generated",
        verification_status="verified",
    ).order_by("number")[:10]
    for q in gen_records:
        clean_g_q = normalize_math_delimiters(q.question_latex) if q.question_latex else ""
        clean_g_sol = normalize_math_delimiters(q.solution_latex) if q.solution_latex else ""
        generated_qs.append({
            "id": q.id,
            "number": q.number,
            "marks": q.marks,
            "topic_label": q.topic_label or topic_title,
            "question_latex": clean_g_q,
            "solution_latex": clean_g_sol,
            "is_cached": True,
        })

    # 3. Initial Topic Notes (Level 2 default)
    from services.prep_ai_router import get_or_generate_topic_notes
    initial_notes_res = get_or_generate_topic_notes(
        course_code=course_code,
        topic_title=topic_title,
        subtopics=subtopics,
        level="level_2",
        course_obj=topic.course if topic else None,
        topic_obj=topic,
        generate_if_missing=False,
    )
    initial_notes = initial_notes_res.get("notes", "") or initial_notes_res.get("content", "")
    initial_notes_error = ""
    if not initial_notes:
        initial_notes_error = initial_notes_res.get(
            "error", "No validated notes are available for this topic yet."
        )

    topic_dict = {
        "id": str(topic.id) if topic else str(topic_id),
        "title": topic_title,
        "course_code": course_code,
        "course_title": course_title,
        "subtopics": subtopics,
        "summary": topic.summary if (topic and topic.summary) else "Core syllabus definitions, theorems, and proofs.",
    }

    context = {
        "active_tab": "history" if from_tab == "history" else "courses",
        "active_subtab": active_subtab,
        "from_history": from_tab == "history",
        "user_credits": wallet.credits_balance,
        "topic": topic_dict,
        "initial_notes": initial_notes,
        "initial_notes_error": initial_notes_error,
        "initial_notes_stale": bool(initial_notes_res.get("stale")),
        "authentic_questions": authentic_qs,
        "generated_questions": generated_qs,
    }
    return render(request, "prep/topic_study.html", context)


@login_required
def prep_past_papers(request):
    """Legacy past papers route; redirect to courses catalogue."""
    return redirect("prep:courses")


@login_required
def prep_paper_detail(request, course_code, paper_id):
    """View questions of a specific CAT / Examination paper from DB."""
    clean_course = course_code.replace("-", " ").upper()
    wallet = PrepWallet.get_or_create_wallet(request.user)

    paper = PrepPaper.objects.filter(id=paper_id).prefetch_related("questions").first()

    if paper:
        questions_list = []
        for q in paper.questions.all().order_by("number"):
            questions_list.append({
                "number": q.number,
                "marks": q.marks,
                "topic": q.topic_label or "Mathematical Assessment",
                "question_latex": q.question_latex,
                "solution_latex": q.solution_latex,
            })
        paper_title = paper.title
        total_marks = paper.total_marks
        year = paper.year
        course_name = paper.course.code

        # Log history
        PrepHistory.objects.get_or_create(
            user=request.user,
            title=paper.title,
            course_code=course_name,
            item_type="CAT Paper",
            defaults={"url": reverse("prep:paper_detail", kwargs={"course_code": course_code, "paper_id": paper_id}) + "?from=history"},
        )
    else:
        paper_title = "Continuous Assessment Test 1 (CAT 1)"
        if "cat2" in paper_id:
            paper_title = "Continuous Assessment Test 2 (CAT 2)"
        elif "exam" in paper_id:
            paper_title = "Final Examination Paper"
        total_marks = 30 if "cat" in paper_id else 70
        year = "2024/2025 Academic Year"
        course_name = clean_course
        questions_list = [
            {
                "number": 1,
                "marks": 10,
                "topic": "Metric Spaces",
                "question_latex": r"Let $(X, d)$ be a metric space. Prove that every open ball $B_r(x) = \{y \in X : d(x, y) < r\}$ is an open set in $(X, d)$.",
            },
            {
                "number": 2,
                "marks": 10,
                "topic": "Discrete Topology",
                "question_latex": r"Show that the discrete metric $d(x, y) = 1$ if $x \neq y$ and $0$ if $x = y$ induces the discrete topology on any set $X$.",
            },
            {
                "number": 3,
                "marks": 10,
                "topic": "Sequential Compactness",
                "question_latex": r"State the Bolzano-Weierstrass theorem for $\mathbb{R}^n$ and prove that every bounded sequence in $\mathbb{R}^n$ contains a convergent subsequence.",
            },
        ]

    from_tab = request.GET.get("from")
    context = {
        "active_tab": "history" if from_tab == "history" else "practice",
        "from_history": from_tab == "history",
        "user_credits": wallet.credits_balance,
        "course_code": course_name,
        "paper_title": paper_title,
        "paper_id": paper_id,
        "year": year,
        "total_marks": total_marks,
        "questions": questions_list,
    }
    return render(request, "prep/paper_detail.html", context)


@login_required
def prep_practice(request, topic_id):
    """Redirect topic practice request to organized paper detail or topic questions."""
    first_paper = PrepPaper.objects.filter(is_published=True).first()
    if first_paper:
        return redirect("prep:paper_detail", course_code=first_paper.course.code.replace(" ", "-"), paper_id=first_paper.id)
    return redirect("prep:past_papers")


@login_required
def prep_upload(request):
    """Document Ingestion Hub with user-specified document metadata and database record creation."""
    wallet = PrepWallet.get_or_create_wallet(request.user)

    if request.method == "POST":
        course_name = request.POST.get("course_name", "").strip()
        doc_type = request.POST.get("doc_type", "Lecture Notes")
        academic_year = request.POST.get("academic_year", "").strip()
        topic_name = request.POST.get("topic_name", "").strip()
        uploaded_file = request.FILES.get("file")

        if not course_name:
            messages.error(request, "Please specify the Course Name or Code.")
            return redirect("prep:upload")

        if not uploaded_file:
            messages.error(request, "Please attach a document file to upload.")
            return redirect("prep:upload")

        # Supported formats check (.pdf, .docx, .doc, .md, .txt)
        valid_extensions = (".pdf", ".docx", ".doc", ".md", ".txt")
        file_ext = os.path.splitext(uploaded_file.name.lower())[1]
        if file_ext not in valid_extensions:
            messages.error(request, "Unsupported file format. Please upload a PDF (.pdf), Word document (.docx), or Markdown file (.md, .txt).")
            return redirect("prep:upload")

        # 15 MB File Limit Check
        max_bytes = 15 * 1024 * 1024
        if uploaded_file.size > max_bytes:
            messages.error(request, "File size exceeds the 15 MB limit. Please upload a smaller document.")
            return redirect("prep:upload")

        # Courses are shared across Mentify Prep. Uploading new material adds to
        # the global catalogue after it has been indexed and reviewed.
        course_code, course_title = parse_course_code_and_title(course_name)
        course = PrepCourse.objects.filter(code__iexact=course_code).first()
        if not course:
            course = PrepCourse.objects.create(
                code=course_code,
                title=course_title,
                level="Undergraduate",
                category="Mathematics" if "SMA" in course_code else ("Statistics" if "SST" in course_code else "Computing"),
            )
            PrepCourseEnrollment.objects.create(user=request.user, course=course, source="upload")
        else:
            PrepCourseEnrollment.objects.get_or_create(
                user=request.user,
                course=course,
                defaults={"source": "upload"},
            )

        # Create Document in Stage 1
        prep_doc = PrepDocument.objects.create(
            user=request.user,
            course=course,
            doc_type=doc_type,
            academic_year=academic_year,
            topic_name=topic_name,
            file=uploaded_file,
            file_size_bytes=uploaded_file.size,
            stage="stage_1",
        )

        # Trigger Step 3 Ingestion Pipeline (pdfplumber + Together Vision OCR + Topic Extraction)
        from services.prep_ingestion import process_prep_document
        try:
            res = process_prep_document(prep_doc)
            if not res.get("success"):
                messages.error(request, res.get("error", "The document could not be processed."))
                return redirect("prep:upload")
            if res.get("duplicate"):
                messages.info(
                    request,
                    f"'{uploaded_file.name}' matches material already submitted for {course.code}. It was saved for audit but no duplicate indexing or credits were applied.",
                )
                return redirect("prep:course_detail", course_code=course.slug or course.code)
            method = res.get("method_used", "")
            if method == "digital_pdfplumber":
                method_label = "Digital PDF Parser ($0)"
            elif method == "digital_docx":
                method_label = "Word Parser ($0)"
            elif method == "digital_markdown":
                method_label = "Markdown Parser ($0)"
            else:
                method_label = "Vision OCR"

            updates_count = res.get("updates_proposed", 0)
            updates_txt = f" {updates_count} course update(s) are ready for tutor review." if updates_count else " No new course changes were detected."

            messages.success(
                request,
                f"'{uploaded_file.name}' successfully parsed via {method_label}.{updates_txt} "
                f"Course materials advanced to Stage 2: Tutor Review Gate ({res.get('credits_deducted', 2)} credits).",
            )
        except Exception as e:
            messages.success(
                request,
                f"'{uploaded_file.name}' uploaded and queued for Stage 1 Ingestion.",
            )

        # Log History
        course_slug = course.slug or course.code.replace(" ", "-")
        PrepHistory.objects.create(
            user=request.user,
            title=f"Uploaded {uploaded_file.name}",
            course_code=course.code,
            item_type=doc_type,
            url=reverse("prep:course_detail", kwargs={"course_code": course_slug}),
        )

        return redirect("prep:course_detail", course_code=course_slug)

    # Recent uploads for this user
    user_docs = PrepDocument.objects.filter(user=request.user).order_by("-created_at")[:5]
    recent_uploads = []
    for d in user_docs:
        size_mb = round(d.file_size_bytes / (1024 * 1024), 1) if d.file_size_bytes else 0
        recent_uploads.append({
            "filename": d.file.name.split("/")[-1] if d.file else "Document.pdf",
            "course": d.course.code,
            "type": d.doc_type,
            "size": f"{size_mb} MB" if size_mb > 0 else "< 1 MB",
            "date": d.created_at.strftime("%Y-%m-%d"),
            "stage": d.get_stage_display(),
        })

    context = {
        "active_tab": "upload",
        "user_credits": wallet.credits_balance,
        "recent_uploads": recent_uploads,
        "search_query": request.GET.get("q", "").strip(),
    }
    if context["search_query"]:
        query = context["search_query"]
        enrolled_ids = set(
            PrepCourseEnrollment.objects.filter(user=request.user).values_list("course_id", flat=True)
        )
        matches = list(
            PrepCourse.objects.filter(is_active=True)
            .filter(Q(code__icontains=query) | Q(title__icontains=query) | Q(category__icontains=query))
            .annotate(topics_count=Count("topics", distinct=True), papers_count=Count("papers", distinct=True))[:10]
        )
        for match in matches:
            match.is_added = match.id in enrolled_ids
        context["matching_courses"] = matches
    else:
        context["matching_courses"] = []
    context["show_upload_form"] = request.GET.get("upload") == "1" or (
        bool(context["search_query"]) and not context["matching_courses"]
    )
    return render(request, "prep/upload.html", context)


@login_required
def prep_history(request):
    """Legacy revision history route; redirect to dashboard."""
    return redirect("prep:dashboard")


@login_required
def prep_billing(request):
    """Credit Balance & M-Pesa Top-Up Page connected to PrepWallet."""
    wallet = PrepWallet.get_or_create_wallet(request.user)

    if wallet.current_plan == "pro":
        plan_display = "Pro (Exam Master)"
    elif wallet.current_plan == "plus":
        plan_display = "Plus (Semester Pass)"
    elif wallet.current_plan == "basic":
        plan_display = "Basic (Starter Prep)"
    elif wallet.current_plan == "expired":
        plan_display = "Free Trial Expired"
    else:
        plan_display = "Free Trial (3 Days)"

    recent_transactions = wallet.transactions.all()[:10]

    context = {
        "active_tab": "billing",
        "wallet": wallet,
        "user_credits": wallet.credits_balance,
        "current_plan": plan_display,
        "is_trial": wallet.current_plan == "trial",
        "can_top_up": has_active_subscription(wallet),
        "plan_expires_at": wallet.plan_expires_at,
        "recent_transactions": recent_transactions,
        "topup_price_kes": 150,
        "plans": [
            {
                "id": "basic_plan",
                "name": "Basic (Starter Prep)",
                "price": "KES 399 / mo",
                "price_num": 399,
                "credits": "250 Credits/mo",
                "tagline": "Essential credits for targeted practice and CAT prep",
                "is_popular": False,
                "theme_color": "#2563eb",
                "theme_bg": "rgba(37, 99, 235, 0.08)",
                "badge_label": "STARTER",
                "features": [
                    "250 Monthly Credits",
                    "10 Document / PDF Uploads",
                    "100 Practice Exam Questions",
                    "5 Handwritten & Scanned Exam Uploads",
                    "Full PDF & DOCX Study Pack Downloads",
                    "Step-by-Step Proofs & Derivations",
                    "All 3 Explanation Levels",
                    "Standard Generation Queue",
                ],
                "active": wallet.current_plan == "basic",
            },
            {
                "id": "plus_plan",
                "name": "Plus (Semester Pass)",
                "price": "KES 499 / mo",
                "price_num": 499,
                "credits": "450 Credits/mo",
                "tagline": "Most Popular: Balanced credits for active, consistent semester revision",
                "is_popular": True,
                "theme_color": "var(--green)",
                "theme_bg": "rgba(15, 118, 110, 0.08)",
                "badge_label": "RECOMMENDED",
                "features": [
                    "450 Monthly Credits",
                    "20 Document / PDF Uploads",
                    "200 Practice Exam Questions",
                    "15 Handwritten & Scanned Exam Uploads",
                    "Full PDF & DOCX Study Pack Downloads",
                    "Step-by-Step Proofs & Derivations",
                    "All 3 Explanation Levels",
                    "Priority Generation Queue",
                ],
                "active": wallet.current_plan == "plus",
            },
            {
                "id": "pro_plan",
                "name": "Pro (Exam Master)",
                "price": "KES 799 / mo",
                "price_num": 799,
                "credits": "750 Credits/mo",
                "tagline": "Maximum credit volume for intensive practice and heavy revision",
                "is_popular": False,
                "theme_color": "#7c3aed",
                "theme_bg": "rgba(124, 58, 237, 0.08)",
                "badge_label": "FULL ACCESS",
                "features": [
                    "750 Monthly Credits",
                    "40 Document / PDF Uploads",
                    "350 Practice Exam Questions",
                    "30 Handwritten & Scanned Exam Uploads",
                    "Full PDF & DOCX Study Pack Downloads",
                    "Step-by-Step Proofs & Derivations",
                    "All 3 Explanation Levels",
                    "Top Priority Queue & Exam Support",
                ],
                "active": wallet.current_plan == "pro",
            },
        ],
    }
    return render(request, "prep/billing.html", context)


# ─── Step 5: Paystack & M-Pesa Payments ──────────────────────────────────────

import uuid
from datetime import timedelta
from django.db import transaction
from django.conf import settings
from services.paystack_service import PaystackService

PREP_PACKAGES = {
    "topup_100": {
        "name": "100 Credits Top-Up",
        "price_kes": 150,
        "credits": 100,
        "type": "topup",
    },
    "basic_plan": {
        "name": "Basic (Starter Prep)",
        "price_kes": 399,
        "credits": 250,
        "type": "plan",
        "plan_id": "basic",
    },
    "plus_plan": {
        "name": "Plus (Semester Pass)",
        "price_kes": 499,
        "credits": 450,
        "type": "plan",
        "plan_id": "plus",
    },
    "pro_plan": {
        "name": "Pro (Exam Master)",
        "price_kes": 799,
        "credits": 750,
        "type": "plan",
        "plan_id": "pro",
    },
}


@login_required
def prep_initiate_payment(request):
    """Initiate M-Pesa / Paystack payment for credits or monthly exam plan."""
    if request.method != "POST":
        return redirect("prep:billing")

    package_key = request.POST.get("package", "topup_100")
    package = PREP_PACKAGES.get(package_key)
    if not package:
        messages.error(request, "Invalid payment package selected.")
        return redirect("prep:billing")

    if package["type"] == "topup" and not has_active_subscription(PrepWallet.get_or_create_wallet(request.user)):
        messages.error(request, "Credit top-ups are available only while you have an active subscription.")
        return redirect("prep:billing")

    reference = f"PREP-{uuid.uuid4().hex[:12].upper()}"
    amount_cents = package["price_kes"] * 100
    callback_url = request.build_absolute_uri(reverse("prep:payment_callback"))

    metadata = {
        "user_id": request.user.id,
        "user_email": request.user.email,
        "package_key": package_key,
        "package_name": package["name"],
        "credits": package["credits"],
        "package_type": package["type"],
        "plan_id": package.get("plan_id"),
        "scope": "prep",
    }

    paystack = PaystackService(
        secret_key=getattr(settings, "PAYSTACK_SECRET_KEY", ""),
        public_key=getattr(settings, "PAYSTACK_PUBLIC_KEY", ""),
        currency=getattr(settings, "PAYSTACK_CURRENCY", "KES"),
    )

    status_code, body = paystack.initialize(
        email=request.user.email,
        amount_cents=amount_cents,
        reference=reference,
        callback_url=callback_url,
        metadata=metadata,
    )

    if status_code == 200 and body.get("status"):
        auth_url = body.get("data", {}).get("authorization_url")
        if auth_url:
            return redirect(auth_url)

    err = paystack.friendly_error(body, fallback="Could not initiate M-Pesa / Card payment.")
    messages.error(request, f"Payment initialization failed: {err}")
    return redirect("prep:billing")


@login_required
def prep_payment_callback(request):
    """Callback after Paystack M-Pesa / Card transaction."""
    reference = request.GET.get("reference") or request.GET.get("trxref")
    if not reference:
        messages.error(request, "No transaction reference provided.")
        return redirect("prep:billing")

    paystack = PaystackService(
        secret_key=getattr(settings, "PAYSTACK_SECRET_KEY", ""),
        currency=getattr(settings, "PAYSTACK_CURRENCY", "KES"),
    )

    status_code, body = paystack.verify(reference)
    if status_code == 200 and body.get("status") and body.get("data", {}).get("status") == "success":
        data = body.get("data", {})
        metadata = data.get("metadata", {})
        credits_to_add = metadata.get("credits", 100)
        package_name = metadata.get("package_name", "Credit Top-Up")
        package_type = metadata.get("package_type", "topup")
        plan_id = metadata.get("plan_id")
        amount_kes = data.get("amount", 0) // 100

        with transaction.atomic():
            wallet = PrepWallet.get_or_create_wallet(request.user)
            # Check if this reference was already credited to prevent duplicate credit grants
            existing_tx = PrepTransaction.objects.filter(reference_code=reference).first()
            if not existing_tx:
                if package_type == "plan" and plan_id:
                    grant_subscription(wallet, plan_id, int(credits_to_add), reference_code=reference)
                else:
                    if not has_active_subscription(wallet):
                        messages.error(
                            request,
                            "The payment was received, but top-up credits require an active subscription. Please contact support with your payment reference.",
                        )
                        return redirect("prep:billing")
                    grant_purchased_topup(
                        wallet,
                        int(credits_to_add),
                        reference_code=reference,
                        description=f"{package_name} (KES {amount_kes}) via Paystack/M-Pesa",
                    )

                wallet.refresh_from_db()

                # Step 6 Email Automation (Resend)
                try:
                    from services.email_service import send_prep_credit_topup_email
                    send_prep_credit_topup_email(wallet, int(credits_to_add), amount_kes, reference, package_name)
                except Exception:
                    pass

        messages.success(request, f"Payment of KES {amount_kes} confirmed! Added {credits_to_add} credits to your Mentify Prep wallet. Receipt sent to your email.")
        return redirect("prep:billing")

    err = paystack.friendly_error(body, fallback="Transaction was not successful or was cancelled.")
    messages.error(request, f"Payment verification: {err}")
    return redirect("prep:billing")



# ─── Step 4: AI Model Router & Zero-Cost Cache JSON Endpoints ────────────────

from django.http import JsonResponse
import json
from services.prep_ai_router import (
    get_or_generate_question_solution,
    get_or_generate_topic_notes,
    generate_similar_practice_questions,
)


@login_required
def prep_solve_question_api(request):
    """
    Solves a question with step-by-step mathematical proof.
    Zero-cost database cache first ($0).
    If fresh generation, routes to DeepSeek-R1, deducts 5 credits, and caches result.
    """
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "POST method required."}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8")) if request.body else request.POST
    except Exception:
        data = request.POST

    question_id = data.get("question_id")
    question_latex = data.get("question_latex", "").strip()
    course_code = data.get("course_code", "").strip()
    topic_label = data.get("topic_label", "").strip()

    wallet = PrepWallet.get_or_create_wallet(request.user)

    q_obj = None
    if question_id:
        try:
            q_obj = PrepQuestion.objects.filter(id=int(question_id)).first()
            if q_obj:
                question_latex = q_obj.question_latex
                course_code = q_obj.paper.course.code if q_obj.paper else (q_obj.topic.course.code if q_obj.topic else course_code)
                topic_label = q_obj.topic_label or (q_obj.topic.title if q_obj.topic else topic_label)
                # If already solved in DB, return at 0 credits
                if q_obj.solution_latex:
                    return JsonResponse({
                        "success": True,
                        "solution": q_obj.solution_latex,
                        "cached": True,
                        "credits_deducted": 0,
                        "model": "Database Verified Cache ($0)",
                        "credits_balance": wallet.credits_balance,
                    })
        except Exception:
            pass

    if not question_latex:
        return JsonResponse({"success": False, "error": "No question LaTeX provided."}, status=400)

    # Check credit balance before fresh AI call
    minimum_cost = 5
    required_balance = estimated_generation_credits(minimum=minimum_cost)
    if get_available_credits(wallet) < required_balance:
        return JsonResponse({
            "success": False,
            "error": f"Insufficient credits. You need at least {required_balance} credits available before generating a step-by-step verified solution. Please subscribe or top up.",
            "credits_balance": wallet.credits_balance,
        }, status=402)

    # Call AI router (with DB cache layer)
    res = get_or_generate_question_solution(
        question_latex=question_latex,
        course_code=course_code or "Mathematics",
        topic_label=topic_label,
        question_obj=q_obj,
    )

    if not res.get("solution"):
        return JsonResponse({"success": False, "error": res.get("error", "Failed to generate solution.")}, status=500)

    # If was cached, 0 credits deducted!
    credits_deducted = 0

    if not res.get("cached"):
        credits_deducted = credits_for_usage(res.get("usage"), minimum=minimum_cost)
        try:
            consume_credits(
                wallet,
                credits_deducted,
                action_type="deep_reasoning",
                description=f"Verified Solution & Proof: {course_code} ({topic_label})",
                usage=res.get("usage"),
                model_name=res.get("model", "deepseek-reasoner"),
            )
        except InsufficientCredits:
            return JsonResponse({
                "success": False,
                "error": "The generated solution requires more credits than are currently available. Please subscribe or top up, then try again.",
                "credits_balance": get_available_credits(wallet),
            }, status=402)

        # Trigger low credit alert if balance is running low
        wallet.refresh_from_db()
        if wallet.credits_balance <= 10:
            try:
                from services.email_service import send_prep_low_credits_email
                send_prep_low_credits_email(wallet)
            except Exception:
                pass

    return JsonResponse({
        "success": True,
        "solution": res["solution"],
        "reasoning": res.get("reasoning", ""),
        "cached": res.get("cached", False),
        "credits_deducted": credits_deducted,
        "credits_balance": wallet.credits_balance,
        "model": res.get("model", "deepseek-reasoner"),
    })


@login_required
def prep_topic_notes_api(request):
    """
    Retrieve or generate syllabus topic notes for a specific level (1, 2, or 3).
    Checks PrepContentCache ($0). If missing, generates via DeepSeek-V3 and caches.
    """
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "POST method required."}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8")) if request.body else request.POST
    except Exception:
        data = request.POST

    topic_id = data.get("topic_id")
    course_code = data.get("course_code", "").strip()
    topic_title = data.get("topic_title", "").strip()
    level = data.get("level", "level_2")

    wallet = PrepWallet.get_or_create_wallet(request.user)

    topic_obj = None
    if topic_id and str(topic_id).isdigit():
        topic_obj = PrepTopic.objects.filter(id=int(topic_id)).first()
        if topic_obj:
            topic_title = topic_obj.title
            course_code = topic_obj.course.code

    if not topic_title:
        return JsonResponse({"success": False, "error": "Topic title is required."}, status=400)

    subtopics = topic_obj.subtopics if (topic_obj and isinstance(topic_obj.subtopics, list)) else []

    # Read the shared validated cache before permitting an AI generation. This
    # prevents a page request from spending provider tokens for a user whose
    # wallet cannot cover a new level.
    cached_res = get_or_generate_topic_notes(
        course_code=course_code or "Course",
        topic_title=topic_title,
        subtopics=subtopics,
        level=level,
        course_obj=topic_obj.course if topic_obj else None,
        topic_obj=topic_obj,
        generate_if_missing=False,
    )

    if cached_res.get("notes") or cached_res.get("content"):
        res = cached_res
    else:
        required_balance = estimated_generation_credits(minimum=1)
        if (
            not cached_res.get("regenerated_from_invalid_cache")
            and get_available_credits(wallet) < required_balance
        ):
            return JsonResponse({
                "success": False,
                "error": (
                    f"Insufficient credits. At least {required_balance} credits are required "
                    "before generating a new notes level."
                ),
                "credits_balance": wallet.credits_balance,
            }, status=402)

        res = get_or_generate_topic_notes(
            course_code=course_code or "Course",
            topic_title=topic_title,
            subtopics=subtopics,
            level=level,
            course_obj=topic_obj.course if topic_obj else None,
            topic_obj=topic_obj,
        )

    if res.get("error") and not res.get("notes"):
        return JsonResponse({"success": False, "error": res["error"]}, status=500)

    credits_deducted = 0
    if not res.get("cached") and not res.get("regenerated_from_invalid_cache"):
        credits_deducted = credits_for_usage(res.get("usage"), minimum=1)
        try:
            consume_credits(
                wallet,
                credits_deducted,
                action_type="topic_notes",
                description=f"AI Topic Notes ({level}): {course_code} - {topic_title}",
                usage=res.get("usage"),
                model_name=res.get("model", "deepseek-chat"),
            )
        except InsufficientCredits:
            return JsonResponse({
                "success": False,
                "error": "These notes require more credits than are currently available. Please subscribe or top up, then try again.",
                "credits_balance": get_available_credits(wallet),
            }, status=402)

    wallet.refresh_from_db()

    notes_payload = res.get("notes", "") or res.get("content", "")
    return JsonResponse({
        "success": True,
        "notes": notes_payload,
        "level": res.get("level", level),
        "cached": res.get("cached", False),
        "credits_deducted": credits_deducted,
        "credits_balance": wallet.credits_balance,
        "model": res.get("model", "deepseek-chat"),
    })


@login_required
def prep_generate_practice_api(request):
    """
    Generate 1 to 5 similar practice questions + step-by-step answers per topic.
    Serves cached variants at 0 credits.
    Deducts 1 credit per fresh generated question variant.
    """
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "POST method required."}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8")) if request.body else request.POST
    except Exception:
        data = request.POST

    topic_id = data.get("topic_id")
    course_code = data.get("course_code", "").strip()
    topic_title = data.get("topic_title", "").strip()
    raw_count = data.get("count", 3)
    try:
        count = int(raw_count)
    except (ValueError, TypeError):
        count = 3
    count = max(1, min(count, 5))

    wallet = PrepWallet.get_or_create_wallet(request.user)

    topic_obj = None
    if topic_id and str(topic_id).isdigit():
        topic_obj = PrepTopic.objects.filter(id=int(topic_id)).first()
        if topic_obj:
            topic_title = topic_obj.title
            course_code = topic_obj.course.code

    if not topic_title:
        return JsonResponse({"success": False, "error": "Topic title or valid topic ID is required."}, status=400)
    if not topic_obj:
        return JsonResponse({
            "success": False,
            "error": "Practice questions can only be generated for a saved course topic.",
        }, status=400)

    # Gather authentic sample questions for this topic as guidance
    authentic_samples = []
    if topic_obj:
        auth_qs = PrepQuestion.objects.filter(
            (
                Q(topic=topic_obj)
                | (
                    Q(topic__isnull=True)
                    & Q(paper__course=topic_obj.course)
                    & Q(topic_label__icontains=topic_title)
                )
            ) & Q(question_type="authentic"),
        )[:3]
        for q in auth_qs:
            authentic_samples.append(f"Q{q.number} ({q.marks} marks): {q.question_latex}")

    # Check existing generated questions in DB
    existing_generated = (
        PrepQuestion.objects.filter(
            topic=topic_obj,
            question_type="generated",
            verification_status="verified",
        ).count()
        if topic_obj
        else 0
    )
    fresh_needed = max(0, count - existing_generated)

    if fresh_needed > 0:
        try:
            enforce_subscription_limit(wallet, "practice_questions", fresh_needed)
        except PlanLimitExceeded as exc:
            return JsonResponse({"success": False, "error": str(exc)}, status=403)

    # Require a protected minimum before an uncached model generation.
    required_balance = estimated_generation_credits(minimum=max(1, fresh_needed))
    if fresh_needed > 0 and get_available_credits(wallet) < required_balance:
        return JsonResponse({
            "success": False,
            "error": f"Insufficient credits. At least {required_balance} credits are required to generate fresh practice questions. Please subscribe or top up.",
            "credits_balance": wallet.credits_balance,
        }, status=402)

    res = generate_similar_practice_questions(
        course_code=course_code or "Course",
        topic_title=topic_title,
        question_count=count,
        authentic_samples=authentic_samples,
        topic_obj=topic_obj,
        course_obj=topic_obj.course if topic_obj else None,
    )

    if not res.get("success"):
        return JsonResponse({
            "success": False,
            "error": res.get("error") or "Practice questions could not be generated at this time.",
        }, status=500)

    fresh_count = res.get("fresh_generated_count", 0)
    credits_deducted = 0

    if fresh_count > 0:
        credits_deducted = credits_for_usage(res.get("usage"), minimum=fresh_count)
        try:
            consume_credits(
                wallet,
                credits_deducted,
                action_type="ai_practice_gen",
                description=f"Generated {fresh_count} Practice Questions: {course_code} - {topic_title}",
                usage=res.get("usage"),
                model_name=res.get("model", "deepseek-chat"),
                metadata={"question_count": fresh_count},
            )
        except InsufficientCredits:
            return JsonResponse({
                "success": False,
                "error": "The generated practice set requires more credits than are currently available. Please subscribe or top up, then try again.",
                "credits_balance": get_available_credits(wallet),
            }, status=402)

        # Low credits advisory
        wallet.refresh_from_db()
        if wallet.credits_balance <= 10:
            try:
                from services.email_service import send_prep_low_credits_email
                send_prep_low_credits_email(wallet)
            except Exception:
                pass

    return JsonResponse({
        "success": True,
        "questions": res.get("questions", []),
        "fresh_count": fresh_count,
        "cached": res.get("cached", False),
        "credits_deducted": credits_deducted,
        "credits_balance": wallet.credits_balance,
        "model": res.get("model", "deepseek-chat"),
    })


# ─── Step 7: LaTeX Document Exports (PDF & DOCX) ─────────────────────────────

from django.http import HttpResponse
from services.prep_export_service import (
    export_topic_notes_pdf,
    export_topic_notes_docx,
    export_paper_questions_pdf,
    export_paper_questions_docx,
)


@login_required
def prep_export_topic(request, topic_id, fmt="pdf"):
    """Export syllabus topic notes in PDF or DOCX format."""
    topic = None
    if str(topic_id).isdigit():
        topic = PrepTopic.objects.filter(id=int(topic_id)).first()

    course_code = topic.course.code if topic else "SMA 300"
    topic_title = topic.title if topic else "Metric Spaces & Topology"

    level = request.GET.get("level", "level_2").strip().lower()
    if level not in {"level_1", "level_2", "level_3"}:
        level = "level_2"

    section = request.GET.get("section", "notes").strip().lower()
    if section == "questions_answers":
        if not topic:
            return HttpResponse("The requested syllabus topic was not found.", status=404)

        topic_filter = (
            Q(topic=topic)
            | (
                Q(topic__isnull=True)
                & Q(paper__course=topic.course)
                & Q(topic_label__icontains=topic_title)
            )
        ) & Q(question_type="authentic")
        authentic_records = PrepQuestion.objects.filter(
            topic_filter,
            question_type="authentic",
        ).select_related("paper").order_by("paper", "number", "id")
        generated_records = PrepQuestion.objects.filter(
            topic=topic,
            question_type="generated",
            verification_status="verified",
        ).order_by("number", "id")

        questions_data = []
        for source_label, records in (
            ("Authentic past question", authentic_records),
            ("Generated practice question", generated_records),
        ):
            for question in records:
                questions_data.append({
                    "number": len(questions_data) + 1,
                    "marks": question.marks,
                    "topic": f"{source_label}: {question.topic_label or topic_title}",
                    "question_latex": question.question_latex,
                    "solution_latex": question.solution_latex,
                })

        if not questions_data:
            return HttpResponse(
                "No authentic or validated generated questions are available for this topic yet.",
                status=404,
                content_type="text/plain; charset=utf-8",
            )

        clean_slug = topic_title.lower().replace(" ", "_")[:35]
        total_marks = sum(question["marks"] for question in questions_data)
        pdf_bytes = export_paper_questions_pdf(
            course_code,
            f"{topic_title} Questions and Answers",
            "Compiled Topic Set",
            total_marks,
            questions_data,
            include_questions=True,
            include_answers=True,
        )
        response = HttpResponse(pdf_bytes, content_type="application/pdf")
        response["Content-Disposition"] = (
            f'attachment; filename="{course_code}_{clean_slug}_questions_answers.pdf"'
        )
        return response

    # 1. Fetch complete revision notes for the requested level
    from services.prep_ai_router import get_or_generate_topic_notes
    notes_res = get_or_generate_topic_notes(
        course_code=course_code,
        topic_title=topic_title,
        subtopics=topic.subtopics if (topic and isinstance(topic.subtopics, list)) else [],
        level=level,
        course_obj=topic.course if topic else None,
        topic_obj=topic,
        generate_if_missing=False,
    )
    notes_content = notes_res.get("notes", "") or notes_res.get("content", "")
    if not notes_content:
        return HttpResponse(
            notes_res.get("error") or "No validated notes are available for this topic yet.",
            status=503,
            content_type="text/plain; charset=utf-8",
        )

    # 2. Fetch authentic questions mapped to this topic
    q_filter = (
        Q(topic=topic)
        | (
            Q(topic__isnull=True)
            & Q(paper__course=topic.course)
            & Q(topic_label__icontains=topic_title)
        )
    ) & Q(question_type="authentic")
    authentic_qs = []
    for q in PrepQuestion.objects.filter(q_filter).select_related("paper")[:15]:
        authentic_qs.append({
            "number": q.number,
            "marks": q.marks,
            "paper_title": q.paper.title if q.paper else f"{course_code} Examination",
            "year": q.paper.year if q.paper else "Official Examination",
            "question_latex": q.question_latex,
            "solution_latex": q.solution_latex,
        })

    # 3. Fetch practice questions for this topic
    practice_qs = []
    if topic:
        for q in PrepQuestion.objects.filter(
            topic=topic,
            question_type="generated",
            verification_status="verified",
        ).order_by("number")[:10]:
            practice_qs.append({
                "number": q.number,
                "marks": q.marks,
                "topic": q.topic_label or topic_title,
                "question_latex": q.question_latex,
                "solution_latex": q.solution_latex,
            })

    clean_slug = topic_title.lower().replace(" ", "_")[:35]

    if fmt.lower() == "docx":
        docx_bytes = export_topic_notes_docx(
            course_code,
            topic_title,
            notes_content,
            authentic_questions=authentic_qs,
            practice_questions=practice_qs,
        )
        resp = HttpResponse(
            docx_bytes,
            content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
        resp["Content-Disposition"] = f'attachment; filename="{course_code}_{clean_slug}_{level}_study_pack.docx"'
        return resp
    else:
        pdf_bytes = export_topic_notes_pdf(
            course_code,
            topic_title,
            notes_content,
            authentic_questions=authentic_qs,
            practice_questions=practice_qs,
            level=level,
        )
        resp = HttpResponse(pdf_bytes, content_type="application/pdf")
        resp["Content-Disposition"] = f'attachment; filename="{course_code}_{clean_slug}_{level}_study_pack.pdf"'
        return resp


@login_required
def prep_export_paper(request, course_code, paper_id, fmt="pdf"):
    """Export a past paper as questions, answers, or the existing combined pack."""
    paper = PrepPaper.objects.filter(id=paper_id).prefetch_related("questions").first()

    clean_course = course_code.replace("-", " ").upper()
    paper_title = paper.title if paper else "Continuous Assessment Test 1 (CAT 1)"
    year = paper.year if paper else "2024/2025 Academic Year"
    total_marks = paper.total_marks if paper else 30

    questions_data = []
    if paper and paper.questions.exists():
        for q in paper.questions.all().order_by("number"):
            questions_data.append({
                "number": q.number,
                "marks": q.marks,
                "topic": q.topic_label or "Mathematical Assessment",
                "question_latex": q.question_latex,
                "solution_latex": q.solution_latex,
            })
    else:
        questions_data = [
            {
                "number": 1,
                "marks": 10,
                "topic": "Metric Spaces",
                "question_latex": r"Let $(X, d)$ be a metric space. Prove that every open ball $B_r(x) = \{y \in X : d(x, y) < r\}$ is an open set in $(X, d)$.",
                "solution_latex": r"Proof: Let y in B_r(x). Take epsilon = r - d(x, y) > 0. For any z in B_epsilon(y), d(x, z) <= d(x, y) + d(y, z) < d(x, y) + r - d(x, y) = r. Hence B_epsilon(y) subset B_r(x), so B_r(x) is open. Q.E.D.",
            },
            {
                "number": 2,
                "marks": 10,
                "topic": "Discrete Topology",
                "question_latex": r"Show that the discrete metric $d(x, y) = 1$ if $x \neq y$ and $0$ if $x = y$ induces the discrete topology on any set $X$.",
                "solution_latex": r"Proof: Every singleton {x} = B_{1/2}(x) is an open ball, so every singleton is open. Since any subset is a union of singletons, every subset is open. Q.E.D.",
            },
        ]

    safe_id = paper_id.replace(" ", "_")
    section = request.GET.get("section", "both").strip().lower()
    section_map = {
        "questions": (True, False, "questions"),
        "answers": (False, True, "answers"),
        "both": (True, True, "study_pack"),
    }
    include_questions, include_answers, filename_suffix = section_map.get(section, section_map["both"])

    if fmt.lower() == "docx":
        docx_bytes = export_paper_questions_docx(clean_course, paper_title, year, total_marks, questions_data)
        resp = HttpResponse(
            docx_bytes,
            content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
        resp["Content-Disposition"] = f'attachment; filename="{clean_course}_{safe_id}.docx"'
        return resp
    else:
        pdf_bytes = export_paper_questions_pdf(
            clean_course,
            paper_title,
            year,
            total_marks,
            questions_data,
            include_questions=include_questions,
            include_answers=include_answers,
        )
        resp = HttpResponse(pdf_bytes, content_type="application/pdf")
        resp["Content-Disposition"] = f'attachment; filename="{clean_course}_{safe_id}_{filename_suffix}.pdf"'
        return resp


@login_required
def prep_notifications_api(request):
    """Returns unread count and latest notifications for the current student."""
    from django.utils.timesince import timesince

    notifs = PrepNotification.objects.filter(user=request.user).order_by("-created_at")[:15]
    unread_count = PrepNotification.objects.filter(user=request.user, is_read=False).count()

    data = []
    for n in notifs:
        time_str = timesince(n.created_at) + " ago"
        data.append({
            "id": str(n.id),
            "title": n.title,
            "message": n.message,
            "category": n.category,
            "is_read": n.is_read,
            "time_ago": time_str,
            "url": n.url or "",
        })

    return JsonResponse({
        "unread_count": unread_count,
        "notifications": data,
    })


@login_required
def prep_mark_notification_read_api(request):
    """Marks one or all notifications as read."""
    if request.method == "POST":
        notif_id = request.POST.get("notification_id")
        if notif_id == "all":
            PrepNotification.objects.filter(user=request.user, is_read=False).update(is_read=True)
            return JsonResponse({"success": True, "marked": "all"})
        elif notif_id:
            PrepNotification.objects.filter(user=request.user, id=notif_id).update(is_read=True)
            return JsonResponse({"success": True, "marked": notif_id})
    return JsonResponse({"error": "Invalid request"}, status=400)


@login_required
def prep_terms(request):
    """Mentify Prep Terms of Service."""
    wallet = PrepWallet.get_or_create_wallet(request.user)
    context = {
        "active_tab": "terms",
        "user_credits": wallet.credits_balance,
    }
    return render(request, "prep/terms.html", context)


@login_required
def prep_privacy(request):
    """Mentify Prep Privacy Policy."""
    wallet = PrepWallet.get_or_create_wallet(request.user)
    context = {
        "active_tab": "privacy",
        "user_credits": wallet.credits_balance,
    }
    return render(request, "prep/privacy.html", context)


@require_POST
def prep_assistant_chat_api(request):
    """
    POST /prep/api/assistant/chat/
    Body: JSON { "message": "user text", "history": [ { "role": "user"|"model", "text": "..." } ] }
    Returns: JSON { "status": "success", "response": "AI response text" }
    """
    import json
    from services.prep_chatbot_service import generate_prep_chat_response

    try:
        data = json.loads(request.body.decode("utf-8")) if request.body else request.POST
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"status": "error", "error": "Invalid JSON format."}, status=400)

    user_message = data.get("message", "").strip()
    if not user_message:
        return JsonResponse({"status": "error", "error": "Message cannot be empty."}, status=400)

    history = data.get("history", [])
    if not isinstance(history, list):
        history = []

    # Session history fallback
    session_history = request.session.get("prep_chat_history", [])
    if not history and session_history:
        history = session_history

    # Generate response using Prep grounding context & Gemini model
    user = request.user if request.user.is_authenticated else None
    ai_response = generate_prep_chat_response(messages_history=history, user_message=user_message, user=user)

    # Save last 10 turns to session
    updated_history = history + [
        {"role": "user", "text": user_message},
        {"role": "model", "text": ai_response},
    ]
    request.session["prep_chat_history"] = updated_history[-10:]

    return JsonResponse({"status": "success", "response": ai_response})
