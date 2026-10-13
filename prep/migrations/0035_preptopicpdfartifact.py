from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("prep", "0034_add_freemium_plan_and_upload_counter"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrepTopicPdfArtifact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("artifact_type", models.CharField(choices=[("notes", "Validated Topic Notes"), ("questions", "Authentic Past Questions and Answers")], max_length=20)),
                ("level", models.CharField(blank=True, max_length=20)),
                ("source_signature", models.CharField(blank=True, db_index=True, max_length=64)),
                ("published_signature", models.CharField(blank=True, max_length=64)),
                ("github_path", models.CharField(blank=True, max_length=500)),
                ("status", models.CharField(choices=[("pending", "Pending"), ("running", "Running"), ("ready", "Ready"), ("empty", "No Eligible Source Content"), ("failed", "Failed")], db_index=True, default="pending", max_length=20)),
                ("request_version", models.PositiveIntegerField(default=1)),
                ("attempts", models.PositiveSmallIntegerField(default=0)),
                ("last_error", models.TextField(blank=True)),
                ("queued_at", models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ("next_attempt_at", models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ("started_at", models.DateTimeField(blank=True, null=True)),
                ("completed_at", models.DateTimeField(blank=True, null=True)),
                ("topic", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="pdf_artifacts", to="prep.preptopic")),
            ],
            options={
                "ordering": ["queued_at", "id"],
                "constraints": [
                    models.UniqueConstraint(fields=("topic", "artifact_type", "level"), name="unique_prep_topic_pdf_artifact"),
                ],
            },
        ),
    ]
