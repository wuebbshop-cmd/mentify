# SST 101 note-rebuild specification

Every rebuilt note must pass the app's own validator. Read this file completely before writing.

## 1. Required structure (exactly these five H2 headings, in this order)

```
## 1. Foundational Concepts, Definitions, and Axioms
## 2. Theorems, Lemmas, and Analytical Properties
## 3. Formal Proofs, Derivations, and Methods
## 4. Representative Worked Examples and Solutions
## 5. Mathematical Extensions, Limits, and Common Errors
```

The heading text must match character for character (`## 5. Mathematical Extensions, Limits, and Common Errors`).
You may use `###` subheadings freely inside each section. The last section must contain at least one
substantial paragraph after its heading (a heading alone is rejected).

## 2. Length

- Each note must be **at least 5,200 words**; aim for 5,500–6,000.
- Coverage must be broad: every subtopic of the topic must be taught, with formulas, derivations, and worked examples.

## 3. Mathematics formatting (strictly enforced)

- Display maths: `$$` alone on its own line, then the expression, then `$$` alone on its own line.
  Put a blank line before the opening `$$` and after the closing `$$`. Never leave a blank line inside the block.
- Inline maths: `$...$`, on a single physical line, always with a space before and after
  (write `the mean $\bar{x}$ is`, never `the mean$\bar{x}$is`).
- Use only `$` and `$$`. Do **not** use `\(`, `\)`, `\[` or `\]`.
- Never split a base from its exponent or subscript across delimiters. Write `$x^{2}$`, `$c_2h^{2}$`,
  `$x_{(i+1)}$` — not `\(c_2h\)^2` and not `$x$_i$.
- Every `\left` needs a matching `\right` inside the same block, and braces must balance.
- Do not end a line with a lone backslash.
- **Never write a currency symbol as `\$` inside maths.** The app's delimiter normalizer treats `\$` as a broken
  delimiter and the note will be rejected at display time. Write amounts without a currency symbol
  ("100 shillings", "400 units of currency") or put the currency in prose outside the maths.
- Standard LaTeX only: `\frac`, `\sqrt`, `\sum`, `\int`, `\bar`, `\hat`, `\sigma`, `\mu`, `\times`,
  `\approx`, `\le`, `\ge`, `\ne`, `\mid`, `\cdot`, `\text{...}`, `\begin{aligned}...\end{aligned}` (inside display maths only).

## 4. Forbidden content

- No fenced code blocks at all (```` ``` ````), in any language.
- No HTML tags, no `<img>`, no `[[VISUAL:...]]` markers, no mermaid, no tikz.
- No phrase such as "see the table below", "the figure above shows", "refer to the graph",
  "as shown in the chart". Explain everything in prose instead.
- No meta-language about sources: never write "according to the approved source", "the syllabus states",
  "the uploaded notes say", "this document lists". Teach the subject directly.
- No course-outline dump: do not reproduce a syllabus list of topics as the body of a section.
- Do not copy sentences verbatim from the course PDFs. Write original teaching prose that covers the
  same mathematics.

## 5. Markdown tables

Every table needs a header row, a separator row of `---` cells with the **same column count**, and data
rows with that same column count. Do not leave a trailing incomplete row or a dangling `|`.

## 6. Worked examples

- Worked mathematics is **never** written as a prose paragraph. Use a heading per example
  (`### 4.1 Problem: ...`, `### 4.2 Solution: ...`) and then numbered steps
  (`Step 1.`, `Step 2.`, ...).
- Each algebraic stage goes in its own display-math block; prose only says what the step does and why.
- Every numerical example must be arithmetically correct. Recompute each value before finishing.

## 7. Level differentiation

- **level_1 — Core Concepts (gentle).** Open with an everyday analogy *before* any mathematical symbol
  (words such as "Imagine", "Think of", "Picture" must appear before the first `$`). Plain language,
  small numbers, short steps, explicit warnings about common beginner mistakes.
- **level_2 — In-Depth (rigorous).** Full definitions, statements of theorems, complete derivations,
  and multi-step worked examples with interpretation.
- **level_3 — Exam Focus.** Same five sections, but aimed at examination performance: high-yield results,
  question patterns and traps, one or two complete model solutions with marking points, and a
  revision/time-strategy checklist in Section 5. Keep it just as mathematically complete.

## 8. Grounding

- Preserve the sound teaching content of the existing note for that topic and level (it is provided to you);
  reorganise it into the five required sections and extend it until the coverage is complete.
- Ground new material in the lesson digests and past-paper text that accompany the topic. Where the course
  material does not cover a syllabus subtopic (for example sampling designs, confidence intervals,
  hypothesis tests, or named distributions), teach the standard, correct theory for that subtopic and keep
  notation conventional.

## 9. Self-check before finishing

Run, from the repository root:

```
C:\Users\adm\.vscode\.venv\Scripts\python.exe _sst101\apply.py --check <topic_pk>_<level>
```

It must print `PASS` with `words` at least 5200. Fix every reported issue and re-run until it passes for
all three levels you were asked to write. Do **not** run the script without `--check`; publishing is not
your job.
