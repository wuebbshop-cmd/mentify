## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The everyday idea behind composite formulae

Imagine you want to measure the area of a long, curved garden path. You cannot lay one giant rectangular mat over it, because the path bends. But you can chop the path into many short strips. Over each short strip, the path is almost straight, so a simple shape (a rectangle or a trapezium) fits it well. Add up the areas of all the small strips, and you have a good estimate of the total area.

That is the whole idea of a **composite formula**. We take a simple rule that works well on a short piece, and we apply it again and again over many short pieces, then add the results. The word *composite* simply means "made by putting many parts together."

The same idea applies to finding the area under a curve $y=f(x)$ between two limits $a$ and $b$. We split the interval $[a,b]$ into $n$ equal small pieces, each of width $h$, and apply a basic rule on each piece.

### 1.2 The everyday idea behind Romberg integration

Now suppose you measure the path twice: once with long strips and once with very short strips. The short-strip answer is usually better. Romberg integration is a clever way of *combining* two such estimates so that the errors partly cancel, giving a much better answer than either estimate alone. It is like asking two people to guess a distance, then averaging their guesses in a smart weighted way to get closer to the truth.

### 1.3 Where this topic sits in the course

This topic builds directly on earlier work on numerical integration (the basic trapezoidal and Simpson rules) and on the study of errors. The key insight is that every numerical integration rule carries an error, and that error has a predictable *shape* as the step size $h$ shrinks. Romberg integration exploits that predictable shape.

> **Scope note.** This unit covers composite trapezoidal and composite Simpson formulae, their error terms, and Romberg integration. It does not cover quadrature methods, iterative root-finding, or Newton–Raphson and secant methods, which belong to later units.

### 1.4 A note on the lesson activities

The course materials frame this unit around a set of learning activities: defining the ideas, computing errors, listing key words in definitions, making short notes on causes of errors and how to reduce them, encouraging participation of all learners, providing feedback, summarising the lesson, and computing propagated errors. These activities are woven through the sections below so that each one is addressed in context.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Setting up the interval and the step size

Let $f$ be a function we can evaluate at any point, and let $a$ and $b$ be the lower and upper limits of integration, with $a<b$. We divide $[a,b]$ into $n$ equal subintervals. Each subinterval has width



$$
h=\frac{b-a}{n}.
$$



The division points are



$$
x_0=a,\quad x_1=a+h,\quad x_2=a+2h,\quad \dots,\quad x_n=a+nh=b.
$$



We write $f_i=f(x_i)$ for the value of the function at the $i$-th point. The symbol $h$ is called the **step size**; it is measured in the same units as $x$.

### 2.2 The composite trapezoidal rule

> **Definition (Composite trapezoidal rule).** For $n$ equal subintervals of width $h=(b-a)/n$, the composite trapezoidal approximation to $\int_a^b f(x)\,dx$ is



$$
> T_n=\frac{h}{2}\Big[f_0+2f_1+2f_2+\dots+2f_{n-1}+f_n\Big].
$$



In words: the two end values $f_0$ and $f_n$ are counted once, and every interior value is counted twice. The factor $h/2$ comes from the area of a single trapezium, $\tfrac{h}{2}(f_{i-1}+f_i)$, summed over all strips.

### 2.3 The composite Simpson rule

> **Definition (Composite Simpson rule).** For an even number $n$ of equal subintervals of width $h=(b-a)/n$, the composite Simpson approximation is



$$
> S_n=\frac{h}{3}\Big[f_0+4f_1+2f_2+4f_3+\dots+2f_{n-2}+4f_{n-1}+f_n\Big].
$$



Here the pattern of coefficients is $1,4,2,4,2,\dots,4,1$: the end values get coefficient $1$, odd-indexed interior values get $4$, and even-indexed interior values get $2$. The rule requires $n$ to be even.

### 2.4 Error terms for the composite rules

> **Result (Error of the composite trapezoidal rule).** If $f$ has a continuous second derivative on $[a,b]$, then



$$
> \int_a^b f(x)\,dx-T_n=-\frac{(b-a)}{12}h^2 f''(\xi)
$$



> for some $\xi\in(a,b)$.

> **Result (Error of the composite Simpson rule).** If $f$ has a continuous fourth derivative on $[a,b]$, then



$$
> \int_a^b f(x)\,dx-S_n=-\frac{(b-a)}{180}h^4 f^{(4)}(\eta)
$$



> for some $\eta\in(a,b)$.

The important structural fact is the power of $h$: the trapezoidal error shrinks like $h^2$, while the Simpson error shrinks like $h^4$. This is why Simpson is normally far more accurate for the same step size.

### 2.5 The error expansion that powers Romberg integration

> **Definition (Asymptotic error expansion).** For a smooth function, the composite trapezoidal values satisfy



$$
> T_n=I+c_1h^2+c_2h^4+c_3h^6+\dots
$$



> where $I=\int_a^b f(x)\,dx$ is the exact integral and $c_1,c_2,\dots$ are constants that do not depend on $h$.

The key point is that only *even* powers of $h$ appear. This is the fact that makes Romberg integration possible: if we know the error behaves like a polynomial in $h^2$, we can eliminate the leading error term by combining two estimates.

### 2.6 Romberg integration

> **Definition (Romberg integration).** Let $T_n(h)$ denote the composite trapezoidal value with step $h$, and let $T_n(h/2)$ denote the value when the step is halved. The first Romberg extrapolation is



$$
> R_{1,1}=T_n(h/2)+\frac{T_n(h/2)-T_n(h)}{3}.
$$



This combination cancels the $h^2$ error term, leaving an error of order $h^4$. Repeating the same idea at successive levels produces the Romberg table, whose entries $R_{k,j}$ are built by the recurrence



$$
R_{k,j}=R_{k,j-1}+\frac{R_{k,j-1}-R_{k-1,j-1}}{4^{\,j-1}-1}.
$$



The denominator $4^{\,j-1}-1$ takes the values $3,15,63,\dots$ as $j$ increases. Each column removes one more power of $h^2$ from the error.

### 2.7 Errors and their computation (supporting definitions)

Because composite formulae are numerical approximations, we must be able to measure how wrong they are. The following definitions, carried over from the earlier study of errors, are used throughout.

> **Definition (Absolute error).** If $x$ is the exact value and $x_r$ is an approximation, the absolute error is



$$
> e_{\text{abs}}=\lvert x-x_r\rvert.
$$



> **Definition (Relative error).** The relative error is



$$
> e_{\text{rel}}=\frac{\lvert x-x_r\rvert}{\lvert x\rvert}.
$$



> **Definition (Percentage error).** The percentage error is the relative error written as a percentage:



$$
> e_{\%}=100\cdot\frac{\lvert x-x_r\rvert}{\lvert x\rvert}.
$$



> **Definition (Round-off error).** Round-off error arises because a machine with finite memory cannot store every real number exactly. It comes from dropping digits, either by chopping (truncating) or by symmetric rounding.

> **Definition (Truncation error).** Truncation error is the error made when an infinite process is replaced by a finite one, for example when a series is cut off after finitely many terms.

> **Definition (Propagated error).** The error in the result of an arithmetic operation that arises from the initial errors in the numbers used in that operation is called the propagated error. The total cumulative error at any step of a procedure is called the accumulated error.

### 2.8 Key words in the definitions (point form)

The course activity asks for the key words in the definitions of errors. In point form:

- **Exact value** — the true, ideal number we would like to have.
- **Approximate value** — the number we actually compute or store.
- **Difference** — the gap between the exact and approximate values.
- **Absolute value** — the size of the gap, ignoring sign.
- **Upper bound** — the largest the gap can possibly be.
- **Relative** — the gap measured as a fraction of the exact value.
- **Percentage** — the relative gap expressed out of one hundred.
- **Round-off** — loss caused by limited storage of digits.
- **Truncation** — loss caused by stopping an infinite process early.
- **Propagated** — error carried forward from inputs into a result.
- **Accumulated** — total error built up over many steps.

### 2.9 Causes of errors and how to reduce them (short notes)

The course activity also asks for short notes on the causes of errors and how to avoid them. In point form:

- **Cause: limited machine memory.** A computer cannot store infinitely many digits. *Remedy:* keep track of significant figures and round only at the end of a calculation.
- **Cause: chopping instead of rounding.** Dropping digits without adjusting the last kept digit biases the answer. *Remedy:* use symmetric rounding, which keeps the error balanced.
- **Cause: truncating an infinite series.** Stopping a series early leaves a remainder. *Remedy:* choose enough terms, or use a rule whose error term is known to be small.
- **Cause: large step size in composite rules.** A coarse grid gives a poor approximation. *Remedy:* reduce $h$, or use a higher-order rule such as Simpson.
- **Cause: subtracting nearly equal numbers.** This magnifies relative error. *Remedy:* rearrange the algebra to avoid the subtraction, or use extra precision.
- **Cause: error carried through many operations.** Small input errors grow. *Remedy:* use the propagation rules in Section 2.10 to bound the final error.

### 2.10 Computation of propagated errors

Let $x$ and $y$ be exact numbers, and let $x^{*}$ and $y^{*}$ be approximations with initial errors $\varepsilon$ and $\eta$ respectively, so that



$$
x=x^{*}+\varepsilon,\qquad y=y^{*}+\eta.
$$



For an arithmetic operation $\circ$, the propagated error is the part of the discrepancy that comes from the input errors, while the generated error is the part produced by the operation itself. The total is the accumulated error.

> **Result (Propagation in addition and subtraction).** For addition and subtraction,



$$
> e_{\text{abs}}(x\pm y)=\lvert\varepsilon\rvert+\lvert\eta\rvert.
$$



> The absolute errors add, regardless of the sign of the operation.

> **Result (Propagation in multiplication).** For multiplication,



$$
> e_{\text{rel}}(xy)\approx e_{\text{rel}}(x)+e_{\text{rel}}(y).
$$



> The relative errors add.

> **Result (Propagation in division).** For division,



$$
> e_{\text{rel}}\!\left(\frac{x}{y}\right)\approx e_{\text{rel}}(x)+e_{\text{rel}}(y).
$$



> Again the relative errors add.

These rules explain why composite formulae, which involve many additions and multiplications, can accumulate noticeable error if the step size is very small and the number of terms very large.

### 2.11 Encouraging participation and providing feedback

The course activity lists two teaching practices that support learning this unit. In point form:

- **Encouraging participation of all learners.** Invite every learner to attempt the error computations and the Romberg table by hand, then compare answers in a group. Ask quieter learners to explain one row of the table in their own words.
- **Providing feedback.** After each attempt, point out exactly which step went wrong (for example, a missing factor of $h/2$, or an odd number of subintervals used with Simpson). Feedback should name the rule and show the corrected line.

### 2.12 Summarising the lesson

In one short summary: composite formulae chop the interval into equal strips and add simple areas; their errors shrink as powers of $h$; Romberg integration combines two trapezoidal estimates to cancel the leading error and produce a much more accurate value; and all of this rests on the earlier definitions of absolute, relative, and propagated error.

## 3. Formal Proofs, Derivations, and Methods

> **Theorem (Composite trapezoidal rule).** Let $f$ be continuous on $[a,b]$ and let $n\ge1$. With $h=(b-a)/n$ and $x_i=a+ih$, the composite trapezoidal approximation is



$$
> T_n=\frac{h}{2}\Big[f_0+2\sum_{i=1}^{n-1}f_i+f_n\Big].
$$



> **Theorem (Composite Simpson rule).** Let $f$ be continuous on $[a,b]$ and let $n$ be even. With $h=(b-a)/n$, the composite Simpson approximation is



$$
> S_n=\frac{h}{3}\Big[f_0+4\!\!\sum_{i\ \text{odd}}\!\!f_i+2\!\!\sum_{i\ \text{even},\,i\ne0,n}\!\!f_i+f_n\Big].
$$



> **Theorem (Error order).** The composite trapezoidal rule has error of order $h^2$, and the composite Simpson rule has error of order $h^4$. Halving $h$ reduces the trapezoidal error by roughly a factor of $4$ and the Simpson error by roughly a factor of $16$.

> **Theorem (Romberg extrapolation).** If the trapezoidal values admit the expansion $T_n=I+c_1h^2+c_2h^4+\dots$, then the combination



$$
> R_{1,1}=T_n(h/2)+\frac{T_n(h/2)-T_n(h)}{3}
$$



> satisfies $R_{1,1}=I+O(h^4)$. Each further Romberg level removes one more even power of $h$ from the error.

> **Theorem (Propagation bounds).** For approximations $x^{*}$ and $y^{*}$ with absolute errors $\lvert\varepsilon\rvert$ and $\lvert\eta\rvert$, the absolute error of $x\pm y$ is at most $\lvert\varepsilon\rvert+\lvert\eta\rvert$, and the relative error of $xy$ or $x/y$ is approximately the sum of the relative errors of the inputs.

## 4. Representative Worked Examples and Solutions
### Worked source example: Romberg integration of 1/x

The module asks for the integral of 1/x from 1 to 2. First use one trapezoid. The interval width is one, and the endpoint heights are 1 and 1/2:



$$
T_1=\frac12\left(1+\frac12\right)=0.7500000.
$$



With two panels, the midpoint is 3/2 and its height is 2/3:



$$
T_2=\frac{1/2}{2}\left[1+2\left(\frac23\right)+\frac12\right]=0.7083333.
$$



Refining to four panels gives T_4≈0.6970238; eight panels give T_8≈0.6941219; sixteen panels give T_16≈0.6933912. These are trapezoidal estimates, not yet the corrected Romberg answers. At each refinement, the new grid keeps the previous points and adds midpoints.

The first correction uses the two coarsest estimates. The finer value T_2 is used first; the signed difference T_2−T_1 is negative:



$$
R_{1,1}=T_2+\frac{T_2-T_1}{3}
=0.7083333+\frac{0.7083333-0.7500000}{3}\approx0.6944444.
$$



For the next pair,



$$
R_{2,1}=T_4+\frac{T_4-T_2}{3}
=0.6970238+\frac{0.6970238-0.7083333}{3}\approx0.6932539.
$$



A further first-column correction gives approximately 0.6931545. The next Romberg columns use denominators fifteen, sixty-three, and so on. Continuing the triangle gives a final diagonal value near 0.69314718. The exact integral is ln 2≈0.69314718, so the computed diagonal agrees to the displayed precision.

The lesson of the example is not that every integral should equal ln 2; it is how the estimates are organized. The trapezoidal values make the left edge, while the corrections use neighboring entries to remove their leading error terms. Keep the fine-minus-coarse sign: reversing it would move the first correction in the wrong direction. When an exact integral is unavailable, compare diagonal entries and report this as convergence evidence rather than a certified bound.

## 5. Mathematical Extensions, Limits, and Common Errors
### 5.1 High-yield takeaways

- **Know both composite formulae by heart.** Trapezoidal uses coefficients $1,2,2,\dots,2,1$ with factor $h/2$. Simpson uses $1,4,2,4,\dots,4,1$ with factor $h/3$ and needs $n$ even.
- **Always compute $h$ first.** Write $h=(b-a)/n$ explicitly before substituting. Most lost marks come from a wrong $h$.
- **Remember the error orders.** Trapezoidal error is $O(h^2)$; Simpson error is $O(h^4)$. Halving $h$ multiplies the trapezoidal error by about $1/4$ and the Simpson error by about $1/16$.
- **Romberg denominator is $4^{j-1}-1$.** The first correction divides by $3$, the next by $15$, then $63$, and so on.
- **Use the halving shortcut.** When refining the trapezoidal value, reuse the old sum: $T_{2n}=\tfrac12 T_n+\tfrac{h_{\text{new}}}{2}(\text{new midpoints})$.
- **State the error definitions precisely.** Absolute error is $\lvert x-x_r\rvert$; relative error divides by $\lvert x\rvert$; percentage error multiplies by $100$.
- **Quote the propagation rules.** Absolute errors add under $+$ and $-$; relative errors add under $\times$ and $\div$.
- **Summarise in words.** A one-line summary at the end of a solution ("the trapezoidal estimate is about $1.768$, improved by Romberg to about $1.769$") earns credit and shows understanding.

### 5.2 Common pitfalls

- **Using an odd $n$ with Simpson.** The composite Simpson rule requires an even number of subintervals. If $n$ is odd, either change $n$ or use the trapezoidal rule.
- **Forgetting to double the interior terms in the trapezoidal rule.** The factor $2$ applies to every interior value, not just some.
- **Mixing up $h/2$ and $h/3$.** Trapezoidal uses $h/2$; Simpson uses $h/3$. Writing the wrong factor is the single most common arithmetic slip.
- **Applying the Romberg correction in the wrong direction.** The correction is added, not subtracted: $R=T_{16}+(T_{16}-T_8)/3$.
- **Confusing absolute and relative error.** Absolute error carries units; relative error is a pure fraction. Do not divide by $\lvert x\rvert$ when absolute error is asked for.
- **Rounding too early.** Keep full precision through the intermediate sums and round only the final answer. Early rounding inflates the propagated error.
- **Ignoring the sign in subtraction.** When subtracting nearly equal numbers, the relative error can blow up even though the absolute error looks small. Mention this in error discussions.
- **Skipping the summary.** The course activity explicitly asks for a lesson summary; a short closing sentence in words shows the marker that the method and its accuracy have been understood.

### Reading the triangular table

The Romberg array is triangular because a correction needs two estimates that already exist. Its left edge contains ordinary composite trapezoidal values. Moving down that edge halves the panel width and doubles the number of trapezia. Moving one column to the right does something different: it combines two adjacent approximations to remove a leading error term. It does not introduce a new set of function values. Keeping those roles separate helps make sense of the table: rows record refinement of the mesh, while columns record extrapolation.

For one composite trapezoidal estimate, each panel contributes its width times the average of its two endpoint heights. When neighboring panels are added, an interior height belongs to two panels, so it is counted twice; the two boundary heights occur only once. This explains the familiar endpoint-once, interior-twice formula. If the panel width is h and there are n panels, check that nh equals b−a before evaluating the weighted sum. The resulting area has units of a function value times a horizontal interval, which is a useful dimensional check.

A curve can bend above or below a straight chord. The trapezoidal bias therefore depends on curvature. It is not safe to memorize that this rule always overestimates or always underestimates: that direction follows only under additional shape conditions. For a smooth function, however, halving h changes the leading global error in a predictable way. Romberg uses this predictable scaling to improve a result without fitting a new polynomial to the function.

### Why the first correction uses three

Suppose a coarse approximation has a leading error proportional to h squared. Halving the panel width changes that error by a factor of one quarter. If the coarse error is E, the fine error is approximately E/4. The difference between the fine and coarse estimates is then approximately −3E/4, so adding one third of that signed difference to the fine estimate cancels the leading bias. That is the reason for the factor one third; it is not a convenient average chosen by trial and error.

The first Romberg correction can be written with a named coarse value and fine value so that the sign remains visible:



$$
R_{1,1}=T_2+\frac{T_2-T_1}{3}.
$$



Here T_2 uses the finer of the two grids. If the fine estimate is smaller, the correction is negative; if it is larger, the correction is positive. Taking an absolute difference before using the formula destroys this information and can send the estimate in the wrong direction.

After the h-squared term is canceled, the next leading error behaves like h to the fourth power. Halving h now scales that term by one sixteenth. The next denominator is therefore fifteen, the difference between sixteen and one. Later denominators follow the same pattern: the j-th correction uses 4 to the power j minus one. The table makes the cancellation visible but does not remove the need to track which entry is coarse and which is fine.

### Source-sized calculation for the logarithm

The lesson's sample integral is the area under 1/x from 1 to 2. Its exact value is ln 2, which can be used after the numerical calculation as a check. On the first grid the width is one and the endpoint heights are one and one half. Their average gives the first trapezoid:



$$
T_1=\frac{1}{2}\left(1+\frac12\right)=0.7500000.
$$



The two-panel grid adds the midpoint 3/2, where the height is 2/3. Its two panels give



$$
T_2=\frac{1/2}{2}\left[1+2\left(\frac23\right)+\frac12\right]=0.7083333.
$$



Continuing the same composite formula gives T_4 approximately 0.6970238, T_8 approximately 0.6941219, and T_16 approximately 0.6933912. These are all raw trapezoidal estimates. They approach ln 2 gradually, showing that merely increasing the number of panels can be less efficient than correcting the leading error.

For the first extrapolation, pair T_1 with T_2. The signed difference is negative, so the correction moves downward:



$$
R_{1,1}=0.7083333+\frac{0.7083333-0.7500000}{3}\approx0.6944444.
$$



The next pair gives



$$
R_{2,1}=0.6970238+\frac{0.6970238-0.7083333}{3}\approx0.6932539.
$$



The next columns use denominators fifteen, sixty-three, and so forth. Completing the table with the nested grids yields a diagonal close to 0.69314718, agreeing with ln 2 to the digits supported by this example. Each step is a repeatable application of the same recurrence, not a fresh quadrature rule.

### Choosing a stopping point and reporting digits

The diagonal of the Romberg table is a useful place to watch for stabilization. A practical calculation can stop when the change between consecutive diagonal values is below a chosen tolerance. But that difference is an indicator, not automatically a guaranteed error bound. Rounded function values may limit the accuracy, and a curve with a jump, corner, or sharp feature may not follow the smooth error pattern that Romberg expects.

A sound report states the panel counts, the final diagonal entry, and how the previous diagonal compares with it. If the exact integral is known, calculate the actual absolute difference. If it is not known, say that the diagonal values have stabilized to the observed precision; do not claim exact digits from a table alone. Avoid printing more decimal places than the data or error analysis justify. One extra column does not restore information lost through rounded ordinates.

Three quick checks prevent many mistakes. The panel counts double at every row; the sum of panel widths remains b−a; and each extrapolated cell uses the adjacent entries specified by the recurrence. If the table behaves oddly, check its labels and arithmetic before assuming the function is unsuitable. If the arithmetic is correct but the values oscillate, inspect smoothness and the quality of the input data instead of blindly extending the triangle.

### Working carefully with endpoints, panel counts, and units

Before arithmetic, draw or list the partition. For an interval [a,b] and n equal panels, the nodes are x_i=a+ih and h=(b−a)/n. The last node must be b; if it is not, either the panel count or the step is wrong. In a composite trapezoid, the first and last heights appear once, and all other heights appear twice. This count follows from the panels touching each point. It also gives a quick check on a long addition: the bracket is f_0+2(f_1+…+f_{n−1})+f_n, not the unweighted sum of all heights.

A common route to error is to round each function value or intermediate weighted sum too early. Keep enough digits through the triangle, then round the final reported approximation. If the problem supplies a short table, do not claim more information than the table contains. The trapezoidal rule can be exact for a straight-line integrand over the entire interval, but a curved function generally leaves an approximation error. A finer mesh usually improves a smooth case, while Romberg attempts to cancel the leading pattern in that error.

### Applying a stopping rule in practice

A learner can use the change in successive diagonal values as a signal to stop refining. Suppose the newest two diagonal entries agree to four decimal places and the requested tolerance is about one part in ten thousand. That agreement supports reporting the result to that precision, but only if the function is smooth and the ordinates are reliable. If the values fail to settle, do not keep adding columns automatically. Check the recurrence, the panel counts, the midpoint evaluations, and the behavior of the integrand.

The lesson's pi assessment gives an especially clear check: its final Romberg estimate rounds to 3.1415927. This agrees with the familiar value of pi, but a different integral will not come with a known answer. In that case, say exactly what the table supports: for example, “the last two diagonal estimates differ by less than the chosen tolerance.” That is more accurate than calling their difference a guaranteed error bound. If a separate error theorem is used, state its assumptions and how they apply to the particular integrand.

### Why a table is not just arithmetic

The first column displays what uniform refinement alone does. The next column displays the correction after the first error term is removed. Later columns show further cancellation. Thus the table tells a story about how the numerical approximation changes as information is refined. It also makes method failures visible: an unexpected jump may indicate a wrong function value, a missed midpoint, a sign error, or a feature of the integrand that the old grid did not see.

When presenting a result, keep four labels visible: the interval, the number of panels, the corresponding width, and whether the value is trapezoidal or extrapolated. Without these labels, two correct numbers can be placed in the wrong table cell and produce a wrong result. With them, another reader can reproduce the computation, verify the triangle, and decide whether the stated precision is credible.

### The lesson's pi question as a final check

The module also asks students to estimate pi from the area under 4/(1+x²) between zero and one and comment on accuracy. This is a useful companion to the logarithm example because the answer is known in advance for checking, but the trapezoidal and Romberg calculations still use sampled values. Start with one panel: the endpoint heights are 4 and 2, so the first trapezoid is 3. Doubling the panels gives 3.1; four panels give approximately 3.1311765; eight give 3.1389885; and sixteen give 3.1409416. The raw estimates steadily approach pi in this example.

The first Romberg correction from 3.0 and 3.1 is 3.1333333. The next one uses 3.1 and 3.1311765, while later entries are formed from their own neighboring corrected values. After four mesh doublings the final diagonal is approximately 3.1415926653, which rounds to 3.1415927. The result is close to pi, and the difference between adjacent diagonal values is small. This is a reasonable comment on the computed convergence.

A student should not say that the method “always gives an exact answer after four steps.” It does not. This assessment is unusually convenient because the integral is a representation of pi, and the integrand is smooth on the interval. For another function, the same calculation may converge more slowly or behave irregularly. The justified conclusion is about this table: its diagonal entries stabilize and its final value agrees closely with the known value.

### Translating the method into a checklist

When the question gives an interval, first write its length and divide it by n to obtain h. Mark the endpoints and interior nodes. Apply the composite trapezoidal formula with each endpoint counted once and each interior value counted twice. To build Romberg values, halve h at each refinement and apply the recurrence column by column. Keep the signs and carry enough digits. At the end, state whether the final number is raw trapezoidal or extrapolated and explain what the changes between estimates show.

This checklist is useful because arithmetic errors often arise before the difficult part of the method. If the panel width does not fit the interval, every trapezoid is wrong. If a node is missed, both the left edge and the extrapolation triangle will be contaminated. If a denominator from the wrong column is used, the table may still look orderly but its values have no Romberg meaning. Naming the panel count and column for every number helps prevent these mistakes.

### Final audit before submitting the table

Before submitting a Romberg answer, re-read the labels as if another learner had to reproduce your work. The interval endpoints should match the first and last nodes; the sum of all panel widths must be exactly the interval length. The raw trapezoid sequence should identify its panel counts, and each extrapolated cell should be attached to a clear row and column. The sign of a correction should follow the written fine-minus-coarse formula, not a remembered expectation about whether the estimate ought to rise or fall.

For the source assessment of pi, the panel counts are 1, 2, 4, 8, and 16 when four doublings follow the starting trapezoid. A verbal report that says “four iterations” but lists only four rows may leave the convention unclear. Writing n explicitly avoids that ambiguity. The final value near 3.1415926653 is a Romberg diagonal value; 3.1409416120 is the last raw trapezoid. Confusing the two numbers would misstate both the method and its achieved accuracy.

A useful interpretation states that the diagonal values settle near the known answer, while also admitting that a table is not a universal proof. This final distinction is part of responsible numerical work: answer the calculation, identify the evidence for the reported precision, and do not claim a stronger bound than the calculation supplies.

### Relating a correction to the original area

An extrapolated value should still be interpreted as an estimate of the same definite integral, not as the area of an additional geometric region. The correction is a numerical adjustment that estimates and removes a leading bias in the trapezoidal values. Its size may be positive or negative. If it is much larger than the difference between the two raw estimates would suggest, check the denominator and row pairing. If it is tiny, that may indicate stabilization, but also check the number of digits carried through the subtraction.

The composite rule itself remains easy to visualize: every panel is a trapezoid, and adjoining panels share a vertical side. This mental picture explains the weighting but does not replace the formula. When the integrand is curved, the straight sides approximate rather than exactly trace the graph. The refinement and extrapolation are systematic ways to improve that representation, and their reliability depends on the function and the values used.