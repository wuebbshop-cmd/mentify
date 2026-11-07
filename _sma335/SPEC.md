# SMA 335 note-authoring specification

Every note must pass `_sma335/apply.py` before it is stored. Read this file completely before writing.

## 1. Required structure — exactly these five H2 headings, in this order

```
## 1. Foundational Concepts, Definitions, and Axioms
## 2. Theorems, Lemmas, and Analytical Properties
## 3. Formal Proofs, Derivations, and Methods
## 4. Representative Worked Examples and Solutions
## 5. Mathematical Extensions, Limits, and Common Errors
```

Character-for-character, including the numbering and the trailing section-5 wording. The note must begin
with the first heading (no title line, no preamble). Use `###` subheadings freely inside each section.
Section 5 needs real prose after its heading, not just a heading.

## 2. Length

At least **5,200 words** per note; aim 5,500–6,500. Every subtopic of the topic must be taught.

## 3. Mathematics formatting — this is where notes fail most often

- **Display maths**: `$$` alone on its own line, the expression on the following lines, then `$$` alone on
  its own line. Blank line before the opening `$$` and blank line after the closing `$$`.
  Never a blank line *inside* the block. Never `$$ expression $$` on one line.
- **Inline maths**: `$...$` on one physical line, with a space before and after
  (`the derivative $\frac{dy}{dx}$ is`, never `the derivative$\frac{dy}{dx}$is`).
- Use only `$` and `$$`. **Never** use `\(`, `\)`, `\[`, `\]`.
- **Never split a base from its exponent or subscript across delimiters.** Write `$x^{2}$`, `$e^{3x}$`,
  `$y_{(n+1)}$`, `$\frac{d^{2}y}{dx^{2}}$`. Never `\(c_2h\)^2`, never `$x$_i`.
- Every `\left` needs its matching `\right` in the same block; braces must balance.
- No line may end with a lone backslash.
- **Never write a currency amount as `\$`.** The renderer treats it as a broken delimiter.
- Multi-line derivations: use separate `$$` blocks, one step per block. If you need alignment, use
  `\begin{aligned}...\end{aligned}` **inside** a `$$` block only.
- Standard LaTeX only: `\frac`, `\dfrac`, `\sqrt`, `\int`, `\sum`, `\prod`, `\lim`, `\partial`, `\nabla`,
  `\bar`, `\hat`, `\dot`, `\ddot`, `\prime`, `\left(`, `\right)`, `\cdot`, `\times`, `\pm`, `\mp`,
  `\le`, `\ge`, `\ne`, `\approx`, `\equiv`, `\to`, `\infty`, `\ln`, `\log`, `\sin`, `\cos`, `\tan`,
  `\sec`, `\cot`, `\sinh`, `\cosh`, `\tanh`, `\arcsin`, `\exp`, `\text{...}`, Greek letters.
- Never use `\begin{array}`, `\begin{matrix}` or similar outside display maths.

## 4. Forbidden content

- No fenced code blocks (```` ``` ````) in any language.
- No HTML, `<img>`, `[[VISUAL:...]]`, mermaid, tikz.
- No figure callouts: never "see the graph below", "the figure above shows", "refer to the diagram".
  Describe everything in prose.
- No source meta-language: never "according to the source", "the module states", "the notes say".
  Teach the mathematics directly.
- Do not copy sentences from the course PDF. Write original exposition.

## 5. Markdown tables

Header row, separator row of `---` cells with the **same** column count, then rows with that same count.
No dangling `|`, no incomplete final row. Tables are the right way to present finite-difference tables,
variation-of-parameters coefficient systems, and eigenvalue work.

## 6. Worked examples — never prose paragraphs

Mathematical work is **never** written as a paragraph. For each example use:

```
### 4.1 Problem: <short statement>

### 4.2 Solution: <approach>

Step 1. <what is done and why>

$$
<formula>
$$

Step 2. ...
```

Every algebraic stage goes in its own display block; prose only says what the step does and why it is valid.
State the final answer explicitly and check it (substitute back, or verify the order/degree, or verify
the initial condition).

## 7. Level differentiation

- **level_1 — Core Concepts (gentle).** Open Section 1 with an everyday analogy *before* any mathematical
  symbol: the words "Imagine", "Think of", or "Picture" must appear before the first `$`. Small numbers,
  names for every symbol in words, short steps, and a beginner-misconceptions list in Section 5.
- **level_2 — In-Depth (rigorous).** Complete definitions, precise theorem statements with hypotheses,
  full derivations, and multi-step worked examples with interpretation of the result.
- **level_3 — Exam Focus.** Same five sections, aimed at examination performance: high-yield results and
  their typical mark values, the shapes of questions asked, an explicit trap table, at least three complete
  model solutions written as numbered steps with per-step marking points, and a revision checklist plus
  time strategy in Section 5. Keep the mathematics just as complete as level 2.

## 8. Correctness — non-negotiable

- Every derivation must be valid; every solution must satisfy the differential equation it claims to solve.
- Verify finals: substitute the solution back, or differentiate it the required number of times and confirm.
- Recompute every numerical value (roots, coefficients, constants) before finishing.
- Do not invent notation the course does not use; where the course's source text is garbled by OCR, use the
  standard correct mathematics for that topic instead of reproducing the garble.

## 9. Self-check before finishing

From the repository root run:

```
C:\Users\adm\.vscode\.venv\Scripts\python.exe _sma335\apply.py --topic <topic_pk>
```

It must print `PASS` for all three levels with `words` at least 5200. Fix and re-run until it passes.
Never run `apply.py` without `--check` or `--topic`; publishing is not your job.
