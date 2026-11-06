## 1. Core Concept Overview & Intuition

### 1.1 Scope and Purpose of the Unit

This unit is the foundational lecture of the numerical analysis sequence. Its central message is that **numerical computation is never exact**. Every quantity that enters a computation — whether it is a measured physical constant, a tabulated function value, or a decimal expansion of an irrational number — is represented on a machine with finite memory. Consequently, every computed result carries an error, and the numerical analyst's task is to *quantify*, *bound*, and *control* that error.

The lecture is organised around a single logical chain:

- **Where do errors come from?** They arise from representing real numbers in finite precision (round-off) and from replacing infinite processes by finite ones (truncation).
- **How do we measure an error?** Through the absolute error, the relative error, and the percentage error.
- **How do we express the accuracy of a stored number?** Through the count of significant figures (or significant digits).
- **What happens when erroneous inputs are fed into arithmetic operations?** The errors combine and grow — this is *propagation of error*.
- **Is there a single formula that governs this growth?** Yes: the general formula for propagated error, built from partial derivatives.

### 1.2 Intuition Behind Each Subtopic

**Round-off and truncation errors.** Imagine trying to write the fraction $\frac{1}{3}$ as a decimal on paper with only four decimal places. You must stop somewhere, and the act of stopping introduces an error. Round-off error is precisely this: the unavoidable loss caused by the finite storage capacity of a machine. It can be executed in two distinct ways — by *chopping* (simply discarding the surplus digits) or by *symmetric rounding* (inspecting the first discarded digit and adjusting the last retained digit upward when appropriate). Truncation error, by contrast, is the error committed when an exact mathematical process is replaced by an approximate one, for instance when an infinite series is cut off after finitely many terms.

**Absolute and relative errors.** Suppose a computed value is $r$ while the exact value is $x$. The absolute error is the raw size of the discrepancy, $\lvert x-r\rvert$. But raw size can be deeply misleading: an absolute error of $0.1$ is catastrophic when the true value is $1$, yet negligible when the true value is $10^{6}$. The relative error divides the absolute error by the magnitude of the exact value, producing a scale-free measure of accuracy. This is why the same relative error can coexist with wildly different absolute errors — a point the source material stresses explicitly.

**Significant figures.** The relative error is the natural gateway to counting significant digits. A number stored with a small relative error is said to be accurate to many significant figures; a number stored with a large relative error is accurate to few. The lecture uses the relative error to *give a measure of the significant digits* of an approximation.

**Propagation errors.** In practice, computations chain together. If $x$ is known only approximately and we compute a function $f(x)$, the error in $x$ is transmitted to $f(x)$. When several approximate quantities are combined, their individual errors interact — sometimes reinforcing, sometimes cancelling. The general formula for propagated error captures this transmission through the derivative (or, for several variables, the partial derivatives) of the function being evaluated.

### 1.3 The Examination Lens

Examiners in this unit test three skills repeatedly:

- **Classification**: given a described situation, decide whether the error is round-off or truncation, absolute or relative.
- **Computation**: carry out rounding and chopping to a stated number of significant figures or decimal places, and compute absolute, relative, and percentage errors.
- **Bounding**: use the general propagation formula to estimate the maximum error in a computed quantity, and to decide how many significant figures a result legitimately possesses.

The high-yield habit is to *always state the formula before substituting*, to *keep the exact value and the approximate value clearly labelled*, and to *report the final error with its correct units or as a dimensionless ratio*.

## 2. Mathematical Formalization & Core Definitions

### 2.1 The Definition of Error

> **Definition (Error).** Let $x$ denote the exact (true) value of a quantity and let $r$ denote an approximate value of it. The error is the quantity
> 

$$
e=x-r.
$$

> The quantity $\lvert x-r\rvert$ is the magnitude of the error.

The source material states this plainly: the quantity *true value minus approximate value* is called the error. Note the sign convention — a positive error means the approximation is an underestimate.

### 2.2 Round-off Error

> **Definition (Round-off Error).** Round-off error arises because it is impossible to represent all real numbers exactly on a machine with finite memory. It is produced by dropping decimal places or significant figures, and may be carried out either by chopping (truncating) or by symmetric rounding.

The two mechanisms must be distinguished carefully:

- **Chopping (truncation of digits):** all digits beyond the retained position are simply discarded. The retained digits are unchanged.
- **Symmetric rounding:** the first discarded digit is inspected. If it is $5$ or greater, the last retained digit is increased by $1$; otherwise it is left unchanged.

The source presents a table of real numbers processed under different conditions, which is reproduced below with the columns made explicit. The column headings are: the real number; the value rounded to four significant figures; the value rounded to four decimal places; and the value chopped to four significant figures.

| Real number | Rounded to 4 s.f. | Rounded to 4 d.p. | Chopped to 4 s.f. |
|---|---|---|---|
| $1.333$ | $1.333$ | $1.3333$ | $1.333$ |
| $0.03333$ | $0.03333$ | $0.0333$ | $0.03333$ |
| $0.6667$ | $0.6667$ | $0.6667$ | $0.6666$ |
| $3.142$ | $3.142$ | $3.1416$ | $3.141$ |

Two lessons emerge from this table. First, rounding and chopping can disagree in the last retained digit — compare $0.6667$ chopped to four significant figures, which gives $0.6666$, with the same number rounded, which gives $0.6667$. Second, the number of significant figures and the number of decimal places are *different specifications*: $0.03333$ to four significant figures is $0.03333$, whereas to four decimal places it is $0.0333$.

> **Result (Rounding Error Bound).** When a number is rounded to $n$ decimal places, the error introduced does not exceed half a unit in the last retained place, that is
> 

$$
\lvert e\rvert\le 0.5\times 10^{-n}.
$$

This bound is the engine behind all the absolute-error estimates in the lecture. For example, if a value is correct to one decimal place, the maximum absolute error is $0.5\times 10^{-1}=0.05$, and the source writes the bound as $\lvert -0.05\rvert=0.05$ in magnitude.

### 2.3 Truncation Error

> **Definition (Truncation Error).** Truncation error is the error committed when an exact mathematical procedure is replaced by an approximate one — for instance, when an infinite process is terminated after finitely many steps, or when a function is replaced by a simpler approximating function.

The distinction to memorise for examinations is causal: round-off error is caused by *storage limitations of the machine*, whereas truncation error is caused by *the mathematical approximation itself* and would persist even on a machine with unlimited memory.

### 2.4 Absolute Error

> **Definition (Absolute Error).** Let $r$ be an approximate number to an exact number $x$. The absolute error is the absolute difference between the exact number and the approximate number:
> 

$$
E_{a}=\lvert x-r\rvert.
$$

If a bound $\delta$ is known such that $\lvert x-r\rvert\le\delta$, then $\delta$ is called the *maximum absolute error*.

### 2.5 Relative and Percentage Error

> **Definition (Relative Error).** The relative error is the absolute error divided by the magnitude of the exact value:
> 

$$
E_{r}=\frac{\lvert x-r\rvert}{\lvert x\rvert},\qquad x\neq 0.
$$

> **Definition (Percentage Error).** The percentage error is the relative error expressed as a percentage:
> 

$$
E_{p}=100\,E_{r}=100\,\frac{\lvert x-r\rvert}{\lvert x\rvert}.
$$

The source material emphasises the interpretive point that must appear in any examination answer: *the same relative error occurs for widely varying absolute errors*. As a measure of accuracy the absolute error can be misleading; the relative error is more meaningful because it takes into consideration the size of the value.

### 2.6 Significant Figures

> **Definition (Significant Figures).** A number is correct to $n$ significant figures when its relative error is small enough that the first $n$ digits of the number are reliable. The relative error is used to give a measure of the significant digits of an approximation.

The operational rule used throughout the lecture is the following. If a number is correct to $n$ decimal places, then its maximum absolute error is

$$
\lvert e\rvert_{\max}=0.5\times 10^{-n},
$$

and the corresponding maximum relative error is obtained by dividing this bound by the magnitude of the number. The count of significant figures is then read off from the size of the relative error: a relative error of order $10^{-k}$ corresponds to roughly $k$ reliable significant digits.

### 2.7 Propagation of Error

> **Definition (Propagated Error).** When approximate quantities are substituted into a function, the errors in the inputs are transmitted to the output. The resulting error in the output is called the propagated error.

For a function of a single variable, $y=f(x)$, with $x$ known only to within an absolute error $\Delta x$, the propagated error in $y$ is estimated by the differential approximation

$$
\Delta y\approx f'(x)\,\Delta x,
$$

so that the maximum absolute propagated error is

$$
\lvert \Delta y\rvert_{\max}\approx \lvert f'(x)\rvert\,\lvert \Delta x\rvert_{\max}.
$$

### 2.8 General Formula for Propagated Error

> **Theorem (General Formula for Propagated Error).** Let $y=f(x_{1},x_{2},\dots,x_{n})$ be a differentiable function of $n$ approximate quantities, and suppose the maximum absolute error in $x_{i}$ is $\Delta x_{i}$ for each $i$. Then the maximum absolute propagated error in $y$ is
> 

$$
\Delta y\approx\sum_{i=1}^{n}\left\lvert\frac{\partial f}{\partial x_{i}}\right\rvert\,\Delta x_{i}.
$$

> The corresponding maximum relative propagated error is
> 

$$
\frac{\Delta y}{\lvert y\rvert}\approx\sum_{i=1}^{n}\left\lvert\frac{\partial f}{\partial x_{i}}\right\rvert\frac{\Delta x_{i}}{\lvert y\rvert}.
$$

The absolute values in the sum are essential: they represent the worst case in which every individual error acts in the same direction, reinforcing the total. This is the conservative bound that examinations expect.

Two special cases are tested constantly and should be memorised as immediate consequences.

**Sum and difference.** If $y=x_{1}\pm x_{2}$, then $\partial f/\partial x_{1}=1$ and $\partial f/\partial x_{2}=\pm 1$, so

$$
\Delta y\approx \Delta x_{1}+\Delta x_{2}.
$$

Absolute errors add regardless of whether the quantities are added or subtracted.

**Product and quotient.** If $y=x_{1}x_{2}$, then the relative errors add:

$$
\frac{\Delta y}{\lvert y\rvert}\approx \frac{\Delta x_{1}}{\lvert x_{1}\rvert}+\frac{\Delta x_{2}}{\lvert x_{2}\rvert}.
$$

The same additive rule holds for a quotient $y=x_{1}/x_{2}$. This is the single most frequently examined consequence of the general formula.

## 3. Key Theorems & Essential Results

### 3.1 The Rounding Bound

> **Result.** If a number is rounded to $n$ decimal places, the absolute error satisfies $\lvert e\rvert\le 0.5\times 10^{-n}$. If a number is correct to $n$ decimal places, the maximum absolute error is $0.5\times 10^{-n}$.

This result converts a statement about decimal places into a numerical error bound, and it is the first step in almost every propagation calculation.

### 3.2 The Relative Error Criterion for Accuracy

> **Result.** The relative error $E_{r}=\lvert x-r\rvert/\lvert x\rvert$ is a scale-free measure of accuracy. Two approximations with the same relative error are equally accurate in the significant-figure sense, even if their absolute errors differ by orders of magnitude.

The source illustrates this with three cases in which the same relative error arises from very different absolute errors, and concludes that the absolute error alone can be misleading.

### 3.3 The General Propagation Formula

> **Theorem.** For $y=f(x_{1},\dots,x_{n})$ differentiable, the maximum absolute propagated error is $\Delta y\approx\sum_{i}\lvert \partial f/\partial x_{i}\rvert\,\Delta x_{i}$, and the maximum relative propagated error is obtained by dividing this expression by $\lvert y\rvert$.

This theorem is the culmination of the lecture and the standard source of multi-mark examination questions.

### 3.4 The Additivity Rules

> **Corollary (Additive Absolute Errors).** For $y=x_{1}\pm x_{2}$, $\Delta y\approx\Delta x_{1}+\Delta x_{2}$.

> **Corollary (Additive Relative Errors).** For $y=x_{1}x_{2}$ or $y=x_{1}/x_{2}$, $\Delta y/\lvert y\rvert\approx \Delta x_{1}/\lvert x_{1}\rvert+\Delta x_{2}/\lvert x_{2}\rvert$.

These corollaries are the practical face of the general formula and should be quoted by name in examination answers.

### 3.5 The Significant-Figures Link

> **Result.** The relative error determines the number of significant digits of an approximation. A relative error of order $10^{-k}$ corresponds to approximately $k$ reliable significant figures.

This result is what allows an examiner to ask "to how many significant figures is the result reliable?" and expect a numerical justification rather than a guess.

## 4. Worked Exemplar Problem with Step-by-Step Solution

### 4.1 Problem Statement

A quantity is measured as $x=2.45$ correct to three significant figures, and a second quantity is measured as $y=1.20$ correct to three significant figures. The computed quantity is

$$
z=\frac{x^{2}}{y}.
$$

Determine the maximum absolute error and the maximum relative error in $z$, and state to how many significant figures $z$ is reliable.

### 4.2 Step 1: Extract the Input Error Bounds

The value $x=2.45$ is correct to three significant figures, that is to two decimal places. By the rounding bound,

$$
\Delta x=0.5\times 10^{-2}=0.005.
$$

Similarly, $y=1.20$ is correct to two decimal places, so

$$
\Delta y=0.5\times 10^{-2}=0.005.
$$

### 4.3 Step 2: Compute the Nominal Value

$$
z=\frac{(2.45)^{2}}{1.20}.
$$

Evaluating the numerator,

$$
(2.45)^{2}=6.0025,
$$

so

$$
z=\frac{6.0025}{1.20}=5.002083\ldots
$$

### 4.4 Step 3: Apply the General Propagation Formula

The function is $z=f(x,y)=x^{2}y^{-1}$. The partial derivatives are

$$
\frac{\partial z}{\partial x}=\frac{2x}{y},\qquad \frac{\partial z}{\partial y}=-\frac{x^{2}}{y^{2}}.
$$

The general formula gives

$$
\Delta z\approx\left\lvert\frac{2x}{y}\right\rvert\Delta x+\left\lvert-\frac{x^{2}}{y^{2}}\right\rvert\Delta y.
$$

Substituting the numerical values,

$$
\frac{2x}{y}=\frac{2(2.45)}{1.20}=4.083333,
$$

and

$$
\frac{x^{2}}{y^{2}}=\frac{6.0025}{1.44}=4.168403.
$$

Therefore

$$
\Delta z\approx (4.083333)(0.005)+(4.168403)(0.005).
$$

Adding the two contributions,

$$
\Delta z\approx 0.0204167+0.0208420=0.0412587.
$$

Hence the maximum absolute error is approximately

$$
\Delta z\approx 0.0413.
$$

### 4.5 Step 4: Compute the Maximum Relative Error

Dividing the absolute error by the magnitude of $z$,

$$
\frac{\Delta z}{\lvert z\rvert}\approx\frac{0.0412587}{5.002083}=0.008248.
$$

Expressed as a percentage,

$$
E_{p}\approx 0.8248\%.
$$

### 4.6 Step 5: Interpret the Significant Figures

The relative error is approximately $8.25\times 10^{-3}$, which is of order $10^{-2}$ to $10^{-3}$. The result is therefore reliable to about two significant figures, so the computed value should be reported as

$$
z\approx 5.0.
$$

Reporting $z=5.002083$ would be a serious overstatement of accuracy and is a classic examination trap.

### 4.7 Step 6: Cross-Check Using the Additivity Rules

As an independent check, apply the product-and-quotient rule directly. Since $z=x^{2}/y$, the relative error is

$$
\frac{\Delta z}{\lvert z\rvert}\approx 2\frac{\Delta x}{\lvert x\rvert}+\frac{\Delta y}{\lvert y\rvert}.
$$

Now

$$
\frac{\Delta x}{\lvert x\rvert}=\frac{0.005}{2.45}=0.0020408,
$$

and

$$
\frac{\Delta y}{\lvert y\rvert}=\frac{0.005}{1.20}=0.0041667.
$$

Therefore

$$
\frac{\Delta z}{\lvert z\rvert}\approx 2(0.0020408)+0.0041667=0.0082483,
$$

which agrees with the partial-derivative computation. The absolute error follows as

$$
\Delta z\approx (0.0082483)(5.002083)=0.04126,
$$

confirming the earlier value.

### 4.8 Step 7: Present the Final Answer

The maximum absolute error in $z$ is approximately $0.041$, the maximum relative error is approximately $0.00825$ (that is $0.825\%$), and the value $z\approx 5.0$ is reliable to two significant figures.

## 5. High-Yield Exam Takeaways & Common Pitfalls

### 5.1 High-Frequency Question Patterns

- **Classify the error.** A question describes a situation and asks whether the error is round-off or truncation. The discriminator is cause: finite machine storage gives round-off; replacing an exact process by an approximate one gives truncation.
- **Round and chop to a stated specification.** You will be asked to round a list of numbers to a given number of significant figures and to a given number of decimal places, and to chop them to a given number of significant figures. The two specifications are not interchangeable.
- **Compute absolute, relative, and percentage errors.** Given an exact value and an approximation, produce all three. Always divide by the magnitude of the *exact* value when forming the relative error.
- **Use the rounding bound.** Convert "correct to $n$ decimal places" into a maximum absolute error of $0.5\times 10^{-n}$ before doing anything else.
- **Apply the general propagation formula.** Multi-variable functions such as products, quotients, and powers are the standard vehicle. Expect to compute partial derivatives, take absolute values, and sum.
- **State the significant figures of a final result.** After computing a relative error, convert it into a statement about reliable significant figures.

### 5.2 Marking Rubric Tips

- **Quote the formula first.** Write the definition or theorem you are using before substituting numbers. Marks are allocated for the stated formula independently of the arithmetic.
- **Label exact and approximate values.** Use distinct symbols, for example $x$ for the exact value and $r$ for the approximation, and keep them consistent throughout.
- **Show the partial derivatives explicitly.** In propagation questions, the derivative computation carries marks even if the final arithmetic slips.
- **Keep absolute values in the propagation sum.** Writing $\Delta y=\sum(\partial f/\partial x_{i})\Delta x_{i}$ without absolute values loses the worst-case interpretation and typically loses marks.
- **Report units and dimensions.** A relative error is dimensionless; an absolute error carries the units of the quantity. State which is which.
- **Finish with an interpretation sentence.** Examiners reward a closing statement such as "the result is reliable to two significant figures".

### 5.3 Common Pitfalls and Traps

- **Confusing significant figures with decimal places.** The number $0.03333$ to four significant figures is $0.03333$, but to four decimal places it is $0.0333$. Read the specification twice.
- **Chopping when rounding was requested, or vice versa.** Chopping $0.6667$ to four significant figures gives $0.6666$, whereas rounding gives $0.6667$. The difference is a mark.
- **Dividing by the approximate value.** The relative error is defined with the exact value in the denominator. Using the approximation introduces a second-order error and is penalised.
- **Forgetting the factor of one half.** The rounding bound is $0.5\times 10^{-n}$, not $10^{-n}$. Omitting the half doubles every downstream error estimate.
- **Dropping the absolute values in the propagation formula.** Errors can have either sign; the worst case requires summing magnitudes. Sign-cancellation in the formula is a conceptual error, not a simplification.
- **Treating the propagation estimate as exact.** The formula is a first-order differential approximation. It is a bound, and it should be reported as approximate.
- **Over-reporting digits.** Presenting a final answer to seven decimal places when the relative error is of order $10^{-3}$ is a standard accuracy error. Round the final answer to the number of significant figures justified by the error analysis.
- **Mixing up the two error types in a single computation.** A computation can suffer from both round-off and truncation simultaneously; identify each separately rather than attributing the whole discrepancy to one cause.

### 5.4 Time-Management Strategy

- **Allocate the first minute to classification.** Decide immediately whether the question concerns round-off, truncation, absolute error, relative error, significant figures, or propagation. This determines the entire solution route.
- **Write the governing formula within the first two minutes.** This secures the method marks early and structures the remaining work.
- **Do the error bounds before the arithmetic.** Extract $\Delta x_{i}$ from the stated decimal places first; the propagation sum then follows mechanically.
- **Reserve the final minute for the interpretation sentence.** The significant-figures conclusion is a discrete mark that is frequently lost to haste.
- **If a partial derivative becomes unwieldy, switch to the additivity rules.** For products, quotients, and powers, the relative-error rule $2\Delta x/\lvert x\rvert+\Delta y/\lvert y\rvert$ is faster and self-checking.

### 5.5 Self-Test Checklist

Before the examination, confirm that you can do each of the following without notes:

- State the definition of error as true value minus approximate value.
- Distinguish round-off from truncation error by cause.
- Round and chop a given number to a stated number of significant figures and decimal places.
- State and use the rounding bound $0.5\times 10^{-n}$.
- Compute absolute, relative, and percentage errors from an exact and an approximate value.
- Explain why the relative error is a better measure of accuracy than the absolute error.
- Convert a relative error into a statement about significant figures.
- State the general formula for propagated error and derive the additivity rules for sums, differences, products, and quotients from it.
- Apply the propagation formula to a multi-variable function and report the result to a justified number of significant figures.