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
    video_file = forms.FileField(
        required=False,
        label="Upload Video",
        widget=forms.ClearableFileInput(attrs={"class": "form-control", "accept": "video/*"}),
    )

    class Meta:
        model = VideoAsset
        fields = ["video_file", "bunny_video_id", "bunny_library_id", "duration_seconds"]
        widgets = {
            "bunny_video_id": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Filled automatically after upload"
            }),
            "bunny_library_id": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Leave blank to use platform default"
            }),
            "duration_seconds": forms.NumberInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        video_file = cleaned_data.get("video_file")
        bunny_video_id = cleaned_data.get("bunny_video_id")
        if video_file and not getattr(video_file, "content_type", "").startswith("video/"):
            raise forms.ValidationError("Upload a valid video file.")
        if not video_file and not bunny_video_id and not self.instance.pk:
            return cleaned_data
        return cleaned_data


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

    def clean(self):
        cleaned_data = super().clean()
        resource_type = cleaned_data.get("resource_type")
        pdf_file = cleaned_data.get("pdf_file")
        external_url = cleaned_data.get("external_url")
        if resource_type == Resource.ResourceType.PDF and not pdf_file:
            raise forms.ValidationError("Upload a PDF file for PDF resources.")
        if resource_type == Resource.ResourceType.LINK and not external_url:
            raise forms.ValidationError("Add a URL for link resources.")
        return cleaned_data
