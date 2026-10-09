from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("prep", "0032_note_pipeline_audit"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrepAssessmentIndexJob",
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
                (
                    "source_signature",
                    models.CharField(max_length=64),
                ),
                ("reconstruct_invalid", models.BooleanField(default=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("running", "Running"),
                            ("complete", "Complete"),
                            ("failed", "Failed"),
                            ("superseded", "Superseded"),
                        ],
                        db_index=True,
                        default="pending",
                        max_length=20,
                    ),
                ),
                (
                    "stage",
                    models.CharField(
                        choices=[
                            ("queued", "Queued"),
                            ("indexing", "Indexing"),
                            ("retry_wait", "Waiting to Retry"),
                            ("complete", "Complete"),
                            ("failed", "Failed"),
                            ("superseded", "Superseded"),
                        ],
                        default="queued",
                        max_length=20,
                    ),
                ),
                ("attempts", models.PositiveSmallIntegerField(default=0)),
                ("indexed_questions", models.PositiveIntegerField(default=0)),
                ("last_error", models.TextField(blank=True)),
                ("queued_at", models.DateTimeField(auto_now_add=True)),
                (
                    "next_attempt_at",
                    models.DateTimeField(db_index=True, default=django.utils.timezone.now),
                ),
                ("started_at", models.DateTimeField(blank=True, null=True)),
                ("completed_at", models.DateTimeField(blank=True, null=True)),
                (
                    "paper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assessment_index_jobs",
                        to="prep.preppaper",
                    ),
                ),
                (
                    "source_document",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assessment_index_jobs",
                        to="prep.prepdocument",
                    ),
                ),
            ],
            options={
                "ordering": ["queued_at", "id"],
                "constraints": [
                    models.UniqueConstraint(
                        fields=("paper", "source_signature", "reconstruct_invalid"),
                        name="unique_prep_assessment_index_version",
                    ),
                ],
            },
        ),
    ]
