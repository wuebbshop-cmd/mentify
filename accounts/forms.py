"""accounts/forms.py — Registration, login, profile update forms."""
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, SetPasswordForm
from django.utils.translation import gettext_lazy as _

from .models import User, Profile


class LearnerRegistrationForm(UserCreationForm):
    """Self-registration form for learners, guardians, and tutors."""
    ROLE_CHOICES = [
        ("learner", "Learner / Student"),
        ("guardian", "Parent / Guardian"),
        ("tutor", "Tutor / Instructor"),
    ]

    first_name = forms.CharField(max_length=150, required=True, label="First Name")
    last_name = forms.CharField(max_length=150, required=True, label="Last Name")
    email = forms.EmailField(required=True, label="Email Address")
    role = forms.ChoiceField(choices=ROLE_CHOICES, initial="learner", label="I am joining as")
    phone = forms.CharField(
        max_length=20, required=False,
        label="Phone Number",
        help_text="Optional — E.164 format e.g. +254700000000"
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "role", "phone", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data.get("role", User.Role.LEARNER)
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
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }


class PasswordChangeForm(SetPasswordForm):
    """Change password for authenticated users."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
