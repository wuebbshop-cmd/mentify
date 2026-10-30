"""
search_assistant/search_engine.py

Universal Web Search & Deep Content Extraction Engine:
1. Live Web Search with Batch URL Decoding (resolves real publisher links)
2. Deep Web Page Content Fetcher (concurrently reads article bodies, tables, and lists)
3. Site-Aware Crawlers (handles specific domains like job boards, movie databases, etc.)
4. GitHub & Wikipedia integrations
"""
import concurrent.futures
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from typing import Any, Dict, List, Optional
from bs4 import BeautifulSoup
import requests

try:
    from googlenewsdecoder import gnewsdecoder
except ImportError:
    gnewsdecoder = None

USER_AGENT = "Mozilla/5.0"


def _clean_text(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_urls_from_text(text: str) -> List[str]:
    """Extract any http/https URLs from user prompt."""
    return re.findall(r"https?://[^\s<>\"']+", text)


def scrape_page_content(url: str, max_chars: int = 4000) -> Dict[str, Any]:
    """
    Scrape and extract readable body text, headings, and lists from a webpage.
    """
    if not url or not url.startswith("http") or "news.google.com/rss/articles" in url:
        return {"error": "Invalid or redirect URL", "text": "", "url": url, "success": False}

    try:
        headers = {"User-Agent": USER_AGENT}
        res = requests.get(url, headers=headers, timeout=6)
        if res.status_code != 200:
            return {"error": f"HTTP {res.status_code}", "text": "", "url": url, "success": False}

        soup = BeautifulSoup(res.text, "html.parser")
        title = soup.title.string.strip() if soup.title and soup.title.string else ""

        # Remove boilerplates
        for tag in soup(["script", "style", "noscript", "nav", "footer", "header", "aside", "svg"]):
            tag.decompose()

        # Extract structured text preserving list items and headings
        lines = []
        for el in soup.find_all(["h1", "h2", "h3", "h4", "p", "li"]):
            t = el.get_text().strip()
            if len(t) > 5:
                lines.append(t)

        full_text = "\n".join(lines)
        return {
            "title": title,
            "text": full_text[:max_chars],
            "url": url,
            "success": True,
        }
    except Exception as e:
        return {"error": str(e), "text": "", "url": url, "success": False}


def decode_google_news_urls(urls: List[str]) -> List[str]:
    """
    Batch decode Google News redirect links to real publisher URLs using gnewsdecoder.
    """
    if not urls or not gnewsdecoder:
        return urls

    try:
        results = gnewsdecoder(urls)
        decoded = []
        if isinstance(results, list):
            for orig, r in zip(urls, results):
                if isinstance(r, dict) and r.get("success") and r.get("decoded_url"):
                    decoded.append(r["decoded_url"])
                else:
                    decoded.append(orig)
            return decoded
    except Exception as e:
        print(f"[Search Engine] Batch decode error: {e}")

    return urls


def search_web(
    query: str,
    time_filter: str = "any",
    max_results: int = 10,
    deep_fetch_content: bool = True,
) -> List[Dict[str, Any]]:
    """
    Search the live web and concurrently extract real page content from top results.
    """
    clean_query = query.strip()
    if time_filter == "day":
        clean_query += " when:1d"
    elif time_filter == "week":
        clean_query += " when:7d"
    elif time_filter == "month":
        clean_query += " when:30d"

    encoded_q = urllib.parse.quote(clean_query)
    url = f"https://news.google.com/rss/search?q={encoded_q}&hl=en-US&gl=US&ceid=US:en"

    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    raw_items = []
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            root = ET.fromstring(resp.read())
            for item in root.findall(".//item")[: max_results * 2]:
                title_elem = item.find("title")
                link_elem = item.find("link")
                pub_elem = item.find("pubDate")
                desc_elem = item.find("description")
                source_elem = item.find("source")

                title = title_elem.text if title_elem is not None else ""
                link = link_elem.text if link_elem is not None else ""
                pub_date = pub_elem.text if pub_elem is not None else ""
                desc = _clean_text(desc_elem.text) if desc_elem is not None else ""
                source = source_elem.text if source_elem is not None else ""

                if not source and " - " in title:
                    parts = title.rsplit(" - ", 1)
                    title, source = parts[0].strip(), parts[1].strip()

                if title and link:
                    raw_items.append(
                        {
                            "title": title,
                            "link": link,
                            "source": source or "Web",
                            "pub_date": pub_date,
                            "snippet": desc,
                            "content": "",
                        }
                    )
    except Exception as e:
        print(f"[Search Engine] Web search error: {e}")
        return []

    results = raw_items[:max_results]

    # Batch decode Google News links to authentic URLs
    links_to_decode = [r["link"] for r in results]
    decoded_links = decode_google_news_urls(links_to_decode)
    for r, dec in zip(results, decoded_links):
        r["link"] = dec

    # Deep Content Fetching: Parallel fetch body text from top valid decoded pages
    if deep_fetch_content:
        fetch_targets = [r for r in results if not r["link"].startswith("https://news.google.com")][:6]
        if fetch_targets:
            with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
                future_map = {executor.submit(scrape_page_content, t["link"]): t for t in fetch_targets}
                for future in concurrent.futures.as_completed(future_map, timeout=12):
                    target = future_map[future]
                    try:
                        page_data = future.result()
                        if page_data.get("success") and page_data.get("text"):
                            target["content"] = page_data["text"]
                    except Exception:
                        pass

    return results


def scrape_domain_jobs(domain: str, keywords: str, max_results: int = 8) -> List[Dict[str, Any]]:
    """Generic or specialized site search for job portals."""
    encoded_q = urllib.parse.quote_plus(keywords.strip())
    results = []
    seen = set()

    if "myjobmag" in domain:
        url = f"https://www.myjobmag.co.ke/search/jobs?q={encoded_q}"
        try:
            res = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=8)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                for h in soup.find_all(["h2", "h3"]):
                    a = h.find("a")
                    if a and a.get("href") and "/job/" in a["href"]:
                        href = a["href"]
                        if href.startswith("/"):
                            href = "https://www.myjobmag.co.ke" + href
                        if href not in seen:
                            seen.add(href)
                            title = a.get_text().strip()
                            results.append(
                                {
                                    "title": title,
                                    "link": href,
                                    "source": "MyJobMag Kenya",
                                    "pub_date": "Active Posting",
                                    "snippet": "Live job vacancy on MyJobMag Kenya.",
                                    "content": "",
                                }
                            )
                            if len(results) >= max_results:
                                break
        except Exception:
            pass

    elif "brightermonday" in domain:
        url = f"https://www.brightermonday.co.ke/jobs?q={encoded_q}"
        try:
            res = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=8)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                for a in soup.find_all("a", href=True):
                    href = a["href"]
                    if ("/listings/" in href or "/job/" in href) and href not in seen:
                        title = a.get_text().strip()
                        if len(title) > 3 and not title.lower().startswith("apply"):
                            seen.add(href)
                            if not href.startswith("http"):
                                href = "https://www.brightermonday.co.ke" + href
                            results.append(
                                {
                                    "title": title,
                                    "link": href,
                                    "source": "BrighterMonday Kenya",
                                    "pub_date": "Active Posting",
                                    "snippet": "Live job vacancy on BrighterMonday Kenya.",
                                    "content": "",
                                }
                            )
                            if len(results) >= max_results:
                                break
        except Exception:
            pass

    return results


def search_github(query: str, max_results: int = 5) -> List[Dict[str, Any]]:
    """Search public GitHub repositories for code, tools, or open-source projects."""
    try:
        encoded_q = urllib.parse.quote(query.strip())
        url = f"https://api.github.com/search/repositories?q={encoded_q}&sort=stars&order=desc&per_page={max_results}"
        res = requests.get(url, headers={"User-Agent": USER_AGENT, "Accept": "application/vnd.github.v3+json"}, timeout=8)
        if res.status_code == 200:
            data = res.json()
            items = []
            for item in data.get("items", [])[:max_results]:
                items.append(
                    {
                        "title": item.get("full_name", ""),
                        "link": item.get("html_url", ""),
                        "source": f"GitHub (★ {item.get('stargazers_count', 0):,})",
                        "pub_date": f"Updated: {item.get('updated_at', '')[:10]}",
                        "snippet": item.get("description") or "No description provided.",
                        "content": "",
                        "language": item.get("language") or "Code",
                    }
                )
            return items
    except Exception as e:
        print(f"[Search Engine] GitHub search error: {e}")
    return []


def search_wikipedia(query: str, max_results: int = 3) -> List[Dict[str, Any]]:
    """Search Wikipedia for definitions, concepts, or background knowledge."""
    try:
        encoded_q = urllib.parse.quote(query.strip())
        url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={encoded_q}&limit={max_results}&format=json"
        res = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=8)
        if res.status_code == 200:
            data = res.json()
            if len(data) >= 4:
                titles = data[1]
                snippets = data[2]
                urls = data[3]
                items = []
                for t, s, u in zip(titles, snippets, urls):
                    if t and u:
                        items.append(
                            {
                                "title": t,
                                "link": u,
                                "source": "Wikipedia",
                                "pub_date": "",
                                "snippet": s or "Encyclopedia entry.",
                                "content": "",
                            }
                        )
                return items
    except Exception as e:
        print(f"[Search Engine] Wikipedia error: {e}")
    return []
