"""payments/forms.py"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, Profile
from courses.models import Cohort
from .models import Subscription


class CashPaymentForm(forms.Form):
    learner = forms.ModelChoiceField(
        queryset=User.objects.filter(role="learner").order_by("last_name", "first_name"),
        label="Learner",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    cohort = forms.ModelChoiceField(
        queryset=Cohort.objects.filter(status="active").select_related("course"),
        label="Cohort",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    amount_kes = forms.DecimalField(
        max_digits=10, decimal_places=2,
        label="Amount (KES)",
        widget=forms.NumberInput(attrs={"class": "form-control", "min": "0"})
    )
    note = forms.CharField(
        required=False,
        label="Note (optional)",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 2,
                                     "placeholder": "e.g. Paid cash on 21 Jul 2026"})
    )


class InlineLearnerCreationForm(UserCreationForm):
    """
    Minimal form to create a learner account inline during cash payment recording.
    """
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    phone = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "phone", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Role.LEARNER
        user.email = self.cleaned_data["email"]
        user.phone = self.cleaned_data.get("phone", "")
        if commit:
            user.save()
            Profile.objects.get_or_create(user=user)
        return user
