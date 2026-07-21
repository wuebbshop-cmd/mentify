"""content/forms.py"""
from django import forms
from .models import Lesson, VideoAsset, Resource


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ["title", "description", "order", "is_published"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "order": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class VideoAssetForm(forms.ModelForm):
    class Meta:
        model = VideoAsset
        fields = ["bunny_video_id", "bunny_library_id", "duration_seconds"]
        widgets = {
            "bunny_video_id": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "e.g. abc12345-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
            }),
            "bunny_library_id": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Leave blank to use platform default"
            }),
            "duration_seconds": forms.NumberInput(attrs={"class": "form-control"}),
        }


class ResourceForm(forms.ModelForm):
    pdf_file = forms.FileField(
        required=False,
        label="Upload PDF",
        widget=forms.ClearableFileInput(attrs={"class": "form-control", "accept": ".pdf"})
    )

    class Meta:
        model = Resource
        fields = ["title", "resource_type", "external_url"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "resource_type": forms.Select(attrs={"class": "form-select"}),
            "external_url": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://..."}),
        }
