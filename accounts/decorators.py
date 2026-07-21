"""accounts/decorators.py — Role-based access decorators."""
from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def role_required(*roles):
    """
    Decorator that restricts a view to users with one of the given roles.
    Admin (is_admin) always passes through.
    Usage:
        @role_required("tutor", "admin")
        def my_view(request): ...
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect(f"/accounts/login/?next={request.path}")

            # Superusers and admins always pass
            if request.user.is_admin:
                return view_func(request, *args, **kwargs)

            if request.user.role not in roles:
                messages.error(request, "You don't have permission to access that page.")
                return redirect(request.user.get_dashboard_url())

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
