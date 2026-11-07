# SCS 209 note-authoring specification

Every note must pass `_scs209/apply.py` before it is stored. Read this file completely before writing.

SCS 209 is a **computing** course. Its notes are technical prose plus real code and session output, not
mathematics.

## 1. Required structure — exactly these five H2 headings, in this order

```
## 1. Concept and Use Case
## 2. Data, Syntax, and Core Concepts
## 3. Methods and Operations
## 4. Worked Implementation from the Notes
## 5. Testing, Interpretation, and Common Errors
```

Character-for-character. The note must begin with the first heading — no title line, no preamble.
Use `###` subheadings freely. Section 5 needs real prose after the heading.

## 2. Length

At least **5,200 words** per note; aim 5,500–6,500. Every subtopic of the topic must be taught.

## 3. Code blocks — allowed here, and required to be valid

This course **permits** fenced code. Rules:

- Every fence must declare a language from this list (lowercase):
  `apache`, `bash`, `conf`, `css`, `html`, `http`, `ini`, `java`, `javascript`, `js`, `json`,
  `markdown`, `nginx`, `php`, `plaintext`, `powershell`, `python`, `sh`, `shell`, `sql`, `text`,
  `typescript`, `ts`, `xml`, `yaml`.
- A fence with no language, or an unknown language, is a hard failure.
- Fences must be balanced and closed. Never nest fences.
- Code must be genuinely correct and runnable or genuinely representative of real output:
  - HTML must be well-formed and semantically valid.
  - Shell/CLI sessions must be plausible (`dig`, `curl -I`, `nslookup`, `telnet`, `ftp`, `tracert`).
  - JSON must parse. CSS must be valid.
- Prefer several short, focused blocks over one enormous block.

## 4. Mathematics is FORBIDDEN in this course

The validator rejects the note outright if it finds math notation outside code. Therefore:

- **Never** use `$...$`, `$$...$$`, `\(`, `\)`, `\[`, `\]`, or LaTeX commands such as `\frac`, `\sum`,
  `\begin{...}`.
- Express quantities in plain words or code: write "a 200 ms round trip", "1 Gbps", "the ratio of header
  bytes to payload bytes", not a formula.
- A literal dollar sign in prose is fine where the source has one, but do not build maths with it.

## 5. Forbidden content

- No HTML `<img>`, no `[[VISUAL:...]]`, no mermaid, no tikz.
- No figure callouts: never "see the diagram below", "the figure above shows". Explain in prose.
- No source meta-language: never "according to the notes", "the module states". Teach directly.
- Do not copy sentences from the course PDFs. Write original explanation.

## 6. Markdown tables

Header row, separator row of `---` cells with the **same** column count, then rows with that same count.
No dangling `|`, no incomplete final row. Tables are the right way to present protocol comparisons,
status-code classes, DNS record types, hosting models, backup schedules.

## 7. Worked implementation

Section 4 must contain **worked, concrete implementations or sessions**, not prose. For each one use:

```
### 4.1 Task: <what is being set up or demonstrated>

### 4.2 Implementation: <approach>

Step 1. <what is done and why>

```html
<!-- concrete, valid markup -->
```

Step 2. ...
```

Every step must show the actual code, command, or observed output, then say what it demonstrates and why
the result is correct.

## 8. Level differentiation

- **level_1 — Core Concepts (gentle).** Open Section 1 with an everyday analogy *before* any technical
  term is dropped: words such as "Imagine", "Think of", or "Picture" must appear in the first paragraph.
  Small examples, plain language, every acronym expanded on first use, and a beginner-misconceptions list
  in Section 5.
- **level_2 — In-Depth (rigorous).** Precise definitions, protocol mechanics step by step, byte-level or
  header-level detail where the course gives it, and complete worked implementations.
- **level_3 — Exam Focus.** Same five sections, aimed at examination performance: high-yield facts with
  typical mark values, the shapes of questions asked, an explicit trap table, at least three complete
  worked answers with per-step marking points, and a revision checklist plus time strategy in Section 5.

## 9. Correctness — non-negotiable

- Protocol facts must be right: default ports (FTP 20/21, SSH 22, Telnet 23, SMTP 25, DNS 53, HTTP 80,
  POP3 110, IMAP 143, HTTPS 443, IMAPS 993, POP3S 995), status-code meanings, DNS record semantics.
- HTML must be valid for the HTML standard the course targets; do not invent attributes.
- Do not invent commands or flags that do not exist.
- Where the course PDF is OCR-damaged, teach the standard correct behaviour instead of reproducing garble.

## 10. Self-check before finishing

From the repository root run:

```
C:\Users\adm\.vscode\.venv\Scripts\python.exe _scs209\apply.py --topic <topic_pk>
```

It must print `PASS` for all three levels with `words` at least 5200. Fix and re-run until it passes.
Never run `apply.py` without `--check` or `--topic`; publishing is not your job.
