from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("prep", "0015_flag_unreadable_authentic_questions"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrepNoteRepair",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("level", models.CharField(max_length=20)),
                ("source_signature", models.CharField(db_index=True, max_length=64)),
                ("cache_key", models.CharField(max_length=255)),
                ("original_content", models.TextField()),
                ("current_content", models.TextField()),
                ("validation_issues", models.JSONField(default=list)),
                ("attempts", models.PositiveSmallIntegerField(default=0)),
                ("status", models.CharField(choices=[("open", "Repair Pending"), ("validated", "Repair Validated"), ("needs_review", "Needs Manual Review")], db_index=True, default="open", max_length=20)),
                ("last_error", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("topic", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="note_repairs", to="prep.preptopic")),
            ],
            options={"ordering": ["-updated_at"]},
        ),
        migrations.AddConstraint(
            model_name="prepnoterepair",
            constraint=models.UniqueConstraint(fields=("topic", "level", "source_signature"), name="unique_prep_note_repair"),
        ),
    ]