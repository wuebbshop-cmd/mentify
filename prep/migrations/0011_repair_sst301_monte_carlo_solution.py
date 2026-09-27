from django.db import migrations


def repair_monte_carlo_solution(apps, schema_editor):
    PrepQuestion = apps.get_model("prep", "PrepQuestion")

    broken_condition = "if (!is.numeric(N) |\n| length(N) != 1 |\n| N < 100) {"
    corrected_condition = (
        "if (!is.numeric(N) || length(N) != 1 || is.na(N) ||\n"
        "      N < 100 || N != as.integer(N)) {"
    )
    questions = PrepQuestion.objects.filter(
        question_latex__icontains="monte_carlo_pi",
        paper__course__code__iexact="SST 301",
    )
    for question in questions:
        corrected_solution = question.solution_latex.replace(broken_condition, corrected_condition)
        if corrected_solution != question.solution_latex:
            question.solution_latex = corrected_solution
            question.save(update_fields=["solution_latex"])


class Migration(migrations.Migration):
    dependencies = [
        ("prep", "0010_alter_prepwallet_current_plan"),
    ]

    operations = [
        migrations.RunPython(repair_monte_carlo_solution, migrations.RunPython.noop),
    ]
