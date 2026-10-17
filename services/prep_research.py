import logging
import re
import requests
from urllib.parse import quote

logger = logging.getLogger(__name__)

ACADEMIC_USER_AGENT = "MentifyAcademic/1.0 (https://mentify.study; contact: support@mentify.study)"

_GENERIC_STOP_WORDS = {
    "introduction", "intro", "basics", "basic", "overview", "chapter", "lecture",
    "unit", "concept", "concepts", "study", "studies", "principles", "principle",
    "part", "fundamentals", "fundamental", "applied", "application", "applications",
    "theory", "general", "advanced", "course", "notes", "tutorial",
}


def _extract_core_keywords(text: str) -> set:
    """Extracts distinctive content words from topic title for relevance validation."""
    words = re.findall(r'[a-zA-Z]{3,}', (text or "").lower())
    return {w for w in words if w not in _GENERIC_STOP_WORDS}


def _reconstruct_openalex_abstract(inverted_index) -> str:
    """Reconstructs readable text from OpenAlex's abstract_inverted_index format."""
    if not isinstance(inverted_index, dict) or not inverted_index:
        return ""
    try:
        pos_map = {}
        for word, positions in inverted_index.items():
            for pos in positions:
                pos_map[pos] = word
        sorted_words = [pos_map[i] for i in sorted(pos_map.keys())]
        abstract = " ".join(sorted_words).strip()
        if len(abstract) > 400:
            return abstract[:397] + "..."
        return abstract
    except Exception:
        return ""


COMMERCIAL_PUBLISHER_DOMAINS = (
    "sciencedirect.com",
    "springer.com",
    "wiley.com",
    "jstor.org",
    "ieee.org",
    "tandfonline.com",
    "sagepub.com",
    "nature.com",
    "oup.com",
    "cambridge.org",
    "cell.com",
)


def _resolve_safe_paper_urls(raw_pdf_url: str, canonical_url: str, doi: str, arxiv_id: str = ""):
    """
    Resolves a reliable reading URL and a canonical DOI / landing page URL.
    - If arXiv ID or trusted open repository (PMC, bioRxiv, DOAJ) is present, prioritizes direct free access.
    - If a commercial publisher URL (Elsevier, Springer, Wiley) has a direct /pdf link that produces
      blank 403 pages, falls back to the canonical abstract/landing page or DOI so students can access it
      or view institutional access options.
    """
    clean_pdf = (raw_pdf_url or "").strip()
    clean_canonical = (canonical_url or "").strip()
    clean_doi = (doi or "").strip()

    doi_url = ""
    if clean_doi:
        if clean_doi.startswith("http://") or clean_doi.startswith("https://"):
            doi_url = clean_doi
        else:
            doi_url = f"https://doi.org/{clean_doi}"

    # If arXiv is available, arXiv PDF and abstract are 100% permanently free
    if arxiv_id:
        clean_aid = arxiv_id.replace("arXiv:", "").strip()
        return f"https://arxiv.org/pdf/{clean_aid}.pdf", f"https://arxiv.org/abs/{clean_aid}"

    is_trusted_open = any(domain in clean_pdf.lower() for domain in (
        "arxiv.org", "ncbi.nlm.nih.gov/pmc", "europepmc.org", "biorxiv.org",
        "medrxiv.org", "doaj.org", "zenodo.org", "hal.science", "osf.io", "semanticscholar.org"
    ))

    is_commercial_hotlink = any(domain in clean_pdf.lower() for domain in COMMERCIAL_PUBLISHER_DOMAINS)

    if is_commercial_hotlink:
        # Avoid naked publisher .pdf hotlinks which return blank 403s on referrers
        reading_url = clean_canonical or doi_url or clean_pdf
    elif is_trusted_open or clean_pdf:
        reading_url = clean_pdf or clean_canonical or doi_url
    else:
        reading_url = clean_canonical or doi_url

    canonical_final = doi_url or clean_canonical or reading_url
    return reading_url, canonical_final


def _is_paper_relevant(paper_title: str, abstract: str, topic_title: str, course_title: str) -> bool:
    """
    Validates whether a candidate paper is academically relevant to the topic.
    Guarantees papers from completely unrelated fields (e.g. crystallography software)
    are strictly rejected.
    """
    p_lower = (paper_title or "").lower()
    a_lower = (abstract or "").lower()
    combined_paper = f"{p_lower} {a_lower}"

    topic_keywords = _extract_core_keywords(topic_title)
    if not topic_keywords:
        # If topic title is purely generic (e.g. "Introduction"), require course title keywords
        course_keywords = _extract_core_keywords(course_title)
        return any(kw in combined_paper for kw in course_keywords)

    # At least one core topic keyword must appear in the paper's title or abstract
    return any(kw in combined_paper for kw in topic_keywords)


def get_or_fetch_academic_papers(topic, limit: int = 3):
    """
    Retrieves cached academic research papers from local DB, or queries
    Semantic Scholar / OpenAlex APIs using topic & discipline relevance matching.
    Stores validated results in PrepTopicAcademicPaper table.
    """
    from prep.models import PrepTopicAcademicPaper

    if not topic or not getattr(topic, "pk", None):
        return []

    # 1. Return cached papers if already stored in DB
    existing = list(
        PrepTopicAcademicPaper.objects.filter(topic=topic, is_approved=True)
        .order_by("-citation_count", "-year")[:limit]
    )
    if existing:
        return existing

    topic_title = getattr(topic, "title", "").strip()
    if not topic_title:
        return []

    course_title = ""
    if topic.course:
        course_title = getattr(topic.course, "title", "").strip()

    # Formulate contextual academic query without alphanumeric course codes
    # e.g. "Sufficient Statistics Theory of Estimation" instead of "Sufficient Statistics SST 305"
    if course_title and course_title.lower() not in topic_title.lower():
        academic_query = f"{topic_title} {course_title}".strip()
    else:
        academic_query = topic_title

    papers = []
    session = requests.Session()
    session.headers.update({
        "User-Agent": ACADEMIC_USER_AGENT,
        "Accept": "application/json",
    })

    # 2. Query Semantic Scholar Graph API (relevance ranking)
    try:
        url = "https://api.semanticscholar.org/graph/v1/paper/search"
        params = {
            "query": academic_query,
            "limit": limit * 2,  # Fetch a few to allow relevance filtering
            "fields": "title,authors,year,venue,citationCount,openAccessPdf,abstract,url,externalIds",
        }
        resp = session.get(url, params=params, timeout=3.5)
        if resp.ok:
            data = resp.json().get("data", [])
            for item in data:
                p_title = (item.get("title") or "").strip()
                if not p_title:
                    continue
                
                abstract_text = (item.get("abstract") or "").strip()
                if not _is_paper_relevant(p_title, abstract_text, topic_title, course_title):
                    continue

                authors_list = [a.get("name", "") for a in item.get("authors", []) if a.get("name")]
                authors_str = ", ".join(authors_list[:3])
                if len(authors_list) > 3:
                    authors_str += " et al."

                pdf_info = item.get("openAccessPdf") or {}
                raw_pdf_url = pdf_info.get("url") or ""
                canonical_page_url = item.get("url") or ""
                
                ext_ids = item.get("externalIds") or {}
                raw_doi = ext_ids.get("DOI") or ""
                arxiv_id = ext_ids.get("ArXiv") or ""

                resolved_pdf_url, resolved_doi_url = _resolve_safe_paper_urls(
                    raw_pdf_url=raw_pdf_url,
                    canonical_url=canonical_page_url,
                    doi=raw_doi,
                    arxiv_id=arxiv_id,
                )

                if abstract_text and len(abstract_text) > 400:
                    abstract_text = abstract_text[:397] + "..."

                paper_obj = PrepTopicAcademicPaper(
                    topic=topic,
                    title=p_title[:300],
                    authors=authors_str[:300],
                    year=item.get("year"),
                    venue=(item.get("venue") or "")[:200],
                    abstract=abstract_text,
                    citation_count=item.get("citationCount") or 0,
                    open_access_pdf_url=resolved_pdf_url[:500],
                    doi_url=resolved_doi_url[:500],
                    source="semantic_scholar",
                    is_approved=True,
                )
                papers.append(paper_obj)
                if len(papers) >= limit:
                    break
    except Exception as exc:
        logger.warning("Semantic Scholar lookup failed for topic %s: %s", topic.pk, exc)

    # 3. Fallback to OpenAlex API (filtered by is_oa:true, ranked by BM25 relevance)
    if not papers:
        try:
            openalex_url = "https://api.openalex.org/works"
            params = {
                "search": academic_query,
                "filter": "is_oa:true",
                "per_page": limit * 2,
            }
            resp = session.get(openalex_url, params=params, timeout=3.5)
            if resp.ok:
                results = resp.json().get("results", [])
                for res in results:
                    p_title = (res.get("display_name") or "").strip()
                    if not p_title:
                        continue

                    abstract_text = _reconstruct_openalex_abstract(res.get("abstract_inverted_index"))
                    if not _is_paper_relevant(p_title, abstract_text, topic_title, course_title):
                        continue

                    authors_list = []
                    for auth in res.get("authorships", []):
                        raw_name = (auth.get("author", {}) or {}).get("display_name")
                        if raw_name:
                            authors_list.append(raw_name)
                    authors_str = ", ".join(authors_list[:3])
                    if len(authors_list) > 3:
                        authors_str += " et al."

                    oa = res.get("open_access") or {}
                    raw_oa_url = oa.get("oa_url") or ""
                    
                    prim_loc = res.get("primary_location") or {}
                    landing_url = prim_loc.get("landing_page_url") or ""
                    pdf_url = prim_loc.get("pdf_url") or raw_oa_url

                    best_oa = res.get("best_oa_location") or {}
                    if not pdf_url:
                        pdf_url = best_oa.get("pdf_url") or best_oa.get("landing_page_url") or ""

                    raw_doi = res.get("doi") or ""
                    ids = res.get("ids") or {}
                    arxiv_id = ""
                    if ids.get("arxiv"):
                        arxiv_id = str(ids["arxiv"]).split("/")[-1]

                    resolved_pdf_url, resolved_doi_url = _resolve_safe_paper_urls(
                        raw_pdf_url=pdf_url,
                        canonical_url=landing_url,
                        doi=raw_doi,
                        arxiv_id=arxiv_id,
                    )

                    venue_name = ""
                    host_venue = (prim_loc.get("source") or {})
                    if host_venue:
                        venue_name = host_venue.get("display_name") or ""

                    paper_obj = PrepTopicAcademicPaper(
                        topic=topic,
                        title=p_title[:300],
                        authors=authors_str[:300],
                        year=res.get("publication_year"),
                        venue=venue_name[:200],
                        abstract=abstract_text,
                        citation_count=res.get("cited_by_count") or 0,
                        open_access_pdf_url=resolved_pdf_url[:500],
                        doi_url=resolved_doi_url[:500],
                        source="openalex",
                        is_approved=True,
                    )
                    papers.append(paper_obj)
                    if len(papers) >= limit:
                        break
        except Exception as exc:
            logger.warning("OpenAlex lookup failed for topic %s: %s", topic.pk, exc)

    # Bulk create validated relevant papers
    if papers:
        try:
            PrepTopicAcademicPaper.objects.bulk_create(papers, ignore_conflicts=True)
            return list(
                PrepTopicAcademicPaper.objects.filter(topic=topic, is_approved=True)
                .order_by("-citation_count", "-year")[:limit]
            )
        except Exception as exc:
            logger.error("Failed saving academic papers for topic %s: %s", topic.pk, exc)

    return []
