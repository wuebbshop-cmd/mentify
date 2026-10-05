import os
import re
import logging
from functools import wraps
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_http_methods
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
    PrepTopicChatSession,
    PrepContentCache,
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

logger = logging.getLogger(__name__)


def _json_api_error_boundary(view_func):
    """Keep unexpected API failures observable in logs and JSON-shaped for clients."""
    @wraps(view_func)
    def wrapped(request, *args, **kwargs):
        try:
            return view_func(request, *args, **kwargs)
        except Exception:
            logger.exception("Unhandled error in JSON API endpoint %s", view_func.__name__)
            return JsonResponse(
                {
                    "success": False,
                    "error": "Topic notes could not be loaded because of a server error. Please retry.",
                },
                status=500,
            )

    return wrapped


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


def _catalog_search_key(value: str) -> str:
    """Make course-code search insensitive to spaces, hyphens, and casing."""
    return re.sub(r"[^a-z0-9]+", "", (value or "").casefold())


def _find_catalog_courses(query: str, *, limit: int = 12, include_category: bool = False):
    """Search the shared catalogue by normalized code, title, and optional category."""
    query_key = _catalog_search_key(query)
    if not query_key:
        return []
    courses = list(
        PrepCourse.objects.filter(is_active=True).annotate(
            topics_count=Count("topics", filter=Q(topics__is_active=True), distinct=True),
            papers_count=Count("papers", distinct=True),
        )
    )

    def matches(course):
        searchable = f"{course.code} {course.title}"
        if include_category:
            searchable += f" {course.category}"
        return query_key in _catalog_search_key(searchable)

    matching_courses = [course for course in courses if matches(course)]
    matching_courses.sort(key=lambda course: (
        _catalog_search_key(course.code) != query_key,
        not _catalog_search_key(course.code).startswith(query_key),
        course.code,
    ))
    return matching_courses[:limit]


def _public_topic_notes(topic):
    """Return the newest complete shared Level 2 notes without generating content."""
    from services.prep_ai_router import _cache_payload_as_dict, get_published_topic_note_levels

    published_levels = get_published_topic_note_levels(topic, validated_only=False)
    content = published_levels.get("level_2", "")
    if content:
        entries = PrepContentCache.objects.filter(
            topic=topic,
            content_type="topic_notes",
        ).order_by("-updated_at", "-id")
        for entry in entries:
            payload = _cache_payload_as_dict(entry.payload)
            if payload and payload.get("level") == "level_2" and payload.get("content") == content:
                return content, entry.updated_at
        return content, None
    return "", None


def _public_topic_questions(topic):
    """Return shared verified questions using the same course-safe matching as study pages."""
    from services.prep_ingestion import learner_visible_assessment_questions

    topic_match = (
        Q(topic=topic)
        | (
            Q(topic__isnull=True)
            & Q(paper__course=topic.course)
            & Q(topic_label__icontains=topic.title)
        )
    )
    records = (
        PrepQuestion.objects.filter(
            topic_match,
            verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
        )
        .filter(Q(paper__isnull=True) | Q(paper__is_published=True))
        .select_related("paper")
        .order_by("question_type", "paper__created_at", "number", "id")
    )
    return learner_visible_assessment_questions(records)


def prep_public_library(request):
    """Public catalogue for search visitors and crawlers, branded as Mentify."""
    courses = (
        PrepCourse.objects.filter(is_active=True)
        .annotate(
            topic_count=Count("topics", filter=Q(topics__is_active=True), distinct=True),
            paper_count=Count("papers", filter=Q(papers__is_published=True), distinct=True),
        )
        .order_by("category", "code")
    )
    return render(request, "prep/public_library.html", {"courses": courses})


def prep_public_course(request, course_slug):
    """Public, canonical course syllabus page with internal links to each topic."""
    course = get_object_or_404(PrepCourse, slug=course_slug, is_active=True)
    topics = list(course.topics.filter(is_active=True).order_by("order", "id"))
    for topic in topics:
        topic.question_count = len(_public_topic_questions(topic))

    return render(
        request,
        "prep/public_course.html",
        {
            "course": course,
            "topics": topics,
            "published_papers": course.papers.filter(is_published=True).order_by("-created_at"),
        },
    )


def prep_public_topic(request, course_slug, topic_id, topic_slug):
    """Public topic resource containing only validated notes and verified shared Q&A."""
    course = get_object_or_404(PrepCourse, slug=course_slug, is_active=True)
    topic = get_object_or_404(PrepTopic, pk=topic_id, course=course, is_active=True)
    if topic.slug != topic_slug:
        return redirect(
            "prep:public_topic",
            course_slug=course.slug,
            topic_id=topic.id,
            topic_slug=topic.slug,
            permanent=True,
        )

    notes, notes_updated_at = _public_topic_notes(topic)
    questions = _public_topic_questions(topic)
    return render(
        request,
        "prep/public_topic.html",
        {
            "course": course,
            "topic": topic,
            "notes": notes,
            "notes_updated_at": notes_updated_at,
            "questions": questions,
            "is_indexable": bool(notes or questions),
        },
    )


def prep_dashboard(request):
    """Mentify Prep Hub Main Landing Page with real database metrics."""
    courses_qs = PrepCourse.objects.filter(is_active=True).annotate(
        topics_count=Count("topics", filter=Q(topics__is_active=True), distinct=True),
        papers_count=Count("papers", distinct=True),
    )

    if request.user.is_authenticated:
        wallet = PrepWallet.get_or_create_wallet(request.user)
        user_credits = get_available_credits(wallet)
        recent_credit_transactions = wallet.transactions.all()[:10]
        enrolled_courses = PrepCourse.objects.filter(
            enrollments__user=request.user,
        ).annotate(
            topics_count=Count("topics", filter=Q(topics__is_active=True), distinct=True),
            papers_count=Count("papers", distinct=True),
        ).order_by("-enrollments__created_at")
        history_qs = PrepHistory.objects.filter(user=request.user).order_by("-created_at")[:5]
        display_courses = enrolled_courses
    else:
        wallet = None
        user_credits = 0
        recent_credit_transactions = []
        enrolled_courses = PrepCourse.objects.none()
        history_qs = PrepHistory.objects.none()
        # For public/crawler visitors, showcase active courses
        display_courses = courses_qs.order_by("-created_at")[:6]

    recent_courses = []
    for c in display_courses:
        clean_title = c.title
        if c.code and c.code in clean_title:
            clean_title = re.sub(r"^" + re.escape(c.code) + r"[\s:\-\–—]*", "", clean_title, flags=re.IGNORECASE).strip()
            if not clean_title:
                clean_title = c.title
        recent_courses.append({
            "id": c.id,
            "code": c.code,
            "slug": c.slug or c.code.replace(" ", "-"),
            "title": clean_title,
            "level": c.level,
            "topics_count": c.topics_count,
            "papers_count": c.papers_count,
        })

    # Recent activity from database
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
    from services.prep_ingestion import learner_visible_assessment_questions

    total_questions = len(learner_visible_assessment_questions(
        PrepQuestion.objects.filter(
            verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES
        )
    ))

    featured_topics = []
    for t in PrepTopic.objects.select_related("course")[:4]:
        from services.prep_ingestion import learner_visible_assessment_questions

        auth_cnt = len(learner_visible_assessment_questions(PrepQuestion.objects.filter(
            Q(topic=t) | Q(topic_label__icontains=t.title),
            question_type__in=["authentic", "adapted"],
            verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
        )))
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

    context = {
        "active_tab": "dashboard",
        "user_credits": user_credits,
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
    user_credits = get_available_credits(wallet)
    query = request.GET.get("q", "").strip()
    enrolled_course_ids = set(
        PrepCourseEnrollment.objects.filter(user=request.user).values_list("course_id", flat=True)
    )

    personal_courses_qs = PrepCourse.objects.filter(
        id__in=enrolled_course_ids,
        is_active=True,
    ).annotate(
        topics_count=Count("topics", filter=Q(topics__is_active=True), distinct=True),
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
            "id": c.id,
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
        matches = _find_catalog_courses(query)
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
        "user_credits": user_credits,
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
def prep_remove_course(request, course_id):
    """Remove a shared course from this user's dashboard only."""
    if request.method != "POST":
        return redirect("prep:dashboard")

    enrollment = PrepCourseEnrollment.objects.filter(
        user=request.user,
        course_id=course_id,
    ).first()
    if enrollment:
        code = enrollment.course.code
        enrollment.delete()
        messages.success(request, f"{code} was removed from your courses.")
    else:
        course = PrepCourse.objects.filter(id=course_id).first()
        code = course.code if course else "Course"
        messages.info(request, f"{code} is not currently in your courses.")

    next_url = request.POST.get("next")
    if next_url == "prep:courses":
        return redirect("prep:courses")
    elif next_url == "prep:dashboard":
        return redirect("prep:dashboard")
    elif next_url and next_url.startswith("/"):
        return redirect(next_url)
    referer = request.META.get("HTTP_REFERER")
    if referer:
        return redirect(referer)
    return redirect("prep:dashboard")


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
    from services.prep_ingestion import learner_visible_assessment_questions

    topics_qs = course.topics.filter(is_active=True).order_by("order")
    for t in topics_qs:
        auth_count = len(learner_visible_assessment_questions(PrepQuestion.objects.filter(
            Q(topic=t) | Q(topic_label__icontains=t.title),
            question_type__in=["authentic", "adapted"],
            verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
        )))
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
            "questions_count": len(learner_visible_assessment_questions(p.questions.filter(
                verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES
            ))),
        })

    pending_documents = []
    for d in course.documents.filter(stage__in=["stage_1", "stage_2"]).order_by("-created_at"):
        document_data = {
            "id": str(d.id),
            "filename": d.file.name.split("/")[-1] if d.file else "Document",
            "doc_type": d.doc_type,
            "stage": d.stage,
            "stage_display": d.get_stage_display(),
            "academic_year": d.academic_year,
            "topic_name": d.topic_name,
            "created_at": d.created_at.strftime("%b %d, %Y"),
        }
        if d.stage == "stage_2":
            pending_documents.append(document_data)
    pending_review_count = len(pending_documents)

    # Clean display title to avoid duplication
    display_title = course.title
    if course.code and course.code in display_title:
        display_title = re.sub(r"^" + re.escape(course.code) + r"[\s:\-\–—]*", "", display_title, flags=re.IGNORECASE).strip()
        if not display_title:
            display_title = course.title

    is_enrolled = PrepCourseEnrollment.objects.filter(user=request.user, course=course).exists()
    course_obj = {
        "id": course.id,
        "code": course.code,
        "title": display_title,
        "level": course.level,
        "is_enrolled": is_enrolled,
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
    2. Topic-scoped tutor grounded in validated notes and approved course material
    3. Authentic Past Examination Questions tagged to this syllabus topic
    4. Practice & Variant Generator (1 to 5 questions per run)
    """
    wallet = PrepWallet.get_or_create_wallet(request.user)
    from_tab = request.GET.get("from")
    active_subtab = request.GET.get("tab", "notes")
    if active_subtab not in {"notes", "assistant", "past_questions", "practice"}:
        active_subtab = "notes"

    topic = None
    if str(topic_id).isdigit():
        topic = PrepTopic.objects.filter(id=int(topic_id), is_active=True).select_related("course").first()

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
    from services.prep_ai_router import normalize_math_delimiters, validated_question_solution

    authentic_qs = []
    q_filter = (
        Q(topic=topic)
        | (
            Q(topic__isnull=True)
            & Q(paper__course=topic.course)
            & Q(topic_label__icontains=topic.title)
        )
    ) & Q(
        question_type__in=["authentic", "adapted"],
        verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
    )
    from services.prep_ingestion import learner_visible_assessment_questions

    authentic_records = learner_visible_assessment_questions(
        PrepQuestion.objects.filter(q_filter).select_related("paper").order_by("paper", "number", "id")
    )

    for q in authentic_records:
        paper_label = q.paper.title if q.paper else f"{course_code} Examination"
        year_label = q.paper.year if q.paper else "Official Examination"
        clean_q = normalize_math_delimiters(q.question_latex) if q.question_latex else ""
        clean_sol = validated_question_solution(q)
        has_formatting_errors = (
            bool(re.search(r"[\uf000-\uffff]||||||||||", q.question_latex or ""))
            or (q.question_latex and len(q.question_latex.strip()) < 15)
        )
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
            "is_flagged": False,
            "has_formatting_errors": has_formatting_errors,
            "is_adapted": q.question_type == "adapted",
        })

    # 2. Existing Practice Variants in DB
    generated_qs = []
    from services.prep_ingestion import learner_visible_assessment_questions

    gen_records = learner_visible_assessment_questions(
        PrepQuestion.objects.filter(
            topic=topic,
            question_type="generated",
            verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
        ).order_by("number", "id")
    )[:10]
    for q in gen_records:
        clean_g_q = normalize_math_delimiters(q.question_latex) if q.question_latex else ""
        clean_g_sol = validated_question_solution(q)
        generated_qs.append({
            "id": q.id,
            "number": q.number,
            "marks": q.marks,
            "topic_label": q.topic_label or topic_title,
            "question_latex": clean_g_q,
            "solution_latex": clean_g_sol,
            "is_cached": True,
        })

    # 3. Preload every already-published level. This is a read-only database
    # lookup, so opening a topic and switching levels never triggers AI work,
    # repeat validation, or a synthesis screen for shared verified notes.
    from services.prep_ai_router import get_published_topic_note_levels
    published_notes_by_level = get_published_topic_note_levels(topic)
    from services.prep_topic_tutor import list_topic_conversations
    assistant_conversations = list_topic_conversations(request.user, topic)
    initial_notes = published_notes_by_level.get("level_2", "")
    initial_notes_error = ""
    if not initial_notes:
        initial_notes_error = "No validated Level 2 notes are available for this topic yet."

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
        "is_enrolled": PrepCourseEnrollment.objects.filter(user=request.user, course=topic.course).exists(),
        "user_credits": wallet.credits_balance,
        "topic": topic_dict,
        "initial_notes": initial_notes,
        "published_notes_by_level": published_notes_by_level,
        "initial_notes_error": initial_notes_error,
        "initial_notes_stale": False,
        "authentic_questions": authentic_qs,
        "generated_questions": generated_qs,
        "assistant_conversations": assistant_conversations,
    }
    return render(request, "prep/topic_study.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def prep_topic_tutor_api(request, topic_id):
    """Load or send a private topic conversation and optional bounded study uploads."""
    topic = get_object_or_404(PrepTopic, pk=topic_id, is_active=True)
    if not (
        request.user.is_staff
        or request.user.is_superuser
        or PrepCourseEnrollment.objects.filter(user=request.user, course=topic.course).exists()
    ):
        return JsonResponse(
            {"success": False, "error": "Add this course to your study list before opening its topic tutor."},
            status=403,
        )

    from services.prep_topic_tutor import (
        MAX_MESSAGE_CHARS,
        TopicTutorError,
        list_topic_conversations,
        send_topic_message,
        serialize_topic_conversation,
    )

    if request.method == "GET":
        session_id = request.GET.get("session_id", "").strip()
        conversations = list_topic_conversations(request.user, topic)
        current = None
        if session_id:
            try:
                current = topic.chat_sessions.get(pk=int(session_id), user=request.user)
            except (ValueError, PrepTopicChatSession.DoesNotExist):
                return JsonResponse(
                    {"success": False, "error": "That conversation was not found for this topic."},
                    status=404,
                )
        wallet = PrepWallet.get_or_create_wallet(request.user)
        return JsonResponse({
            "success": True,
            "conversations": conversations,
            "conversation": serialize_topic_conversation(current) if current else None,
            "credits_balance": get_available_credits(wallet),
        })

    session = None
    session_id = request.POST.get("session_id", "").strip()
    if session_id:
        try:
            session = topic.chat_sessions.get(pk=int(session_id), user=request.user)
        except (ValueError, PrepTopicChatSession.DoesNotExist):
            return JsonResponse(
                {"success": False, "error": "That conversation was not found for this topic."},
                status=404,
            )

    message_text = request.POST.get("message", "").strip()
    if not message_text:
        return JsonResponse({"success": False, "error": "Enter a question about this topic."}, status=400)
    if len(message_text) > MAX_MESSAGE_CHARS:
        return JsonResponse(
            {"success": False, "error": f"Keep each message under {MAX_MESSAGE_CHARS} characters."},
            status=400,
        )

    from services.prep_course_billing import ensure_note_access
    allowed, available_credits = ensure_note_access(request.user, topic, "level_2")
    if not allowed:
        return JsonResponse(
            {
                "success": False,
                "error": (
                    "Your course materials are not covered by the current credit balance. "
                    "Top up to unlock this topic's notes and tutor."
                ),
                "credits_balance": available_credits,
            },
            status=402,
        )

    try:
        result = send_topic_message(
            user=request.user,
            topic=topic,
            session=session,
            user_message=request.POST.get("message", ""),
            uploaded_files=request.FILES.getlist("files"),
        )
    except TopicTutorError as exc:
        wallet = PrepWallet.get_or_create_wallet(request.user)
        return JsonResponse(
            {
                "success": False,
                "error": str(exc),
                "credits_balance": get_available_credits(wallet),
                "credits_charged": exc.credits_charged,
            },
            status=exc.status,
        )
    except Exception:
        logger.exception("Topic tutor request failed for topic %s and user %s", topic.pk, request.user.pk)
        return JsonResponse(
            {"success": False, "error": "The topic tutor could not complete this request. Please try again."},
            status=500,
        )

    wallet = PrepWallet.get_or_create_wallet(request.user)
    result_session = result.get("session")
    result["conversation"] = (
        serialize_topic_conversation(result_session) if result_session else None
    )
    result["conversations"] = list_topic_conversations(request.user, topic)
    return JsonResponse({
        "success": True,
        "answer": result["answer"],
        "session_id": result_session.pk if result_session else None,
        "conversation": result["conversation"],
        "conversations": result["conversations"],
        "credits_charged": result["credits_charged"],
        "ocr_credits": result.get("ocr_credits", 0),
        "credits_balance": get_available_credits(wallet),
        "uploads": result.get("uploads", []),
    })


@login_required
def prep_past_papers(request):
    """Legacy past papers route; redirect to courses catalogue."""
    return redirect("prep:courses")


@login_required
def prep_paper_detail(request, course_code, paper_id):
    """View questions of a specific CAT / Examination paper from DB."""
    clean_course = course_code.replace("-", " ").upper()
    wallet = PrepWallet.get_or_create_wallet(request.user)
    from services.prep_ai_router import validated_question_solution

    paper = PrepPaper.objects.filter(id=paper_id).prefetch_related("questions").first()

    if paper:
        questions_list = []
        from services.prep_ingestion import learner_visible_assessment_questions

        for q in learner_visible_assessment_questions(
            paper.questions.filter(
                verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES
            ).order_by("number", "id")
        ):
            questions_list.append({
                "number": q.number,
                "marks": q.marks,
                "topic": q.topic_label or "Mathematical Assessment",
                "question_latex": q.question_latex,
                "solution_latex": validated_question_solution(q),
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


def prep_upload(request):
    """Upload one document group to an existing course or create a new course."""
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.info(request, "Please sign in or create a free account to upload study materials.")
            return redirect(f"/accounts/login/?next={request.path}")

        course_id = request.POST.get("course_id", "").strip()
        course_name = request.POST.get("course_name", "").strip()
        doc_type = request.POST.get("doc_type", "Lecture Notes")
        academic_year = request.POST.get("academic_year", "").strip()
        topic_name = request.POST.get("topic_name", "").strip()
        uploaded_files = request.FILES.getlist("files") or request.FILES.getlist("file")

        if not uploaded_files:
            messages.error(request, "Please attach at least one document file to upload.")
            return redirect("prep:upload")

        if len(uploaded_files) > 10:
            messages.error(request, "Upload up to 10 documents in one batch.")
            return redirect("prep:upload")

        valid_extensions = (".pdf", ".docx", ".doc", ".md", ".txt")
        max_bytes = 15 * 1024 * 1024
        invalid_file = next(
            (
                uploaded_file
                for uploaded_file in uploaded_files
                if os.path.splitext(uploaded_file.name.lower())[1] not in valid_extensions
                or uploaded_file.size > max_bytes
            ),
            None,
        )
        if invalid_file:
            file_ext = os.path.splitext(invalid_file.name.lower())[1]
            if file_ext not in valid_extensions:
                messages.error(
                    request,
                    f"'{invalid_file.name}' has an unsupported format. Use PDF, Word, Markdown, or text files.",
                )
            else:
                messages.error(request, f"'{invalid_file.name}' exceeds the 15 MB per-file limit.")
            return redirect("prep:upload")

        valid_doc_types = dict(PrepDocument.DOC_TYPES)
        if doc_type not in valid_doc_types:
            messages.error(request, "Choose a valid document type.")
            return redirect("prep:upload")

        if course_id:
            try:
                course = PrepCourse.objects.get(pk=int(course_id), is_active=True)
            except (ValueError, PrepCourse.DoesNotExist):
                messages.error(request, "Choose an active course from the list or select a new course.")
                return redirect("prep:upload")
        else:
            if not course_name:
                messages.error(request, "Choose an existing course or enter a course code and title.")
                return redirect("prep:upload")
            course_code, course_title = parse_course_code_and_title(course_name)
            course = PrepCourse.objects.filter(code__iexact=course_code).first()
            if not course:
                course = PrepCourse.objects.create(
                    code=course_code,
                    title=course_title,
                    level="Undergraduate",
                    category="Other",
                )

        PrepCourseEnrollment.objects.get_or_create(
            user=request.user,
            course=course,
            defaults={"source": "upload"},
        )

        from services.prep_ingestion import process_prep_document
        succeeded = 0
        duplicates = 0
        failures = []
        for uploaded_file in uploaded_files:
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

            try:
                result = process_prep_document(prep_doc)
                if not result.get("success"):
                    failure = result.get("error", "The document could not be processed.")
                    failures.append(f"{uploaded_file.name}: {failure}")
                    prep_doc.tutor_review_notes = f"Ingestion failed before review. {failure[:900]}"
                    prep_doc.save(update_fields=["tutor_review_notes", "updated_at"])
                    continue
                if result.get("duplicate"):
                    duplicates += 1
                else:
                    succeeded += 1

                course_slug = course.slug or course.code.replace(" ", "-")
                PrepHistory.objects.create(
                    user=request.user,
                    title=f"Uploaded {uploaded_file.name}",
                    course_code=course.code,
                    item_type=doc_type,
                    url=reverse("prep:course_detail", kwargs={"course_code": course_slug}),
                )
            except Exception as exc:
                failures.append(f"{uploaded_file.name}: ingestion failed")
                prep_doc.tutor_review_notes = f"Ingestion failed before review: {str(exc)[:1000]}"
                prep_doc.save(update_fields=["tutor_review_notes", "updated_at"])

        if succeeded:
            messages.success(request, f"Processed {succeeded} document(s) for {course.code}; they are in the tutor review queue.")
        if duplicates:
            messages.info(request, f"{duplicates} duplicate document(s) were saved for audit and not re-indexed.")
        if failures:
            messages.error(request, f"{len(failures)} document(s) need attention: " + "; ".join(failures)[:800])

        return redirect(f"{reverse('prep:upload')}?course_id={course.pk}")

    # Recent uploads for this user (if authenticated)
    recent_uploads = []
    user_credits = 30
    if request.user.is_authenticated:
        wallet = PrepWallet.get_or_create_wallet(request.user)
        user_credits = wallet.credits_balance
        user_docs = PrepDocument.objects.filter(user=request.user).order_by("-created_at")[:5]
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
    selected_course_id = request.GET.get("course_id", "").strip()
    courses = PrepCourse.objects.filter(is_active=True).order_by("code")
    if not selected_course_id.isdigit() or not courses.filter(pk=selected_course_id).exists():
        selected_course_id = ""
    context = {
        "active_tab": "upload",
        "user_credits": user_credits,
        "recent_uploads": recent_uploads,
        "upload_courses": courses,
        "selected_course_id": selected_course_id,
    }
    return render(request, "prep/upload.html", context)


@login_required
def prep_history(request):
    """Legacy revision history route; redirect to dashboard."""
    return redirect("prep:dashboard")


def prep_billing(request):
    """Credit Balance & M-Pesa Top-Up Page connected to PrepWallet."""
    if request.user.is_authenticated:
        wallet = PrepWallet.get_or_create_wallet(request.user)
        user_credits = wallet.credits_balance
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
        is_trial = wallet.current_plan == "trial"
        can_top_up = has_active_subscription(wallet)
        plan_expires_at = wallet.plan_expires_at
        recent_transactions = wallet.transactions.all()[:10]
        current_plan_code = wallet.current_plan
    else:
        wallet = None
        user_credits = 30
        plan_display = "Free 30-Credit Trial (Sign Up Free)"
        is_trial = False
        can_top_up = False
        plan_expires_at = None
        recent_transactions = []
        current_plan_code = None

    context = {
        "active_tab": "billing",
        "wallet": wallet,
        "user_credits": user_credits,
        "current_plan": plan_display,
        "is_trial": is_trial,
        "can_top_up": can_top_up,
        "plan_expires_at": plan_expires_at,
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
                "active": current_plan_code == "basic",
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
                "active": current_plan_code == "plus",
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
                "active": current_plan_code == "pro",
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
    generate_adapted_past_question,
    _nontechnical_solution_has_proof_scaffold,
    _question_solution_uses_nontechnical_format,
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
                if q_obj.verification_status not in PrepQuestion.ANSWERABLE_STATUSES:
                    return JsonResponse({
                        "success": False,
                        "error": "This question is pending tutor review and cannot be answered yet.",
                        "verification_status": q_obj.verification_status,
                    }, status=409)
                from services.prep_ingestion import assessment_question_rendering_issues

                question_issues = assessment_question_rendering_issues(q_obj.question_latex)
                if question_issues:
                    return JsonResponse({
                        "success": False,
                        "error": "This question did not pass the current formatting and extraction checks.",
                        "validation_issues": question_issues,
                    }, status=409)
                question_latex = q_obj.question_latex
                course_code = q_obj.paper.course.code if q_obj.paper else (q_obj.topic.course.code if q_obj.topic else course_code)
                topic_label = q_obj.topic_label or (q_obj.topic.title if q_obj.topic else topic_label)
                # If already solved in DB, return at 0 credits
                stored_solution = validated_question_solution(q_obj)
                if stored_solution:
                    return JsonResponse({
                        "success": True,
                        "solution": stored_solution,
                        "cached": True,
                        "credits_deducted": 0,
                        "model": "Database Validated Cache ($0)",
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
def prep_adapt_question_api(request):
    """Create a credit-paid, validated equivalent for an unreadable source question."""
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "POST method required."}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8")) if request.body else request.POST
    except Exception:
        data = request.POST

    try:
        question_id = int(data.get("question_id"))
    except (TypeError, ValueError):
        return JsonResponse({"success": False, "error": "A valid question is required."}, status=400)

    question = PrepQuestion.objects.select_related("paper__course", "topic__course").filter(
        id=question_id,
        question_type__in=["authentic", "adapted"],
    ).first()
    if not question:
        return JsonResponse({"success": False, "error": "This question was not found."}, status=404)

    target_topic = question.topic
    topic_id_param = data.get("topic_id")
    if not target_topic and topic_id_param and str(topic_id_param).isdigit():
        target_topic = PrepTopic.objects.filter(id=int(topic_id_param), is_active=True).first()
    if not target_topic and question.paper:
        target_topic = PrepTopic.objects.filter(
            course=question.paper.course,
            title__icontains=question.topic_label
        ).first()

    adapted_label = f"Adapted from Question {question.number}"
    from services.prep_ai_router import validated_question_solution

    existing = PrepQuestion.objects.filter(
        paper=question.paper,
        topic=target_topic or question.topic,
        question_type="adapted",
        topic_label=adapted_label,
        reconstructed_from=question,
        verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
    ).first()
    wallet = PrepWallet.get_or_create_wallet(request.user)
    if existing:
        from services.prep_ingestion import assessment_question_rendering_issues

        existing_issues = assessment_question_rendering_issues(existing.question_latex)
        if existing_issues:
            return JsonResponse({
                "success": False,
                "error": "The saved adapted question did not pass the current formatting and extraction checks.",
                "validation_issues": existing_issues,
            }, status=409)
        return JsonResponse({
            "success": True,
            "cached": True,
            "question_id": existing.id,
            "question_latex": existing.question_latex,
            "solution_latex": validated_question_solution(existing),
            "marks": existing.marks,
            "topic_label": existing.topic_label or "",
            "credits_deducted": 0,
            "credits_balance": wallet.credits_balance,
        })

    try:
        enforce_subscription_limit(wallet, "practice_questions", 1)
    except PlanLimitExceeded as exc:
        return JsonResponse({"success": False, "error": str(exc)}, status=403)

    minimum_cost = 5
    required_balance = estimated_generation_credits(minimum=minimum_cost)
    if get_available_credits(wallet) < required_balance:
        return JsonResponse({
            "success": False,
            "error": f"Insufficient credits. At least {required_balance} credits are required to reconstruct this question.",
            "credits_balance": wallet.credits_balance,
        }, status=402)

    result = generate_adapted_past_question(question)
    if not result.get("success"):
        return JsonResponse({"success": False, "error": result.get("error")}, status=422)

    item = result["question"]
    answer_candidate = PrepQuestion(
        paper=question.paper,
        topic=target_topic or question.topic,
        question_type="adapted",
        verification_status="reconstructed",
        topic_label=adapted_label,
        question_latex=item["question_latex"],
        solution_latex=item["solution_latex"],
    )
    validated_answer = validated_question_solution(answer_candidate)
    if not validated_answer:
        return JsonResponse({
            "success": False,
            "error": "The adapted solution failed current course/topic answer validation and was not saved.",
        }, status=422)
    item["solution_latex"] = validated_answer
    try:
        credits_deducted = credits_for_usage(result.get("usage"), minimum=minimum_cost)
        course_name = question.paper.course.code if question.paper else (question.topic.course.code if question.topic else "Course")
        t_label = question.topic_label or (target_topic.title if target_topic else (question.topic.title if question.topic else "Mathematics"))
        consume_credits(
            wallet,
            credits_deducted,
            action_type="ai_practice_gen",
            description=f"Adapted Past Question: {course_name} - {t_label}",
            usage=result.get("usage"),
            model_name=result.get("model", "deepseek-reasoner"),
            metadata={"source_question_id": question.id, "adapted": True},
        )
    except InsufficientCredits:
        return JsonResponse({
            "success": False,
            "error": "The adapted question requires more credits than are currently available.",
            "credits_balance": get_available_credits(wallet),
        }, status=402)

    reconstruction_metadata = result.get("reconstruction_metadata")
    reconstruction_metadata = reconstruction_metadata if isinstance(reconstruction_metadata, dict) else {}
    model_confidence = reconstruction_metadata.get("model_confidence")
    auto_validated = (
        isinstance(model_confidence, (int, float))
        and not isinstance(model_confidence, bool)
        and 0.8 <= model_confidence <= 1
    )
    reconstruction_metadata.update({
        "review_status": "auto_validated" if auto_validated else "pending",
        "auto_validation_threshold": 0.8,
    })
    adapted = PrepQuestion.objects.create(
        paper=question.paper,
        topic=target_topic or question.topic,
        source_document=question.source_document or (question.paper.source_document if question.paper_id else None),
        source_page_number=question.source_page_number,
        extraction_confidence=question.extraction_confidence,
        reconstructed_from=question,
        question_type="adapted",
        number=question.number,
        marks=int(item.get("marks") or question.marks),
        topic_label=adapted_label,
        question_latex=item["question_latex"],
        solution_latex=item["solution_latex"],
        verification_status="reconstructed" if auto_validated else "pending",
        reconstruction_metadata=reconstruction_metadata,
    )
    wallet.refresh_from_db()
    return JsonResponse({
        "success": True,
        "cached": False,
        "question_id": adapted.id,
        "question_latex": adapted.question_latex,
        "solution_latex": validated_question_solution(adapted),
        "marks": adapted.marks,
        "topic_label": adapted.topic_label or "",
        "credits_deducted": credits_deducted,
        "credits_balance": wallet.credits_balance,
    })


@login_required
@_json_api_error_boundary
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
    level = str(data.get("level", "level_2") or "level_2").strip().lower()
    if level not in {"level_1", "level_2", "level_3"}:
        level = "level_2"

    wallet = PrepWallet.get_or_create_wallet(request.user)
    balance_before_notes = get_available_credits(wallet)
    credits_deducted = 0

    topic_obj = None
    if topic_id and str(topic_id).isdigit():
        topic_obj = PrepTopic.objects.filter(id=int(topic_id), is_active=True).first()
        if topic_obj:
            topic_title = topic_obj.title
            course_code = topic_obj.course.code

    if not topic_title:
        return JsonResponse({"success": False, "error": "Topic title is required."}, status=400)

    subtopics = topic_obj.subtopics if (topic_obj and isinstance(topic_obj.subtopics, list)) else []

    from services.prep_course_billing import ensure_note_access
    if topic_obj:
        allowed, available_credits = ensure_note_access(request.user, topic_obj, level)
        credits_deducted = max(0, balance_before_notes - available_credits)
        if not allowed:
            return JsonResponse({
                "success": False,
                "error": "Your course share for this topic is not covered by your current credits. Top up to unlock this and later topics.",
                "level": level,
                "credits_balance": available_credits,
                "credits_deducted": credits_deducted,
            }, status=402)

    # Use the same published-level source that rendered the notes on the page.
    # Shared notes are returned only after this learner's course share is settled.
    from services.prep_ai_router import get_published_topic_note_levels
    published_notes = get_published_topic_note_levels(topic_obj, validated_only=True) if topic_obj else {}
    if level in published_notes:
        wallet.refresh_from_db()
        return JsonResponse({
            "success": True,
            "notes": published_notes[level],
            "level": level,
            "cached": True,
            "credits_deducted": credits_deducted,
            "credits_balance": wallet.credits_balance,
            "model": "Published Shared Notes",
        })

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

    if cached_res.get("needs_review"):
        wallet.refresh_from_db()
        return JsonResponse({
            "success": False,
            "needs_review": True,
            "error": cached_res.get("error") or "These notes are awaiting tutor review.",
            "level": level,
            "credits_deducted": 0,
            "credits_balance": wallet.credits_balance,
        }, status=409)

    if cached_res.get("notes") or cached_res.get("content"):
        res = cached_res
    else:
        required_balance = estimated_generation_credits(minimum=1)
        trial_exempt = False
        if topic_obj:
            from services.prep_course_billing import is_trial_exempt_for_course_cost

            trial_exempt = is_trial_exempt_for_course_cost(wallet, "topic_notes", level)
        if (
            not cached_res.get("regenerated_from_invalid_cache")
            and not trial_exempt
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

    if res.get("needs_review"):
        wallet.refresh_from_db()
        return JsonResponse({
            "success": False,
            "needs_review": True,
            "error": res.get("error") or "These notes are awaiting tutor review.",
            "level": level,
            "credits_deducted": 0,
            "credits_balance": wallet.credits_balance,
        }, status=409)

    if res.get("error") and not res.get("notes"):
        # The provider may return structurally invalid notes. That is an
        # expected validation rejection, not an application/server failure.
        status = 422 if res.get("validation_failed") else 502
        return JsonResponse({"success": False, "error": res["error"]}, status=status)

    cost = None
    if topic_obj and not res.get("cached"):
        from services.prep_course_billing import create_shared_course_cost, settle_course_cost_share
        from services.prep_ai_router import _topic_notes_cache_signature

        usage = res.get("usage") or {}
        cost = create_shared_course_cost(
            course=topic_obj.course,
            cost_type="topic_notes",
            total_credits=credits_for_usage(usage, minimum=1),
            source_key=(
                f"topic-notes:{topic_obj.pk}:{level}:"
                f"{_topic_notes_cache_signature(topic_obj.course, topic_obj, topic_title, subtopics)}"
            ),
            topic=topic_obj,
            level=level,
            usage=usage,
            model_name=res.get("model", "deepseek-chat"),
        )
        current_share = cost.shares.filter(user=request.user).first()
        paid_before = current_share.paid_credits if current_share else 0
        for share in cost.shares.select_related("user", "cost").all():
            settle_course_cost_share(share)
        if current_share:
            current_share.refresh_from_db(fields=["paid_credits"])
            credits_deducted += current_share.paid_credits - paid_before
    elif not topic_obj and not res.get("cached") and not res.get("regenerated_from_invalid_cache"):
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

    if topic_obj:
        balance_before_final_settlement = get_available_credits(wallet)
        allowed, available_credits = ensure_note_access(request.user, topic_obj, level)
        credits_deducted += max(0, balance_before_final_settlement - available_credits)
        if not allowed:
            return JsonResponse({
                "success": False,
                "error": "Your course share for this topic is not covered by your current credits. Top up to unlock this and later topics.",
                "level": level,
                "credits_balance": available_credits,
                "credits_deducted": credits_deducted,
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
        topic_obj = PrepTopic.objects.filter(id=int(topic_id), is_active=True).first()
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
        from services.prep_ingestion import learner_visible_assessment_questions

        auth_qs = learner_visible_assessment_questions(PrepQuestion.objects.filter(
            (
                Q(topic=topic_obj)
                | (
                    Q(topic__isnull=True)
                    & Q(paper__course=topic_obj.course)
                    & Q(topic_label__icontains=topic_title)
                )
            ) & Q(
                question_type__in=["authentic", "adapted"],
                verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
            ),
        ).order_by("paper", "number", "id"))[:3]
        for q in auth_qs:
            authentic_samples.append(f"Q{q.number} ({q.marks} marks): {q.question_latex}")

    # Check existing generated questions in DB
    if topic_obj:
        from services.prep_ingestion import learner_visible_assessment_questions

    existing_generated = (
        len(learner_visible_assessment_questions(PrepQuestion.objects.filter(
            topic=topic_obj,
            question_type="generated",
            verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
        )))
        if topic_obj
        else 0
    )
    # A verified shared set is reused exactly as it stands. Do not reserve
    # credits for a larger later selection, because that must not append paid
    # variants to an existing set.
    fresh_needed = 0 if existing_generated else count

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
        topic = PrepTopic.objects.filter(id=int(topic_id), is_active=True).first()

    course_code = topic.course.code if topic else "SMA 300"
    topic_title = topic.title if topic else "Metric Spaces & Topology"

    level = request.GET.get("level", "level_2").strip().lower()
    if level not in {"level_1", "level_2", "level_3"}:
        level = "level_2"

    section = request.GET.get("section", "notes").strip().lower()
    if section == "questions_answers":
        if not topic:
            return HttpResponse("The requested syllabus topic was not found.", status=404)
        from services.prep_ai_router import validated_question_solution

        topic_filter = (
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
        authentic_records = PrepQuestion.objects.filter(
            topic_filter,
            question_type__in=["authentic", "adapted"],
            verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
        ).select_related("paper").order_by("paper", "number", "id")
        generated_records = PrepQuestion.objects.filter(
            topic=topic,
            question_type="generated",
            verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
        ).order_by("number", "id")
        from services.prep_ingestion import learner_visible_assessment_questions

        authentic_records = learner_visible_assessment_questions(authentic_records)
        generated_records = learner_visible_assessment_questions(generated_records)

        questions_data = []
        for question in authentic_records:
            questions_data.append({
                "number": len(questions_data) + 1,
                "marks": question.marks,
                "topic": f"Authentic past question: {question.topic_label or topic_title}",
                "question_latex": question.question_latex,
                "solution_latex": validated_question_solution(question),
            })
        for question in generated_records:
            questions_data.append({
                "number": len(questions_data) + 1,
                "marks": question.marks,
                "topic": f"Generated practice question: {question.topic_label or topic_title}",
                "question_latex": question.question_latex,
                "solution_latex": validated_question_solution(question),
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

    # 1. Export the same published shared source shown on the study page.
    # This direct lookup avoids a second cache-key path producing a false
    # "No validated notes" response on a mobile download request.
    from services.prep_ai_router import (
        get_or_generate_topic_notes,
        get_published_topic_note_levels,
        validated_question_solution,
    )
    published_notes = get_published_topic_note_levels(topic, validated_only=True) if topic else {}
    notes_content = published_notes.get(level, "")
    notes_res = {"notes": notes_content}
    if not notes_content:
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
        err_msg = notes_res.get("error") or "Notes for this level are still being prepared. Please open the topic page first to load notes before exporting."
        messages.warning(request, err_msg)
        if topic:
            return redirect(reverse("prep:topic_study", kwargs={"topic_id": topic_id}) + f"?tab=notes&level={level}")
        return redirect("prep:dashboard")

    # 2. Fetch authentic questions mapped to this topic
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

    # 3. Fetch practice questions for this topic
    practice_qs = []
    if topic:
        for q in learner_visible_assessment_questions(PrepQuestion.objects.filter(
            topic=topic,
            question_type="generated",
            verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
        ).order_by("number", "id"))[:10]:
            practice_qs.append({
                "number": q.number,
                "marks": q.marks,
                "topic": q.topic_label or topic_title,
                "question_latex": q.question_latex,
                "solution_latex": validated_question_solution(q),
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
    from services.prep_ai_router import validated_question_solution

    paper = PrepPaper.objects.filter(id=paper_id).prefetch_related("questions").first()

    clean_course = course_code.replace("-", " ").upper()
    paper_title = paper.title if paper else "Continuous Assessment Test 1 (CAT 1)"
    year = paper.year if paper else "2024/2025 Academic Year"
    total_marks = paper.total_marks if paper else 30

    questions_data = []
    if paper and paper.questions.filter(
        verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES
    ).exists():
        from services.prep_ingestion import learner_visible_assessment_questions

        for q in learner_visible_assessment_questions(
            paper.questions.filter(
                verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES
            ).order_by("number", "id")
        ):
            questions_data.append({
                "number": q.number,
                "marks": q.marks,
                "topic": q.topic_label or "Mathematical Assessment",
                "question_latex": q.question_latex,
                "solution_latex": validated_question_solution(q),
            })
    elif paper:
        return HttpResponse(
            "This paper has no verified extractable questions yet.",
            status=404,
            content_type="text/plain; charset=utf-8",
        )
    else:
        return HttpResponse("The requested paper was not found.", status=404)

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


def prep_terms(request):
    """Mentify Prep Terms of Service."""
    credits = 30
    if request.user.is_authenticated:
        wallet = PrepWallet.get_or_create_wallet(request.user)
        credits = wallet.credits_balance
    context = {
        "active_tab": "terms",
        "user_credits": credits,
    }
    return render(request, "prep/terms.html", context)


def prep_privacy(request):
    """Mentify Prep Privacy Policy."""
    credits = 30
    if request.user.is_authenticated:
        wallet = PrepWallet.get_or_create_wallet(request.user)
        credits = wallet.credits_balance
    context = {
        "active_tab": "privacy",
        "user_credits": credits,
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
