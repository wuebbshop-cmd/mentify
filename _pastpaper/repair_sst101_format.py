"""Surgical formatting/content repairs for SST 101 past-paper rows."""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
os.chdir(BASE_DIR)
sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django

django.setup()

from prep.models import PrepQuestion

OUT = BASE_DIR / "_pastpaper" / "sst101_format_backup_40.json"

TEXT = {
    785: """The scores of candidates in an entrance examination, graded on a scale from 0 to 100, are recorded in the table below.

| Class Boundaries | Number of students |
| --- | --- |
| 0-10 | 10 |
| 10-20 | 15 |
| 20-30 | 10 |
| 30-40 | 21 |
| 40-50 | 33 |
| 50-60 | 40 |
| 60-70 | 25 |
| 70-80 | 12 |
| 80-90 | 8 |
| 90-100 | 1 |

(a) Calculate the arithmetic mean using:

(i) The direct method **(4 marks)**

(ii) An assumed mean of 40 **(4 marks)**

(iii) The coding method **(4 marks)**

(b) Calculate $Q_1$, $Q_2$, and $Q_3$. **(6 marks)**

(c) Calculate the semi-interquartile range. **(2 marks)**""",
    786: """Two students were graded in 11 subjects, and their results are recorded in the table below.

| Subject | Benny | Flora |
| --- | --- | --- |
| 1 | 3 | 6 |
| 2 | 11 | 10 |
| 3 | 12 | 10 |
| 4 | 10 | 4 |
| 5 | 12 | 4 |
| 6 | 10 | 5 |
| 7 | 4 | 8 |
| 8 | 10 | 9 |
| 9 | 2 | 1 |
| 10 | 0 | 6 |
| 11 | 4 | 5 |

(a) Calculate the coefficient of variation for Benny. **(4 marks)**

(b) Calculate the coefficient of variation for Flora. **(4 marks)**

(c) Which student is least consistent? **(4 marks)**

(d) Calculate the second moment about the mean for Benny. **(4 marks)**

(e) Calculate the second moment about the mean for Flora. **(4 marks)**""",
    810: "A bar chart shows the distribution of students' favourite programming languages in a class: Python (45%), R (25%), Java (20%), and C++ (10%). Draw a vertical bar chart for these data.",
    811: "A bar chart is used to summarize survey results on students' preferred study times: Morning, Afternoon, Evening, and Night. Discuss two possible misrepresentations that could occur if the chart is poorly constructed, such as unequal bar widths or a non-zero baseline. Explain why these issues affect the interpretation of the data.",
    812: "Two bar charts compare student club membership in two faculties. Faculty A has Debate (40), Music (35), and Sports (50). Faculty B has Debate (60), Music (70), and Sports (55). Draw side-by-side bar charts for the two faculties. Comment on the similarities and differences in club popularity.",
    813: """The marks obtained by 40 students in a mathematics test are grouped as follows.

| Marks | Frequency |
| --- | --- |
| 0-10 | 3 |
| 10-20 | 7 |
| 20-30 | 10 |
| 30-40 | 8 |
| 40-50 | 12 |

Construct a histogram to represent the data.""",
    815: """A random sample of 100 names was drawn from a database. The distribution of the lengths of the names is as follows:

| Number of letters | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Frequency | 3 | 10 | 18 | 20 | 18 | 12 | 8 | 4 | 5 | 2 |

(a) Calculate the first four moments about the mean.

(b) Calculate the coefficient of skewness and comment.

(c) Calculate the coefficient of kurtosis and comment.""",
    816: """The ages $x$ (in years) and heights $y$ (in centimetres) of 10 boys are given below.

| $x$ | 6.6 | 6.8 | 6.9 | 7.8 | 7.8 | 8.2 | 10.1 | 11.4 | 12.8 | 13.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $y$ | 119 | 116 | 116 | 124 | 122 | 123 | 135 | 151 | 141 | 140 |

(i) Calculate the regression equation of $y$ on $x$.

(ii) Estimate the height of a boy aged 9.0 years.""",
    834: """Consider the following frequency distribution table.

| Class Interval | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 |
| --- | --- | --- | --- | --- | --- | --- |
| Frequency | 5 | 10 | 14 | 10 | 6 | 5 |

(a) Find the mean and the standard deviation by changing both the location, using an assumed mean of 35, and the scale, using the common class width. **(7 marks)**

(b) Find:

(i) The mode.

(ii) The median.

(iii) The interquartile range.

(iv) The coefficient of variation based on the standard deviation.

(v) The coefficient of skewness based on quartiles. **(13 marks)**""",
    838: """Obtain the equation of the line of best fit by the least-squares method for the following data.

| $X$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $Y$ | 2 | 1 | 3 | 2 | 4 | 3 | 5 |""",
    839: """The following table shows classes and frequencies.

| Class | 5-7 | 8-10 | 11-13 | 14-16 | 17-19 | 20-22 | 23-25 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Frequency | 2 | 4 | 8 | 7 | 5 | 3 | 1 |

Calculate:

(a) The median and mode.

(b) The first and third quartiles.

(c) The 7th and 84th percentiles.

(d) The mean and standard deviation using an assumed mean $A=12$.

(e) Both Pearson coefficients of skewness.

(f) Bowley's coefficient of skewness.""",
}


FOOTER_PATTERNS = (
    r"\n+\*\*INVOLVEMENT IN ANY EXAMINATION IRREGULARITY SHALL LEAD TO DISCONTINUATION\*\*.*\Z",
    r"\n+\*INVOLVEMENT IN ANY EXAMINATION IRREGULARITY SHALL LEAD TO DISCONTINUATION\*.*\Z",
    r"\n+\*\*Page \d+(?: of \d+)?\*\*.*\Z",
)


def main() -> None:
    ids = set(TEXT)
    rows = list(PrepQuestion.objects.filter(id__in=ids))
    backup = {
        str(q.id): {
            "question_latex": q.question_latex,
            "verification_status": q.verification_status,
        }
        for q in rows
    }
    OUT.write_text(json.dumps(backup, ensure_ascii=False, indent=2), encoding="utf-8")

    for q in rows:
        text = TEXT.get(q.id, q.question_latex)
        text = re.sub(r"^[-]+[*]{2}\s*", "", text.strip())
        for pattern in FOOTER_PATTERNS:
            text = re.sub(pattern, "", text.strip(), flags=re.I | re.S)
        text = text.replace("\ufffd", "-")
        PrepQuestion.objects.filter(pk=q.id).update(
            question_latex=text.strip(),
            verification_status="reconstructed",
        )

    for q in PrepQuestion.objects.filter(
        topic_id__in=[140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]
    ):
        text = q.question_latex or ""
        cleaned = text.strip()
        cleaned = re.sub(r"^[-]+[*]{2}\s*", "", cleaned)
        for pattern in FOOTER_PATTERNS:
            cleaned = re.sub(pattern, "", cleaned.strip(), flags=re.I | re.S)
        cleaned = cleaned.replace("\ufffd", "-")
        if cleaned != text:
            PrepQuestion.objects.filter(pk=q.id).update(question_latex=cleaned)

    print(f"format_repaired={len(rows)} backup={OUT}")


if __name__ == "__main__":
    main()
