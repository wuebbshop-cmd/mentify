import os
import re
import json
import datetime
import logging
from functools import wraps
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_http_methods
from django.core.cache import cache
from django.views.decorators.cache import never_cache
from django.utils.cache import patch_vary_headers
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.db.models import Count, Q
from django.utils import timezone
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
    PrepTopicNotesJob,
    PrepTransaction,
    PrepHistory,
    PrepNotification,
)
from services.credit_service import (
    InsufficientCredits,
    PlanLimitExceeded,
    UploadLimitExceeded,
    consume_credits,
    credits_for_usage,
    enforce_subscription_limit,
    enforce_upload_limit,
    estimated_generation_credits,
    get_available_credits,
    get_remaining_practice_question_allowance,
    get_remaining_scanned_allowance,
    get_remaining_upload_allowance,
    grant_purchased_topup,
    grant_subscription,
    has_active_subscription,
    record_upload,
)

logger = logging.getLogger(__name__)


def set_prep_cache_headers(response, *, max_age: int = 600, is_public: bool = False, is_authenticated: bool = False):
    """
    Apply appropriate HTTP Cache-Control headers to Mentify Prep responses.
    - Public/anonymous: Cache-Control: public, max-age={max_age}, stale-while-revalidate={max_age * 2}
    - Authenticated: Cache-Control: private, max-age={max(60, max_age // 2)}, stale-while-revalidate={max_age} + Vary: Cookie
    """
    if is_authenticated:
        response["Cache-Control"] = f"private, max-age={max(60, max_age // 2)}, stale-while-revalidate={max_age}"
        patch_vary_headers(response, ["Cookie"])
    elif is_public:
        response["Cache-Control"] = f"public, max-age={max_age}, stale-while-revalidate={max_age * 2}"
        patch_vary_headers(response, ["Accept-Encoding"])
    return response


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


def infer_course_category(code: str, title: str) -> str:
    """Infer standard PrepCourse.category from course code and title."""
    code_upper = str(code or "").strip().upper()
    title_lower = str(title or "").strip().lower()
    prefix = re.split(r"[\s\-_0-9]+", code_upper)[0] if code_upper else ""

    # 1. Computing / Computer Science
    if prefix in {"CIT", "CCS", "CSC", "ICS", "BIT", "SIT", "COM", "CSE"} or any(
        kw in title_lower for kw in ("computer", "computing", "programming", "software", "algorithm", "data structure", "database", "information technology")
    ):
        return "Computing"

    # 2. Statistics
    if prefix in {"SST", "STA", "ACT"} or any(
        kw in title_lower for kw in ("statistic", "estimation", "probability", "stochastic", "regression", "time series", "sampling", "actuarial")
    ):
        return "Statistics"

    # 3. Mathematics
    if prefix in {"SMA", "MAT", "MATH", "MTH", "CAL", "ALG", "GEO"} or any(
        kw in title_lower for kw in ("mathematic", "calculus", "geometry", "algebra", "trigonometry", "linear algebra", "discrete math", "differential equation", "real analysis")
    ):
        return "Mathematics"

    # 4. Business & Economics
    if prefix in {"EET", "ECO", "BBA", "BCOM", "FIN", "ACC", "BUS"} or any(
        kw in title_lower for kw in ("economic", "microeconomic", "macroeconomic", "finance", "accounting", "business", "commerce", "management")
    ):
        return "Business & Economics"

    # 5. Social Sciences
    if prefix in {"ASC", "SOC", "PSY", "ANT", "POL", "DEV"} or any(
        kw in title_lower for kw in ("sociology", "psychology", "anthropology", "political", "social", "society", "development studies")
    ):
        return "Social Sciences"

    # 6. Chemistry
    if prefix in {"SCH", "CHE", "BCH"} or any(
        kw in title_lower for kw in ("chemistry", "chemical", "organic", "inorganic", "biochemistry")
    ):
        return "Chemistry"

    # 7. Physics
    if prefix in {"SPH", "PHY"} or any(
        kw in title_lower for kw in ("physics", "mechanics", "electromagnetism", "quantum", "optics")
    ):
        return "Physics"

    # 8. Engineering
    if prefix in {"ENG", "ECE", "MCE", "CVE", "EEE", "MECH", "CIV"} or any(
        kw in title_lower for kw in ("engineering", "circuit", "structural")
    ):
        return "Engineering"

    # 9. Health & Sciences / General Sciences
    if prefix in {"SBT", "SZL", "MED", "NUR", "PHA", "HNS", "BIO"} or any(
        kw in title_lower for kw in ("health", "medical", "nursing", "clinical", "anatomy", "physiology", "pathology", "pharmacology", "biology", "genetics")
    ):
        return "General Sciences"

    # 10. Humanities
    if prefix in {"UCU", "AEN", "ALT", "AHI", "ARE", "APS", "PHI", "LIT", "HIS", "REL"} or any(
        kw in title_lower for kw in ("communication", "communication skills", "literature", "history", "philosophy", "linguistics", "ethics", "critical thinking", "writing")
    ):
        return "Humanities"

    return "Other"


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


def clean_topic_summary(summary: str, title: str = "", subtopics: list[str] | None = None) -> str:
    """
    Ensure topic descriptions strictly describe academic course content and subject matter,
    stripping institutional names, universities, schools, lecturers, degrees, or cover-page metadata.
    """
    text = (summary or "").strip()
    if text:
        # Strip institutional / school / university references
        text = re.sub(
            r"(?i)\b(?:offered\s+at|taught\s+at|examined\s+at|taken\s+at)\s+[^,.;]+(?:University|College|Institute|School|Campus|Faculty|Polytechnic)[^,.;]*",
            "",
            text,
        )
        text = re.sub(
            r"(?i)\b(?:at|in)\s+[A-Z][A-Za-z\s]+(?:University|College|Institute|School|Campus|Faculty|Polytechnic)\b[^,.;]*",
            "",
            text,
        )
        text = re.sub(
            r"(?i)\busing\s+[A-Z][A-Za-z\s]+(?:University|College|Institute|School)\s+as\s+an?\s+(?:illustrative\s+)?example\b[^,.;]*",
            "",
            text,
        )
        text = re.sub(r"(?i)\b(?:lecturer|instructor|professor|prof\.|dr\.)\s*:[^,.;]+", "", text)
        text = re.sub(r"(?i)\b(?:academic\s+year|semester|term|undergraduate|postgraduate|degree|diploma)\b[^,.;]*", "", text)
        # Strip leading "An introductory course in ...", "A course covering ..." if it was purely a course blurb
        text = re.sub(r"(?i)^an?\s+(?:introductory\s+)?course\s+(?:in|covering)\s+[^,.;]+[.,;]?\s*", "", text)
        text = re.sub(r"\s+", " ", text).strip(" ,.;:-")

    # If empty or too trivial, synthesize a crisp subject-matter summary based on title & subtopics
    if not text or len(text) < 15:
        clean_title = (title or "").strip()
        if subtopics and len(subtopics) > 0:
            joined_st = ", ".join(subtopics[:3])
            text = f"Covers core theoretical principles and analytical methods for {clean_title}, focusing on {joined_st}."
        elif clean_title:
            text = f"Foundational concepts, theoretical frameworks, and core analytical principles for {clean_title}."
        else:
            text = "Canonical syllabus topics, foundational definitions, and worked analytical examples."
    return text


def _catalog_search_key(value: str) -> str:
    """Make course-code search insensitive to spaces, hyphens, and casing."""
    return re.sub(r"[^a-z0-9]+", "", (value or "").casefold())


def _find_catalog_courses(query: str, *, limit: int = 12, include_category: bool = False):
    """Search the shared catalogue by normalized code, title, and optional category."""
    query_key = _catalog_search_key(query)
    if not query_key:
        return []
    courses = cache.get("prep_annotated_catalog_courses")
    if courses is None:
        courses = list(
            PrepCourse.objects.filter(is_active=True).annotate(
                topics_count=Count("topics", filter=Q(topics__is_active=True), distinct=True),
                papers_count=Count("papers", distinct=True),
            )
        )
        cache.set("prep_annotated_catalog_courses", courses, 900)

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
    cache_key = f"prep_pub_topic_notes_{topic.pk}"
    cached_val = cache.get(cache_key)
    if cached_val is not None:
        return cached_val

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
                val = (content, entry.updated_at)
                cache.set(cache_key, val, 900)
                return val
        val = (content, None)
        cache.set(cache_key, val, 900)
        return val
    val = ("", None)
    cache.set(cache_key, val, 900)
    return val


def _public_topic_questions(topic):
    """Return shared verified questions using the same course-safe matching as study pages."""
    cache_key = f"prep_pub_topic_questions_{topic.pk}"
    cached_val = cache.get(cache_key)
    if cached_val is not None:
        return cached_val

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
    res = learner_visible_assessment_questions(records)
    cache.set(cache_key, res, 900)
    return res


def prep_public_library(request):
    """Public catalogue for search visitors and crawlers, branded as Mentify."""
    cache_key = "prep_pub_lib_courses_v3"
    bundle = cache.get(cache_key)
    if bundle is None:
        raw_courses = list(
            PrepCourse.objects.filter(is_active=True)
            .annotate(
                topic_count=Count("topics", filter=Q(topics__is_active=True), distinct=True),
                paper_count=Count("papers", filter=Q(papers__is_published=True), distinct=True),
            )
            .order_by("category", "code")
        )

        courses_data = []
        categories_set = set()
        total_units = 0
        total_papers = 0

        for c in raw_courses:
            cat_meta = _resolve_course_category_meta(c)
            cat_name = cat_meta["category"]
            categories_set.add(cat_name)
            total_units += c.topic_count
            total_papers += c.paper_count

            # Clean display title to avoid duplication
            display_title = c.title
            if c.code and c.code in display_title:
                display_title = re.sub(
                    r"^" + re.escape(c.code) + r"[\s:\-\–—]*", "", display_title, flags=re.IGNORECASE
                ).strip()
                if not display_title:
                    display_title = c.title

            desc = (c.description or "").strip()
            if desc:
                desc = re.sub(
                    r"(?i)\b(?:offered\s+at|taught\s+at|at\s+[A-Z][A-Za-z\s]+(?:University|College|Institute|School))\b[^.;]*",
                    "",
                    desc,
                ).strip(" ,.;:-")
            if not desc or len(desc) < 15:
                desc = f"Structured syllabus units, lecture notes, and verified past examination problems."

            courses_data.append({
                "id": c.id,
                "code": c.code,
                "slug": c.slug,
                "title": display_title,
                "category": cat_name,
                "subject_key": cat_meta["subject_key"],
                "description": desc,
                "topic_count": c.topic_count,
                "paper_count": c.paper_count,
            })

        bundle = {
            "courses": courses_data,
            "categories": sorted(list(categories_set)),
            "total_courses": len(courses_data),
            "total_units": total_units,
            "total_papers": total_papers,
            "total_disciplines": len(categories_set),
        }
        cache.set(cache_key, bundle, 900)

    context = {
        **bundle,
        "active_tab": "library",
    }
    resp = render(request, "prep/public_library.html", context)
    return set_prep_cache_headers(
        resp,
        max_age=600,
        is_public=not request.user.is_authenticated,
        is_authenticated=request.user.is_authenticated,
    )


def _get_course_topics_summary(course):
    """
    Fast, bulk-aggregated topic summary for course overviews.
    Uses indexed queries instead of scanning and parsing hundreds of pages of raw text per topic,
    reducing course page latency from ~35s down to <0.5s.
    """
    cache_key = f"prep_course_topics_summary_v4_{course.pk}"
    cached_bundle = cache.get(cache_key)
    if cached_bundle is not None:
        return cached_bundle

    topics_qs = list(course.topics.filter(is_active=True).order_by("order", "id"))
    topic_ids = [t.id for t in topics_qs]

    # 1. Bulk aggregate verified questions by topic
    q_counts = dict(
        PrepQuestion.objects.filter(
            topic_id__in=topic_ids,
            verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
        )
        .filter(Q(paper__isnull=True) | Q(paper__is_published=True))
        .values("topic_id")
        .annotate(cnt=Count("id"))
        .values_list("topic_id", "cnt")
    )

    # 2. Bulk inspect notes levels available in PrepContentCache
    cache_entries = PrepContentCache.objects.filter(
        topic_id__in=topic_ids,
        content_type="topic_notes",
    ).values_list("topic_id", "cache_key")

    levels_by_topic = {tid: set() for tid in topic_ids}
    for tid, ckey in cache_entries:
        ck = str(ckey or "")
        if ":level_1:" in ck or "_level_1_" in ck or ck.endswith("_level_1"):
            levels_by_topic[tid].add("level_1")
        elif ":level_2:" in ck or "_level_2_" in ck or ck.endswith("_level_2"):
            levels_by_topic[tid].add("level_2")
        elif ":level_3:" in ck or "_level_3_" in ck or ck.endswith("_level_3"):
            levels_by_topic[tid].add("level_3")

    topics_data = []
    total_questions = 0

    for t in topics_qs:
        auth_count = q_counts.get(t.id, 0)
        total_questions += auth_count

        found_levels = levels_by_topic.get(t.id, set())

        ready_levels_list = []
        if "level_1" in found_levels:
            ready_levels_list.append({"key": "level_1", "label": "Foundation", "num": 1})
        if "level_2" in found_levels:
            ready_levels_list.append({"key": "level_2", "label": "Core Concepts", "num": 2})
        if "level_3" in found_levels:
            ready_levels_list.append({"key": "level_3", "label": "Exam Focus", "num": 3})

        preferred_level = "level_2"
        if any(r["key"] == "level_2" for r in ready_levels_list):
            preferred_level = "level_2"
        elif ready_levels_list:
            preferred_level = ready_levels_list[0]["key"]

        raw_subtopics = t.subtopics if isinstance(t.subtopics, list) else []
        clean_subtopics = [clean_tag_label(str(st)) for st in raw_subtopics if clean_tag_label(str(st))]

        t_data = {
            "id": str(t.id),
            "num": t.order,
            "order": t.order,
            "title": clean_tag_label(t.title) if clean_tag_label(t.title) else t.title,
            "slug": t.slug,
            "summary": clean_topic_summary(t.summary, t.title, clean_subtopics),
            "subtopics": clean_subtopics,
            "subtopics_count": len(clean_subtopics),
            "question_count": auth_count,
            "authentic_count": auth_count,
            "ready_levels": ready_levels_list,
            "ready_levels_count": len(ready_levels_list),
            "preferred_level": preferred_level,
        }
        topics_data.append(t_data)

    result = (topics_data, total_questions)
    cache.set(cache_key, result, 900)
    return result


def prep_public_course(request, course_slug):
    """Public, canonical course syllabus page with internal links to each topic."""
    course = get_object_or_404(PrepCourse, slug=course_slug, is_active=True)
    topics_data, total_questions_count = _get_course_topics_summary(course)
    cat_meta = _resolve_course_category_meta(course)

    display_title = course.title
    if course.code and course.code in display_title:
        display_title = re.sub(
            r"^" + re.escape(course.code) + r"[\s:\-\–—]*", "", display_title, flags=re.IGNORECASE
        ).strip()
        if not display_title:
            display_title = course.title

    desc = (course.description or "").strip()
    if desc:
        desc = re.sub(
            r"(?i)\b(?:offered\s+at|taught\s+at|at\s+[A-Z][A-Za-z\s]+(?:University|College|Institute|School))\b[^.;]*",
            "",
            desc,
        ).strip(" ,.;:-")
    if not desc or len(desc) < 15:
        desc = "Canonical syllabus units, structured theorems, lecture notes, and past examination problems."

    course_obj = {
        "id": course.id,
        "code": course.code,
        "slug": course.slug,
        "title": display_title,
        "category": cat_meta["category"],
        "subject_key": cat_meta["subject_key"],
        "description": desc,
    }

    resp = render(
        request,
        "prep/public_course.html",
        {
            "course": course_obj,
            "topics": topics_data,
            "total_questions_count": total_questions_count,
            "published_papers": course.papers.filter(is_published=True).order_by("-created_at"),
            "active_tab": "library",
        },
    )
    return set_prep_cache_headers(
        resp,
        max_age=600,
        is_public=not request.user.is_authenticated,
        is_authenticated=request.user.is_authenticated,
    )


def _prepare_public_topic_preview(notes: str, questions: list) -> dict:
    """
    Split topic notes and examination questions into an SEO-optimized preview.
    Provides enough high-quality introductory content and question statements
    for search engines to index core syllabus concepts, while protecting
    deep mathematical proofs, worked exemplars, examiner pitfalls, and full
    marking rubrics behind the interactive study conversion barrier.
    """
    preview_notes = ""
    has_locked_notes = False
    locked_sections_count = 0

    if notes:
        headings = list(re.finditer(r"^##\s+", notes, flags=re.MULTILINE))
        if len(headings) >= 3:
            split_idx = headings[2].start()
            preview_notes = notes[:split_idx].strip()
            has_locked_notes = True
            locked_sections_count = len(headings) - 2
        elif len(headings) == 2 and len(notes) > 1800:
            split_idx = headings[1].start()
            preview_notes = notes[:split_idx].strip()
            has_locked_notes = True
            locked_sections_count = 1
        elif len(notes) > 2200:
            cut = notes[:2000].rfind("\n\n")
            preview_notes = notes[:cut].strip() if cut > 800 else notes[:1800].strip()
            has_locked_notes = True
            locked_sections_count = 1
        else:
            preview_notes = notes
            has_locked_notes = False

    sample_questions = questions[:2] if questions else []
    locked_questions_count = max(0, len(questions) - len(sample_questions))

    return {
        "preview_notes": preview_notes,
        "has_locked_notes": has_locked_notes,
        "locked_sections_count": locked_sections_count,
        "sample_questions": sample_questions,
        "locked_questions_count": locked_questions_count,
        "total_question_count": len(questions),
    }


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
    preview = _prepare_public_topic_preview(notes, questions)
    resp = render(
        request,
        "prep/public_topic.html",
        {
            "course": course,
            "topic": topic,
            "notes": notes,
            "preview_notes": preview["preview_notes"],
            "has_locked_notes": preview["has_locked_notes"],
            "locked_sections_count": preview["locked_sections_count"],
            "sample_questions": preview["sample_questions"],
            "locked_questions_count": preview["locked_questions_count"],
            "total_question_count": preview["total_question_count"],
            "notes_updated_at": notes_updated_at,
            "questions": questions,
            "is_indexable": bool(notes or questions),
            "active_tab": "library",
        },
    )
    return set_prep_cache_headers(
        resp,
        max_age=900,
        is_public=not request.user.is_authenticated,
        is_authenticated=request.user.is_authenticated,
    )


def _resolve_course_category_meta(course: PrepCourse) -> dict:
    """Resolve a course's discipline key and clean display tag from its study_profile, category, and title."""
    code_upper = str(course.code or "").strip().upper()
    title_lower = str(course.title or "").strip().lower()
    raw_cat = str(course.category or "").strip()
    profile = course.study_profile if isinstance(course.study_profile, dict) else {}
    family = str(profile.get("subject_family") or "").strip().lower()
    caps = profile.get("capabilities") if isinstance(profile.get("capabilities"), dict) else {}

    cat_map = {
        "Mathematics": ("mathematics", "Mathematics"),
        "Statistics": ("statistics", "Statistics"),
        "Computing": ("computing", "Computing"),
        "Business & Economics": ("economics", "Economics"),
        "Social Sciences": ("social_science", "Social Sciences"),
        "Humanities": ("humanities", "Humanities"),
        "Chemistry": ("chemistry", "Chemistry"),
        "Physics": ("physics", "Physics"),
        "Engineering": ("engineering", "Engineering"),
        "General Sciences": ("general_science", "General Sciences"),
    }

    # 1. Non-default model category field (explicit category assigned in DB)
    if raw_cat in cat_map and raw_cat != "Other":
        sk, label = cat_map[raw_cat]
        return {"subject_key": sk, "category": label}

    # 2. Explicit computing / programming course signals from title or code
    if (
        any(kw in title_lower for kw in ("programming", "software", "algorithm", "data structure", "database", "computer"))
        or (caps.get("code") and "programming" in title_lower)
    ):
        return {"subject_key": "computing", "category": "Computing"}

    # 3. Study profile family mapping (if profile was properly extracted)
    family_map = {
        "statistics": ("statistics", "Statistics"),
        "computing": ("computing", "Computing"),
        "business_economics": ("economics", "Economics"),
        "social_science": ("social_science", "Social Sciences"),
        "humanities": ("humanities", "Humanities"),
        "chemistry": ("chemistry", "Chemistry"),
        "physics": ("physics", "Physics"),
        "engineering": ("engineering", "Engineering"),
        "general_science": ("general_science", "General Sciences"),
        "mathematics": ("mathematics", "Mathematics"),
    }
    if family in family_map:
        sk, label = family_map[family]
        return {"subject_key": sk, "category": label}

    # 4. Fallback inference by code prefix and title keywords
    inferred = infer_course_category(code_upper, course.title)
    if inferred in cat_map:
        sk, label = cat_map[inferred]
        return {"subject_key": sk, "category": label}

    return {"subject_key": "other", "category": raw_cat or "Other"}


@never_cache
def prep_dashboard(request):
    """Mentify Prep Hub Main Landing Page with real database metrics."""
    courses_qs = PrepCourse.objects.filter(is_active=True).annotate(
        topics_count=Count("topics", filter=Q(topics__is_active=True), distinct=True),
        papers_count=Count("papers", distinct=True),
    )

    today_credits_used = 0
    week_credits_used = 0
    if request.user.is_authenticated:
        wallet = PrepWallet.get_or_create_wallet(request.user)
        user_credits = get_available_credits(wallet)
        recent_credit_transactions = wallet.transactions.all()[:10]
        now_ts = timezone.now()
        today_date = now_ts.date()
        week_start = now_ts - datetime.timedelta(days=7)
        for tx in wallet.transactions.filter(created_at__gte=week_start, amount__lt=0):
            spent = abs(tx.amount)
            week_credits_used += spent
            if tx.created_at.date() == today_date:
                today_credits_used += spent
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
        cat_meta = _resolve_course_category_meta(c)
        recent_courses.append({
            "id": c.id,
            "code": c.code,
            "slug": c.slug or c.code.replace(" ", "-"),
            "title": clean_title,
            "level": c.level,
            "category": cat_meta["category"],
            "subject_key": cat_meta["subject_key"],
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

    user_pending_review_docs = []
    if request.user.is_authenticated:
        user_pending_review_docs = [
            {
                "id": str(d.id),
                "filename": d.file.name.split("/")[-1] if d.file else "Document",
                "course_code": d.course.code,
                "course_title": d.course.title,
                "doc_type": d.doc_type,
                "created_at": d.created_at.strftime("%b %d, %Y"),
            }
            for d in PrepDocument.objects.filter(user=request.user, stage="stage_2").select_related("course").order_by("-created_at")[:5]
        ]

    due_spaced_cards = []
    if request.user.is_authenticated:
        from services.prep_spaced_repetition import get_due_spaced_cards
        due_spaced_cards = get_due_spaced_cards(request.user, limit=5)

    context = {
        "active_tab": "dashboard",
        "user_credits": user_credits,
        "today_credits_used": today_credits_used,
        "week_credits_used": week_credits_used,
        "recent_courses": recent_courses,
        "recent_activity": recent_activity,
        "recent_credit_transactions": recent_credit_transactions,
        "total_active_courses": enrolled_courses.count(),
        "total_papers": total_papers,
        "total_topics": total_topics,
        "total_questions": total_questions,
        "featured_topics": featured_topics,
        "latest_study_item": latest_study_item,
        "user_pending_review_docs": user_pending_review_docs,
        "due_spaced_cards": due_spaced_cards,
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
        cat_meta = _resolve_course_category_meta(c)
        courses_data.append({
            "id": c.id,
            "code": c.code,
            "slug": c.slug or c.code.replace(" ", "-"),
            "title": clean_title,
            "level": c.level,
            "category": cat_meta["category"],
            "subject_key": cat_meta["subject_key"],
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
            cat_meta = _resolve_course_category_meta(course)
            result = {
                "id": course.id,
                "code": course.code,
                "title": title,
                "level": course.level,
                "category": cat_meta["category"],
                "subject_key": cat_meta["subject_key"],
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

    course_papers = []
    topics_data, total_questions_count = _get_course_topics_summary(course)

    from services.prep_ingestion import learner_visible_assessment_questions
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
    # Documents under review should ONLY be visible to the user who uploaded them (or staff/admin)
    pending_docs_qs = course.documents.filter(stage__in=["stage_1", "stage_2"]).order_by("-created_at")
    if not request.user.is_staff:
        pending_docs_qs = pending_docs_qs.filter(user=request.user)

    for d in pending_docs_qs:
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
    cat_meta = _resolve_course_category_meta(course)
    course_obj = {
        "id": course.id,
        "code": course.code,
        "title": display_title,
        "level": course.level,
        "category": cat_meta["category"],
        "subject_key": cat_meta["subject_key"],
        "is_enrolled": is_enrolled,
        "description": course.description or "Canonical syllabus units, structured theorems, lecture notes, and past examination problems.",
    }

    total_subtopics_count = sum(len(t.get("subtopics") or []) for t in topics_data)
    ready_topics_count = sum(1 for t in topics_data if t.get("ready_levels"))

    context = {
        "active_tab": "courses",
        "user_credits": get_available_credits(wallet),
        "course": course_obj,
        "topics": topics_data,
        "total_questions_count": total_questions_count,
        "total_subtopics_count": total_subtopics_count,
        "ready_topics_count": ready_topics_count,
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
    if active_subtab not in {"notes", "assistant", "past_questions", "practice", "explore"}:
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

    # 2. Practice Variants: Persist questions already unlocked/generated by THIS student.
    # If the student has never unlocked questions for this topic, keep empty so they
    # are prompted to generate and cannot view variants for free.
    generated_qs = []
    if request.user.is_authenticated and topic:
        from prep.models import PrepStudentQuestionUnlock
        unlocked_records = (
            PrepQuestion.objects.filter(
                unlocked_by_students__user=request.user,
                unlocked_by_students__topic=topic,
                question_type="generated",
                verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
            )
            .select_related("paper")
            .order_by("unlocked_by_students__unlocked_at", "number", "id")
            .distinct()
        )
        for q in unlocked_records:
            clean_q = normalize_math_delimiters(q.question_latex) if q.question_latex else ""
            clean_sol = validated_question_solution(q)
            has_formatting_errors = (
                bool(re.search(r"[\uf000-\uffff]||||||||||", q.question_latex or ""))
                or (q.question_latex and len(q.question_latex.strip()) < 15)
            )
            generated_qs.append({
                "id": q.id,
                "number": q.number,
                "marks": q.marks,
                "paper_title": q.paper.title if q.paper else f"{course_code} Practice Variant",
                "year": q.paper.year if q.paper else "Variant",
                "topic_label": q.topic_label or topic_title,
                "question_latex": clean_q,
                "solution_latex": clean_sol,
                "has_solution": bool(clean_sol),
                "is_flagged": False,
                "has_formatting_errors": has_formatting_errors,
                "is_adapted": False,
            })

    # 3. Preload notes with tiered access:
    # Level 2 (Core Concepts) is free for all students.
    # Level 1 (Foundation: 2 credits) and Level 3 (Exam Focus: 4 credits) are charged
    # only upon fetch/unlock, and only if notes exist in cache.
    from services.prep_ai_router import get_published_topic_note_levels
    from services.prep_note_access import (
        get_unlocked_topic_note_levels,
        unlock_topic_note_level,
        NOTE_LEVEL_CREDIT_COSTS,
        NOTE_LEVEL_LABELS,
    )
    all_published_notes = get_published_topic_note_levels(topic)
    unlocked_levels = get_unlocked_topic_note_levels(request.user, topic)
    from services.prep_topic_tutor import list_topic_conversations, serialize_topic_conversation
    assistant_conversations = list_topic_conversations(request.user, topic)
    latest_session = topic.chat_sessions.filter(user=request.user).order_by("-updated_at", "-id").first()
    initial_assistant_conversation = serialize_topic_conversation(latest_session) if latest_session else None
    
    requested_level = request.GET.get("level", "").strip().lower()
    initial_notes_error = ""

    if requested_level in ("level_1", "level_3"):
        note_candidate = all_published_notes.get(requested_level, "")
        success, deducted, err = unlock_topic_note_level(
            request.user, topic, requested_level, note_candidate
        )
        if success:
            initial_level = requested_level
            initial_notes = note_candidate
            unlocked_levels.add(requested_level)
        else:
            initial_level = "level_2"
            initial_notes = all_published_notes.get("level_2", "")
            initial_notes_error = err
    else:
        initial_level = "level_2"
        initial_notes = all_published_notes.get("level_2", "")

    if not initial_notes:
        initial_notes_error = initial_notes_error or "No validated notes are available for this topic yet."

    # Filter published_notes_by_level so only unlocked levels (level_2 is always unlocked)
    # are sent in the initial HTML to prevent free unauthorized scraping.
    published_notes_by_level = {
        lvl: c for lvl, c in all_published_notes.items()
        if lvl in unlocked_levels
    }

    course_id_val = str(topic.course_id) if (topic and getattr(topic, "course_id", None)) else ""

    topic_dict = {
        "id": str(topic.id) if topic else str(topic_id),
        "title": topic_title,
        "course_id": course_id_val,
        "course_code": course_code,
        "course_title": course_title,
        "subtopics": subtopics,
        "summary": topic.summary if (topic and topic.summary) else "Core syllabus definitions, theorems, and proofs.",
    }

    is_enrolled = PrepCourseEnrollment.objects.filter(user=request.user, course=topic.course).exists()
    if not is_enrolled and request.user.is_authenticated:
        PrepCourseEnrollment.objects.get_or_create(user=request.user, course=topic.course, defaults={"source": "topic_study"})
        is_enrolled = True

    context = {
        "active_tab": "history" if from_tab == "history" else "courses",
        "active_subtab": active_subtab,
        "from_history": from_tab == "history",
        "is_enrolled": is_enrolled,
        "user_credits": get_available_credits(wallet),
        "course_id": course_id_val,
        "topic": topic_dict,
        "initial_level": initial_level,
        "initial_notes": initial_notes,
        "published_notes_by_level": published_notes_by_level,
        "unlocked_levels": {
            "level_1": "level_1" in unlocked_levels,
            "level_2": True,
            "level_3": "level_3" in unlocked_levels,
        },
        "level_costs": NOTE_LEVEL_CREDIT_COSTS,
        "level_labels": NOTE_LEVEL_LABELS,
        "initial_notes_error": initial_notes_error,
        "initial_notes_stale": False,
        "authentic_questions": authentic_qs,
        "generated_questions": generated_qs,
        "assistant_conversations": assistant_conversations,
        "initial_assistant_conversation": initial_assistant_conversation,
        "tutor_ocr_credits_per_image_page": max(
            1,
            int(getattr(settings, "PREP_OCR_CREDITS_PER_IMAGE_PAGE", 5)),
        ),
    }

    # 4. Explore Further: Approved learning resources & Wikipedia concept overview
    from prep.models import PrepTopicResource, PrepTopicWikipedia, PrepTopicAcademicPaper, PrepStudentSpacedCard

    topic_resources_list = list(PrepTopicResource.objects.filter(
        Q(topic=topic) | (Q(topic__isnull=True) & Q(course=topic.course)),
        is_approved=True,
    ).order_by("-created_at"))

    topic_simulations = [r for r in topic_resources_list if r.resource_type == "simulation"]
    topic_videos = [r for r in topic_resources_list if r.resource_type in ("youtube", "video")]
    topic_readings = [r for r in topic_resources_list if r.resource_type not in ("youtube", "video", "simulation")]

    # Fast DB cache read only (~1ms). Never block initial page render with external Wikimedia HTTP calls!
    wiki_entry = PrepTopicWikipedia.objects.filter(topic=topic).first()
    topic_papers = list(PrepTopicAcademicPaper.objects.filter(topic=topic, is_approved=True).order_by("-citation_count", "-year")[:5])

    is_in_spaced_deck = False
    if request.user.is_authenticated:
        is_in_spaced_deck = PrepStudentSpacedCard.objects.filter(
            user=request.user, topic=topic, question__isnull=True
        ).exists()

    context["topic_resources"] = topic_resources_list
    context["topic_simulations"] = topic_simulations
    context["topic_videos"] = topic_videos
    context["topic_readings"] = topic_readings
    context["topic_papers"] = topic_papers
    context["wiki_entry"] = wiki_entry
    context["is_in_spaced_deck"] = is_in_spaced_deck
    return render(request, "prep/topic_study.html", context)


@never_cache
@require_http_methods(["GET"])
def prep_topic_wikipedia_api(request, topic_id):
    """Asynchronous background endpoint to fetch or retrieve cached Wikipedia summary without blocking page load."""
    topic = get_object_or_404(PrepTopic, pk=topic_id, is_active=True)
    from services.prep_wikipedia import get_or_fetch_wikipedia_summary
    entry = get_or_fetch_wikipedia_summary(topic)
    if not entry or not entry.extract:
        return JsonResponse({"success": False, "found": False})
    return JsonResponse({
        "success": True,
        "found": True,
        "title": entry.wikipedia_title,
        "extract": entry.extract,
        "canonical_url": entry.canonical_url,
        "thumbnail_url": entry.thumbnail_url,
        "description": entry.description,
    })


@never_cache
@require_http_methods(["GET"])
def prep_topic_papers_api(request, topic_id):
    """Asynchronous background endpoint to fetch or retrieve cached academic research papers."""
    topic = get_object_or_404(PrepTopic, pk=topic_id, is_active=True)
    from services.prep_research import get_or_fetch_academic_papers
    papers = get_or_fetch_academic_papers(topic, limit=3)
    papers_data = []
    for p in papers:
        papers_data.append({
            "id": p.id,
            "title": p.title,
            "authors": p.authors,
            "year": p.year,
            "venue": p.venue,
            "abstract": p.abstract,
            "citation_count": p.citation_count,
            "open_access_pdf_url": p.open_access_pdf_url,
            "doi_url": p.doi_url,
            "source": p.source,
        })
    return JsonResponse({
        "success": True,
        "count": len(papers_data),
        "papers": papers_data,
    })


@login_required
@never_cache
@require_http_methods(["GET"])
def prep_spaced_cards_due_api(request):
    """Returns spaced repetition topic cards due for review for the authenticated student."""
    from services.prep_spaced_repetition import get_due_spaced_cards
    topic_id = request.GET.get("topic_id")
    topic = None
    if topic_id and topic_id.isdigit():
        topic = PrepTopic.objects.filter(pk=int(topic_id), is_active=True).first()
    
    cards = get_due_spaced_cards(request.user, topic=topic, limit=12)
    cards_data = []
    for c in cards:
        cards_data.append({
            "id": c.id,
            "topic_id": c.topic_id,
            "topic_title": c.topic.title,
            "course_code": c.topic.course.code if c.topic.course else "",
            "card_title": c.card_title or c.topic.title,
            "prompt_text": c.prompt_text,
            "answer_text": c.answer_text,
            "reps": c.reps,
            "state": c.state,
            "due_date": c.due_date.isoformat(),
        })
    return JsonResponse({
        "success": True,
        "count": len(cards_data),
        "cards": cards_data,
    })


@login_required
@never_cache
@require_http_methods(["POST"])
def prep_spaced_card_review_api(request, card_id):
    """Applies FSRS memory rating for a card ('again', 'hard', 'good', 'easy')."""
    from services.prep_spaced_repetition import review_spaced_card
    try:
        import json
        payload = json.loads(request.body.decode("utf-8") or "{}")
    except Exception:
        payload = {}
    
    rating = payload.get("rating", "good")
    res = review_spaced_card(card_id, request.user, rating)
    if not res:
        return JsonResponse({"success": False, "error": "Card not found or access denied."}, status=404)
    return JsonResponse({
        "success": True,
        "card": res,
    })


@login_required
@never_cache
@require_http_methods(["POST"])
def prep_spaced_card_add_api(request):
    """Enrolls or removes a syllabus topic in the student's FSRS spaced repetition daily deck."""
    from services.prep_spaced_repetition import toggle_spaced_card_for_topic
    try:
        import json
        payload = json.loads(request.body.decode("utf-8") or "{}")
    except Exception:
        payload = {}

    topic_id = payload.get("topic_id")
    if not topic_id:
        return JsonResponse({"success": False, "error": "topic_id is required."}, status=400)

    topic = PrepTopic.objects.filter(pk=topic_id).first()
    if not topic:
        return JsonResponse({"success": False, "error": "Topic not found."}, status=404)

    card, is_enrolled = toggle_spaced_card_for_topic(request.user, topic)
    return JsonResponse({
        "success": True,
        "is_enrolled": is_enrolled,
        "card_id": card.id if card else None,
        "due_date": card.due_date.isoformat() if card else None,
        "topic_id": topic.id,
        "topic_title": topic.title,
    })


@never_cache
@require_http_methods(["GET"])
def prep_topic_quiz_api(request, topic_id):
    """
    Returns 5 multiple-choice drill questions for the topic.
    Withholds correct answers and explanations until submitted.
    """
    if not request.user.is_authenticated:
        return JsonResponse({
            "success": False,
            "error": "Please sign in or create an account to start active recall drills.",
        }, status=401)

    topic = get_object_or_404(PrepTopic, pk=topic_id, is_active=True)
    from services.credit_service import (
        enforce_subscription_limit,
        get_available_credits,
        consume_credits,
        InsufficientCredits,
        PlanLimitExceeded,
    )
    from prep.models import PrepWallet

    count = 5
    try:
        raw_count = int(request.GET.get("count", 5))
        count = max(1, min(raw_count, 10))
    except (ValueError, TypeError):
        count = 5

    wallet = PrepWallet.get_or_create_wallet(request.user)
    available_credits = get_available_credits(wallet)

    # Check whether the drill is covered by active subscription allowance
    has_sub = has_active_subscription(wallet)
    allowance = get_remaining_practice_question_allowance(wallet) if has_sub else 0
    is_covered_by_plan = has_sub and allowance >= count

    cost_in_credits = 0 if is_covered_by_plan else count
    if cost_in_credits > 0 and available_credits < cost_in_credits:
        if wallet.current_plan == "freemium":
            err_msg = f"Insufficient credits: Active recall drills require {cost_in_credits} credits on Freemium. You currently have {available_credits} credits. Please top up your credits or subscribe to a plan."
        else:
            err_msg = f"Insufficient credits: You have used your monthly plan question allowance and have {available_credits} credits. At least {cost_in_credits} credits are required to launch this drill. Please top up credits or upgrade to Pro."
        return JsonResponse({
            "success": False,
            "error": err_msg,
            "credits_balance": available_credits,
            "upgrade_required": True,
        }, status=402)

    fresh = request.GET.get("fresh") in {"1", "true", "True"}
    try:
        from services.prep_topic_quiz import get_or_create_topic_quiz
        questions = get_or_create_topic_quiz(
            topic,
            count=count,
            user=request.user,
            force_fresh=fresh,
        )
        if not questions:
            return JsonResponse({
                "success": False,
                "error": "Drill questions could not be prepared at this time. Please try again shortly.",
                "credits_balance": get_available_credits(wallet),
            }, status=503)

        course_code = topic.course.code if topic.course else ""
        if is_covered_by_plan:
            credits_deducted = 0
            PrepTransaction.objects.create(
                wallet=wallet,
                amount=0,
                action_type="active_recall_drill",
                description=f"Active Recall Drill ({len(questions)} Qs, Plan Allowance): {course_code} - {topic.title}",
                metadata={"topic_id": topic.id, "count": len(questions), "covered_by_plan": True},
            )
        else:
            credits_deducted = min(len(questions), cost_in_credits)
            try:
                consume_credits(
                    wallet,
                    amount=credits_deducted,
                    action_type="active_recall_drill",
                    description=f"Active Recall Drill ({len(questions)} Qs): {course_code} - {topic.title}",
                    metadata={"topic_id": topic.id, "count": len(questions)},
                )
            except InsufficientCredits:
                return JsonResponse({
                    "success": False,
                    "error": f"Active recall drill requires {credits_deducted} credits (available: {get_available_credits(wallet)}).",
                    "credits_balance": get_available_credits(wallet),
                }, status=402)

        # Downgrade trial -> freemium immediately if trial credits hit zero
        if wallet.current_plan == "trial" and get_available_credits(wallet) == 0:
            wallet.current_plan = "freemium"
            wallet.save(update_fields=["current_plan", "updated_at"])

        data = []
        for q in questions:
            data.append({
                "id": q.id,
                "question": q.question_text,
                "options": q.options,
                "difficulty": q.difficulty,
            })
        return JsonResponse({
            "success": True,
            "topic_id": topic.id,
            "topic_title": topic.title,
            "course_code": course_code,
            "count": len(data),
            "questions": data,
            "credits_deducted": credits_deducted,
            "credits_balance": get_available_credits(wallet),
        })
    except Exception as exc:
        logger.exception("[prep_topic_quiz_api] Failed to prepare quiz for topic %s: %s", topic.id, exc)
        return JsonResponse({
            "success": False,
            "error": "Drill questions could not be prepared at this time. Please try again shortly.",
            "credits_balance": get_available_credits(wallet),
        }, status=503)



@never_cache
@require_http_methods(["POST"])
def prep_topic_quiz_submit_api(request, topic_id):
    """
    Evaluates a user's chosen option for a quiz question.
    Returns correct status, correct answer, and distractor explanations.
    """
    topic = get_object_or_404(PrepTopic, pk=topic_id, is_active=True)
    try:
        import json
        payload = json.loads(request.body.decode("utf-8") or "{}")
    except Exception:
        payload = request.POST

    question_id = payload.get("question_id")
    selected_option = payload.get("selected_option")
    if not question_id or not selected_option:
        return JsonResponse({"success": False, "error": "question_id and selected_option are required."}, status=400)

    from services.prep_topic_quiz import evaluate_quiz_answer
    res = evaluate_quiz_answer(
        quiz_question_id=int(question_id),
        selected_option=str(selected_option),
        user=request.user if request.user.is_authenticated else None,
    )
    if not res.get("success"):
        return JsonResponse(res, status=400)
    return JsonResponse(res)


@login_required
@never_cache
@require_http_methods(["POST"])
def prep_topic_quiz_generate_api(request, topic_id):
    """
    Generates fresh multiple-choice drill questions for the topic.
    """
    topic = get_object_or_404(PrepTopic, pk=topic_id, is_active=True)
    try:
        import json
        payload = json.loads(request.body.decode("utf-8") or "{}")
    except Exception:
        payload = request.POST

    count = 5
    try:
        count = max(1, min(int(payload.get("count", 5)), 10))
    except (ValueError, TypeError):
        count = 5

    difficulty = str(payload.get("difficulty") or "medium").lower()
    from services.prep_topic_quiz import generate_topic_quiz_questions
    created = generate_topic_quiz_questions(topic, count=count, difficulty=difficulty)
    return JsonResponse({
        "success": True,
        "count": len(created),
        "message": f"Generated {len(created)} new drill questions for {topic.title}.",
    })



@login_required
@never_cache
@require_http_methods(["GET", "POST"])
def prep_topic_tutor_api(request, topic_id):
    """Load or send a private topic conversation and optional bounded study uploads."""
    topic = get_object_or_404(PrepTopic, pk=topic_id, is_active=True)
    if not (
        request.user.is_staff
        or request.user.is_superuser
        or PrepCourseEnrollment.objects.filter(user=request.user, course=topic.course).exists()
    ):
        if request.user.is_authenticated:
            PrepCourseEnrollment.objects.get_or_create(user=request.user, course=topic.course, defaults={"source": "topic_tutor"})
        else:
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
        elif conversations:
            current = topic.chat_sessions.filter(pk=conversations[0]["id"], user=request.user).first()
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

    wallet = PrepWallet.get_or_create_wallet(request.user)
    available_credits = get_available_credits(wallet)
    if available_credits < 1:
        return JsonResponse(
            {
                "success": False,
                "error": "You need at least 1 credit to ask the AI Tutor. Please top up your wallet to continue.",
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
            status=200,
        )
    except Exception:
        logger.exception("Topic tutor request failed for topic %s and user %s", topic.pk, request.user.pk)
        return JsonResponse(
            {"success": False, "error": "The topic tutor could not complete this request. Please try again."},
            status=200,
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
        "user_credits": get_available_credits(wallet),
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


def _serialize_upload_document(d: PrepDocument) -> dict:
    size_mb = round(d.file_size_bytes / (1024 * 1024), 1) if d.file_size_bytes else 0
    notes_text = str(d.tutor_review_notes or "").strip()
    failed = bool(d.stage == "stage_1" and notes_text.startswith("Ingestion failed"))
    course_slug = d.course.slug or d.course.code.replace(" ", "-")
    course_title = getattr(d.course, "clean_title", "") or d.course.title
    if failed:
        stage_label = "Needs attention"
    elif d.is_duplicate:
        stage_label = "Duplicate"
    elif d.stage == "stage_1":
        stage_label = "Processing"
    elif d.stage == "stage_3":
        stage_label = "Ready to study"
    else:
        stage_label = "In tutor review"
    return {
        "id": str(d.id),
        "filename": d.file.name.split("/")[-1] if d.file else "Document.pdf",
        "course": d.course.code,
        "course_title": course_title,
        "course_url": reverse("prep:course_detail", kwargs={"course_code": course_slug}),
        "type": d.doc_type,
        "size": f"{size_mb} MB" if size_mb > 0 else "< 1 MB",
        "date": d.created_at.strftime("%b %d, %Y"),
        "stage_code": "failed" if failed else d.stage,
        "stage": stage_label,
        "is_duplicate": bool(d.is_duplicate),
        "failed": failed,
        "error": notes_text if failed else "",
    }


@never_cache
def prep_upload(request):
    """Upload one document group to an existing course or create a new course."""
    if request.method == "POST":
        is_async = (
            request.headers.get("X-Requested-With") == "XMLHttpRequest"
            or request.POST.get("async") == "1"
        )

        def _reject(msg: str, status_code: int = 400):
            if is_async:
                return JsonResponse({"success": False, "error": msg}, status=status_code)
            messages.error(request, msg)
            return redirect("prep:upload")

        if not request.user.is_authenticated:
            if is_async:
                return JsonResponse(
                    {
                        "success": False,
                        "error": "Please sign in or create a free account to upload study materials.",
                        "login_url": f"/accounts/login/?next={request.path}",
                    },
                    status=401,
                )
            messages.info(request, "Please sign in or create a free account to upload study materials.")
            return redirect(f"/accounts/login/?next={request.path}")

        upload_mode = request.POST.get("upload_mode", "document").strip()
        if upload_mode == "resource_link":
            resource_url = request.POST.get("resource_url", "").strip()
            resource_title = request.POST.get("resource_title", "").strip()
            resource_type = request.POST.get("resource_type", "website").strip()
            resource_desc = request.POST.get("resource_description", "").strip()
            course_id = request.POST.get("course_id", "").strip()
            course_name = request.POST.get("course_name", "").strip()
            target_topic_id = request.POST.get("topic_id", "").strip()

            if not resource_url or not (resource_url.startswith("http://") or resource_url.startswith("https://")):
                return _reject("Please enter a valid web URL starting with http:// or https://")

            course = None
            if course_id:
                try:
                    course = PrepCourse.objects.get(pk=int(course_id), is_active=True)
                except (ValueError, PrepCourse.DoesNotExist):
                    return _reject("Choose an active course from the list.")
            else:
                if not course_name:
                    return _reject("Choose a course for this learning resource.")
                course_code, course_title = parse_course_code_and_title(course_name)
                course = PrepCourse.objects.filter(code__iexact=course_code).first()
                if not course:
                    course = PrepCourse.objects.create(
                        code=course_code,
                        title=course_title,
                        level="Standard",
                        category=infer_course_category(course_code, course_title),
                    )

            target_topic = None
            if target_topic_id and target_topic_id.isdigit():
                target_topic = PrepTopic.objects.filter(pk=int(target_topic_id), course=course).first()

            from services.prep_wikipedia import extract_youtube_id
            from prep.models import PrepTopicResource

            yt_id = extract_youtube_id(resource_url)
            embed_id = ""
            thumbnail_url = ""
            if yt_id:
                embed_id = yt_id
                resource_type = "youtube"
                thumbnail_url = f"https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"
                if not resource_title:
                    resource_title = f"{course.code} Video Lecture"

            if not resource_title:
                resource_title = f"{course.code} Learning Resource"

            valid_types = {"youtube", "video", "article", "simulation", "website"}
            if resource_type not in valid_types:
                resource_type = "website"

            PrepTopicResource.objects.create(
                course=course,
                topic=target_topic,
                title=resource_title[:255],
                url=resource_url[:500],
                resource_type=resource_type,
                description=resource_desc,
                thumbnail_url=thumbnail_url,
                embed_id=embed_id,
                submitted_by=request.user,
                is_approved=False,
            )

            PrepNotification.objects.create(
                user=request.user,
                title="Learning Resource Submitted",
                message=f"'{resource_title}' has been submitted for {course.code} and placed in the tutor review queue.",
                category="upload",
                url=reverse("prep:course_detail", kwargs={"course_code": course.slug or course.code.replace(" ", "-")}),
            )

            success_msg = f"'{resource_title}' was submitted successfully! It is now in the review queue and will appear under Explore Further once approved."
            if is_async:
                return JsonResponse({"success": True, "message": success_msg})
            messages.success(request, success_msg)
            return redirect(f"{reverse('prep:upload')}?course_id={course.pk}&tab=resource")

        course_id = request.POST.get("course_id", "").strip()
        course_name = request.POST.get("course_name", "").strip()
        doc_type = request.POST.get("doc_type", "Lecture Notes")
        academic_year = request.POST.get("academic_year", "").strip()
        topic_name = request.POST.get("topic_name", "").strip()
        uploaded_files = request.FILES.getlist("files") or request.FILES.getlist("file")

        if not uploaded_files:
            return _reject("Please attach at least one document file to upload.")

        if len(uploaded_files) > 10:
            return _reject("Upload up to 10 documents in one batch.")

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
                return _reject(
                    f"'{invalid_file.name}' has an unsupported format. Use PDF, Word, Markdown, or text files."
                )
            return _reject(f"'{invalid_file.name}' exceeds the 15 MB per-file limit.")

        valid_doc_types = dict(PrepDocument.DOC_TYPES)
        if doc_type not in valid_doc_types:
            return _reject("Choose a valid document type.")

        if course_id:
            try:
                course = PrepCourse.objects.get(pk=int(course_id), is_active=True)
            except (ValueError, PrepCourse.DoesNotExist):
                return _reject("Choose an active course from the list or select a new course.")
        else:
            if not course_name:
                return _reject("Choose an existing course or enter a course code and title.")
            course_code, course_title = parse_course_code_and_title(course_name)
            course = PrepCourse.objects.filter(code__iexact=course_code).first()
            if not course:
                course = PrepCourse.objects.create(
                    code=course_code,
                    title=course_title,
                    level="Standard",
                    category=infer_course_category(course_code, course_title),
                )

        PrepCourseEnrollment.objects.get_or_create(
            user=request.user,
            course=course,
            defaults={"source": "upload"},
        )

        if is_async:
            import hashlib
            from services.prep_ingestion import enqueue_prep_document_ingestion

            wallet = PrepWallet.get_or_create_wallet(request.user)

            # ── Plan upload gate — check allowance or credit balance before touching files ──
            try:
                enforce_upload_limit(wallet, required_credits=2)
            except InsufficientCredits as exc:
                return JsonResponse({
                    "success": False,
                    "error": str(exc),
                    "credits_balance": get_available_credits(wallet),
                    "upgrade_required": True,
                }, status=402)
            except UploadLimitExceeded as exc:
                return JsonResponse({"success": False, "error": str(exc), "upgrade_required": True}, status=403)

            course_slug = course.slug or course.code.replace(" ", "-")
            course_url = reverse("prep:course_detail", kwargs={"course_code": course_slug})

            queued = 0
            duplicates = 0
            failures = []
            created_docs = []
            total_credits_deducted = 0

            for uploaded_file in uploaded_files:
                target_course = course
                # Course Code Mismatch Safeguard: if filename explicitly mentions another active course
                # (e.g. SMA 190 in SMA_190_NOTES.pdf while SMA 103 was selected), auto-route to correct course
                file_code_match = re.search(r'\b([A-Za-z]{2,4})[_\s-]*(\d{3,4})\b', uploaded_file.name)
                if file_code_match:
                    detected_prefix = file_code_match.group(1).upper()
                    detected_num = file_code_match.group(2)
                    detected_course = (
                        PrepCourse.objects.filter(code__iexact=f"{detected_prefix} {detected_num}", is_active=True).first()
                        or PrepCourse.objects.filter(code__iexact=f"{detected_prefix}{detected_num}", is_active=True).first()
                    )
                    if detected_course and detected_course.id != course.id:
                        logger.info("Auto-routing '%s' from %s to matching course %s", uploaded_file.name, course.code, detected_course.code)
                        target_course = detected_course

                try:
                    raw_bytes = uploaded_file.read()
                    uploaded_file.seek(0)
                except Exception as exc:
                    failures.append(f"{uploaded_file.name}: could not read file ({exc})")
                    continue

                file_sha256 = hashlib.sha256(raw_bytes).hexdigest()
                duplicate = (
                    PrepDocument.objects.filter(course=target_course, file_sha256=file_sha256)
                    .order_by("created_at")
                    .first()
                )
                if duplicate:
                    prep_doc = PrepDocument.objects.create(
                        user=request.user,
                        course=target_course,
                        doc_type=doc_type,
                        academic_year=academic_year,
                        topic_name=topic_name,
                        file=uploaded_file,
                        file_size_bytes=uploaded_file.size,
                        file_sha256=file_sha256,
                        is_duplicate=True,
                        duplicate_of=duplicate,
                        stage="stage_2",
                    )
                    duplicates += 1
                    created_docs.append(_serialize_upload_document(prep_doc))
                    continue

                # Document is NOT a duplicate. Check plan allowance or deduct credits.
                is_scanned_ocr = "scanned" in doc_type.lower() or "exam" in doc_type.lower()
                doc_credit_cost = 5 if is_scanned_ocr else 2
                allowance = get_remaining_upload_allowance(wallet)
                scanned_allowance = get_remaining_scanned_allowance(wallet)
                has_sub = has_active_subscription(wallet)

                # Paid subscriptions (Basic, Plus, Pro) cover uploads within their allowance
                if is_scanned_ocr:
                    covered_by_plan = has_sub and (scanned_allowance is None or scanned_allowance > 0)
                else:
                    covered_by_plan = allowance is None or (allowance > 0 if has_sub else False)

                if covered_by_plan:
                    # Covered by plan allowance (0 credits deducted)
                    record_upload(wallet)
                    PrepTransaction.objects.create(
                        wallet=wallet,
                        amount=0,
                        action_type="upload_ocr" if is_scanned_ocr else "upload_text",
                        description=f"Course Material Upload (Plan Allowance - {'OCR' if is_scanned_ocr else 'Digital'}): {target_course.code} - {uploaded_file.name}",
                        metadata={"course_code": target_course.code, "file_name": uploaded_file.name, "covered_by_plan": True},
                    )
                else:
                    # Plan allowance exhausted or Freemium: pay with credits
                    try:
                        consume_credits(
                            wallet,
                            amount=doc_credit_cost,
                            action_type="upload_ocr" if is_scanned_ocr else "upload_text",
                            description=f"Course Material Upload ({'OCR' if is_scanned_ocr else 'Digital'}): {target_course.code} - {uploaded_file.name}",
                            metadata={"course_code": target_course.code, "file_name": uploaded_file.name},
                        )
                        total_credits_deducted += doc_credit_cost
                    except InsufficientCredits:
                        failures.append(
                            f"{uploaded_file.name}: requires {doc_credit_cost} credits (available: {get_available_credits(wallet)})"
                        )
                        continue

                prep_doc = PrepDocument.objects.create(
                    user=request.user,
                    course=target_course,
                    doc_type=doc_type,
                    academic_year=academic_year,
                    topic_name=topic_name,
                    file=uploaded_file,
                    file_size_bytes=uploaded_file.size,
                    file_sha256=file_sha256,
                    stage="stage_1",
                )
                target_slug = target_course.slug or target_course.code.replace(" ", "-")
                target_course_url = reverse("prep:course_detail", kwargs={"course_code": target_slug})
                PrepHistory.objects.create(
                    user=request.user,
                    title=f"Uploaded {uploaded_file.name}",
                    course_code=target_course.code,
                    item_type=doc_type,
                    url=target_course_url,
                )
                enqueue_prep_document_ingestion(prep_doc.pk)
                queued += 1
                created_docs.append(_serialize_upload_document(prep_doc))

            status_parts = []
            if queued:
                status_parts.append(
                    f"Uploaded {queued} document(s) for {course.code}. Background extraction & syllabus indexing has started."
                )
                if total_credits_deducted > 0:
                    status_parts.append(f"({total_credits_deducted} credits deducted).")
            if duplicates:
                status_parts.append(
                    f"{duplicates} duplicate document(s) recognized ($0 free) and saved without re-indexing."
                )
            if failures:
                status_parts.append(f"{len(failures)} document(s) need attention: " + "; ".join(failures)[:500])

            status_code = 202 if queued else (200 if duplicates else (402 if any("requires" in f for f in failures) else 400))
            return JsonResponse(
                {
                    "success": bool(queued or duplicates or not failures),
                    "queued_count": queued,
                    "duplicate_count": duplicates,
                    "failed_count": len(failures),
                    "failures": failures,
                    "message": " ".join(status_parts) or "Upload processed.",
                    "course_id": course.pk,
                    "course_code": course.code,
                    "course_title": f"{course.code} — {course.title}",
                    "course_url": course_url,
                    "status_url": reverse("prep:api_document_upload_status"),
                    "credits_deducted": total_credits_deducted,
                    "credits_balance": get_available_credits(wallet),
                    "documents": created_docs,
                },
                status=status_code,
            )

        from services.prep_ingestion import enqueue_prep_document_ingestion
        succeeded = 0
        duplicates = 0
        failures = []
        for uploaded_file in uploaded_files:
            target_course = course
            file_code_match = re.search(r'\b([A-Za-z]{2,4})[_\s-]*(\d{3,4})\b', uploaded_file.name)
            if file_code_match:
                detected_prefix = file_code_match.group(1).upper()
                detected_num = file_code_match.group(2)
                detected_course = (
                    PrepCourse.objects.filter(code__iexact=f"{detected_prefix} {detected_num}", is_active=True).first()
                    or PrepCourse.objects.filter(code__iexact=f"{detected_prefix}{detected_num}", is_active=True).first()
                )
                if detected_course and detected_course.id != course.id:
                    logger.info("Auto-routing '%s' from %s to matching course %s", uploaded_file.name, course.code, detected_course.code)
                    target_course = detected_course

            prep_doc = PrepDocument.objects.create(
                user=request.user,
                course=target_course,
                doc_type=doc_type,
                academic_year=academic_year,
                topic_name=topic_name,
                file=uploaded_file,
                file_size_bytes=uploaded_file.size,
                stage="stage_1",
            )

            try:
                enqueue_prep_document_ingestion(prep_doc.pk)
                succeeded += 1

                course_slug = target_course.slug or target_course.code.replace(" ", "-")
                PrepHistory.objects.create(
                    user=request.user,
                    title=f"Uploaded {uploaded_file.name}",
                    course_code=target_course.code,
                    item_type=doc_type,
                    url=reverse("prep:course_detail", kwargs={"course_code": course_slug}),
                )
            except Exception as exc:
                failures.append(f"{uploaded_file.name}: enqueue failed ({exc})")
                prep_doc.tutor_review_notes = f"Ingestion queue failed: {str(exc)[:1000]}"
                prep_doc.save(update_fields=["tutor_review_notes", "updated_at"])

        if succeeded:
            messages.success(request, f"Uploaded {succeeded} document(s) for {course.code}. Background processing & syllabus indexing has started.")
        if duplicates:
            messages.info(request, f"{duplicates} duplicate document(s) were saved for audit and not re-indexed.")
        if failures:
            messages.error(request, f"{len(failures)} document(s) need attention: " + "; ".join(failures)[:800])

        return redirect(f"{reverse('prep:upload')}?course_id={course.pk}")

    user_credits = 0
    uploads_remaining = 0
    wallet_plan = "freemium"
    if request.user.is_authenticated:
        wallet = PrepWallet.get_or_create_wallet(request.user)
        user_credits = get_available_credits(wallet)
        uploads_remaining = get_remaining_upload_allowance(wallet)
        wallet_plan = wallet.current_plan
    selected_course_id = request.GET.get("course_id", "").strip()
    courses = PrepCourse.objects.filter(is_active=True).order_by("code")
    if not selected_course_id.isdigit() or not courses.filter(pk=selected_course_id).exists():
        selected_course_id = ""
    upload_tab = request.GET.get("tab", "document").strip()
    if upload_tab not in {"document", "resource"}:
        upload_tab = "document"

    course_topics = []
    if selected_course_id:
        course_topics = PrepTopic.objects.filter(course_id=int(selected_course_id), is_active=True).order_by("order", "id")

    all_course_topics = PrepTopic.objects.filter(course__in=courses, is_active=True).values("id", "title", "course_id").order_by("order", "id")

    context = {
        "active_tab": "upload",
        "user_credits": user_credits,
        "uploads_remaining": uploads_remaining,
        "wallet_plan": wallet_plan,
        "upload_courses": courses,
        "selected_course_id": selected_course_id,
        "upload_tab": upload_tab,
        "course_topics": course_topics,
        "all_course_topics": all_course_topics,
    }
    return render(request, "prep/upload.html", context)


@never_cache
@login_required
@require_http_methods(["GET"])
def prep_document_upload_status_api(request):
    """Lightweight status polling endpoint for student background document uploads (max 10)."""
    ids_param = request.GET.get("ids", "").strip()
    qs = PrepDocument.objects.filter(user=request.user).select_related("course")
    if ids_param:
        raw_ids = [part.strip() for part in ids_param.split(",") if part.strip()]
        valid_ids = []
        for raw_id in raw_ids[:10]:
            try:
                valid_ids.append(uuid.UUID(raw_id))
            except (ValueError, TypeError):
                continue
        if valid_ids:
            docs = list(qs.filter(pk__in=valid_ids).order_by("-created_at")[:10])
        else:
            return JsonResponse({"success": True, "documents": [], "has_processing": False})
    else:
        docs = list(qs.order_by("-created_at")[:10])

    serialized = [_serialize_upload_document(d) for d in docs]
    has_processing = any(item["stage_code"] == "stage_1" for item in serialized)
    return JsonResponse(
        {
            "success": True,
            "documents": serialized,
            "has_processing": has_processing,
        }
    )




@never_cache
@login_required
def prep_history(request):
    """Legacy revision history route; redirect to dashboard."""
    return redirect("prep:dashboard")


@never_cache
def prep_billing(request):
    """Credit Balance & M-Pesa Top-Up Page connected to PrepWallet."""
    from services.credit_service import get_plan_upload_limit
    if request.user.is_authenticated:
        wallet = PrepWallet.get_or_create_wallet(request.user)
        user_credits = get_available_credits(wallet)
        if wallet.current_plan == "pro":
            plan_display = "Pro (Exam Master)"
        elif wallet.current_plan == "plus":
            plan_display = "Plus (Semester Pass)"
        elif wallet.current_plan == "basic":
            plan_display = "Basic (Starter Prep)"
        elif wallet.current_plan == "freemium":
            plan_display = "Freemium (Free Forever)"
        elif wallet.current_plan == "expired":
            plan_display = "Expired — Upgrade to Continue"
        else:
            plan_display = "Free Trial (7 Days)"
        is_trial = wallet.current_plan == "trial"
        is_freemium = wallet.current_plan == "freemium"
        can_top_up = True   # Open to all authenticated users on any plan
        plan_expires_at = wallet.plan_expires_at
        recent_transactions = wallet.transactions.all()[:10]
        current_plan_code = wallet.current_plan
        upload_limit = get_plan_upload_limit(wallet)
        uploads_used = wallet.pdf_uploads_this_month
        uploads_remaining = None if upload_limit is None else max(0, upload_limit - uploads_used)
    else:
        wallet = None
        user_credits = 0
        plan_display = "Free 100-Credit Trial (Sign Up Free)"
        is_trial = False
        is_freemium = False
        can_top_up = False
        plan_expires_at = None
        recent_transactions = []
        current_plan_code = None
        upload_limit = 0
        uploads_used = 0
        uploads_remaining = 0

    context = {
        "active_tab": "billing",
        "wallet": wallet,
        "user_credits": user_credits,
        "current_plan": plan_display,
        "is_trial": is_trial,
        "is_freemium": is_freemium,
        "can_top_up": can_top_up,
        "plan_expires_at": plan_expires_at,
        "recent_transactions": recent_transactions,
        "topup_rate_per_credit": 1.5,   # KES 1.5 per credit — used by template JS
        "topup_min_credits": 10,
        "upload_limit": upload_limit,
        "uploads_used": uploads_used,
        "uploads_remaining": uploads_remaining,
        "plans": [
            {
                "id": "freemium_plan",
                "name": "Freemium",
                "price": "KES 0 / mo",
                "price_num": 0,
                "credits": "20 Credits/mo",
                "tagline": "Permanent free access — cached notes and past Q&A always available",
                "is_popular": False,
                "theme_color": "#64748b",
                "theme_bg": "rgba(100, 116, 139, 0.08)",
                "badge_label": "FREE",
                "features": [
                    "20 Free Credits Every Month (auto-refresh)",
                    "Cached Lecture Notes (Read Only)",
                    "Past Exam Questions & Answers",
                    "AI Tutor & Generated Questions (uses credits)",
                    "Upload Course Documents (2–5 credits/doc)",
                    "Buy credit top-ups anytime",
                ],
                "active": current_plan_code == "freemium",
            },
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
                    "20 Free PDF / Document Uploads/mo (then 2–5 credits)",
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
                    "40 Free PDF / Document Uploads/mo (then 2–5 credits)",
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
                    "Unlimited Free Document Uploads",
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



@never_cache
def prep_metrics(request):
    """
    Mentify Prep Metrics & Activity Page.
    Allows students to monitor their credit usage over time (daily) in an interactive graph,
    select/filter by day or date range, and audit their complete credit transaction ledger.
    """
    if not request.user.is_authenticated:
        return redirect(f"{reverse('accounts:login')}?next={reverse('prep:metrics')}")

    wallet = PrepWallet.get_or_create_wallet(request.user)
    available_credits = get_available_credits(wallet)

    days_param = request.GET.get("days", "30").strip()
    date_param = request.GET.get("date", "").strip()

    now = timezone.now()
    if days_param == "7":
        num_days = 7
    elif days_param == "14":
        num_days = 14
    elif days_param == "90":
        num_days = 90
    elif days_param == "all":
        num_days = 365
    else:
        num_days = 30

    start_date = now - datetime.timedelta(days=num_days)
    all_transactions = wallet.transactions.all().order_by("-created_at")

    selected_date_obj = None
    if date_param:
        try:
            selected_date_obj = datetime.date.fromisoformat(date_param)
            table_transactions = all_transactions.filter(
                created_at__date=selected_date_obj
            )
        except ValueError:
            table_transactions = all_transactions
    else:
        table_transactions = all_transactions

    # Daily aggregation over the selected range
    daily_stats = {}
    for i in range(num_days - 1, -1, -1):
        d = (now - datetime.timedelta(days=i)).date()
        iso = d.isoformat()
        daily_stats[iso] = {
            "date": iso,
            "label": d.strftime("%b %d"),
            "used": 0,
            "gained": 0,
            "practice": 0,
            "notes": 0,
            "tutor": 0,
            "ocr": 0,
            "other": 0,
        }

    period_transactions = all_transactions.filter(created_at__gte=start_date)
    total_period_used = 0
    total_period_gained = 0

    category_counts = {
        "AI Practice": 0,
        "Topic Notes": 0,
        "AI Study Tutor": 0,
        "Document OCR": 0,
        "Top-ups & Grants": 0,
    }

    for tx in period_transactions:
        tx_date = tx.created_at.date().isoformat()
        amt = tx.amount
        if tx_date in daily_stats:
            if amt < 0:
                spent = abs(amt)
                daily_stats[tx_date]["used"] += spent
                total_period_used += spent
                if tx.action_type == "ai_practice_gen":
                    daily_stats[tx_date]["practice"] += spent
                    category_counts["AI Practice"] += spent
                elif tx.action_type == "topic_notes":
                    daily_stats[tx_date]["notes"] += spent
                    category_counts["Topic Notes"] += spent
                elif tx.action_type == "topic_tutor":
                    daily_stats[tx_date]["tutor"] += spent
                    category_counts["AI Study Tutor"] += spent
                elif tx.action_type in ("upload_ocr", "topic_tutor_ocr", "upload_text"):
                    daily_stats[tx_date]["ocr"] += spent
                    category_counts["Document OCR"] += spent
                else:
                    daily_stats[tx_date]["other"] += spent
            else:
                daily_stats[tx_date]["gained"] += amt
                total_period_gained += amt
                category_counts["Top-ups & Grants"] += amt

    chart_dates = []
    chart_labels = []
    chart_used = []
    chart_gained = []
    chart_practice = []
    chart_notes = []
    chart_tutor = []
    chart_ocr = []

    for d_iso, s in daily_stats.items():
        chart_dates.append(d_iso)
        chart_labels.append(s["label"])
        chart_used.append(s["used"])
        chart_gained.append(s["gained"])
        chart_practice.append(s["practice"])
        chart_notes.append(s["notes"])
        chart_tutor.append(s["tutor"])
        chart_ocr.append(s["ocr"])

    avg_daily_used = round(total_period_used / max(num_days, 1), 1)
    active_categories = {k: v for k, v in category_counts.items() if k != "Top-ups & Grants" and v > 0}
    top_category = max(active_categories, key=active_categories.get) if active_categories else "None"

    context = {
        "active_tab": "metrics",
        "wallet": wallet,
        "user_credits": available_credits,
        "total_period_used": total_period_used,
        "total_period_gained": total_period_gained,
        "avg_daily_used": avg_daily_used,
        "top_category": top_category,
        "days_selected": str(num_days),
        "selected_date": date_param,
        "chart_dates_json": json.dumps(chart_dates),
        "chart_labels_json": json.dumps(chart_labels),
        "chart_used_json": json.dumps(chart_used),
        "chart_gained_json": json.dumps(chart_gained),
        "chart_practice_json": json.dumps(chart_practice),
        "chart_notes_json": json.dumps(chart_notes),
        "chart_tutor_json": json.dumps(chart_tutor),
        "chart_ocr_json": json.dumps(chart_ocr),
        "daily_stats_json": json.dumps(daily_stats),
        "transactions": table_transactions[:10],
        "total_transactions_count": all_transactions.count(),
    }
    return render(request, "prep/metrics.html", context)


# ─── Step 5: Paystack & M-Pesa Payments ──────────────────────────────────────

import uuid
from datetime import timedelta
from django.db import transaction
from django.conf import settings
from services.paystack_service import PaystackService

PREP_PACKAGES = {
    "topup_custom": {
        # Dynamic — amount and credits are computed in prep_initiate_payment from POST data
        "name": "Custom Credit Top-Up",
        "price_kes": None,   # set dynamically
        "credits": None,     # set dynamically
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

# KES per credit for custom top-up
TOPUP_RATE_KES_PER_CREDIT = 1.5
TOPUP_MIN_CREDITS = 10


@never_cache
@login_required
def prep_initiate_payment(request):
    """Initiate M-Pesa / Paystack payment for credits or monthly exam plan."""
    if request.method != "POST":
        return redirect("prep:billing")

    package_key = request.POST.get("package", "topup_custom")

    # ── Dynamic custom top-up (open to all plans) ──────────────────────────────
    if package_key == "topup_custom":
        try:
            credit_amount = int(request.POST.get("credit_amount", 0))
        except (ValueError, TypeError):
            messages.error(request, "Invalid credit amount entered.")
            return redirect("prep:billing")
        if credit_amount < TOPUP_MIN_CREDITS:
            messages.error(request, f"Minimum top-up is {TOPUP_MIN_CREDITS} credits (KES {round(TOPUP_MIN_CREDITS * TOPUP_RATE_KES_PER_CREDIT)}).")
            return redirect("prep:billing")
        price_kes = round(credit_amount * TOPUP_RATE_KES_PER_CREDIT)
        package = {
            "name": f"{credit_amount} Credits Top-Up",
            "price_kes": price_kes,
            "credits": credit_amount,
            "type": "topup",
        }
    else:
        package = PREP_PACKAGES.get(package_key)
        if not package:
            messages.error(request, "Invalid payment package selected.")
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

    try:
        status_code, body = paystack.initialize(
            email=request.user.email,
            amount_cents=amount_cents,
            reference=reference,
            callback_url=callback_url,
            metadata=metadata,
        )
    except Exception as exc:
        logger.error("Paystack payment initialization error: %s", exc)
        messages.error(request, "Unable to connect to the payment gateway. Please try again in a moment.")
        return redirect("prep:billing")

    if status_code == 200 and body.get("status"):
        auth_url = body.get("data", {}).get("authorization_url")
        if auth_url:
            return redirect(auth_url)

    err = paystack.friendly_error(body, fallback="Could not initiate M-Pesa / Card payment.")
    messages.error(request, f"Payment initialization failed: {err}")
    return redirect("prep:billing")


@never_cache
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

    try:
        status_code, body = paystack.verify(reference)
    except Exception as exc:
        logger.error("Paystack verification error for ref %s: %s", reference, exc)
        messages.error(request, "Unable to verify payment with the gateway. If your payment was deducted, please contact support.")
        return redirect("prep:billing")
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
            # Prevent duplicate credit grants for the same Paystack reference
            existing_tx = PrepTransaction.objects.filter(reference_code=reference).first()
            if not existing_tx:
                if package_type == "plan" and plan_id:
                    grant_subscription(wallet, plan_id, int(credits_to_add), reference_code=reference)
                else:
                    # Top-ups are open to all plans — no subscription gate
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


@never_cache
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
                from services.prep_ai_router import repair_question_and_solution_text
                repaired_q = repair_question_and_solution_text(q_obj.question_latex)
                if repaired_q != q_obj.question_latex:
                    q_obj.question_latex = repaired_q
                    q_obj.save(update_fields=["question_latex"])
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
                        "credits_balance": get_available_credits(wallet),
                    })
        except Exception:
            pass

    if not question_latex:
        return JsonResponse({"success": False, "error": "No question LaTeX provided."}, status=400)

    # Check allowance or credit balance before fresh AI call
    has_sub = has_active_subscription(wallet)
    allowance = get_remaining_practice_question_allowance(wallet) if has_sub else 0
    is_covered_by_plan = has_sub and allowance >= 1

    minimum_cost = 5
    required_balance = 0 if is_covered_by_plan else estimated_generation_credits(minimum=minimum_cost)
    if not is_covered_by_plan and get_available_credits(wallet) < required_balance:
        if wallet.current_plan == "freemium":
            err_msg = f"Insufficient credits. You need at least {required_balance} credits available on Freemium before generating a step-by-step verified solution. Please subscribe or top up."
        else:
            err_msg = f"You have used your monthly plan question allowance ({wallet.current_plan.title()}). At least {required_balance} credits are required to generate verified solutions. Please top up credits or upgrade to Pro."
        return JsonResponse({
            "success": False,
            "error": err_msg,
            "credits_balance": get_available_credits(wallet),
            "upgrade_required": True,
        }, status=402)

    # Call AI router (with DB cache layer)
    try:
        res = get_or_generate_question_solution(
            question_latex=question_latex,
            course_code=course_code or "Mathematics",
            topic_label=topic_label,
            question_obj=q_obj,
        )
    except Exception as exc:
        logger.error("Failed in get_or_generate_question_solution: %s", exc)
        return JsonResponse({"success": False, "error": "Unable to generate verified solution right now. Please try again shortly."}, status=500)

    if not res.get("solution"):
        return JsonResponse({"success": False, "error": res.get("error", "Failed to generate solution.")}, status=500)

    # If was cached, 0 credits deducted!
    credits_deducted = 0

    if not res.get("cached"):
        if is_covered_by_plan:
            credits_deducted = 0
            u_data = res.get("usage") if isinstance(res.get("usage"), dict) else {}
            in_tok = int(u_data.get("prompt_tokens") or u_data.get("input_tokens") or 0)
            out_tok = int(u_data.get("completion_tokens") or u_data.get("output_tokens") or 0)
            tot_tok = int(u_data.get("total_tokens") or (in_tok + out_tok))
            PrepTransaction.objects.create(
                wallet=wallet,
                amount=0,
                action_type="deep_reasoning",
                description=f"Verified Solution & Proof (Plan Allowance): {course_code} ({topic_label})",
                input_tokens=in_tok or None,
                output_tokens=out_tok or None,
                total_tokens=tot_tok or None,
                model_name=res.get("model", "deepseek-reasoner"),
                metadata={"covered_by_plan": True, "question_count": 1},
            )
        else:
            credits_deducted = credits_for_usage(res.get("usage"), minimum=minimum_cost)
            try:
                consume_credits(
                    wallet,
                    credits_deducted,
                    action_type="deep_reasoning",
                    description=f"Verified Solution & Proof: {course_code} ({topic_label})",
                    usage=res.get("usage"),
                    model_name=res.get("model", "deepseek-reasoner"),
                    metadata={"question_count": 1},
                )
            except InsufficientCredits:
                return JsonResponse({
                    "success": False,
                    "error": "The generated solution requires more credits than are currently available. Please subscribe or top up, then try again.",
                    "credits_balance": get_available_credits(wallet),
                }, status=402)

        # Downgrade trial → freemium immediately if credits are now zero
        from services.credit_service import check_and_downgrade_trial
        check_and_downgrade_trial(wallet)

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
        "credits_balance": get_available_credits(wallet),
        "model": res.get("model", "deepseek-reasoner"),
    })


@never_cache
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
        from services.prep_ai_router import repair_question_and_solution_text
        repaired_q = repair_question_and_solution_text(existing.question_latex)
        if repaired_q != existing.question_latex:
            existing.question_latex = repaired_q
            existing.save(update_fields=["question_latex"])
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
            "credits_balance": get_available_credits(wallet),
        })

    # Check allowance or credit balance before fresh AI call
    has_sub = has_active_subscription(wallet)
    allowance = get_remaining_practice_question_allowance(wallet) if has_sub else 0
    is_covered_by_plan = has_sub and allowance >= 1

    minimum_cost = 5
    required_balance = 0 if is_covered_by_plan else estimated_generation_credits(minimum=minimum_cost)
    if not is_covered_by_plan and get_available_credits(wallet) < required_balance:
        if wallet.current_plan == "freemium":
            err_msg = f"Insufficient credits. At least {required_balance} credits are required to reconstruct this question on Freemium. Please subscribe or top up."
        else:
            err_msg = f"You have used your monthly plan question allowance ({wallet.current_plan.title()}). At least {required_balance} credits are required to reconstruct this question. Please top up credits or upgrade to Pro."
        return JsonResponse({
            "success": False,
            "error": err_msg,
            "credits_balance": get_available_credits(wallet),
            "upgrade_required": True,
        }, status=402)

    try:
        result = generate_adapted_past_question(question)
    except Exception as exc:
        logger.error("Failed in generate_adapted_past_question: %s", exc)
        return JsonResponse({"success": False, "error": "Unable to adapt question at this time. Please try again shortly."}, status=500)
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

    credits_deducted = 0
    course_name = question.paper.course.code if question.paper else (question.topic.course.code if question.topic else "Course")
    t_label = question.topic_label or (target_topic.title if target_topic else (question.topic.title if question.topic else "Mathematics"))

    if is_covered_by_plan:
        credits_deducted = 0
        u_data = result.get("usage") if isinstance(result.get("usage"), dict) else {}
        in_tok = int(u_data.get("prompt_tokens") or u_data.get("input_tokens") or 0)
        out_tok = int(u_data.get("completion_tokens") or u_data.get("output_tokens") or 0)
        tot_tok = int(u_data.get("total_tokens") or (in_tok + out_tok))
        PrepTransaction.objects.create(
            wallet=wallet,
            amount=0,
            action_type="ai_practice_gen",
            description=f"Adapted Past Question (Plan Allowance): {course_name} - {t_label}",
            input_tokens=in_tok or None,
            output_tokens=out_tok or None,
            total_tokens=tot_tok or None,
            model_name=result.get("model", "deepseek-reasoner"),
            metadata={"source_question_id": question.id, "adapted": True, "covered_by_plan": True, "question_count": 1},
        )
    else:
        try:
            credits_deducted = credits_for_usage(result.get("usage"), minimum=minimum_cost)
            consume_credits(
                wallet,
                credits_deducted,
                action_type="ai_practice_gen",
                description=f"Adapted Past Question: {course_name} - {t_label}",
                usage=result.get("usage"),
                model_name=result.get("model", "deepseek-reasoner"),
                metadata={"source_question_id": question.id, "adapted": True, "question_count": 1},
            )
        except InsufficientCredits:
            return JsonResponse({
                "success": False,
                "error": "The adapted question requires more credits than are currently available.",
                "credits_balance": get_available_credits(wallet),
            }, status=402)

    # Downgrade trial → freemium immediately if credits are now zero
    from services.credit_service import check_and_downgrade_trial
    check_and_downgrade_trial(wallet)

    reconstruction_metadata = result.get("reconstruction_metadata")
    reconstruction_metadata = reconstruction_metadata if isinstance(reconstruction_metadata, dict) else {}
    model_confidence = reconstruction_metadata.get("model_confidence")
    auto_validated = (
        reconstruction_metadata.get("source_review_status") == "pass"
        and isinstance(model_confidence, (int, float))
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
        "credits_balance": get_available_credits(wallet),
    })


@never_cache
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

    # Note Access & Spending:
    # Level 2 (Core Concepts) is free for all students.
    # Level 1 (2 credits) and Level 3 (4 credits) are charged ONLY IF notes are present in cache.
    from services.prep_ai_router import get_published_topic_note_levels
    from services.prep_note_access import (
        unlock_topic_note_level,
        is_topic_note_unlocked,
        NOTE_LEVEL_CREDIT_COSTS,
        NOTE_LEVEL_LABELS,
    )

    published_notes = get_published_topic_note_levels(topic_obj, validated_only=False) if topic_obj else {}
    note_content = published_notes.get(level, "")

    if not note_content:
        # Check cache directly
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
            note_content = cached_res.get("notes", "") or cached_res.get("content", "")

    if not note_content:
        # Notes are absent / awaiting background preparation
        if topic_obj:
            PrepTopicNotesJob.objects.get_or_create(
                topic=topic_obj,
                level=level,
                defaults={"status": "pending", "course": topic_obj.course},
            )
        label = NOTE_LEVEL_LABELS.get(level, level)
        return JsonResponse({
            "success": False,
            "error": f"{label} notes are currently being prepared in the background or awaiting review. No credits were deducted.",
            "level": level,
            "credits_deducted": 0,
            "credits_balance": get_available_credits(wallet),
        }, status=200)

    # Notes ARE present! Attempt to unlock / deliver
    success, credits_deducted, error_msg = unlock_topic_note_level(
        request.user, topic_obj, level, note_content
    )

    if not success:
        return JsonResponse({
            "success": False,
            "error": error_msg,
            "level": level,
            "credits_deducted": 0,
            "credits_required": NOTE_LEVEL_CREDIT_COSTS.get(level, 0),
            "credits_balance": get_available_credits(wallet),
        }, status=402)

    wallet.refresh_from_db()
    return JsonResponse({
        "success": True,
        "notes": note_content,
        "level": level,
        "cached": True,
        "credits_deducted": credits_deducted,
        "credits_balance": get_available_credits(wallet),
        "already_unlocked": (credits_deducted == 0 and level != "level_2"),
        "model": "Published Shared Notes",
    })

    job_id = data.get("job_id")
    if job_id:
        if not topic_obj or not str(job_id).isdigit():
            return JsonResponse(
                {"success": False, "error": "Invalid notes generation job."},
                status=400,
            )
        job = PrepTopicNotesJob.objects.filter(
            pk=int(job_id),
            topic=topic_obj,
            level=level,
        ).first()
        if not job:
            return JsonResponse(
                {"success": False, "error": "Notes generation job was not found."},
                status=404,
            )
        if job.status in {"pending", "running"}:
            return JsonResponse(
                {
                    "success": True,
                    "pending": True,
                    "job_id": job.pk,
                    "status": job.status,
                    "level": level,
                },
                status=202,
            )
        if job.status == "failed":
            from services.prep_ai_router import get_published_topic_note_levels
            published_notes = get_published_topic_note_levels(topic_obj, validated_only=False) if topic_obj else {}
            if level in published_notes:
                wallet.refresh_from_db()
                return JsonResponse({
                    "success": True,
                    "notes": published_notes[level],
                    "level": level,
                    "cached": True,
                    "credits_deducted": credits_deducted,
                    "credits_balance": get_available_credits(wallet),
                    "model": "Published Shared Notes",
                })
            # If the failure was due to missing sources but approved sources now exist, auto-reset the job
            if "approved course material" in (job.last_error or "").lower() or "independent review" in (job.last_error or "").lower():
                from services.prep_ai_router import _approved_course_source_context
                if topic_obj and _approved_course_source_context(topic_obj.course, topic_obj.title):
                    logger.info("Auto-resetting failed topic notes job %s for topic %s now that approved sources are available", job.pk, topic_obj.pk)
                    job.status = "pending"
                    job.attempts = 0
                    job.last_error = ""
                    job.save(update_fields=["status", "attempts", "last_error", "started_at"])
                    return JsonResponse(
                        {
                            "success": True,
                            "pending": True,
                            "job_id": job.pk,
                            "status": "pending",
                            "level": level,
                        },
                        status=202,
                    )
            logger.error(
                "Topic notes job failed topic=%s level=%s job=%s: %s",
                topic_obj.pk,
                level,
                job.pk,
                job.last_error,
            )
            return JsonResponse(
                {
                    "success": False,
                    "error": "Notes could not be prepared right now. Please retry in a moment.",
                    "level": level,
                },
                status=502,
            )

    # Use the same published-level source that rendered the notes on the page.
    # Shared notes are returned only after this learner's course share is settled.
    from services.prep_ai_router import get_published_topic_note_levels
    published_notes = get_published_topic_note_levels(topic_obj, validated_only=False) if topic_obj else {}
    if level in published_notes:
        wallet.refresh_from_db()
        return JsonResponse({
            "success": True,
            "notes": published_notes[level],
            "level": level,
            "cached": True,
            "credits_deducted": credits_deducted,
            "credits_balance": get_available_credits(wallet),
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
            "credits_balance": get_available_credits(wallet),
        }, status=409)

    if cached_res.get("validation_failed") and not (
        cached_res.get("notes") or cached_res.get("content")
    ):
        return JsonResponse(
            {
                "success": False,
                "error": cached_res.get("error")
                or "These notes do not meet the approved topic requirements.",
            },
            status=422,
        )

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
                "credits_balance": get_available_credits(wallet),
            }, status=402)

        if topic_obj:
            from services.prep_ai_router import _topic_notes_cache_signature

            source_signature = _topic_notes_cache_signature(
                topic_obj.course,
                topic_obj,
                topic_title,
                subtopics,
            )
            if level in {"level_1", "level_3"}:
                level_two_job, level_two_created = PrepTopicNotesJob.objects.get_or_create(
                    topic=topic_obj,
                    level="level_2",
                    source_signature=source_signature,
                    defaults={"status": "pending"},
                )
                if not level_two_created and level_two_job.status == "failed":
                    level_two_job.status = "pending"
                    level_two_job.attempts = 0
                    level_two_job.last_error = ""
                    level_two_job.provider_usage = {}
                    level_two_job.model_name = ""
                    level_two_job.queued_at = timezone.now()
                    level_two_job.started_at = None
                    level_two_job.completed_at = None
                    level_two_job.save(update_fields=[
                        "status",
                        "attempts",
                        "last_error",
                        "provider_usage",
                        "model_name",
                        "queued_at",
                        "started_at",
                        "completed_at",
                    ])
            job, created = PrepTopicNotesJob.objects.get_or_create(
                topic=topic_obj,
                level=level,
                source_signature=source_signature,
                defaults={"status": "pending"},
            )
            if not created and job.status in {"failed", "complete"}:
                job.status = "pending"
                job.attempts = 0
                job.last_error = ""
                job.provider_usage = {}
                job.model_name = ""
                job.started_at = None
                job.completed_at = None
                job.queued_at = timezone.now()
                job.save(
                    update_fields=[
                        "status",
                        "attempts",
                        "last_error",
                        "provider_usage",
                        "model_name",
                        "started_at",
                        "completed_at",
                        "queued_at",
                    ]
                )
            return JsonResponse(
                {
                    "success": True,
                    "pending": True,
                    "job_id": job.pk,
                    "status": job.status,
                    "level": level,
                },
                status=202,
            )

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
            "credits_balance": get_available_credits(wallet),
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

        # Downgrade trial → freemium immediately if credits are now zero
        from services.credit_service import check_and_downgrade_trial
        check_and_downgrade_trial(wallet)

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
        "credits_balance": get_available_credits(wallet),
        "model": res.get("model", "deepseek-chat"),
    })


@never_cache
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

    # Check existing unseen generated questions in DB for this user
    from prep.models import PrepStudentQuestionUnlock
    already_unlocked_ids = set()
    if request.user.is_authenticated and topic_obj:
        already_unlocked_ids = set(
            PrepStudentQuestionUnlock.objects.filter(
                user=request.user,
                topic=topic_obj,
            ).values_list("question_id", flat=True)
        )

    existing_unseen_count = 0
    if topic_obj:
        from services.prep_ingestion import learner_visible_assessment_questions
        existing_unseen_count = len(learner_visible_assessment_questions(
            PrepQuestion.objects.filter(
                topic=topic_obj,
                question_type="generated",
                verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
            ).exclude(id__in=already_unlocked_ids)
        ))

    force_fresh = bool(data.get("force_fresh", False))
    existing_count = 0
    try:
        existing_count = int(data.get("existing_count", 0))
    except (ValueError, TypeError):
        existing_count = 0

    # If user already has variants displayed (existing_count > 0) or requested force_fresh,
    # generate a fresh batch of `count` questions.
    # Otherwise, if unseen variants exist in DB, fetch them at $0 cost.
    if force_fresh or existing_count > 0:
        fresh_needed = count
        should_force_fresh = True
    elif existing_unseen_count >= count:
        fresh_needed = 0
        should_force_fresh = False
    else:
        fresh_needed = count - existing_unseen_count
        should_force_fresh = False

    has_sub = has_active_subscription(wallet)
    allowance = get_remaining_practice_question_allowance(wallet) if has_sub else 0
    is_covered_by_plan = has_sub and allowance >= fresh_needed

    required_balance = 0 if is_covered_by_plan else estimated_generation_credits(minimum=max(1, fresh_needed))
    if fresh_needed > 0 and not is_covered_by_plan and get_available_credits(wallet) < required_balance:
        if wallet.current_plan == "freemium":
            err_msg = f"Generating fresh practice questions requires at least {required_balance} credits on Freemium. Please top up your credits or subscribe to a plan."
        else:
            err_msg = f"You have used your monthly plan question allowance ({wallet.current_plan.title()}). At least {required_balance} credits are required to generate additional practice questions. Please top up credits or upgrade to Pro."
        return JsonResponse({
            "success": False,
            "error": err_msg,
            "credits_balance": get_available_credits(wallet),
            "upgrade_required": True,
        }, status=402)

    try:
        res = generate_similar_practice_questions(
            course_code=course_code or "Course",
            topic_title=topic_title,
            question_count=count,
            authentic_samples=authentic_samples,
            topic_obj=topic_obj,
            course_obj=topic_obj.course if topic_obj else None,
            force_fresh=should_force_fresh,
            exclude_question_ids=list(already_unlocked_ids),
        )
    except Exception as exc:
        logger.error("Failed in generate_similar_practice_questions: %s", exc)
        return JsonResponse({"success": False, "error": "Unable to generate practice questions at this time. Please try again shortly."}, status=500)

    if not res.get("success"):
        return JsonResponse({
            "success": False,
            "error": res.get("error") or "Practice questions could not be generated at this time.",
        }, status=500)

    # Record newly delivered questions in PrepStudentQuestionUnlock so they persist on revisit
    delivered_questions = res.get("questions", [])
    if request.user.is_authenticated and topic_obj and delivered_questions:
        unlock_records = [
            PrepStudentQuestionUnlock(user=request.user, question_id=q["id"], topic=topic_obj)
            for q in delivered_questions if q.get("id")
        ]
        PrepStudentQuestionUnlock.objects.bulk_create(unlock_records, ignore_conflicts=True)

    fresh_count = res.get("fresh_generated_count", 0)
    credits_deducted = 0

    if fresh_count > 0:
        if is_covered_by_plan:
            credits_deducted = 0
            u_data = res.get("usage") if isinstance(res.get("usage"), dict) else {}
            in_tok = int(u_data.get("prompt_tokens") or u_data.get("input_tokens") or 0)
            out_tok = int(u_data.get("completion_tokens") or u_data.get("output_tokens") or 0)
            tot_tok = int(u_data.get("total_tokens") or (in_tok + out_tok))
            PrepTransaction.objects.create(
                wallet=wallet,
                amount=0,
                action_type="ai_practice_gen",
                description=f"Generated {fresh_count} Practice Questions (Plan Allowance): {course_code} - {topic_title}",
                input_tokens=in_tok or None,
                output_tokens=out_tok or None,
                total_tokens=tot_tok or None,
                model_name=res.get("model", "deepseek-chat"),
                metadata={"question_count": fresh_count, "covered_by_plan": True},
            )
        else:
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

        # Downgrade trial → freemium immediately if credits are now zero
        from services.credit_service import check_and_downgrade_trial
        check_and_downgrade_trial(wallet)

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
        "credits_balance": get_available_credits(wallet),
        "model": res.get("model", "deepseek-chat"),
    })


# ─── Step 7: LaTeX Document Exports (PDF & DOCX) ─────────────────────────────

from django.http import HttpResponse
from services.prep_export_service import (
    export_topic_notes_docx,
    export_paper_questions_pdf,
    export_paper_questions_docx,
)


def _download_topic_pdf_artifact(request, topic, artifact_type, level, filename, tab_query):
    from services.prep_pdf_artifacts import enqueue_topic_pdf_artifact, github_pdf_bytes

    try:
        artifact, _ = enqueue_topic_pdf_artifact(topic, artifact_type, level)
    except Exception:
        logger.exception(
            "Unable to queue/check %s PDF for topic %s.",
            artifact_type,
            topic.pk,
        )
        messages.error(request, "The PDF could not be checked right now. Please try again shortly.")
        return redirect(
            reverse("prep:topic_study", kwargs={"topic_id": topic.pk})
            + f"?tab={tab_query}"
        )

    has_good_version = bool(artifact.github_path and artifact.published_signature)
    can_serve = artifact.status == "ready" or (
        artifact.status in {"pending", "running", "failed"} and has_good_version
    )
    if can_serve and has_good_version:
        try:
            pdf_bytes = github_pdf_bytes(artifact.github_path)
            if not pdf_bytes.startswith(b"%PDF"):
                raise RuntimeError("GitHub returned an invalid PDF artifact.")
        except Exception:
            logger.exception(
                "Unable to download ready PDF artifact %s for topic %s.",
                artifact.pk,
                topic.pk,
            )
            try:
                enqueue_topic_pdf_artifact(topic, artifact_type, level, force=True)
            except Exception:
                logger.exception(
                    "Unable to requeue missing GitHub PDF artifact %s.",
                    artifact.pk,
                )
            return HttpResponse(
                "The saved PDF is temporarily unavailable. Please try again shortly.",
                status=503,
                content_type="text/plain; charset=utf-8",
            )
        response = HttpResponse(pdf_bytes, content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="{filename}"'
        response["Cache-Control"] = "private, no-store"
        if artifact.published_signature != artifact.source_signature:
            response["X-Prep-PDF-Stale"] = "true"
        return response

    if artifact.status == "empty":
        messages.info(
            request,
            "No validated content is available for this PDF yet. It will be prepared after the source content is ready.",
        )
    elif artifact.status == "failed":
        messages.error(
            request,
            "PDF preparation failed. The preparation worker will retry; please try again later.",
        )
    else:
        messages.info(
            request,
            "Your PDF is being prepared in the background. Please try downloading it again shortly.",
        )
    return redirect(
        reverse("prep:topic_study", kwargs={"topic_id": topic.pk})
        + f"?tab={tab_query}"
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
        if fmt.lower() == "pdf":
            return _download_topic_pdf_artifact(
                request,
                topic,
                "questions",
                "",
                f"{topic.course.code}_{topic.slug}_past_questions_answers.pdf",
                "questions_answers",
            )
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
    if fmt.lower() == "pdf":
        if not topic:
            return HttpResponse("The requested syllabus topic was not found.", status=404)
        # Gate Level 1 and Level 3 PDF downloads behind note unlock check.
        # Level 2 is always free. Staff / superusers bypass the gate.
        if level in {"level_1", "level_3"} and not (
            request.user.is_staff or request.user.is_superuser
        ):
            from services.prep_note_access import is_topic_note_unlocked
            if not is_topic_note_unlocked(request.user, topic, level):
                level_label = {
                    "level_1": "Foundation & Intuition",
                    "level_3": "Exam Focus",
                }.get(level, level)
                messages.warning(
                    request,
                    f"Please open the {level_label} notes on the study page first to unlock this PDF download.",
                )
                return redirect(
                    reverse("prep:topic_study", kwargs={"topic_id": topic_id})
                    + f"?tab=notes&level={level}"
                )
        return _download_topic_pdf_artifact(
            request,
            topic,
            "notes",
            level,
            f"{topic.course.code}_{topic.slug}_{level}_notes.pdf",
            f"notes&level={level}",
        )

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

    try:
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
    except Exception as exc:
        logger.error("Failed to generate topic export (%s): %s", fmt, exc)
        messages.error(request, f"Unable to generate {fmt.upper()} export at this time. Please try again.")
        if topic:
            return redirect("prep:topic_study", topic_id=topic.id)
        return redirect("prep:dashboard")


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
        question_type__in=("authentic", "adapted"),
        verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES
    ).exists():
        from services.prep_ingestion import learner_visible_assessment_questions

        for q in learner_visible_assessment_questions(
            paper.questions.filter(
                question_type__in=("authentic", "adapted"),
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

    try:
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
    except Exception as exc:
        logger.error("Failed to generate paper export (%s): %s", fmt, exc)
        messages.error(request, f"Unable to generate {fmt.upper()} export for this past paper at this time. Please try again.")
        return redirect("prep:paper_detail", course_code=course_code, paper_id=paper_id)


@never_cache
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


@never_cache
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
    credits = 0
    if request.user.is_authenticated:
        wallet = PrepWallet.get_or_create_wallet(request.user)
        credits = get_available_credits(wallet)
    context = {
        "active_tab": "terms",
        "user_credits": credits,
    }
    resp = render(request, "prep/terms.html", context)
    return set_prep_cache_headers(
        resp,
        max_age=1800,
        is_public=not request.user.is_authenticated,
        is_authenticated=request.user.is_authenticated,
    )


def prep_privacy(request):
    """Mentify Prep Privacy Policy."""
    credits = 0
    if request.user.is_authenticated:
        wallet = PrepWallet.get_or_create_wallet(request.user)
        credits = get_available_credits(wallet)
    context = {
        "active_tab": "privacy",
        "user_credits": credits,
    }
    resp = render(request, "prep/privacy.html", context)
    return set_prep_cache_headers(
        resp,
        max_age=1800,
        is_public=not request.user.is_authenticated,
        is_authenticated=request.user.is_authenticated,
    )


@never_cache
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
    try:
        ai_response = generate_prep_chat_response(messages_history=history, user_message=user_message, user=user)
    except Exception as exc:
        logger.error("Prep assistant chat error: %s", exc)
        ai_response = "The Mentify Prep Assistant encountered a momentary issue. Please try again shortly or explore your [Courses & Syllabi](/prep/courses/) directly."

    # Save last 10 turns to session
    updated_history = history + [
        {"role": "user", "text": user_message},
        {"role": "model", "text": ai_response},
    ]
    request.session["prep_chat_history"] = updated_history[-10:]

    return JsonResponse({"status": "success", "response": ai_response})
