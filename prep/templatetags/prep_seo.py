"""Safe server-side Markdown rendering for public, crawlable Prep resources."""

from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

try:
    import markdown
except ImportError:  # pragma: no cover - markdown is a production dependency.
    markdown = None


register = template.Library()


@register.filter(name="render_prep_markdown")
def render_prep_markdown(value):
    """Render validated Markdown as HTML while treating source HTML as text."""
    source = str(value or "")
    if not source:
        return ""
    if markdown is None:
        return mark_safe("<p>" + escape(source).replace("\n", "<br>") + "</p>")

    rendered = markdown.markdown(
        escape(source),
        extensions=["extra", "fenced_code", "tables", "sane_lists", "nl2br"],
        output_format="html5",
    )
    return mark_safe(rendered)
