from django.db import migrations


def mark_legacy_users_verified(apps, schema_editor):
    """Preserve access for accounts created before email verification existed."""
    User = apps.get_model("accounts", "User")
    User.objects.filter(is_email_verified=False).update(is_email_verified=True)


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0005_profile_experience_summary_profile_headline_and_more"),
    ]

    operations = [
        migrations.RunPython(mark_legacy_users_verified, migrations.RunPython.noop),
    ]
