## 1. Foundational Concepts, Definitions, and Axioms

Numerical integration seeks to approximate a definite integral $\int_{a}^{b} f(x)\,dx$ when the integrand is known only through a table of values or when its antiderivative cannot be expressed in elementary form. The elementary Newton–Cotes rules (trapezoidal and Simpson's rules) approximate the integrand by a low-degree polynomial on a single interval. Their accuracy improves dramatically when the interval $[a,b]$ is subdivided into many small subintervals and the elementary rule is applied to each piece. The resulting formulas are called **composite formulae**.

The composite trapezoidal rule replaces $f$ by a straight line on each subinterval, producing a piecewise-linear approximation whose error is governed by the second derivative of $f$. The composite Simpson's rule replaces $f$ by a parabola on each pair of subintervals, producing an error governed by the fourth derivative. In both cases the total error is a sum of local truncation errors, and the global error decreases as a power of the step size $h$.

**Romberg integration** is an extrapolation device built on top of the composite trapezoidal rule. The key observation is that the composite trapezoidal approximation $T(h)$ admits an asymptotic error expansion in even powers of $h$:



$$
T(h) = I + c_1 h^2 + c_2 h^4 + c_3 h^6 + \cdots,
$$



where $I$ is the exact integral and the coefficients $c_k$ depend on $f$ and its derivatives at the endpoints but not on $h$. By evaluating $T(h)$ at two step sizes $h$ and $h/2$ and eliminating the leading $h^2$ term, one obtains an approximation whose error is $O(h^4)$. Repeating this elimination produces a triangular table of increasingly accurate values, each column corresponding to a higher order of accuracy. This is the essence of Romberg integration: systematic Richardson extrapolation applied to the trapezoidal rule.

The intuition is that the trapezoidal rule's error is not random but structured; by computing the rule at successively halved step sizes and combining the results with the correct weights, the structured error cancels order by order, leaving a rapidly convergent sequence of approximations.

## 2. Theorems, Lemmas, and Analytical Properties

> **Definition (Composite Trapezoidal Rule).** Let $[a,b]$ be divided into $n$ equal subintervals of width $h=(b-a)/n$ by the nodes $x_i = a + ih$ for $i=0,1,\dots,n$. The composite trapezoidal rule is



$$
> T_n = \frac{h}{2}\left[f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n)\right].
$$



The factor $2$ on the interior nodes arises because each interior node is shared by two adjacent subintervals, and the trapezoidal rule on each subinterval contributes $\frac{h}{2}f(x_i)$ from each side.

> **Definition (Composite Simpson's Rule).** Let $n$ be even and $h=(b-a)/n$. The composite Simpson's rule is



$$
> S_n = \frac{h}{3}\left[f(x_0) + 4\sum_{i\ \text{odd}} f(x_i) + 2\sum_{i\ \text{even},\,i\neq 0,n} f(x_i) + f(x_n)\right].
$$



Here the odd-indexed interior nodes receive weight $4$ and the even-indexed interior nodes receive weight $2$, reflecting the parabolic fit over each pair of subintervals.

> **Definition (Romberg Integration).** Let $T(h)$ denote the composite trapezoidal approximation with step size $h$. Define the first extrapolation



$$
> R_{1,1} = T(h), \qquad R_{2,1} = T\!\left(\frac{h}{2}\right),
$$



> and in general the Romberg table entries



$$
> R_{k,j} = R_{k,j-1} + \frac{R_{k,j-1} - R_{k-1,j-1}}{4^{\,j-1}-1}, \qquad j=2,3,\dots,k.
$$



The denominator $4^{j-1}-1$ is the Richardson extrapolation factor that cancels the $h^{2(j-1)}$ term in the error expansion. The first column $R_{k,1}$ consists of trapezoidal approximations with step sizes $h, h/2, h/4, \dots$; the second column $R_{k,2}$ consists of Simpson-type approximations; the third column corresponds to Boole-type accuracy, and so on.

> **Definition (Error of the Composite Trapezoidal Rule).** If $f\in C^2[a,b]$, there exists $\xi\in(a,b)$ such that



$$
> \int_{a}^{b} f(x)\,dx - T_n = -\frac{(b-a)}{12}h^2 f''(\xi).
$$



> **Definition (Error of the Composite Simpson's Rule).** If $f\in C^4[a,b]$ and $n$ is even, there exists $\xi\in(a,b)$ such that



$$
> \int_{a}^{b} f(x)\,dx - S_n = -\frac{(b-a)}{180}h^4 f^{(4)}(\xi).
$$



These error terms are the foundation of the extrapolation idea: the leading error of $T_n$ is proportional to $h^2$, so halving $h$ reduces the error by a factor of approximately $4$, and the residual can be eliminated algebraically.

### 2.1 Key Words in the Definitions

In point form, the essential terms in the definitions above are:

- **Nodes**: the equally spaced points $x_i = a + ih$ at which $f$ is evaluated.
- **Step size** $h$: the common width of each subinterval, $h=(b-a)/n$.
- **Subinterval**: each interval $[x_{i-1},x_i]$ on which an elementary rule is applied.
- **Weights**: the coefficients $\frac{h}{2}, \frac{h}{3}, 4, 2$ multiplying the function values.
- **Composite**: the rule is applied repeatedly over subintervals and the results summed.
- **Extrapolation**: combining approximations at different step sizes to cancel leading error terms.
- **Romberg table**: the triangular array $R_{k,j}$ of extrapolated values.
- **Order of accuracy**: the power of $h$ in the leading error term.

### 2.2 Causes of Error and Their Control

The errors in composite formulae and Romberg integration arise from several sources, and each admits a standard remedy:

- **Truncation error** from replacing $f$ by a polynomial on each subinterval. It is controlled by reducing $h$ (increasing $n$) or by using a higher-order rule.
- **Round-off error** from finite-precision arithmetic when many function values are summed. It grows as $n$ increases, so there is an optimal $n$ beyond which further subdivision is counterproductive.
- **Data error** when the tabulated values of $f$ are themselves approximations. This propagates linearly through the weighted sum.
- **Cancellation in extrapolation** when differences $R_{k,j-1}-R_{k-1,j-1}$ become small relative to the entries themselves; this limits the useful depth of the Romberg table.

The standard measures to minimise these errors are: choose $h$ so that truncation and round-off are balanced; use the composite Simpson rule when $f$ is smooth; use Romberg extrapolation to obtain high accuracy from relatively few trapezoidal evaluations; and retain sufficient significant figures in intermediate sums.

### 2.3 Propagation of Error Through the Weighted Sum

Each composite formula is a linear combination of function values,



$$
Q = \sum_{i=0}^{n} w_i f(x_i),
$$



where the $w_i$ are the weights. If each tabulated value carries an initial error $\varepsilon_i$, the propagated error in $Q$ is bounded by



$$
\lvert \Delta Q \rvert \le \sum_{i=0}^{n} \lvert w_i \rvert\,\lvert \varepsilon_i \rvert.
$$



For the composite trapezoidal rule with uniform bound $\lvert \varepsilon_i \rvert \le \varepsilon$, this gives



$$
\lvert \Delta T_n \rvert \le \frac{h}{2}\left(\varepsilon + 2(n-1)\varepsilon + \varepsilon\right) = n h \varepsilon = (b-a)\varepsilon.
$$



Thus the propagated error in the trapezoidal rule is independent of $n$ to first order: subdividing more finely does not amplify a uniform data error. For Romberg extrapolation, the amplification factor of the $j$-th column is the sum of the absolute values of the extrapolation coefficients, which grows with $j$; this is why deep extrapolation becomes sensitive to round-off.

### 2.4 Reconciling the Two Error Statements

The two statements about error growth are not in conflict once the distinction between the two error models is made explicit.

The bound $(b-a)\varepsilon$ describes **data error**: a fixed perturbation $\varepsilon$ attached to each tabulated value $f(x_i)$, with the arithmetic itself performed exactly. Because the trapezoidal weights sum to $b-a$ (the interior weights $2\cdot\frac{h}{2}=h$ telescope against the subinterval widths), the total amplification of a uniform data perturbation is exactly $b-a$, whatever $n$ is. Refining the mesh redistributes the same total weight over more nodes but does not increase it.

**Round-off error** is a different mechanism. It arises from the finite precision of each individual floating-point addition and multiplication, so each of the roughly $n$ additions in the weighted sum contributes a fresh rounding of relative size about $u$ (the unit round-off). The accumulated round-off therefore behaves like a sum of $n$ independent perturbations of size proportional to $u$ times the magnitude of the partial sums, and grows with $n$ — typically like $n u$ in the worst case and like $\sqrt{n}\,u$ in a random-walk model. The $(b-a)\varepsilon$ result does not contradict this because it assumes the $\varepsilon_i$ are fixed once and for all and are not regenerated at every arithmetic step.

The practical consequence is the classical truncation–round-off trade-off: truncation error decreases like $h^2$ (or $h^4$ for Simpson), while round-off grows with the number of operations, so there is an optimal mesh size beyond which refinement degrades the result.

## 3. Formal Proofs, Derivations, and Methods

> **Theorem (Euler–Maclaurin Error Expansion).** If $f\in C^{2m+2}[a,b]$, then the composite trapezoidal rule satisfies



$$
> T(h) = I + c_1 h^2 + c_2 h^4 + \cdots + c_m h^{2m} + O(h^{2m+2}),
$$



> where $I=\int_a^b f(x)\,dx$ and the coefficients $c_k$ depend on $f$ and its derivatives at $a$ and $b$ but not on $h$.

This theorem is the theoretical justification for Romberg integration: the error contains only even powers of $h$, so each extrapolation step can eliminate one term exactly.

> **Theorem (Richardson Extrapolation).** Suppose $T(h) = I + c_1 h^2 + O(h^4)$. Then



$$
> \frac{4T(h/2) - T(h)}{3} = I + O(h^4).
$$



The proof is a direct algebraic cancellation: writing $T(h)=I+c_1h^2+O(h^4)$ and $T(h/2)=I+c_1h^2/4+O(h^4)$, the combination $\frac{4T(h/2)-T(h)}{3}$ removes the $c_1h^2$ term. This is precisely the first Romberg extrapolation $R_{2,2}$.

> **Theorem (Convergence of Romberg Integration).** Suppose $f\in C^{2k}[a,b]$. Then the diagonal entry $R_{k,k}$ satisfies



$$
> I - R_{k,k} = O\!\left(h^{2k}\right),
$$



> where $h$ is the step size of the coarsest trapezoidal approximation $R_{1,1}=T(h)$. More generally, for fixed $j$ the column $R_{k,j}$ converges to $I$ at the rate $O(h^{2j})$ as $k\to\infty$.

The order $O(h^{2k})$ is a statement about the leading term of the error expansion and requires the stated smoothness; for functions of limited smoothness the observed rate can be lower. The theorem does not assert that a column converges faster than every fixed power of $h$; it asserts a specific power rate for each column, improving by two powers of $h$ with each additional extrapolation.

> **Theorem (Error of Composite Simpson's Rule).** If $f\in C^4[a,b]$ and $n$ is even, then



$$
> \int_a^b f(x)\,dx - S_n = -\frac{(b-a)}{180}h^4 f^{(4)}(\xi)
$$



> for some $\xi\in(a,b)$.

The composite Simpson rule is closely related to the first Romberg extrapolation of the trapezoidal rule, but the correspondence must be stated with care. If $T(h)$ and $T(h/2)$ are the trapezoidal approximations with step sizes $h$ and $h/2$, then the Richardson combination



$$
\frac{4T(h/2)-T(h)}{3}
$$



equals the composite Simpson rule evaluated on the finer mesh of step $h/2$, that is, $S_{2n}$ with $n=(b-a)/h$. The identity requires the Simpson rule to use the finer step $h/2$; it does not hold if the Simpson rule is taken on the coarser mesh. In particular, when the trapezoidal values are built from a fixed table of nodes, the extrapolated value $R_{2,2}$ coincides with the composite Simpson value only when the table contains the nodes required by that Simpson rule. This is why the second column of the Romberg table is described as Simpson-type rather than as the composite Simpson rule itself.

## 4. Representative Worked Examples and Solutions
### Worked assessment: estimating pi with four doublings

Use the source integral



$$
\pi=\int_0^1\frac{4}{1+x^2}\,dx.
$$



Let T_n denote the composite trapezoidal estimate using n equal panels. Four doublings after the initial one-panel estimate use n=1,2,4,8,16. The corresponding values are



$$
\begin{aligned}
T_1&=3.0000000000, &T_2&=3.1000000000,\\
T_4&=3.1311764706, &T_8&=3.1389884945,\\
T_{16}&=3.1409416120.
\end{aligned}
$$



For the first extrapolation, use the formula with denominator 3:



$$
R_{1,1}=T_2+\frac{T_2-T_1}{3}=3.1000000000+\frac{0.1000000000}{3}=3.1333333333.
$$



The next adjacent pairs give R_{2,1}=3.1415686275, R_{3,1}=3.1415925025, and R_{4,1}=3.1415926512. To form the second column, the denominator is 4²−1=15. Its entries are 3.1421176471, 3.1415940941, and 3.1415926611. The third column uses 4³−1=63 and gives 3.1415857838 and 3.1415926384. The last entry uses 4⁴−1=255:



$$
R_{4,4}=R_{4,3}+\frac{R_{4,3}-R_{3,3}}{255}\approx3.1415926653.
$$



Thus the Romberg estimate rounds to 3.1415927, as in the module's answer. The exact pi is 3.141592653589…, so this example's actual difference is about 1.2×10⁻⁸. A full table should label its left edge as trapezoidal approximations and each subsequent column by the extrapolation order; the panel count and the column number mean different things.

The observed closeness to pi confirms this worked computation, but it does not prove that the Romberg table always supplies a rigorous error bound. In a new problem with no exact value, report the final diagonal and compare consecutive diagonal entries. Explain that this is a practical stabilization check, and state that a mathematical bound would need additional derivative information and verified hypotheses.

## 5. Mathematical Extensions, Limits, and Common Errors
**High-yield takeaways.**

- The composite trapezoidal rule is $T_n=\frac{h}{2}\left[f_0+2\sum_{i=1}^{n-1}f_i+f_n\right]$; the interior nodes carry weight $2$.
- The composite Simpson's rule is $S_n=\frac{h}{3}\left[f_0+4\sum_{\text{odd}}f_i+2\sum_{\text{even}}f_i+f_n\right]$; $n$ must be even.
- The trapezoidal error is $-\frac{(b-a)}{12}h^2f''(\xi)$; the Simpson error is $-\frac{(b-a)}{180}h^4f^{(4)}(\xi)$.
- Romberg extrapolation uses $R_{k,j}=R_{k,j-1}+\frac{R_{k,j-1}-R_{k-1,j-1}}{4^{j-1}-1}$; the first column is trapezoidal, the second is Simpson-type, the third is Boole-type.
- The Romberg table is built from top-left downward; each new row requires one new trapezoidal value at a halved step size.
- The propagated error in a weighted sum is bounded by $\sum_i\lvert w_i\rvert\lvert\varepsilon_i\rvert$; for the trapezoidal rule with uniform data error $\varepsilon$ it is $(b-a)\varepsilon$, independent of $n$.

**Common pitfalls.**

- Forgetting the factor $2$ on interior nodes in the trapezoidal rule, or misassigning the $4$ and $2$ weights in Simpson's rule.
- Using an odd number of subintervals with Simpson's rule; $n$ must be even.
- Confusing the step size $h$ with the number of subintervals $n$; always compute $h=(b-a)/n$ first.
- In Romberg integration, using the wrong denominator: the $j$-th column uses $4^{j-1}-1$, not $4^{j}-1$.
- Building the Romberg table in the wrong order; each entry $R_{k,j}$ depends on $R_{k,j-1}$ (same row, previous column) and $R_{k-1,j-1}$ (previous row, previous column).
- Assuming that more subdivisions always improve accuracy; round-off eventually dominates, and Romberg extrapolation can amplify data errors in deep columns.
- Reporting the trapezoidal value as the final answer when the question asks for Romberg improvement; always carry the extrapolation to the requested column.
- Omitting units or the interval of integration in the final statement of the integral's value.

### Error expansion and the logic of Richardson extrapolation

The composite trapezoidal rule can be derived panel by panel. On [x_i,x_{i+1}], replace f by its linear interpolant through the two endpoint values and integrate that line. The local area is h(f_i+f_{i+1})/2. Summation over all panels counts each interior ordinate twice and each endpoint once. This derivation explains the weights and makes clear that the compact formula assumes a uniform h. On a nonuniform partition, each panel must retain its own width; one cannot use a single common h without changing the rule.

For a sufficiently smooth integrand over a fixed interval, the global trapezoidal error has an expansion in even powers of h. The leading term is proportional to h squared, followed by terms proportional to h to the fourth power, h to the sixth power, and so on. If T(h)=I+c_2h^2+c_4h^4+…, then T(h/2)=I+c_2h^2/4+c_4h^4/16+…. Subtracting these expressions and forming a suitable linear combination removes c_2h^2. The first Romberg value is therefore more accurate in the asymptotic regime than either of its trapezoidal inputs.

Once the leading term has been removed, the next error term scales by one sixteenth when h is halved. A second extrapolation eliminates that term. Repeating the operation produces the triangular Romberg table. If R_{k,0}=T_{2^k}, where the subscript denotes the number of panels, the recurrence is



$$
\begin{aligned}
R_{k,j}&=R_{k,j-1}+\frac{R_{k,j-1}-R_{k-1,j-1}}{4^j-1},\\
k&\geq j,\qquad j=1,2,\ldots .
\end{aligned}
$$



The denominator belongs to the extrapolation column, not to the total row count. The first column uses three; the second uses fifteen; the third uses sixty-three. Some books use reversed superscript and subscript conventions, so an answer should define its notation before populating the array. This prevents a plausible-looking but misindexed table.

The formal gain in order is conditional. The smooth even-power expansion is useful when f has enough derivatives and the mesh sizes are in a regime where asymptotic behavior has begun. A discontinuity, singular endpoint, sharp boundary layer, noisy measurement, or heavily rounded table can make early rows misleading. A high-order label does not guarantee high accuracy for arbitrary inputs. In a rigorous analysis, state the smoothness assumptions and separate the extrapolation's truncation-error cancellation from errors already present in the function values.

### Recursive evaluation on nested meshes

The nested-grid property avoids recomputing every ordinate. Suppose T_n is based on n panels of width h_n=(b−a)/n. The refined grid has 2n panels of width h_n/2; it consists of all old nodes and n new midpoints. The sum of the old-node contributions is one half of T_n, while each new midpoint contributes h_n/2 times its function value. Thus



$$
T_{2n}=\frac12T_n+\frac{h_n}{2}\sum_{i=0}^{n-1}f\!\left(a+\left(i+\frac12\right)h_n\right).
$$



Equivalently, if h_{2n}=h_n/2, the coefficient on the midpoint sum is h_{2n}. Both forms are the same identity. The equation is an efficient way to build the left edge of the Romberg table; it is not a new integration method. Check that the midpoint sum has n terms, that the old endpoint values are retained, and that no newly inserted node is counted twice.

For hand computation, the direct composite formula is often clearer on the first few rows. For a program or a long table, recursive refinement saves evaluations. A robust calculation can compute the first row directly, then use the recurrence, while independently checking one refined row by direct summation. The mesh label should include n or h, since “row 3” alone says nothing about whether the estimate uses four or eight panels.

### Source assessment: estimating pi

The lesson's assessment estimates pi from 4/(1+x²) on [0,1]. Four doublings after the initial one-panel estimate use panel counts 1, 2, 4, 8, 16. The composite trapezoidal values are approximately



$$
\begin{aligned}
T_1&=3.0000000000, &T_2&=3.1000000000,\\
T_4&=3.1311764706, &T_8&=3.1389884945,\\
T_{16}&=3.1409416120.
\end{aligned}
$$



The first correction is



$$
R_{1,1}=T_2+\frac{T_2-T_1}{3}=3.1000000000+\frac{0.1000000000}{3}=3.1333333333.
$$



Continuing the first extrapolation column gives 3.1415686275, 3.1415925025, and 3.1415926512. Using denominator fifteen for the next column gives 3.1421176471, 3.1415940941, and 3.1415926611. The next denominator is sixty-three, and the final one is 255. The fourth extrapolation produces approximately 3.1415926653, which rounds to 3.1415927 and agrees with the module's answer. The exact value of pi is 3.1415926536…; the discrepancy in this known example is about 1.2×10⁻⁸.

This table is also a sign check. The first fine trapezoid exceeds the coarse one, so the first correction is positive. Reversing the difference while retaining the plus sign would give a value below 3.1 and contradict the computed change. Later entries need not move monotonically because the extrapolations remove successive error terms whose coefficients can have different signs. Use the recurrence rather than assuming a direction.

### Interpreting error and selecting a method

If an exact integral I is available, the actual absolute error of a computed estimate Q is |I−Q| and the relative error is |I−Q|/|I| when I is nonzero. These definitions describe the observed error; they do not supply a bound unless I is known. When the exact answer is unavailable, the difference between adjacent diagonal values is a practical convergence indicator. It can be a sensible stopping rule when combined with a maximum iteration count and a check for stable behavior, but it is not a theorem guaranteeing that the true error is no larger than that difference.

Composite trapezoidal integration is a transparent choice when the function is tabulated on equally spaced nodes, a low-cost baseline is needed, or nested refinement is convenient. Romberg is more attractive when repeated evaluations are possible and f is smooth enough for the error expansion to be informative. For a nonsmooth or noisy integrand, the extrapolation can amplify uncertainty or mistake a pre-asymptotic sequence for convergence. A practical decision therefore considers smoothness, available nodes, function-evaluation cost, and input precision—not simply which formula has the highest formal order.

In a written solution, separate evidence from assurance. Give panel counts and step sizes; show the trapezoidal sequence; state the recurrence and its denominators; identify the final diagonal value; and describe how the diagonal changes. If the task requests an accuracy comment, report an exact comparison when available. Otherwise, state that the computed entries stabilize and explicitly call the diagonal difference an indicator. This makes the conclusion reproducible without claiming more than the numerical evidence supports.

### Separating discretization error from input uncertainty

Romberg extrapolation targets discretization error: the difference between the exact integral of the represented function and the composite trapezoidal approximation on a finite mesh. It does not remove error in the ordinates themselves. If each f(x_i) is a measured or rounded value, the quadrature sum is a weighted combination of those uncertainties. The signed cancellations that are useful for truncation error can also magnify uncertainty when extrapolated entries are formed. Consequently, the observed stabilization of a Romberg diagonal is persuasive only when the function values are substantially more accurate than the requested integral tolerance.

This distinction is especially important when the table values are given to a limited number of decimal places. Carry guard digits through the arithmetic, but do not interpret guard digits as new measurement information. If the integral is evaluated from an analytic function, the values can be recomputed at higher precision. If they are supplied measurements, reducing h further may produce no trustworthy improvement. The relevant method choice depends not only on formal order but also on the quality and repeatability of function evaluation.

### A structured exam response

A full answer can be organized in a short reproducible sequence. First identify [a,b], n, h, and the nodes. Next state the composite trapezoidal formula and show the values or sum used. Then add the next mesh level by halving h, rather than inventing unrelated ordinates. Build the extrapolation triangle using the factor 4^j−1 for column j. Finally give the last available diagonal value and a measured comment on its stability. If the problem provides an exact answer, compare against it; otherwise label the diagonal difference as a practical indicator.

For the source example estimating pi, the initial panel counts 1, 2, 4, 8, 16 give a coherent left edge. Four doublings produce the final estimate approximately 3.1415926653, which rounds to the printed answer 3.1415927. Retaining enough digits is essential because the extrapolation subtracts close estimates. If each row is rounded too aggressively before the next correction, the small difference can be dominated by arithmetic rounding and the final digit becomes unreliable.

### Diagnosing an unexpected table

If the first column does not approach a stable region, inspect whether the integrand is sufficiently smooth, whether the grid resolves a rapid change, and whether endpoints or midpoints have been entered correctly. If the first column looks plausible but the extrapolation column suddenly diverges, check the sign and denominator in the recurrence. The second column uses 15, not 3; the third uses 63. A missing row changes the pair of estimates and invalidates every subsequent entry.

A table with tiny differences can also be misleading. A rounded function table may cause repeated values, while cancellation may make two successive estimates close even though their common bias remains. Compare more than one diagonal transition where possible, and use any exact value, derivative information, or independent method that the problem supplies. Do not equate decimal agreement with a proof of accuracy.

### Accuracy comments that respect what the table can prove

Numerical analysis separates a computed approximation from a guarantee about its error. The Romberg table supplies a sequence of values. When the diagonal stabilizes, this is practical evidence that further refinement is changing the result only slightly. It is not, on its own, a rigorous upper bound on the difference from the exact integral. A bound needs more information, such as a derivative estimate together with an applicable error theorem. This distinction should be stated whenever a problem asks for a comment rather than supplying a known answer.

In the pi assessment, the exact integral is known. The final diagonal value 3.1415926653 differs from 3.1415926536… by about 1.2×10⁻⁸. This actual error is a property of that particular function, interval, and number of refinements. It is not inferred solely from the difference between two diagonal values. For the source logarithm example, ln 2 is likewise available for an after-the-fact check. If neither exact value is known, do not manufacture one; compare consecutive diagonal entries and call their difference an empirical indicator.

Precision of the input also matters. If f(x_i) is rounded, the quadrature result combines these rounded values with nonnegative trapezoidal weights. Increasing n may reduce discretization error while simultaneously increasing the number of approximate ordinates. Romberg's linear combinations can magnify the effect of those input uncertainties. A table whose entries are reported to three decimal places cannot support a claim of ten accurate digits merely because the recurrence prints them.

### When to refine and when to change the plan

Mesh refinement is sensible when a smooth function is under-resolved and additional evaluations are affordable. Romberg is especially effective when the trapezoidal error follows its expected even-power expansion over the available mesh widths. If the first two diagonal entries change substantially, another refinement can be useful. If they stop improving, test the arithmetic, inspect whether the integrand has a kink or endpoint feature, and check whether input rounding has become dominant.

The composite trapezoidal rule remains a useful baseline for irregular behavior because it is easy to interpret panel by panel. Romberg's extrapolation assumes more structure than the trapezoidal rule itself. A singularity or discontinuity can violate that structure, and a noisy table can cause the corrections to chase noise. In those cases, subdivide at known discontinuities, transform the interval only when the change of variables is justified, or choose another quadrature family. Blindly increasing the Romberg order is not a substitute for diagnosing the integrand.

An exam response can earn a clear accuracy conclusion with three facts: the final diagonal estimate, the change from the preceding diagonal value, and the known exact value if the exercise provides one. Add a sentence about assumptions. For an unknown integral, say that the diagonal appears stable to the shown precision, not that the true error is proved to be below the diagonal difference. Such wording is mathematically careful and still answers the question directly.

### Mesh interpretation for non-unit intervals

The examples in the module use intervals of width one, but the bookkeeping is unchanged on any [a,b]. With n panels, h=(b−a)/n and x_i=a+ih. On a longer interval, halving h doubles n while leaving a and b fixed. A frequent mistake is to halve the endpoint interval or to retain the old h after doubling the panel count. The node formula and the equality nh=b−a detect both mistakes immediately.

The composite trapezoidal sum is an approximation to an integral, so its scale should reflect both the ordinate and the interval width. If f is multiplied by a constant c, every trapezoidal and Romberg value is multiplied by c. If the interval is shortened, the area usually changes accordingly. These simple invariance checks help catch errors in weights, factors of h, and interval transformations.

When intervals are subdivided at a known feature, each subinterval can be integrated separately and the results added. This is often more defensible than asking a single uniform grid to straddle a jump or sharp corner. The smooth error expansion underlying Romberg should be assessed on each smooth piece; it should not be assumed across a discontinuity. This practical observation connects method selection to the shape of the actual integrand rather than to a formula alone.

### Why the weights and error scaling must be kept separate

Two different sets of weights occur in a Romberg computation. The trapezoidal weights arise from integrating the piecewise-linear interpolant and assign half contributions to the two endpoints of the interval and full contributions to interior grid points. The extrapolation coefficients arise from canceling the mesh-error expansion and depend on the Romberg column. Confusing these layers can lead to incorrect sums: first compute a valid trapezoidal value, then combine those valid values with the extrapolation recurrence.

The factor four in the error scaling comes from h² when the mesh is halved. It is not the factor by which the number of function evaluations grows. Panel counts double, while the leading error quarters. Later powers follow from the remaining error terms. This conceptual separation is helpful both for derivations and for checking code: panel recursion handles function values; extrapolation handles already computed quadrature approximations.