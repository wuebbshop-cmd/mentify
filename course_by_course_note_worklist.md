# Course-by-Course Preparation Worklist

The inventories below are a historical snapshot from 2026-11-02; they are not a current audit of learner-visible notes. In particular, cached text and completed generation jobs do not prove that a note is currently publishable.

## Note publication status

The app's note status is determined by `get_published_topic_note_levels` in `services/prep_ai_router.py`: a note is available only when its content passes current validation. A signature mismatch alone is not a permanent rejection; the app now revalidates the note against the current topic and refreshes its signature and validation metadata when it passes. Notes that fail validation remain unavailable.

Catalog-wide revalidation completed against the local development database on 2026-11-04. It checked 771 note-cache entries across 205 active topics: 18 entries had their validation metadata/signature refreshed, 256 entries passed current validation, and 515 entries failed current validation and remain unpublished. The command ensured 405 current-signature jobs for rejected levels are pending; this count includes jobs that were already pending, so it is not a count of newly created jobs. Failed notes remain hidden until replacement content passes validation.

A targeted post-run publication check for SMA 190 found all three note levels published for six topics. Database Management Systems had only level 2 published, and Computers And Communications had levels 2 and 3 published; current-signature jobs for the absent levels are pending.

To recheck or backfill cached notes in future, run `python manage.py revalidate_topic_note_cache --dry-run` first, then `python manage.py revalidate_topic_note_cache` to apply passing refreshes and ensure current-signature replacement jobs are pending for failed cached levels. Use `--course <code-or-id>` to scope the run.

The past-paper sections below use the app's learner-visible rendering and deduplication filter; PDF gaps use the app's download gate. The original snapshot checked 207 active topics.

Detailed source PDF records and paper question status/topic coverage: [full inventory](course_notes_pdf_past_paper_inventory.md).

## ASC 100 — INTRODUCTION TO SOCIOLOGY


### Generated PDFs not downloadable
- Introduction to Sociology: notes level_1, notes level_3.
- Social Structure: notes level_1, notes level_2, notes level_3.

## EET 100 — Microeconomic Theory I


## SCS 209 — INTERNET TECHNOLOGY

### No learner-visible past-paper questions
- Html Fundamentals And Document Structure.
- Essential Html Tags.
- Block-Level And Inline Containers.
- Links And Images.
- Containers And Element Types.
- Combining Essential Html Tags.

### Generated PDFs not downloadable
- Html Fundamentals And Document Structure: notes level_1, notes level_2, notes level_3, questions.
- Essential Html Tags: notes level_1, notes level_2, notes level_3, questions.
- Block-Level And Inline Containers: notes level_1, notes level_2, notes level_3, questions.
- Links And Images: notes level_1, notes level_2, notes level_3, questions.
- Containers And Element Types: notes level_1, notes level_2, notes level_3, questions.
- Combining Essential Html Tags: notes level_1, notes level_2, notes level_3, questions.

## SMA 102 — BASIC MATHEMATICS


## SMA 103 — ANALYTICAL GEOMETRY

### Generated PDFs not downloadable
- The Straight Line: notes level_1, notes level_2, notes level_3, questions.
- The Circle: notes level_1, notes level_2, notes level_3, questions.
- Polar Coordinates: notes level_1, notes level_2, notes level_3, questions.
- The Parabola: notes level_1, notes level_2, notes level_3, questions.
- The Ellipse: notes level_1, notes level_2, notes level_3, questions.
- The Hyperbola: notes level_1, notes level_2, notes level_3, questions.
- Trigonometric Identities & Equations: notes level_1, notes level_2, notes level_3, questions.

## SMA 190 — INTRODUCTION TO COMPUTERS


### No learner-visible past-paper questions
- Basic Hardware Units Of A Computer.
- Computer Software.
- Windows Basics.
- Word Processing.
- Spreadsheets.
- Database Management Systems.
- Presentation Graphics.
- Computers And Communications.

### Generated PDFs not downloadable
- Basic Hardware Units Of A Computer: notes level_1, notes level_2, notes level_3, questions.
- Computer Software: notes level_1, notes level_2, notes level_3, questions.
- Windows Basics: notes level_1, notes level_2, notes level_3, questions.
- Word Processing: notes level_1, notes level_2, notes level_3, questions.
- Spreadsheets: notes level_1, notes level_2, notes level_3, questions.
- Database Management Systems: notes level_1, notes level_2, notes level_3, questions.
- Presentation Graphics: notes level_1, notes level_2, notes level_3, questions.
- Computers And Communications: notes level_1, notes level_2, notes level_3, questions.

## SMA 200 — CALCULUS 2


### No learner-visible past-paper questions
- Integration Of Functions Using Basic Formulae 1.
- Integration Of Functions Using The Extension Of The Basic.
- Integration Using Substitutions 16.
- Integration By Parts 26.
- Integration Using Trigonometric Identities 34.
- Integration Using Partial Fractions 47.
- Definite Integrals And The Fundamental Theorem Of The.
- Area Under A Curve 61.
- Improper Integrals 71.
- Length Of Arc Of A Curve 83.
- Volume And Surface Area Of Solids Of Revolution 93.
- Numerical Integration (Trapezoidal And Simpsons Rules).

### Generated PDFs not downloadable
- Integration Of Functions Using Basic Formulae 1: notes level_1, notes level_2, notes level_3, questions.
- Integration Of Functions Using The Extension Of The Basic: notes level_1, notes level_2, notes level_3, questions.
- Integration Using Substitutions 16: notes level_1, notes level_2, notes level_3, questions.
- Integration By Parts 26: notes level_1, notes level_2, notes level_3, questions.
- Integration Using Trigonometric Identities 34: notes level_1, notes level_2, notes level_3, questions.
- Integration Using Partial Fractions 47: notes level_1, notes level_2, notes level_3, questions.
- Definite Integrals And The Fundamental Theorem Of The: notes level_1, notes level_2, notes level_3, questions.
- Area Under A Curve 61: notes level_1, notes level_2, notes level_3, questions.
- Improper Integrals 71: notes level_1, notes level_2, notes level_3, questions.
- Length Of Arc Of A Curve 83: notes level_1, notes level_2, notes level_3, questions.
- Volume And Surface Area Of Solids Of Revolution 93: notes level_1, notes level_2, notes level_3, questions.
- Numerical Integration (Trapezoidal And Simpsons Rules): notes level_1, notes level_2, notes level_3, questions.

## SMA 230 — VECTOR ANALYSIS


### No learner-visible past-paper questions
- Dot And Cross Product.
- Ordinary Differentiation Of Vectors.
- Vector Integration And Integral Theorems.
- Curvilinear Coordinates.

### Generated PDFs not downloadable
- Vector Algebra: notes level_1, notes level_2, notes level_3, questions.
- Dot And Cross Product: notes level_1, notes level_2, notes level_3, questions.
- Reciprocal Set Of Vectors: notes level_1, notes level_2, notes level_3, questions.
- Ordinary Differentiation Of Vectors: notes level_1, notes level_2, notes level_3, questions.
- Vector Integration And Integral Theorems: notes level_1, notes level_2, notes level_3, questions.
- Curvilinear Coordinates: notes level_1, notes level_2, notes level_3, questions.

## SMA 300 — Real Analysis I

### No learner-visible past-paper questions
- Countable and Uncountable Sets.

### Generated PDFs not downloadable
- Sequences: notes level_2, notes level_3.
- Countable and Uncountable Sets: questions.

## SMA 330 — NUMERICAL ANALYSIS 1

### No learner-visible past-paper questions
- Errors And Approximations In Numerical Computations.
- Interpolation And Ploynomial Approximation.
- Numerical Differentiation.
- Quadrature Methods.

### Generated PDFs not downloadable
- Errors And Approximations In Numerical Computations: notes level_1, notes level_2, notes level_3, questions.
- Polynomials And Interpolation: notes level_1, notes level_2, notes level_3, questions.
- Polynomials And Synthetic Division: notes level_1, notes level_2, notes level_3, questions.
- Interpolation And Ploynomial Approximation: notes level_1, notes level_2, notes level_3, questions.
- Numerical Integration: notes level_1, notes level_2, notes level_3, questions.
- Numerical Differentiation: notes level_1, notes level_2, notes level_3, questions.
- Composite Formulae And Romberg Integration: notes level_1, notes level_2, notes level_3, questions.
- Quadrature Methods: notes level_1, notes level_2, notes level_3, questions.
- Iteration Techniques For Non Linear Equations: notes level_1, notes level_2, notes level_3, questions.
- Newton Raphson And Secant Method: notes level_1, notes level_2, notes level_3, questions.

## SMA 335 — ORDINARY DIFFERENTIAL EQUATIONS 1


### Generated PDFs not downloadable
- Differential Equations: Definitions, Classification, And Solutions: notes level_1, notes level_2, notes level_3, questions.
- First-Order Differential Equations: Separation Of Variables And Homogeneous Equations: notes level_1, notes level_2, notes level_3, questions.

## SST 101 — INTRODUCTION TO PROBABILITY & STATISTICS


### No learner-visible past-paper questions
- Introduction To Statistics And Probability.
- Types Of Data.
- Data Collection Methods.
- Data Representation.
- Measures Of Central Tendency.
- Measures Of Dispersion.
- Probability Concepts.
- Probability Distributions.
- Sampling Techniques.
- Estimation And Confidence Intervals.
- Hypothesis Testing.
- Correlation And Regression.
- Skewness And Kurtosis.
- Moments.
- Uses Of Statistics In Real Life.

### Generated PDFs not downloadable
- Introduction To Statistics And Probability: notes level_1, notes level_2, notes level_3, questions.
- Types Of Data: notes level_1, notes level_2, notes level_3, questions.
- Data Collection Methods: notes level_1, notes level_2, notes level_3, questions.
- Data Representation: notes level_1, notes level_2, notes level_3, questions.
- Measures Of Central Tendency: notes level_1, notes level_2, notes level_3, questions.
- Measures Of Dispersion: notes level_1, notes level_2, notes level_3, questions.
- Probability Concepts: notes level_1, notes level_2, notes level_3, questions.
- Probability Distributions: notes level_1, notes level_2, notes level_3, questions.
- Sampling Techniques: notes level_1, notes level_2, notes level_3, questions.
- Estimation And Confidence Intervals: notes level_1, notes level_2, notes level_3, questions.
- Hypothesis Testing: notes level_1, notes level_2, notes level_3, questions.
- Correlation And Regression: notes level_1, notes level_2, notes level_3, questions.
- Skewness And Kurtosis: notes level_1, notes level_2, notes level_3, questions.
- Moments: notes level_1, notes level_2, notes level_3, questions.
- Uses Of Statistics In Real Life: notes level_1, notes level_2, notes level_3, questions.

## SST 200 — INTRODUCTION TO COMPUTER INTERACTIVE STATISTICS


### No learner-visible past-paper questions
- 7 Flow Control.
- 9 Probability Distributions.
- 12 Statistical Graphics.

### Generated PDFs not downloadable
- 5 Language Essentials: notes level_1, notes level_2, notes level_3, questions.
- 7 Flow Control: notes level_1, notes level_2, notes level_3, questions.
- 9 Probability Distributions: notes level_1, notes level_2, notes level_3, questions.
- 12 Statistical Graphics: notes level_1, notes level_2, notes level_3, questions.
- 14 Statistical Functions: notes level_1, notes level_2, notes level_3, questions.

## SST 202 — OBJECT ORIENTED PROGRAMMING


### No learner-visible past-paper questions
- Methods.
- Operators.
- Control Statements.
- Strings.

### Generated PDFs not downloadable
- Classes And Objects: notes level_1, notes level_2, notes level_3, questions.
- Methods: notes level_1, notes level_2, notes level_3, questions.
- Data Types: notes level_1, notes level_2, notes level_3, questions.
- Operators: notes level_1, notes level_2, notes level_3, questions.
- Control Statements: notes level_1, notes level_2, notes level_3, questions.
- Arrays: notes level_1, notes level_2, notes level_3, questions.
- Strings: notes level_1, notes level_2, notes level_3, questions.

## SST 204 — Probability and Statistics 1


### No learner-visible past-paper questions
- Expectation.
- Gamma, Exponential And Beta Distributions.

### Generated PDFs not downloadable
- Random Variables: notes level_1, notes level_2, notes level_3, questions.
- Distribution Functions: notes level_1, notes level_2, notes level_3, questions.
- Mode And Median: notes level_1, notes level_2, notes level_3, questions.
- Expectation: notes level_1, notes level_2, notes level_3, questions.
- Moments And Variance Properties: notes level_1, notes level_2, notes level_3, questions.
- Moment Generating Function And Probability Generating Function: notes level_1, notes level_2, notes level_3, questions.
- Special Discrete Probability Distributions: notes level_1, notes level_2, notes level_3, questions.
- Poisson Distribution And Binomial Approximation: notes level_1, notes level_2, notes level_3, questions.
- Normal Distribution And Probability Computation: notes level_1, notes level_2, notes level_3, questions.
- Gamma, Exponential And Beta Distributions: notes level_1, notes level_2, notes level_3, questions.
- Change Of Variable: notes level_1, notes level_2, notes level_3, questions.

## SST 301 — Programming Language for Statistics 1


### No learner-visible past-paper questions
- Course Overview & Introduction.
- Solutions of Systems of Linear Equations.
- Differentiation & Integration of Univariate Functions.
- Determining Roots of Equations & Optimization.
- Pseudo-Random Number Generators & Simulation.

### Generated PDFs not downloadable
- Course Overview & Introduction: questions.
- Solutions of Systems of Linear Equations: questions.
- Differentiation & Integration of Univariate Functions: questions.
- Determining Roots of Equations & Optimization: questions.
- Pseudo-Random Number Generators & Simulation: questions.

## SST 304 — MULTIVARIATE STATISTICAL METHODS 1


### Generated PDFs not downloadable
- Random And Mean Vectors: notes level_1, notes level_2, notes level_3, questions.
- Determination Of Parameters Of Mvn Distribution: notes level_1, notes level_2, notes level_3, questions.
- Multinomial Distribution: notes level_1, notes level_2, notes level_3, questions.
- The Weak Law Of Large Numbers: notes level_1, notes level_2, notes level_3, questions.

## SST 305 — Theory of Estimation

### No learner-visible past-paper questions
- Sufficient Statistics.
- Moment Estimation.
- Maximum Likelihood Estimation.

### Generated PDFs not downloadable
- Sufficient Statistics: questions.
- Maximum Likelihood Estimation: questions.

## SST 401 — Decision Theory


### No learner-visible past-paper questions
- Overview And Lesson Plans (Lessons 1–11).
- Decision Making Under Uncertainty 6.
- Decision Making Under Regret 9.
- Decision Making Under Risk 11.
- Opportunity Loss 14.
- Expected Value Under Perfect Information 17.
- Relationship Between Eol, Emv And Evpi 20.
- Return To Risk Ratio 22.
- Bayes’ Decision Analysis 25.
- Expected Utility Criterion 29.
- Decision Trees 31.

### Generated PDFs not downloadable
- Overview And Lesson Plans (Lessons 1–11): notes level_1, notes level_2, notes level_3, questions.
- Decision Making Under Uncertainty 6: notes level_1, notes level_2, notes level_3, questions.
- Decision Making Under Regret 9: notes level_1, notes level_2, notes level_3, questions.
- Decision Making Under Risk 11: notes level_1, notes level_2, notes level_3, questions.
- Opportunity Loss 14: notes level_1, notes level_2, notes level_3, questions.
- Expected Value Under Perfect Information 17: notes level_1, notes level_2, notes level_3, questions.
- Relationship Between Eol, Emv And Evpi 20: notes level_1, notes level_2, notes level_3, questions.
- Return To Risk Ratio 22: notes level_1, notes level_2, notes level_3, questions.
- Bayes’ Decision Analysis 25: notes level_1, notes level_2, notes level_3, questions.
- Expected Utility Criterion 29: notes level_1, notes level_2, notes level_3, questions.
- Decision Trees 31: notes level_1, notes level_2, notes level_3, questions.

## SST 408 — Design and Analysis of Sample Surveys II


### No learner-visible past-paper questions
- Cluster Sampling Designs 6.
- Multistage Cluster Sampling 13.
- Multiphase Sampling Designs With Regression And Ratio Estimators 18.
- Repeated Sampling Designs 24.
- Non-Sampling Errors 30.
- Regression Estimation Using Multiphase Sampling Designs. In This Lesson We Assume That The Relationship Between The.
- Ratio Estimation Using Multiphase Sampling Designs. In This Lesson We Assume That The Relationship Between The Survey.
- Repeated Sampling Designs. In This Lesson We Introduce A New Type Of Sampling Design Called A Repeated Sampling Design.
- Non-Sampling Errors In Survey Sampling. In All The Previous Lessons We Considered That The Observation On The 𝑖th Unit.

### Generated PDFs not downloadable
- Cluster Sampling Designs 6: notes level_1, notes level_2, notes level_3, questions.
- Multistage Cluster Sampling 13: notes level_1, notes level_2, notes level_3, questions.
- Multiphase Sampling Designs With Regression And Ratio Estimators 18: notes level_1, notes level_2, notes level_3, questions.
- Repeated Sampling Designs 24: notes level_1, notes level_2, notes level_3, questions.
- Non-Sampling Errors 30: notes level_1, notes level_2, notes level_3, questions.
- Regression Estimation Using Multiphase Sampling Designs. In This Lesson We Assume That The Relationship Between The: notes level_1, notes level_2, notes level_3, questions.
- Ratio Estimation Using Multiphase Sampling Designs. In This Lesson We Assume That The Relationship Between The Survey: notes level_1, notes level_2, notes level_3, questions.
- Repeated Sampling Designs. In This Lesson We Introduce A New Type Of Sampling Design Called A Repeated Sampling Design: notes level_1, notes level_2, notes level_3, questions.
- Non-Sampling Errors In Survey Sampling. In All The Previous Lessons We Considered That The Observation On The 𝑖th Unit: notes level_1, notes level_2, notes level_3, questions.

## SST 409 — STOCHASTIC PROCESSES

### No learner-visible past-paper questions
- Poisson Process.
- Introduction: Random Phenomena And Stochastic Processes.
- Generating Functions.
- Probability Generating Function (Pgf).
- The Pgf And Moments Of Standard Distributions.
- Tail Or Cumulative Probabilities.
- Probability Generating Function Of The Sum Of Independent Random Variables.
- Stochastic Processes With Discrete States In Continuous Time.
- Birthdeath Processes.
- Queuing Models.
- Stochastic Processes With Discrete States In Discrete Time.

### Generated PDFs not downloadable
- Poisson Process: notes level_1, notes level_2, notes level_3, questions.
- Introduction: Random Phenomena And Stochastic Processes: notes level_1, notes level_2, notes level_3, questions.
- Generating Functions: notes level_1, notes level_2, notes level_3, questions.
- Probability Generating Function (Pgf): notes level_1, notes level_2, notes level_3, questions.
- The Pgf And Moments Of Standard Distributions: notes level_1, notes level_2, notes level_3, questions.
- Tail Or Cumulative Probabilities: notes level_1, notes level_2, notes level_3, questions.
- Probability Generating Function Of The Sum Of Independent Random Variables: notes level_1, notes level_2, notes level_3, questions.
- Stochastic Processes With Discrete States In Continuous Time: notes level_1, notes level_2, notes level_3, questions.
- Birthdeath Processes: notes level_1, notes level_2, notes level_3, questions.
- Queuing Models: notes level_1, notes level_2, notes level_3, questions.
- Stochastic Processes With Discrete States In Discrete Time: notes level_1, notes level_2, notes level_3, questions.

## SST 411 — TIME SERIES ANALYSIS

### Notes with no usable cache recorded
- Definition Of A Time Series (L3).
- The Four Components Of Time Series (L3).
- Graphic Method (L3).
- Stationary Time Series (L3).
- Determination Of Trend By Weighted Moving Average Process (L3).
- Method Of Simple Averages (L3).
- Measurement Of Cyclic Variations (L3).
- Purely Random Process (L3).
- The Ar(1) Process (L1, L3).


### No learner-visible past-paper questions
- Definition Of A Time Series.
- The Four Components Of Time Series.
- Graphic Method.
- Stationary Time Series.
- Determination Of Trend By Weighted Moving Average Process.
- Method Of Simple Averages.
- Measurement Of Cyclic Variations.
- Purely Random Process.
- The Ar(1) Process.

### Generated PDFs not downloadable
- Definition Of A Time Series: notes level_1, notes level_2, notes level_3, questions.
- The Four Components Of Time Series: notes level_1, notes level_2, notes level_3, questions.
- Graphic Method: notes level_1, notes level_2, notes level_3, questions.
- Stationary Time Series: notes level_1, notes level_2, notes level_3, questions.
- Determination Of Trend By Weighted Moving Average Process: notes level_1, notes level_2, notes level_3, questions.
- Method Of Simple Averages: notes level_1, notes level_2, notes level_3, questions.
- Measurement Of Cyclic Variations: notes level_1, notes level_2, notes level_3, questions.
- Purely Random Process: notes level_1, notes level_2, notes level_3, questions.
- The Ar(1) Process: notes level_1, notes level_2, notes level_3, questions.

## SST 412 — Design and Analysis Of Experiments


### No learner-visible past-paper questions
- Completely Randomized Design 3.
- Randomized Block Design 9.
- Estimation Of A Missing Observation In A Rbd 14.
- Latin Square Design 16.
- Analysis Of Graeco–Latin Squares 22.
- Balanced Incomplete Block Design (Bibd) 23.
- Comparison Of Designs 28.

### Generated PDFs not downloadable
- Completely Randomized Design 3: notes level_1, notes level_2, notes level_3, questions.
- Randomized Block Design 9: notes level_1, notes level_2, notes level_3, questions.
- Estimation Of A Missing Observation In A Rbd 14: notes level_1, notes level_2, notes level_3, questions.
- Latin Square Design 16: notes level_1, notes level_2, notes level_3, questions.
- Analysis Of Graeco–Latin Squares 22: notes level_1, notes level_2, notes level_3, questions.
- Balanced Incomplete Block Design (Bibd) 23: notes level_1, notes level_2, notes level_3, questions.
- Comparison Of Designs 28: notes level_1, notes level_2, notes level_3, questions.

## SST 413 — Measure and  Probability

### Notes with no usable cache recorded
- Definitions (L3).
- Sequences And Limits (L3).
- Fields (L3).
- Approaches To Probability (L3).
- Moments (L3).
- Fatou’S Theorem (L3).
- Dominated Convergence Theorem (Lebesgue) (L3).
- Fubini’S Theorem (L3).
- Characteristic Functions (L3).
- Kolmogorov’S 01 Law (L3).
- Bernoulli’S Weak Law Of Large Numbers (L3).


### No learner-visible past-paper questions
- Definitions.
- Sequences And Limits.
- Fields.
- Approaches To Probability.
- Moments.
- Fatou’S Theorem.
- Dominated Convergence Theorem (Lebesgue).
- Fubini’S Theorem.
- Characteristic Functions.
- Kolmogorov’S 01 Law.
- Bernoulli’S Weak Law Of Large Numbers.

### Generated PDFs not downloadable
- Definitions: notes level_1, notes level_2, notes level_3, questions.
- Sequences And Limits: notes level_1, notes level_2, notes level_3, questions.
- Fields: notes level_1, notes level_2, notes level_3, questions.
- Approaches To Probability: notes level_1, notes level_2, notes level_3, questions.
- Moments: notes level_1, notes level_2, notes level_3, questions.
- Fatou’S Theorem: notes level_1, notes level_2, notes level_3, questions.
- Dominated Convergence Theorem (Lebesgue): notes level_1, notes level_2, notes level_3, questions.
- Fubini’S Theorem: notes level_1, notes level_2, notes level_3, questions.
- Characteristic Functions: notes level_1, notes level_2, notes level_3, questions.
- Kolmogorov’S 01 Law: notes level_1, notes level_2, notes level_3, questions.
- Bernoulli’S Weak Law Of Large Numbers: notes level_1, notes level_2, notes level_3, questions.

## SST404 — ECONOMETRICS 2


### No learner-visible past-paper questions
- Simultaneous Equation Relationships.
- Equation Bias.
- Structural Equations Form.
- Definition Of The Problem Of Identification.
- The Indirect Least Squares Method (Ils).
- E-Tivity 6 — The Two-Stage Least Squares Estimation Method (2Sls).
- The Iv Method.

### Generated PDFs not downloadable
- Simultaneous Equation Relationships: notes level_1, notes level_2, notes level_3, questions.
- Equation Bias: notes level_1, notes level_2, notes level_3, questions.
- Structural Equations Form: notes level_1, notes level_2, notes level_3, questions.
- Definition Of The Problem Of Identification: notes level_1, notes level_2, notes level_3, questions.
- The Indirect Least Squares Method (Ils): notes level_1, notes level_2, notes level_3, questions.
- E-Tivity 6 — The Two-Stage Least Squares Estimation Method (2Sls): notes level_1, notes level_2, notes level_3, questions.
- The Iv Method: notes level_1, notes level_2, notes level_3, questions.

## UCU 110 — COMMUNICATION SKILLS

### Notes with no usable cache recorded
- Reading Skills and Information Literacy (L3).


### No learner-visible past-paper questions
- Listening and Note-Taking.

### Generated PDFs not downloadable
- Fundamentals of Communication and Collaboration: notes level_1, notes level_2, notes level_3, questions.
- Listening and Note-Taking: notes level_1, notes level_2, notes level_3, questions.
- Study Skills and Time Management: notes level_1, notes level_2, notes level_3, questions.
- Collaboration and Interpersonal Skills: notes level_1, notes level_2, notes level_3, questions.
- Reading Skills and Information Literacy: notes level_1, notes level_2, notes level_3, questions.
- Academic and Professional Writing: notes level_1, notes level_2, notes level_3, questions.


# ----------

---

### 1. Root Cause Analysis: How the Mistake Occurred

Your assessment was completely accurate:

1. **AI Agent Intervention & Bypassed Structure**:
   An AI agent previously created scripts (`repair_all_failed_valid_notes.py`, `repair_failed_topic_notes_bulk.py`, `tmp_sst409_manual_notes.py`, etc.) to clear failed note jobs. For `SST 305` (Level 2), condensed outline notes were injected directly into the cache. 
   - These entries lack worked exemplar problems (`## 4. Worked Exemplar Problem with Step-by-Step Solution`), definitions, and high-yield pitfalls.
   - They contain broken KaTeX math delimiters lacking backslashes (e.g. `$prod_i f_theta(x_i)$`, `$phat=n/sum_i x_i=1/Xbar$`, `$thetahat$`).
   - They are ~3,000 characters long (28 to 30 lines), whereas genuine generated notes in the catalog are **15,000 to 35,000+ characters** (150 to 500+ lines).

2. **Validation Gap in the API Router**:
   In [`services/prep_ai_router.py`](file:///C:/Users/adm/.vscode/Products/EduAI/services/prep_ai_router.py#L2206-L2217):
   - `_required_note_sections()` only verified regex numbers (`## 1.`, `## 2.`, `## 3.`, `## 4.`, `## 5.`). It **never checked the actual section headings** or enforced the required course study profile structure.
   - The length check only verified `len(final_body) < 120` on section 5. There was no total note length requirement (e.g., minimum 8,000 characters), so these 3,000-character notes passed validator checks and were marked `validated-v11-numbered-figure-context`.

---

### 2. Benchmark Comparison

| Attribute | Earlier Catalog Standard (e.g. SST 301, SMA 102, Topic 49 L1/L3) | Malformed Notes (e.g. SST 305 Level 2) |
| :--- | :--- | :--- |
| **Length** | 15,000 – 35,000+ characters (200 – 500+ lines) | ~2,500 – 3,700 characters (28 – 35 lines) |
| **Structure** | 5 standard pedagogical sections matching study profile | Arbitrary 5 headers (e.g., *1. Likelihood*, *2. Geometric model*, *5. Exam method*) |
| **Worked Examples** | Complete worked exam problems with derivations | None or brief high-level remarks |
| **LaTeX / KaTeX** | Proper LaTeX (`\prod_{i=1}^n`, `\hat{\theta}`, `\frac{n}{\sum x_i}`) | Raw ASCII text (`$prod_i f_theta$`, `$phat$`) |

---

### 3. Complete List of All Affected Courses, Topics, and Levels

A total of **30 cached notes** across **7 courses** were identified as having this short, defective structure (< 5,000 chars, 28–49 lines):

#### 1. SST 305 — Theory of Estimation (9 topics affected — all Level 2)
All Level 2 notes across the entire course suffer from this exact issue:
- **Topic 45** [`level_2`]: *Properties of Estimators* — 3,721 chars, 30 lines
- **Topic 46** [`level_2`]: *Confidence Interval Estimation* — 3,514 chars, 28 lines
- **Topic 47** [`level_2`]: *Sufficient Statistics* — 3,291 chars, 28 lines
- **Topic 48** [`level_2`]: *Moment Estimation* — 3,335 chars, 30 lines
- **Topic 49** [`level_2`]: *Maximum Likelihood Estimation* — 3,019 chars, 28 lines *(sample cited)*
- **Topic 50** [`level_2`]: *Least Squares Estimation* — 2,968 chars, 28 lines
- **Topic 51** [`level_2`]: *Method of Minimum Variance* — 3,393 chars, 28 lines
- **Topic 52** [`level_2`]: *Interval Estimation* — 3,134 chars, 28 lines
- **Topic 53** [`level_2`]: *Interval Estimation: Confidence Intervals...* — 3,004 chars, 28 lines

#### 2. SST 401 — Decision Theory (8 topics affected)
- **Topic 218** [`level_2`]: *Overview And Lesson Plans* — 2,798 chars, 49 lines
- **Topic 219** [`level_2`]: *Decision Making Under Uncertainty* — 2,768 chars, 49 lines
- **Topic 220** [`level_2`]: *Decision Making Under Regret* — 2,738 chars, 49 lines
- **Topic 221** [`level_1`]: *Decision Making Under Risk* — 2,732 chars, 49 lines
- **Topic 222** [`level_2`]: *Opportunity Loss* — 2,672 chars, 49 lines
- **Topic 224** [`level_2`]: *Relationship Between Eol, Emv And E* — 2,804 chars, 49 lines
- **Topic 226** [`level_2`]: *Bayes' Decision Analysis* — 2,720 chars, 49 lines
- **Topic 228** [`level_2`]: *Decision Trees* — 2,660 chars, 49 lines

#### 3. SMA 330 — Numerical Analysis 1 (5 topics affected)
- **Topic 197** [`level_1`]: *Errors And Approximations In Numerical Analysis* — 2,867 chars, 28 lines
- **Topic 197** [`level_2`]: *Errors And Approximations In Numerical Analysis* — 3,580 chars, 58 lines
- **Topic 197** [`level_3`]: *Errors And Approximations In Numerical Analysis* — 3,853 chars, 28 lines
- **Topic 202** [`level_3`]: *Numerical Differentiation* — 3,516 chars, 28 lines

#### 4. SST 409 — Stochastic Processes (5 topics affected)
- **Topic 249** [`level_2`]: *Generating Functions* — 2,677 chars, 48 lines
- **Topic 252** [`level_1`]: *Tail Or Cumulative Probabilities* — 2,872 chars, 30 lines
- **Topic 252** [`level_2`]: *Tail Or Cumulative Probabilities* — 2,456 chars, 60 lines
- **Topic 252** [`level_3`]: *Tail Or Cumulative Probabilities* — 2,941 chars, 28 lines

#### 5. SMA 300 — Real Analysis I (1 topic affected)
- **Topic 19** [`level_2`]: *The Real Number System* — 2,441 chars, 36 lines

#### 6. SST 411 — Time Series Analysis (1 topic affected)
- **Topic 266** [`level_2`]: *The Ar(1) Process* — 2,587 chars, 89 lines

#### 7. SST 413 — Measure and Probability (1 topic affected)
- **Topic 276** [`level_1`]: *Kolmogorov's 0-1 Law* — 2,546 chars, 53 lines

---

### 4. Recommended Next Steps

1. **Tighten Router Validation** in [`services/prep_ai_router.py`](file:///C:/Users/adm/.vscode/Products/EduAI/services/prep_ai_router.py):
   - Add a minimum character threshold (e.g., `len(content) >= 7000`) in `_note_completion_issues()`.
   - Reject unescaped math variable tokens like `$prod_i$`, `$theta$`, and `$phat$`.
   - Validate that section headings conform to expected titles or the course study profile.
2. **Purge and Regenerate**:
   - Delete the 30 defective cache entries from `PrepContentCache`.
   - Queue regeneration jobs via `run_prep_note_worker` using DeepSeek (`deepseek-chat`) so they are regenerated to full length with proper formulas and worked exemplars.

-----
-----
SCS 209 — Containers And Element Types: Level 3
SST 409 — Poisson Process: Levels 1 and 3
SST 409 — Generating Functions: Levels 1 and 3

--------
-------

Ran check PrepTopic course related_name
Ran test fast extraction of vs and level · Exited with code 1
Created test_speed.py
Ran run test speed script
Checked task Run test speed script
Created generate_final_report.py
Ran execute generate_final_report.py
Checked task Execute generate_final_report.py
Checked task Execute generate_final_report.py
Checked task Execute generate_final_report.py
Ran read task-42829 log
Analyzed final_missing_notes_report.txt:L1-121
Ran audit SST 305 specifically · Exited with code 1
Created check_sst305.py
Ran run check_sst305.py
Ran check for any other short validated notes · Exited with code 1
Created check_short_notes.py
Ran run check_short_notes.py

Here is the audit of all missing and unvalidated topic notes across all courses in the database.

---

### Audit Summary Across All Courses

| Category | Count | Status Description |
| :--- | :--- | :--- |
| **Total Active Topics** | **207** | Across 26 active courses (621 total level slots across Levels 1, 2, and 3) |
| **Validated & Display Ready** | **579** | Fully cached with `validation_state: "validated-v11-numbered-figure-context"` |
| **Cached but NOT Validated for App** | **20** | Cached entries exist in `PrepContentCache`, but `validation_state` is unvalidated/`None`, blocking display in the app |
| **NOT Cached at All** | **22** | No cache record exists in `PrepContentCache` for that topic and level |
| *Defective Short Stubs (< 5,000 chars)* | *24* | Marked validated by the earlier batch, but are defective stubs (~2,500–3,800 chars) lacking full syllabus content |

---

### 1. Notes NOT Cached at All (22 Slots)

These topics have no cache record in `PrepContentCache` for the specified levels:

#### Course: SST 411 — Time Series Analysis (Course ID: 3637)
- **Topic 258**: *Definition Of A Time Series*
  - `level_3`: Not cached
- **Topic 259**: *The Four Components Of Time Series*
  - `level_3`: Not cached
- **Topic 260**: *Graphic Method*
  - `level_3`: Not cached
- **Topic 261**: *Stationary Time Series*
  - `level_3`: Not cached
- **Topic 262**: *Determination Of Trend By Weighted Moving Average Process*
  - `level_3`: Not cached
- **Topic 263**: *Method Of Simple Averages*
  - `level_3`: Not cached
- **Topic 264**: *Measurement Of Cyclic Variations*
  - `level_3`: Not cached
- **Topic 265**: *Purely Random Process*
  - `level_3`: Not cached
- **Topic 266**: *The AR(1) Process*
  - `level_1`: Not cached
  - `level_3`: Not cached

#### Course: SST 413 — Measure and Probability (Course ID: 3639)
- **Topic 267**: *Definitions*
  - `level_3`: Not cached
- **Topic 268**: *Sequences And Limits*
  - `level_3`: Not cached
- **Topic 269**: *Fields*
  - `level_3`: Not cached
- **Topic 270**: *Approaches To Probability*
  - `level_3`: Not cached
- **Topic 271**: *Moments*
  - `level_3`: Not cached
- **Topic 272**: *Fatou's Theorem*
  - `level_3`: Not cached
- **Topic 273**: *Dominated Convergence Theorem (Lebesgue)*
  - `level_3`: Not cached
- **Topic 274**: *Fubini's Theorem*
  - `level_3`: Not cached
- **Topic 275**: *Characteristic Functions*
  - `level_3`: Not cached
- **Topic 276**: *Kolmogorov's 0-1 Law*
  - `level_3`: Not cached
- **Topic 277**: *Bernoulli's Weak Law Of Large Numbers*
  - `level_3`: Not cached

#### Course: UCU 110 — Communication Skills (Course ID: 39)
- **Topic 137**: *Reading Skills and Information Literacy*
  - `level_3`: Not cached

---

### 2. Notes Cached but NOT Validated for Display in App (20 Slots)

These notes exist in `PrepContentCache` but have `validation_state: None` / unvalidated, so `get_published_topic_note_levels()` rejects them from the app interface:

#### Course: SCS 209 — Internet Technology (Course ID: 47)
- **Topic 173**: *HTML Fundamentals And Document Structure* — `level_3` (Unvalidated)
- **Topic 174**: *Essential HTML Tags* — `level_3` (Unvalidated)
- **Topic 175**: *Block-Level And Inline Containers* — `level_3` (Unvalidated)

#### Course: SMA 230 — Vector Analysis (Course ID: 43)
- **Topic 242**: *Dot And Cross Product* — `level_3` (Unvalidated)

#### Course: SST 204 — Probability and Statistics 1 (Course ID: 46)
- **Topic 185**: *Special Discrete Probability Distributions* — `level_3` (Unvalidated)

#### Course: SST 304 — Multivariate Statistical Methods 1 (Course ID: 3635)
- **Topic 167**: *Random And Mean Vectors* — `level_3` (Unvalidated)

#### Course: SST 401 — Decision Theory (Course ID: 59)
- **Topic 218**: *Overview And Lesson Plans (Lessons 1–11)* — `level_3` (Unvalidated)
- **Topic 219**: *Decision Making Under Uncertainty* — `level_1` (Unvalidated), `level_3` (Unvalidated)
- **Topic 220**: *Decision Making Under Regret* — `level_1` (Unvalidated)
- **Topic 221**: *Decision Making Under Risk* — `level_3` (Unvalidated)
- **Topic 222**: *Opportunity Loss* — `level_3` (Unvalidated)
- **Topic 223**: *Expected Value Under Perfect Information* — `level_1` (Unvalidated), `level_3` (Unvalidated)
- **Topic 225**: *Return To Risk Ratio* — `level_3` (Unvalidated)
- **Topic 226**: *Bayes' Decision Analysis* — `level_1` (Unvalidated), `level_3` (Unvalidated)
- **Topic 227**: *Expected Utility Criterion* — `level_1` (Unvalidated), `level_3` (Unvalidated)
- **Topic 228**: *Decision Trees* — `level_3` (Unvalidated)

---

### 3. Defective Short Stubs (< 5,000 Chars) Marked Validated (24 Slots)

These are notes that passed the validator flag previously, but are short stubs (~2,400–3,800 characters) lacking the full 5-section structure and worked examples:

| Course | Topic ID & Title | Level | Length |
| :--- | :--- | :--- | :--- |
| **SST 305** | Topic 51 (*Method of Minimum Variance*) | `level_2` | 3,393 chars |
| **SST 305** | Topic 52 (*Interval Estimation*) | `level_2` | 3,134 chars |
| **SST 305** | Topic 53 (*Interval Estimation: Two Independent Normal Distributions*) | `level_2` | 3,004 chars |
| **SST 401** | Topic 218 (*Overview And Lesson Plans*) | `level_2` | 2,798 chars |
| **SST 401** | Topic 219 (*Decision Making Under Uncertainty*) | `level_2` | 2,768 chars |
| **SST 401** | Topic 220 (*Decision Making Under Regret*) | `level_2` | 2,738 chars |
| **SST 401** | Topic 221 (*Decision Making Under Risk*) | `level_1` | 2,732 chars |
| **SST 401** | Topic 222 (*Opportunity Loss*) | `level_2` | 2,672 chars |
| **SST 401** | Topic 224 (*Relationship Between EOL, EMV, EVPI*) | `level_2` | 2,804 chars |
| **SST 401** | Topic 226 (*Bayes' Decision Analysis*) | `level_2` | 2,720 chars |
| **SST 401** | Topic 228 (*Decision Trees*) | `level_2` | 2,660 chars |
| **SST 409** | Topic 249 (*Generating Functions*) | `level_2` | 2,677 chars |
| **SST 409** | Topic 252 (*Tail Or Cumulative Probabilities*) | `level_1`, `level_2`, `level_3` | ~2,450–2,940 chars |
| **SST 411** | Topic 266 (*The AR(1) Process*) | `level_2` | 2,587 chars |
| **SST 413** | Topic 276 (*Kolmogorov's 0-1 Law*) | `level_1` | 2,546 chars |
| **SMA 300** | Topic 19 (*The Real Number System*) | `level_2` | 2,441 chars |
| **SMA 330** | Topic 197 (*Errors And Approximations*) | `level_1`, `level_2`, `level_3` | ~2,860–3,850 chars |
| **SMA 330** | Topic 202 (*Numerical Differentiation*) | `level_3` | 3,516 chars |

---

### SST 305 Current Status

- **Topics 45, 46, 47, 48, 49, 50**: Successfully generated, fully validated, and committed at **18,000–24,700+ characters** each.
- **Topics 51, 52, 53 (`level_2`)**: Ready to be regenerated and committed to replace the short ~3,000 character stubs.

Ready to proceed with generating Topic 51 (*Method of Minimum Variance*).

Created inspect_models.py
Ran inspect models for questions and PDFs
Checked task Inspect models for questions and PDFs
Created inspect_fields.py
Ran inspect model fields for Paper, Question, PDF
Created inspect_stats_summary.py
Ran run inspect stats summary
Created generate_q_pdf_report.py
Ran run generate_q_pdf_report.py
Checked task Run generate_q_pdf_report.py
Analyzed past_questions_pdf_report.txt:L1-150
Created generate_active_q_pdf_report.py
Ran run filtered active courses Q & PDF report
Analyzed active_courses_q_pdf_report.txt:L1-250
Analyzed active_courses_q_pdf_report.txt:L251-500
Analyzed active_courses_q_pdf_report.txt:L501-737

Here is the complete audit and statistics for **Past Questions** and **Generated PDF Artifacts** across the catalog.

---

### 1. Overall System Summary

| Category | Metric | Count / Detail |
| :--- | :--- | :--- |
| **Past Exam Papers** | Total Papers in Database | **140 papers** |
| **Past Questions** | Total Extracted Questions | **2,320 questions** |
| | - Linked to Specific Topics | 1,822 questions (78.5%) |
| | - Unlinked (Paper-Level Only) | 498 questions (21.5%) |
| | - With Complete Worked Solution | **877 questions** (37.8%) |
| | - Without Solution | 1,443 questions (62.2%) |
| **Question Quality Status** | - Auto-Validated (`auto_validated`) | 712 |
| | - Formally Verified (`verified`) | 129 |
| | - AI-Reconstructed (`reconstructed`) | 458 |
| | - Flagged for Review (`flagged`) | 758 |
| | - Pending Initial Review (`pending`) | 263 |
| **Topic PDF Artifacts** | Total Artifact Records Tracked | **754 PDFs** |
| | - **Ready (Generated & Downloadable)** | **44 PDFs** |
| | - **Pending (Queued / Not Yet Generated)** | **686 PDFs** |
| | - **Empty (No Content Available to Build)** | **24 PDFs** (e.g., 0 questions or missing notes) |

---

### 2. PDF Artifacts Breakdown by Type & Status

| Artifact Type | Level / Variant | Ready | Pending | Empty | Total Records |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Topic Notes PDF** | `level_1` | 14 | 185 | 0 | 199 |
| **Topic Notes PDF** | `level_2` | 14 | 180 | 7 | 201 |
| **Topic Notes PDF** | `level_3` | 16 | 163 | 1 | 180 |
| **Past Questions PDF** | All Levels (Combined) | 0 | 158 | 16 | 174 |
| **Total** | | **44** | **686** | **24** | **754** |

> [!NOTE]
> The **44 Ready PDFs** currently exist in three courses:
> - **SST 305** (*Theory of Estimation*): **25 ready**
> - **SMA 300** (*Real Analysis I*): **16 ready**
> - **SST 301** (*Programming Language for Statistics 1*): **3 ready**
>
> All other courses have their PDF build jobs in `pending` status awaiting precomputation or generation.

---

### 3. Course-by-Course Stats (Active Prep Courses)

| Course Code & Title | Past Papers | Total Questions | With Solution | Unlinked Qs | Ready PDFs | Pending PDFs | Empty PDFs |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **ASC 100** — Introduction to Sociology | 5 | 30 | 23 | 0 | 0 | 24 | 0 |
| **EET 100** — Microeconomic Theory I | 7 | 53 | 53 | 0 | 0 | 20 | 0 |
| **SCS 209** — Internet Technology | 0 | 0 | 0 | 0 | 0 | 20 | 0 |
| **SMA 102** — Basic Mathematics | 8 | 94 | 57 | 0 | 0 | 32 | 0 |
| **SMA 103** — Analytical Geometry | 7 | 59 | 28 | 0 | 0 | 21 | 7 |
| **SMA 190** — Introduction to Computers | 0 | 3 | 3 | 0 | 0 | 24 | 8 |
| **SMA 200** — Calculus 2 | 8 | 242 | 0 | 242 | 0 | 48 | 0 |
| **SMA 230** — Vector Analysis | 13 | 133 | 53 | 26 | 0 | 22 | 0 |
| **SMA 300** — Real Analysis I | 9 | 161 | 97 | 7 | **16** | 6 | 1 |
| **SMA 330** — Numerical Analysis 1 | 12 | 126 | 35 | 18 | 0 | 40 | 0 |
| **SMA 335** — Ordinary Differential Equations 1 | 16 | 362 | 152 | 36 | 0 | 8 | 0 |
| **SST 101** — Intro to Probability & Statistics | 8 | 108 | 0 | 108 | 0 | 60 | 0 |
| **SST 200** — Computer Interactive Statistics | 4 | 22 | 3 | 6 | 0 | 20 | 0 |
| **SST 202** — Object Oriented Programming | 6 | 28 | 5 | 16 | 0 | 28 | 0 |
| **SST 204** — Probability and Statistics 1 | 17 | 551 | 189 | 5 | 0 | 42 | 1 |
| **SST 301** — Programming for Statistics 1 | 3 | 55 | 38 | 0 | **3** | 28 | 5 |
| **SST 304** — Multivariate Statistical Methods 1 | 5 | 83 | 34 | 8 | 0 | 15 | 0 |
| **SST 305** — Theory of Estimation | 7 | 145 | 76 | 0 | **25** | 10 | 1 |
| **SST 401** — Decision Theory | 0 | 0 | 0 | 0 | 0 | 24 | 0 |
| **SST 408** — Sample Surveys II | 0 | 0 | 0 | 0 | 0 | 36 | 0 |
| **SST 409** — Stochastic Processes | 1 | 19 | 0 | 19 | 0 | 33 | 0 |
| **SST 411** — Time Series Analysis | 1 | 7 | 0 | 7 | 0 | 27 | 0 |
| **SST 412** — Design & Analysis of Experiments | 0 | 0 | 0 | 0 | 0 | 28 | 0 |
| **SST 413** — Measure and Probability | 0 | 0 | 0 | 0 | 0 | 21 | 0 |
| **SST 404** — Econometrics 2 | 0 | 0 | 0 | 0 | 0 | 26 | 0 |
| **UCU 110** — Communication Skills | 3 | 39 | 31 | 0 | 0 | 23 | 1 |

---

### 4. SST 305 Focus (Your Current Target Course)

| Topic | Questions (Total / Solved) | Notes PDFs Ready | Questions PDF Status |
| :--- | :---: | :---: | :---: |
| **Topic 45**: Properties of Estimators | 5 / 4 | Level 1, 2, 3 (Ready) | Pending |
| **Topic 46**: Confidence Interval Estimation | 7 / 5 | Level 1, 2, 3 (Ready) | Pending |
| **Topic 47**: Sufficient Statistics | 0 / 0 | Level 1, 2, 3 (Ready) | Empty (No Questions) |
| **Topic 48**: Moment Estimation | 8 / 4 | Level 1, 2, 3 (Ready) | Pending |
| **Topic 49**: Maximum Likelihood Estimation | 4 / 2 | Level 1, 2, 3 (Ready) | Pending |
| **Topic 50**: Least Squares Estimation | 4 / 2 | Level 2 (Ready), L1/L3 Pending | Pending |
| **Topic 51**: Method of Minimum Variance | 70 / 35 | Level 1, 2, 3 (Ready) | Pending |
| **Topic 52**: Interval Estimation | 8 / 4 | Level 1, 2, 3 (Ready) | Pending |
| **Topic 53**: Interval Estimation (Two Means) | 39 / 20 | Level 1, 2, 3 (Ready) | Pending |
| **Course Total** | **145 / 76** | **25 Ready** | **1 Empty, 8 Pending** |

Ready to resume generating publication-grade notes for **Topic 51 (*Method of Minimum Variance*)**.