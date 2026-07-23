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
        label="Upload video",
        help_text="(ensure the video uploaded is to a reasonable size and length; Maximum video duration: 45 minutes and Maximum file size: 1.5 GB, and 1080p (Full HD) resolution; anything more than these is declined)",
        widget=forms.ClearableFileInput(attrs={"class": "form-control", "accept": "video/*"}),
    )

    class Meta:
        model = VideoAsset
        fields = ["video_file", "bunny_video_id", "bunny_library_id", "duration_seconds"]
        widgets = {
            "bunny_video_id": forms.HiddenInput(),
            "bunny_library_id": forms.HiddenInput(),
            "duration_seconds": forms.HiddenInput(),
        }

    def clean_video_file(self):
        video_file = self.cleaned_data.get("video_file")
        if video_file:
            if not getattr(video_file, "content_type", "").startswith("video/"):
                raise forms.ValidationError("Upload a valid video file.")
            max_size = 1.5 * 1024 * 1024 * 1024
            if video_file.size > max_size:
                raise forms.ValidationError("File size exceeds the maximum limit of 1.5 GB.")
        return video_file

    def clean(self):
        cleaned_data = super().clean()
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
