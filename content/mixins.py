"""
content/mixins.py

Subscription access gate mixin for class-based views,
and a function decorator for function-based views.
"""
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone

from courses.models import Cohort, Enrollment
from payments.models import Subscription


def check_cohort_access(user, cohort):
    """
    Returns True if the user has active access to the cohort.
    Admins and tutors who own the cohort always pass.
    Learners need an active Enrollment AND a valid Subscription.
    """
    if not user.is_authenticated:
        return False
    if user.is_admin:
        return True
    if user.is_tutor and cohort.tutor_id == user.id:
        return True
    if user.is_learner:
        enrolled = Enrollment.objects.filter(
            learner=user, cohort=cohort, status="active"
        ).exists()
        if not enrolled:
            return False
        paid = Subscription.objects.filter(
            learner=user,
            cohort=cohort,
            status="active",
            paid_until__gte=timezone.now().date(),
        ).exists()
        return paid
    return False


def cohort_access_required(view_func):
    """
    Decorator for function-based views.
    Expects `cohort_id` as a URL kwarg.
    """
    from functools import wraps

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        cohort_id = kwargs.get("cohort_id")
        cohort = get_object_or_404(Cohort, id=cohort_id)
        if not check_cohort_access(request.user, cohort):
            messages.error(
                request,
                "You need an active subscription to access this content. "
                "Please subscribe or renew your subscription."
            )
            return redirect("payments:initiate", cohort_id=cohort.id)
        return view_func(request, *args, **kwargs)
    return wrapper
