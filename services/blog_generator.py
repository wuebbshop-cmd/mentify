import email.utils
import hashlib
import json
import logging
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import timedelta
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify

from blog.models import Category, Post
from services.prep_ai_router import call_deepseek

logger = logging.getLogger(__name__)

CATEGORY_BEATS = {
    "ai-automation": {
        "name": "AI & Automation",
        "query": "Artificial Intelligence OR open-source LLM OR AI agents OR DeepSeek OR Anthropic OR machine learning when:2d",
        "focus": "Global foundation models, open weights, AI agent frameworks, system architectures, and practical deployment.",
        "personas": [
            "Senior AI Systems Engineer",
            "Machine Learning Infrastructure Architect",
            "Open-Source AI Contributor",
            "Mentify AI Research Desk",
        ],
        "image_keywords": "artificial-intelligence,neural-network,server-code",
    },
    "programming-tech": {
        "name": "Programming & Tech",
        "query": "Python programming OR Rust language OR cloud architecture OR Kubernetes OR distributed systems when:2d",
        "focus": "Backend engineering, language performance, distributed systems, developer productivity, and cloud tooling.",
        "personas": [
            "Staff Backend Engineer",
            "Cloud Infrastructure Architect",
            "Systems Programmer",
            "Mentify Dev Lab",
        ],
        "image_keywords": "coding,programming,technology,data-center",
    },
    "career-industry": {
        "name": "Career & Industry",
        "query": "remote tech jobs OR software developers Kenya OR fintech Africa OR tech careers when:2d",
        "focus": "Global remote software work realities, African tech ecosystem shifts, developer compensation, and fintech infrastructure.",
        "personas": [
            "Tech Career Strategist",
            "Remote Engineering Consultant",
            "African Tech Ecosystem Analyst",
            "Mentify Career Insights",
        ],
        "image_keywords": "modern-office,tech-workspace,entrepreneur,laptop",
    },
    "academia": {
        "name": "Academia",
        "query": "Kenya university OR HELB university OR higher education OR graduate scholarships when:2d",
        "focus": "Kenyan university education dynamics, higher education financing (HEF/HELB), academic reforms, and global student scholarships.",
        "personas": [
            "Higher Education Policy Analyst",
            "Academic Research Fellow",
            "Scholarship & Graduate Advisor",
            "Mentify Academic Desk",
        ],
        "image_keywords": "university,graduation,library,academic-books",
    },
}

STOP_WORDS = {
    "a", "an", "the", "and", "or", "in", "on", "at", "to", "for", "of", "with",
    "by", "from", "up", "about", "into", "over", "after", "is", "are", "was", "were",
    "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "if",
    "because", "as", "until", "while", "how", "what", "which", "who", "when",
    "where", "why", "new", "latest", "update", "updates", "report", "reports",
    "says", "announces", "launches", "unveils", "reveals", "plans", "first",
    "more", "than", "will", "would", "could", "should", "their", "there", "they"
}


def _extract_keywords(text: str) -> set[str]:
    """Extract normalized alphanumeric keyword tokens of length >= 3 excluding stop words."""
    tokens = re.findall(r"[A-Za-z0-9]+", (text or "").lower())
    return {t for t in tokens if len(t) >= 3 and t not in STOP_WORDS}


def _sanitize_cliches(text: str) -> str:
    """Sanitize and remove clichéd AI tropes, contrasting paradoxes, em-dashes, and gimmicky headings."""
    if not text:
        return text

    # Remove em-dashes (\u2014) and en-dashes (\u2013)
    text = re.sub(r"(\d)\s*[\u2013\u2014]\s*(\d)", r"\1-\2", text)
    text = re.sub(r"\s*[\u2014]\s*", " - ", text)
    text = re.sub(r"\s*[\u2013]\s*", " - ", text)

    patterns = [
        (re.compile(r"###?\s+Why (.*?) Is a Feature, Not a Bug", re.IGNORECASE), r"### Structural Dynamics of \1"),
        (re.compile(r"Is a Feature, Not a Bug", re.IGNORECASE), "Operates by Design"),
        (re.compile(r"A Feature, Not a Bug", re.IGNORECASE), "An Architectural Trade-Off"),
        (re.compile(r"###?\s+The (.*?) Paradox: Why (.*)", re.IGNORECASE), r"### Architectural Trade-offs in \1"),
        (re.compile(r"It('?s| is) not about ([^,;]+)[,;]\s*it('?s| is) about", re.IGNORECASE), r"Beyond \2, the focus centers on"),
    ]
    cleaned = text
    for pat, repl in patterns:
        cleaned = pat.sub(repl, cleaned)
    return cleaned


UNSPLASH_FALLBACK_POOLS = {
    "ai-automation": [
        "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1531746790731-6c087fecd65a?auto=format&fit=crop&w=1200&q=80",
    ],
    "programming-tech": [
        "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1542831371-29b0f74f9713?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1504639725590-34d0984388bd?auto=format&fit=crop&w=1200&q=80",
    ],
    "career-industry": [
        "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=1200&q=80",
    ],
    "academia": [
        "https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&w=1200&q=80",
    ],
}


def resolve_blog_preview_image(
    headline: dict,
    tags: str = "",
    category_slug: str = "ai-automation",
    image_prompt: str = "",
) -> str:
    """
    Hybrid preview image resolution:
    1. Try to extract authentic og:image from the source article URL if directly accessible.
    2. Generate a custom, story-specific AI editorial banner (Pollinations 1200x630) matching the exact headline.
    3. Fallback to a diverse curated pool of high-res Unsplash photography per category.
    """
    title = headline.get("title", "")
    link = headline.get("link", "")

    # Tier 1: Authentic publisher og:image (if direct URL, avoiding Google consent walls)
    if link and not ("google.com" in link and "rss/articles" in link):
        try:
            req = urllib.request.Request(
                link,
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"},
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
                m = re.search(
                    r'<meta[^>]+(?:property|name)=[\'"](?:og:image|twitter:image)[\'"][^>]+content=[\'"]([^\'"]+)[\'"]',
                    html,
                    re.I,
                )
                if not m:
                    m = re.search(
                        r'<meta[^>]+content=[\'"]([^\'"]+)[\'"][^>]+(?:property|name)=[\'"](?:og:image|twitter:image)[\'"]',
                        html,
                        re.I,
                    )
                if m:
                    og_url = m.group(1).strip()
                    if og_url.startswith("http") and not any(
                        p in og_url.lower() for p in ("1x1", "favicon", "avatar", "icon", "placeholder")
                    ):
                        logger.info(f"[Blog Generator] Resolved authentic og:image for '{title[:40]}'")
                        return og_url
        except Exception:
            pass

    # Tier 2: AI Editorial Banner generated specifically for this headline & topic
    try:
        seed = int(hashlib.md5(title.encode()).hexdigest(), 16) % 100000
        subject = image_prompt or f"{title}, {tags}"
        clean_subj = re.sub(r'["\'\(\)\{\}\[\]\n\r]', ' ', subject).strip()
        visual_prompt = f"modern editorial tech journalism illustration, {clean_subj}, cinematic lighting, sleek 3d graphic, high resolution 8k"
        encoded_prompt = urllib.parse.quote(visual_prompt[:180])
        ai_banner_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1200&height=630&nologo=true&seed={seed}"
        return ai_banner_url
    except Exception as e:
        logger.warning(f"[Blog Generator] AI banner generation failed: {e}")

    # Tier 3: Curated diversified fallback photo pool
    pool = UNSPLASH_FALLBACK_POOLS.get(category_slug, UNSPLASH_FALLBACK_POOLS["ai-automation"])
    idx = int(hashlib.md5(title.encode()).hexdigest(), 16) % len(pool)
    return pool[idx]


def fetch_live_headlines(query: str, limit: int = 10) -> list[dict]:
    """
    Fetch live, real-time news headlines with URLs from RSS feeds.
    Strictly filters out any articles older than 2 days (48 hours).
    """
    encoded_q = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={encoded_q}&hl=en-US&gl=US&ceid=US:en"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"},
    )
    headlines = []
    now = timezone.now()
    two_days_ago = now - timedelta(days=2)

    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            tree = ET.fromstring(response.read())
            for item in tree.findall(".//item"):
                title_elem = item.find("title")
                link_elem = item.find("link")
                date_elem = item.find("pubDate")
                source_elem = item.find("source")

                title = title_elem.text.strip() if title_elem is not None and title_elem.text else ""
                link = link_elem.text.strip() if link_elem is not None and link_elem.text else ""
                pub_date_str = date_elem.text.strip() if date_elem is not None and date_elem.text else ""
                source_name = source_elem.text.strip() if source_elem is not None and source_elem.text else ""

                if not title or len(title) < 15:
                    continue

                # Strict freshness validation: reject items older than 2 days (48 hours)
                if pub_date_str:
                    try:
                        pub_dt = email.utils.parsedate_to_datetime(pub_date_str)
                        if pub_dt and pub_dt < two_days_ago:
                            logger.info(f"[Blog Generator] Skipping headline older than 48h '{title}' ({pub_date_str})")
                            continue
                    except Exception:
                        pass

                clean_title = re.sub(r"\s+-\s+[^-]+$", "", title).strip()

                headlines.append({
                    "title": clean_title,
                    "raw_title": title,
                    "link": link,
                    "pub_date": pub_date_str,
                    "source": source_name,
                })
                if len(headlines) >= limit:
                    break
    except Exception as exc:
        logger.warning(f"[Blog Generator] Failed fetching live headlines for '{query}': {exc}")
    return headlines


def _get_target_db() -> str:
    return "substitute" if "substitute" in getattr(settings, "DATABASES", {}) else "default"


def _is_headline_already_covered(
    headline: dict,
    db_alias: str,
    session_seen_keywords: list[set[str]] | None = None,
    session_seen_links: set[str] | None = None,
) -> bool:
    """
    Check if the headline or a close topical variation has already been published
    in the database or within the current running batch.
    """
    title = headline.get("title", "").strip()
    link = headline.get("link", "").strip()

    if session_seen_links and link and link in session_seen_links:
        logger.info(f"[Blog Generator] Duplicate link in current batch: {link}")
        return True

    cand_keywords = _extract_keywords(title)
    if not cand_keywords:
        return True

    # Check against in-batch seen keywords
    if session_seen_keywords:
        for seen_kw in session_seen_keywords:
            overlap = cand_keywords & seen_kw
            if len(overlap) >= 3 or (len(overlap) >= 2 and len(overlap) / max(1, len(cand_keywords)) >= 0.4):
                logger.info(f"[Blog Generator] Skipping '{title}' - overlaps with batch topic {overlap}")
                return True

    # Query all existing posts in db_alias (no time cutoff to prevent any duplicate ever)
    existing_posts = list(Post.objects.using(db_alias).all().values("title", "slug", "markdown_content", "excerpt"))
    cand_slug = slugify(title)

    for p in existing_posts:
        p_title = p["title"]
        p_slug = p["slug"]

        if cand_slug and (cand_slug == p_slug or (len(cand_slug) > 10 and (cand_slug in p_slug or p_slug in cand_slug))):
            logger.info(f"[Blog Generator] Slug conflict for '{title}' vs '{p_title}'")
            return True

        p_keywords = _extract_keywords(p_title)
        overlap = cand_keywords & p_keywords
        union = cand_keywords | p_keywords
        jaccard = len(overlap) / max(1, len(union))

        if len(overlap) >= 3 or jaccard >= 0.35:
            logger.info(f"[Blog Generator] Skipping duplicate headline '{title}' - matches existing post '{p_title}' (overlap: {overlap})")
            return True

        # Check if source URL already cited in article body
        if link and (link in (p.get("markdown_content") or "") or link in (p.get("excerpt") or "")):
            logger.info(f"[Blog Generator] Source link already cited in post '{p_title}'")
            return True

    return False


def generate_single_blog_post(
    category_slug: str,
    headline: dict,
    author_persona: str,
    db_alias: str | None = None,
) -> Post | None:
    """
    Generate an authentic, highly technical, and human-style blog post for a headline
    and persist it to the substitute database.
    """
    if db_alias is None:
        db_alias = _get_target_db()

    beat = CATEGORY_BEATS.get(category_slug, CATEGORY_BEATS["ai-automation"])
    category_obj = Category.objects.using(db_alias).filter(slug=category_slug).first()
    if not category_obj:
        category_obj = Category.objects.using(db_alias).first()

    current_date_str = timezone.now().strftime("%B %d, %Y")

    system_prompt = (
        "You are a distinguished technical staff engineer, investigative tech journalist, and lead architectural essayist "
        "writing for Mentify (https://mlaudit.info/blog/). Mentify is an engineering and academic tech hub.\n\n"
        "EDITORIAL & WRITING STANDARDS (MANDATORY FOR NATURAL HUMAN WRITING):\n"
        f"1. CURRENT CALENDAR DATE: {current_date_str}. All news context, timelines, and references must reflect breaking developments "
        f"from THE LAST 48 HOURS ({current_date_str}). NEVER invent past dates or reference events as happening in past months.\n"
        "2. NEVER use repetitive, cookie-cutter section headings. STRICTLY FORBIDDEN: 'TL;DR', 'The Breakdown', 'Why It Matters', "
        "'Conclusion', 'Summary', 'Deep Dive', or 'Looking Ahead' as section titles.\n"
        "3. NO CONTRASTING OR PARADOXICAL AI CLICHÉS. STRICTLY FORBIDDEN: Tropes like 'Why X is a feature, not a bug', "
        "'X is not what you think', 'The [Noun] Paradox', 'It is not about X, it is about Y', 'Double-edged sword', "
        "or pseudo-philosophical antithesis statements in headings or body text. Headings must be grounded, authoritative, "
        "and descriptive technical statements (e.g. 'Market Saturation and Compensation Distribution in Python' or 'Memory Overhead in Hot Loop Transpilation').\n"
        "4. STRICT PUNCTUATION RULE (ZERO EM DASHES): NEVER use em dashes (—) or en dashes (–) anywhere in the article. "
        "Instead, use natural human punctuation: commas, parentheses, colons, semicolons, standard hyphens (-), or periods.\n"
        "5. Invent STORY-SPECIFIC, insightful Markdown subheadings (H2, H3) that describe the actual mechanics, trade-offs, and technical specifics.\n"
        "6. Write with depth, voice, and narrative rhythm. Vary sentence length and structure. Avoid AI clichés like 'In this fast-paced world', "
        "'A testament to', 'Delve into', or 'Exciting times ahead'.\n"
        "7. Include concrete technical context: architectures, memory trade-offs, latency numbers, benchmarks, or command-line/code snippets where appropriate.\n"
        "8. Naturally integrate verified external references to the primary news source and related documentation using Markdown hyperlinks.\n"
        "9. Return strictly valid JSON containing: 'title', 'slug', 'excerpt', 'markdown_content', 'tags', 'author_name', 'image_prompt'."
    )

    user_prompt = (
        f"Write an original, comprehensive technical article (1,200 to 1,800 words in Markdown) covering this breaking development from the past 48 hours ({current_date_str}):\n\n"
        f"HEADLINE: {headline['title']}\n"
        f"PRIMARY SOURCE: {headline.get('source', 'Industry Report')}\n"
        f"SOURCE URL: {headline['link']}\n"
        f"PUBLISHED DATE: {headline.get('pub_date', current_date_str)}\n"
        f"CATEGORY BEAT: {beat['name']} - {beat['focus']}\n"
        f"AUTHOR PERSONA: {author_persona}\n\n"
        "JSON OUTPUT REQUIREMENTS:\n"
        "{\n"
        '  "title": "Punchy, authoritative, non-clickbait title",\n'
        '  "slug": "url-friendly-lowercase-slug-without-trailing-punctuation",\n'
        '  "excerpt": "2-3 crisp sentences summarizing the technical breakthrough for social share cards",\n'
        '  "tags": "3 to 5 comma-separated tags (e.g. LLMs, Open Source, DeepSeek, Cloud)",\n'
        '  "author_name": "Author name matching the persona",\n'
        '  "image_prompt": "10-15 word visual description of an editorial cover illustration depicting the technical core of this article",\n'
        '  "markdown_content": "Full article body in Markdown with custom H2/H3 headings, code/tables where relevant, and markdown citations."\n'
        "}\n\n"
        "Return ONLY the JSON object. Do not wrap in markdown fences or include explanations."
    )

    result = call_deepseek(
        [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        model="deepseek-chat",
        max_tokens=3500,
        temperature=0.35,
        thinking_enabled=False,
    )

    if not result.get("success") or not result.get("content"):
        logger.error(f"[Blog Generator] DeepSeek call failed for {headline['title']}: {result.get('error')}")
        return None

    raw_text = str(result["content"]).strip()
    raw_text = re.sub(r"^```(?:json)?\s*", "", raw_text, flags=re.IGNORECASE)
    raw_text = re.sub(r"\s*```$", "", raw_text)

    try:
        data = json.loads(raw_text)
    except Exception:
        match = re.search(r"\{[\s\S]*\}", raw_text)
        if match:
            try:
                data = json.loads(match.group(0))
            except Exception as e:
                logger.error(f"[Blog Generator] Failed parsing JSON payload: {e}")
                return None
        else:
            return None

    title = _sanitize_cliches(str(data.get("title") or headline["title"]).strip())
    slug = slugify(str(data.get("slug") or title))[:220]
    excerpt = _sanitize_cliches(str(data.get("excerpt") or "").strip()[:480])
    markdown_content = _sanitize_cliches(str(data.get("markdown_content") or "").strip())
    tags = str(data.get("tags") or "").strip()[:240]
    author_name = str(data.get("author_name") or author_persona).strip()
    image_prompt = str(data.get("image_prompt") or "").strip()

    if not markdown_content or len(markdown_content) < 400:
        logger.warning(f"[Blog Generator] Incomplete content returned for {title}")
        return None

    featured_image = resolve_blog_preview_image(
        headline=headline,
        tags=tags,
        category_slug=category_slug,
        image_prompt=image_prompt,
    )

    base_slug = slug
    counter = 1
    while Post.objects.using(db_alias).filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    post = Post.objects.using(db_alias).create(
        title=title,
        slug=slug,
        excerpt=excerpt,
        markdown_content=markdown_content,
        featured_image_url=featured_image,
        author=None,
        author_display_name=author_name,
        category=category_obj,
        tags=tags,
        is_published=True,
        is_featured=False,
        published_at=timezone.now(),
    )
    logger.info(f"[Blog Generator] Published new post: '{post.title}' ({post.slug}) in {category_obj.name} on {db_alias}")
    return post


def run_daily_blog_batch(target_count: int = 4, db_alias: str | None = None) -> list[Post]:
    """
    Execute daily batch to generate at least `target_count` articles across the active categories.
    If a category has no fresh headline, dynamically reallocates to another high-signal category.
    Strictly avoids duplicates against the database and within the batch.
    """
    if db_alias is None:
        db_alias = _get_target_db()

    categories = ["ai-automation", "programming-tech", "career-industry", "academia"]
    created_posts = []
    session_seen_keywords: list[set[str]] = []
    session_seen_links: set[str] = set()

    candidates_by_category = {}
    for cat_slug in categories:
        beat = CATEGORY_BEATS[cat_slug]
        headlines = fetch_live_headlines(beat["query"], limit=10)
        fresh_headlines = [
            h for h in headlines if not _is_headline_already_covered(
                h, db_alias, session_seen_keywords, session_seen_links
            )
        ]
        candidates_by_category[cat_slug] = fresh_headlines

    # Pass 1: Try to publish 1 post per category
    for cat_slug in categories:
        if len(created_posts) >= target_count:
            break
        fresh = candidates_by_category.get(cat_slug, [])
        while fresh:
            candidate = fresh.pop(0)
            if _is_headline_already_covered(candidate, db_alias, session_seen_keywords, session_seen_links):
                continue
            persona = CATEGORY_BEATS[cat_slug]["personas"][len(created_posts) % len(CATEGORY_BEATS[cat_slug]["personas"])]
            post = generate_single_blog_post(cat_slug, candidate, persona, db_alias=db_alias)
            if post:
                created_posts.append(post)
                session_seen_keywords.append(_extract_keywords(post.title))
                if candidate.get("link"):
                    session_seen_links.add(candidate["link"])
                break

    # Pass 2: If we still need posts (e.g. a category was empty), dynamically reallocate
    fallback_priority = ["ai-automation", "programming-tech", "career-industry", "academia"]
    while len(created_posts) < target_count:
        made_progress = False
        for cat_slug in fallback_priority:
            fresh = candidates_by_category.get(cat_slug, [])
            while fresh and len(created_posts) < target_count:
                candidate = fresh.pop(0)
                if _is_headline_already_covered(candidate, db_alias, session_seen_keywords, session_seen_links):
                    continue
                persona = CATEGORY_BEATS[cat_slug]["personas"][(len(created_posts) + 1) % len(CATEGORY_BEATS[cat_slug]["personas"])]
                post = generate_single_blog_post(cat_slug, candidate, persona, db_alias=db_alias)
                if post:
                    created_posts.append(post)
                    session_seen_keywords.append(_extract_keywords(post.title))
                    if candidate.get("link"):
                        session_seen_links.add(candidate["link"])
                    made_progress = True
                    break
            if len(created_posts) >= target_count:
                break
        if not made_progress:
            break

    return created_posts
