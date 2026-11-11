# Topic PDF Pack Audit — Per Course

**Audit time:** Live update 2026-11-08

## Current pipeline status

- **Current pipeline state:** Continuous official queue processor is running and processing reconciled jobs without catalogue-wide reconciliation scans.
- **Latest progress:** 53 ready, 693 pending, 10 empty, 1 running, 0 failed.
- **Why reconciliation was skipped:** The first full reconciliation exceeded MySQL's idle connection window and lost the database connection.
- **Last worker attempt:** Failed during reconciliation with MySQL error `2013 Lost connection to server during query`.
- **Latest queue-worker error:** Job processing ended with MySQL DNS error `(2005) Unknown server host mysql-38ae4425-electoole-c2b3.i.aivencloud.com`.
- **Chromium:** Verified installed and Playwright launch succeeded with Chrome/Edge support.
- **Playwright package:** Restored at the version declared by the project (`playwright==1.52.0`).
- **Cloudflare R2:** Configured for PDF artifact uploads.
- **Fallback:** ReportLab is available and carries the same branded footer. It is used only if the normal browser pipeline falls back or Chromium cannot render.

## Global totals

| Metric | Value |
|---|---:|
| Active courses in this audit | 26 |
| Active topics | 220 |
| Existing PDF artifact records | 757 |
| Validated source note slots | 391 |
| Question pack slots | 220 |
| Logical source-backed note + question packs | 611 |
| Ready | 53 |
| Empty / no eligible source | 10 |
| Pending | 693 |
| Running | 1 |
| Failed | 0 |

## Artifact status at audit time

| Status | Artifact records |
|---|---:|
| ready | 53 |
| empty | 10 |
| pending | 693 |
| running | 1 |
| failed | 0 |

## How to read this document

- **Validated note slots** counts only notes whose cache payload has the current validation marker and non-empty content.
- **Question slots** is one question pack per active topic.
- **Logical packs** is the source-backed number of note packs plus the one question pack per topic.
- **Missing** counts artifact records which should exist but do not yet exist.
- `empty` means the pipeline found no eligible source content; it is not a PDF-generation failure.
- `pending` means work is queued or waiting for processing.
- `running` means a worker claimed it and no completion state was recorded.
- `failed` means processing exhausted its retry attempts.
- Per-course rows are sorted by course code.

## Course-by-course status

| Course | Topics | Validated note slots | Question slots | Logical packs | Ready | Empty | Pending | Running | Failed | Missing records | Visible past questions |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ASC 100 - INTRODUCTION TO SOCIOLOGY | 6 | 15 | 6 | 21 | 0 | 0 | 24 | 0 | 0 | 0 | 27 |
| EET 100 - Microeconomic Theory I | 5 | 15 | 5 | 20 | 0 | 0 | 20 | 0 | 0 | 0 | 35 |
| SCS 209 - INTERNET TECHNOLOGY | 8 | 24 | 8 | 32 | 0 | 0 | 22 | 0 | 0 | 10 | 0 |
| SMA 102 - BASIC MATHEMATICS | 8 | 24 | 8 | 32 | 0 | 0 | 32 | 0 | 0 | 0 | 81 |
| SMA 103 - ANALYTICAL GEOMETRY | 7 | 21 | 7 | 28 | 0 | 0 | 28 | 0 | 0 | 0 | 52 |
| SMA 190 - INTRODUCTION TO COMPUTERS | 8 | 21 | 8 | 29 | 7 | 8 | 17 | 0 | 0 | 0 | 0 |
| SMA 200 - CALCULUS 2 | 12 | 6 | 12 | 18 | 0 | 0 | 48 | 0 | 0 | 0 | 179 |
| SMA 230 - VECTOR ANALYSIS | 6 | 0 | 6 | 6 | 0 | 0 | 22 | 0 | 0 | 0 | 100 |
| SMA 300 - Real Analysis I | 6 | 18 | 6 | 24 | 0 | 0 | 24 | 0 | 0 | 0 | 115 |
| SMA 330 - NUMERICAL ANALYSIS 1 | 10 | 30 | 10 | 40 | 0 | 0 | 40 | 0 | 0 | 0 | 132 |
| SMA 335 - ORDINARY DIFFERENTIAL EQUATIONS 1 | 13 | 39 | 13 | 52 | 0 | 0 | 8 | 0 | 0 | 44 | 583 |
| SST 101 - INTRODUCTION TO PROBABILITY & STATISTICS | 15 | 45 | 15 | 60 | 0 | 0 | 60 | 0 | 0 | 0 | 196 |
| SST 200 - INTRODUCTION TO COMPUTER INTERACTIVE STATISTICS | 5 | 0 | 5 | 5 | 0 | 0 | 20 | 0 | 0 | 0 | 25 |
| SST 202 - OBJECT ORIENTED PROGRAMMING | 7 | 21 | 7 | 28 | 0 | 0 | 28 | 0 | 0 | 0 | 36 |
| SST 204 - Probability and Statistics 1 | 11 | 32 | 11 | 43 | 0 | 1 | 42 | 0 | 0 | 0 | 1218 |
| SST 301 - Programming Language for Statistics 1 | 9 | 27 | 9 | 36 | 0 | 0 | 36 | 0 | 0 | 0 | 13 |
| SST 304 - MULTIVARIATE STATISTICAL METHODS 1 | 4 | 9 | 4 | 13 | 0 | 0 | 15 | 0 | 0 | 0 | 56 |
| SST 305 - Theory of Estimation | 9 | 27 | 9 | 36 | 0 | 0 | 36 | 0 | 0 | 0 | 293 |
| SST 401 - Decision Theory | 11 | 0 | 11 | 11 | 0 | 0 | 24 | 0 | 0 | 0 | 0 |
| SST 408 - Design and Analysis of Sample Surveys II | 9 | 0 | 9 | 9 | 0 | 0 | 36 | 0 | 0 | 0 | 0 |
| SST 409 - STOCHASTIC PROCESSES | 11 | 0 | 11 | 11 | 0 | 0 | 33 | 0 | 0 | 11 | 0 |
| SST 411 - TIME SERIES ANALYSIS | 9 | 0 | 9 | 9 | 0 | 0 | 27 | 0 | 0 | 9 | 0 |
| SST 412 - Design and Analysis Of Experiments | 7 | 0 | 7 | 7 | 0 | 0 | 28 | 0 | 0 | 0 | 0 |
| SST 413 - Measure and  Probability | 11 | 0 | 11 | 11 | 0 | 0 | 21 | 0 | 0 | 11 | 0 |
| SST404 - ECONOMETRICS 2 | 7 | 0 | 7 | 7 | 0 | 0 | 26 | 0 | 0 | 2 | 0 |
| UCU 110 - COMMUNICATION SKILLS | 6 | 17 | 6 | 23 | 0 | 1 | 22 | 1 | 0 | 0 | 40 |

## Courses with missing artifact records

### SCS 209 - INTERNET TECHNOLOGY
- Topic 173 — Internet Fundamentals, Architecture & Connectivity: level_3:missing
- Topic 174 — Internet Services & Application Layer Protocols: level_3:missing
- Topic 175 — The World Wide Web & Client-Server Architecture: level_3:missing
- Topic 177 — Domain Name System (DNS) & Name Resolution: level_3:missing
- Topic 285 — HTML Layout Containers, Tables & Forms: level_1:missing, level_3:missing, questions:missing
- Topic 286 — Web Hosting, Site Deployment, Security & Disaster Recovery: level_1:missing, level_3:missing, questions:missing

### SMA 335 - ORDINARY DIFFERENTIAL EQUATIONS 1
- Topic 287 — First Order Exact Equations And Integrating Factors: level_1:missing, level_2:missing, level_3:missing, questions:missing
- Topic 288 — First Order Linear Equations And Equations Reducible To This Form (Bernoulis Equations): level_1:missing, level_2:missing, level_3:missing, questions:missing
- Topic 289 — Second Order Homogeneous Linear Equations With Constant Coefficients: level_1:missing, level_2:missing, level_3:missing, questions:missing
- Topic 290 — Second Order Nonhomogeneous Linear Equations With Constant Coefficients: level_1:missing, level_2:missing, level_3:missing, questions:missing
- Topic 291 — Determination Of Particular Integrals Using Short Methods: level_1:missing, level_2:missing, level_3:missing, questions:missing
- Topic 292 — Second Order Equations With Variable Coefficients: level_1:missing, level_2:missing, level_3:missing, questions:missing
- Topic 293 — Linear Equations Of Order N: level_1:missing, level_2:missing, level_3:missing, questions:missing
- Topic 294 — Reduction Of Nth Order Equations To A First Order System Of N Equations: level_1:missing, level_2:missing, level_3:missing, questions:missing
- Topic 295 — Singular Points Of Differential Equations And Power Series Solutions Near Singular Points: level_1:missing, level_2:missing, level_3:missing, questions:missing
- Topic 296 — Power Series Solutions Of First And Second Order Equations: level_1:missing, level_2:missing, level_3:missing, questions:missing
- Topic 297 — Application Of Differential Equations: level_1:missing, level_2:missing, level_3:missing, questions:missing

### SST 409 - STOCHASTIC PROCESSES
- Topic 247 — Poisson Process: questions:missing
- Topic 248 — Introduction to Stochastic Processes: questions:missing
- Topic 249 — Generating Functions: questions:missing
- Topic 250 — Branching Processes and Offspring Distributions: questions:missing
- Topic 251 — Markov Chains: questions:missing
- Topic 252 — Classification of States in Markov Chains: questions:missing
- Topic 253 — Stationary Distributions and Long-Run Behavior: questions:missing
- Topic 254 — Continuous-Time Markov Chains (CTMC): questions:missing
- Topic 255 — Birth and Death Processes: questions:missing
- Topic 256 — Brownian Motion and Diffusion Processes: questions:missing
- Topic 257 — Renewal Theory and Applications: questions:missing

### SST 411 - TIME SERIES ANALYSIS
- Topic 258 — Introduction to Time Series Analysis: questions:missing
- Topic 259 — Trend Estimation and Smoothing Methods: questions:missing
- Topic 260 — Autoregressive (AR) Models: questions:missing
- Topic 261 — Moving Average (MA) Models: questions:missing
- Topic 262 — Autoregressive Moving Average (ARMA) Models: questions:missing
- Topic 263 — Non-Stationary Series and ARIMA Models: questions:missing
- Topic 264 — Seasonal ARIMA (SARIMA) Models: questions:missing
- Topic 265 — Model Estimation and Diagnostic Checking: questions:missing
- Topic 266 — Forecasting and Volatility Modeling (ARCH/GARCH): questions:missing

### SST 413 - Measure and  Probability
- Topic 267 — Sets, Fields, and Sigma-Fields: questions:missing
- Topic 268 — Measures and Probability Measures: questions:missing
- Topic 269 — Outer Measure and Extension of Measures: questions:missing
- Topic 270 — Measurable Functions and Random Variables: questions:missing
- Topic 271 — Lebesgue Integration and Mathematical Expectation: questions:missing
- Topic 272 — Convergence Theorems in Integration: questions:missing
- Topic 273 — Modes of Convergence for Random Variables: questions:missing
- Topic 274 — Product Measures and Fubini's Theorem: questions:missing
- Topic 275 — Absolute Continuity and Radon-Nikodym Theorem: questions:missing
- Topic 276 — Conditional Expectation Given a Sigma-Field: questions:missing
- Topic 277 — Laws of Large Numbers and Central Limit Theorems: questions:missing

### SST404 - ECONOMETRICS 2
- Topic 283 — The Two-Stage Least Squares Estimation Method (2SLS): questions:missing
- Topic 284 — The Instrumental Variables (IV) Method: questions:missing

## Recommended processing order

1. Restart the PDF worker only after MySQL is stable.
2. Prefer the worker with initial reconciliation skipped once the source-backed queue has already been reconciled.
3. Process `failed` and stale `running` jobs first, then `pending` jobs.
4. Regenerate only source-backed validated note levels and each topic's questions pack.
5. Verify Cloudflare R2 keys and downloadability after processing.
6. Regenerate this audit document after each batch.
