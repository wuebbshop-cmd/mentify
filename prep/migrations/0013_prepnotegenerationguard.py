from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("prep", "0012_flag_malformed_generated_questions"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrepNoteGenerationGuard",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("level", models.CharField(max_length=20)),
                ("source_signature", models.CharField(db_index=True, max_length=64)),
                ("failed_attempts", models.PositiveSmallIntegerField(default=0)),
                ("status", models.CharField(choices=[("open", "Retry permitted"), ("needs_review", "Needs tutor/admin review")], db_index=True, default="open", max_length=20)),
                ("last_error", models.TextField(blank=True)),
                ("last_failed_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("topic", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="note_generation_guards", to="prep.preptopic")),
            ],
            options={"ordering": ["-updated_at"]},
        ),
        migrations.AddConstraint(
            model_name="prepnotegenerationguard",
            constraint=models.UniqueConstraint(fields=("topic", "level", "source_signature"), name="unique_prep_note_generation_guard"),
        ),
    ]
