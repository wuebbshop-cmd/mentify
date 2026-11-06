## 1. Foundational Concepts, Definitions, and Axioms

Quadrature methods are the numerical techniques used to approximate the value of a definite integral when an exact antiderivative is unavailable or inconvenient. The word "quadrature" historically referred to the construction of a square with area equal to a given figure; in modern numerical analysis it denotes the approximation of $\int_a^b f(x)\,dx$ by a finite weighted sum of function values.

The central idea is to replace the integrand $f$ by a simpler function — typically a polynomial interpolant — whose integral can be evaluated exactly, and then to use that integral as an estimate of the true integral. The error of a quadrature rule is therefore the difference between the exact integral and the weighted sum, and the study of quadrature is inseparable from the study of the errors introduced by this replacement.

Two distinct error concepts recur throughout the topic:

- The **local (truncation) error** of a single application of a rule on a subinterval, which measures how well the rule reproduces the integral of a smooth function on that subinterval.
- The **global (accumulated) error** of a composite rule, which is the total error obtained when the interval $[a,b]$ is subdivided and the rule is applied repeatedly.

Because quadrature is a numerical computation, the errors already studied in earlier lessons — round-off error, truncation error, absolute error, relative error, and propagated error — all interact with the quadrature error. A rule with a small truncation error may still deliver a poor result if the function values themselves carry propagated errors from earlier arithmetic, and a composite rule with many subintervals may accumulate round-off error even as its truncation error decreases.

The intuition behind the standard rules is geometric. The trapezoidal rule replaces the integrand on each subinterval by the straight chord joining the endpoint values, so the approximating region is a trapezium. Simpson's rule replaces the integrand on each pair of subintervals by the parabola through three equally spaced points, so the approximating region is bounded by parabolic arcs. Higher-order Newton–Cotes rules use higher-degree interpolating polynomials through equally spaced nodes. Gaussian quadrature instead chooses the nodes optimally so that a rule with $n$ nodes integrates polynomials of degree up to $2n-1$ exactly.

The practical workflow of quadrature is therefore: choose a rule appropriate to the smoothness of $f$; subdivide the interval if higher accuracy is required; compute the weighted sum; and estimate the error, either from the truncation-error formula or by comparing successive refinements (as in Romberg integration, which exploits the structure of the composite trapezoidal error to extrapolate to higher accuracy).

## 2. Theorems, Lemmas, and Analytical Properties

> **Definition (Quadrature Rule).** Let $f$ be a real-valued function on $[a,b]$. A quadrature rule with nodes $x_0,x_1,\dots,x_n \in [a,b]$ and weights $w_0,w_1,\dots,w_n \in \mathbb{R}$ is an approximation of the form



$$
\int_a^b f(x)\,dx \approx \sum_{i=0}^{n} w_i f(x_i).
$$



> The nodes and weights are fixed numbers determined by the rule and do not depend on $f$.

> **Definition (Degree of Precision / Degree of Exactness).** A quadrature rule has degree of precision $m$ if it integrates exactly every polynomial of degree at most $m$, and fails to integrate exactly at least one polynomial of degree $m+1$. Equivalently,



$$
\int_a^b p(x)\,dx = \sum_{i=0}^{n} w_i p(x_i)
$$



> for every polynomial $p$ with $\deg p \le m$.

> **Definition (Local Truncation Error).** For a quadrature rule applied on $[a,b]$, the local truncation error is



$$
E(f) = \int_a^b f(x)\,dx - \sum_{i=0}^{n} w_i f(x_i).
$$



> **Definition (Composite Quadrature Rule).** Let $[a,b]$ be divided into $N$ subintervals by the points $a = x_0 < x_1 < \dots < x_N = b$, with $h = (b-a)/N$. A composite rule applies a basic rule on each subinterval $[x_{j-1},x_j]$ and sums the results:



$$
\int_a^b f(x)\,dx \approx \sum_{j=1}^{N} \left( \text{basic rule applied on } [x_{j-1},x_j] \right).
$$



> **Definition (Propagated Error).** Let $x$ and $y$ be exact numbers and let $x^{*}$ and $y^{*}$ be approximations with initial errors $\varepsilon$ and $\eta$ respectively, so that



$$
x = x^{*} + \varepsilon, \qquad y = y^{*} + \eta.
$$



> For an arithmetic operation $\omega$, the error in the result arising from the initial errors is called the **propagated error**, and the total cumulative error at any step of a procedure is called the **accumulated error**.

> **Definition (Absolute, Relative and Percentage Error).** Let $x_r$ be an approximation to an exact number $x$. The absolute error is



$$
e_{\text{abs}} = \lvert x - x_r \rvert,
$$



> and if $\Delta x$ is an upper bound with $e_{\text{abs}} = \lvert x - x_r \rvert \le \Delta x$, then $\Delta x$ is the error bound. The relative error is



$$
e_r = \frac{\lvert x - x_r \rvert}{\lvert x \rvert},
$$



> and the percentage error is $100\, e_r$.

> **Definition (Round-off and Truncation Error).** Round-off error arises because it is impossible to represent all real numbers exactly on a machine with finite memory; it involves dropping decimal places or significant figures, and may be performed by chopping (truncating) or by symmetric rounding. Truncation error is the error committed when an infinite or limiting process is replaced by a finite one, as when a series is cut off after finitely many terms.

> **Definition (Standard Quadrature Rules).** On the interval $[a,b]$ with $h = b-a$, the trapezoidal rule and Simpson's rule are



$$
\int_a^b f(x)\,dx \approx \frac{h}{2}\bigl[f(a) + f(b)\bigr],
$$





$$
\int_a^b f(x)\,dx \approx \frac{h}{6}\left[f(a) + 4f\!\left(\frac{a+b}{2}\right) + f(b)\right].
$$



> **Definition (Composite Trapezoidal and Composite Simpson Rules).** With $h = (b-a)/N$ and $x_j = a + jh$,



$$
T_N = \frac{h}{2}\left[f(x_0) + 2\sum_{j=1}^{N-1} f(x_j) + f(x_N)\right],
$$



> and, when $N$ is even,



$$
S_N = \frac{h}{3}\left[f(x_0) + 4\sum_{j \text{ odd}} f(x_j) + 2\sum_{j \text{ even},\, j \ne 0,N} f(x_j) + f(x_N)\right].
$$



### Key Words in the Definition of Error

In point form, the key words in the definition of error are:

- **Exact number** $x$: the true, unknowable value being approximated.
- **Approximate number** $x_r$: the computed or representable value.
- **Difference**: error is measured as a difference, not as a ratio.
- **Absolute value**: the sign of the difference is discarded, so error is non-negative.
- **Upper bound** $\Delta x$: a guaranteed ceiling on the magnitude of the error.
- **Relative**: the error scaled by the size of the exact quantity.
- **Percentage**: the relative error expressed on a scale of one hundred.
- **Propagated**: error transmitted from inputs to the output of an operation.
- **Accumulated**: error summed over the steps of a procedure.
- **Round-off**: error from finite representation.
- **Truncation**: error from replacing an infinite process by a finite one.

### Causes of Errors and How to Avoid Them

Short notes on the causes of errors and the measures used to avoid them:

- **Finite machine representation.** Real numbers generally cannot be stored exactly, so round-off error is unavoidable. It is minimized by working with higher precision, by avoiding subtraction of nearly equal numbers, and by arranging computations so that small quantities are not multiplied by large ones.
- **Chopping versus symmetric rounding.** Chopping discards trailing digits and biases results downward in magnitude; symmetric rounding to the nearest representable value reduces the bias and is preferred.
- **Loss of significance (cancellation).** Subtracting two nearly equal numbers destroys significant figures. It is avoided by algebraic rearrangement, for example replacing a difference of nearly equal quantities by an equivalent product or quotient form.
- **Truncation of infinite processes.** Replacing a series or limit by finitely many terms introduces truncation error. It is controlled by retaining more terms or by using a remainder estimate.
- **Propagation through arithmetic.** Errors in inputs are transmitted to outputs; the propagated error must be estimated and, where possible, the operation reordered to reduce amplification.
- **Accumulation over many steps.** Repeated operations accumulate error; it is controlled by limiting the number of steps, by using stable composite formulas, and by monitoring successive refinements.
- **Data error.** The input data themselves may be inexact; no numerical method can recover information absent from the data, so the conditioning of the problem must be assessed.

### Encouraging Participation, Feedback and Summarising

The lesson is conducted as an interactive session in which learners attempt the tasks and post their answers for peer review. The moderator directs the group discussion, encourages the participation of all learners, provides feedback on the posted attempts, and summarises the lesson at the close. Learners study the posts of their colleagues, note anything new, and improve their own answers accordingly. The lesson is scheduled for two hours, and the next topic is propagated errors.

## 3. Formal Proofs, Derivations, and Methods
### Constructing the three-point rule by moments and orthogonality

The source's Gaussian quadrature theorem can be understood in two connected ways. The direct calculation determines unknown nodes and weights by matching moments; the orthogonality argument explains why an n-point Gaussian rule reaches degree 2n−1. On [−1,1], symmetry suggests three nodes −r,0,r and weights A,B,A. Exactness for 1, x², and x⁴ gives

$$
2A+B=2,\qquad 2Ar^2=\frac23,\qquad 2Ar^4=\frac25.
$$

Dividing the last relation by the second gives r²=3/5, and back-substitution yields A=5/9 and B=8/9. Odd moments vanish on both sides by symmetry. Thus the rule is exact through degree five, not merely through degree two, because the even moments through degree four and all intervening odd moments agree.

For a general n-node Gaussian rule, let q_n be a degree-n polynomial orthogonal on the interval to every polynomial of degree at most n−1. Its n roots are the quadrature nodes. To see the exactness, divide any polynomial p of degree at most 2n−1 by q_n:

$$
p(x)=q_n(x)s(x)+r(x),\qquad \deg s\le n-1,\quad \deg r\le n-1.
$$

Orthogonality makes the integral of q_ns vanish. At every Gaussian node x_i, q_n(x_i)=0, so the quadrature sum of q_ns also vanishes. The remainder r has degree at most n−1 and is integrated exactly by the interpolatory rule determined by the nodes and weights. Therefore the quadrature and the true integral agree for p. This decomposition is the core reason Gaussian quadrature doubles the exactness degree relative to a simple “n conditions for n weights” intuition.

For Legendre weight one on [−1,1], the degree-three orthogonal polynomial is proportional to 5x³−3x. Its roots are 0 and ±√(3/5), matching the moment derivation. The corresponding Lagrange basis polynomials integrate to 5/9, 8/9, 5/9. This second route explains the general theorem while the moment equations are usually quicker when a three-point rule must be derived by hand.

### Mapping the reference rule to a general interval

A tabulated Gauss–Legendre rule on [−1,1] is transferred to [a,b] using the linear map x=c+dt, where c=(a+b)/2 and d=(b−a)/2. Then dx=d dt, and the integral becomes

$$
\int_a^b f(x)\,dx=d\int_{-1}^{1}f(c+dt)\,dt
\approx d\sum_{i=1}^{n}A_i f(c+dt_i).
$$

The factor d multiplies the weighted sum; omitting it is a common scaling error. The transformed nodes are x_i=c+dt_i and remain inside [a,b]. For a reversed interval, d is negative and the signed integral changes orientation consistently.

For example, on [0,1], c=d=1/2. The three nodes become (1−√(3/5))/2, 1/2, and (1+√(3/5))/2. Applying the reference weights requires one function evaluation at each of these nonuniform points, then multiplication of the weighted sum by one half. This transformed form is preferable to re-deriving a new rule on every interval.

## 4. Representative Worked Examples and Solutions
### Worked source exercise: Gauss–Legendre approximation of x^6

On [−1,1], the three-point nodes are −r,0,r with r=√(3/5), and the weights are 5/9,8/9,5/9. For x^6, symmetry makes the two outer contributions equal and the central contribution vanishes:

$$
\begin{aligned}
Q_3[x^6]&=\frac59(-r)^6+\frac89(0)^6+\frac59r^6\\
&=\frac{10}{9}\left(\frac35\right)^3=\frac{6}{25}=0.24.
\end{aligned}
$$

The exact value is

$$
\int_{-1}^{1}x^6\,dx=\left[\frac{x^7}{7}\right]_{-1}^{1}=\frac27\approx0.2857142857.
$$

The absolute error is 2/7−6/25=8/175≈0.0457143, the value given for this exercise. This is a deliberate degree-of-precision test. The theorem guarantees exactness through degree five, not six. For x^4, in contrast, both the exact integral and the Gaussian result are 2/5.

### Worked interval transformation: integrate e^x on [0,1]

Let c=d=1/2 and map t∈[−1,1] to x=c+dt=(1+t)/2. Then dx=dt/2, and the transformed three-point formula is

$$
Q=\frac12\left[\frac59e^{(1-\sqrt{3/5})/2}+\frac89e^{1/2}+\frac59e^{(1+\sqrt{3/5})/2}\right].
$$

The evaluations give Q≈1.7182810044. Since the exact integral equals e−1≈1.7182818285, the absolute difference is approximately 8.24×10⁻⁷. The smooth exponential is approximated well by the rule but is not exactly integrated by the degree-five polynomial guarantee. A sound answer reports the method's exactness class and the observed error separately.

## 5. Mathematical Extensions, Limits, and Common Errors
### High-Yield Takeaways

- **Definition of a quadrature rule.** A quadrature rule is a weighted sum $\sum w_i f(x_i)$ approximating $\int_a^b f(x)\,dx$; the nodes and weights are fixed in advance and do not depend on $f$.
- **Degree of precision.** The trapezoidal rule is exact for polynomials of degree at most $1$; Simpson's rule is exact for polynomials of degree at most $3$. This is the fastest way to check a rule or to construct one.
- **Error orders.** The local trapezoidal error is $O(h^3)$ and the composite error is $O(h^2)$; the local Simpson error is $O(h^5)$ and the composite error is $O(h^4)$. Halving $h$ reduces the composite trapezoidal error by a factor of about $4$ and the composite Simpson error by a factor of about $16$.
- **Error constants.** The composite trapezoidal error carries the factor $-(b-a)h^2/12$ multiplying $f''(\xi)$; the composite Simpson error carries $-(b-a)h^4/180$ multiplying $f^{(4)}(\xi)$.
- **Richardson extrapolation.** The combination $(4T_{2N} - T_N)/3$ cancels the leading $h^2$ error term and yields a Simpson-type estimate; iterating this idea produces the Romberg table with entries $R_{k,j} = R_{k,j-1} + (R_{k,j-1} - R_{k-1,j-1})/(4^j - 1)$.
- **Propagated error in a weighted sum.** For weights $w_i$ and function-value errors bounded by $\delta$, the error in the quadrature sum is bounded by $\delta \sum_i \lvert w_i \rvert$. For the composite trapezoidal rule this is $(b-a)\delta$, and for the composite Simpson rule it is $\tfrac{2}{3}(b-a)\delta$.
- **Correctly rounded numbers.** A number correct to $n$ decimal places has absolute error at most $0.5 \times 10^{-n}$; this is the standard bound used when assessing the input error of tabulated function values.
- **Relative versus absolute error.** The relative error $\lvert x - x_r \rvert / \lvert x \rvert$ is the appropriate measure when comparing approximations of quantities of different magnitudes; the percentage error is $100$ times the relative error.
- **Error budget.** The total error of a quadrature computation is the sum of truncation error, propagated input error, and accumulated round-off error. The dominant term determines the strategy: refine the mesh if truncation dominates, increase precision if round-off dominates.

### Common Pitfalls

- **Applying Simpson's rule with an odd number of subintervals.** The composite Simpson rule requires $N$ even; with $N$ odd the pairing of subintervals fails and the formula is invalid.
- **Confusing local and composite error orders.** The local trapezoidal error is $O(h^3)$ but the composite error is $O(h^2)$; quoting the wrong order is a frequent source of lost marks.
- **Forgetting the factor $h/2$ versus $h/3$.** The trapezoidal rule uses $h/2$ and Simpson's rule uses $h/3$; these factors are not interchangeable.
- **Using the wrong derivative in the error formula.** The trapezoidal error involves $f''$ and the Simpson error involves $f^{(4)}$; substituting $f'$ or $f'''$ invalidates the bound.
- **Ignoring the sign of the error term.** The error formulas carry a negative sign, so the true integral is less than the trapezoidal estimate when $f'' > 0$ on the interval; the sign indicates the direction of the error, not its magnitude.
- **Assuming that more nodes always means more accuracy.** Beyond a certain point, round-off and accumulated error can dominate, particularly with high-order Newton–Cotes rules on equally spaced nodes.
- **Neglectingthe propagated error in the inputs.** A quadrature sum is only as accurate as the function values it uses; if the tabulated values carry errors of order $10^{-3}$, no amount of mesh refinement will produce a result accurate to $10^{-6}$.

- **Treating the error bound as the actual error.** The formulas give upper bounds involving an unknown point $\xi$; the true error is generally smaller, and the bound should be reported as a guarantee, not as an exact value.
- **Misapplying the propagation rule for division.** The propagated error in $x/y$ is $\bigl(y^{*}\varepsilon - x^{*}\eta\bigr)/\bigl(y^{*}(y^{*}+\eta)\bigr)$, not $\varepsilon/\eta$; the denominator involves the full approximate value, not the error.
- **Dropping the cross term in multiplication.** The propagated error in $xy$ includes the term $\varepsilon\eta$; it is usually negligible but must be acknowledged when a rigorous bound is required.
- **Confusing chopping with symmetric rounding.** Chopping biases results systematically in one direction, whereas symmetric rounding is unbiased; the bound $0.5 \times 10^{-n}$ applies to symmetric rounding, not to chopping.
- **Overlooking cancellation.** Subtracting nearly equal function values in a quadrature sum can destroy significant figures; the propagated-error analysis must account for the actual magnitudes involved, not merely the nominal precision.
- **Reporting too many significant figures.** A result computed from data accurate to six decimal places cannot legitimately be quoted to ten; the number of significant figures in the answer must be consistent with the error bound.
- **Forgetting to state the interval of the error point.** The error formulas assert the existence of some $\xi \in (a,b)$; the bound is obtained by maximising the relevant derivative over $[a,b]$, and omitting this maximisation step leaves the estimate unjustified.

### Degree of precision and what it does not say

A quadrature rule's degree of precision is the largest integer m for which it integrates every polynomial of degree at most m exactly. This is stronger than testing one polynomial: every linear combination of the basis monomials through degree m is then exact by linearity. The n-point Gauss–Legendre rule has degree 2n−1, so the three-point rule has degree five. Its exactness is a structural property of the chosen nodes and weights, not a result of using a very fine mesh.

Degree of precision must be distinguished from an error bound on a general function. For a non-polynomial f, the output depends on how well its behavior is represented by the sampled values and the rule's implied polynomial approximation. A smooth exponential may be accurate even though it is not integrated exactly; a polynomial just beyond degree five may show a more visible error. The exactness theorem alone does not provide the error for either case. Avoid statements such as “three points give six correct digits” unless a separate estimate establishes them.

The three-point rule's moments provide a diagnostic. For constants, the weighted sum is 2. For x² it is 2/3, and for x⁴ it is 2/5. Odd powers have zero integral and cancel because the nodes and weights are symmetric. These moment checks validate the node/weight table and are more reliable than memorizing decimals. They also reveal that the center point cannot be assigned the same weight as the outer nodes: doing so would fail the constant and second-moment equations.

### Source example beyond the exactness range

For f(x)=x^6 on [−1,1], the exact integral is 2/7. The three-point formula uses the two outer nodes whose sixth powers are (3/5)^3=27/125; the center term is zero. Therefore

$$
Q_3[x^6]=\frac59\frac{27}{125}+\frac89(0)+\frac59\frac{27}{125}=\frac{6}{25}=0.24.
$$

The exact value 2/7 is approximately 0.285714, so the error is about 0.0457143. This agrees with the lesson's listed value 0.045714285. The discrepancy is expected: x^6 has degree six, one more than the exactness limit of five. It would be a mistake to call the Gaussian rule inaccurate merely because this polynomial lies outside its guarantee; the example illustrates precisely where the guarantee ends.

By contrast, for x^4 the exact integral and Gaussian sum are both 2/5. This contrast is a useful verification pair: the method matches a degree-four polynomial and does not have to match a degree-six polynomial. In either case, the comparison should be based on the exact integral rather than on a vague statement that the result “looks close.”

### Comparison with equally spaced Newton–Cotes rules

The source distinguishes Newton–Cotes formulas, which use equally spaced nodes, from Gaussian quadrature, which chooses nodes and weights to achieve high exactness. Composite trapezoidal and Simpson formulas are especially convenient when values are already tabulated on a uniform grid. A Gaussian rule is attractive when the function can be evaluated at its nonuniform nodes and a high polynomial degree of precision per evaluation is useful.

These methods answer the same broad question—approximating a definite integral—but have different data requirements. Do not apply a Gauss–Legendre weight table to arbitrary equally spaced table entries; first map the reference nodes and obtain values at those points. Conversely, do not claim Gaussian quadrature is automatically superior when only fixed-grid observations are available. Method choice must fit both the integrand and the permitted evaluations.


### How many nodes should be used?

The theorem gives a direct relation between node count and polynomial precision: n Gaussian nodes integrate degree at most 2n−1 exactly. This helps estimate how many nodes may be useful when the integrand is well represented by a low-degree polynomial. For the source's three-node rule, the guaranteed degree is five. Increasing n raises the guaranteed polynomial degree, but the theorem does not say that the error for every non-polynomial function decreases monotonically at each increase.

Method selection should begin with the data and the integrand. If f can be evaluated at Gaussian nodes and is smooth, an n-point rule may achieve high accuracy with few evaluations. If values are supplied at equally spaced points, a Newton–Cotes formula uses those observations directly. If f varies sharply in part of the interval, composite application on subintervals can resolve the feature; simply using more global nodes may not be the best choice. Computation cost, node availability, smoothness, and requested precision all matter.

### Numerical error and reproducible reporting

A Gaussian approximation has two kinds of numerical uncertainty. Truncation error comes from replacing the integral by the weighted sample sum. Evaluation and rounding error comes from approximating f(x_i) and forming the weighted sum in finite arithmetic. The polynomial exactness theorem addresses the first type only for a specified class; it does not remove arithmetic error or errors in supplied measurements.

For a known exact integral I, report absolute error |I−Q| and, when I is nonzero, relative error |I−Q|/|I|. If I is unknown, do not invent an exact comparison. Report the quadrature rule, node count, transformed nodes, weights, and an independent comparison or refinement if available. Keep intermediate digits during calculation and round the final number to a precision consistent with inputs.

### Exactness checks by moments

The three-point moment equations provide an efficient verification checklist. The weights must satisfy A_1+A_2+A_3=2; symmetry gives A_1=A_3; the second moment must equal 2/3; and the fourth moment must equal 2/5. These conditions yield the familiar nodes and weights. Odd moments vanish because the interval and rule are symmetric. A table copied from a reference can therefore be checked without evaluating a complicated test function.

If the weights sum to something other than two, the constant integral fails. If the second moment fails, a scaling or node error has occurred. If the x^4 moment fails, the rule does not have the stated degree-five precision. Testing moments isolates the source of a mistake more effectively than checking only one unrelated integral.


### Interpreting polynomial exactness with a basis argument

The degree-five conclusion can be verified without testing every possible polynomial separately. Every polynomial p of degree at most five has a unique representation

$$
p(x)=c_0+c_1x+c_2x^2+c_3x^3+c_4x^4+c_5x^5.
$$

Integration and the quadrature sum are linear operations. It is therefore sufficient to check that they agree on the six monomials 1,x,x²,x³,x⁴,x⁵. The three-point Legendre rule matches the even moments 1,x²,x⁴ through its moment equations; symmetry makes both the integral and rule vanish for x,x³,x⁵. Agreement on a basis proves agreement for every linear combination, hence for every polynomial in the degree range.

This reasoning also explains why an example with a single polynomial is not a proof of degree of precision. Checking x^4 confirms one moment. It does not establish exactness for every polynomial up to that degree unless the remaining basis elements have also been considered or a general theorem has been invoked. The orthogonality proof supplies that theorem for n nodes and degree at most 2n−1.

The three-point rule provides a vivid counterexample outside the range. For x^6, the quadrature value is 6/25 whereas the exact integral is 2/7. Thus degree five is the highest guaranteed degree; exactness on a particular higher-degree polynomial could occur accidentally, but cannot be asserted for all degree-six polynomials. Precision is a universal guarantee within a vector space, not a claim that every function outside it must fail.

### Relation between interpolatory and Gaussian construction

Given n distinct nodes, one can form the degree-(n−1) Lagrange interpolating polynomial through the sampled values and integrate that polynomial. The resulting interpolatory rule has weights obtained by integrating the Lagrange basis. Because interpolation reproduces all polynomials through degree n−1, the rule is exact at least through that degree. If the nodes are arbitrary, one should not expect the degree to double.

Gaussian quadrature changes the nodes as well as the weights. Choosing them as the zeros of an appropriate orthogonal polynomial makes the rule exact to degree 2n−1. The polynomial-division proof shows exactly where this improvement enters: the part divisible by q_n has zero integral by orthogonality and zero quadrature contribution because q_n vanishes at every node. The remaining polynomial has degree below n and is already handled by interpolation. The extra exactness is therefore a consequence of a coordinated node-and-weight construction.

For n=3 and Legendre weight one, P_3(x)=(5x³−3x)/2. Its roots are 0 and ±√(3/5). The root polynomial is orthogonal to lower-degree polynomials, and its roots lead to the same nodes obtained by the symmetric moment equations. The orthogonal-polynomial route generalizes; the symmetric equations are an efficient concrete derivation for this low-order case.

### Change of variable as a linear functional

The affine map is more than a device for moving points. It transforms both the limits and the differential. With x=c+dt, the endpoints t=−1 and t=1 map to a and b, while dx=d dt. Thus

$$
\int_a^b f(x)\,dx=d\int_{-1}^{1}f(c+dt)\,dt.
$$

Applying the reference rule to the transformed integrand produces the mapped nodes and the shared factor d. The same derivation works for any panel, which is why the composite method can reuse a single table. Omitting d changes the units and scales the constant integral incorrectly; using b−a instead of d doubles the result.

In a partition a=x_0<x_1<\cdots<x_m=b, panel j has midpoint c_j=(x_{j-1}+x_j)/2 and half-width d_j=(x_j−x_{j-1})/2. Its three mapped points are c_j−d_jr,c_j,c_j+d_jr. The composite estimate is the sum over panels of d_j times each panel's weighted values. Writing the panel index prevents accidental reuse of the global midpoint or width.

If every panel is a uniform width h, then d_j=h/2 for all j. This may simplify the outer scale, but the evaluation points are still Gaussian interior points within each panel, not the uniform grid endpoints. The total computation cost and sample pattern should be described accordingly. A function's values at panel boundaries are not required by the three-point Gauss rule unless they coincide with one of its interior nodes, which generally they do not.

### Building a defensible accuracy statement

There are three distinct statements that are often confused. “The rule is exact for degree at most five” is a theorem about polynomials in exact arithmetic. “This computed value differs from a known integral by a certain amount” is an error measurement for one problem. “The error is guaranteed below a tolerance” requires a valid error bound and verified hypotheses. The first statement alone does not imply the third.

For the exponential example, the antiderivative gives an exact reference, so the absolute error can be computed as |(e−1)−Q|. A relative error may also be reported because the integral is nonzero. When no exact reference exists, repeating the calculation on smaller panels or comparing different orders can reveal sensitivity. However, agreement between two approximations is not a formal guarantee unless a convergence or error theorem is used.

Function evaluation may itself be rounded or noisy. If the sampled ordinates have errors, the quadrature sum reflects weighted versions of those errors. Increasing the formal polynomial precision cannot undo inaccurate input values. This is especially important when measurements rather than analytic function evaluations are used. State whether the values are exact, rounded, or measured if that information affects interpretation.

### Selecting between global and composite application

A global Gaussian rule puts all its nodes across the full interval. It is efficient for sufficiently smooth integrands whose values can be evaluated at those locations. Composite application localizes the approximation by dividing the interval; this is useful when behavior varies across the domain, because each subinterval receives its own midpoint and nodes. Subdivision also increases evaluation cost, so it should be guided by the desired accuracy and observed behavior rather than applied blindly.

Newton–Cotes methods retain an important practical advantage: their equally spaced nodes fit common tables and can be repeated over a uniform partition. Gaussian quadrature offers more polynomial precision per node but demands nonuniform evaluations. The right comparison therefore includes data access, smoothness, computational cost, and the required result quality. No universal ranking follows from degree of precision alone.

