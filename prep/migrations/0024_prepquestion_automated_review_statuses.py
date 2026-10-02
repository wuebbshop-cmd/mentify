from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prep", "0023_prepquestion_source_and_reconstruction_provenance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prepquestion",
            name="verification_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending Verification"),
                    ("verified", "Verified (Tutor / SymPy)"),
                    ("auto_validated", "Auto-validated source extraction"),
                    ("reconstructed", "AI-reconstructed equivalent"),
                    ("flagged", "Flagged for Correction"),
                ],
                default="verified",
                max_length=20,
            ),
        ),
    ]