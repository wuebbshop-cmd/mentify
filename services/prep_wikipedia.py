import logging
import re
from urllib.parse import quote
import requests

logger = logging.getLogger(__name__)

WIKIPEDIA_USER_AGENT = "Mentify/1.0 (https://mentify.study; contact: support@mentify.study)"


def extract_youtube_id(url: str) -> str:
    """Extract YouTube video ID from various standard YouTube URL formats."""
    if not url or not isinstance(url, str):
        return ""
    clean_url = url.strip()
    patterns = [
        r"(?:https?:\/\/)?(?:www\.|m\.)?youtube\.com\/watch\?(?:.*&)?v=([a-zA-Z0-9_-]{11})",
        r"(?:https?:\/\/)?youtu\.be\/([a-zA-Z0-9_-]{11})",
        r"(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]{11})",
        r"(?:https?:\/\/)?(?:www\.)?youtube\.com\/v\/([a-zA-Z0-9_-]{11})",
        r"(?:https?:\/\/)?(?:www\.|m\.)?youtube\.com\/shorts\/([a-zA-Z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, clean_url)
        if match:
            return match.group(1)
    return ""


def clean_topic_title_for_wiki(raw_title: str) -> str:
    """Strip common syllabus prefixes like 'Topic 1 -', 'Unit 2:', 'Chapter 3.' for better Wikipedia matching."""
    if not raw_title:
        return ""
    cleaned = raw_title.strip()
    # Strip prefixes like "Topic 1:", "Unit 2 -", "Week 3:"
    cleaned = re.sub(r"^(?:Topic|Unit|Chapter|Week|Module|Lesson)\s*\d+[:\-\.]\s*", "", cleaned, flags=re.IGNORECASE)
    # Strip course codes like "SMA 203:" or "CS101 -"
    cleaned = re.sub(r"^[A-Z]{2,4}\s*\d{3,4}[:\-\.]\s*", "", cleaned)
    # Remove leading numbering like "1. ", "1.2 "
    cleaned = re.sub(r"^\d+(?:\.\d+)*[:\-\.]\s*", "", cleaned)
    return cleaned.strip() or raw_title.strip()


def get_or_fetch_wikipedia_summary(topic):
    """
    Retrieves cached Wikipedia concept entry for a topic, or queries Wikimedia REST API.
    Complies with Wikimedia API User-Agent policy and caches results permanently in the DB.
    Guaranteed zero-cost, non-blocking fallback on any error.
    """
    from prep.models import PrepTopicWikipedia

    if not topic or not getattr(topic, "pk", None):
        return None

    # 1. Return cached entry if already fetched
    existing = PrepTopicWikipedia.objects.filter(topic=topic).first()
    if existing:
        return existing

    topic_title = clean_topic_title_for_wiki(topic.title)
    if not topic_title:
        return None

    session = requests.Session()
    session.headers.update({
        "User-Agent": WIKIPEDIA_USER_AGENT,
        "Accept": "application/json",
    })

    candidate_title = topic_title
    try:
        # 2. Try direct Wikipedia REST summary API
        encoded_slug = quote(candidate_title.replace(" ", "_"), safe="_")
        summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded_slug}"
        resp = session.get(summary_url, timeout=3.5)

        # 3. Fallback to Wikimedia Search API if direct title was 404 or missing
        if resp.status_code == 404 or not resp.ok:
            search_query = topic_title
            if topic.course and getattr(topic.course, "title", None):
                search_query = f"{topic_title} {topic.course.title}"
            
            search_url = "https://en.wikipedia.org/w/api.php"
            params = {
                "action": "query",
                "list": "search",
                "srsearch": search_query,
                "utf8": 1,
                "format": "json",
                "srlimit": 1,
            }
            search_resp = session.get(search_url, params=params, timeout=3.5)
            if search_resp.ok:
                items = search_resp.json().get("query", {}).get("search", [])
                if items:
                    candidate_title = items[0]["title"]
                    encoded_slug = quote(candidate_title.replace(" ", "_"), safe="_")
                    summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded_slug}"
                    resp = session.get(summary_url, timeout=3.5)

        if resp.ok:
            data = resp.json()
            extract = data.get("extract", "").strip()
            if extract:
                thumbnail_url = (data.get("thumbnail") or {}).get("source", "")
                page_url = (
                    (data.get("content_urls") or {}).get("desktop", {}).get("page")
                    or f"https://en.wikipedia.org/wiki/{candidate_title.replace(' ', '_')}"
                )
                description = data.get("description", "")[:250]
                wiki_title = data.get("title") or candidate_title

                entry, _ = PrepTopicWikipedia.objects.get_or_create(
                    topic=topic,
                    defaults={
                        "wikipedia_title": wiki_title,
                        "extract": extract,
                        "canonical_url": page_url,
                        "thumbnail_url": thumbnail_url,
                        "description": description,
                    },
                )
                return entry
    except Exception as exc:
        logger.warning("Could not retrieve Wikipedia summary for topic %s: %s", topic.pk, exc)

    return None
