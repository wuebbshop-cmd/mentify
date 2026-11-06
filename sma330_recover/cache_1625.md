## 1. Foundational Concepts, Definitions, and Axioms — Collocation, approximation, and the three lesson sequence

Given distinct nodes, the Vandermonde interpolation problem is nonsingular, yielding a unique polynomial of degree at most n. The Lagrange representation constructs it from cardinal functions; Newton’s representation is nested and exposes the incremental divided-difference coefficients. For equal spacing, forward differences encode those coefficients through factorial polynomials, while backward differences anchor the expansion at the terminal node. The representations are algebraically equivalent but have different data and evaluation conveniences.

Scope is deliberately bounded to lessons 4–6. The key results are collocation existence and uniqueness, the Lagrange formula, Taylor polynomial construction, finite-difference recursion and constant-difference property, Newton forward/backward formulas, and divided differences for unequally spaced data. We do not treat unrelated numerical integration or general root-solving. Error claims are conditional: interpolation error formulas need smoothness hypotheses; extrapolation can be poor; and approximate input values propagate through computed coefficients.

When auditing a derivation, retain node order, spacing, and indexing throughout. A forward table begins at the first node, a backward table at the last, and a divided-difference denominator spans the endpoints of its node subset. Most errors are not deep theorem failures but mismatched indices, incorrect spacing, an omitted factor of h, or a numerator and denominator using different node orderings.

## 2. Theorems, Lemmas, and Analytical Properties — Lagrange, Newton, and finite-difference definitions

Existence can be seen constructively from Lagrange basis functions; uniqueness follows from the root-count theorem. The interpolation error, when f is n+1 times continuously differentiable, has form f(x)-P_n(x)=f^(n+1)(ξ)/(n+1)! product_i(x-x_i) for some ξ in the interval. This explains exact agreement at nodes and why distance from nodes and higher derivatives affect error. The source’s Weierstrass result is different: it guarantees some polynomial approximation uniformly close to a continuous function on a compact interval, not necessarily the particular interpolant through a selected table.

Finite differences are discrete analogues of derivatives. If x_i=x_0+ih, then Δf_i=f_(i+1)-f_i; repeated application defines Δ^k. For a polynomial of degree m, Δ^m is constant and Δ^(m+1)=0. Newton forward interpolation follows from expressing values in the falling-factorial basis. The backward form follows by anchoring the same polynomial at x_n and using backward differences. This indexing distinction is essential at endpoints.

Unequal spacing replaces constant-step differences with divided differences. Their recursive denominators are x_(i+k)-x_i; changing node order changes intermediate coefficients but not the unique polynomial. Error bounds and diagnosis from rounded tables must be stated cautiously: near-constant high differences can indicate a low-degree model, but measurement and rounding noise prevents exact constancy in practice.

## 3. Formal Proofs, Derivations, and Methods — Construction, uniqueness, and error interpretation

A proof-oriented workflow separates construction, verification, and error interpretation. First identify node geometry and choose a representation. Then derive coefficients while preserving index conventions. Verify interpolation constraints exactly before simplifying. Finally state what the polynomial approximates and under what assumptions an error statement applies.

For equal spacing, define Δ recursively and form the triangular difference table. Newton’s forward basis is u(u-1)...(u-k+1)/k!, and the coefficient is Δ^k y_0. Backward interpolation uses a terminal anchor and backward differences, with basis v(v+1)...(v+k-1)/k!. For nonuniform data, use divided differences. Do not use a fixed h when gaps vary.

The Lagrange construction is direct but can be expensive to recompute after a new node; Newton form is incremental. Both are theoretically the same polynomial. Taylor polynomials use local derivative data rather than collocation values. Their remainder behavior is local and depends on derivatives; the source warns that accuracy can deteriorate away from the expansion point. A claimed error bound must name its smoothness interval and the derivative bound it uses.

## 4. Representative Worked Examples and Solutions — Checked data, interpolation, and polynomial examples

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

### 4.7 Lagrange construction from three nodes

Worked example 7 — Lagrange construction from three nodes. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The data are (0,-1), (1,0), and (2,1). Each node gets a cardinal polynomial. The denominators come from the corresponding node differences; checking the values at 0, 1, and 2 ensures the basis has the required one-at-its-own-node, zero-at-the-other-nodes behavior.

$$
L_0(x)=\frac{(x-1)(x-2)}2,\quad L_1(x)=-x(x-2),\quad L_2(x)=\frac{x(x-1)}2
$$

The interpolant is P(x)=-1L_0(x)+0L_1(x)+1L_2(x). Simplification gives P(x)=(0)x^2+(1)x+(-1); at x=1/2 it is -1/2. Re-substitution recovers all three ordinates. This example shows how the basis formula performs the construction rather than merely checking a polynomial guessed in advance.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.8 Newton forward formula on equal spacing

Worked example 8 — Newton forward formula on equal spacing. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

Here the nodes are 4, 6, 8, and 10, so h=2 and the forward parameter at x=7 is u=(7-4)/2=3/2. The table’s first differences are [4, 4, 4]; the second differences are [0, 0]; and the third difference is 0. These entries follow from subtracting adjacent values, not from dividing by h.

$$
P(x)=10+u(4)+\frac{u(u-1)}2(0)+\frac{u(u-1)(u-2)}6(0)
$$

Substituting u=3/2 gives P(7)=16. Because the data were generated from a quadratic, the third difference vanishes and the formula reduces to the quadratic terms. The four node substitutions reproduce the table. The calculation illustrates why equal spacing must be verified before reading a forward-difference column as Newton coefficients.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.9 Newton backward formula near the last node

Worked example 9 — Newton backward formula near the last node. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The table is equally spaced with h=1, and the target x=5/2 lies half a step before the last node x_3=3. Thus v=(x-x_3)/h=-1/2. The terminal value is y_3=6; the last backward first difference is 2, and the last backward second difference is 0. Since the data are quadratic, higher differences vanish.

$$
P(x)=y_3+v\nabla y_3+\frac{v(v+1)}2\nabla^2 y_3
= 6+v(2)+\frac{v(v+1)}2(0)
$$

Evaluation gives P(5/2)=5. This is the same unique polynomial that a forward formula would produce, but the terminal anchor keeps the relevant differences at the end of the table. Replacing v by (x-x_0)/h would mix two different conventions.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.10 Divided differences for unequal nodes

Worked example 10 — Divided differences for unequal nodes. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The data use nodes 0, 1, 2, and 4; the last gap is two, so a constant-step forward table is not applicable. The first divided differences are [4.0, 10.0, 19.0], the second are [3.0, 3.0], and the third is 0.0. Each denominator spans the outer nodes of the divided-difference entry.

$$
P(x)=-1+(4.0)(x-0)+(3.0)(x-0)(x-1)+(0.0)(x-0)(x-1)(x-2)
$$

At x=3 the value is 29. Substituting x=0,1,2,4 returns the four data values. Divided differences retain the actual unequal spacings and produce a Newton polynomial whose leading diagonal entries are its coefficients.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.11 Maclaurin approximation to cosine

Worked example 11 — Maclaurin approximation to cosine. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

A Taylor polynomial is fitted to derivative information at its center, not to a list of function values. At zero, the successive derivatives of the selected function have values 1, 0, -1, and 0. Dividing each derivative value by its factorial gives the cubic coefficients; a zero derivative removes the corresponding power.

$$
P_3(x)=1-x^2/2,\qquad P_3(0.2)\approx 0.98000000
$$

For comparison, the function value is 0.98006658, so the absolute discrepancy is 6.66e-05. The source’s sine calculation gives x-x^3/6 and approximately 0.0998333 at 0.1. Agreement near the center is expected; it does not imply the same accuracy far away, since the omitted terms grow with distance.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.12 Using constant second differences to audit a misprint

Worked example 12 — Using constant second differences to audit a misprint. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

Suppose equally spaced integer abscissae 0 through 4 are expected to follow a quadratic trend, but the listed ordinates are [0, 3, 13, 15, 24]. A quadratic has constant second differences. The observed second differences are [7, -8, 7], so the middle value is suspect. If the expected constant is 2, solving the middle second-difference equation gives the corrected ordinate 8.

$$
\Delta^2y_0=y_2-2y_1+y_0,\qquad
\Delta^2y_1=y_3-2y_2+y_1
$$

Replacing only the suspect entry gives second differences [2, 2, 2]. This is a plausible correction under the stated quadratic assumption, not a conclusion available from data alone. Without a degree or smoothness model, any finite list can be interpolated exactly by a sufficiently high-degree polynomial. State the assumption that makes a correction identifiable.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.13 Lagrange construction from three nodes

Worked example 13 — Lagrange construction from three nodes. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The data are (0,0), (1,0), and (2,4). Each node gets a cardinal polynomial. The denominators come from the corresponding node differences; checking the values at 0, 1, and 2 ensures the basis has the required one-at-its-own-node, zero-at-the-other-nodes behavior.

$$
L_0(x)=\frac{(x-1)(x-2)}2,\quad L_1(x)=-x(x-2),\quad L_2(x)=\frac{x(x-1)}2
$$

The interpolant is P(x)=0L_0(x)+0L_1(x)+4L_2(x). Simplification gives P(x)=(2)x^2+(-2)x+(0); at x=1/2 it is -1/2. Re-substitution recovers all three ordinates. This example shows how the basis formula performs the construction rather than merely checking a polynomial guessed in advance.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.14 Newton forward formula on equal spacing

Worked example 14 — Newton forward formula on equal spacing. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

Here the nodes are 4, 6, 8, and 10, so h=2 and the forward parameter at x=7 is u=(7-4)/2=3/2. The table’s first differences are [38, 54, 70]; the second differences are [16, 16]; and the third difference is 0. These entries follow from subtracting adjacent values, not from dividing by h.

$$
P(x)=28+u(38)+\frac{u(u-1)}2(16)+\frac{u(u-1)(u-2)}6(0)
$$

Substituting u=3/2 gives P(7)=91. Because the data were generated from a quadratic, the third difference vanishes and the formula reduces to the quadratic terms. The four node substitutions reproduce the table. The calculation illustrates why equal spacing must be verified before reading a forward-difference column as Newton coefficients.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.15 Newton backward formula near the last node

Worked example 15 — Newton backward formula near the last node. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The table is equally spaced with h=1, and the target x=5/2 lies half a step before the last node x_3=3. Thus v=(x-x_3)/h=-1/2. The terminal value is y_3=2; the last backward first difference is 0, and the last backward second difference is 0. Since the data are quadratic, higher differences vanish.

$$
P(x)=y_3+v\nabla y_3+\frac{v(v+1)}2\nabla^2 y_3
= 2+v(0)+\frac{v(v+1)}2(0)
$$

Evaluation gives P(5/2)=2. This is the same unique polynomial that a forward formula would produce, but the terminal anchor keeps the relevant differences at the end of the table. Replacing v by (x-x_0)/h would mix two different conventions.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.16 Divided differences for unequal nodes

Worked example 16 — Divided differences for unequal nodes. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The data use nodes 0, 1, 2, and 4; the last gap is two, so a constant-step forward table is not applicable. The first divided differences are [0.0, 12.0, 54.0], the second are [6.0, 14.0], and the third is 2.0. Each denominator spans the outer nodes of the divided-difference entry.

$$
P(x)=-1+(0.0)(x-0)+(6.0)(x-0)(x-1)+(2.0)(x-0)(x-1)(x-2)
$$

At x=3 the value is 47. Substituting x=0,1,2,4 returns the four data values. Divided differences retain the actual unequal spacings and produce a Newton polynomial whose leading diagonal entries are its coefficients.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.17 Taylor approximation to the exponential

Worked example 17 — Taylor approximation to the exponential. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

A Taylor polynomial is fitted to derivative information at its center, not to a list of function values. At zero, the successive derivatives of the selected function have values 1, 1, 1, and 1. Dividing each derivative value by its factorial gives the cubic coefficients; a zero derivative removes the corresponding power.

$$
P_3(x)=1+x+x^2/2+x^3/6,\qquad P_3(0.1)\approx 1.10516667
$$

For comparison, the function value is 1.10517092, so the absolute discrepancy is 4.25e-06. The source’s sine calculation gives x-x^3/6 and approximately 0.0998333 at 0.1. Agreement near the center is expected; it does not imply the same accuracy far away, since the omitted terms grow with distance.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.18 Using constant second differences to audit a misprint

Worked example 18 — Using constant second differences to audit a misprint. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

Suppose equally spaced integer abscissae 0 through 4 are expected to follow a quadratic trend, but the listed ordinates are [0, 3, 13, 15, 24]. A quadratic has constant second differences. The observed second differences are [7, -8, 7], so the middle value is suspect. If the expected constant is 2, solving the middle second-difference equation gives the corrected ordinate 8.

$$
\Delta^2y_0=y_2-2y_1+y_0,\qquad
\Delta^2y_1=y_3-2y_2+y_1
$$

Replacing only the suspect entry gives second differences [2, 2, 2]. This is a plausible correction under the stated quadratic assumption, not a conclusion available from data alone. Without a degree or smoothness model, any finite list can be interpolated exactly by a sufficiently high-degree polynomial. State the assumption that makes a correction identifiable.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.19 Lagrange construction from three nodes

Worked example 19 — Lagrange construction from three nodes. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The data are (0,1), (1,2), and (2,1). Each node gets a cardinal polynomial. The denominators come from the corresponding node differences; checking the values at 0, 1, and 2 ensures the basis has the required one-at-its-own-node, zero-at-the-other-nodes behavior.

$$
L_0(x)=\frac{(x-1)(x-2)}2,\quad L_1(x)=-x(x-2),\quad L_2(x)=\frac{x(x-1)}2
$$

The interpolant is P(x)=1L_0(x)+2L_1(x)+1L_2(x). Simplification gives P(x)=(-1)x^2+(2)x+(1); at x=1/2 it is 7/4. Re-substitution recovers all three ordinates. This example shows how the basis formula performs the construction rather than merely checking a polynomial guessed in advance.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.20 Newton forward formula on equal spacing

Worked example 20 — Newton forward formula on equal spacing. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

Here the nodes are 4, 6, 8, and 10, so h=2 and the forward parameter at x=7 is u=(7-4)/2=3/2. The table’s first differences are [2, 2, 2]; the second differences are [0, 0]; and the third difference is 0. These entries follow from subtracting adjacent values, not from dividing by h.

$$
P(x)=6+u(2)+\frac{u(u-1)}2(0)+\frac{u(u-1)(u-2)}6(0)
$$

Substituting u=3/2 gives P(7)=9. Because the data were generated from a quadratic, the third difference vanishes and the formula reduces to the quadratic terms. The four node substitutions reproduce the table. The calculation illustrates why equal spacing must be verified before reading a forward-difference column as Newton coefficients.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.21 Newton backward formula near the last node

Worked example 21 — Newton backward formula near the last node. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The table is equally spaced with h=1, and the target x=5/2 lies half a step before the last node x_3=3. Thus v=(x-x_3)/h=-1/2. The terminal value is y_3=-6; the last backward first difference is -2, and the last backward second difference is 0. Since the data are quadratic, higher differences vanish.

$$
P(x)=y_3+v\nabla y_3+\frac{v(v+1)}2\nabla^2 y_3
= -6+v(-2)+\frac{v(v+1)}2(0)
$$

Evaluation gives P(5/2)=-5. This is the same unique polynomial that a forward formula would produce, but the terminal anchor keeps the relevant differences at the end of the table. Replacing v by (x-x_0)/h would mix two different conventions.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.22 Divided differences for unequal nodes

Worked example 22 — Divided differences for unequal nodes. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The data use nodes 0, 1, 2, and 4; the last gap is two, so a constant-step forward table is not applicable. The first divided differences are [-3.0, -9.0, -18.0], the second are [-3.0, -3.0], and the third is 0.0. Each denominator spans the outer nodes of the divided-difference entry.

$$
P(x)=-1+(-3.0)(x-0)+(-3.0)(x-0)(x-1)+(0.0)(x-0)(x-1)(x-2)
$$

At x=3 the value is -28. Substituting x=0,1,2,4 returns the four data values. Divided differences retain the actual unequal spacings and produce a Newton polynomial whose leading diagonal entries are its coefficients.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.23 Maclaurin approximation to sine

Worked example 23 — Maclaurin approximation to sine. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

A Taylor polynomial is fitted to derivative information at its center, not to a list of function values. At zero, the successive derivatives of the selected function have values 0, 1, 0, and -1. Dividing each derivative value by its factorial gives the cubic coefficients; a zero derivative removes the corresponding power.

$$
P_3(x)=x-x^3/6,\qquad P_3(0.1)\approx 0.09983333
$$

For comparison, the function value is 0.09983342, so the absolute discrepancy is 8.33e-08. The source’s sine calculation gives x-x^3/6 and approximately 0.0998333 at 0.1. Agreement near the center is expected; it does not imply the same accuracy far away, since the omitted terms grow with distance.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.24 Using constant second differences to audit a misprint

Worked example 24 — Using constant second differences to audit a misprint. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

Suppose equally spaced integer abscissae 0 through 4 are expected to follow a quadratic trend, but the listed ordinates are [0, 3, 13, 15, 24]. A quadratic has constant second differences. The observed second differences are [7, -8, 7], so the middle value is suspect. If the expected constant is 2, solving the middle second-difference equation gives the corrected ordinate 8.

$$
\Delta^2y_0=y_2-2y_1+y_0,\qquad
\Delta^2y_1=y_3-2y_2+y_1
$$

Replacing only the suspect entry gives second differences [2, 2, 2]. This is a plausible correction under the stated quadratic assumption, not a conclusion available from data alone. Without a degree or smoothness model, any finite list can be interpolated exactly by a sufficiently high-degree polynomial. State the assumption that makes a correction identifiable.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.25 Lagrange construction from three nodes

Worked example 25 — Lagrange construction from three nodes. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The data are (0,2), (1,2), and (2,4). Each node gets a cardinal polynomial. The denominators come from the corresponding node differences; checking the values at 0, 1, and 2 ensures the basis has the required one-at-its-own-node, zero-at-the-other-nodes behavior.

$$
L_0(x)=\frac{(x-1)(x-2)}2,\quad L_1(x)=-x(x-2),\quad L_2(x)=\frac{x(x-1)}2
$$

The interpolant is P(x)=2L_0(x)+2L_1(x)+4L_2(x). Simplification gives P(x)=(1)x^2+(-1)x+(2); at x=1/2 it is 7/4. Re-substitution recovers all three ordinates. This example shows how the basis formula performs the construction rather than merely checking a polynomial guessed in advance.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.26 Newton forward formula on equal spacing

Worked example 26 — Newton forward formula on equal spacing. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

Here the nodes are 4, 6, 8, and 10, so h=2 and the forward parameter at x=7 is u=(7-4)/2=3/2. The table’s first differences are [36, 52, 68]; the second differences are [16, 16]; and the third difference is 0. These entries follow from subtracting adjacent values, not from dividing by h.

$$
P(x)=24+u(36)+\frac{u(u-1)}2(16)+\frac{u(u-1)(u-2)}6(0)
$$

Substituting u=3/2 gives P(7)=84. Because the data were generated from a quadratic, the third difference vanishes and the formula reduces to the quadratic terms. The four node substitutions reproduce the table. The calculation illustrates why equal spacing must be verified before reading a forward-difference column as Newton coefficients.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.27 Newton backward formula near the last node

Worked example 27 — Newton backward formula near the last node. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The table is equally spaced with h=1, and the target x=5/2 lies half a step before the last node x_3=3. Thus v=(x-x_3)/h=-1/2. The terminal value is y_3=5; the last backward first difference is 1, and the last backward second difference is 0. Since the data are quadratic, higher differences vanish.

$$
P(x)=y_3+v\nabla y_3+\frac{v(v+1)}2\nabla^2 y_3
= 5+v(1)+\frac{v(v+1)}2(0)
$$

Evaluation gives P(5/2)=9/2. This is the same unique polynomial that a forward formula would produce, but the terminal anchor keeps the relevant differences at the end of the table. Replacing v by (x-x_0)/h would mix two different conventions.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.28 Divided differences for unequal nodes

Worked example 28 — Divided differences for unequal nodes. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The data use nodes 0, 1, 2, and 4; the last gap is two, so a constant-step forward table is not applicable. The first divided differences are [5.0, 19.0, 64.0], the second are [7.0, 15.0], and the third is 2.0. Each denominator spans the outer nodes of the divided-difference entry.

$$
P(x)=-1+(5.0)(x-0)+(7.0)(x-0)(x-1)+(2.0)(x-0)(x-1)(x-2)
$$

At x=3 the value is 68. Substituting x=0,1,2,4 returns the four data values. Divided differences retain the actual unequal spacings and produce a Newton polynomial whose leading diagonal entries are its coefficients.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.29 Maclaurin approximation to cosine

Worked example 29 — Maclaurin approximation to cosine. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

A Taylor polynomial is fitted to derivative information at its center, not to a list of function values. At zero, the successive derivatives of the selected function have values 1, 0, -1, and 0. Dividing each derivative value by its factorial gives the cubic coefficients; a zero derivative removes the corresponding power.

$$
P_3(x)=1-x^2/2,\qquad P_3(0.2)\approx 0.98000000
$$

For comparison, the function value is 0.98006658, so the absolute discrepancy is 6.66e-05. The source’s sine calculation gives x-x^3/6 and approximately 0.0998333 at 0.1. Agreement near the center is expected; it does not imply the same accuracy far away, since the omitted terms grow with distance.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.30 Using constant second differences to audit a misprint

Worked example 30 — Using constant second differences to audit a misprint. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

Suppose equally spaced integer abscissae 0 through 4 are expected to follow a quadratic trend, but the listed ordinates are [0, 3, 13, 15, 24]. A quadratic has constant second differences. The observed second differences are [7, -8, 7], so the middle value is suspect. If the expected constant is 2, solving the middle second-difference equation gives the corrected ordinate 8.

$$
\Delta^2y_0=y_2-2y_1+y_0,\qquad
\Delta^2y_1=y_3-2y_2+y_1
$$

Replacing only the suspect entry gives second differences [2, 2, 2]. This is a plausible correction under the stated quadratic assumption, not a conclusion available from data alone. Without a degree or smoothness model, any finite list can be interpolated exactly by a sufficiently high-degree polynomial. State the assumption that makes a correction identifiable.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.31 Lagrange construction from three nodes

Worked example 31 — Lagrange construction from three nodes. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The data are (0,-2), (1,-1), and (2,-4). Each node gets a cardinal polynomial. The denominators come from the corresponding node differences; checking the values at 0, 1, and 2 ensures the basis has the required one-at-its-own-node, zero-at-the-other-nodes behavior.

$$
L_0(x)=\frac{(x-1)(x-2)}2,\quad L_1(x)=-x(x-2),\quad L_2(x)=\frac{x(x-1)}2
$$

The interpolant is P(x)=-2L_0(x)+-1L_1(x)+-4L_2(x). Simplification gives P(x)=(-2)x^2+(3)x+(-2); at x=1/2 it is -1. Re-substitution recovers all three ordinates. This example shows how the basis formula performs the construction rather than merely checking a polynomial guessed in advance.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.32 Newton forward formula on equal spacing

Worked example 32 — Newton forward formula on equal spacing. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

Here the nodes are 4, 6, 8, and 10, so h=2 and the forward parameter at x=7 is u=(7-4)/2=3/2. The table’s first differences are [0, 0, 0]; the second differences are [0, 0]; and the third difference is 0. These entries follow from subtracting adjacent values, not from dividing by h.

$$
P(x)=2+u(0)+\frac{u(u-1)}2(0)+\frac{u(u-1)(u-2)}6(0)
$$

Substituting u=3/2 gives P(7)=2. Because the data were generated from a quadratic, the third difference vanishes and the formula reduces to the quadratic terms. The four node substitutions reproduce the table. The calculation illustrates why equal spacing must be verified before reading a forward-difference column as Newton coefficients.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.33 Newton backward formula near the last node

Worked example 33 — Newton backward formula near the last node. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The table is equally spaced with h=1, and the target x=5/2 lies half a step before the last node x_3=3. Thus v=(x-x_3)/h=-1/2. The terminal value is y_3=-3; the last backward first difference is -1, and the last backward second difference is 0. Since the data are quadratic, higher differences vanish.

$$
P(x)=y_3+v\nabla y_3+\frac{v(v+1)}2\nabla^2 y_3
= -3+v(-1)+\frac{v(v+1)}2(0)
$$

Evaluation gives P(5/2)=-5/2. This is the same unique polynomial that a forward formula would produce, but the terminal anchor keeps the relevant differences at the end of the table. Replacing v by (x-x_0)/h would mix two different conventions.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

### 4.34 Divided differences for unequal nodes

Worked example 34 — Divided differences for unequal nodes. The goal is to expose the derivation as well as the answer. Each coefficient is tied to a specific basis term, and the stated node pattern determines whether ordinary finite differences or divided differences are appropriate.

The data use nodes 0, 1, 2, and 4; the last gap is two, so a constant-step forward table is not applicable. The first divided differences are [-3.0, -7.0, -13.0], the second are [-2.0, -2.0], and the third is 0.0. Each denominator spans the outer nodes of the divided-difference entry.

$$
P(x)=-1+(-3.0)(x-0)+(-2.0)(x-0)(x-1)+(0.0)(x-0)(x-1)(x-2)
$$

At x=3 the value is -22. Substituting x=0,1,2,4 returns the four data values. Divided differences retain the actual unequal spacings and produce a Newton polynomial whose leading diagonal entries are its coefficients.

Verification against defining conditions is a compact proof of correctness. Error interpretation is separate: a correct interpolant can still be a poor model between widely separated nodes or outside the data interval.

## 5. Mathematical Extensions, Limits, and Common Errors — Method selection, verification, and source limits

Method selection is determined by the data geometry: Lagrange is general for distinct nodes; Newton divided differences are incremental and nonuniform; Newton forward/backward use equal spacing and are most convenient near their anchor; Taylor uses derivatives at one center. No formula can be selected responsibly without first checking the nodes.

Error interpretation is conditional. The interpolation remainder involves f^(n+1)(ξ) and the product of node distances; smoothness and interval location matter. Uniform polynomial approximation for a continuous function is an existence theorem and does not identify a particular interpolant. Rounded finite-difference tables can obscure exact constant-difference patterns and may amplify measurement noise.

Source caution: the OCR-extracted Lagrange sample on fractional nodes is incomplete and corrupted, so its coefficients cannot be verified reliably. It is not reproduced as a worked answer. The legible lesson 6 four-node example is checked directly; the forward-difference values are 2,5,12; 3,7; and 4. Always distinguish a demonstrable calculation from a damaged source fragment.