from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("prep", "0035_preptopicpdfartifact"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PrepTopicResource",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("url", models.URLField(max_length=500)),
                (
                    "resource_type",
                    models.CharField(
                        choices=[
                            ("youtube", "YouTube Video"),
                            ("video", "Video Lecture"),
                            ("article", "Reference Article / Paper"),
                            ("simulation", "Interactive Simulation / Lab"),
                            ("website", "Learning Website / Slides"),
                        ],
                        default="website",
                        max_length=30,
                    ),
                ),
                ("description", models.TextField(blank=True, default="")),
                ("thumbnail_url", models.URLField(blank=True, default="", max_length=500)),
                ("embed_id", models.CharField(blank=True, default="", help_text="e.g. YouTube video ID for embedded player", max_length=100)),
                ("is_approved", models.BooleanField(db_index=True, default=False)),
                ("reviewed_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="resources", to="prep.prepcourse")),
                ("submitted_by", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="submitted_prep_resources", to=settings.AUTH_USER_MODEL)),
                ("topic", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="resources", to="prep.preptopic")),
            ],
            options={
                "verbose_name": "Prep Topic Resource",
                "verbose_name_plural": "Prep Topic Resources",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="PrepTopicWikipedia",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("wikipedia_title", models.CharField(max_length=255)),
                ("extract", models.TextField(blank=True, default="", help_text="Concise definition/summary from Wikipedia")),
                ("canonical_url", models.URLField(blank=True, default="", max_length=500)),
                ("thumbnail_url", models.URLField(blank=True, default="", max_length=500)),
                ("description", models.CharField(blank=True, default="", max_length=255)),
                ("fetched_at", models.DateTimeField(auto_now=True)),
                ("topic", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="wikipedia_entry", to="prep.preptopic")),
            ],
            options={
                "verbose_name": "Prep Topic Wikipedia Entry",
                "verbose_name_plural": "Prep Topic Wikipedia Entries",
            },
        ),
    ]
