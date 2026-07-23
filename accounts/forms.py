"""accounts/forms.py - Registration, login, profile update forms."""
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, SetPasswordForm, PasswordResetForm
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from .models import User, Profile


def build_username_from_email(email: str, *, existing_user: User | None = None) -> str:
    """Create a safe, unique username from an email address."""
    base = (email or "").split("@", 1)[0].strip().lower()
    base = "".join(c for c in base if c.isalnum() or c in "._-")[:30] or "user"
    base = base.rstrip("._-") or "user"

    candidate = base
    counter = 2
    qs = User.objects.filter(username__iexact=candidate)
    if existing_user is not None:
        qs = qs.exclude(pk=existing_user.pk)

    while qs.exists():
        candidate = f"{base}{counter}"
        counter += 1
        qs = User.objects.filter(username__iexact=candidate)
        if existing_user is not None:
            qs = qs.exclude(pk=existing_user.pk)

    return candidate


class LearnerRegistrationForm(UserCreationForm):
    """Self-registration form for learners, guardians, and tutors."""

    first_name = forms.CharField(max_length=150, required=True, label="First Name")
    last_name = forms.CharField(max_length=150, required=True, label="Last Name")
    email = forms.EmailField(required=True, label="Email Address")
    phone = forms.CharField(
        max_length=20, required=False,
        label="Phone Number",
        help_text="Optional - E.164 format e.g. +254700000000",
    )
    agree_to_terms = forms.BooleanField(
        required=True,
        label="I agree to the Terms and Privacy Policy",
        error_messages={"required": "You must agree to the terms and privacy policy to continue."},
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone", "password1", "password2", "agree_to_terms"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("username", None)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        self.fields["agree_to_terms"].widget.attrs["class"] = "form-check-input"

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if email:
            cleaned_data["username"] = build_username_from_email(email)
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone = self.cleaned_data.get("phone", "")
        user.username = self.cleaned_data.get("username") or build_username_from_email(user.email, existing_user=user)
        if commit:
            user.save()
            Profile.objects.get_or_create(user=user)
        return user


class TutorRegistrationForm(UserCreationForm):
    """Admin-created tutor account form."""
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "phone", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Role.TUTOR
        user.email = self.cleaned_data["email"]
        user.phone = self.cleaned_data.get("phone", "")
        if commit:
            user.save()
            Profile.objects.get_or_create(user=user)
        return user


class GuardianChildLinkForm(forms.Form):
    email_or_username = forms.CharField(
        max_length=255,
        label="Learner email or username",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "learner@example.com or username",
        }),
    )
    notes = forms.CharField(
        required=False,
        label="Notes for learner",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 3,
            "placeholder": "Optional message to help the learner recognize you.",
        }),
    )

    def clean_email_or_username(self):
        identifier = self.cleaned_data["email_or_username"].strip()
        learner = User.objects.filter(
            Q(email__iexact=identifier) | Q(username__iexact=identifier),
            role=User.Role.LEARNER,
        ).first()
        if not learner:
            raise forms.ValidationError(
                "No learner found with that email or username. Please check and try again."
            )
        return learner

    def clean(self):
        cleaned_data = super().clean()
        learner = cleaned_data.get("email_or_username")
        if learner and learner.role != User.Role.LEARNER:
            raise forms.ValidationError("Selected account is not a learner.")
        return cleaned_data


class MentifyLoginForm(AuthenticationForm):
    """Custom login form styled for Mentify."""
    username = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={"autofocus": True, "class": "form-control", "placeholder": "you@example.com"})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "••••••••"})
    )


class MentifyPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "you@example.com",
            "autofocus": True,
        })


class MentifySetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class ProfileUpdateForm(forms.ModelForm):
    """Let users update their bio, county, school etc."""
    class Meta:
        model = Profile
        fields = [
            "headline",
            "specialty",
            "bio",
            "experience_summary",
            "date_of_birth",
            "county",
            "school",
            "class_level",
        ]
        widgets = {
            "headline": forms.TextInput(attrs={"class": "form-control", "placeholder": "Short profile headline"}),
            "specialty": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Python, CBE Mathematics, AI, Robotics"}),
            "bio": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
            "experience_summary": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
            "date_of_birth": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "county": forms.TextInput(attrs={"class": "form-control"}),
            "school": forms.TextInput(attrs={"class": "form-control"}),
            "class_level": forms.TextInput(attrs={"class": "form-control"}),
        }


class UserUpdateForm(forms.ModelForm):
    """Update core user fields (name, phone)."""
    avatar_image = forms.ImageField(
        required=False,
        label="Profile image",
        help_text="Uploads to the configured GitHub repo and uses it as your profile image.",
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["avatar_image"].widget.attrs["class"] = "form-control"

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        exists = User.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists()
        if exists:
            raise forms.ValidationError("Another account already uses this email address.")
        return email


class PasswordChangeForm(SetPasswordForm):
    """Change password for authenticated users."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, label="Your name")
    email = forms.EmailField(label="Email address")
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 6, "class": "form-control"}), label="How can we help?")
    consent = forms.BooleanField(
        required=True,
        label="I consent to being contacted about my request",
        error_messages={"required": "Please confirm that you want us to contact you."},
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")
        self.fields["consent"].widget.attrs["class"] = "form-check-input"
