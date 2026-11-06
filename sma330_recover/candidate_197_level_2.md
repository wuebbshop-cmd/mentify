## 1. Foundational Concepts, Definitions, and Axioms

Numerical analysis is the discipline concerned with the development and evaluation of methods for computing required numerical results from given numerical data. In every numerical computation, errors and approximations are inevitably involved, so the computed result is only approximate, though it should lie very near the true value. The central purpose of this unit is to characterize the possibilities of error occurrence and to establish measures that safeguard against them.

Input information is rarely exact, since it ordinarily originates from measurement devices of some sort. The fundamental quantity of the subject is therefore the discrepancy between what is desired and what is obtained: the quantity *true value minus approximate value* is called the error. Round-off arises when finite storage represents a real number by a limited set of digits; the stored result may be obtained by chopping or by symmetric rounding. In numerical methods, truncation error can also describe the effect of stopping a mathematical process early, such as omitting later terms. Because some sources use “truncation” for digit chopping as well, identify which operation is meant rather than treating the two usages as identical. A further mechanism is the amplification of small input discrepancies as they pass through arithmetic operations; this is propagation of error.

The intuition that governs the whole lecture is that the *size* of an error is not by itself a reliable measure of the *quality* of an approximation. An absolute discrepancy of $0.1$ is catastrophic when the true value is $1$, but negligible when the true value is $10^{6}$. Accuracy must therefore be judged relative to the magnitude of the quantity being approximated, and this observation motivates the definitions of relative and percentage error and, in turn, the notion of significant figures. The lecture objectives are precisely to define and calculate round-off and truncation errors, to identify measures taken to minimize round-off errors, to define and calculate absolute, relative and percentage errors, and to calculate propagated errors with reference to numerical computations.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Round-off and Truncation Errors

> **Definition (Round-off error).** Round-off error arises because it is impossible to represent all real numbers exactly on a machine with finite memory. It involves dropping out decimal places or significant figures, and may be performed either by chopping or by symmetric rounding.

The two modes of discarding digits are distinct procedures for reducing the number of retained figures. Chopping deletes all digits beyond the retained position and keeps the remaining digits unchanged; it is sometimes called truncation in the specific sense of truncating a decimal representation. Symmetric rounding also discards surplus digits but selects the retained value according to a rounding rule, so that the retained value is nearest to the original number. When discussing the error of a numerical method, “truncation error” may instead refer to the effect of omitting part of a mathematical process. State the context explicitly: a decimal chop is a representation choice, whereas an omitted term or step is a method approximation. Neither description should be substituted for the other without explanation.

The following table records certain real numbers rounded off under different conditions, illustrating the divergence between the two modes.

| Real number | Rounded to 4 sf | Rounded to 4 dp | Chopped to 4 sf |
|:--- |:--- |:--- |:--- |
| $1.3333\ldots$ | $1.333$ | $1.3333$ | $1.333$ |
| $0.03333\ldots$ | $0.03333$ | $0.0333$ | $0.03333$ |
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

The formula is obtained by expanding $f$ in a first-order Taylor series about the measured values and retaining only the linear terms; the partial derivatives measure the sensitivity of the result to each operand. For a sum or difference $y=x_{1}\pm x_{2}$, the absolute error is bounded by the sum of the absolute input errors. For products and quotients, relative errors add only as a **first-order approximation** when the relative input errors are small and the relevant inputs are nonzero. The exact formulas make the scope clear. Write the exact inputs as $x_{1}=x_{1r}(1+\delta_{1})$ and $x_{2}=x_{2r}(1+\delta_{2})$, where $x_{1r},x_{2r}$ are the values used in the computation. Then the product’s relative error, measured against the computed product, is $\delta_{1}+\delta_{2}+\delta_{1}\delta_{2}$; the quotient’s is $(\delta_{1}-\delta_{2})/(1+\delta_{2})$, provided $1+\delta_{2}\ne0$. Dropping the product term and replacing the quotient denominator by $1$ yields the familiar first-order sums of magnitudes. These relations are not exact additive rules for arbitrary errors. Subtraction of nearly equal quantities remains dangerous because the absolute input errors may add while the result shrinks, making the relative error of the difference large.

## 3. Formal Proofs, Derivations, and Methods

> **Result 1 (Rounding bound).** When rounding to $n$ decimal places, the error introduced should be bounded by half a unit in the last retained place, that is, by $\tfrac{1}{2}\times 10^{-n}$.

> **Result 2 (Significant-figure criterion).** If a number is correct to $n$ significant figures, the maximum absolute error is $\lvert x\rvert\cdot 10^{-n}$, where $x$ is the exact quantity. Equivalently, the relative error of such an approximation is at most $10^{-n}$.

> **Result 3 (Additive propagation).** For $y=x_{1}\pm x_{2}$, the absolute error satisfies $\lvert \Delta y\rvert\le\lvert \Delta x_{1}\rvert+\lvert \Delta x_{2}\rvert$, and the relative error satisfies $\lvert \Delta y/y\rvert\le(\lvert \Delta x_{1}\rvert+\lvert \Delta x_{2}\rvert)/\lvert y\rvert$.

> **Result 4 (First-order multiplicative propagation).** For nonzero inputs with small relative errors $\delta_i=\Delta x_i/x_i$, the first-order estimate is $\lvert\Delta(x_1x_2)/(x_1x_2)\rvert\approx|\delta_1|+|\delta_2|$ and likewise for $x_1/x_2$. The exact signed relative errors, when measured against the computed results, are $\delta_1+\delta_2+\delta_1\delta_2$ for a product and $(\delta_1-\delta_2)/(1+\delta_2)$ for a quotient. The first-order estimate omits higher-order terms and the quotient denominator must be nonzero.



## 4. Representative Worked Examples and Solutions

### 4.1 Problem Statement

(a) Define relative error as used in computation.

(b) The table below gives certain real numbers rounded off using different conditions. For the real number $x=0.6666\ldots$, state the value rounded to $4$ significant figures, the value rounded to $4$ decimal places, and the value chopped to $4$ significant figures, and compute the relative error of the chopped value.

### 4.2 Part (a): Definitions

(i) *Relative error.* If $r$ is an approximation to an exact quantity $x$, the relative error is $\lvert x-r\rvert/\lvert x\rvert$, the absolute error scaled by the magnitude of the exact quantity.


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

### 4.1 Addition and subtraction: absolute bounds first

Let exact inputs be $x$ and $y$, and let the values used in a calculation be $\bar{x}$ and $\bar{y}$. Suppose their absolute errors are bounded by $a$ and $b$. For the sum, the triangle inequality gives

$$
\left|(x+y)-(\bar{x}+\bar{y})\right|
\le |x-\bar{x}|+|y-\bar{y}|\le a+b.
$$

The same worst-case absolute bound holds for the difference, because

$$
\left|(x-y)-(\bar{x}-\bar{y})\right|
=\left|(x-\bar{x})-(y-\bar{y})\right|
\le a+b.
$$

The sign between the terms does not permit the user to assume cancellation. The two errors might have opposite signs, but the guaranteed maximum must include the possibility that they reinforce one another.

For example, measurements of $x=8.2\pm0.1$ and $y=8.0\pm0.1$ produce the central difference $0.2$. The absolute error of this difference can be as large as $0.2$. Its relative error with respect to the central difference can therefore approach $100\%$. By contrast, the sum is $16.2$ with the same absolute-error bound $0.2$, which is only about $1.23\%$ of its central magnitude. The operands have the same uncertainty in both operations; the operation changes the scale of the result. This is the numerical reason subtraction of nearly equal values deserves special care.

### 4.2 Product: exact expansion and linear estimate

For the product, write the exact inputs as $x=\bar{x}+\delta x$ and $y=\bar{y}+\delta y$. Expanding gives

$$
xy-\bar{x}\bar{y}
=\bar{x}\,\delta y+\bar{y}\,\delta x+\delta x\,\delta y.
$$

If $|\delta x|\le a$ and $|\delta y|\le b$, a rigorous absolute bound is

$$
|xy-\bar{x}\bar{y}|
\le |\bar{x}|b+|\bar{y}|a+ab.
$$

The first two terms are the total-differential estimate; $ab$ is the product of the errors. When the uncertainties are small compared with the operands, this cross term is usually much smaller, but it does not vanish merely because it is inconvenient.

Take $\bar{x}=4$ with $a=0.02$ and $\bar{y}=3$ with $b=0.01$. The computed product is $12$. The first-order error estimate is

$$
|\bar{x}|b+|\bar{y}|a=4(0.01)+3(0.02)=0.10.
$$

The exact bound adds $ab=0.0002$, giving $0.1002$. Relative to the computed product, these are about $0.8333\%$ and $0.835\%$, respectively. The closeness of the values supports using the first-order estimate here, while the algebra shows precisely what was omitted.

This distinction becomes more visible when uncertainties are large. If a length $a=5\pm1$ is multiplied by $b=18\pm2$, the differential estimate is $28$, while the cross term is $2$. The exact interval has area from $4(16)=64$ to $6(20)=120$, so the deviations from the central value $90$ are $-26$ and $+30$. The exact worst-case bound is $30$, not $28$. Label the differential result as an estimate rather than an exact maximum.

### 4.3 Quotient: denominator conditions matter

For a quotient, the exact difference between the true and computed values is

$$
\frac{x}{y}-\frac{\bar{x}}{\bar{y}}
=\frac{\bar{y}\,\delta x-\bar{x}\,\delta y}
{\bar{y}(\bar{y}+\delta y)}.
$$

The denominator must remain nonzero. If $|\delta y|\le b<|\bar{y}|$, the triangle inequality yields

$$
\left|\frac{x}{y}-\frac{\bar{x}}{\bar{y}}\right|
\le
\frac{|\bar{y}|a+|\bar{x}|b}
{|\bar{y}|(|\bar{y}|-b)}.
$$

For small relative errors, replacing the perturbed denominator by its central value gives the familiar first-order estimate

$$
\frac{|\Delta(x/y)|}{|\bar{x}/\bar{y}|}
\approx \frac{a}{|\bar{x}|}+\frac{b}{|\bar{y}|}.
$$

The approximation is not safe if $b$ is comparable with $|\bar{y}|$. If the allowed denominator interval includes zero, the quotient may be unbounded; no finite relative-error estimate can repair that problem.

As a numerical check, take $\bar{x}=10\pm0.1$ and $\bar{y}=4\pm0.04$. The central quotient is $2.5$. The first-order relative-error estimate is $0.1/10+0.04/4=0.02$, or $2\%$, and the corresponding absolute estimate is $0.05$. The exact quotient interval is

$$
\frac{9.9}{4.04}\le\frac{x}{y}\le\frac{10.1}{3.96},
$$

approximately $[2.4505,2.5505]$. The maximum deviation from $2.5$ is about $0.0505$, close to the linear estimate because both relative input uncertainties are small. Repeating the example with a denominator uncertainty almost as large as its central value would make the interval much wider and the linear estimate unreliable.

### 4.4 Combining propagated and generated errors

Propagation describes the effect of uncertainty already in the inputs. A calculation can also generate a fresh representation error when an intermediate or final result is rounded. Keep these sources separate before combining them. For example, suppose an input measurement is rounded to two decimal places, used in a product, and the product is then rounded to one decimal place. The input contributes a bound from the first rounding; the product formula propagates that bound; the last rounding adds a new half-unit bound of $0.05$ in the result’s units.

A conservative absolute bound adds the separately justified contributions. It is conservative because their signs are not known. If a first-order propagation formula was used, describe the result as an estimate plus the final rounding allowance rather than calling the combined figure a strict exact bound. If a strict bound is needed, use input intervals, evaluate extrema where possible, and then include the last rounding interval.

Consider a simple sequence: a length is reported as $6.20\pm0.005$ m and is multiplied by a speed $v=3.0\pm0.1$ m/s to form a distance-like product. The central result is $18.6$. A first-order estimate of its uncertainty is $|v|\Delta x+|x|\Delta v=3(0.005)+6.20(0.1)=0.635$. The cross term is $0.0005$, and rounding $18.6$ to one decimal place introduces at most another $0.05$. Keeping the stages visible explains why the uncertainty is dominated by the speed, not by the last digit of the length.

### 4.5 Sensitivity and the general formula

For a differentiable function $z=f(x_1,\ldots,x_n)$, the partial derivative with respect to $x_i$ measures the local change in $z$ caused by changing $x_i$ while holding the other inputs fixed. The first-order formula combines these individual effects:

$$
\Delta z\approx\sum_i\frac{\partial f}{\partial x_i}\Delta x_i,
\qquad
|\Delta z|\lesssim\sum_i\left|\frac{\partial f}{\partial x_i}\right|\,|\Delta x_i|.
$$

The absolute values prevent accidental cancellation when an upper bound is required. The symbol $\lesssim$ or the word “estimate” is appropriate for the linearized expression unless a theorem supplies a remainder bound.

For $z=x^2+y$, a small uncertainty in $x$ contributes approximately $2|x|\Delta x$, while uncertainty in $y$ contributes $\Delta y$. If $x=3\pm0.02$ and $y=1.5\pm0.01$, the central value is $10.5$, and the first-order error estimate is $2(3)(0.02)+0.01=0.13$. The exact change from perturbations includes $(\Delta x)^2$ in addition to the linear term. Its maximum contribution is only $0.0004$, so the differential estimate is excellent at this scale. The example also shows why the same absolute uncertainty in $x$ matters more when $|x|$ is larger: the derivative $2x$ grows with the operating point.

### 4.6 A practical decision procedure

When a computation contains several operations, first write the mathematical expression and mark which values are exact, rounded, or measured with a stated tolerance. Convert each stated decimal precision into an absolute interval. Then choose a propagation tool matching the operation: triangle inequalities for sums and differences, an exact expansion or a first-order estimate for products, a denominator check for quotients, and partial derivatives for a general smooth formula.

After calculating, compare the error bound with the magnitude of the result. A small absolute bound paired with a very small result can still represent poor relative accuracy. Keep intermediate digits until the end, but do not claim that those guard digits reflect the precision of the original data. Finally, state whether the answer is a rigorous interval bound, an upper bound from worst-case input errors, or a first-order sensitivity estimate. These labels communicate what the mathematics actually guarantees.

### 4.7 Range analysis for a quotient of uncertain inputs

Let

$$
q=\frac{a+b}{c},\qquad
a=1.2\pm0.05,\quad b=2.3\pm0.05,\quad c=0.8\pm0.02.
$$

The central calculation is $q=3.5/0.8=4.375$. Since all allowed values of $c$ are positive, the quotient increases when the numerator increases and decreases when the denominator increases. The numerator interval is $[3.4,3.6]$ and the denominator interval is $[0.78,0.82]$, so

$$
\frac{3.4}{0.82}\le q\le\frac{3.6}{0.78},
$$

approximately $[4.1463,4.6154]$. The largest deviation from the central value is about $0.2404$. The width is not symmetric around $4.375$, because a quotient is nonlinear and its denominator changes.

A first-order estimate provides a useful comparison. The partial derivatives are $1/c$ with respect to each of $a,b$, and $-(a+b)/c^2$ with respect to $c$. At the central values, the absolute sensitivity estimate is

$$
\frac{0.05}{0.8}+\frac{0.05}{0.8}
+\frac{3.5(0.02)}{0.8^2}
=0.234375.
$$

Dividing by $q=4.375$ gives a relative estimate of about $5.36\%$. The estimate is close to the exact interval width but not identical. The interval method is the stronger guarantee when the input bounds are exact; the derivative calculation explains which input dominates the local uncertainty.

If the possible values of $c$ had included zero, the endpoint rule would not produce a finite interval. The quotient could become arbitrarily large in magnitude near a zero denominator. This is why a denominator condition is part of the mathematical conclusion, not merely a computational convenience.

### 4.8 Accumulation through repeated multiplication

Repeated products show why small relative errors can accumulate. Suppose a computed quantity is multiplied successively by factors with relative errors $\delta_1,\delta_2,\ldots,\delta_m$. If each exact factor is the computed factor times $1+\delta_i$, the total relative factor is

$$
\prod_{i=1}^{m}(1+\delta_i).
$$

For small errors, expanding the product gives approximately $1+\sum_i\delta_i$, because products of two or more small errors are higher order. A worst-case first-order estimate therefore sums their magnitudes. This is a useful diagnostic, not an exact statement that the total relative error equals the sum for arbitrary errors.

For instance, three successive factors each carrying a relative error of at most $0.001$ have a first-order total bound near $0.003$. The exact worst-direction product is $(1.001)^3-1\approx0.003003001$, slightly larger. If instead the errors have known signs and partially cancel, the actual outcome may be smaller; a guaranteed maximum should not rely on that cancellation.

This example distinguishes propagated and accumulated error. The input errors are propagated through each multiplication, while the error in the final computed result may also include new rounding at each operation. In a long calculation, a reliable method controls both the size of intermediate errors and how sensitive later steps are to them.

### 4.9 Sensitivity, scaling, and cancellation

The partial derivative in the general propagation formula is a local sensitivity coefficient. For $z=x^2$, the derivative is $2x$, so the same absolute error in $x$ produces a larger absolute output change when $|x|$ is large. For $z=\sqrt{x}$, the derivative $1/(2\sqrt{x})$ grows as $x$ approaches zero, showing that small input changes can have a large effect near the boundary.

Sensitivity has units: $\partial z/\partial x$ has units of $z$ divided by units of $x$. Multiplying it by an input error returns a contribution in the units of $z$, making it possible to add terms in a propagated absolute-error estimate. A dimensionless relative sensitivity is often easier to compare across scales, but it requires nonzero inputs and outputs.

Cancellation deserves a separate check. For $z=x-y$, the first-order absolute bound is $\Delta x+\Delta y$. Dividing that by $|x-y|$ can make the relative bound enormous if $x$ and $y$ are close. This is a property of the problem’s sensitivity at those values, not necessarily a failure of the arithmetic device. If the problem permits an equivalent stable formula, it may reduce avoidable round-off; it cannot restore information absent from the measurements.

### 4.10 Designing an error budget

An error budget is a concise table or list of sources, their estimated contributions, and the assumptions used. For a multi-stage result, separate input measurement uncertainty, approximation or truncation, arithmetic round-off, and any final reporting round. Convert contributions into common output units before comparing them. Do not combine a relative percentage directly with an absolute error until both are expressed in a compatible form.

Suppose the first-order estimate from a measured speed contributes $0.6$ units of error, while a geometric length contributes $0.02$ units. The first contribution dominates this particular result, so improving the length measurement alone will have little effect. If a final rounding contributes $0.05$, it is also smaller than the speed uncertainty. Such prioritization helps allocate effort: refining an algorithm is valuable only if its error is large enough to matter relative to the data and other stages.

When no probability model is given, worst-case bounds add magnitudes because errors may align in the least favorable direction. A root-sum-square combination assumes additional statistical information, such as independent zero-mean errors. Do not use it as a guaranteed bound or infer independence from the fact that measurements were taken separately.

### 4.11 Selecting the appropriate mathematical statement

Use an exact algebraic expansion when finite input errors are not small or when a cross term is easy to retain. Use the differential formula to estimate local sensitivity when perturbations are small. Use interval arithmetic when the problem gives explicit ranges and a rigorous output enclosure is needed. Use relative error when the reference quantity is nonzero and the scale of the quantity matters.

Each method answers a different question. A first-order estimate is concise and often accurate for small perturbations. An exact bound may be more conservative but certifies a range. A relative error communicates scale but can be undefined or misleading near zero. In a complete answer, name the method, state its conditions, and avoid presenting one kind of result as another.

### 4.12 Propagating uncertainty through a power

Let $z=x^m$ for a positive integer $m$ and write $x=\bar{x}+\delta x$. The first-order change is $m\bar{x}^{m-1}\delta x$. Dividing by the computed value $\bar{x}^m$ gives a relative estimate of $m\,\delta x/\bar{x}$, provided $\bar{x}\ne0$ and the relative perturbation is small. This explains the useful rule that a small relative input error can be magnified by the exponent.

For example, if $x=2.00\pm0.01$ and $z=x^3$, the central value is $8$. The first-order absolute estimate is $3(2^2)(0.01)=0.12$, corresponding to $1.5\%$. The exact endpoints are $1.99^3\approx7.8806$ and $2.01^3\approx8.1206$, so the exact deviations are about $0.1194$ and $0.1206$. The higher-order terms are small at this precision, and the interval confirms the estimate.

If $x$ is close to zero, relative-error rules involving division by $x$ are inappropriate. Use an absolute expansion or interval endpoints instead. As with the quotient, the condition on the reference value is part of the reasoning.

### 4.13 Combining a measured difference with a ratio

Consider $r=(a-b)/c$ with measured values $a=50.02\pm0.01$, $b=50.00\pm0.01$, and $c=2.0\pm0.02$. The central numerator is only $0.02$, so the numerator’s absolute uncertainty can be $0.02$, equal to its central value. The central ratio is $0.01$, but a first-order relative-error formula around this point would be unstable because the numerator is close to zero.

The interval method makes the issue obvious: $a-b$ can range from zero to $0.04$, while $c$ ranges from $1.98$ to $2.02$. The ratio can be zero and can reach approximately $0.04/1.98\approx0.0202$. Reporting only the central value $0.01$ hides a possible factor-of-two variation. This is a more informative error analysis than blindly applying a product of relative-error estimates.

The lesson is to examine intermediate quantities before applying a relative-error shortcut. A well-scaled denominator does not rescue a numerator formed by near cancellation. First bound each intermediate interval, then propagate the resulting range through the next operation.

### 4.14 Error budgets for successive stages

An error budget can be updated step by step. For each intermediate quantity, record its central value, absolute uncertainty, and source. When two values are added or subtracted, combine their absolute bounds. When they are multiplied or divided, either use interval endpoints or state the first-order assumptions. If the calculator rounds the intermediate result, add that new contribution in the output’s units.

For example, in a chain $u=a+b$, $v=uc$, the uncertainty in $u$ is established before it is used in the product. It should not be counted once as a new independent measurement and again as the same original uncertainties. Carry the bound forward; do not duplicate it. A clear ledger prevents both undercounting and double counting.

The resulting total may be conservative because all worst-case signs are assumed to align. That is acceptable when the question asks for a maximum bound. If a problem asks for an expected or standard deviation, it requires a statistical model. Use the model that matches the wording, not the one that produces the smallest answer.

### 4.15 A worst-case relative bound for a product

Let $\rho_x=a/|\bar{x}|$ and $\rho_y=b/|\bar{y}|$ be relative input-error bounds for nonzero central inputs. From the exact product expansion, the relative error measured against the computed product is bounded by

$$
\frac{|xy-\bar{x}\bar{y}|}{|\bar{x}\bar{y}|}
\le \rho_x+\rho_y+\rho_x\rho_y.
$$

If both relative errors are below one percent, their product term is below $0.0001$, or $0.01$ percentage points. In that case the first-order sum is a useful approximation. If they are not small, report the exact bound or compute a range instead of treating relative errors as exactly additive.

For a quotient, the exact relative-error bound additionally contains a denominator factor. If $\rho_y<1$, then

$$
\frac{\left|x/y-\bar{x}/\bar{y}\right|}{|\bar{x}/\bar{y}|}
\le \frac{\rho_x+\rho_y}{1-\rho_y}.
$$

As $\rho_y$ approaches one, this bound grows without limit. That behavior reflects the fact that the possible denominator approaches zero. The first-order expression $\rho_x+\rho_y$ is reasonable only when $\rho_y$ is small enough that the denominator factor is close to one.

### 4.16 Propagation through a sum followed by a product

Let $z=(x+y)w$, with central inputs $\bar{x},\bar{y},\bar{w}$ and absolute input bounds $a,b,c$. The central sum is $\bar{s}=\bar{x}+\bar{y}$, with absolute error at most $a+b$. The first-order product estimate for $z$ is

$$
|\Delta z|\approx |\bar{w}|(a+b)+|\bar{s}|c.
$$

This can be checked directly by expanding

$$
z-\bar{z}=\bar{w}(\delta x+\delta y)+\bar{s}\delta w
+(\delta x+\delta y)\delta w.
$$

The exact bound includes the final cross term $(a+b)c$. Writing the expression before differentiating helps prevent a common mistake: the uncertainty of the intermediate sum must be propagated through the multiplication, not added directly to the product error in incompatible units.

If $x$ and $y$ nearly cancel, the absolute bound for their sum may be small relative to the operands but large relative to the result. The subsequent multiplication by $w$ changes the absolute scale but does not restore lost relative accuracy. Examine both intermediate and final magnitudes when deciding how many digits to report.

### 4.17 Choosing an estimate for the scale of the problem

Use the first-order formula when all perturbations are small enough that the omitted higher-order terms are negligible for the requested accuracy. Use the exact algebraic expansion when the expression is simple and the perturbations may not be small. Use interval endpoints when finite ranges and monotonicity determine clear extrema. The choice should reflect the size of the uncertainty and the consequence of an inaccurate bound.

If the problem only asks for a propagated error “to first order,” the differential formula is the intended tool. If it asks for a guaranteed maximum error, a first-order estimate alone may be insufficient unless a remainder bound is provided. If it asks for an approximate percentage accuracy, a relative-error estimate is appropriate when the reference is nonzero and the input perturbations are small.

State the convention before presenting the final number. This gives the reader enough information to interpret whether a reported result is a local estimate, an exact finite-error upper bound, or a range. Numerical analysis is as much about stating what a calculation guarantees as it is about carrying out its arithmetic.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 High-Yield Takeaways

- The error is defined as true value minus approximate value; the absolute error is its magnitude, the relative error divides that magnitude by the magnitude of the exact quantity, and the percentage error multiplies the relative error by one hundred.
- Round-off error originates in the finite representation of real numbers and is realized either by chopping or by symmetric rounding; truncation error originates in replacing an exact infinite process by a finite one; chopping is a digit-discarding rule, not this approximation error.
- Rounding to $n$ decimal places introduces an error bounded by half a unit in the last retained place, that is, by $\tfrac{1}{2}\times 10^{-n}$.
- If a number is correct to $n$ significant figures, the maximum absolute error is $\lvert x\rvert\cdot 10^{-n}$, where $x$ is the exact quantity; equivalently the relative error is at most $10^{-n}$.
- The general propagated-error formula is the first-order Taylor expansion $\Delta y\approx\sum_{i}\frac{\partial f}{\partial x_{i}}\Delta x_{i}$, with the maximum bound obtained by replacing each term by its absolute value.
- Absolute errors add under addition and subtraction. For products and quotients, addition of relative-error magnitudes is a small-error, first-order estimate; it is not an exact identity for arbitrary input errors.
- Relative error, not absolute error, is the correct measure of accuracy, because it accounts for the size of the quantity being approximated.
- Diagnose cancellation when subtracting nearly equal quantities, since it can reduce the number of reliable significant digits; use the stated arithmetic rules and avoid unsupported repair methods.

### 5.2 Common Pitfalls

### 5.3 A complete first-order error budget for a measured area

Let a rectangle have exact dimensions \(L\) and \(W\), while the recorded dimensions are \(L_r\) and \(W_r\). Write \(L=L_r+\varepsilon_L\) and \(W=W_r+\varepsilon_W\). Subtracting the computed product from the exact product gives

$$
LW-L_rW_r=L_r\varepsilon_W+W_r\varepsilon_L+\varepsilon_L\varepsilon_W.
$$

This identity is more informative than a slogan that “product relative errors add.” It separates the two first-order input effects from the cross-term, which is second order when both input errors are small. If the measured dimensions are \(L_r=12.4\) cm and \(W_r=5.8\) cm, each correct to the nearest \(0.1\) cm, then \(|\varepsilon_L|,|\varepsilon_W|\le 0.05\) cm. Consequently,

$$
|LW-L_rW_r|\le 12.4(0.05)+5.8(0.05)+(0.05)^2
=0.9125\text{ cm}^2.
$$

The computed area is \(71.92\text{ cm}^2\); the bound says that, under the stated measurement model, the true area is within \(0.9125\text{ cm}^2\) of it. It is not a prediction that the error is exactly the bound. If the input errors have opposite signs, some of the first-order contributions may cancel, but a guaranteed worst-case bound does not assume cancellation.

Dividing the first-order part by \(L_rW_r\) yields the familiar relative-error estimate

$$
\frac{|\Delta A|}{|A_r|}
\lesssim \frac{|\varepsilon_L|}{|L_r|}
+\frac{|\varepsilon_W|}{|W_r|}.
$$

For these measurements the right side is approximately \(0.05/12.4+0.05/5.8\), or about \(0.01267\), which is roughly \(1.27\%\). The exact relative error uses the unknown exact area in its denominator; this computed percentage is an approximate bound based on the recorded values. Explicitly stating that convention avoids treating a differential estimate as an exact identity.

### 5.4 Combining stages without losing the source of uncertainty

Suppose a later calculation uses the rectangle’s perimeter and area together. The perimeter is \(P=2(L+W)\), so its first-order absolute error is bounded by \(2(|\varepsilon_L|+|\varepsilon_W|)\). With the same measurements this is at most \(0.2\) cm. The area and perimeter bounds have different units and must not be added directly. If a final quantity combines them, first write that quantity as a function of \(L\) and \(W\), then differentiate that function or propagate each intermediate bound with consistent units.

For example, if \(Q=A/P\), then near the recorded values the relative sensitivity of the quotient depends on both the area and perimeter errors. A compact differential statement is

$$
\Delta Q\approx \frac{\Delta A}{P_r}
-\frac{A_r}{P_r^2}\Delta P.
$$

This expression exposes two possible contributions and their signs. For a worst-case estimate, take magnitudes and add the bounds; do not rely on the signs cancelling. If \(P_r\) is near zero, the denominator makes the quotient highly sensitive and the linear estimate itself must be treated cautiously. Here the perimeter is positive and far from zero, so that particular difficulty does not arise.

An error budget is easiest to audit when it is written in layers: measurement uncertainty, propagation through each formula, arithmetic round-off, and any truncation introduced by a numerical method. These are not interchangeable labels. A more accurate calculator setting can reduce round-off but cannot recover digits absent from the measurements. More terms in an approximation can reduce truncation but may add arithmetic operations. A useful final sentence therefore states which contribution controls the reported precision and whether the result is an exact bound or a first-order estimate.

- Reporting an absolute error as though it measured accuracy, without reference to the magnitude of the quantity; the same relative error can accompany wildly different absolute errors.
- Confusing chopping with symmetric rounding, or confusing decimal truncation with truncation error in a finite method: state which use is intended before comparing errors.
- Applying the significant-figure criterion with the wrong exponent, using $5\times 10^{-n}$ where $\lvert x\rvert\cdot 10^{-n}$ is required, or scaling by the approximate rather than the exact magnitude.
- Forgetting to round every intermediate result when the question specifies $k$-digit rounding arithmetic; the instruction applies at each operation, not only at the end.
- Subtracting nearly equal quantities without recognizing the resulting loss of significant digits, and failing to recognize that cancellation can reduce the number of reliable significant digits.
