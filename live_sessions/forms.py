"""sessions/forms.py"""
from django import forms
from .models import LiveSession, Attendance


class LiveSessionForm(forms.ModelForm):
    class Meta:
        model = LiveSession
        fields = ["title", "scheduled_at", "duration_minutes", "meeting_link", "notes"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "scheduled_at": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
            "duration_minutes": forms.NumberInput(attrs={"class": "form-control", "min": 15}),
            "meeting_link": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://meet.google.com/xxx-xxxx-xxx",
            }),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


class MakeupSessionForm(forms.ModelForm):
    class Meta:
        model = LiveSession
        fields = ["title", "scheduled_at", "duration_minutes", "meeting_link", "notes"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "scheduled_at": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
            "duration_minutes": forms.NumberInput(attrs={"class": "form-control", "min": 15}),
            "meeting_link": forms.URLInput(attrs={"class": "form-control"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
