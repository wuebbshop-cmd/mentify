import re
from django import template
from django.utils.safestring import mark_safe
from django.utils.text import slugify

register = template.Library()

try:
    import markdown

    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False


def _convert_video_embeds(html: str) -> str:
    """Convert raw YouTube URLs inside paragraph text into responsive iframe video embeds."""
    youtube_pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    
    def repl_yt(match):
        video_id = match.group(1)
        return (
            f'<div class="blog-video-embed my-6 overflow-hidden rounded-xl shadow-lg aspect-video" style="position:relative; padding-bottom:56.25%; height:0; overflow:hidden; margin: 1.5rem 0; border-radius: 8px;">'
            f'<iframe src="https://www.youtube.com/embed/{video_id}" '
            f'style="position:absolute; top:0; left:0; width:100%; height:100%; border:0;" allowfullscreen '
            f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture">'
            f'</iframe></div>'
        )

    return re.sub(youtube_pattern, repl_yt, html)


def _add_heading_ids(html: str) -> str:
    """Add anchor IDs to h2 and h3 tags for table of contents linking."""
    def repl(match):
        tag = match.group(1).lower()
        title = match.group(2).strip()
        clean_text = re.sub(r'<[^>]+>', '', title)
        heading_id = slugify(clean_text) or 'section'
        return f'<{tag} id="{heading_id}">{title}</{tag}>'

    return re.sub(r'<(h[23])>(.*?)</\1>', repl, html, flags=re.IGNORECASE | re.DOTALL)


def _fallback_markdown_parser(text: str) -> str:
    """Lightweight pure-python fallback markdown parser if markdown library is unavailable."""
    if not text:
        return ""

    lines = text.split("\n")
    html_lines = []
    in_code_block = False
    in_ul = False
    in_ol = False
    code_buffer = []

    for line in lines:
        stripped = line.strip()

        # Handle Code Blocks (```)
        if stripped.startswith("```"):
            if in_ul:
                html_lines.append("</ul>")
                in_ul = False
            if in_ol:
                html_lines.append("</ol>")
                in_ol = False

            if in_code_block:
                escaped_code = (
                    "\n".join(code_buffer)
                    .replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                )
                html_lines.append(f'<pre><code>{escaped_code}</code></pre>')
                code_buffer = []
                in_code_block = False
            else:
                in_code_block = True
            continue

        if in_code_block:
            code_buffer.append(line)
            continue

        # Horizontal Rules (---, ***, ___)
        if stripped in ("---", "***", "___") or re.match(r'^(\-{3,}|\*{3,}|_{3,})$', stripped):
            if in_ul:
                html_lines.append("</ul>")
                in_ul = False
            if in_ol:
                html_lines.append("</ol>")
                in_ol = False
            html_lines.append("<hr>")
            continue

        # Headings
        if stripped.startswith("### "):
            if in_ul: html_lines.append("</ul>"); in_ul = False
            if in_ol: html_lines.append("</ol>"); in_ol = False
            html_lines.append(f"<h3>{stripped[4:].strip()}</h3>")
            continue
        elif stripped.startswith("## "):
            if in_ul: html_lines.append("</ul>"); in_ul = False
            if in_ol: html_lines.append("</ol>"); in_ol = False
            html_lines.append(f"<h2>{stripped[3:].strip()}</h2>")
            continue
        elif stripped.startswith("# "):
            if in_ul: html_lines.append("</ul>"); in_ul = False
            if in_ol: html_lines.append("</ol>"); in_ol = False
            html_lines.append(f"<h1>{stripped[2:].strip()}</h1>")
            continue

        # Blockquote (> Quote)
        if stripped.startswith("> "):
            if in_ul: html_lines.append("</ul>"); in_ul = False
            if in_ol: html_lines.append("</ol>"); in_ol = False
            html_lines.append(f"<blockquote><p>{stripped[2:].strip()}</p></blockquote>")
            continue

        # Unordered Bullet List (- item or * item)
        if re.match(r'^[\-\*]\s+', stripped):
            if in_ol:
                html_lines.append("</ol>")
                in_ol = False
            if not in_ul:
                html_lines.append("<ul>")
                in_ul = True
            item_text = re.sub(r'^[\-\*]\s+', '', stripped)
            html_lines.append(f"<li>{item_text}</li>")
            continue

        # Ordered Numbered List (1. item)
        if re.match(r'^\d+\.\s+', stripped):
            if in_ul:
                html_lines.append("</ul>")
                in_ul = False
            if not in_ol:
                html_lines.append("<ol>")
                in_ol = True
            item_text = re.sub(r'^\d+\.\s+', '', stripped)
            html_lines.append(f"<li>{item_text}</li>")
            continue

        # Close lists if empty or non-list line
        if in_ul:
            html_lines.append("</ul>")
            in_ul = False
        if in_ol:
            html_lines.append("</ol>")
            in_ol = False

        if not stripped:
            continue

        html_lines.append(f"<p>{stripped}</p>")

    if in_ul: html_lines.append("</ul>")
    if in_ol: html_lines.append("</ol>")

    html = "".join(html_lines)

    # Inline formatting
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)  # Inline code backticks
    html = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', html)
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>', html)

    return html


@register.filter(name="render_markdown")
def render_markdown(value: str) -> str:
    """Template filter converting markdown text into formatted HTML with TOC IDs and video embeds."""
    if not value:
        return ""

    if HAS_MARKDOWN:
        md = markdown.Markdown(
            extensions=[
                "extra",       # Includes tables, fenced_code, hr, attr_list, def_list, etc.
                "fenced_code",
                "tables",
                "toc",
                "nl2br",
                "sane_lists",
            ]
        )
        raw_html = md.convert(value)
    else:
        raw_html = _fallback_markdown_parser(value)

    raw_html = _add_heading_ids(raw_html)
    raw_html = _convert_video_embeds(raw_html)

    return mark_safe(raw_html)


@register.filter(name="extract_toc")
def extract_toc(value: str) -> list[dict]:
    """Extract headings (h2, h3) from markdown for rendering a Table of Contents menu."""
    if not value:
        return []

    toc = []
    for line in value.split("\n"):
        line_str = line.strip()
        if line_str.startswith("## "):
            title = line_str[3:].strip()
            clean_title = re.sub(r'[\*\_\`\[\]\(\)]', '', title)
            toc.append({
                "level": 2,
                "title": clean_title,
                "anchor": slugify(clean_title) or "section",
            })
        elif line_str.startswith("### "):
            title = line_str[4:].strip()
            clean_title = re.sub(r'[\*\_\`\[\]\(\)]', '', title)
            toc.append({
                "level": 3,
                "title": clean_title,
                "anchor": slugify(clean_title) or "section",
            })

    return toc
