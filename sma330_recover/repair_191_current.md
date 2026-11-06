## 1. Core Concept Overview & Intuition

Numerical analysis is the discipline concerned with the development and evaluation of methods for computing required numerical results from given numerical data. In every numerical computation, errors and approximations are inevitably involved, so the computed result is only approximate and merely very near to the true value. The quantity obtained by subtracting the approximate value from the true value is called the error. Because input information rarely is exact (it ordinarily comes from measurement devices of some sort), the study of how errors arise, how they are measured, and how they propagate through arithmetic is foundational to all later work on polynomials, interpolation, finite differences, and iterative methods.

Two broad mechanisms generate computational error. **Round-off error** arises because it is impossible to represent all real numbers exactly on a machine with finite memory; it is produced by dropping decimal places or significant figures, either by chopping (truncating) or by symmetric rounding. **Truncation error** arises when an infinite or more detailed process is replaced by a finite or simpler one. Once an error exists, it must be quantified. The **absolute error** measures the raw size of the discrepancy, while the **relative error** measures that discrepancy in proportion to the magnitude of the quantity itself; the relative error is the more meaningful measure of accuracy because it takes into consideration the size of the value, whereas the absolute error can be misleading. The relative error also yields a practical measure of the number of **significant digits** that may be trusted, and it is the natural vehicle for studying **propagation of error**, that is, how errors in input quantities combine to produce an error in a computed result. The general formula for propagated error expresses the total error of a function of several approximate arguments in terms of the errors of those arguments.

## 2. Mathematical Formalization & Core Definitions

> **Definition (Error).** If $x$ denotes the true value of a quantity and $r$ denotes an approximate value of it, then the error is the quantity true value minus approximate value.

> **Definition (Round-off Error).** Round-off error is the error introduced because it is impossible to represent all real numbers exactly on a machine with finite memory. It is produced by dropping decimal places or significant figures, and may be carried out either by chopping (truncating) or by symmetric rounding.

> **Definition (Absolute Error).** Let $r$ be an approximate number to an exact number $x$. The absolute error is the absolute difference between the exact number and the approximate number, namely $\lvert x-r \rvert$.

> **Definition (Relative Error).** The relative error is defined as the absolute error measured against the exact quantity, namely

$$
\frac{\lvert x-r \rvert}{\lvert x \rvert}.
$$

The relative error can be used to evaluate the percentage error, which expresses the same discrepancy as a proportion of the exact value.

### 2.1 Rounding Conventions and the Error Bound

When a number is rounded to $n$ decimal places, the error introduced is bounded by half a unit in the last retained place. If a number is correct to $n$ decimal places, then the maximum absolute error is

$$
\text{maximum absolute error}=\frac{1}{2}\times 10^{-n}.
$$

The following table records the behaviour of representative real numbers under different rounding conditions, where "4sf" means four significant figures, "4dp" means four decimal places, and "chopped to 4s" means truncated to four significant figures.

| Real number | Rounded to 4sf | Rounded to 4dp | Chopped to 4sf |
|---|---|---|---|
| $1.333$ | $1.333$ | $1.3333$ | $1.333$ |
| $0.03333$ | $0.0333$ | $0.0333$ | $0.03333$ |
| $0.6667$ | $0.6667$ | $0.6667$ | $0.6666$ |
| $3.142$ | $3.142$ | $3.1416$ | $3.141$ |

Chopping and symmetric rounding differ precisely in the last retained digit: chopping always discards the tail, whereas symmetric rounding adjusts the last retained digit upward when the discarded tail is at least half a unit.

### 2.2 Absolute Error Bounds in Practice

If a number is correct to one decimal place, the maximum absolute error is $0.05$, since

$$
\frac{1}{2}\times 10^{-1}=0.05.
$$

If a number is correct to three decimal places, the maximum absolute error is

$$
\frac{1}{2}\times 10^{-3}=0.0005.
$$

In general, if a number is correct to $n$ decimal places, then the maximum absolute error is $\tfrac{1}{2}\times 10^{-n}$.

### 2.3 Relative Error and Significant Digits

The relative error can be used to give a measure of the significant digits of an approximation. The same relative error can occur for widely varying absolute errors, which is exactly why the relative error is the preferred measure of accuracy: it takes into consideration the size of the value being approximated.

> **Definition (Significant Figures).** The significant figures of an approximation are the digits that carry meaning contributing to its precision; the relative error provides a quantitative measure of how many such digits may be trusted.

## 3. Key Theorems & Essential Results

> **Result (Maximum Absolute Error for $n$ Decimal Places).** If a number is correct to $n$ decimal places, then the maximum absolute error is $\tfrac{1}{2}\times 10^{-n}$.

> **Result (Relative Error as an Accuracy Measure).** For an exact quantity $x$ and approximation $r$, the relative error is $\lvert x-r \rvert/\lvert x \rvert$. It is more meaningful than the absolute error because it takes into consideration the size of the value, and it can be used to evaluate the percentage error.

> **Result (General Formula for Propagated Error).** When a computed quantity depends on several approximate arguments, the error in the result is obtained by combining the errors of the arguments according to the sensitivity of the result to each argument. The propagated error is therefore expressed as a sum of contributions, each contribution being the error of one argument multiplied by the rate at which the result responds to that argument.

The practical content of the propagation result is that errors do not simply add as raw magnitudes; they are weighted by the influence each input has on the output. An input to which the result is highly sensitive contributes a large share of the total error even if its own error is small, while an input to which the result is insensitive contributes little even if its own error is comparatively large. This is the analytical justification for the emphasis placed on relative error: a computation should be judged by how large the propagated error is relative to the size of the answer.

### 3.1 Measures Taken to Minimize Round-off Error

The lecture objectives require the identification of measures taken to minimize round-off error. The controlling principle is to reduce the number of arithmetic operations performed on finite-memory representations, and to avoid subtracting nearly equal quantities. Rearranging an expression so that fewer operations are required, and so that no step destroys significant digits through cancellation, directly reduces the accumulated round-off. This principle motivates the nested (Horner) form of a polynomial, in which the polynomial is rewritten as a succession of multiply-and-add steps rather than as a sum of separately computed powers.

## 4. Worked Exemplar Problem with Step-by-Step Solution

**Problem.** A quantity is known to be correct to three decimal places, and its approximate value is $r=10.788$. Determine the maximum absolute error, and hence bound the relative error of the approximation.

**Step 1. Identify the number of correct decimal places.** The value is correct to $n=3$ decimal places.

**Step 2. Apply the maximum absolute error bound.**

$$
\text{maximum absolute error}=\frac{1}{2}\times 10^{-3}=0.0005.
$$

**Step 3. Form the relative error bound.** Using the exact magnitude $x\approx 10.788$,

$$
\text{relative error}\le \frac{0.0005}{10.788}\approx 4.63\times 10^{-5}.
$$

**Step 4. Interpret the result.** The absolute error is at most half a unit in the third decimal place, and the relative error is of order $10^{-5}$, confirming that roughly five significant digits of the approximation may be trusted.

**Illustration of the contrast between absolute and relative error.** Consider three approximations. If $x=100$ and the absolute error is $0.1$, the relative error is $0.1/100=0.001$. If $x=10$ and the absolute error is $0.1$, the relative error is $0.1/10=0.01$. If $x=1$ and the absolute error is $0.1$, the relative error is $0.1/1=0.1$. The absolute error is identical in all three cases, yet the relative error varies by two orders of magnitude, which demonstrates that the absolute error alone can be misleading as a measure of accuracy.

**Illustration of the propagation principle.** Suppose a computed result is formed from two approximate arguments, one carrying a small error but entering the computation with a large multiplier, and the other carrying a larger error but entering with a small multiplier. The propagated error is dominated by the first argument, because each argument's error is weighted by the sensitivity of the result to that argument. The correct procedure is therefore to compute each weighted contribution separately and then combine them, rather than to compare the raw input errors directly.

## 5. High-Yield Exam Takeaways & Common Pitfalls

**High-yield takeaways.**

- The error is defined as true value minus approximate value; the absolute error is $\lvert x-r \rvert$ and the relative error is $\lvert x-r \rvert/\lvert x \rvert$.
- Round-off error originates in finite machine memory and is realized by chopping or by symmetric rounding; truncation error originates in replacing an infinite or more detailed process by a finite or simpler one.
- A number correct to $n$ decimal places has maximum absolute error $\tfrac{1}{2}\times 10^{-n}$; a number correct to one decimal place has maximum absolute error $0.05$.
- The relative error, not the absolute error, is the meaningful measure of accuracy, because it accounts for the size of the value; the percentage error is $100$ times the relative error.
- The relative error supplies a measure of the significant digits that may be trusted in an approximation.
- Propagated error is obtained by weighting each argument's error by the sensitivity of the result to that argument and combining the weighted contributions.
- Round-off error is minimized by reducing the number of operations and by avoiding cancellation between nearly equal quantities.

**Common pitfalls.**

- Reporting the absolute error as though it measured accuracy: the same absolute error can correspond to relative errors differing by orders of magnitude, so the absolute error alone can be misleading.
- Confusing chopping with symmetric rounding: chopping always discards the tail, whereas symmetric rounding may raise the last retained digit.
- Using $\tfrac{1}{2}\times 10^{-n}$ with the wrong $n$: the exponent must match the number of correct decimal places, not the number of significant figures.
- Forgetting to take the absolute value in the absolute and relative error definitions, which produces a negative "error" and an incorrect bound.
- Treating propagated errors as simple sums of raw input errors instead of weighting each by the sensitivity of the result to that argument.
- Neglecting the reduction of operation count when minimizing round-off, thereby allowing avoidable accumulation of error in a long computation.