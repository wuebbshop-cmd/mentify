"""assignments/forms.py"""
from django import forms
from .models import Assignment, Submission, Grade


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["title", "description", "due_date", "max_score", "is_published"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "due_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "max_score": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class SubmissionForm(forms.ModelForm):
    submission_file = forms.FileField(
        required=False,
        label="Upload File (optional)",
        widget=forms.ClearableFileInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Submission
        fields = ["text_response"]
        widgets = {
            "text_response": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 8,
                "placeholder": "Type your answer, paste code, or describe your solution here...",
            }),
        }


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["total_score", "tutor_comment"]
        widgets = {
            "total_score": forms.NumberInput(attrs={"class": "form-control", "step": "0.5"}),
            "tutor_comment": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }
