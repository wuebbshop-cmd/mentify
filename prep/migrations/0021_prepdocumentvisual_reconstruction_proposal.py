from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prep", "0020_prepdocument_page_evidence_prepdocumentvisual"),
    ]

    operations = [
        migrations.AddField(
            model_name="prepdocumentvisual",
            name="reconstruction_proposal",
            field=models.JSONField(blank=True, default=dict),
        ),
    ]