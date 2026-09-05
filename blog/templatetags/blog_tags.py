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
    """Convert raw YouTube and Vimeo URLs inside paragraph text into responsive iframe video embeds."""
    youtube_pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    
    def repl_yt(match):
        video_id = match.group(1)
        return (
            f'<div class="blog-video-embed my-6 overflow-hidden rounded-xl shadow-lg aspect-video">'
            f'<iframe src="https://www.youtube.com/embed/{video_id}" '
            f'class="w-full h-full border-0" allowfullscreen '
            f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture">'
            f'</iframe></div>'
        )

    return re.sub(youtube_pattern, repl_yt, html)


def _add_heading_ids(html: str) -> str:
    """Add anchor IDs to h2 and h3 tags for table of contents linking."""
    def repl(match):
        tag = match.group(1)
        title = match.group(2).strip()
        # Strip internal tags if any
        clean_text = re.sub(r'<[^>]+>', '', title)
        heading_id = slugify(clean_text) or 'section'
        return f'<{tag} id="{heading_id}" class="scroll-mt-24 font-bold text-gray-900 dark:text-white mt-8 mb-4">{title}</{tag}>'

    return re.sub(r'<(h[23])>(.*?)</\1>', repl, html, flags=re.IGNORECASE | re.DOTALL)


def _fallback_markdown_parser(text: str) -> str:
    """Lightweight pure-python fallback markdown parser if markdown library is unavailable."""
    if not text:
        return ""

    lines = text.split("\n")
    html_lines = []
    in_code_block = False
    code_lang = ""
    code_buffer = []

    for line in lines:
        if line.startswith("```"):
            if in_code_block:
                escaped_code = (
                    "\n".join(code_buffer)
                    .replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                )
                html_lines.append(
                    f'<pre class="blog-code-block my-6 p-4 rounded-xl bg-gray-900 text-gray-100 font-mono text-sm overflow-x-auto"><code>{escaped_code}</code></pre>'
                )
                code_buffer = []
                in_code_block = False
            else:
                in_code_block = True
                code_lang = line[3:].strip()
            continue

        if in_code_block:
            code_buffer.append(line)
            continue

        # Headings
        if line.startswith("### "):
            html_lines.append(f"<h3>{line[4:].strip()}</h3>")
            continue
        elif line.startswith("## "):
            html_lines.append(f"<h2>{line[3:].strip()}</h2>")
            continue
        elif line.startswith("# "):
            html_lines.append(f"<h1>{line[2:].strip()}</h1>")
            continue

        # Blockquote
        if line.startswith("> "):
            html_lines.append(
                f'<blockquote class="my-6 border-l-4 border-teal-600 pl-4 italic text-gray-700 dark:text-gray-300">{line[2:].strip()}</blockquote>'
            )
            continue

        # List items
        if line.startswith("- ") or line.startswith("* "):
            html_lines.append(f'<li class="ml-6 list-disc my-1">{line[2:].strip()}</li>')
            continue

        if not line.strip():
            html_lines.append("<br>")
            continue

        html_lines.append(f"<p class='my-4 leading-relaxed'>{line}</p>")

    html = "".join(html_lines)

    # Inline formatting
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    html = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1" class="my-6 rounded-xl shadow-md max-w-full h-auto">', html)
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank" rel="noopener noreferrer" class="text-teal-600 dark:text-teal-400 underline font-medium hover:text-teal-700">\1</a>', html)

    return html


@register.filter(name="render_markdown")
def render_markdown(value: str) -> str:
    """Template filter converting markdown text into formatted HTML with TOC IDs and video embeds."""
    if not value:
        return ""

    if HAS_MARKDOWN:
        md = markdown.Markdown(
            extensions=[
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
    # Find h2 and h3 headings in markdown
    for line in value.split("\n"):
        line_str = line.strip()
        if line_str.startswith("## "):
            title = line_str[3:].strip()
            # Strip formatting characters
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
