## 1. Foundational Concepts, Definitions, and Axioms

Quadrature methods are the numerical techniques used to approximate the value of a definite integral $\int_a^b f(x)\,dx$ when the antiderivative of $f$ is unknown, difficult to obtain, or when $f$ is known only through a set of tabulated values. The word *quadrature* historically referred to the construction of a square with area equal to a given figure; in numerical analysis it now denotes any systematic rule for estimating an integral from a finite number of function evaluations.

The central intuition is that a definite integral measures a signed area under a curve. If the curve is replaced by a simpler function — typically a polynomial — that agrees with $f$ at selected points, then the integral of that simpler function can be computed exactly and used as an estimate of the true integral. Every quadrature rule is therefore built from two ingredients: a set of *nodes* $x_0,x_1,\dots,x_n$ in $[a,b]$ and a set of *weights* $w_0,w_1,\dots,w_n$ such that



$$
\int_a^b f(x)\,dx \approx \sum_{i=0}^{n} w_i f(x_i).
$$



The weights encode the geometry of the interpolating polynomial, and the accuracy of the rule depends on how well that polynomial mimics $f$ over the whole interval. This is why quadrature is inseparable from the interpolation and finite-difference material studied earlier: the same nodes and the same polynomial basis drive both constructions.

Because quadrature is an approximation, every computed value carries an error. The study of quadrature methods is therefore inseparable from the study of errors: the *truncation error* of the rule (the error committed by replacing $f$ with a polynomial) and the *round-off error* inherited from evaluating $f$ and forming the weighted sum. The course treats these two error sources together, and the examinable skill is to state a rule, apply it, and then bound or estimate the error it commits.

## 2. Theorems, Lemmas, and Analytical Properties

> **Definition (Quadrature Rule).** Let $f$ be integrable on $[a,b]$. A quadrature rule for $\int_a^b f(x)\,dx$ is a formula of the form



$$
> Q[f]=\sum_{i=0}^{n} w_i f(x_i),
$$



> where the nodes $x_i\in[a,b]$ and the weights $w_i\in\mathbb{R}$ are fixed numbers independent of $f$. The rule is *exact of degree $m$* if $Q[f]=\int_a^b f(x)\,dx$ for every polynomial $f$ of degree at most $m$.

> **Definition (Error of a Quadrature Rule).** The error (truncation error) of the rule $Q$ applied to $f$ is



$$
> E[f]=\int_a^b f(x)\,dx-Q[f].
$$



> **Definition (Absolute, Relative and Percentage Error).** Let $x$ be an exact number and $x_r$ an approximation to it. The absolute error is



$$
> e_{abs}=\lvert x-x_r\rvert,
$$



> the relative error is



$$
> e_r=\frac{\lvert x-x_r\rvert}{\lvert x\rvert},
$$



> and the percentage error is $100\,e_r$. The quantity $\Delta x$ satisfying $e_{abs}=\lvert x-x_r\rvert\le\Delta x$ is called the upper bound on the absolute error.

> **Definition (Round-off Error).** Round-off error arises because it is impossible to represent all real numbers exactly on a machine with finite memory. It is produced by dropping decimal places or significant figures, either by chopping (truncation) or by symmetric rounding.

> **Definition (Propagated and Accumulated Error).** The error in the result of an arithmetic operation arising from initial errors in the numbers used in that operation is called the *propagated error*. The total cumulative error at any step of a procedure is called the *accumulated error*.

> **Definition (Significant-Digit Error Bound).** If a number is correct to $n$ decimal places, then its maximum absolute error is



$$
> e_{abs}=0.5\times 10^{-n}.
$$



### Key Words in the Definition of Error

In point form, the examinable key words embedded in the definitions above are:

- **Exact number** $x$: the true, unknowable value being approximated.
- **Approximate number** $x_r$: the representable value actually used.
- **Difference**: error is always a difference between exact and approximate values.
- **Absolute value**: the error is taken as a magnitude, hence non-negative.
- **Upper bound** $\Delta x$: a guaranteed ceiling on the magnitude of the error.
- **Relative**: error scaled by the size of the exact quantity.
- **Percentage**: relative error expressed per hundred.
- **Truncation/chopping**: discarding digits without adjustment.
- **Symmetric rounding**: adjusting the last retained digit to the nearer value.
- **Propagated**: error transmitted through an operation.
- **Accumulated**: error summed over a sequence of operations.

### Causes of Errors and How to Minimise Them

Short notes on the sources of error and the standard remedies:

- **Finite machine representation.** Real numbers with infinite decimal expansions cannot be stored exactly; the remedy is to work with a controlled number of significant figures and to track the resulting bound $0.5\times10^{-n}$.
- **Chopping versus rounding.** Chopping always biases the result in one direction; symmetric rounding keeps the bias small. Prefer rounding, and avoid subtracting two nearly equal rounded numbers.
- **Loss of significance (subtractive cancellation).** When $x\approx y$, the difference $x-y$ loses leading significant digits. Rearrange formulas algebraically to avoid subtracting nearly equal quantities.
- **Error propagation through arithmetic.** Addition and subtraction add absolute errors; multiplication and division add relative errors. Keep the operation with the largest relative error under control.
- **Accumulation over many steps.** In a sum of many terms, small errors add up. Sum from smallest to largest magnitude, and use composite rules with a modest number of panels rather than a single high-order rule.
- **Truncation of infinite processes.** Replacing a series or an interpolant by finitely many terms introduces a truncation error; choose the order of the rule to match the required accuracy.

### Teaching and Feedback Cycle for This Unit

The lesson is delivered as a two-hour guided session with the following structure, which also indicates how the material is examined:

- **Definition and computation of errors** are introduced first, with worked numerical illustrations.
- **Key-word listing** in point form is used to consolidate the definition before computation begins.
- **Short notes on causes of errors and their avoidance** are produced individually and then compared.
- **Encouraging participation of all learners** is achieved by directing group discussion so that every learner attempts the tasks and posts a response.
- **Providing feedback** is achieved by reviewing posted answers, correcting misconceptions, and noting improvements drawn from peers.
- **Summarising the lesson** closes the session by restating the definitions, the error bounds, and the propagation rules, and by naming the next topic (propagated errors).

## 3. Formal Proofs, Derivations, and Methods
### Orthogonality proof of Gaussian exactness

Let q_n be a degree-n polynomial orthogonal on [a,b] with weight w(x) to every polynomial of degree less than n, and let its n distinct roots x_1,…,x_n be the Gaussian nodes. Define the interpolatory quadrature weights by integrating the Lagrange basis functions associated with those nodes. The resulting rule is exact for every polynomial of degree at most n−1 by construction. The stronger degree 2n−1 result follows from polynomial division.

For any polynomial p with deg p≤2n−1, write p=q_ns+r with deg s≤n−1 and deg r≤n−1. Orthogonality gives ∫wq_ns=0. At each quadrature node q_n(x_i)=0, so the discrete sum of w(x_i)q_n(x_i)s(x_i) also vanishes. The remainder r is exactly integrated by the interpolatory rule. Hence the quadrature sum of p equals its weighted integral. The Gaussian choice therefore achieves exactness through degree 2n−1 while using only n evaluations. The node selection is crucial: arbitrary distinct nodes with interpolatory weights do not in general have this doubled precision.

For the Legendre case, w(x)=1 on [−1,1]. For three nodes, the orthogonal cubic is proportional to P_3(x)=(5x³−3x)/2. Its roots are −√(3/5), 0, √(3/5). Symmetry forces equal outer weights. Moment matching yields 5/9, 8/9, 5/9. The Gaussian theorem says the resulting formula is exact for every polynomial through degree five; this is also checked by matching the even moments 1, x², x⁴ and using symmetry for x, x³, x⁵.

The theorem assumes an appropriate orthogonal polynomial and distinct nodes in the interval. Its exactness conclusion is algebraic; it does not by itself quantify the error for a general smooth non-polynomial function. A higher node count increases the degree of polynomial exactness, but the actual error depends on the integrand and the interval. Do not infer a universal error bound merely from the degree-of-precision statement.

### Undetermined coefficients as an alternative derivation

On the symmetric reference interval, begin with unknown symmetric nodes −r,0,r and weights A,B,A. Matching moments gives 2A+B=2, 2Ar²=2/3, and 2Ar⁴=2/5. The ratio of the last two equations gives r²=3/5; the remaining equations give A=5/9 and B=8/9. This calculation illustrates the general undetermined-coefficients method described in the lecture: choose an ansatz, impose exactness on an appropriate polynomial basis, and solve for the unknown constants.

A subtle point is that merely matching n monomials for n weights at fixed nodes produces exactness through degree n−1, not automatically 2n−1. Gaussian precision comes from selecting the nodes as roots of the orthogonal polynomial. The moment derivation with free symmetric nodes makes this extra freedom visible: the node location r is solved along with the weights. This distinction helps identify why a Gaussian rule is special rather than just another interpolatory sum.

### Affine transformation and orientation

Set c=(a+b)/2 and d=(b−a)/2. Under x=c+dt, t ranges from −1 to 1, dx=d dt, and

$$
\int_a^b f(x)\,dx=d\int_{-1}^{1}f(c+dt)\,dt\approx d\sum_{i=1}^n A_i f(c+dt_i).
$$

When a<b, d>0. If the integration limits are reversed, d<0 and the mapped rule preserves the sign of the oriented integral. This is a useful consistency check. The transformed nodes are not uniformly spaced; for the three-point rule they are c−d√(3/5), c, c+d√(3/5). The weights themselves stay the same on the reference scale, while the common Jacobian factor d rescales all contributions.

## 4. Representative Worked Examples and Solutions
### Examination exemplar: three-point Gauss–Legendre rule

The rule on [−1,1] has t_1=−√(3/5), t_2=0, t_3=√(3/5), with A_1=A_3=5/9 and A_2=8/9. Apply it to the source exercise f(x)=x^6:

$$
\begin{aligned}
Q_3[f]&=\frac59f(-\sqrt{3/5})+\frac89f(0)+\frac59f(\sqrt{3/5})\\
&=\frac{10}{9}\left(\frac35\right)^3=\frac{6}{25}=0.24.
\end{aligned}
$$

The exact integral is 2/7, hence

$$
E=\int_{-1}^{1}x^6\,dx-Q_3[f]=\frac27-\frac6{25}=\frac8{175}\approx0.0457142857.
$$

This matches the module's listed result. Since degree six exceeds the rule's precision degree five, nonzero error is expected and does not disprove the exactness theorem. As a calibration check, x^4 lies within the guaranteed range and is integrated exactly: the Gaussian sum and integral both equal 2/5.

### General-interval exemplar and accuracy comparison

For ∫_0^1e^x dx, set c=d=1/2 and x=c+dt. The transformed nodes are (1−√(3/5))/2, 1/2, (1+√(3/5))/2. Include the Jacobian d=1/2:

$$
Q=\frac12\left[\frac59e^{(1-\sqrt{3/5})/2}+\frac89e^{1/2}+\frac59e^{(1+\sqrt{3/5})/2}\right]\approx1.7182810044.
$$

The exact value e−1≈1.7182818285, so |E|≈8.24×10⁻⁷. This is an observed error because the exact answer is available. The theorem alone only guarantees exactness for polynomials through degree five; it does not claim that e^x is exact. A solution should distinguish the numerical comparison from the polynomial precision guarantee.

A quick scaling check sets f=1. The reference weights sum to 2, and after multiplying by d=1/2 the rule returns 1, the length of [0,1]. This verifies that the Jacobian is present. If the factor were omitted, the constant integral would be 2, immediately exposing the error.

## 5. Mathematical Extensions, Limits, and Common Errors
### High-Yield Takeaways

- **State the rule before computing.** For any quadrature or error question, write the defining formula, identify the nodes and weights (or the exact and approximate values), then substitute. Marks are awarded for the stated formula.
- **The bound $e_{abs}=0.5\times10^{-n}$ is a guaranteed mark.** Whenever a value is described as "correct to $n$ decimal places", immediately write the interval of width $10^{-n}$ centred on the value and quote the bound.
- **Distinguish absolute from relative error.** Absolute error carries units; relative error is dimensionless and is the correct measure when comparing approximations of quantities of different size.
- **Propagation rules are additive.** Absolute errors add under $+$ and $-$; relative errors add under $\times$ and $\div$. Quote this explicitly.
- **Separate propagated from generated error.** The decomposition into propagated and generated parts, summing to the accumulated error, is a standard short-answer question.
- **Know the key-word list.** Be ready to list, in point form, the key words in the definition of error and the causes of error with their remedies.
- **Link quadrature to interpolation.** A quadrature rule is the integral of an interpolating polynomial; the degree of that polynomial determines the order of the truncation error.

### Common Pitfalls and Traps

- **Forgetting the factor $0.5$.** The bound is $0.5\times10^{-n}$, not $10^{-n}$. Writing $10^{-n}$ loses the mark.
- **Using the wrong $n$.** For a value correct to three *decimal places*, $n=3$; for three *significant figures*, the exponent depends on the position of the leading digit. Read the wording carefully.
- **Dividing by the approximate value.** Relative error is defined with the *exact* value in the denominator, $\lvert x\rvert$, not $\lvert x_r\rvert$.
- **Ignoring cancellation.** In $x-y$ with $x\approx y$, the absolute error stays the same while the relative error explodes. Examiners test this deliberately.
- **Adding relative errors for sums.** Relative errors do not add under addition; only absolute errors do.
- **Dropping the sign convention.** Absolute error is a magnitude and is never negative; a negative answer signals a sign slip.
- **Confusing truncation error with round-off error.** Truncation error comes from the approximation method; round-off error comes from finite machine representation. Name the correct one.
- **Omitting the interval argument.** For full marks, show the interval $[x_r-0.5\times10^{-n},\,x_r+0.5\times10^{-n}]$ and the subtraction that produces the bound.

### Answer Structure and Time Management

- **Structure:** definition, formula, substitution, numerical result, interpretation. For propagation questions, add a one-line statement of which errors add.
- **Time allocation:** spend roughly one third of the time on the definition and formula, one third on the arithmetic, and one third on the error bound and interpretation.
- **Marking rubric tips:** explicit formulas, correct interval bounds, correct classification of error type, and a stated conclusion each attract marks independently. Even if the arithmetic slips, the stated method earns credit.
- **Final check:** verify that every error is non-negative, that relative errors are dimensionless, and that the quoted bound is consistent with the number of decimal places given.

### Exactness proof and error interpretation

For n Gaussian nodes, the orthogonality construction selects a degree-n polynomial q_n whose roots are the nodes. If p has degree at most 2n−1, polynomial division gives p=q_ns+r with both s and r of degree at most n−1. Orthogonality makes the integral of q_ns vanish. At every Gaussian node q_n is zero, so the quadrature sum of q_ns vanishes as well. The remainder r is integrated exactly by the interpolatory weights. Therefore the full p is exact. This proof identifies the key premise: the nodes are roots of the appropriate orthogonal polynomial. Equal node count alone does not give the degree 2n−1 guarantee.

For three-point Legendre quadrature, q_3 is proportional to 5x³−3x and the roots are 0 and ±√(3/5). The weights 5/9, 8/9, 5/9 integrate the Lagrange basis polynomials. The direct moment approach is often shorter for hand calculation, but the orthogonality proof explains the n-to-2n−1 result used by the lecture. These are complementary derivations, not competing formulas.

The exactness result is not an error estimate for an arbitrary f. In particular, do not infer a universal error expression merely from the phrase “degree 2n−1.” Error formulas require smoothness and a theorem specific to the Gaussian rule. For this course's task, the reliable conclusions are: the rule is exact through degree five for three nodes; it approximates other functions; and accuracy should be assessed with a suitable comparison or error analysis rather than an unsupported digit count.

### Mapping, scaling, and composite use

On [a,b], let c=(a+b)/2 and d=(b−a)/2. The affine map x=c+dt transforms the reference interval and its quadrature rule:

$$
\int_a^b f(x)\,dx=d\int_{-1}^{1}f(c+dt)\,dt\approx d\sum_{i=1}^{n}A_i f(c+dt_i).
$$

For the three-point rule, the physical nodes are c−d√(3/5), c, and c+d√(3/5), with the same weights and a common factor d. The sum of the reference weights is two, so applying the rule to f=1 returns 2d=b−a. This provides a decisive normalization check. If a and b are reversed, d changes sign and the integral orientation is preserved.

A composite Gaussian procedure partitions [a,b] into smaller intervals and applies the mapped rule on each, summing the local estimates. This resolves variation that one three-point panel might miss while preserving the same node/weight table. Each local mapping must use that panel's own midpoint and half-width. Reusing the whole-interval d for every subpanel produces a wrong scale. The result is not identical to a composite trapezoidal rule: each local panel samples three specially placed interior points instead of two endpoints.

### Source assessment: x^6 and the three-point formula

The lesson asks for the three-point Gauss–Legendre evaluation of x^6 on [−1,1]. Let r=√(3/5). The nodes are −r,0,r and the weights are 5/9,8/9,5/9. Since x^6 is even, the two outer function values are equal; since the center value is zero, only the outer contributions remain:

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

Thus the Gaussian estimate is lower by about 0.0457142857, which rounds to the answer listed in the module. The result is not a contradiction: x^6 is degree six, outside the three-point rule's degree-five exactness. If the same calculation is repeated for x^4, both exact integral and quadrature sum equal 2/5. Contrasting these cases is a direct test of the stated precision.

### A transformed exponential example

To see how a non-polynomial integrand is handled on a general interval, estimate ∫_0^1 e^x dx. Map t∈[−1,1] to x=(1+t)/2. The Jacobian is one half, so the three-point approximation is

$$
Q=\frac12\left[\frac59e^{(1-\sqrt{3/5})/2}+\frac89e^{1/2}+\frac59e^{(1+\sqrt{3/5})/2}\right].
$$

Evaluating the terms gives approximately 1.7182810044. The exact integral is e−1≈1.7182818285, so the absolute difference is about 8.24×10⁻⁷. The function is smooth and the estimate is close, but not exact: the Gaussian precision theorem covers polynomials through degree five, not exponentials. The example also shows the practical cost: three evaluations at nonuniform interior points and one interval scale factor.

### Selecting a quadrature method and stating a conclusion

Use a Gaussian rule when the function can be evaluated at its specified nodes and a high degree of exactness with relatively few evaluations is valuable. Use composite Newton–Cotes formulas when data are already equally spaced or when local panel interpretation is preferred. For rapidly varying or nonsmooth functions, subdividing the interval can be more important than simply increasing a Gaussian order. Selection should account for node availability, smoothness, interval scaling, function-evaluation cost, and the accuracy required.

When answering an exam question, identify the reference formula, map the interval, substitute nodes and weights, include the Jacobian factor, and state what degree of precision applies. If the integrand is a polynomial of degree at most five, say that the result is exact in exact arithmetic. For x^6 or e^x, report an approximation and use an exact value or independent error information if available. Do not claim a formal error bound from node count alone.


### Evaluating the Gaussian rule against Newton–Cotes methods

Newton–Cotes rules use equally spaced nodes; the Gaussian construction chooses nodes as roots of an orthogonal polynomial. The composite trapezoidal rule and Simpson's rule are convenient on uniform tables and can be repeated over subintervals. Gauss–Legendre quadrature achieves degree 2n−1 with n optimally selected nodes on the reference interval. These are complementary design choices, not a claim that one method is universally preferable.

A Gauss–Legendre rule is attractive when f can be evaluated at the nonuniform nodes, the integrand is reasonably smooth, and function evaluations are costly. A composite equally spaced rule is often natural when data are already tabulated at regular locations. For localized rapid variation, subdividing the interval can improve resolution. For a singularity or discontinuity, the method and interval partition must account for it; the nominal polynomial exactness of a global rule does not cure nonsmoothness.

When assessing a result, distinguish quadrature truncation from function-evaluation uncertainty. If each sampled ordinate has an error, the weighted sum inherits a combination of those errors. High-order exactness cannot recover information missing from noisy or rounded inputs. Likewise, a theorem about exact polynomials does not certify the error of an arbitrary analytic function without an appropriate remainder theorem. The safest report gives the rule and nodes, shows the transformed sum, and states the basis of any accuracy claim.

### Constructing the weights and checking implementation

For fixed nodes, an interpolatory quadrature rule integrates the Lagrange basis polynomials to obtain its weights. In the Gaussian construction, the nodes themselves are selected from the orthogonal polynomial, increasing the exactness beyond the degree of the interpolating polynomial. For the three-point Legendre case, symmetry reduces the unknowns to r, A, and B. Matching the zeroth, second, and fourth moments gives r²=3/5, A=5/9, and B=8/9. This derivation is compact enough to reproduce in an examination answer and transparent enough to catch transcription errors.

A numerical implementation should keep the reference nodes and weights in one table, map the nodes using c and d for each interval, evaluate f at each mapped point, then multiply the weighted sum by d. Check that the mapped nodes lie within the interval, the weights sum to two before scaling, and the constant function integrates to b−a after scaling. Reversing a and b should reverse the sign. These checks cover node mapping, Jacobian, and orientation.

### Reporting exactness and error carefully

When f is a polynomial of degree at most five, the three-node rule's exactness theorem supplies a strong conclusion: in exact arithmetic, Q equals the integral. For x^6, it does not. The lesson's x^6 calculation gives Q=6/25 while the exact integral is 2/7, yielding 8/175 absolute error. This explicit counterexample is an effective guard against extending the degree-five guarantee by one degree.

For a non-polynomial function such as e^x, the rule can be highly accurate without being exact. On [0,1], the computed value approximately 1.7182810044 differs from e−1 by about 8.24×10⁻⁷. This observed error can be reported because the exact integral is available. Without that reference, compare another rule or refine the interval and label the result as an estimate; do not state a guaranteed tolerance merely because the rule has three Gaussian nodes.


### Why the division proof is the decisive argument

An interpolatory rule with n nodes is immediately exact through degree n−1, because those polynomials are reproduced by interpolation. The surprising Gaussian result is exactness through degree 2n−1. To justify the stronger statement, one must use a property not shared by arbitrary interpolation nodes: their defining polynomial q_n is orthogonal to every polynomial of lower degree.

Polynomial division gives p=q_ns+r. The degree bound on p ensures deg s≤n−1 and deg r≤n−1. Orthogonality eliminates the integral of the first term. At the nodes, q_n is zero, so that same term contributes nothing to the weighted sum. The remaining r is integrated exactly by the interpolatory rule. This argument proves agreement of the integral and quadrature for the entire class, not merely for a list of examples.

Each premise has a role. Orthogonality concerns the continuous integral with its weight. The roots make the discrete contribution vanish. The remainder degree ensures the lower-degree exactness of the interpolatory rule applies. Omitting any of these links leaves a gap. In particular, saying only that the nodes are roots does not prove exactness unless the orthogonality and remainder arguments are also supplied.

For the Legendre three-node case, the weight function is one and q_3 can be taken as P_3=(5x³−3x)/2. Its three roots lie within the reference interval. The resulting weights integrate the Lagrange basis and are 5/9,8/9,5/9. This construction therefore has degree of precision five. The moment approach confirms the same result directly, while the division proof explains its general origin.

### A detailed error reading of the source polynomial example

The source's x^6 exercise deliberately uses a polynomial just beyond the exactness range. At the two nonzero nodes r=√(3/5), the sixth power is r^6=(3/5)^3=27/125; at zero it is zero. The outer terms combine to

$$
Q_3=\frac{10}{9}\frac{27}{125}=\frac{6}{25}.
$$

The antiderivative gives ∫_{−1}^{1}x^6 dx=2/7. Subtracting the quadrature value from the exact value gives

$$
\frac27-\frac6{25}=\frac{50-42}{175}=\frac8{175}\approx0.0457143.
$$

This difference is positive, so the rule underestimates this even integrand on this interval. That observed sign is specific to x^6; it is not a general rule that Gaussian quadrature underestimates positive functions. The example establishes a boundary of the degree guarantee, not a universal direction for error.

For x^4, the same nodes produce the exact moment 2/5. For odd monomials up to degree five, symmetry yields zero exactly. Together these checks make a complete basis verification. The x^6 discrepancy then illustrates what can happen immediately outside that space. A careful solution distinguishes “the rule has degree five” from “this particular result happens to be close.”

### Interval maps, panel maps, and orientation

For a general interval, c=(a+b)/2 and d=(b−a)/2. The transformed integrand is f(c+dt), and the scale is d. In a composite rule, the same formula is applied independently to each panel. Replacing d with the interval length is a factor-of-two error; mapping t using c but forgetting to transform dx is another. These mistakes can be caught by applying the procedure to the constant integrand, whose exact integral is b−a.

Orientation is also encoded in d. If the limits are reversed, then d<0 and the change of variables yields a negative integral, as required by the definition ∫_b^a f=−∫_a^b f. A procedure that takes an absolute half-width without separately restoring orientation loses that sign. Most exercises use a<b, but a general derivation should retain the signed half-width.

For a partition, each panel contributes d_j times a reference weighted sum. This is not equivalent to applying one global formula and then dividing its answer among panels. Local mapping changes the evaluation points and scales for every subinterval. Writing the local formula before summing makes the composite structure explicit and allows panel-level refinement where the integrand varies most.

### Comparison with equally spaced quadrature

The trapezoidal and Simpson formulas use equally spaced ordinates, and their composite versions are convenient when a regular table is given. Gaussian formulas instead optimize node locations for polynomial precision. With n Gaussian evaluations, degree 2n−1 is integrated exactly; this high precision can be valuable when function evaluation is expensive and the nodes are available.

That comparison concerns exactness on polynomials, not total practical accuracy in all settings. A table containing only equally spaced data cannot supply Gaussian values at arbitrary interior points without additional approximation. If the integrand has sharp local variation, a composite method may represent that variation more transparently than a single global panel. If there is a discontinuity or singularity, the interval should be treated in a way that respects it; smooth-function intuition should not be carried over without checking assumptions.

The method choice should be justified from the actual information available. Ask whether function evaluation is permitted, whether data are tabulated, whether the function is smooth over the entire interval, and how much accuracy is needed. The Gaussian formula is a powerful option, not an instruction to disregard these constraints.

### Numerical reporting and reproducibility

A reproducible numerical answer identifies the interval, the specific node-weight rule, the transformed nodes, and the scale factor. It should show enough intermediate work to verify the weighted sum. For the exponential example, preserve the three transformed abscissae and evaluate each exponential there; combine the center and outer contributions with their distinct weights, then multiply by one half. This transparent sequence makes the approximation independently checkable.

Report a useful number of digits rather than every digit produced by a calculator. If an exact reference is available, give an absolute error and, where useful, a relative error. If it is unavailable, state that the answer is an approximation and describe any comparison or refinement used. A rounded decimal is not itself an error guarantee.

Finally, separate mathematical truncation from arithmetic effects. Exactness for a polynomial says that the ideal weighted sum equals its integral. In floating-point computation, node representations, function values, multiplication, addition, and final rounding can introduce small discrepancies. Those effects do not invalidate the theorem, but they explain why a computed exact-polynomial test may differ in its last digits. A robust check compares within an appropriate numerical tolerance and retains exact fractions as long as practical.

