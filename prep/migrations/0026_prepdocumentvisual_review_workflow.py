from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("prep", "0025_prepdocumentvisual_context_crop"),
    ]

    operations = [
        migrations.AddField(
            model_name="prepdocumentvisual",
            name="reviewed_topic",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reviewed_visual_candidates",
                to="prep.preptopic",
            ),
        ),
        migrations.AddField(
            model_name="prepdocumentvisual",
            name="reviewed_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reviewed_prep_visuals",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="prepdocumentvisual",
            name="reviewed_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="prepdocumentvisual",
            name="review_notes",
            field=models.TextField(blank=True),
        ),
    ]