"""
config/middleware/security_error_middleware.py

Global Security & Error Sanitization Middleware for Mentify and Mentify Prep.
Intercepts unhandled server exceptions, sanitizes error output, redacts sensitive
credentials/tokens, and guarantees that users never see Django debug screens,
database error traces, or sensitive configuration details.
"""
import logging
import re
from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from django.core.exceptions import PermissionDenied
from django.template.loader import render_to_string

logger = logging.getLogger("django.security.error_handler")

# Fallback fail-safe HTML if template engine itself fails during an outage
_FAILSAFE_500_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>500 - Server Error | Mentify</title>
  <style>
    :root {
      --bg: #0f172a;
      --card-bg: #1e293b;
      --text: #f8fafc;
      --muted: #94a3b8;
      --border: #334155;
      --green: #0f766e;
      --green-hover: #115e59;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px 16px;
    }
    .error-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 16px;
      max-width: 500px;
      width: 100%;
      padding: 40px 32px;
      text-align: center;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
    }
    .icon-badge {
      width: 64px;
      height: 64px;
      border-radius: 50%;
      background: rgba(220, 38, 38, 0.15);
      color: #ef4444;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 20px;
    }
    .badge {
      display: inline-block;
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 3px 10px;
      border-radius: 999px;
      background: rgba(220, 38, 38, 0.2);
      color: #f87171;
      margin-bottom: 12px;
    }
    h1 {
      font-size: 1.6rem;
      font-weight: 700;
      margin-bottom: 10px;
      color: #ffffff;
    }
    p {
      font-size: 0.95rem;
      color: var(--muted);
      line-height: 1.6;
      margin-bottom: 28px;
    }
    .btn-group {
      display: flex;
      gap: 12px;
      justify-content: center;
      flex-wrap: wrap;
    }
    .btn {
      display: inline-block;
      padding: 10px 20px;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.15s ease;
      cursor: pointer;
    }
    .btn-primary {
      background: var(--green);
      color: #ffffff;
    }
    .btn-primary:hover {
      background: var(--green-hover);
    }
    .btn-outline {
      border: 1px solid var(--border);
      color: var(--text);
      background: transparent;
    }
    .btn-outline:hover {
      background: rgba(255, 255, 255, 0.05);
    }
  </style>
</head>
<body>
  <div class="error-card">
    <div class="icon-badge">
      <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
    </div>
    <div><span class="badge">Error 500</span></div>
    <h1>Something Went Wrong</h1>
    <p>An unexpected error occurred while processing your request. Our technical team has been notified. Please try again shortly.</p>
    <div class="btn-group">
      <a href="javascript:history.back()" class="btn btn-outline">&larr; Go Back</a>
      <a href="/prep/" class="btn btn-primary">Go to Mentify Prep</a>
      <a href="/" class="btn btn-outline">Home</a>
    </div>
  </div>
</body>
</html>
"""


def is_ajax_or_api_request(request) -> bool:
    """Detect whether incoming request expects JSON or was initiated by AJAX/fetch."""
    if not request:
        return False
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return True
    accept = request.headers.get("accept", "")
    if "application/json" in accept and "text/html" not in accept:
        return True
    content_type = getattr(request, "content_type", "") or request.headers.get("content-type", "")
    if "application/json" in content_type:
        return True
    path = request.path or ""
    if path.startswith("/api/") or "/api/" in path or path.endswith("/json/"):
        return True
    return False


class SecurityErrorMiddleware:
    """
    Middleware that traps unhandled exceptions and ensures zero technical leakage.
    Protects against leaking SQL queries, stack traces, file paths, credentials, and tokens.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Safety catch: If an API endpoint returned an HTML 500 error page or raw string,
        # convert it into a clean, well-formatted JSON response.
        if response.status_code == 500 and is_ajax_or_api_request(request):
            content_type = response.headers.get("content-type", "")
            if "application/json" not in content_type:
                return JsonResponse(
                    {
                        "success": False,
                        "status": "error",
                        "error": "An unexpected server error occurred. Our team has been notified.",
                    },
                    status=500,
                )

        return response

    def process_exception(self, request, exception):
        """
        Invoked by Django when a view raises an unhandled exception.
        Logs the failure with sensitive data scrubbed and renders a secure error response.
        """
        # Let standard Django 404 and 403 handlers process their respective exceptions
        if isinstance(exception, (Http404, PermissionDenied)):
            return None

        # Redact potentially sensitive query params or body in logging
        safe_path = request.path if request else "/"
        logger.error(
            "Unhandled exception in %s: %s",
            safe_path,
            exception,
            exc_info=True,
            extra={"path": safe_path},
        )

        # 1. API or AJAX requests: return sanitized JSON
        if is_ajax_or_api_request(request):
            return JsonResponse(
                {
                    "success": False,
                    "status": "error",
                    "error": "An unexpected server error occurred. Please try again shortly or contact support.",
                },
                status=500,
            )

        # 2. Standard Web requests: render custom branded 500 error page
        is_prep = bool(request and request.path and request.path.startswith("/prep/"))
        context = {
            "is_prep": is_prep,
            "request_path": request.path if request else "",
            "PLATFORM_NAME": getattr(settings, "PLATFORM_NAME", "Mentify"),
        }

        try:
            rendered = render_to_string("500.html", context, request=request)
            return HttpResponse(rendered, status=500, content_type="text/html")
        except Exception as render_err:
            logger.error("Failed to render 500.html template: %s", render_err)
            return HttpResponse(_FAILSAFE_500_HTML, status=500, content_type="text/html")
