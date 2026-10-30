from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("prep", "0040_prepstudentquestionunlock_prepstudentquizseen"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrepCourseRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("note", models.CharField(blank=True, max_length=300)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("open", "Open"),
                            ("fulfilled", "Fulfilled"),
                            ("declined", "Declined"),
                        ],
                        db_index=True,
                        default="open",
                        max_length=20,
                    ),
                ),
                ("resolution_note", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="requests",
                        to="prep.prepcourse",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="prep_course_requests",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Prep Course Request",
                "verbose_name_plural": "Prep Course Requests",
                "ordering": ["-created_at"],
                "indexes": [
                    models.Index(fields=["status", "created_at"], name="prep_prepco_status_8a1f2b_idx"),
                    models.Index(fields=["course", "status"], name="prep_prepco_course__4c7d19_idx"),
                ],
            },
        ),
    ]
