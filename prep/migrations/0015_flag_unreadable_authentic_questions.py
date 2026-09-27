import re

from django.db import migrations


def flag_unreadable_authentic_questions(apps, schema_editor):
    PrepQuestion = apps.get_model("prep", "PrepQuestion")
    private_use = re.compile(r"[\ue000-\uf8ff]")

    for question in PrepQuestion.objects.filter(question_type="authentic").iterator():
        source = question.question_latex or ""
        if private_use.search(source) or "\ufffd" in source:
            question.verification_status = "flagged"
            question.save(update_fields=["verification_status"])


class Migration(migrations.Migration):
    dependencies = [
        ("prep", "0014_prepnotegenerationguard_notification_sent_at"),
    ]

    operations = [
        migrations.RunPython(flag_unreadable_authentic_questions, migrations.RunPython.noop),
    ]
