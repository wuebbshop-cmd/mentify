## 1. Foundational Concepts, Definitions, and Axioms

Numerical analysis develops ways to calculate useful answers from numerical data. The data may come from a measuring device, and a computer can store only a finite number of digits. For both reasons, a computed value is usually an approximation to the true value.

Imagine measuring a table that is actually 1.237 m long with a ruler marked in centimetres. You may record 1.24 m. The recorded value is convenient, but it is not the exact length. The difference between the true value and the recorded value is the error. Error does not always mean someone made a careless mistake; it can be an unavoidable part of measurement and computation. The goal is to understand its size and keep it within an acceptable limit.

Three related ideas should stay separate:

- The exact value is the value we would know with perfect data and exact arithmetic.
- The approximation is the value available to us.
- The error describes the difference between them.

## 2. Theorems, Lemmas, and Analytical Properties

### Round-off and truncation

A computer cannot keep every digit of every real number. If it stores only a limited number of digits, it must shorten a value. This creates round-off error.

There are two common ways to shorten a decimal:

- **Chopping**: discard the digits after the last kept digit.
- **Rounding**: inspect the next digit and adjust the last kept digit when needed.

For example, to keep four significant digits in 1.3339, chopping gives 1.333 while rounding gives 1.334. Both are approximations, but rounding is generally closer to the original number. A cut-off can also arise in a mathematical method: if an infinite series is stopped after a finite number of terms, the omitted part creates truncation error. Round-off comes from finite representation; truncation comes from stopping an exact mathematical process early.

### Absolute, relative, and percentage error

Let $x$ be the exact value and $x_r$ the recorded or computed approximation. Absolute error is the size of their difference:



$$
E_{abs}=|x-x_r|.
$$



If the exact value is 12.50 kg and the approximation is 12.47 kg, the absolute error is 0.03 kg. The units are the same as the quantity.

Relative error compares the error with the size of the exact value:



$$
E_{rel}=\frac{|x-x_r|}{|x|},\qquad x\ne 0.
$$



Percentage error is the relative error written as a percentage:



$$
E_{pct}=100E_{rel}\%.
$$



The relative measure helps compare errors on different scales. An error of 0.03 is small for a 12.50 kg object but large for a quantity whose true value is 0.04 kg. If the exact value is zero, relative error cannot be calculated because its denominator would be zero; report absolute error instead.

### Accuracy to decimal places and significant figures

Correct to $n$ decimal places refers to digits after the decimal point. Correct to $n$ significant figures refers to the first $n$ meaningful digits, starting at the first nonzero digit. For example, 0.004568 rounded to two significant figures is 0.0046, while rounded to three decimal places it is 0.005. These are different instructions and produce different approximations.

When rounding to the nearest unit in the last decimal place, the maximum absolute rounding error is half of that unit. Thus, rounding to $n$ decimal places gives



$$
E_{abs}\le \frac{1}{2}10^{-n}.
$$



For example, a value recorded as 2.4 to one decimal place lies within 0.05 of 2.4 under the usual nearest-rounding rule. That gives the interval $2.35\le x<2.45$. This interval is useful when a question asks for upper and lower bounds rather than only the rounded value.

## 3. Formal Proofs, Derivations, and Methods

### Input error

Measurements and supplied data may already be approximate. If a length is measured only to the nearest centimetre, later calculations cannot recover the unrecorded millimetres. A careful calculation should not report more certainty than the input supports.

### Round-off error

Finite-digit arithmetic introduces round-off at each stored value and operation. Chopping and rounding can produce different answers, especially after many operations. To reduce avoidable round-off:

- keep guard digits in intermediate steps;
- delay rounding until the final answer;
- use a stable order of calculation when alternatives are available;
- do not treat calculator output as exact merely because many digits are displayed.

Subtraction of nearly equal numbers deserves special care. For example, subtracting two values close to 10 may leave a small result. Errors that were small compared with 10 can then be large compared with that small difference. Division by a very small approximate value can also magnify an absolute error.

### Truncation error

Truncation error is introduced when a formula or process is stopped early. If a method uses only the first few terms of an expansion, the omitted terms contribute error. Unlike round-off, this error can often be reduced by taking more terms or choosing a more accurate approximation, though doing so may increase the amount of computation.

## 4. Representative Worked Examples and Solutions

Suppose the exact inputs are $x$ and $y$, while the values used in a calculation are $x_r$ and $y_r$. Write their input errors as



$$
x=x_r+\varepsilon,\qquad y=y_r+\nu,
$$



where $\varepsilon$ and $\nu$ may be positive or negative. The error in the output caused by these input errors is called **propagated error**. New rounding introduced while carrying out the operation is **generated error**. The total accumulated error at a step includes both propagated error and generated error.

For addition or subtraction, the worst-case absolute error is bounded by the sum of the input error bounds:



$$
|\Delta(x\pm y)|\le |\varepsilon|+|\nu|.
$$



This is a worst-case bound because the two errors could act in the same direction. If they happen to cancel, the actual error may be smaller, but we cannot rely on cancellation when guaranteeing accuracy.

For multiplication, expand the exact product:



$$
xy=(x_r+\varepsilon)(y_r+\nu)
=x_ry_r+x_r\nu+y_r\varepsilon+\varepsilon\nu.
$$



Therefore the product error contains two first-order terms and a smaller product of the input errors. When the input errors are small, a useful first-order bound is



$$
|\Delta(xy)|\approx |x_r|\,|\nu|+|y_r|\,|\varepsilon|.
$$



For division, provided the denominator is not zero or close to zero, the first-order relative-error estimate is



$$
\frac{|\Delta(x/y)|}{|x_r/y_r|}
\approx \frac{|\varepsilon|}{|x_r|}+\frac{|\nu|}{|y_r|}.
$$



The denominator condition matters: if $y_r$ is tiny, even a small error in $y$ can have a large effect on the quotient. Products and quotients are often easier to estimate with relative errors, while sums and differences are usually estimated with absolute errors.

### 4.1 Reading a quoted measurement as an interval

A quoted decimal is not automatically an exact value. If a length is reported as $2.4$ m to the nearest tenth of a metre, the last digit represents a rounding decision. The unknown true measurement is no more than half of one tenth away from the displayed value. This turns the report into an interval rather than a single point.

The endpoints are found by subtracting and adding the half-step:

$$
2.35\ \text{m}\le L<2.45\ \text{m}.
$$

The upper endpoint is usually written as open for a specified nearest-value convention because a tie at $2.45$ would normally round to the next reported tenth, depending on the stated tie rule. In a basic error-bound answer, the central message is the half-width $0.05$ m. It is not correct to say that the measurement is exact merely because the display contains one decimal digit. If the task gives no tie convention and asks only for a maximum error, state the half-unit bound rather than arguing over endpoint inclusion.

Now compare this with a value rounded to two decimal places. The step size is one hundredth, so the half-step is half of that:

$$
E_{\text{abs}}\le 0.005.
$$

The phrase “two decimal places” concerns the location of the decimal point. It does not say how large the number is. For $0.03$, an error of $0.005$ is a substantial fraction of the value; for $3000.03$, the same absolute error is negligible. The written precision and the scale of the quantity must therefore both be examined before judging whether a result is useful.

If several rounded observations are used to calculate a total, preserve their uncertainty until the final operation. Suppose three lengths are each reported to the nearest centimetre. Each has a maximum error of $0.5$ cm. Adding the three displayed lengths gives a central total, but in the worst case all three individual errors point in the same direction. The total’s absolute error bound is therefore $1.5$ cm. It is not automatically $0.5$ cm just because the total is reported once. If some errors happen to cancel, the actual error may be lower; a guaranteed bound cannot assume that lucky cancellation.

### 4.2 Choosing the right error measure

Consider two measurements that both miss their true values by $0.2$ units. The first true value is $1$, and the second is $1000$. Both have absolute error $0.2$, but the first approximation is much less accurate in context. Their relative errors express this difference:

$$
\frac{0.2}{1}=0.2=20\%,\qquad \frac{0.2}{1000}=0.0002=0.02\%.
$$

The unit of absolute error remains the unit of the measurement. Relative error is a ratio, so the units cancel. A reported “relative error of $0.2$” is a fraction; converting it to a percentage gives $20\%$. A frequent presentation mistake is to write $0.2\%$ when the calculation actually produced $0.2$ as a fraction. The extra multiplication by one hundred is required only when the question requests percentage error.

For a quantity whose exact value is zero, relative error is not defined because it would require division by zero. That does not make the approximation error unknowable: the absolute difference can still be computed. If the exact quantity is close to zero rather than exactly zero, the relative error may become very large. In that case, report both measures and explain that the large relative error is a consequence of the small reference scale, not necessarily a large absolute discrepancy.

An accuracy comparison should therefore name the reference value. If a calculator shows an approximation to an exact quantity, the usual relative error divides by the magnitude of the exact quantity. If the exact value is not available but only a central measured value and a tolerance are known, call the result an estimated or bounded relative error and specify the reference used. Do not silently switch between the true value and the rounded observation.

### 4.3 A complete comparison of chopping and rounding

Take the recurring decimal $0.6666\ldots$ and retain four significant figures. Chopping keeps the first four significant digits and discards the rest. Symmetric rounding also looks at the next digit. Since that next digit is $6$, the last retained digit increases by one.

$$
0.6666\ldots\longrightarrow
\begin{cases}
0.6666,&\text{by chopping},\\
0.6667,&\text{by rounding}.
\end{cases}
$$

The exact value is larger than both displayed values, but rounding is closer in this case. If the target instead is $1.3333\ldots$ to four significant figures, the fourth significant digit is already $3$ and the next digit is $3$, so rounding does not increase it. Both chopping and rounding give $1.333$. A difference between the methods appears only when the discarded tail changes the rounding decision.

Significant figures and decimal places can also give different answers for the same number. For $0.004568$, the first nonzero digit is in the thousandths place. Three significant figures retain $4,5,6$ and inspect the next digit $8$; the rounded value is $0.00457$. Three decimal places instead retain only digits through the thousandths place and round to $0.005$. The first instruction controls the number of meaningful digits; the second controls the number of digits after the decimal point.

After applying a rounding instruction, do not report more digits as though they were newly accurate. Rounding $0.004568$ to three significant figures does not justify writing $0.004570000$ as a measured result. Extra trailing digits might be useful internally for a later calculation, but they do not increase the precision of the supplied value. Keep guard digits while computing and round the final answer to a precision supported by the data.

### 4.4 Propagation in a two-stage calculation

Suppose a rectangular sheet has a measured width $w=12.0\pm0.1$ cm and a measured height $h=8.0\pm0.1$ cm. The central area estimate is $96.0\ \text{cm}^2$. The uncertainty in the inputs does not simply remain $0.1$ after multiplication because width and height influence the area at different rates.

For small input errors, the area change is estimated by changing one side at a time: an additional $0.1$ cm in width changes area by about $8.0(0.1)=0.8\ \text{cm}^2$; an additional $0.1$ cm in height changes it by about $12.0(0.1)=1.2\ \text{cm}^2$. Adding the possible magnitudes gives a first-order area uncertainty near $2.0\ \text{cm}^2$.

This estimate has a clear interpretation. A centimetre of width matters in proportion to the height, while a centimetre of height matters in proportion to the width. The calculation does not claim that the actual error must equal two square centimetres; it is a worst-direction first-order estimate. If the errors are not small, the exact corner values of the allowed width-height rectangle give a safer range. Here the exact dimensions lie in $[11.9,12.1]$ and $[7.9,8.1]$, so the area lies between $94.01$ and $98.01\ \text{cm}^2$.

The example also illustrates the difference between inherited and generated uncertainty. The width and height were already uncertain before multiplication; these are input or inherent errors. The product calculation carries those uncertainties into the area. If the calculator then rounds $96.0$ or intermediate values, that creates an additional numerical representation effect. To keep the accounting clear, record the input tolerance first, calculate the propagated contribution, then mention any extra rounding only if it is material.

### 4.5 Error accumulation without false precision

Suppose an estimate is produced in three stages: a measurement is rounded, two approximate values are subtracted, and the difference is divided by another measured value. The final result is affected by every stage. A useful habit is to keep an “error ledger” in words: what uncertainty entered from the data, what arithmetic operation acted on it, and whether a further rounding occurred.

For subtraction, the largest absolute discrepancy in the result can be as large as the sum of the two input discrepancies. If the central values are $20.04$ and $20.00$, their displayed difference is only $0.04$. If each original value could be wrong by $0.02$, the worst-case difference error is $0.04$, the same size as the result. The relative error can then be near $100\%$. The small-looking subtraction result should not be given many confident digits.

For division, ask how close the denominator might get to zero. A denominator whose central value is $0.2$ and uncertainty is $0.1$ remains positive, but its relative uncertainty is large. If the denominator’s range reaches zero, a finite quotient bound may not exist at all. The correct response is not to apply a routine small-error formula outside its conditions; it is to examine the allowed interval and explain why the quotient is unstable or unbounded.

When a sequence of calculations is involved, do not add relative errors indiscriminately. Absolute error bounds are natural for addition and subtraction. Relative error is often easier for multiplication and division, provided the values are nonzero and relative errors are small. A nonlinear formula may be handled by sensitivity to each input. A careful solution states which estimate is being used and whether it is first order or a rigorous interval bound.

### 4.6 Self-check questions for an error calculation

Before accepting a numerical answer, ask what the problem calls exact and what value is actually used in the arithmetic. Then check that the numerator of an absolute-error expression is a difference, that absolute error is nonnegative, and that relative error uses the magnitude of the exact reference quantity. Confirm that a percentage includes the factor of one hundred.

For a rounding question, identify the requested place or significant digit before inspecting the next digit. For a table of values, check the headings carefully: a number can have four significant figures but a different number of decimal places. For an interval question, write both endpoints and confirm that the lower endpoint is smaller. For propagation, note the operation and the scale of the result. Addition and subtraction can suffer cancellation, multiplication carries cross effects, and division requires a denominator bounded away from zero.

The last check is about interpretation. Does the number of digits shown agree with the uncertainty? Are the units preserved in an absolute error and cancelled in a relative error? Is a claimed maximum a true interval bound or only a local first-order estimate? A technically correct calculation can still be misleading if the answer labels an estimate as exact or presents a central value with unsupported precision.

### 4.7 A rate computed from two rounded quantities

Suppose a runner’s time is recorded as $12.4$ seconds to the nearest tenth and the distance is recorded as $100$ m to the nearest metre. The central speed is $100/12.4\approx8.0645$ m/s. But the time lies within a half-tenth of its displayed value and the distance lies within a half-metre, so the speed is not an exact decimal. The fastest possible speed comes from the largest allowed distance and shortest allowed time; the slowest comes from the smallest distance and longest time:

$$
\frac{99.5}{12.45}\le v\le\frac{100.5}{12.35}.
$$

Numerically, this is about $7.992$ to $8.138$ m/s. The interval communicates more than the central value alone: it shows which digits are supported by the measurement precision. Writing $8.064516129$ m/s without an uncertainty statement would suggest a level of accuracy the input data do not provide.

The denominator check matters here. The time interval is positive and far from zero, so both endpoints produce finite speeds. If an unknown denominator could equal zero, this endpoint procedure would not yield a finite upper limit. Always check the sign and range before dividing intervals.

### 4.8 Why unit checks help error analysis

If a distance is in metres and time in seconds, a quotient of distance by time has units metres per second. The absolute error in that quotient has the same units; its relative error is dimensionless. This simple check can expose a formula error: adding a time error directly to a distance error is not meaningful, while comparing each fractional error after forming a product or quotient is dimensionally consistent.

For example, consider the perimeter of a rectangle with side lengths $a$ and $b$. If each side carries a length uncertainty, then the perimeter $2a+2b$ has a length uncertainty. The coefficient two matters: increasing $a$ by a small amount changes the perimeter twice as much as that amount because both parallel sides contribute. A derivative or a careful expansion captures that multiplicity; copying the uncertainty unchanged would not.

Units also help interpret percentage error. A result such as $0.03$ metres is an absolute error; $0.03$ as a relative error is a ratio and corresponds to $3\%$. State units next to absolute quantities and a percent sign next to percentage error, rather than relying on the reader to infer which convention was used.

### 4.9 Accuracy statements and significant digits

Suppose two estimates are $0.00072$ and $7200$, and each has a relative error of $0.01$. The corresponding absolute errors are $0.0000072$ and $72$. These values differ by ten million, yet the estimates have the same relative accuracy. Conversely, if two measurements share the same absolute tolerance, the one closer to zero has the larger relative uncertainty.

Significant figures summarize relative scale. When a value is stated to a certain number of significant figures, the first nonzero digit determines the starting point; leading zeros locate the decimal point but do not count as significant digits. Trailing zeros may be significant if the notation says so, which is why scientific notation can be helpful. For instance, writing $4.20\times10^3$ communicates three significant figures, while a bare $4200$ can be ambiguous without context.

An accuracy claim should not exceed the evidence. A value calculated from a rounded input can retain guard digits internally, but the final display should reflect the requested precision and error bound. If a method produces more digits than the input precision supports, explain whether those digits are computational intermediates or justified output digits.

### 4.10 Comparing error types in one computation

Imagine calculating the average of repeated measurements. The original measurements may differ from the true quantity because the instrument has limited resolution; this uncertainty is inherent in the data. A computer may store each number using finite digits, causing round-off. If a formula is evaluated only approximately or a series is cut off, the method contributes its own truncation error. Arithmetic then transmits these contributions into the final result.

These are not competing names for the same event. They describe where the discrepancy enters. An error budget can list the source and stage: “input tolerance,” “finite-digit representation,” “method approximation,” and “propagation through the formula.” Sometimes the course or textbook uses “truncation” for discarding decimal digits as well as for stopping a method. In that case, identify whether the context is representation or an omitted mathematical step.

The distinction guides a remedy. Better measurement can reduce input uncertainty; retaining more guard digits can reduce avoidable round-off; refining a method can reduce truncation error; and reformulating a sensitive calculation may reduce amplification. No single remedy fixes every source. If the instrument uncertainty dominates, using a much finer numerical method may produce more digits without improving the answer’s actual accuracy.

### 4.11 Short audit before submitting an answer

Read the exact wording of the question and label the target: absolute, relative, percentage, propagated, or accumulated error. Write down the exact or reference value and the computed approximation. For a percentage, compute the relative error first and multiply by $100$ only at the final step. For a decimal-place bound, use half of the last retained place under ordinary rounding.

For a calculation involving several approximate values, use the operation to decide how to proceed. Add absolute uncertainty bounds for sums and differences. Use a first-order relative estimate for products only when the relative perturbations are small, or retain exact cross terms when they are not. For division, inspect the entire denominator interval. For a general formula, identify how strongly the output changes with each input and label a differential result as an estimate.

Finally, check units, signs, interval order, and reported precision. A high-quality numerical answer is not just a decimal: it includes enough information for another reader to understand the approximation, reproduce it, and judge whether its uncertainty is acceptable.

### 4.12 One input tolerance, several consequences

Suppose a side of a square is measured as $s=3.0\pm0.1$ m. The central area is $9.0\ \text{m}^2$. The differential estimate is $2s\Delta s=0.6\ \text{m}^2$, because changing the side changes both dimensions of the square. The exact allowed side interval is $[2.9,3.1]$, so the area lies in $[8.41,9.61]\ \text{m}^2$. Relative to the central area, the deviations are $0.59$ and $0.61\ \text{m}^2$. The first-order estimate is close, and the interval shows the small asymmetry caused by squaring the perturbed side.

The same input error would have a different effect if the requested quantity were the perimeter $P=4s$. The central perimeter would be $12.0$ m and the absolute error bound would be $4(0.1)=0.4$ m, exactly because the expression is linear. A formula, not just the measurement tolerance, determines how the uncertainty is transmitted.

If the problem asks which measurement should be improved, compare their contributions after multiplying by the appropriate sensitivity. Improving the side measurement from $\pm0.1$ to $\pm0.01$ reduces both area and perimeter uncertainty; adding extra digits to the calculator output does neither.

### 4.13 Repeated measurements and averages

Suppose three readings of a temperature are $18.2$, $18.4$, and $18.3$ degrees, each rounded to the nearest tenth. Their arithmetic mean is $18.3$. If the only known uncertainty is rounding, each reading can differ from its true value by at most $0.05$ degree. The mean’s worst-case absolute error is also at most $0.05$ degree, because the mean of three signed errors cannot exceed the largest common bound when all have the same maximum sign.

The bound does not automatically shrink to $0.05/\sqrt{3}$. That reduction would require a random-error model with assumptions about independence and distribution. The fact that there are three observations alone does not justify statistical error reduction. A deterministic maximum bound and a statistical standard error answer different questions.

This distinction is important whenever measurements are averaged. If a course problem gives only a maximum error, use a worst-case argument. If it gives a probabilistic model or sample variance, use the stated statistical method and name the assumption. Do not mix the two conventions in one numerical answer without explanation.

### 4.14 A final unit and magnitude comparison

Suppose a calculator reports an absolute error of $0.04$ litres in a small bottle holding about $0.5$ litres. The relative error is $0.04/0.5=0.08$, or $8\%$. The same $0.04$-litre error in a tank holding $200$ litres is $0.0002$, or $0.02\%$. The absolute error has the same physical unit and size, but the consequences differ.

It is often useful to state both numbers: “an absolute error of $0.04$ litres, which is $8\%$ of the bottle’s volume.” This avoids hiding the scale behind a percentage or losing physical meaning by reporting only a dimensionless ratio. For a quantity near zero, the percentage can be unstable, so emphasize absolute error and the choice of reference.

### 4.15 A tolerance can change the decision

Imagine that a design is acceptable only if its computed length is below $10.0$ cm. A displayed result of $9.99$ cm might appear to pass. If the underlying measurement has a possible error of $0.02$ cm, however, the true value could be as high as $10.01$ cm. The central value alone cannot establish compliance. The interval must be compared with the limit: if the whole interval lies below the threshold, the result is guaranteed to pass; if the interval crosses the threshold, more accurate data or a conservative decision is needed.

This is one reason error bounds are practical, not merely theoretical. An approximation with a small relative error may still be unacceptable if its absolute uncertainty crosses a safety or engineering tolerance. Conversely, a comparatively large percentage error may be harmless when the quantity itself is unimportant and the absolute deviation is small. Accuracy is always evaluated relative to the decision being made.

### 4.16 Significant figures in the final display

Consider a calculator output of $0.009876543$ obtained from a measurement reported to three significant figures. The first nonzero digit is $9$; the next two significant digits are $8$ and $7$, and the following digit $6$ determines rounding. The three-significant-figure display is $0.00988$. The leading zeros locate the decimal place but do not increase the count of significant digits.

The same value rounded to three decimal places would be $0.010$, which communicates a different precision. Trailing zeros after the decimal point can be meaningful: $0.010$ has two significant figures under the usual convention, while $0.01$ has one. If the intent is ambiguous, scientific notation makes the count explicit.

Precision in the final display should not exceed the evidence. If the calculation is an intermediate step, retaining extra digits can reduce rounding error in subsequent operations. If it is the answer, extra digits should either be justified by the input data and error analysis or clearly identified as guard digits rather than measurement accuracy.

### 4.17 A three-question numerical diagnosis

When a computed result appears unreliable, ask three questions in order. First, what is the size and origin of the input uncertainty? A measurement tolerance cannot be removed by arithmetic. Second, what operation carries that uncertainty forward? Subtraction can cancel leading digits, division can become unstable near a zero denominator, and multiplication can scale absolute errors. Third, what new approximation or rounding does the method introduce?

For example, if the final value changes significantly when the last input digit is altered within its allowed range, then input sensitivity is the main issue. If it changes when the order of arithmetic operations is altered but the mathematical expression is unchanged, round-off or cancellation may be significant. If it changes as a finite method is refined, the current result may still carry truncation error.

The diagnosis points to a specific remedy: improve data, choose a more stable equivalent calculation, retain more precision in intermediate work, or refine the numerical method. Applying a remedy unrelated to the dominant source can produce a longer calculation without producing a more trustworthy answer.

## 5. Mathematical Extensions, Limits, and Common Errors

Many calculations use several approximate inputs. If



$$
z=f(x_1,x_2,\ldots,x_n),
$$



and the input $x_i$ has a small error $\Delta x_i$, then a first-order estimate for the output error is



$$
|\Delta z|\approx \sum_{i=1}^{n}
\left|\frac{\partial f}{\partial x_i}\right|\,|\Delta x_i|.
$$



Each partial derivative measures how strongly the output responds to a small change in one input while the others are held fixed. A large derivative means that even a small input error can noticeably affect the result. The formula is an estimate for small errors; it is not an exact bound for every large change.

For a square with side length $s$, the area is $A=s^2$, so $dA/ds=2s$. If $s=10$ m and the side-length uncertainty is at most 0.1 m, then



$$
|\Delta A|\approx |2s|\,|\Delta s|=2(10)(0.1)=2\text{ m}^2.
$$



The area uncertainty is about 2 square metres. This example shows why the formula of a calculation matters: the same measurement error can have a different effect in a different quantity.

As a second illustration, suppose a rectangle has measured sides $a=4$ m and $b=3$ m, with possible errors of 0.02 m and 0.01 m. Its area is $A=ab$, so



$$
|\Delta A|\approx |b|(0.02)+|a|(0.01)
=3(0.02)+4(0.01)=0.10\text{ m}^2.
$$



This estimate helps decide whether the measurements are accurate enough for the intended use.

### Additional source-grounded lesson connections

### Example: error in an approximation to $\pi$

Use $x=\pi$ and $x_r=3.14$.

1. Absolute error:



$$
E_{abs}=|\pi-3.14|\approx 0.00159265.
$$



2. Relative error:



$$
E_{rel}=\frac{0.00159265}{\pi}\approx 0.000507.
$$



3. Percentage error:



$$
E_{pct}\approx 100(0.000507)\%=0.0507\%.
$$



The same approximation therefore has three descriptions: an absolute difference, a scale-adjusted difference, and that scale-adjusted difference as a percentage.

### Example: adding rounded measurements

Suppose 3.45 and 4.87 are each rounded to the nearest 0.01. Each input can differ from its true value by at most 0.005. The computed sum is 8.32, and its worst-case absolute input-error bound is



$$
0.005+0.005=0.01.
$$



So the exact sum lies between 8.31 and 8.33 (with endpoint details depending on the tie-rounding convention). Reporting many extra decimal places would not be justified by these inputs.

### Check yourself before submitting

### A small measurement chain, checked in plain language

Suppose a rectangular card is recorded as 12.4 cm long and 5.8 cm wide, with each measurement rounded to the nearest tenth of a centimetre. The measurements are not exact points; each is the centre of a small interval. The length differs from its true value by no more than 0.05 cm, and the same is true of the width. The recorded area is 71.92 square centimetres, but that is an area calculated from rounded inputs, not a promise that the true area is exactly 71.92.

The useful first question is not “How many digits does the calculator show?” It is “How much could the measurements themselves change the product?” A longer side makes the area more responsive to a width change, and a wider side makes it more responsive to a length change. Using the first-order product estimate gives

$$
|\Delta A|\approx 5.8(0.05)+12.4(0.05)=0.91\text{ cm}^2.
$$

The omitted cross-effect is at most \(0.05(0.05)=0.0025\text{ cm}^2\), so a conservative product bound adds that amount. This is a useful scale check: the uncertainty is close to one square centimetre, so reporting the area to many decimal places would suggest unjustified certainty. The estimate does not mean the actual error must equal 0.91; the signs of the two measurement errors may reinforce or partly cancel.

Now imagine the same absolute uncertainty for a tiny object whose area is about \(0.2\text{ cm}^2\). An uncertainty around \(0.9\text{ cm}^2\) would be larger than the quantity itself, so the recorded measurements would not support a useful area estimate. This comparison explains why relative error is important: it says how large the discrepancy is compared with the value being described. Absolute error answers “how many units?”; relative error answers “what fraction of the value?”; percentage error answers the same question per hundred.

### Three checks that prevent a plausible-looking wrong answer

First, identify the reference value. If an exercise gives an exact value and a rounded value, use the exact one in the denominator of relative error. Second, preserve the unit: an area error is measured in square units, not in the original length unit. Third, distinguish a tolerance from an observed error. “Rounded to the nearest tenth” supplies a bound on the possible measurement discrepancy; it does not tell us the actual signed error. A calculated bound should therefore be described as a maximum or estimate, not as the error that definitely occurred.

These checks also clarify the difference between rounding and truncation in a calculation. Rounding selects the nearest retained decimal according to the next digit. Chopping simply removes later digits. If several intermediate quantities are rounded, each later operation receives already altered inputs, so avoid adding unnecessary rounding steps. Keep guard digits while calculating, then round the final answer to a precision that the original measurements can support.

Finally, ask whether the mathematical operation magnifies a small discrepancy. Adding two measured lengths usually carries their absolute uncertainties into the sum. Multiplying them makes the result depend on each side’s size as well as its uncertainty. Subtracting two nearly equal measurements is especially delicate: the difference may be small even though each original measurement was fairly large, making the error a large fraction of the answer. A sound numerical report gives both the computed result and an honest description of its uncertainty.

- Is the question asking for absolute error, relative error, or percentage error?
- Is the exact value nonzero before using relative error?
- Does “decimal places” or “significant figures” describe the requested rounding?
- Are input errors being propagated, or is new rounding generated during the calculation?
- Is a small denominator or subtraction of nearly equal numbers making the result sensitive?
- Have you kept extra digits during working and rounded only at the end?

The main lesson is not that every computation can be exact. It is that a good numerical answer states what was approximated, identifies where error entered, estimates how it affects the result, and reports only precision the data can support.
