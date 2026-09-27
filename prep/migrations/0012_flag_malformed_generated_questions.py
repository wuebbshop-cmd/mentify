import re

from django.db import migrations


def _has_split_inline_math(source):
    source = re.sub(r"```[\s\S]*?```", "", source or "")
    source = re.sub(r"\$\$[\s\S]*?\$\$", "", source)
    opening = None
    backslashes = 0
    for index, char in enumerate(source):
        if char == "\\":
            backslashes += 1
            continue
        escaped = backslashes % 2 == 1
        backslashes = 0
        if char != "$" or escaped:
            continue
        if (index > 0 and source[index - 1] == "$") or (
            index + 1 < len(source) and source[index + 1] == "$"
        ):
            continue
        if opening is None:
            opening = index
        else:
            if "\n" in source[opening + 1:index] or "\r" in source[opening + 1:index]:
                return True
            opening = None
    return False


def flag_malformed_generated_questions(apps, schema_editor):
    PrepQuestion = apps.get_model("prep", "PrepQuestion")
    for question in PrepQuestion.objects.filter(
        question_type="generated",
        verification_status="verified",
    ).iterator():
        source = f"{question.question_latex or ''}\n{question.solution_latex or ''}"
        has_bad_r_operator = bool(re.search(r"```(?:r|rscript)\s*\n[\s\S]*?\|\s*\n\s*\|", source, re.IGNORECASE))
        has_blank_display_break = bool(re.search(r"\$\$[\s\S]*?\n[ \t]*\n[\s\S]*?\$\$", source))
        if has_bad_r_operator or has_blank_display_break or _has_split_inline_math(source):
            question.verification_status = "flagged"
            question.save(update_fields=["verification_status"])


class Migration(migrations.Migration):
    dependencies = [
        ("prep", "0011_repair_sst301_monte_carlo_solution"),
    ]

    operations = [
        migrations.RunPython(flag_malformed_generated_questions, migrations.RunPython.noop),
    ]
