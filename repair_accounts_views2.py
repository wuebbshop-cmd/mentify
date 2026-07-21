from pathlib import Path
import re

path = Path(r'c:\Users\adm\.vscode\Products\EduAI\accounts\views.py')
text = path.read_text(encoding='utf-8')

# Fix imports
import_stmt = '''from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden
from django.conf import settings
from django.urls import reverse
'''
new_import_stmt = '''from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models import Q
'''
if import_stmt in text:
    text = text.replace(import_stmt, new_import_stmt, 1)
else:
    print('Import block not found or already patched')

models_stmt = 'from .models import User, Profile\n'
new_models_stmt = 'from .models import User, Profile, Guardian, GuardianLinkRequest, GuardianLinkRequestLog\n'
if models_stmt in text:
    text = text.replace(models_stmt, new_models_stmt, 1)
else:
    print('Models import line not found or already patched')

# Remove stray dead code from promote_if_admin_email
text = text.replace('        return\n        from django.core.mail import send_mail\n        from django.urls import reverse\n        from django.conf import settings\n        from django.template.loader import render_to_string\n', '        return\n')

# Replace the broken register_tutor + nested function block
pattern = re.compile(r'def register_tutor\(request\):[\s\S]*?def login_view\(request\):', re.MULTILINE)
match = pattern.search(text)
if not match:
    raise SystemExit('Broken register_tutor block not found')

replacement = '''def register_tutor(request):
    """Tutor self-registration."""
    if request.user.is_authenticated:
        return redirect(request.user.get_dashboard_url())
    if request.method == "POST":
        form = LearnerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "tutor"
            user.save()
            Profile.objects.get_or_create(user=user)
            promote_if_admin_email(user)
            login(request, user)
            messages.success(request, f"Welcome to Mentify, {user.first_name}!")
            return redirect(user.get_dashboard_url())
    else:
        form = LearnerRegistrationForm()
    return render(request, "accounts/register_tutor.html", {"form": form})


@login_required
@role_required("guardian")
def guardian_link_request(request):
    """Guardian self-service request to link to their learner's account."""
    if request.method == "POST":
        form = GuardianChildLinkForm(request.POST)
        if form.is_valid():
            learner = form.cleaned_data["learner"]
            guardian = request.user
            request_obj, created = GuardianLinkRequest.objects.get_or_create(
                guardian=guardian,
                learner=learner,
                defaults={"notes": form.cleaned_data.get("notes", "")},
            )
            if not created and request_obj.status == GuardianLinkRequest.Status.PENDING:
                messages.info(request, "A pending request already exists for this learner.")
            else:
                request_obj.status = GuardianLinkRequest.Status.PENDING
                request_obj.notes = form.cleaned_data.get("notes", "") or request_obj.notes
                request_obj.responded_at = None
                request_obj.save()
                GuardianLinkRequestLog.objects.create(
                    request=request_obj,
                    event=GuardianLinkRequestLog.Event.REQUESTED,
                    actor=guardian,
                    message="Guardian requested link to learner account.",
                )
                confirm_url = request.build_absolute_uri(reverse("accounts:guardian_link_confirm", args=[request_obj.token]))
                subject = f"Guardian link request from {guardian.get_full_name()}"
                message_body = render_to_string("accounts/emails/guardian_link_request.txt", {
                    "learner": learner,
                    "guardian": guardian,
                    "link_url": confirm_url,
                    "PLATFORM_NAME": getattr(settings, "PLATFORM_NAME", "Mentify"),
                })
                send_mail(
                    subject,
                    message_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [learner.email],
                    fail_silently=True,
                )
                messages.success(request, "Your request has been sent. The learner will be notified by email.")
                return redirect("accounts:guardian_dashboard")
    else:
        form = GuardianChildLinkForm()

    pending_requests = GuardianLinkRequest.objects.filter(
        guardian=request.user
    ).select_related("learner").order_by("-created_at")

    return render(request, "accounts/guardian_link_request.html", {
        "form": form,
        "pending_requests": pending_requests,
    })


@login_required
@role_required("learner")
def guardian_link_confirm(request, token):
    """Learner confirms or rejects a guardian link request."""
    request_obj = get_object_or_404(GuardianLinkRequest, token=token)
    if request.user != request_obj.learner:
        return HttpResponseForbidden("You are not authorized to confirm this link.")

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "accept":
            request_obj.status = GuardianLinkRequest.Status.ACCEPTED
            request_obj.responded_at = timezone.now()
            request_obj.save()
            guardian_profile, _ = Guardian.objects.get_or_create(user=request_obj.guardian)
            guardian_profile.learners.add(request_obj.learner)
            GuardianLinkRequestLog.objects.create(
                request=request_obj,
                event=GuardianLinkRequestLog.Event.ACCEPTED,
                actor=request.user,
                message="Learner accepted guardian link request.",
            )
            messages.success(request, "Link accepted. Your guardian can now see your progress.")
        else:
            request_obj.status = GuardianLinkRequest.Status.REJECTED
            request_obj.responded_at = timezone.now()
            request_obj.save()
            GuardianLinkRequestLog.objects.create(
                request=request_obj,
                event=GuardianLinkRequestLog.Event.REJECTED,
                actor=request.user,
                message="Learner rejected guardian link request.",
            )
            messages.info(request, "Link rejected. Your guardian will not be able to see your progress.")
        return redirect(request.user.get_dashboard_url())

    return render(request, "accounts/guardian_link_confirm.html", {"request_obj": request_obj})


def login_view(request):'''

start, end = match.span()
# preserve the login_view start line
footer = text[end- len('def login_view(request):') :]
text = text[:start] + replacement + footer
path.write_text(text, encoding='utf-8')
print('Patched accounts/views.py successfully.')
print('--- Block after patch ---')
print(text[text.index('def register_tutor(request):'):text.index('def login_view(request):')+len('def login_view(request):')])
