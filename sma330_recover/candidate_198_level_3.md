## 1. Foundational Concepts, Definitions, and Axioms

Given distinct nodes, the Vandermonde interpolation problem is nonsingular, yielding a unique polynomial of degree at most n. The Lagrange representation constructs it from cardinal functions; Newton’s representation is nested and exposes the incremental divided-difference coefficients. For equal spacing, forward differences encode those coefficients through factorial polynomials, while backward differences anchor the expansion at the terminal node. The representations are algebraically equivalent but have different data and evaluation conveniences.

Scope is deliberately bounded to lessons 4–6. The key results are collocation existence and uniqueness, the Lagrange formula, Taylor polynomial construction, finite-difference recursion and constant-difference property, Newton forward/backward formulas, and divided differences for unequally spaced data. We do not treat unrelated numerical integration or general root-solving. Error claims are conditional: interpolation error formulas need smoothness hypotheses; extrapolation can be poor; and approximate input values propagate through computed coefficients.

When auditing a derivation, retain node order, spacing, and indexing throughout. A forward table begins at the first node, a backward table at the last, and a divided-difference denominator spans the endpoints of its node subset. Most errors are not deep theorem failures but mismatched indices, incorrect spacing, an omitted factor of h, or a numerator and denominator using different node orderings.

## 2. Theorems, Lemmas, and Analytical Properties

Existence can be seen constructively from Lagrange basis functions; uniqueness follows from the root-count theorem. The interpolation error, when f is n+1 times continuously differentiable, has form f(x)-P_n(x)=f^(n+1)(ξ)/(n+1)! product_i(x-x_i) for some ξ in the interval. This explains exact agreement at nodes and why distance from nodes and higher derivatives affect error. The source’s Weierstrass result is different: it guarantees some polynomial approximation uniformly close to a continuous function on a compact interval, not necessarily the particular interpolant through a selected table.

Finite differences are discrete analogues of derivatives. If x_i=x_0+ih, then Δf_i=f_(i+1)-f_i; repeated application defines Δ^k. For a polynomial of degree m, Δ^m is constant and Δ^(m+1)=0. Newton forward interpolation follows from expressing values in the falling-factorial basis. The backward form follows by anchoring the same polynomial at x_n and using backward differences. This indexing distinction is essential at endpoints.

Unequal spacing replaces constant-step differences with divided differences. Their recursive denominators are x_(i+k)-x_i; changing node order changes intermediate coefficients but not the unique polynomial. Error bounds and diagnosis from rounded tables must be stated cautiously: near-constant high differences can indicate a low-degree model, but measurement and rounding noise prevents exact constancy in practice.

## 3. Formal Proofs, Derivations, and Methods

A proof-oriented workflow separates construction, verification, and error interpretation. First identify node geometry and choose a representation. Then derive coefficients while preserving index conventions. Verify interpolation constraints exactly before simplifying. Finally state what the polynomial approximates and under what assumptions an error statement applies.

For equal spacing, define Δ recursively and form the triangular difference table. Newton’s forward basis is u(u-1)...(u-k+1)/k!, and the coefficient is Δ^k y_0. Backward interpolation uses a terminal anchor and backward differences, with basis v(v+1)...(v+k-1)/k!. For nonuniform data, use divided differences. Do not use a fixed h when gaps vary.

The Lagrange construction is direct but can be expensive to recompute after a new node; Newton form is incremental. Both are theoretically the same polynomial. Taylor polynomials use local derivative data rather than collocation values. Their remainder behavior is local and depends on derivatives; the source warns that accuracy can deteriorate away from the expansion point. A claimed error bound must name its smoothness interval and the derivative bound it uses.

## 4. Representative Worked Examples and Solutions

### 4.1 Lagrange construction from three nodes

Worked example 1 — Lagrange construction from three nodes. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The data are (0,-2), (1,-7), and (2,-16). Each node gets a cardinal polynomial. The denominators come from the corresponding node differences; checking the values at 0, 1, and 2 ensures the basis has the required one-at-its-own-node, zero-at-the-other-nodes behavior.

$$
L_0(x)=\frac{(x-1)(x-2)}2,\quad L_1(x)=-x(x-2),\quad L_2(x)=\frac{x(x-1)}2
$$

The interpolant is P(x)=-2L_0(x)+-7L_1(x)+-16L_2(x). Simplification gives P(x)=(-2)x^2+(-3)x+(-2); at x=1/2 it is -4. Re-substitution recovers all three ordinates. This example shows how the basis formula performs the construction rather than merely checking a polynomial guessed in advance.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.2 Newton forward formula on equal spacing

Worked example 2 — Newton forward formula on equal spacing. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

Here the nodes are 4, 6, 8, and 10, so h=2 and the forward parameter at x=7 is u=(7-4)/2=3/2. The table’s first differences are [40, 56, 72]; the second differences are [16, 16]; and the third difference is 0. These entries follow from subtracting adjacent values, not from dividing by h.

$$
P(x)=32+u(40)+\frac{u(u-1)}2(16)+\frac{u(u-1)(u-2)}6(0)
$$

Substituting u=3/2 gives P(7)=98. Because the data were generated from a quadratic, the third difference vanishes and the formula reduces to the quadratic terms. The four node substitutions reproduce the table. The calculation illustrates why equal spacing must be verified before reading a forward-difference column as Newton coefficients.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.3 Newton backward formula near the last node

Worked example 3 — Newton backward formula near the last node. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The table is equally spaced with h=1, and the target x=5/2 lies half a step before the last node x_3=3. Thus v=(x-x_3)/h=-1/2. The terminal value is y_3=-1; the last backward first difference is -1, and the last backward second difference is 0. Since the data are quadratic, higher differences vanish.

$$
P(x)=y_3+v\nabla y_3+\frac{v(v+1)}2\nabla^2 y_3
= -1+v(-1)+\frac{v(v+1)}2(0)
$$

Evaluation gives P(5/2)=-1/2. This is the same unique polynomial that a forward formula would produce, but the terminal anchor keeps the relevant differences at the end of the table. Replacing v by (x-x_0)/h would mix two different conventions.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.4 Divided differences for unequal nodes

Worked example 4 — Divided differences for unequal nodes. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The data use nodes 0, 1, 2, and 4; the last gap is two, so a constant-step forward table is not applicable. The first divided differences are [0.0, 10.0, 49.0], the second are [5.0, 13.0], and the third is 2.0. Each denominator spans the outer nodes of the divided-difference entry.

$$
P(x)=-1+(0.0)(x-0)+(5.0)(x-0)(x-1)+(2.0)(x-0)(x-1)(x-2)
$$

At x=3 the value is 41. Substituting x=0,1,2,4 returns the four data values. Divided differences retain the actual unequal spacings and produce a Newton polynomial whose leading diagonal entries are its coefficients.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.5 Maclaurin approximation to sine

Worked example 5 — Maclaurin approximation to sine. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

A Taylor polynomial is fitted to derivative information at its center, not to a list of function values. At zero, the successive derivatives of the selected function have values 0, 1, 0, and -1. Dividing each derivative value by its factorial gives the cubic coefficients; a zero derivative removes the corresponding power.

$$
P_3(x)=x-x^3/6,\qquad P_3(0.1)\approx 0.09983333
$$

For comparison, the function value is 0.09983342, so the absolute discrepancy is 8.33e-08. The source’s sine calculation gives x-x^3/6 and approximately 0.0998333 at 0.1. Agreement near the center is expected; it does not imply the same accuracy far away, since the omitted terms grow with distance.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.6 Using constant second differences to audit a misprint

Worked example 6 — Using constant second differences to audit a misprint. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

Suppose equally spaced integer abscissae 0 through 4 are expected to follow a quadratic trend, but the listed ordinates are [0, 3, 13, 15, 24]. A quadratic has constant second differences. The observed second differences are [7, -8, 7], so the middle value is suspect. If the expected constant is 2, solving the middle second-difference equation gives the corrected ordinate 8.

$$
\Delta^2y_0=y_2-2y_1+y_0,\qquad
\Delta^2y_1=y_3-2y_2+y_1
$$

Replacing only the suspect entry gives second differences [2, 2, 2]. This is a plausible correction under the stated quadratic assumption, not a conclusion available from data alone. Without a degree or smoothness model, any finite list can be interpolated exactly by a sufficiently high-degree polynomial. State the assumption that makes a correction identifiable.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.1 Why the interpolation polynomial is unique

The uniqueness theorem has a short proof that also explains why distinct nodes are essential. Suppose two polynomials $P$ and $Q$, each of degree at most $n$, fit the same $n+1$ node-value pairs. Their difference $R=P-Q$ has degree at most $n$ and satisfies $R(x_i)=0$ at every node. A nonzero polynomial of degree at most $n$ cannot have more than $n$ distinct roots. Hence $R$ must be the zero polynomial and $P=Q$.

This proof separates two ideas. Existence says that at least one polynomial fits the data; the Lagrange formula constructs one. Uniqueness says that no second polynomial of the same degree limit can also fit the data. If two nodes coincide but prescribe different ordinates, no function can satisfy both conditions. If a node is repeated with the same ordinate, the number of distinct interpolation conditions is lower than the count of rows, and the usual uniqueness claim must be restated in terms of distinct nodes.

The Vandermonde system gives an equivalent algebraic viewpoint. Write $P(x)=a_0+a_1x+\cdots+a_nx^n$ and impose $P(x_i)=y_i$. The coefficient vector solves a linear system whose matrix has rows $(1,x_i,\ldots,x_i^n)$. Its determinant is a nonzero product of pairwise node differences when all nodes are distinct. Therefore the coefficients are uniquely determined. The determinant argument and the root-count argument reach the same conclusion but emphasize different mechanisms: one is a linear-algebra statement, the other a fact about polynomial roots.

### 4.2 The Lagrange basis and exactness checks

For nodes $x_0,\ldots,x_n$, define

$$
L_k(x)=\prod_{\substack{0\le j\le n\\j\ne k}}
\frac{x-x_j}{x_k-x_j}.
$$

Every denominator is nonzero precisely because the nodes are distinct. When $x=x_k$, all factors equal one; when $x=x_j$ for $j\ne k$, one numerator factor vanishes. Thus $L_k(x_i)$ equals one if $i=k$ and zero otherwise. The polynomial $P(x)=\sum_{k=0}^n y_kL_k(x)$ consequently satisfies every interpolation condition.

This construction supplies a direct diagnostic for a computed polynomial. First evaluate each basis at the nodes; the resulting values should form an identity matrix. Then use the data ordinates as weights and check that the final interpolant returns every $y_i$. Only after this check should the expression be expanded or evaluated at a new point. Simplifying too early can hide a missing factor in one basis polynomial.

For the nodes $0,1,2$ and values $1,2,5$, the basis is

$$
L_0=\frac{(x-1)(x-2)}{2},\qquad
L_1=-x(x-2),\qquad
L_2=\frac{x(x-1)}{2}.
$$

The weighted sum $L_0+2L_1+5L_2$ simplifies to $x^2+1$. The node test is immediate: the values are $1,2,5$. At the interior point $1.5$, the result is $3.25$. The construction makes existence transparent, while the uniqueness proof ensures that Newton’s formula, if correctly formed from these same nodes and values, must simplify to the same polynomial.

### 4.3 Divided differences and the incremental Newton form

The Newton representation builds the interpolant one condition at a time. Start with the constant $P_0(x)=y_0$. To incorporate the next node $x_1$ without changing the value at $x_0$, add a multiple of $(x-x_0)$:

$$
P_1(x)=y_0+c_1(x-x_0).
$$

Choosing $c_1$ so that $P_1(x_1)=y_1$ gives $c_1=(y_1-y_0)/(x_1-x_0)=f[x_0,x_1]$. The next correction must vanish at both existing nodes, so it is a multiple of $(x-x_0)(x-x_1)$. The coefficient that enforces the value at $x_2$ is the second divided difference. Continuing gives

$$
P_n(x)=f[x_0]+f[x_0,x_1](x-x_0)
+f[x_0,x_1,x_2](x-x_0)(x-x_1)+\cdots.
$$

The recursion

$$
f[x_i,\ldots,x_{i+k}]
=\frac{f[x_{i+1},\ldots,x_{i+k}]-f[x_i,\ldots,x_{i+k-1}]}
{x_{i+k}-x_i}
$$

uses the actual outer-node separation. This is why divided differences work with unequal spacing, unlike a forward-difference formula that assumes a common interval length. In a triangular table, each new column is a higher-order difference; the Newton coefficient is the entry at the appropriate beginning of that column.

An important practical advantage is incremental updating. If a new distinct node is added, the earlier Newton terms already fit the old points. Only one additional coefficient and basis product are needed to extend the polynomial. By contrast, a fully expanded monomial polynomial may need to be recomputed. The new data point can nevertheless change the curve substantially between nodes, particularly when the degree becomes high; efficient updating is not the same as guaranteed stability.

### 4.4 Finite differences as scaled derivative information

For equally spaced nodes $x_i=x_0+ih$, the forward difference is $\Delta y_i=y_{i+1}-y_i$. A second difference subtracts adjacent first differences, and higher differences repeat the operation. For a polynomial of degree $m$, the $m$-th differences are constant on an exact equally spaced table and the next differences vanish. This fact explains why finite-difference tables can reveal polynomial degree.

The scaling with $h$ matters. A first difference is approximately $h f'(x)$ for a smooth function; a second difference is related to $h^2 f''(x)$; higher differences carry higher powers of $h$. If $h\ne1$, the numerical difference is not itself the derivative. The normalized variable $u=(x-x_0)/h$ places the Newton forward basis in dimensionless form, and factorials convert the successive difference contributions into the corresponding polynomial coefficients.

For $y=1,2,5,10$ at $x=0,1,2,3$, the first differences are $1,3,5$ and the second differences are $2,2$. Since the third difference is zero, the data fit a quadratic. The Newton forward expression is

$$
P(x)=1+x+\frac{x(x-1)}{2}(2)=x^2+1.
$$

If the same observations were at spacing $h=2$, the normalized variable would be $u=(x-x_0)/2$; inserting $x$ directly into the unit-spacing formula would be wrong. Always inspect the node gaps before computing a difference table.

For measured data, differences are affected by rounding. A high-order difference may be small or zero only within the precision of the table. It is therefore a diagnostic rather than a proof that the underlying function is exactly a polynomial. Report the pattern that is observed and qualify any conclusion about degree.

### 4.5 Interpolation error and the domain of a conclusion

When $f$ has sufficiently many derivatives on an interval containing the nodes and the evaluation point, the interpolation remainder has the form

$$
f(x)-P_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}
\prod_{i=0}^n(x-x_i)
$$

for some $\xi$ in that interval. The formula explains two contributors to error: the size of the next derivative and the product of distances from the evaluation point to every node. It also shows why the remainder is zero at each interpolation node.

This expression is only useful as a bound if a valid bound for $|f^{(n+1)}|$ is available across the whole interval under consideration. A derivative value at one point is not a bound over an interval. Likewise, the product factor can become large away from the node set, so extrapolation can be much less reliable than interpolation. If smoothness or derivative information is unavailable, state that the exact fitted values are known but the between-node error is not certified by this formula.

The remainder theorem does not say that adding nodes always improves an interpolant at every point. A higher-degree polynomial fits more observations, but its basis factors may grow and the data may contain noise. Node placement, interval width, smoothness, and arithmetic precision all influence practical behavior. A reliable solution distinguishes the polynomial’s exact interpolation property from a guaranteed approximation quality.

### 4.6 Evaluation, conditioning, and reporting

The monomial form $a_0+a_1x+\cdots+a_nx^n$ can be evaluated by Horner’s recurrence, which replaces repeated powers with nested multiplication and addition. For a degree-$n$ polynomial, this needs roughly $n$ multiplications and $n$ additions after the coefficients are known. It also reduces some unnecessary rounding from separately forming every power. It does not remove error in the coefficients or cure a poorly conditioned interpolation problem.

When nodes are close together, divided-difference denominators can be small, so small changes in data may create large changes in coefficients. When a polynomial is evaluated far from its nodes, large terms may cancel. These are reasons to preserve the node form or use a numerically careful evaluation method rather than expanding and rounding coefficients prematurely. They are not reasons to distrust every polynomial result; they are prompts to examine the scale and data geometry.

A complete interpolation report should identify the nodes, the construction method, the degree limit, the output at the requested point, and any error limitation. For equally spaced data, state $h$ and the normalized coordinate. For nonuniform data, use the actual node differences. Verify all interpolation conditions, preserve guard digits, and distinguish an interpolated in-range value from an extrapolated out-of-range prediction.

### 4.1 Forward and backward formulas are coordinate choices

The forward and backward Newton forms represent the same interpolating polynomial when they use the same equally spaced data. Their difference lies in the anchor point and basis factors. The forward form begins at $x_0$ and uses $u=(x-x_0)/h$; the backward form begins at $x_n$ and uses $v=(x-x_n)/h$. Choosing the form whose anchor is near the requested point often keeps the normalized coordinate small and the arithmetic more manageable.

For nodes $0,1,2,3$ with values $1,2,5,10$, the forward differences begin with $\Delta y_0=1$, $\Delta^2y_0=2$, and the backward differences end with $\nabla y_3=5$, $\nabla^2y_3=2$. At $x=2.5$, the forward coordinate is $u=2.5$ and the backward coordinate is $v=-0.5$. The respective expressions are

$$
P(x)=1+u+\frac{u(u-1)}{2}(2)
$$

and

$$
P(x)=10+5v+\frac{v(v+1)}{2}(2).
$$

Substitution gives $7.25$ in either form, matching $x^2+1$. The numerical coordinates differ, but both satisfy the same node constraints. A practical solution can use the more convenient form and verify at least one endpoint value to confirm the direction convention.

### 4.2 Perturbing observations changes the interpolant

The interpolation conditions are linear in the ordinates. If one datum $y_j$ changes by $\epsilon$, the interpolating polynomial changes by $\epsilon L_j(x)$, where $L_j$ is its fundamental Lagrange polynomial. This follows directly by subtracting the two Lagrange sums: every other term cancels, leaving only the changed ordinate multiplied by its basis.

At the node $x_j$, $L_j(x_j)=1$, so the polynomial change is exactly $\epsilon$. At other nodes, $L_j(x_i)=0$, so the other interpolation conditions remain unchanged. Between nodes, however, the magnitude $|L_j(x)|$ determines how strongly that single measurement affects the prediction. A basis value larger than one amplifies the observation perturbation at that point.

This is a direct way to understand why exact interpolation of noisy data can be unstable. The polynomial continues to pass through every altered ordinate; it does not average the error away. If the task is to reproduce the table, interpolation is appropriate. If the task is to estimate an underlying trend from noisy observations, a method that does not force every noisy point to be matched may be more appropriate, but that is a different problem.

### 4.3 Reading a remainder formula as a conditional bound

For $f$ with a continuous $(n+1)$-st derivative on an interval containing the nodes and an evaluation point $x$, the interpolation remainder can be written

$$
f(x)-P_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}
\prod_{i=0}^n(x-x_i)
$$

for some $\xi$ in that interval. Taking magnitudes and using a derivative bound $M=\max |f^{(n+1)}|$ gives

$$
|f(x)-P_n(x)|\le \frac{M}{(n+1)!}
\left|\prod_{i=0}^n(x-x_i)\right|.
$$

This deduction has two separate requirements: the derivative must exist with the stated continuity, and $M$ must bound it over the whole relevant interval. If either condition is missing, the displayed expression cannot be advertised as a guaranteed numerical error bound.

The node product also reveals why location matters. At a node it vanishes, matching exact interpolation. Between nodes it may be moderate, while far beyond the node interval its factors can all grow. The formula therefore gives a mathematical explanation for the increased risk of extrapolation, though the derivative factor may also change across a wider interval.

### 4.4 Polynomial degree, exact data, and noisy data

For exact ordinates from a polynomial of degree $m$, every forward difference of order greater than $m$ is zero on an equally spaced grid. The converse is useful when a finite table is known to be exact and equally spaced: a zero difference row supports a polynomial of lower degree. If the table is rounded, the same conclusion is approximate rather than exact.

Suppose the entries are printed to two decimal places. Each value may have an error of up to half a hundredth. Taking a first difference subtracts two such values; taking second differences combines four values with alternating signs. High-order differences can therefore magnify the display noise relative to their size. A near-zero high-order row should be interpreted against the precision of the table.

This reasoning also helps detect transcription issues. Recompute the table from its original data and check a suspected row using the definition of the difference operator. If exact polynomial structure is known independently, it can constrain a missing or mistyped entry. Without that independent premise, changing the observation to force a desired zero row is unjustified.

### 4.5 Separating algebraic conditioning from evaluation cost

Horner evaluation reduces the number of arithmetic operations needed to evaluate a polynomial in monomial form. It can also reduce the number of times a power of $x$ is rounded. But it does not make the coefficients exact, remove sensitivity to perturbed nodes, or ensure that the polynomial is a good model for the data.

Likewise, an incremental Newton form makes it easy to add a node, but a small divided-difference denominator can amplify changes in the ordinates. The representation determines how efficiently the polynomial is constructed or evaluated; the conditioning describes how much the answer changes when the data change. These questions should not be conflated.

When checking a computation, use independent forms if available: a Newton expression and a Lagrange expression should agree after both are correctly formed; a Horner evaluation should agree with direct substitution at a low-degree test point. Agreement catches algebra mistakes but does not certify the physical accuracy of the data or the suitability of the model.

### 4.7 A coefficient perturbation example

The Lagrange basis gives a direct sensitivity calculation. For the nodes $0,1,2$,

$$
L_0(x)=\frac{(x-1)(x-2)}{2}.
$$

At $x=1.5$, this basis value is $L_0(1.5)=-0.125$. If the first ordinate changes by $\epsilon$, while the other two remain fixed, the interpolated value at $1.5$ changes by $-0.125\epsilon$. The sign means that increasing the first endpoint value decreases the estimate at this particular interior point. At a different point, the same basis can have a different sign or magnitude.

This example makes interpolation’s dependence on data explicit. The polynomial continues to satisfy all node conditions after the perturbation because the other basis polynomials vanish at the first node and $L_0$ vanishes at the other nodes. It also shows why the word “exact” must be localized: the polynomial exactly fits its input ordinates, but its predictions inherit any uncertainty in those ordinates.

For several uncertain ordinates with independent absolute bounds $\epsilon_i$, the triangle inequality gives

$$
|\Delta P(x)|\le\sum_{i=0}^n|L_i(x)|\,\epsilon_i.
$$

This is a finite linear sensitivity bound for the interpolation formula at fixed nodes. It does not account for uncertainty in the node locations, which changes the basis functions themselves. If the abscissae are uncertain, additional analysis is required.

### 4.8 Node geometry and extrapolation

The product $\prod_i(x-x_i)$ in the interpolation remainder can be read geometrically. Each factor measures the distance from the requested value to one of the nodes. If $x$ is one of the nodes, the product is zero. If $x$ lies between nodes, some factors may be small and the product may remain moderate. If $x$ lies well outside the node range, every factor can be large in magnitude.

The derivative term also depends on the interval. An extrapolation point farther from the data may require controlling a higher derivative over a wider interval, and that derivative may grow. Thus the remainder formula does not say “extrapolation is always inaccurate”; it explains why the conditions needed for a useful bound become harder to satisfy.

In a practical calculation, inspect the node range, distance to the nearest node, and available smoothness information. If only a table is given, state that the interpolated polynomial provides a model-based extension and that a rigorous error bound is not available from the table alone. Avoid adding unsupported confidence to an out-of-range value merely because the polynomial evaluation is exact arithmetic.

### 4.9 Computational checks across representations

The monomial, Lagrange, and Newton forms can all represent the same unique polynomial but have different audit advantages. The monomial form makes coefficients and degree explicit. Lagrange shows how each ordinate contributes and is direct for a fixed set of nodes. Newton exposes incremental divided differences and can be extended efficiently when another node is added. Horner evaluates a monomial coefficient list with a compact sequence of multiply-add operations.

For a low-degree test problem, build the polynomial in one form and evaluate it in another. If the Lagrange expression gives $x^2+1$ and the Newton form gives a different value at an interior point, check the basis denominators, difference indexing, factorial, and step-size normalization. If the forms agree at nodes but not elsewhere, at least one expression is not the same polynomial; matching only a subset of nodes is not sufficient.

Independent checks should use unrounded coefficients until the comparison is complete. If one method rounds an intermediate coefficient and the other does not, small discrepancies may reflect arithmetic precision rather than a conceptual disagreement. The report should state the precision used and avoid treating agreement to a few digits as proof of the underlying data’s accuracy.

### 4.10 A reconstruction audit for an interpolant

After constructing a polynomial from a table, verify it in a way that checks both the coefficients and the data indexing. For an equally spaced table, start with the first ordinate, then evaluate the Newton forward expression at $u=0,1,\ldots,n$. At $u=0$, every correction term vanishes. At $u=1$, all terms after the first difference vanish. At $u=2$, the second-order correction is the first new term that contributes. This triangular structure is why the Newton basis is convenient for checking the construction row by row.

For arbitrary nodes, substitute each $x_i$ into the Lagrange sum. Only the $i$-th basis polynomial should remain, so the result must be $y_i$. If an expansion was used, compare it with the unexpanded form at one additional point. A mismatch can indicate either algebra error or premature coefficient rounding.

The residual at a node is $P(x_i)-y_i$. For exact arithmetic and a correctly formed interpolant, it is zero. With floating-point arithmetic, it may be a small nonzero number. Its size should be compared with the scale of the data and the arithmetic precision. A small residual confirms the algebraic fit but does not estimate the error between nodes.

### 4.11 Choosing a representation for the next operation

The best polynomial form depends on what must be done next. If the task is to inspect degree or leading behavior, the monomial form is transparent. If the data are arbitrary and only one interpolant is needed, Lagrange’s form is direct. If new nodes may arrive sequentially, Newton’s divided-difference form supports incremental extension. If an equally spaced table is evaluated near an endpoint, forward or backward differences can simplify the normalized coordinates. For repeated evaluation of a known coefficient list, Horner’s recurrence reduces work.

These are not competing claims about which polynomial is “the real one.” Uniqueness guarantees the same degree-at-most-$n$ polynomial when each formula is correctly applied. The representations simply organize the arithmetic differently. Select them according to data structure and computational task, then verify the node conditions independently.

An interpolant can be algebraically correct but poorly conditioned for the requested evaluation. If basis factors or monomial powers become large and cancel, many digits may be lost. In that case preserve a stable nested or barycentric-like form only if it is within the approved method; otherwise explain the sensitivity and avoid overstating the result’s precision.

## 5. Mathematical Extensions, Limits, and Common Errors

Method selection is determined by the data geometry: Lagrange is general for distinct nodes; Newton divided differences are incremental and nonuniform; Newton forward/backward use equal spacing and are most convenient near their anchor; Taylor uses derivatives at one center. No formula can be selected responsibly without first checking the nodes.

Error interpretation is conditional. The interpolation remainder involves f^(n+1)(ξ) and the product of node distances; smoothness and interval location matter. Uniform polynomial approximation for a continuous function is an existence theorem and does not identify a particular interpolant. Rounded finite-difference tables can obscure exact constant-difference patterns and may amplify measurement noise.

Source caution: the OCR-extracted Lagrange sample on fractional nodes is incomplete and corrupted, so its coefficients cannot be verified reliably. It is not reproduced as a worked answer. The legible lesson 6 four-node example is checked directly; the forward-difference values are 2,5,12; 3,7; and 4. Always distinguish a demonstrable calculation from a damaged source fragment.

### Lessons 5–6: finite differences and Newton interpolation
The interpolation sequence continues from values at nodes to differences between neighboring values. For equally spaced arguments, write the step as $h$ and use $\Delta y_i=y_{i+1}-y_i$; repeated differences are formed by taking differences of the preceding row. The pattern in the table reveals whether a lower-degree polynomial is plausible: constant first differences indicate a linear pattern, constant second differences a quadratic pattern, and constant third differences a cubic pattern. This is a diagnostic for a table, not a claim that every data set must have constant differences.

For the source table $x=1,2,3,4,5,6$ with $y=-4,-2,2,14,40,86$, the first differences are $2,4,12,26,46$; the second differences are $2,8,14,20$; and the third differences are $6,6,6$. Hence Newton's forward polynomial through these equally spaced data is cubic. At $x=2.5$, $h=1$ and $u=(x-x_0)/h=1.5$. Substituting the leading forward differences gives

$$
P(x)=-4+2u+\frac{2}{2!}u(u-1)+\frac{6}{3!}u(u-1)(u-2),\qquad P(2.5)=-0.625.
$$

The formula's factors are not decorative: each new term vanishes at all earlier nodes, so adding a new difference term corrects the polynomial to fit the next data value without undoing previous matches. Near the last tabulated point, Newton's backward form uses $v=(x-x_n)/h$ and backward differences, arranging its products as $v(v+1)$, $v(v+1)(v+2)$, and so forth. For the same table, at $x=5.5$, $v=-0.5$, $\nabla y_6=46$, $\nabla^2 y_6=20$, and $\nabla^3 y_6=6$, so the cubic backward expression gives $P(5.5)=60.125$. The forward and backward forms are two organizations of the same unique interpolating polynomial; choose the one whose origin is near the requested $x$ to keep the dimensionless parameter small.

These later lessons complement, rather than replace, the earlier representations. Synthetic division efficiently tests a candidate linear factor and supplies a quotient; Lagrange's basis constructs a polynomial directly from node/value pairs; finite differences expose regular spacing and successive changes; Newton's forward/backward forms then make those differences the coefficients of a progressively built interpolant. Keeping these roles distinct prevents the common error of treating an interpolation formula as a division algorithm or assuming an equally spaced difference table applies to irregular nodes.
