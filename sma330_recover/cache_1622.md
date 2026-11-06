## 1. Foundational Concepts, Definitions, and Axioms — Polynomial language and the division problem

The coefficient recurrence underlying synthetic division provides a compact derivation and a useful stability perspective. For P(x)=a_n x^n+...+a_0 and divisor x-r, define b_n=a_n and then b_k=a_k+r b_{k+1} while descending through the remaining coefficients. The final b_0 is P(r); the preceding b-values are coefficients of the quotient. This recurrence is Horner evaluation and synthetic division at once. The result is exact over exact arithmetic and is verified by P(x)=(x-r)Q(x)+P(r).

The source lesson asks for the procedure and polynomial notes rather than a broad numerical root-finding course. The advanced treatment here consequently concentrates on proving the identity, interpreting roots and multiplicity correctly, understanding nested form, auditing the extracted worked examples, and analyzing where arithmetic or transcription errors enter. Root existence via a sign change is stated with its continuity hypothesis, and the method’s limitations are separated from its exact algebraic conclusions.

The difference between evaluating a polynomial and dividing it should remain explicit. Evaluation asks only for the last recurrence value. Division reads all earlier recurrence values as a quotient. If the remainder is zero, the division identity certifies a factor; if it is nonzero, the same identity still holds and reports precisely how far the proposed factorization is from an exact one.

## 2. Theorems, Lemmas, and Analytical Properties — Division, remainder, factors, and roots

The recurrence can be derived directly without invoking a tableau. Seek Q(x)=b_nx^(n-1)+...+b_1. In (x-r)Q+R, the coefficient of x^n is b_n; the coefficient of x^k for 1<=k<n is b_k-rb_(k+1); and the constant is R-rb_1. Equating with a_n,...,a_0 gives b_n=a_n, b_k=a_k+r b_(k+1), and R=a_0+r b_1. This is exactly synthetic division. Its final recurrence value is P(r), as also follows by substitution in the identity.

Uniqueness is immediate from the division algorithm or from coefficient comparison. The remainder theorem is thus not an independent computational coincidence: it is forced by the division identity. The factor theorem is its zero-remainder case. If a candidate r is not a root, the identity remains useful because it quantifies the residual R and supplies the quotient for a nearby-factor analysis.

The source’s endpoint-sign argument relies on the intermediate value theorem: a polynomial is continuous on every closed interval, so opposite signs at endpoints force a zero inside. The converse is false. For an even-multiplicity root, a polynomial may meet the horizontal axis and return to the same side. Likewise, a single sign change ensures existence, not uniqueness, unless additional information about monotonicity or the degree is supplied. These limits prevent a correct computation from being overinterpreted.

Horner evaluation groups operations to avoid separately forming high powers. The arithmetic count is linear in degree: one multiply and one add per coefficient after the leading coefficient. This is a reduced operation count, not a proof of zero round-off. If coefficient data are approximate, the computed value inherits their uncertainty; if intermediate operations are rounded, a small computed residual is not necessarily proof of an exact mathematical root.

## 3. Formal Proofs, Derivations, and Methods — From long division to the synthetic recurrence

The synthetic row is a compressed long division. Long division chooses the leading quotient coefficient to cancel the highest remaining term. Since the divisor is monic x-r, that coefficient is the current leading coefficient; multiplying by -r shifts the correction to the next power. Recording only the resulting coefficients yields b_k=a_k+r b_(k+1). The tableau therefore retains all information needed for quotient and remainder while suppressing powers and repeated subtraction.

For nested evaluation, the recurrence starts at the leading coefficient and ends at P(x). At each stage the partial polynomial is evaluated at x before one lower coefficient is added. This gives an inductive proof: after processing a_n through a_k, the running value equals a_nx^(n-k)+a_(n-1)x^(n-k-1)+...+a_k. The final stage is P(x).

Checks should be independent: (1) compare the remainder to direct P(r); (2) expand (x-r)Q+R and compare coefficients; (3) if a root is claimed from an interval, recompute endpoint signs. The first check tests the final scalar, the second tests every quotient coefficient, and the third tests the logic of existence. A disagreement should trigger an audit of sign convention, omitted powers, coefficient order, or arithmetic rather than an arbitrary adjustment to the answer.

## 4. Representative Worked Examples and Solutions — Checked synthetic-division and nested-form examples

### 4.1 Remainder Evaluation

Worked example 1 — remainder evaluation. The dividend is P(x)=2x^5 - 6x^4 - x^3 + 4x^2 - 4x + 1, and the proposed divisor is x-(-1). The coefficient row, including any zeros, is 2, -6, -1, 4, -4, 1. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
-1 & 2 & -6 & -1 & 4 & -4 & 1 \\
 & -2 & 8 & -7 & 3 & 1 \\
 & 2 & -8 & 7 & -3 & -1 & 2
\end{array}
$$

Bring down 2. The successive products are -2, 8, -7, 3, 1, and adding them to the next coefficients gives the bottom row 2, -8, 7, -3, -1, 2. Therefore Q(x)=2x^4 - 8x^3 + 7x^2 - 3x - 1 and R=2; the remainder theorem identifies P(-1)=2. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -1 gives 2. The complete identity is P(x)=(x-(-1))(2x^4 - 8x^3 + 7x^2 - 3x - 1)+(2). When the result is used to test a root, the conclusion is conditional: -1 is a root only if this remainder is zero. Here the calculation reports 2, so the tableau does not certify a root unless that value is zero.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.2 Quotient Reconstruction

Worked example 2 — quotient reconstruction. Consider P(x)=-4x^3 + 6x - 2 and test r=0. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
0 & -4 & 0 & 6 & -2 \\
 & 0 & 0 & 0 \\
 & -4 & 0 & 6 & -2
\end{array}
$$

The multiply-and-add recurrence begins with -4. At each subsequent column it multiplies by 0, then adds the original coefficient. The product row is 0, 0, 0; the resulting row is -4, 0, 6, -2. Reading it by powers gives Q(x)=-4x^2 + 6, while the final scalar is R=-2. Hence P(x)=(x-(0))Q(x)+R.

Set x=0 in the identity: the factor term vanishes and the equation reduces to P(0)=-2. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(0). If the original divisor were described as x+0, its corresponding trial number would be negative.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.3 A Missing-Power Alignment Check

Worked example 3 — a missing-power alignment check. A candidate computation uses P(x)=3x^4 - 5x^3 - 3 at r=1. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
1 & 3 & -5 & 0 & 0 & -3 \\
 & 3 & -2 & -2 & -2 \\
 & 3 & -2 & -2 & -2 & -5
\end{array}
$$

Carry 3 down; use the current carry times 1 to form the products 3, -2, -2, -2; add columnwise to obtain 3, -2, -2, -2, -5. The quotient is Q(x)=3x^3 - 2x^2 - 2x - 2 and the remainder is R=-5. Therefore the algebraic certificate is P(x)=(x-(1))(3x^3 - 2x^2 - 2x - 2)+(-5), and P(1)=-5 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(1) directly. A zero remainder establishes the factor x-(1); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.4 Factor Certification

Worked example 4 — factor certification. The dividend is P(x)=-3x^5 + 2x^4 - 6x^3 - x^2 + 4x - 4, and the proposed divisor is x-(2). The coefficient row, including any zeros, is -3, 2, -6, -1, 4, -4. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
2 & -3 & 2 & -6 & -1 & 4 & -4 \\
 & -6 & -8 & -28 & -58 & -108 \\
 & -3 & -4 & -14 & -29 & -54 & -112
\end{array}
$$

Bring down -3. The successive products are -6, -8, -28, -58, -108, and adding them to the next coefficients gives the bottom row -3, -4, -14, -29, -54, -112. Therefore Q(x)=-3x^4 - 4x^3 - 14x^2 - 29x - 54 and R=-112; the remainder theorem identifies P(2)=-112. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 2 gives -112. The complete identity is P(x)=(x-(2))(-3x^4 - 4x^3 - 14x^2 - 29x - 54)+(-112). When the result is used to test a root, the conclusion is conditional: 2 is a root only if this remainder is zero. Here the calculation reports -112, so the tableau does not certify a root unless that value is zero.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.5 Nested Numerical Evaluation

Worked example 5 — nested numerical evaluation. Consider P(x)=4x^3 - 4x^2 + x + 6 and test r=3. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
3 & 4 & -4 & 1 & 6 \\
 & 12 & 24 & 75 \\
 & 4 & 8 & 25 & 81
\end{array}
$$

The multiply-and-add recurrence begins with 4. At each subsequent column it multiplies by 3, then adds the original coefficient. The product row is 12, 24, 75; the resulting row is 4, 8, 25, 81. Reading it by powers gives Q(x)=4x^2 + 8x + 25, while the final scalar is R=81. Hence P(x)=(x-(3))Q(x)+R.

Set x=3 in the identity: the factor term vanishes and the equation reduces to P(3)=81. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(3). If the original divisor were described as x+3, its corresponding trial number would be negative.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.6 Sign-Convention Practice

Worked example 6 — sign-convention practice. A candidate computation uses P(x)=-2x^4 - 5x^2 + 5 at r=-3. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
-3 & -2 & 0 & -5 & 0 & 5 \\
 & 6 & -18 & 69 & -207 \\
 & -2 & 6 & -23 & 69 & -202
\end{array}
$$

Carry -2 down; use the current carry times -3 to form the products 6, -18, 69, -207; add columnwise to obtain -2, 6, -23, 69, -202. The quotient is Q(x)=-2x^3 + 6x^2 - 23x + 69 and the remainder is R=-202. Therefore the algebraic certificate is P(x)=(x-(-3))(-2x^3 + 6x^2 - 23x + 69)+(-202), and P(-3)=-202 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(-3) directly. A zero remainder establishes the factor x-(-3); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.7 A Root Candidate That Is Not A Root

Worked example 7 — a root candidate that is not a root. The dividend is P(x)=5x^5 - 3x^4 + 2x^3 - 6x^2 - x + 4, and the proposed divisor is x-(-2). The coefficient row, including any zeros, is 5, -3, 2, -6, -1, 4. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
-2 & 5 & -3 & 2 & -6 & -1 & 4 \\
 & -10 & 26 & -56 & 124 & -246 \\
 & 5 & -13 & 28 & -62 & 123 & -242
\end{array}
$$

Bring down 5. The successive products are -10, 26, -56, 124, -246, and adding them to the next coefficients gives the bottom row 5, -13, 28, -62, 123, -242. Therefore Q(x)=5x^4 - 13x^3 + 28x^2 - 62x + 123 and R=-242; the remainder theorem identifies P(-2)=-242. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -2 gives -242. The complete identity is P(x)=(x-(-2))(5x^4 - 13x^3 + 28x^2 - 62x + 123)+(-242). When the result is used to test a root, the conclusion is conditional: -2 is a root only if this remainder is zero. Here the calculation reports -242, so the tableau does not certify a root unless that value is zero.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.8 A Sparse Polynomial

Worked example 8 — a sparse polynomial. Consider P(x)=-x^3 + 4x^2 + 1 and test r=-1. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
-1 & -1 & 4 & 0 & 1 \\
 & 1 & -5 & 5 \\
 & -1 & 5 & -5 & 6
\end{array}
$$

The multiply-and-add recurrence begins with -1. At each subsequent column it multiplies by -1, then adds the original coefficient. The product row is 1, -5, 5; the resulting row is -1, 5, -5, 6. Reading it by powers gives Q(x)=-x^2 + 5x - 5, while the final scalar is R=6. Hence P(x)=(x-(-1))Q(x)+R.

Set x=-1 in the identity: the factor term vanishes and the equation reduces to P(-1)=6. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(-1). If the original divisor were described as x+1, its corresponding trial number would be negative.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.9 Independent Substitution

Worked example 9 — independent substitution. A candidate computation uses P(x)=6x^4 - 2x^3 + 3x^2 - 5x at r=0. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
0 & 6 & -2 & 3 & -5 & 0 \\
 & 0 & 0 & 0 & 0 \\
 & 6 & -2 & 3 & -5 & 0
\end{array}
$$

Carry 6 down; use the current carry times 0 to form the products 0, 0, 0, 0; add columnwise to obtain 6, -2, 3, -5, 0. The quotient is Q(x)=6x^3 - 2x^2 + 3x - 5 and the remainder is R=0. Therefore the algebraic certificate is P(x)=(x-(0))(6x^3 - 2x^2 + 3x - 5)+(0), and P(0)=0 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(0) directly. A zero remainder establishes the factor x-(0); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.10 Coefficient-Order Auditing

Worked example 10 — coefficient-order auditing. The dividend is P(x)=x^5 - 3x^3 + 2x^2 - 6x - 1, and the proposed divisor is x-(1). The coefficient row, including any zeros, is 1, 0, -3, 2, -6, -1. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
1 & 1 & 0 & -3 & 2 & -6 & -1 \\
 & 1 & 1 & -2 & 0 & -6 \\
 & 1 & 1 & -2 & 0 & -6 & -7
\end{array}
$$

Bring down 1. The successive products are 1, 1, -2, 0, -6, and adding them to the next coefficients gives the bottom row 1, 1, -2, 0, -6, -7. Therefore Q(x)=x^4 + x^3 - 2x^2 - 6 and R=-7; the remainder theorem identifies P(1)=-7. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 1 gives -7. The complete identity is P(x)=(x-(1))(x^4 + x^3 - 2x^2 - 6)+(-7). When the result is used to test a root, the conclusion is conditional: 1 is a root only if this remainder is zero. Here the calculation reports -7, so the tableau does not certify a root unless that value is zero.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.11 A Decimal Input

Worked example 11 — a decimal input. Consider P(x)=-6x^3 - x^2 + 4x - 4 and test r=2. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
2 & -6 & -1 & 4 & -4 \\
 & -12 & -26 & -44 \\
 & -6 & -13 & -22 & -48
\end{array}
$$

The multiply-and-add recurrence begins with -6. At each subsequent column it multiplies by 2, then adds the original coefficient. The product row is -12, -26, -44; the resulting row is -6, -13, -22, -48. Reading it by powers gives Q(x)=-6x^2 - 13x - 22, while the final scalar is R=-48. Hence P(x)=(x-(2))Q(x)+R.

Set x=2 in the identity: the factor term vanishes and the equation reduces to P(2)=-48. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(2). If the original divisor were described as x+2, its corresponding trial number would be negative.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.12 Degree Reduction

Worked example 12 — degree reduction. A candidate computation uses P(x)=x^4 + 6x^3 - 2x^2 + 3x - 5 at r=3. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
3 & 1 & 6 & -2 & 3 & -5 \\
 & 3 & 27 & 75 & 234 \\
 & 1 & 9 & 25 & 78 & 229
\end{array}
$$

Carry 1 down; use the current carry times 3 to form the products 3, 27, 75, 234; add columnwise to obtain 1, 9, 25, 78, 229. The quotient is Q(x)=x^3 + 9x^2 + 25x + 78 and the remainder is R=229. Therefore the algebraic certificate is P(x)=(x-(3))(x^3 + 9x^2 + 25x + 78)+(229), and P(3)=229 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(3) directly. A zero remainder establishes the factor x-(3); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.13 Remainder Evaluation

Worked example 13 — remainder evaluation. The dividend is P(x)=-5x^5 + 5x^3 - 3x^2 - 6, and the proposed divisor is x-(-3). The coefficient row, including any zeros, is -5, 0, 5, -3, 0, -6. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
-3 & -5 & 0 & 5 & -3 & 0 & -6 \\
 & 15 & -45 & 120 & -351 & 1053 \\
 & -5 & 15 & -40 & 117 & -351 & 1047
\end{array}
$$

Bring down -5. The successive products are 15, -45, 120, -351, 1053, and adding them to the next coefficients gives the bottom row -5, 15, -40, 117, -351, 1047. Therefore Q(x)=-5x^4 + 15x^3 - 40x^2 + 117x - 351 and R=1047; the remainder theorem identifies P(-3)=1047. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -3 gives 1047. The complete identity is P(x)=(x-(-3))(-5x^4 + 15x^3 - 40x^2 + 117x - 351)+(1047). When the result is used to test a root, the conclusion is conditional: -3 is a root only if this remainder is zero. Here the calculation reports 1047, so the tableau does not certify a root unless that value is zero.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.14 Quotient Reconstruction

Worked example 14 — quotient reconstruction. Consider P(x)=2x^3 - x + 4 and test r=-2. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
-2 & 2 & 0 & -1 & 4 \\
 & -4 & 8 & -14 \\
 & 2 & -4 & 7 & -10
\end{array}
$$

The multiply-and-add recurrence begins with 2. At each subsequent column it multiplies by -2, then adds the original coefficient. The product row is -4, 8, -14; the resulting row is 2, -4, 7, -10. Reading it by powers gives Q(x)=2x^2 - 4x + 7, while the final scalar is R=-10. Hence P(x)=(x-(-2))Q(x)+R.

Set x=-2 in the identity: the factor term vanishes and the equation reduces to P(-2)=-10. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(-2). If the original divisor were described as x+2, its corresponding trial number would be negative.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.15 A Missing-Power Alignment Check

Worked example 15 — a missing-power alignment check. A candidate computation uses P(x)=-4x^4 + x^3 + 6x^2 - 2x + 3 at r=-1. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
-1 & -4 & 1 & 6 & -2 & 3 \\
 & 4 & -5 & -1 & 3 \\
 & -4 & 5 & 1 & -3 & 6
\end{array}
$$

Carry -4 down; use the current carry times -1 to form the products 4, -5, -1, 3; add columnwise to obtain -4, 5, 1, -3, 6. The quotient is Q(x)=-4x^3 + 5x^2 + x - 3 and the remainder is R=6. Therefore the algebraic certificate is P(x)=(x-(-1))(-4x^3 + 5x^2 + x - 3)+(6), and P(-1)=6 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(-1) directly. A zero remainder establishes the factor x-(-1); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.16 Factor Certification

Worked example 16 — factor certification. The dividend is P(x)=3x^5 - 5x^4 + 5x^2 - 3x + 2, and the proposed divisor is x-(0). The coefficient row, including any zeros, is 3, -5, 0, 5, -3, 2. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
0 & 3 & -5 & 0 & 5 & -3 & 2 \\
 & 0 & 0 & 0 & 0 & 0 \\
 & 3 & -5 & 0 & 5 & -3 & 2
\end{array}
$$

Bring down 3. The successive products are 0, 0, 0, 0, 0, and adding them to the next coefficients gives the bottom row 3, -5, 0, 5, -3, 2. Therefore Q(x)=3x^4 - 5x^3 + 5x - 3 and R=2; the remainder theorem identifies P(0)=2. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 0 gives 2. The complete identity is P(x)=(x-(0))(3x^4 - 5x^3 + 5x - 3)+(2). When the result is used to test a root, the conclusion is conditional: 0 is a root only if this remainder is zero. Here the calculation reports 2, so the tableau does not certify a root unless that value is zero.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.17 Nested Numerical Evaluation

Worked example 17 — nested numerical evaluation. Consider P(x)=-3x^3 + 2x^2 - 6x - 1 and test r=1. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
1 & -3 & 2 & -6 & -1 \\
 & -3 & -1 & -7 \\
 & -3 & -1 & -7 & -8
\end{array}
$$

The multiply-and-add recurrence begins with -3. At each subsequent column it multiplies by 1, then adds the original coefficient. The product row is -3, -1, -7; the resulting row is -3, -1, -7, -8. Reading it by powers gives Q(x)=-3x^2 - x - 7, while the final scalar is R=-8. Hence P(x)=(x-(1))Q(x)+R.

Set x=1 in the identity: the factor term vanishes and the equation reduces to P(1)=-8. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(1). If the original divisor were described as x+1, its corresponding trial number would be negative.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.18 Sign-Convention Practice

Worked example 18 — sign-convention practice. A candidate computation uses P(x)=4x^4 + x^2 - 2 at r=2. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
2 & 4 & 0 & 1 & 0 & -2 \\
 & 8 & 16 & 34 & 68 \\
 & 4 & 8 & 17 & 34 & 66
\end{array}
$$

Carry 4 down; use the current carry times 2 to form the products 8, 16, 34, 68; add columnwise to obtain 4, 8, 17, 34, 66. The quotient is Q(x)=4x^3 + 8x^2 + 17x + 34 and the remainder is R=66. Therefore the algebraic certificate is P(x)=(x-(2))(4x^3 + 8x^2 + 17x + 34)+(66), and P(2)=66 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(2) directly. A zero remainder establishes the factor x-(2); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.19 A Root Candidate That Is Not A Root

Worked example 19 — a root candidate that is not a root. The dividend is P(x)=-2x^5 + 3x^4 - 5x^3 + 5x - 3, and the proposed divisor is x-(3). The coefficient row, including any zeros, is -2, 3, -5, 0, 5, -3. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
3 & -2 & 3 & -5 & 0 & 5 & -3 \\
 & -6 & -9 & -42 & -126 & -363 \\
 & -2 & -3 & -14 & -42 & -121 & -366
\end{array}
$$

Bring down -2. The successive products are -6, -9, -42, -126, -363, and adding them to the next coefficients gives the bottom row -2, -3, -14, -42, -121, -366. Therefore Q(x)=-2x^4 - 3x^3 - 14x^2 - 42x - 121 and R=-366; the remainder theorem identifies P(3)=-366. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 3 gives -366. The complete identity is P(x)=(x-(3))(-2x^4 - 3x^3 - 14x^2 - 42x - 121)+(-366). When the result is used to test a root, the conclusion is conditional: 3 is a root only if this remainder is zero. Here the calculation reports -366, so the tableau does not certify a root unless that value is zero.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.20 A Sparse Polynomial

Worked example 20 — a sparse polynomial. Consider P(x)=5x^3 - 3x^2 + 2x - 6 and test r=-3. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
-3 & 5 & -3 & 2 & -6 \\
 & -15 & 54 & -168 \\
 & 5 & -18 & 56 & -174
\end{array}
$$

The multiply-and-add recurrence begins with 5. At each subsequent column it multiplies by -3, then adds the original coefficient. The product row is -15, 54, -168; the resulting row is 5, -18, 56, -174. Reading it by powers gives Q(x)=5x^2 - 18x + 56, while the final scalar is R=-174. Hence P(x)=(x-(-3))Q(x)+R.

Set x=-3 in the identity: the factor term vanishes and the equation reduces to P(-3)=-174. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(-3). If the original divisor were described as x+3, its corresponding trial number would be negative.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.21 Independent Substitution

Worked example 21 — independent substitution. A candidate computation uses P(x)=-x^4 + 4x^3 - 4x^2 + x + 6 at r=-2. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
-2 & -1 & 4 & -4 & 1 & 6 \\
 & 2 & -12 & 32 & -66 \\
 & -1 & 6 & -16 & 33 & -60
\end{array}
$$

Carry -1 down; use the current carry times -2 to form the products 2, -12, 32, -66; add columnwise to obtain -1, 6, -16, 33, -60. The quotient is Q(x)=-x^3 + 6x^2 - 16x + 33 and the remainder is R=-60. Therefore the algebraic certificate is P(x)=(x-(-2))(-x^3 + 6x^2 - 16x + 33)+(-60), and P(-2)=-60 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(-2) directly. A zero remainder establishes the factor x-(-2); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.22 Coefficient-Order Auditing

Worked example 22 — coefficient-order auditing. The dividend is P(x)=6x^5 + 3x^3 - 5x^2 + 5, and the proposed divisor is x-(-1). The coefficient row, including any zeros, is 6, 0, 3, -5, 0, 5. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
-1 & 6 & 0 & 3 & -5 & 0 & 5 \\
 & -6 & 6 & -9 & 14 & -14 \\
 & 6 & -6 & 9 & -14 & 14 & -9
\end{array}
$$

Bring down 6. The successive products are -6, 6, -9, 14, -14, and adding them to the next coefficients gives the bottom row 6, -6, 9, -14, 14, -9. Therefore Q(x)=6x^4 - 6x^3 + 9x^2 - 14x + 14 and R=-9; the remainder theorem identifies P(-1)=-9. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -1 gives -9. The complete identity is P(x)=(x-(-1))(6x^4 - 6x^3 + 9x^2 - 14x + 14)+(-9). When the result is used to test a root, the conclusion is conditional: -1 is a root only if this remainder is zero. Here the calculation reports -9, so the tableau does not certify a root unless that value is zero.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.23 A Decimal Input

Worked example 23 — a decimal input. Consider P(x)=x^3 + 5x^2 + 2 and test r=0. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
0 & 1 & 5 & 0 & 2 \\
 & 0 & 0 & 0 \\
 & 1 & 5 & 0 & 2
\end{array}
$$

The multiply-and-add recurrence begins with 1. At each subsequent column it multiplies by 0, then adds the original coefficient. The product row is 0, 0, 0; the resulting row is 1, 5, 0, 2. Reading it by powers gives Q(x)=x^2 + 5x, while the final scalar is R=2. Hence P(x)=(x-(0))Q(x)+R.

Set x=0 in the identity: the factor term vanishes and the equation reduces to P(0)=2. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(0). If the original divisor were described as x+0, its corresponding trial number would be negative.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.24 Degree Reduction

Worked example 24 — degree reduction. A candidate computation uses P(x)=-6x^4 - x^3 + 4x^2 - 4x + 1 at r=1. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
1 & -6 & -1 & 4 & -4 & 1 \\
 & -6 & -7 & -3 & -7 \\
 & -6 & -7 & -3 & -7 & -6
\end{array}
$$

Carry -6 down; use the current carry times 1 to form the products -6, -7, -3, -7; add columnwise to obtain -6, -7, -3, -7, -6. The quotient is Q(x)=-6x^3 - 7x^2 - 3x - 7 and the remainder is R=-6. Therefore the algebraic certificate is P(x)=(x-(1))(-6x^3 - 7x^2 - 3x - 7)+(-6), and P(1)=-6 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(1) directly. A zero remainder establishes the factor x-(1); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.25 Remainder Evaluation

Worked example 25 — remainder evaluation. The dividend is P(x)=x^5 + 6x^4 - 2x^3 + 3x^2 - 5x, and the proposed divisor is x-(2). The coefficient row, including any zeros, is 1, 6, -2, 3, -5, 0. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
2 & 1 & 6 & -2 & 3 & -5 & 0 \\
 & 2 & 16 & 28 & 62 & 114 \\
 & 1 & 8 & 14 & 31 & 57 & 114
\end{array}
$$

Bring down 1. The successive products are 2, 16, 28, 62, 114, and adding them to the next coefficients gives the bottom row 1, 8, 14, 31, 57, 114. Therefore Q(x)=x^4 + 8x^3 + 14x^2 + 31x + 57 and R=114; the remainder theorem identifies P(2)=114. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 2 gives 114. The complete identity is P(x)=(x-(2))(x^4 + 8x^3 + 14x^2 + 31x + 57)+(114). When the result is used to test a root, the conclusion is conditional: 2 is a root only if this remainder is zero. Here the calculation reports 114, so the tableau does not certify a root unless that value is zero.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.26 Quotient Reconstruction

Worked example 26 — quotient reconstruction. Consider P(x)=-5x^3 + 5x - 3 and test r=3. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
3 & -5 & 0 & 5 & -3 \\
 & -15 & -45 & -120 \\
 & -5 & -15 & -40 & -123
\end{array}
$$

The multiply-and-add recurrence begins with -5. At each subsequent column it multiplies by 3, then adds the original coefficient. The product row is -15, -45, -120; the resulting row is -5, -15, -40, -123. Reading it by powers gives Q(x)=-5x^2 - 15x - 40, while the final scalar is R=-123. Hence P(x)=(x-(3))Q(x)+R.

Set x=3 in the identity: the factor term vanishes and the equation reduces to P(3)=-123. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(3). If the original divisor were described as x+3, its corresponding trial number would be negative.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.27 A Missing-Power Alignment Check

Worked example 27 — a missing-power alignment check. A candidate computation uses P(x)=2x^4 - 6x^3 - x^2 + 4x - 4 at r=-3. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
-3 & 2 & -6 & -1 & 4 & -4 \\
 & -6 & 36 & -105 & 303 \\
 & 2 & -12 & 35 & -101 & 299
\end{array}
$$

Carry 2 down; use the current carry times -3 to form the products -6, 36, -105, 303; add columnwise to obtain 2, -12, 35, -101, 299. The quotient is Q(x)=2x^3 - 12x^2 + 35x - 101 and the remainder is R=299. Therefore the algebraic certificate is P(x)=(x-(-3))(2x^3 - 12x^2 + 35x - 101)+(299), and P(-3)=299 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(-3) directly. A zero remainder establishes the factor x-(-3); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.28 Factor Certification

Worked example 28 — factor certification. The dividend is P(x)=-4x^5 + x^4 + 6x^3 - 2x^2 - 5, and the proposed divisor is x-(-2). The coefficient row, including any zeros, is -4, 1, 6, -2, 0, -5. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
-2 & -4 & 1 & 6 & -2 & 0 & -5 \\
 & 8 & -18 & 24 & -44 & 88 \\
 & -4 & 9 & -12 & 22 & -44 & 83
\end{array}
$$

Bring down -4. The successive products are 8, -18, 24, -44, 88, and adding them to the next coefficients gives the bottom row -4, 9, -12, 22, -44, 83. Therefore Q(x)=-4x^4 + 9x^3 - 12x^2 + 22x - 44 and R=83; the remainder theorem identifies P(-2)=83. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -2 gives 83. The complete identity is P(x)=(x-(-2))(-4x^4 + 9x^3 - 12x^2 + 22x - 44)+(83). When the result is used to test a root, the conclusion is conditional: -2 is a root only if this remainder is zero. Here the calculation reports 83, so the tableau does not certify a root unless that value is zero.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.29 Nested Numerical Evaluation

Worked example 29 — nested numerical evaluation. Consider P(x)=3x^3 - 5x^2 + 5 and test r=-1. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
-1 & 3 & -5 & 0 & 5 \\
 & -3 & 8 & -8 \\
 & 3 & -8 & 8 & -3
\end{array}
$$

The multiply-and-add recurrence begins with 3. At each subsequent column it multiplies by -1, then adds the original coefficient. The product row is -3, 8, -8; the resulting row is 3, -8, 8, -3. Reading it by powers gives Q(x)=3x^2 - 8x + 8, while the final scalar is R=-3. Hence P(x)=(x-(-1))Q(x)+R.

Set x=-1 in the identity: the factor term vanishes and the equation reduces to P(-1)=-3. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(-1). If the original divisor were described as x+1, its corresponding trial number would be negative.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.30 Sign-Convention Practice

Worked example 30 — sign-convention practice. A candidate computation uses P(x)=-3x^4 - 6x^2 - x + 4 at r=0. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
0 & -3 & 0 & -6 & -1 & 4 \\
 & 0 & 0 & 0 & 0 \\
 & -3 & 0 & -6 & -1 & 4
\end{array}
$$

Carry -3 down; use the current carry times 0 to form the products 0, 0, 0, 0; add columnwise to obtain -3, 0, -6, -1, 4. The quotient is Q(x)=-3x^3 - 6x - 1 and the remainder is R=4. Therefore the algebraic certificate is P(x)=(x-(0))(-3x^3 - 6x - 1)+(4), and P(0)=4 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(0) directly. A zero remainder establishes the factor x-(0); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.31 A Root Candidate That Is Not A Root

Worked example 31 — a root candidate that is not a root. The dividend is P(x)=4x^5 - 4x^4 + x^3 + 6x^2 - 2x + 3, and the proposed divisor is x-(1). The coefficient row, including any zeros, is 4, -4, 1, 6, -2, 3. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
1 & 4 & -4 & 1 & 6 & -2 & 3 \\
 & 4 & 0 & 1 & 7 & 5 \\
 & 4 & 0 & 1 & 7 & 5 & 8
\end{array}
$$

Bring down 4. The successive products are 4, 0, 1, 7, 5, and adding them to the next coefficients gives the bottom row 4, 0, 1, 7, 5, 8. Therefore Q(x)=4x^4 + x^2 + 7x + 5 and R=8; the remainder theorem identifies P(1)=8. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 1 gives 8. The complete identity is P(x)=(x-(1))(4x^4 + x^2 + 7x + 5)+(8). When the result is used to test a root, the conclusion is conditional: 1 is a root only if this remainder is zero. Here the calculation reports 8, so the tableau does not certify a root unless that value is zero.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.32 A Sparse Polynomial

Worked example 32 — a sparse polynomial. Consider P(x)=-2x^3 + 3x^2 - 5x and test r=2. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
2 & -2 & 3 & -5 & 0 \\
 & -4 & -2 & -14 \\
 & -2 & -1 & -7 & -14
\end{array}
$$

The multiply-and-add recurrence begins with -2. At each subsequent column it multiplies by 2, then adds the original coefficient. The product row is -4, -2, -14; the resulting row is -2, -1, -7, -14. Reading it by powers gives Q(x)=-2x^2 - x - 7, while the final scalar is R=-14. Hence P(x)=(x-(2))Q(x)+R.

Set x=2 in the identity: the factor term vanishes and the equation reduces to P(2)=-14. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(2). If the original divisor were described as x+2, its corresponding trial number would be negative.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.33 Independent Substitution

Worked example 33 — independent substitution. A candidate computation uses P(x)=5x^4 - 3x^3 + 2x^2 - 1 at r=3. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
3 & 5 & -3 & 2 & 0 & -1 \\
 & 15 & 36 & 114 & 342 \\
 & 5 & 12 & 38 & 114 & 341
\end{array}
$$

Carry 5 down; use the current carry times 3 to form the products 15, 36, 114, 342; add columnwise to obtain 5, 12, 38, 114, 341. The quotient is Q(x)=5x^3 + 12x^2 + 38x + 114 and the remainder is R=341. Therefore the algebraic certificate is P(x)=(x-(3))(5x^3 + 12x^2 + 38x + 114)+(341), and P(3)=341 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(3) directly. A zero remainder establishes the factor x-(3); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

### 4.34 Coefficient-Order Auditing

Worked example 34 — coefficient-order auditing. The dividend is P(x)=-x^5 - 4x^3 + x^2 + 6x - 2, and the proposed divisor is x-(-3). The coefficient row, including any zeros, is -1, 0, -4, 1, 6, -2. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
-3 & -1 & 0 & -4 & 1 & 6 & -2 \\
 & 3 & -9 & 39 & -120 & 342 \\
 & -1 & 3 & -13 & 40 & -114 & 340
\end{array}
$$

Bring down -1. The successive products are 3, -9, 39, -120, 342, and adding them to the next coefficients gives the bottom row -1, 3, -13, 40, -114, 340. Therefore Q(x)=-x^4 + 3x^3 - 13x^2 + 40x - 114 and R=340; the remainder theorem identifies P(-3)=340. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -3 gives 340. The complete identity is P(x)=(x-(-3))(-x^4 + 3x^3 - 13x^2 + 40x - 114)+(340). When the result is used to test a root, the conclusion is conditional: -3 is a root only if this remainder is zero. Here the calculation reports 340, so the tableau does not certify a root unless that value is zero.

The recurrence is an instance of Horner evaluation, and the quotient coefficients are the intermediate partial values. This dual interpretation explains why division and evaluation are inseparable for a linear divisor. It also identifies the invariant to use when debugging: each new carry equals the next original coefficient plus r times the preceding carry.

## 5. Mathematical Extensions, Limits, and Common Errors — Revision, numerical interpretation, and source checks

The core proof chain is: the division algorithm gives P=(x-r)Q+R; evaluation at r gives R=P(r); therefore P(r)=0 iff x-r divides P. The synthetic recurrence computes the unique Q and R, and the same recurrence evaluates P in nested form. A correct root-location argument adds continuity and opposite endpoint signs; it does not infer uniqueness without further hypotheses.

Audit source calculations by reconciling all representations: coefficient row, recurrence, quotient, remainder, expanded identity, direct value, and root conclusion. In the approved extraction, the cubic division’s final identity has a constant-term typo; the quartic example’s final identity is corrupted; and the root interval example’s stated endpoint arithmetic does not match the polynomial. Each has been recalculated here and explicitly flagged rather than silently propagated.