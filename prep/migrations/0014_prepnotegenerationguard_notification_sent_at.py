from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prep", "0013_prepnotegenerationguard"),
    ]

    operations = [
        migrations.AddField(
            model_name="prepnotegenerationguard",
            name="notification_sent_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
