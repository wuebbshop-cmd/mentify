from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prep", "0024_prepquestion_automated_review_statuses"),
    ]

    operations = [
        migrations.AddField(
            model_name="prepdocumentvisual",
            name="context_crop",
            field=models.FileField(blank=True, upload_to="prep/visual-context/%Y/%m/"),
        ),
    ]
