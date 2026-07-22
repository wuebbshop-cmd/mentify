"""accounts/forms.py - Registration, login, profile update forms."""
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, SetPasswordForm
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from .models import User, Profile


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

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("username", None)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if email:
            cleaned_data["username"] = self._make_username(email)
        return cleaned_data

    @staticmethod
    def _make_username(email: str) -> str:
        base = email.split("@")[0]
        base = "".join(c if c.isalnum() or c in "._-" else "_" for c in base)[:30] or "user"
        candidate = base
        suffix = 1
        while User.objects.filter(username=candidate).exists():
            candidate = f"{base}{suffix}"
            suffix += 1
        return candidate

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone = self.cleaned_data.get("phone", "")
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


class ProfileUpdateForm(forms.ModelForm):
    """Let users update their bio, county, school etc."""
    class Meta:
        model = Profile
        fields = ["bio", "date_of_birth", "county", "school", "class_level"]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
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
        fields = ["first_name", "last_name", "phone"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["avatar_image"].widget.attrs["class"] = "form-control"


class PasswordChangeForm(SetPasswordForm):
    """Change password for authenticated users."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
