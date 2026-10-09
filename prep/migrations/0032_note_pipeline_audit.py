from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prep", "0031_prepcreditreservation"),
    ]

    operations = [
        migrations.AddField(
            model_name="preptopicnotesjob",
            name="provider_usage",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name="preptopicnotesjob",
            name="model_name",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="prepnoterepair",
            name="repair_log",
            field=models.JSONField(blank=True, default=list),
        ),
    ]
