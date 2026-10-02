from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prep", "0021_prepdocumentvisual_reconstruction_proposal"),
    ]

    operations = [
        migrations.AddField(
            model_name="prepdocument",
            name="validation_report",
            field=models.JSONField(blank=True, default=dict),
        ),
    ]