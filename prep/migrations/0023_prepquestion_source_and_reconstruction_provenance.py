import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prep", "0022_prepdocument_validation_report"),
    ]

    operations = [
        migrations.AddField(
            model_name="prepquestion",
            name="source_document",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sourced_questions",
                to="prep.prepdocument",
            ),
        ),
        migrations.AddField(
            model_name="prepquestion",
            name="source_page_number",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="prepquestion",
            name="extraction_confidence",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="prepquestion",
            name="reconstructed_from",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="adapted_reconstructions",
                to="prep.prepquestion",
            ),
        ),
        migrations.AddField(
            model_name="prepquestion",
            name="reconstruction_metadata",
            field=models.JSONField(blank=True, default=dict),
        ),
    ]