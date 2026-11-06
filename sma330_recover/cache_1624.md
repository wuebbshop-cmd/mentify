## 1. Foundational Concepts, Definitions, and Axioms — Collocation, approximation, and the three lesson sequence

Interpolation converts discrete observations into a polynomial model. For distinct abscissae x_0,...,x_n and ordinates y_i, there is exactly one polynomial of degree at most n with P(x_i)=y_i. Lagrange’s cardinal basis gives a direct formula; Newton’s form organizes the same result using differences. Equally spaced nodes enable forward and backward finite-difference formulas; unequal spacing calls for divided differences or Lagrange basis construction.

The approved lessons explicitly distinguish collocation from approximation. A collocation polynomial matches supplied function values at nodes. Taylor approximation matches derivative information at a selected center; the source’s sin x example uses values of successive derivatives at zero and evaluates the cubic near zero. The Weierstrass approximation statement is about the existence of a polynomial uniformly close to a continuous function on a closed interval; it does not assert that every interpolation polynomial of arbitrary degree is automatically accurate.

Finite differences also have a diagnostic role. The k-th forward differences are obtained by repeated subtraction of adjacent entries. For equally spaced nodes, a polynomial of degree m has constant m-th differences and zero higher differences in exact arithmetic. Rounded or erroneous data perturb this pattern, so tables can suggest a misprint but do not identify it without a model or additional information.

## 2. Theorems, Lemmas, and Analytical Properties — Lagrange, Newton, and finite-difference definitions

The Lagrange cardinal polynomial is L_i(x)=product over j≠i of (x-x_j)/(x_i-x_j). It satisfies L_i(x_k)=δ_ik, so P_n(x)=sum y_i L_i(x) interpolates. Uniqueness follows because the difference of two degree-at-most-n interpolants would have n+1 distinct roots while its degree is at most n, forcing it to be zero.

Newton’s divided differences are recursive: f[x_i]=f(x_i), f[x_i,x_(i+1)]=(f_(i+1)-f_i)/(x_(i+1)-x_i), and higher orders subtract adjacent lower-order differences and divide by the span between outer nodes. The resulting polynomial adds terms successively: f[x_0]+f[x_0,x_1](x-x_0)+... . A new node appends a new term without rebuilding prior coefficients.

For equal spacing, Δ^k y_i is the k-th forward difference. Newton’s forward interpolation polynomial is y_0+uΔy_0+u(u-1)Δ²y_0/2!+... . The backward formula is anchored at x_n, with v=(x-x_n)/h and backward differences at the end of the table. These forms are not interchangeable without re-indexing. For a degree-m polynomial, its m-th finite differences are constant and all higher differences vanish under exact arithmetic; this is a useful table check.

## 3. Formal Proofs, Derivations, and Methods — Construction, uniqueness, and error interpretation

For Newton forward interpolation, set u=(x-x_0)/h and read the first entry in each forward-difference column. Evaluate the polynomial in nested form when possible. For backward interpolation, set v=(x-x_n)/h and read terminal backward differences. The alternating falling products are formed from v, v+1, v+2,...; derive the pattern from the table’s indexing rather than memorizing isolated signs.

For a divided-difference table, use each actual x gap. The leading diagonal values f[x_0], f[x_0,x_1], ... become coefficients. Verify the constructed polynomial at all nodes; for a non-tabular query, state that it is interpolation only if the query lies within the node range.

For Taylor approximation about x_0, determine coefficients from P^(k)(x_0)=f^(k)(x_0). The coefficient of (x-x_0)^k is f^(k)(x_0)/k!. The source’s sin x cubic at zero uses sin(0)=0, cos(0)=1, and alternating higher derivatives, giving x-x^3/6. Evaluate at 0.1 and compare with a known accurate value only as a check, not as the derivation.

## 4. Representative Worked Examples and Solutions — Checked data, interpolation, and polynomial examples

### 4.1 Lagrange construction from three nodes

Worked example 1 — Lagrange construction from three nodes. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The data are (0,-2), (1,-7), and (2,-16). Each node gets a cardinal polynomial. The denominators come from the corresponding node differences; checking the values at 0, 1, and 2 ensures the basis has the required one-at-its-own-node, zero-at-the-other-nodes behavior.

$$
L_0(x)=\frac{(x-1)(x-2)}2,\quad L_1(x)=-x(x-2),\quad L_2(x)=\frac{x(x-1)}2
$$

The interpolant is P(x)=-2L_0(x)+-7L_1(x)+-16L_2(x). Simplification gives P(x)=(-2)x^2+(-3)x+(-2); at x=1/2 it is -4. Re-substitution recovers all three ordinates. This example shows how the basis formula performs the construction rather than merely checking a polynomial guessed in advance.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.2 Newton forward formula on equal spacing

Worked example 2 — Newton forward formula on equal spacing. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

Here the nodes are 4, 6, 8, and 10, so h=2 and the forward parameter at x=7 is u=(7-4)/2=3/2. The table’s first differences are [40, 56, 72]; the second differences are [16, 16]; and the third difference is 0. These entries follow from subtracting adjacent values, not from dividing by h.

$$
P(x)=32+u(40)+\frac{u(u-1)}2(16)+\frac{u(u-1)(u-2)}6(0)
$$

Substituting u=3/2 gives P(7)=98. Because the data were generated from a quadratic, the third difference vanishes and the formula reduces to the quadratic terms. The four node substitutions reproduce the table. The calculation illustrates why equal spacing must be verified before reading a forward-difference column as Newton coefficients.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.3 Newton backward formula near the last node

Worked example 3 — Newton backward formula near the last node. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The table is equally spaced with h=1, and the target x=5/2 lies half a step before the last node x_3=3. Thus v=(x-x_3)/h=-1/2. The terminal value is y_3=-1; the last backward first difference is -1, and the last backward second difference is 0. Since the data are quadratic, higher differences vanish.

$$
P(x)=y_3+v\nabla y_3+\frac{v(v+1)}2\nabla^2 y_3
= -1+v(-1)+\frac{v(v+1)}2(0)
$$

Evaluation gives P(5/2)=-1/2. This is the same unique polynomial that a forward formula would produce, but the terminal anchor keeps the relevant differences at the end of the table. Replacing v by (x-x_0)/h would mix two different conventions.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.4 Divided differences for unequal nodes

Worked example 4 — Divided differences for unequal nodes. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The data use nodes 0, 1, 2, and 4; the last gap is two, so a constant-step forward table is not applicable. The first divided differences are [0.0, 10.0, 49.0], the second are [5.0, 13.0], and the third is 2.0. Each denominator spans the outer nodes of the divided-difference entry.

$$
P(x)=-1+(0.0)(x-0)+(5.0)(x-0)(x-1)+(2.0)(x-0)(x-1)(x-2)
$$

At x=3 the value is 41. Substituting x=0,1,2,4 returns the four data values. Divided differences retain the actual unequal spacings and produce a Newton polynomial whose leading diagonal entries are its coefficients.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.5 Maclaurin approximation to sine

Worked example 5 — Maclaurin approximation to sine. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

A Taylor polynomial is fitted to derivative information at its center, not to a list of function values. At zero, the successive derivatives of the selected function have values 0, 1, 0, and -1. Dividing each derivative value by its factorial gives the cubic coefficients; a zero derivative removes the corresponding power.

$$
P_3(x)=x-x^3/6,\qquad P_3(0.1)\approx 0.09983333
$$

For comparison, the function value is 0.09983342, so the absolute discrepancy is 8.33e-08. The source’s sine calculation gives x-x^3/6 and approximately 0.0998333 at 0.1. Agreement near the center is expected; it does not imply the same accuracy far away, since the omitted terms grow with distance.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.6 Using constant second differences to audit a misprint

Worked example 6 — Using constant second differences to audit a misprint. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

Suppose equally spaced integer abscissae 0 through 4 are expected to follow a quadratic trend, but the listed ordinates are [0, 3, 13, 15, 24]. A quadratic has constant second differences. The observed second differences are [7, -8, 7], so the middle value is suspect. If the expected constant is 2, solving the middle second-difference equation gives the corrected ordinate 8.

$$
\Delta^2y_0=y_2-2y_1+y_0,\qquad
\Delta^2y_1=y_3-2y_2+y_1
$$

Replacing only the suspect entry gives second differences [2, 2, 2]. This is a plausible correction under the stated quadratic assumption, not a conclusion available from data alone. Without a degree or smoothness model, any finite list can be interpolated exactly by a sufficiently high-degree polynomial. State the assumption that makes a correction identifiable.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.7 Lagrange construction from three nodes

Worked example 7 — Lagrange construction from three nodes. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The data are (0,-1), (1,0), and (2,1). Each node gets a cardinal polynomial. The denominators come from the corresponding node differences; checking the values at 0, 1, and 2 ensures the basis has the required one-at-its-own-node, zero-at-the-other-nodes behavior.

$$
L_0(x)=\frac{(x-1)(x-2)}2,\quad L_1(x)=-x(x-2),\quad L_2(x)=\frac{x(x-1)}2
$$

The interpolant is P(x)=-1L_0(x)+0L_1(x)+1L_2(x). Simplification gives P(x)=(0)x^2+(1)x+(-1); at x=1/2 it is -1/2. Re-substitution recovers all three ordinates. This example shows how the basis formula performs the construction rather than merely checking a polynomial guessed in advance.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.8 Newton forward formula on equal spacing

Worked example 8 — Newton forward formula on equal spacing. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

Here the nodes are 4, 6, 8, and 10, so h=2 and the forward parameter at x=7 is u=(7-4)/2=3/2. The table’s first differences are [4, 4, 4]; the second differences are [0, 0]; and the third difference is 0. These entries follow from subtracting adjacent values, not from dividing by h.

$$
P(x)=10+u(4)+\frac{u(u-1)}2(0)+\frac{u(u-1)(u-2)}6(0)
$$

Substituting u=3/2 gives P(7)=16. Because the data were generated from a quadratic, the third difference vanishes and the formula reduces to the quadratic terms. The four node substitutions reproduce the table. The calculation illustrates why equal spacing must be verified before reading a forward-difference column as Newton coefficients.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.9 Newton backward formula near the last node

Worked example 9 — Newton backward formula near the last node. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The table is equally spaced with h=1, and the target x=5/2 lies half a step before the last node x_3=3. Thus v=(x-x_3)/h=-1/2. The terminal value is y_3=6; the last backward first difference is 2, and the last backward second difference is 0. Since the data are quadratic, higher differences vanish.

$$
P(x)=y_3+v\nabla y_3+\frac{v(v+1)}2\nabla^2 y_3
= 6+v(2)+\frac{v(v+1)}2(0)
$$

Evaluation gives P(5/2)=5. This is the same unique polynomial that a forward formula would produce, but the terminal anchor keeps the relevant differences at the end of the table. Replacing v by (x-x_0)/h would mix two different conventions.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.10 Divided differences for unequal nodes

Worked example 10 — Divided differences for unequal nodes. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The data use nodes 0, 1, 2, and 4; the last gap is two, so a constant-step forward table is not applicable. The first divided differences are [4.0, 10.0, 19.0], the second are [3.0, 3.0], and the third is 0.0. Each denominator spans the outer nodes of the divided-difference entry.

$$
P(x)=-1+(4.0)(x-0)+(3.0)(x-0)(x-1)+(0.0)(x-0)(x-1)(x-2)
$$

At x=3 the value is 29. Substituting x=0,1,2,4 returns the four data values. Divided differences retain the actual unequal spacings and produce a Newton polynomial whose leading diagonal entries are its coefficients.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.11 Maclaurin approximation to cosine

Worked example 11 — Maclaurin approximation to cosine. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

A Taylor polynomial is fitted to derivative information at its center, not to a list of function values. At zero, the successive derivatives of the selected function have values 1, 0, -1, and 0. Dividing each derivative value by its factorial gives the cubic coefficients; a zero derivative removes the corresponding power.

$$
P_3(x)=1-x^2/2,\qquad P_3(0.2)\approx 0.98000000
$$

For comparison, the function value is 0.98006658, so the absolute discrepancy is 6.66e-05. The source’s sine calculation gives x-x^3/6 and approximately 0.0998333 at 0.1. Agreement near the center is expected; it does not imply the same accuracy far away, since the omitted terms grow with distance.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.12 Using constant second differences to audit a misprint

Worked example 12 — Using constant second differences to audit a misprint. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

Suppose equally spaced integer abscissae 0 through 4 are expected to follow a quadratic trend, but the listed ordinates are [0, 3, 13, 15, 24]. A quadratic has constant second differences. The observed second differences are [7, -8, 7], so the middle value is suspect. If the expected constant is 2, solving the middle second-difference equation gives the corrected ordinate 8.

$$
\Delta^2y_0=y_2-2y_1+y_0,\qquad
\Delta^2y_1=y_3-2y_2+y_1
$$

Replacing only the suspect entry gives second differences [2, 2, 2]. This is a plausible correction under the stated quadratic assumption, not a conclusion available from data alone. Without a degree or smoothness model, any finite list can be interpolated exactly by a sufficiently high-degree polynomial. State the assumption that makes a correction identifiable.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.13 Lagrange construction from three nodes

Worked example 13 — Lagrange construction from three nodes. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The data are (0,0), (1,0), and (2,4). Each node gets a cardinal polynomial. The denominators come from the corresponding node differences; checking the values at 0, 1, and 2 ensures the basis has the required one-at-its-own-node, zero-at-the-other-nodes behavior.

$$
L_0(x)=\frac{(x-1)(x-2)}2,\quad L_1(x)=-x(x-2),\quad L_2(x)=\frac{x(x-1)}2
$$

The interpolant is P(x)=0L_0(x)+0L_1(x)+4L_2(x). Simplification gives P(x)=(2)x^2+(-2)x+(0); at x=1/2 it is -1/2. Re-substitution recovers all three ordinates. This example shows how the basis formula performs the construction rather than merely checking a polynomial guessed in advance.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.14 Newton forward formula on equal spacing

Worked example 14 — Newton forward formula on equal spacing. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

Here the nodes are 4, 6, 8, and 10, so h=2 and the forward parameter at x=7 is u=(7-4)/2=3/2. The table’s first differences are [38, 54, 70]; the second differences are [16, 16]; and the third difference is 0. These entries follow from subtracting adjacent values, not from dividing by h.

$$
P(x)=28+u(38)+\frac{u(u-1)}2(16)+\frac{u(u-1)(u-2)}6(0)
$$

Substituting u=3/2 gives P(7)=91. Because the data were generated from a quadratic, the third difference vanishes and the formula reduces to the quadratic terms. The four node substitutions reproduce the table. The calculation illustrates why equal spacing must be verified before reading a forward-difference column as Newton coefficients.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.15 Newton backward formula near the last node

Worked example 15 — Newton backward formula near the last node. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The table is equally spaced with h=1, and the target x=5/2 lies half a step before the last node x_3=3. Thus v=(x-x_3)/h=-1/2. The terminal value is y_3=2; the last backward first difference is 0, and the last backward second difference is 0. Since the data are quadratic, higher differences vanish.

$$
P(x)=y_3+v\nabla y_3+\frac{v(v+1)}2\nabla^2 y_3
= 2+v(0)+\frac{v(v+1)}2(0)
$$

Evaluation gives P(5/2)=2. This is the same unique polynomial that a forward formula would produce, but the terminal anchor keeps the relevant differences at the end of the table. Replacing v by (x-x_0)/h would mix two different conventions.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.16 Divided differences for unequal nodes

Worked example 16 — Divided differences for unequal nodes. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The data use nodes 0, 1, 2, and 4; the last gap is two, so a constant-step forward table is not applicable. The first divided differences are [0.0, 12.0, 54.0], the second are [6.0, 14.0], and the third is 2.0. Each denominator spans the outer nodes of the divided-difference entry.

$$
P(x)=-1+(0.0)(x-0)+(6.0)(x-0)(x-1)+(2.0)(x-0)(x-1)(x-2)
$$

At x=3 the value is 47. Substituting x=0,1,2,4 returns the four data values. Divided differences retain the actual unequal spacings and produce a Newton polynomial whose leading diagonal entries are its coefficients.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.17 Taylor approximation to the exponential

Worked example 17 — Taylor approximation to the exponential. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

A Taylor polynomial is fitted to derivative information at its center, not to a list of function values. At zero, the successive derivatives of the selected function have values 1, 1, 1, and 1. Dividing each derivative value by its factorial gives the cubic coefficients; a zero derivative removes the corresponding power.

$$
P_3(x)=1+x+x^2/2+x^3/6,\qquad P_3(0.1)\approx 1.10516667
$$

For comparison, the function value is 1.10517092, so the absolute discrepancy is 4.25e-06. The source’s sine calculation gives x-x^3/6 and approximately 0.0998333 at 0.1. Agreement near the center is expected; it does not imply the same accuracy far away, since the omitted terms grow with distance.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.18 Using constant second differences to audit a misprint

Worked example 18 — Using constant second differences to audit a misprint. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

Suppose equally spaced integer abscissae 0 through 4 are expected to follow a quadratic trend, but the listed ordinates are [0, 3, 13, 15, 24]. A quadratic has constant second differences. The observed second differences are [7, -8, 7], so the middle value is suspect. If the expected constant is 2, solving the middle second-difference equation gives the corrected ordinate 8.

$$
\Delta^2y_0=y_2-2y_1+y_0,\qquad
\Delta^2y_1=y_3-2y_2+y_1
$$

Replacing only the suspect entry gives second differences [2, 2, 2]. This is a plausible correction under the stated quadratic assumption, not a conclusion available from data alone. Without a degree or smoothness model, any finite list can be interpolated exactly by a sufficiently high-degree polynomial. State the assumption that makes a correction identifiable.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.19 Lagrange construction from three nodes

Worked example 19 — Lagrange construction from three nodes. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The data are (0,1), (1,2), and (2,1). Each node gets a cardinal polynomial. The denominators come from the corresponding node differences; checking the values at 0, 1, and 2 ensures the basis has the required one-at-its-own-node, zero-at-the-other-nodes behavior.

$$
L_0(x)=\frac{(x-1)(x-2)}2,\quad L_1(x)=-x(x-2),\quad L_2(x)=\frac{x(x-1)}2
$$

The interpolant is P(x)=1L_0(x)+2L_1(x)+1L_2(x). Simplification gives P(x)=(-1)x^2+(2)x+(1); at x=1/2 it is 7/4. Re-substitution recovers all three ordinates. This example shows how the basis formula performs the construction rather than merely checking a polynomial guessed in advance.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.20 Newton forward formula on equal spacing

Worked example 20 — Newton forward formula on equal spacing. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

Here the nodes are 4, 6, 8, and 10, so h=2 and the forward parameter at x=7 is u=(7-4)/2=3/2. The table’s first differences are [2, 2, 2]; the second differences are [0, 0]; and the third difference is 0. These entries follow from subtracting adjacent values, not from dividing by h.

$$
P(x)=6+u(2)+\frac{u(u-1)}2(0)+\frac{u(u-1)(u-2)}6(0)
$$

Substituting u=3/2 gives P(7)=9. Because the data were generated from a quadratic, the third difference vanishes and the formula reduces to the quadratic terms. The four node substitutions reproduce the table. The calculation illustrates why equal spacing must be verified before reading a forward-difference column as Newton coefficients.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.21 Newton backward formula near the last node

Worked example 21 — Newton backward formula near the last node. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The table is equally spaced with h=1, and the target x=5/2 lies half a step before the last node x_3=3. Thus v=(x-x_3)/h=-1/2. The terminal value is y_3=-6; the last backward first difference is -2, and the last backward second difference is 0. Since the data are quadratic, higher differences vanish.

$$
P(x)=y_3+v\nabla y_3+\frac{v(v+1)}2\nabla^2 y_3
= -6+v(-2)+\frac{v(v+1)}2(0)
$$

Evaluation gives P(5/2)=-5. This is the same unique polynomial that a forward formula would produce, but the terminal anchor keeps the relevant differences at the end of the table. Replacing v by (x-x_0)/h would mix two different conventions.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.22 Divided differences for unequal nodes

Worked example 22 — Divided differences for unequal nodes. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The data use nodes 0, 1, 2, and 4; the last gap is two, so a constant-step forward table is not applicable. The first divided differences are [-3.0, -9.0, -18.0], the second are [-3.0, -3.0], and the third is 0.0. Each denominator spans the outer nodes of the divided-difference entry.

$$
P(x)=-1+(-3.0)(x-0)+(-3.0)(x-0)(x-1)+(0.0)(x-0)(x-1)(x-2)
$$

At x=3 the value is -28. Substituting x=0,1,2,4 returns the four data values. Divided differences retain the actual unequal spacings and produce a Newton polynomial whose leading diagonal entries are its coefficients.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.23 Maclaurin approximation to sine

Worked example 23 — Maclaurin approximation to sine. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

A Taylor polynomial is fitted to derivative information at its center, not to a list of function values. At zero, the successive derivatives of the selected function have values 0, 1, 0, and -1. Dividing each derivative value by its factorial gives the cubic coefficients; a zero derivative removes the corresponding power.

$$
P_3(x)=x-x^3/6,\qquad P_3(0.1)\approx 0.09983333
$$

For comparison, the function value is 0.09983342, so the absolute discrepancy is 8.33e-08. The source’s sine calculation gives x-x^3/6 and approximately 0.0998333 at 0.1. Agreement near the center is expected; it does not imply the same accuracy far away, since the omitted terms grow with distance.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.24 Using constant second differences to audit a misprint

Worked example 24 — Using constant second differences to audit a misprint. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

Suppose equally spaced integer abscissae 0 through 4 are expected to follow a quadratic trend, but the listed ordinates are [0, 3, 13, 15, 24]. A quadratic has constant second differences. The observed second differences are [7, -8, 7], so the middle value is suspect. If the expected constant is 2, solving the middle second-difference equation gives the corrected ordinate 8.

$$
\Delta^2y_0=y_2-2y_1+y_0,\qquad
\Delta^2y_1=y_3-2y_2+y_1
$$

Replacing only the suspect entry gives second differences [2, 2, 2]. This is a plausible correction under the stated quadratic assumption, not a conclusion available from data alone. Without a degree or smoothness model, any finite list can be interpolated exactly by a sufficiently high-degree polynomial. State the assumption that makes a correction identifiable.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.25 Lagrange construction from three nodes

Worked example 25 — Lagrange construction from three nodes. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The data are (0,2), (1,2), and (2,4). Each node gets a cardinal polynomial. The denominators come from the corresponding node differences; checking the values at 0, 1, and 2 ensures the basis has the required one-at-its-own-node, zero-at-the-other-nodes behavior.

$$
L_0(x)=\frac{(x-1)(x-2)}2,\quad L_1(x)=-x(x-2),\quad L_2(x)=\frac{x(x-1)}2
$$

The interpolant is P(x)=2L_0(x)+2L_1(x)+4L_2(x). Simplification gives P(x)=(1)x^2+(-1)x+(2); at x=1/2 it is 7/4. Re-substitution recovers all three ordinates. This example shows how the basis formula performs the construction rather than merely checking a polynomial guessed in advance.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.26 Newton forward formula on equal spacing

Worked example 26 — Newton forward formula on equal spacing. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

Here the nodes are 4, 6, 8, and 10, so h=2 and the forward parameter at x=7 is u=(7-4)/2=3/2. The table’s first differences are [36, 52, 68]; the second differences are [16, 16]; and the third difference is 0. These entries follow from subtracting adjacent values, not from dividing by h.

$$
P(x)=24+u(36)+\frac{u(u-1)}2(16)+\frac{u(u-1)(u-2)}6(0)
$$

Substituting u=3/2 gives P(7)=84. Because the data were generated from a quadratic, the third difference vanishes and the formula reduces to the quadratic terms. The four node substitutions reproduce the table. The calculation illustrates why equal spacing must be verified before reading a forward-difference column as Newton coefficients.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.27 Newton backward formula near the last node

Worked example 27 — Newton backward formula near the last node. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The table is equally spaced with h=1, and the target x=5/2 lies half a step before the last node x_3=3. Thus v=(x-x_3)/h=-1/2. The terminal value is y_3=5; the last backward first difference is 1, and the last backward second difference is 0. Since the data are quadratic, higher differences vanish.

$$
P(x)=y_3+v\nabla y_3+\frac{v(v+1)}2\nabla^2 y_3
= 5+v(1)+\frac{v(v+1)}2(0)
$$

Evaluation gives P(5/2)=9/2. This is the same unique polynomial that a forward formula would produce, but the terminal anchor keeps the relevant differences at the end of the table. Replacing v by (x-x_0)/h would mix two different conventions.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.28 Divided differences for unequal nodes

Worked example 28 — Divided differences for unequal nodes. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The data use nodes 0, 1, 2, and 4; the last gap is two, so a constant-step forward table is not applicable. The first divided differences are [5.0, 19.0, 64.0], the second are [7.0, 15.0], and the third is 2.0. Each denominator spans the outer nodes of the divided-difference entry.

$$
P(x)=-1+(5.0)(x-0)+(7.0)(x-0)(x-1)+(2.0)(x-0)(x-1)(x-2)
$$

At x=3 the value is 68. Substituting x=0,1,2,4 returns the four data values. Divided differences retain the actual unequal spacings and produce a Newton polynomial whose leading diagonal entries are its coefficients.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.29 Maclaurin approximation to cosine

Worked example 29 — Maclaurin approximation to cosine. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

A Taylor polynomial is fitted to derivative information at its center, not to a list of function values. At zero, the successive derivatives of the selected function have values 1, 0, -1, and 0. Dividing each derivative value by its factorial gives the cubic coefficients; a zero derivative removes the corresponding power.

$$
P_3(x)=1-x^2/2,\qquad P_3(0.2)\approx 0.98000000
$$

For comparison, the function value is 0.98006658, so the absolute discrepancy is 6.66e-05. The source’s sine calculation gives x-x^3/6 and approximately 0.0998333 at 0.1. Agreement near the center is expected; it does not imply the same accuracy far away, since the omitted terms grow with distance.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.30 Using constant second differences to audit a misprint

Worked example 30 — Using constant second differences to audit a misprint. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

Suppose equally spaced integer abscissae 0 through 4 are expected to follow a quadratic trend, but the listed ordinates are [0, 3, 13, 15, 24]. A quadratic has constant second differences. The observed second differences are [7, -8, 7], so the middle value is suspect. If the expected constant is 2, solving the middle second-difference equation gives the corrected ordinate 8.

$$
\Delta^2y_0=y_2-2y_1+y_0,\qquad
\Delta^2y_1=y_3-2y_2+y_1
$$

Replacing only the suspect entry gives second differences [2, 2, 2]. This is a plausible correction under the stated quadratic assumption, not a conclusion available from data alone. Without a degree or smoothness model, any finite list can be interpolated exactly by a sufficiently high-degree polynomial. State the assumption that makes a correction identifiable.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.31 Lagrange construction from three nodes

Worked example 31 — Lagrange construction from three nodes. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The data are (0,-2), (1,-1), and (2,-4). Each node gets a cardinal polynomial. The denominators come from the corresponding node differences; checking the values at 0, 1, and 2 ensures the basis has the required one-at-its-own-node, zero-at-the-other-nodes behavior.

$$
L_0(x)=\frac{(x-1)(x-2)}2,\quad L_1(x)=-x(x-2),\quad L_2(x)=\frac{x(x-1)}2
$$

The interpolant is P(x)=-2L_0(x)+-1L_1(x)+-4L_2(x). Simplification gives P(x)=(-2)x^2+(3)x+(-2); at x=1/2 it is -1. Re-substitution recovers all three ordinates. This example shows how the basis formula performs the construction rather than merely checking a polynomial guessed in advance.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.32 Newton forward formula on equal spacing

Worked example 32 — Newton forward formula on equal spacing. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

Here the nodes are 4, 6, 8, and 10, so h=2 and the forward parameter at x=7 is u=(7-4)/2=3/2. The table’s first differences are [0, 0, 0]; the second differences are [0, 0]; and the third difference is 0. These entries follow from subtracting adjacent values, not from dividing by h.

$$
P(x)=2+u(0)+\frac{u(u-1)}2(0)+\frac{u(u-1)(u-2)}6(0)
$$

Substituting u=3/2 gives P(7)=2. Because the data were generated from a quadratic, the third difference vanishes and the formula reduces to the quadratic terms. The four node substitutions reproduce the table. The calculation illustrates why equal spacing must be verified before reading a forward-difference column as Newton coefficients.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.33 Newton backward formula near the last node

Worked example 33 — Newton backward formula near the last node. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The table is equally spaced with h=1, and the target x=5/2 lies half a step before the last node x_3=3. Thus v=(x-x_3)/h=-1/2. The terminal value is y_3=-3; the last backward first difference is -1, and the last backward second difference is 0. Since the data are quadratic, higher differences vanish.

$$
P(x)=y_3+v\nabla y_3+\frac{v(v+1)}2\nabla^2 y_3
= -3+v(-1)+\frac{v(v+1)}2(0)
$$

Evaluation gives P(5/2)=-5/2. This is the same unique polynomial that a forward formula would produce, but the terminal anchor keeps the relevant differences at the end of the table. Replacing v by (x-x_0)/h would mix two different conventions.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

### 4.34 Divided differences for unequal nodes

Worked example 34 — Divided differences for unequal nodes. This calculation makes the method choice explicit before arithmetic begins. Record the spacing, anchoring node, and required degree; those choices determine which differences can be used and how to interpret the resulting polynomial.

The data use nodes 0, 1, 2, and 4; the last gap is two, so a constant-step forward table is not applicable. The first divided differences are [-3.0, -7.0, -13.0], the second are [-2.0, -2.0], and the third is 0.0. Each denominator spans the outer nodes of the divided-difference entry.

$$
P(x)=-1+(-3.0)(x-0)+(-2.0)(x-0)(x-1)+(0.0)(x-0)(x-1)(x-2)
$$

At x=3 the value is -22. Substituting x=0,1,2,4 returns the four data values. Divided differences retain the actual unequal spacings and produce a Newton polynomial whose leading diagonal entries are its coefficients.

The result should be read with its assumptions attached: exact node agreement is guaranteed, but off-node accuracy depends on the function, interval, and data precision.

## 5. Mathematical Extensions, Limits, and Common Errors — Method selection, verification, and source limits

The source lesson sequence maps precisely as follows: Lesson 4 develops collocation and Lagrange interpolation and illustrates Taylor approximation; Lesson 5 defines forward, central, and backward differences, constructs tables, and discusses detection of data errors; Lesson 6 presents Newton forward/backward formulas for equal spacing and divided differences for unequal spacing. “Central difference” in Lesson 5 is a difference-table concept; it should not be confused with an unsupported derivative formula.

The extracted Lagrange sample has OCR damage in its node row and formula. Its general theorem and basis construction are intact, but malformed fractions and missing abscissae cannot be reconstructed confidently from the extraction. This note uses intact source datasets elsewhere in Lessons 4–6 and does not invent a corrected version of that damaged sample. The four-point dataset (4,1),(6,3),(8,8),(10,20) is readable and its forward-difference table yields first differences 2,5,12, second differences 3,7, and third difference 4.

Misprints in difference tables should be located by checking the whole pattern and the original functional relationship. A table alone may admit multiple corrections. State the assumed degree or smoothness before declaring a unique repair.