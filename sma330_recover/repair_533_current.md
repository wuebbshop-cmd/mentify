## 1. Core Concept Overview & Intuition

Numerical analysis is the discipline concerned with the development and evaluation of methods for computing required numerical results from given numerical data. In every numerical computation, errors and approximations are inevitably involved, so the computed result is only approximate, though it should lie very near the true value. The central purpose of this unit is to characterize the possibilities of error occurrence and to establish measures that safeguard against them.

Input information is rarely exact, since it ordinarily originates from measurement devices of some sort. The fundamental quantity of the subject is therefore the discrepancy between what is desired and what is obtained: the quantity *true value minus approximate value* is called the error. Two distinct mechanisms generate such discrepancies. The first is the impossibility of representing all real numbers exactly on a machine with finite memory, which produces round-off error. The second is the deliberate replacement of an exact infinite process by a finite one, which produces truncation error. A third, more subtle, mechanism is the amplification of small input discrepancies as they pass through a sequence of arithmetic operations; this is propagation of error.

The intuition that governs the whole lecture is that the *size* of an error is not by itself a reliable measure of the *quality* of an approximation. An absolute discrepancy of $0.1$ is catastrophic when the true value is $1$, but negligible when the true value is $10^{6}$. Accuracy must therefore be judged relative to the magnitude of the quantity being approximated, and this observation motivates the definitions of relative and percentage error and, in turn, the notion of significant figures. The lecture objectives are precisely to define and calculate round-off and truncation errors, to identify measures taken to minimize round-off errors, to define and calculate absolute, relative and percentage errors, and to calculate propagated errors with reference to numerical computations.

## 2. Mathematical Formalization & Core Definitions

### 2.1 Round-off and Truncation Errors

> **Definition (Round-off error).** Round-off error arises because it is impossible to represent all real numbers exactly on a machine with finite memory. It involves dropping out decimal places or significant figures, and may be performed either by chopping (truncating) or by symmetric rounding.

The two modes of discarding digits are distinct procedures for reducing the number of retained figures. Chopping, also called truncation, deletes all digits beyond the retained position and keeps the remaining digits unchanged. Symmetric rounding also discards the surplus digits but selects the retained value according to a rounding rule, so that the retained value is the one nearest to the original number. The two procedures therefore generally produce different approximations of the same real number, and the difference between them is visible whenever the discarded portion is nonzero.

The following table records certain real numbers rounded off under different conditions, illustrating the divergence between the two modes.

| Real number | Rounded to 4 sf | Rounded to 4 dp | Chopped to 4 sf |
|:--- |:--- |:--- |:--- |
| $1.3333\ldots$ | $1.333$ | $1.3333$ | $1.333$ |
| $0.03333\ldots$ | $0.0333$ | $0.0333$ | $0.03333$ |
| $0.6666\ldots$ | $0.6667$ | $0.6667$ | $0.6666$ |
| $3.14159\ldots$ | $3.142$ | $3.1416$ | $3.141$ |

When rounding to $n$ decimal places, the error introduced should be bounded by half a unit in the last retained place. The measures taken to minimize round-off error follow directly from this bound: retain as many digits as the machine permits, avoid subtracting nearly equal quantities, and arrange computations so that small quantities are not multiplied by large ones before being combined.

### 2.2 Absolute and Relative Error

> **Definition (Absolute error).** Let $r$ be an approximate number to an exact number $x$. The absolute error is the absolute difference between the exact number and the approximate number, namely $\lvert x-r \rvert$.

> **Definition (Relative error).** The relative error is the absolute error divided by the magnitude of the exact quantity, namely $\lvert x-r \rvert/\lvert x \rvert$.

> **Definition (Percentage error).** The percentage error is the relative error expressed as a percentage, namely $100\lvert x-r \rvert/\lvert x \rvert$.

The relative error is the more meaningful measure of accuracy because it takes into consideration the size of the value. The same relative error can occur for widely varying absolute errors, so an absolute error used alone as a measure of accuracy can be misleading.

### 2.3 Significant Figures

> **Definition (Significant figures).** If a number is correct to $n$ significant figures, the maximum absolute error consistent with that statement is $\lvert x\rvert\cdot 10^{-n}$, where $x$ is the exact quantity being approximated.

The relative error supplies a direct measure of the number of significant digits carried by an approximation. The significant-figure criterion is stated through the maximum absolute error, obtained by scaling the factor $10^{-n}$ by the magnitude of the quantity. Equivalently, the relative error of an approximation correct to $n$ significant figures is at most $10^{-n}$, so the relative error can be used to give a measure of the significant digits of an approximation.

### 2.4 Propagation Errors and the General Formula

> **Definition (Propagated error).** When approximate quantities are combined by arithmetic operations, the errors in the operands combine to produce an error in the result. The resulting discrepancy is the propagated error.

> **Theorem (General formula for propagated error).** If a quantity $y$ depends on measured quantities $x_{1},x_{2},\ldots,x_{n}$ through a differentiable function $y=f(x_{1},x_{2},\ldots,x_{n})$, and if $\Delta x_{i}$ denotes the error in $x_{i}$, then to first order the error in $y$ is

$$
\Delta y \approx \sum_{i=1}^{n}\frac{\partial f}{\partial x_{i}}\,\Delta x_{i}.
$$

> Consequently the maximum absolute propagated error is bounded by

$$
\lvert \Delta y \rvert \le \sum_{i=1}^{n}\left\lvert \frac{\partial f}{\partial x_{i}}\right\rvert\,\lvert \Delta x_{i} \rvert,
$$

> and the maximum relative propagated error is bounded by

$$
\left\lvert \frac{\Delta y}{y}\right\rvert \le \sum_{i=1}^{n}\left\lvert \frac{\partial f}{\partial x_{i}}\right\rvert\frac{\lvert \Delta x_{i}\rvert}{\lvert y \rvert}.
$$

The formula is obtained by expanding $f$ in a first-order Taylor series about the measured values and retaining only the linear terms; the partial derivatives measure the sensitivity of the result to each operand. For the elementary operations the formula specializes as follows. For a sum or difference $y=x_{1}\pm x_{2}$ the absolute errors add, so $\lvert \Delta y\rvert\le\lvert \Delta x_{1}\rvert+\lvert \Delta x_{2}\rvert$. For a product $y=x_{1}x_{2}$ the relative errors add, so the relative error of the product is at most the sum of the relative errors of the factors. For a quotient $y=x_{1}/x_{2}$ the relative error is at most the sum of the relative errors of numerator and denominator. These specializations explain why subtraction of nearly equal quantities is dangerous: the absolute errors add while the result shrinks, so the relative error of the difference can become enormous.

## 3. Key Theorems & Essential Results

> **Result 1 (Rounding bound).** When rounding to $n$ decimal places, the error introduced should be bounded by half a unit in the last retained place, that is, by $\tfrac{1}{2}\times 10^{-n}$.

> **Result 2 (Significant-figure criterion).** If a number is correct to $n$ significant figures, the maximum absolute error is $\lvert x\rvert\cdot 10^{-n}$, where $x$ is the exact quantity. Equivalently, the relative error of such an approximation is at most $10^{-n}$.

> **Result 3 (Additive propagation).** For $y=x_{1}\pm x_{2}$, the absolute error satisfies $\lvert \Delta y\rvert\le\lvert \Delta x_{1}\rvert+\lvert \Delta x_{2}\rvert$, and the relative error satisfies $\lvert \Delta y/y\rvert\le(\lvert \Delta x_{1}\rvert+\lvert \Delta x_{2}\rvert)/\lvert y\rvert$.

> **Result 4 (Multiplicative propagation).** For $y=x_{1}x_{2}$ or $y=x_{1}/x_{2}$, the relative error satisfies $\lvert \Delta y/y\rvert\le\lvert \Delta x_{1}/x_{1}\rvert+\lvert \Delta x_{2}/x_{2}\rvert$.

> **Result 5 (Reformulation).** Reformulation is the algebraic rearrangement of an expression into an equivalent form that is numerically more stable, so that the propagated error of the computed result is reduced without changing the exact value.

> **Result 6 (Interpolation).** Interpolation is the process of constructing a function, typically a polynomial, that passes exactly through a given set of data points and is used to estimate the value of the underlying function at points lying between the tabulated arguments.

## 4. Worked Exemplar Problem with Step-by-Step Solution

### 4.1 Problem Statement

(a) Define the following terms as used in computation: (i) relative error, (ii) reformulation, (iii) interpolation.

(b) The table below gives certain real numbers rounded off using different conditions. For the real number $x=0.6666\ldots$, state the value rounded to $4$ significant figures, the value rounded to $4$ decimal places, and the value chopped to $4$ significant figures, and compute the relative error of the chopped value.

### 4.2 Part (a): Definitions

(i) *Relative error.* If $r$ is an approximation to an exact quantity $x$, the relative error is $\lvert x-r\rvert/\lvert x\rvert$, the absolute error scaled by the magnitude of the exact quantity.

(ii) *Reformulation.* Reformulation is the rewriting of a computational expression into an algebraically equivalent form chosen to reduce propagated and round-off error, for example replacing a subtraction of nearly equal quantities by an equivalent expression free of cancellation.

(iii) *Interpolation.* Interpolation is the construction of a function, usually a polynomial, that agrees exactly with a given set of data values at prescribed arguments and is then used to estimate values of the underlying function between those arguments.

### 4.3 Part (b): Rounding and Chopping the Given Number

The exact quantity is $x=0.6666\ldots$, the recurring decimal for two thirds.

*Step 1: Round to $4$ significant figures.* The first four significant digits are $6666$, and the next digit is $6$, so the retained last digit is increased by one:

$$
x\approx 0.6667.
$$

*Step 2: Round to $4$ decimal places.* The first four decimal places are $6666$, and the next digit is $6$, so again the retained last digit is increased by one:

$$
x\approx 0.6667.
$$

*Step 3: Chop to $4$ significant figures.* The surplus digits are simply deleted and the retained digits are left unchanged:

$$
x\approx 0.6666.
$$

### 4.4 Relative Error of the Chopped Value

The absolute error of the chopped value is

$$
\lvert x-r\rvert=\lvert 0.6666\ldots-0.6666\rvert=0.0000666\ldots
$$

The relative error is the absolute error divided by the magnitude of the exact quantity:

$$
\frac{\lvert x-r\rvert}{\lvert x\rvert}=\frac{0.0000666\ldots}{0.6666\ldots}\approx 0.0001.
$$

The percentage error is therefore approximately $0.01\%$.

### 4.5 Interpretation

The rounded and chopped values differ in the fourth decimal place, and the chopped value carries a relative error of about $10^{-4}$, consistent with the significant-figure criterion for four significant figures. The example illustrates that chopping and symmetric rounding are distinct procedures: both discard the surplus digits, but only rounding adjusts the retained value, so the two approximations of the same real number generally differ, and their errors differ accordingly.

## 5. High-Yield Exam Takeaways & Common Pitfalls

### 5.1 High-Yield Takeaways

- The error is defined as true value minus approximate value; the absolute error is its magnitude, the relative error divides that magnitude by the magnitude of the exact quantity, and the percentage error multiplies the relative error by one hundred.
- Round-off error originates in the finite representation of real numbers and is realized either by chopping or by symmetric rounding; truncation error originates in replacing an exact infinite process by a finite one.
- Rounding to $n$ decimal places introduces an error bounded by half a unit in the last retained place, that is, by $\tfrac{1}{2}\times 10^{-n}$.
- If a number is correct to $n$ significant figures, the maximum absolute error is $\lvert x\rvert\cdot 10^{-n}$, where $x$ is the exact quantity; equivalently the relative error is at most $10^{-n}$.
- The general propagated-error formula is the first-order Taylor expansion $\Delta y\approx\sum_{i}\frac{\partial f}{\partial x_{i}}\Delta x_{i}$, with the maximum bound obtained by replacing each term by its absolute value.
- Absolute errors add under addition and subtraction; relative errors add under multiplication and division.
- Relative error, not absolute error, is the correct measure of accuracy, because it accounts for the size of the quantity being approximated.
- Reformulation is the standard remedy for cancellation, and interpolation is the standard construction for estimating a function between tabulated arguments.

### 5.2 Common Pitfalls

- Reporting an absolute error as though it measured accuracy, without reference to the magnitude of the quantity; the same relative error can accompany wildly different absolute errors.
- Confusing chopping with symmetric rounding: chopping deletes the surplus digits and leaves the retained digits unchanged, whereas rounding selects the retained value by a rounding rule, so the two give different results whenever the discarded portion is nonzero.
- Applying the significant-figure criterion with the wrong exponent, using $5\times 10^{-n}$ where $\lvert x\rvert\cdot 10^{-n}$ is required, or scaling by the approximate rather than the exact magnitude.
- Forgetting to round every intermediate result when the question specifies $k$-digit rounding arithmetic; the instruction applies at each operation, not only at the end.
- Subtracting nearly equal quantities without recognizing the resulting loss of significant digits, and failing to reformulate the expression to avoid the cancellation.