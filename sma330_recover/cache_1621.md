## 1. Foundational Concepts, Definitions, and Axioms — Polynomial language and the division problem

Polynomial computation is one of the central numerical tasks because algorithms usually evaluate expressions through sequences of additions and multiplications. A polynomial of degree n can be represented by its coefficient vector, and division by x-r transforms that vector through a recurrence. Synthetic division is therefore not a visual trick; it is a compact realization of the polynomial division algorithm. It simultaneously computes the quotient coefficients and the remainder, and the remainder theorem identifies that constant with P(r).

Lesson 3 explicitly names polynomial definitions, the synthetic-division procedure, evaluation of selected values, nested form, and examples locating roots by endpoint signs. The numerical-analysis interpretation is restrained: fewer operations can reduce opportunities for arithmetic and rounding error, but no finite procedure guarantees a correct answer if its inputs or arithmetic are wrong. We distinguish exact algebraic identities from decimal approximations and check each result both by substitution and, when practical, by expansion.

The logic of root-finding is also important. A zero is a value at which the function is zero. A sign change over an interval guarantees a root for a continuous polynomial, but a root need not produce a sign change: a repeated factor can touch the axis. Synthetic division tests a candidate value exactly by producing its remainder; it does not by itself prove a root exists between arbitrary endpoints.

## 2. Theorems, Lemmas, and Analytical Properties — Division, remainder, factors, and roots

Let P have degree n and let r be any scalar. Polynomial division gives unique Q and R with P=(x-r)Q+R and deg R<1; hence R is a scalar. Evaluating at r proves R=P(r), while rearrangement gives Q=(P(x)-P(r))/(x-r) when x is treated algebraically. Coefficient comparison or long division proves existence; uniqueness follows because if (x-r)Q_1+R_1=(x-r)Q_2+R_2, then (x-r)(Q_1-Q_2)=R_2-R_1, and a nonzero multiple of x-r cannot be a nonzero constant.

Write P(x)=a_nx^n+...+a_0. Define b_n=a_n and b_k=a_k+r b_{k+1} for k=n-1,...,0. Then Q(x)=b_nx^{n-1}+b_{n-1}x^{n-2}+...+b_1 and R=b_0. Expanding (x-r)Q+R makes the intermediate coefficients cancel consecutively, leaving exactly P. The last recurrence is also Horner’s rule for P(r).

The factor theorem is an equivalence, not merely a one-way test. If P(r)=0 then the remainder is zero and x-r divides P; if x-r divides P then substitution gives P(r)=0. A root of multiplicity m means (x-r)^m divides P but (x-r)^(m+1) does not. This broader observation explains why repeated roots may not change sign, while the basic lesson’s sign-change argument only establishes at least one root under continuity.

## 3. Formal Proofs, Derivations, and Methods — From long division to the synthetic recurrence

Algorithmic invariant: after processing the coefficient a_k, the partial quotient coefficients already produced are exactly those needed to cancel the high-degree terms of P-(x-r)Q. The next multiplication by r is the amount contributed by the factor -r in the divisor; adding it to a_k determines the next quotient coefficient. This invariant explains why the same recurrence works for every degree and why omitted zero coefficients invalidate alignment.

To evaluate P(x) in nested form, initialize v=a_n and update v <- xv+a_k for k=n-1,...,0. This needs n multiplications and n additions. Directly computing all powers can require more work and repeated reuse of rounded powers. The source’s claim about reducing relative error should be read as a numerical advantage of fewer operations, not a universal bound independent of arithmetic precision.

For an interval root test, evaluate both endpoints using synthetic division or Horner’s rule. Report the two signs before claiming existence. A zero endpoint is already a root; opposite nonzero signs give an interior root by continuity; equal signs give no conclusion. To divide successively by factors, repeat synthetic division only after confirming the remainder is zero for the proposed factor.

## 4. Representative Worked Examples and Solutions — Checked synthetic-division and nested-form examples

### 4.1 Remainder Evaluation

Worked example 1 — remainder evaluation. The dividend is P(x)=-4x^5 + x^4 + 6x^3 - 2x^2 + 3x - 5, and the proposed divisor is x-(1). The coefficient row, including any zeros, is -4, 1, 6, -2, 3, -5. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
1 & -4 & 1 & 6 & -2 & 3 & -5 \\
 & -4 & -3 & 3 & 1 & 4 \\
 & -4 & -3 & 3 & 1 & 4 & -1
\end{array}
$$

Bring down -4. The successive products are -4, -3, 3, 1, 4, and adding them to the next coefficients gives the bottom row -4, -3, 3, 1, 4, -1. Therefore Q(x)=-4x^4 - 3x^3 + 3x^2 + x + 4 and R=-1; the remainder theorem identifies P(1)=-1. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 1 gives -1. The complete identity is P(x)=(x-(1))(-4x^4 - 3x^3 + 3x^2 + x + 4)+(-1). When the result is used to test a root, the conclusion is conditional: 1 is a root only if this remainder is zero. Here the calculation reports -1, so the tableau does not certify a root unless that value is zero.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.2 Quotient Reconstruction

Worked example 2 — quotient reconstruction. Consider P(x)=3x^3 + 5 and test r=2. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
2 & 3 & 0 & 0 & 5 \\
 & 6 & 12 & 24 \\
 & 3 & 6 & 12 & 29
\end{array}
$$

The multiply-and-add recurrence begins with 3. At each subsequent column it multiplies by 2, then adds the original coefficient. The product row is 6, 12, 24; the resulting row is 3, 6, 12, 29. Reading it by powers gives Q(x)=3x^2 + 6x + 12, while the final scalar is R=29. Hence P(x)=(x-(2))Q(x)+R.

Set x=2 in the identity: the factor term vanishes and the equation reduces to P(2)=29. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(2). If the original divisor were described as x+2, its corresponding trial number would be negative.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.3 A Missing-Power Alignment Check

Worked example 3 — a missing-power alignment check. A candidate computation uses P(x)=-3x^4 + 2x^3 - 6x^2 - x + 4 at r=3. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
3 & -3 & 2 & -6 & -1 & 4 \\
 & -9 & -21 & -81 & -246 \\
 & -3 & -7 & -27 & -82 & -242
\end{array}
$$

Carry -3 down; use the current carry times 3 to form the products -9, -21, -81, -246; add columnwise to obtain -3, -7, -27, -82, -242. The quotient is Q(x)=-3x^3 - 7x^2 - 27x - 82 and the remainder is R=-242. Therefore the algebraic certificate is P(x)=(x-(3))(-3x^3 - 7x^2 - 27x - 82)+(-242), and P(3)=-242 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(3) directly. A zero remainder establishes the factor x-(3); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.4 Factor Certification

Worked example 4 — factor certification. The dividend is P(x)=4x^5 - 4x^4 + x^3 + 6x^2 - 2x + 3, and the proposed divisor is x-(-3). The coefficient row, including any zeros, is 4, -4, 1, 6, -2, 3. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
-3 & 4 & -4 & 1 & 6 & -2 & 3 \\
 & -12 & 48 & -147 & 423 & -1263 \\
 & 4 & -16 & 49 & -141 & 421 & -1260
\end{array}
$$

Bring down 4. The successive products are -12, 48, -147, 423, -1263, and adding them to the next coefficients gives the bottom row 4, -16, 49, -141, 421, -1260. Therefore Q(x)=4x^4 - 16x^3 + 49x^2 - 141x + 421 and R=-1260; the remainder theorem identifies P(-3)=-1260. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -3 gives -1260. The complete identity is P(x)=(x-(-3))(4x^4 - 16x^3 + 49x^2 - 141x + 421)+(-1260). When the result is used to test a root, the conclusion is conditional: -3 is a root only if this remainder is zero. Here the calculation reports -1260, so the tableau does not certify a root unless that value is zero.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.5 Nested Numerical Evaluation

Worked example 5 — nested numerical evaluation. Consider P(x)=-2x^3 + 3x^2 and test r=-2. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
-2 & -2 & 3 & 0 & 0 \\
 & 4 & -14 & 28 \\
 & -2 & 7 & -14 & 28
\end{array}
$$

The multiply-and-add recurrence begins with -2. At each subsequent column it multiplies by -2, then adds the original coefficient. The product row is 4, -14, 28; the resulting row is -2, 7, -14, 28. Reading it by powers gives Q(x)=-2x^2 + 7x - 14, while the final scalar is R=28. Hence P(x)=(x-(-2))Q(x)+R.

Set x=-2 in the identity: the factor term vanishes and the equation reduces to P(-2)=28. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(-2). If the original divisor were described as x+2, its corresponding trial number would be negative.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.6 Sign-Convention Practice

Worked example 6 — sign-convention practice. A candidate computation uses P(x)=5x^4 + 2x^2 - 6x - 1 at r=-1. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
-1 & 5 & 0 & 2 & -6 & -1 \\
 & -5 & 5 & -7 & 13 \\
 & 5 & -5 & 7 & -13 & 12
\end{array}
$$

Carry 5 down; use the current carry times -1 to form the products -5, 5, -7, 13; add columnwise to obtain 5, -5, 7, -13, 12. The quotient is Q(x)=5x^3 - 5x^2 + 7x - 13 and the remainder is R=12. Therefore the algebraic certificate is P(x)=(x-(-1))(5x^3 - 5x^2 + 7x - 13)+(12), and P(-1)=12 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(-1) directly. A zero remainder establishes the factor x-(-1); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.7 A Root Candidate That Is Not A Root

Worked example 7 — a root candidate that is not a root. The dividend is P(x)=-x^5 + 4x^4 - 4x^3 + x^2 + 6x - 2, and the proposed divisor is x-(0). The coefficient row, including any zeros, is -1, 4, -4, 1, 6, -2. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
0 & -1 & 4 & -4 & 1 & 6 & -2 \\
 & 0 & 0 & 0 & 0 & 0 \\
 & -1 & 4 & -4 & 1 & 6 & -2
\end{array}
$$

Bring down -1. The successive products are 0, 0, 0, 0, 0, and adding them to the next coefficients gives the bottom row -1, 4, -4, 1, 6, -2. Therefore Q(x)=-x^4 + 4x^3 - 4x^2 + x + 6 and R=-2; the remainder theorem identifies P(0)=-2. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 0 gives -2. The complete identity is P(x)=(x-(0))(-x^4 + 4x^3 - 4x^2 + x + 6)+(-2). When the result is used to test a root, the conclusion is conditional: 0 is a root only if this remainder is zero. Here the calculation reports -2, so the tableau does not certify a root unless that value is zero.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.8 A Sparse Polynomial

Worked example 8 — a sparse polynomial. Consider P(x)=6x^3 - 2x^2 + 3x - 5 and test r=1. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
1 & 6 & -2 & 3 & -5 \\
 & 6 & 4 & 7 \\
 & 6 & 4 & 7 & 2
\end{array}
$$

The multiply-and-add recurrence begins with 6. At each subsequent column it multiplies by 1, then adds the original coefficient. The product row is 6, 4, 7; the resulting row is 6, 4, 7, 2. Reading it by powers gives Q(x)=6x^2 + 4x + 7, while the final scalar is R=2. Hence P(x)=(x-(1))Q(x)+R.

Set x=1 in the identity: the factor term vanishes and the equation reduces to P(1)=2. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(1). If the original divisor were described as x+1, its corresponding trial number would be negative.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.9 Independent Substitution

Worked example 9 — independent substitution. A candidate computation uses P(x)=x^4 + 5x^3 - 3x^2 + 2x - 6 at r=2. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
2 & 1 & 5 & -3 & 2 & -6 \\
 & 2 & 14 & 22 & 48 \\
 & 1 & 7 & 11 & 24 & 42
\end{array}
$$

Carry 1 down; use the current carry times 2 to form the products 2, 14, 22, 48; add columnwise to obtain 1, 7, 11, 24, 42. The quotient is Q(x)=x^3 + 7x^2 + 11x + 24 and the remainder is R=42. Therefore the algebraic certificate is P(x)=(x-(2))(x^3 + 7x^2 + 11x + 24)+(42), and P(2)=42 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(2) directly. A zero remainder establishes the factor x-(2); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.10 Coefficient-Order Auditing

Worked example 10 — coefficient-order auditing. The dividend is P(x)=-6x^5 + 4x^3 - 4x^2 + 6, and the proposed divisor is x-(3). The coefficient row, including any zeros, is -6, 0, 4, -4, 0, 6. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
3 & -6 & 0 & 4 & -4 & 0 & 6 \\
 & -18 & -54 & -150 & -462 & -1386 \\
 & -6 & -18 & -50 & -154 & -462 & -1380
\end{array}
$$

Bring down -6. The successive products are -18, -54, -150, -462, -1386, and adding them to the next coefficients gives the bottom row -6, -18, -50, -154, -462, -1380. Therefore Q(x)=-6x^4 - 18x^3 - 50x^2 - 154x - 462 and R=-1380; the remainder theorem identifies P(3)=-1380. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 3 gives -1380. The complete identity is P(x)=(x-(3))(-6x^4 - 18x^3 - 50x^2 - 154x - 462)+(-1380). When the result is used to test a root, the conclusion is conditional: 3 is a root only if this remainder is zero. Here the calculation reports -1380, so the tableau does not certify a root unless that value is zero.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.11 A Decimal Input

Worked example 11 — a decimal input. Consider P(x)=x^3 + 6x^2 - 2x + 3 and test r=-3. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
-3 & 1 & 6 & -2 & 3 \\
 & -3 & -9 & 33 \\
 & 1 & 3 & -11 & 36
\end{array}
$$

The multiply-and-add recurrence begins with 1. At each subsequent column it multiplies by -3, then adds the original coefficient. The product row is -3, -9, 33; the resulting row is 1, 3, -11, 36. Reading it by powers gives Q(x)=x^2 + 3x - 11, while the final scalar is R=36. Hence P(x)=(x-(-3))Q(x)+R.

Set x=-3 in the identity: the factor term vanishes and the equation reduces to P(-3)=36. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(-3). If the original divisor were described as x+3, its corresponding trial number would be negative.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.12 Degree Reduction

Worked example 12 — degree reduction. A candidate computation uses P(x)=-5x^4 + 5x^2 - 3x + 2 at r=-2. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
-2 & -5 & 0 & 5 & -3 & 2 \\
 & 10 & -20 & 30 & -54 \\
 & -5 & 10 & -15 & 27 & -52
\end{array}
$$

Carry -5 down; use the current carry times -2 to form the products 10, -20, 30, -54; add columnwise to obtain -5, 10, -15, 27, -52. The quotient is Q(x)=-5x^3 + 10x^2 - 15x + 27 and the remainder is R=-52. Therefore the algebraic certificate is P(x)=(x-(-2))(-5x^3 + 10x^2 - 15x + 27)+(-52), and P(-2)=-52 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(-2) directly. A zero remainder establishes the factor x-(-2); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.13 Remainder Evaluation

Worked example 13 — remainder evaluation. The dividend is P(x)=2x^5 - 6x^4 - x^3 + 4x^2 - 4x + 1, and the proposed divisor is x-(-1). The coefficient row, including any zeros, is 2, -6, -1, 4, -4, 1. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
-1 & 2 & -6 & -1 & 4 & -4 & 1 \\
 & -2 & 8 & -7 & 3 & 1 \\
 & 2 & -8 & 7 & -3 & -1 & 2
\end{array}
$$

Bring down 2. The successive products are -2, 8, -7, 3, 1, and adding them to the next coefficients gives the bottom row 2, -8, 7, -3, -1, 2. Therefore Q(x)=2x^4 - 8x^3 + 7x^2 - 3x - 1 and R=2; the remainder theorem identifies P(-1)=2. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -1 gives 2. The complete identity is P(x)=(x-(-1))(2x^4 - 8x^3 + 7x^2 - 3x - 1)+(2). When the result is used to test a root, the conclusion is conditional: -1 is a root only if this remainder is zero. Here the calculation reports 2, so the tableau does not certify a root unless that value is zero.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.14 Quotient Reconstruction

Worked example 14 — quotient reconstruction. Consider P(x)=-4x^3 + 6x - 2 and test r=0. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
0 & -4 & 0 & 6 & -2 \\
 & 0 & 0 & 0 \\
 & -4 & 0 & 6 & -2
\end{array}
$$

The multiply-and-add recurrence begins with -4. At each subsequent column it multiplies by 0, then adds the original coefficient. The product row is 0, 0, 0; the resulting row is -4, 0, 6, -2. Reading it by powers gives Q(x)=-4x^2 + 6, while the final scalar is R=-2. Hence P(x)=(x-(0))Q(x)+R.

Set x=0 in the identity: the factor term vanishes and the equation reduces to P(0)=-2. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(0). If the original divisor were described as x+0, its corresponding trial number would be negative.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.15 A Missing-Power Alignment Check

Worked example 15 — a missing-power alignment check. A candidate computation uses P(x)=3x^4 - 5x^3 - 3 at r=1. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
1 & 3 & -5 & 0 & 0 & -3 \\
 & 3 & -2 & -2 & -2 \\
 & 3 & -2 & -2 & -2 & -5
\end{array}
$$

Carry 3 down; use the current carry times 1 to form the products 3, -2, -2, -2; add columnwise to obtain 3, -2, -2, -2, -5. The quotient is Q(x)=3x^3 - 2x^2 - 2x - 2 and the remainder is R=-5. Therefore the algebraic certificate is P(x)=(x-(1))(3x^3 - 2x^2 - 2x - 2)+(-5), and P(1)=-5 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(1) directly. A zero remainder establishes the factor x-(1); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.16 Factor Certification

Worked example 16 — factor certification. The dividend is P(x)=-3x^5 + 2x^4 - 6x^3 - x^2 + 4x - 4, and the proposed divisor is x-(2). The coefficient row, including any zeros, is -3, 2, -6, -1, 4, -4. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
2 & -3 & 2 & -6 & -1 & 4 & -4 \\
 & -6 & -8 & -28 & -58 & -108 \\
 & -3 & -4 & -14 & -29 & -54 & -112
\end{array}
$$

Bring down -3. The successive products are -6, -8, -28, -58, -108, and adding them to the next coefficients gives the bottom row -3, -4, -14, -29, -54, -112. Therefore Q(x)=-3x^4 - 4x^3 - 14x^2 - 29x - 54 and R=-112; the remainder theorem identifies P(2)=-112. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 2 gives -112. The complete identity is P(x)=(x-(2))(-3x^4 - 4x^3 - 14x^2 - 29x - 54)+(-112). When the result is used to test a root, the conclusion is conditional: 2 is a root only if this remainder is zero. Here the calculation reports -112, so the tableau does not certify a root unless that value is zero.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.17 Nested Numerical Evaluation

Worked example 17 — nested numerical evaluation. Consider P(x)=4x^3 - 4x^2 + x + 6 and test r=3. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
3 & 4 & -4 & 1 & 6 \\
 & 12 & 24 & 75 \\
 & 4 & 8 & 25 & 81
\end{array}
$$

The multiply-and-add recurrence begins with 4. At each subsequent column it multiplies by 3, then adds the original coefficient. The product row is 12, 24, 75; the resulting row is 4, 8, 25, 81. Reading it by powers gives Q(x)=4x^2 + 8x + 25, while the final scalar is R=81. Hence P(x)=(x-(3))Q(x)+R.

Set x=3 in the identity: the factor term vanishes and the equation reduces to P(3)=81. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(3). If the original divisor were described as x+3, its corresponding trial number would be negative.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.18 Sign-Convention Practice

Worked example 18 — sign-convention practice. A candidate computation uses P(x)=-2x^4 - 5x^2 + 5 at r=-3. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
-3 & -2 & 0 & -5 & 0 & 5 \\
 & 6 & -18 & 69 & -207 \\
 & -2 & 6 & -23 & 69 & -202
\end{array}
$$

Carry -2 down; use the current carry times -3 to form the products 6, -18, 69, -207; add columnwise to obtain -2, 6, -23, 69, -202. The quotient is Q(x)=-2x^3 + 6x^2 - 23x + 69 and the remainder is R=-202. Therefore the algebraic certificate is P(x)=(x-(-3))(-2x^3 + 6x^2 - 23x + 69)+(-202), and P(-3)=-202 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(-3) directly. A zero remainder establishes the factor x-(-3); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.19 A Root Candidate That Is Not A Root

Worked example 19 — a root candidate that is not a root. The dividend is P(x)=5x^5 - 3x^4 + 2x^3 - 6x^2 - x + 4, and the proposed divisor is x-(-2). The coefficient row, including any zeros, is 5, -3, 2, -6, -1, 4. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
-2 & 5 & -3 & 2 & -6 & -1 & 4 \\
 & -10 & 26 & -56 & 124 & -246 \\
 & 5 & -13 & 28 & -62 & 123 & -242
\end{array}
$$

Bring down 5. The successive products are -10, 26, -56, 124, -246, and adding them to the next coefficients gives the bottom row 5, -13, 28, -62, 123, -242. Therefore Q(x)=5x^4 - 13x^3 + 28x^2 - 62x + 123 and R=-242; the remainder theorem identifies P(-2)=-242. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -2 gives -242. The complete identity is P(x)=(x-(-2))(5x^4 - 13x^3 + 28x^2 - 62x + 123)+(-242). When the result is used to test a root, the conclusion is conditional: -2 is a root only if this remainder is zero. Here the calculation reports -242, so the tableau does not certify a root unless that value is zero.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.20 A Sparse Polynomial

Worked example 20 — a sparse polynomial. Consider P(x)=-x^3 + 4x^2 + 1 and test r=-1. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
-1 & -1 & 4 & 0 & 1 \\
 & 1 & -5 & 5 \\
 & -1 & 5 & -5 & 6
\end{array}
$$

The multiply-and-add recurrence begins with -1. At each subsequent column it multiplies by -1, then adds the original coefficient. The product row is 1, -5, 5; the resulting row is -1, 5, -5, 6. Reading it by powers gives Q(x)=-x^2 + 5x - 5, while the final scalar is R=6. Hence P(x)=(x-(-1))Q(x)+R.

Set x=-1 in the identity: the factor term vanishes and the equation reduces to P(-1)=6. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(-1). If the original divisor were described as x+1, its corresponding trial number would be negative.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.21 Independent Substitution

Worked example 21 — independent substitution. A candidate computation uses P(x)=6x^4 - 2x^3 + 3x^2 - 5x at r=0. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
0 & 6 & -2 & 3 & -5 & 0 \\
 & 0 & 0 & 0 & 0 \\
 & 6 & -2 & 3 & -5 & 0
\end{array}
$$

Carry 6 down; use the current carry times 0 to form the products 0, 0, 0, 0; add columnwise to obtain 6, -2, 3, -5, 0. The quotient is Q(x)=6x^3 - 2x^2 + 3x - 5 and the remainder is R=0. Therefore the algebraic certificate is P(x)=(x-(0))(6x^3 - 2x^2 + 3x - 5)+(0), and P(0)=0 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(0) directly. A zero remainder establishes the factor x-(0); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.22 Coefficient-Order Auditing

Worked example 22 — coefficient-order auditing. The dividend is P(x)=x^5 - 3x^3 + 2x^2 - 6x - 1, and the proposed divisor is x-(1). The coefficient row, including any zeros, is 1, 0, -3, 2, -6, -1. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
1 & 1 & 0 & -3 & 2 & -6 & -1 \\
 & 1 & 1 & -2 & 0 & -6 \\
 & 1 & 1 & -2 & 0 & -6 & -7
\end{array}
$$

Bring down 1. The successive products are 1, 1, -2, 0, -6, and adding them to the next coefficients gives the bottom row 1, 1, -2, 0, -6, -7. Therefore Q(x)=x^4 + x^3 - 2x^2 - 6 and R=-7; the remainder theorem identifies P(1)=-7. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 1 gives -7. The complete identity is P(x)=(x-(1))(x^4 + x^3 - 2x^2 - 6)+(-7). When the result is used to test a root, the conclusion is conditional: 1 is a root only if this remainder is zero. Here the calculation reports -7, so the tableau does not certify a root unless that value is zero.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.23 A Decimal Input

Worked example 23 — a decimal input. Consider P(x)=-6x^3 - x^2 + 4x - 4 and test r=2. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
2 & -6 & -1 & 4 & -4 \\
 & -12 & -26 & -44 \\
 & -6 & -13 & -22 & -48
\end{array}
$$

The multiply-and-add recurrence begins with -6. At each subsequent column it multiplies by 2, then adds the original coefficient. The product row is -12, -26, -44; the resulting row is -6, -13, -22, -48. Reading it by powers gives Q(x)=-6x^2 - 13x - 22, while the final scalar is R=-48. Hence P(x)=(x-(2))Q(x)+R.

Set x=2 in the identity: the factor term vanishes and the equation reduces to P(2)=-48. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(2). If the original divisor were described as x+2, its corresponding trial number would be negative.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.24 Degree Reduction

Worked example 24 — degree reduction. A candidate computation uses P(x)=x^4 + 6x^3 - 2x^2 + 3x - 5 at r=3. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
3 & 1 & 6 & -2 & 3 & -5 \\
 & 3 & 27 & 75 & 234 \\
 & 1 & 9 & 25 & 78 & 229
\end{array}
$$

Carry 1 down; use the current carry times 3 to form the products 3, 27, 75, 234; add columnwise to obtain 1, 9, 25, 78, 229. The quotient is Q(x)=x^3 + 9x^2 + 25x + 78 and the remainder is R=229. Therefore the algebraic certificate is P(x)=(x-(3))(x^3 + 9x^2 + 25x + 78)+(229), and P(3)=229 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(3) directly. A zero remainder establishes the factor x-(3); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.25 Remainder Evaluation

Worked example 25 — remainder evaluation. The dividend is P(x)=-5x^5 + 5x^3 - 3x^2 - 6, and the proposed divisor is x-(-3). The coefficient row, including any zeros, is -5, 0, 5, -3, 0, -6. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
-3 & -5 & 0 & 5 & -3 & 0 & -6 \\
 & 15 & -45 & 120 & -351 & 1053 \\
 & -5 & 15 & -40 & 117 & -351 & 1047
\end{array}
$$

Bring down -5. The successive products are 15, -45, 120, -351, 1053, and adding them to the next coefficients gives the bottom row -5, 15, -40, 117, -351, 1047. Therefore Q(x)=-5x^4 + 15x^3 - 40x^2 + 117x - 351 and R=1047; the remainder theorem identifies P(-3)=1047. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -3 gives 1047. The complete identity is P(x)=(x-(-3))(-5x^4 + 15x^3 - 40x^2 + 117x - 351)+(1047). When the result is used to test a root, the conclusion is conditional: -3 is a root only if this remainder is zero. Here the calculation reports 1047, so the tableau does not certify a root unless that value is zero.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.26 Quotient Reconstruction

Worked example 26 — quotient reconstruction. Consider P(x)=2x^3 - x + 4 and test r=-2. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
-2 & 2 & 0 & -1 & 4 \\
 & -4 & 8 & -14 \\
 & 2 & -4 & 7 & -10
\end{array}
$$

The multiply-and-add recurrence begins with 2. At each subsequent column it multiplies by -2, then adds the original coefficient. The product row is -4, 8, -14; the resulting row is 2, -4, 7, -10. Reading it by powers gives Q(x)=2x^2 - 4x + 7, while the final scalar is R=-10. Hence P(x)=(x-(-2))Q(x)+R.

Set x=-2 in the identity: the factor term vanishes and the equation reduces to P(-2)=-10. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(-2). If the original divisor were described as x+2, its corresponding trial number would be negative.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.27 A Missing-Power Alignment Check

Worked example 27 — a missing-power alignment check. A candidate computation uses P(x)=-4x^4 + x^3 + 6x^2 - 2x + 3 at r=-1. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
-1 & -4 & 1 & 6 & -2 & 3 \\
 & 4 & -5 & -1 & 3 \\
 & -4 & 5 & 1 & -3 & 6
\end{array}
$$

Carry -4 down; use the current carry times -1 to form the products 4, -5, -1, 3; add columnwise to obtain -4, 5, 1, -3, 6. The quotient is Q(x)=-4x^3 + 5x^2 + x - 3 and the remainder is R=6. Therefore the algebraic certificate is P(x)=(x-(-1))(-4x^3 + 5x^2 + x - 3)+(6), and P(-1)=6 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(-1) directly. A zero remainder establishes the factor x-(-1); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.28 Factor Certification

Worked example 28 — factor certification. The dividend is P(x)=3x^5 - 5x^4 + 5x^2 - 3x + 2, and the proposed divisor is x-(0). The coefficient row, including any zeros, is 3, -5, 0, 5, -3, 2. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
0 & 3 & -5 & 0 & 5 & -3 & 2 \\
 & 0 & 0 & 0 & 0 & 0 \\
 & 3 & -5 & 0 & 5 & -3 & 2
\end{array}
$$

Bring down 3. The successive products are 0, 0, 0, 0, 0, and adding them to the next coefficients gives the bottom row 3, -5, 0, 5, -3, 2. Therefore Q(x)=3x^4 - 5x^3 + 5x - 3 and R=2; the remainder theorem identifies P(0)=2. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 0 gives 2. The complete identity is P(x)=(x-(0))(3x^4 - 5x^3 + 5x - 3)+(2). When the result is used to test a root, the conclusion is conditional: 0 is a root only if this remainder is zero. Here the calculation reports 2, so the tableau does not certify a root unless that value is zero.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.29 Nested Numerical Evaluation

Worked example 29 — nested numerical evaluation. Consider P(x)=-3x^3 + 2x^2 - 6x - 1 and test r=1. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
1 & -3 & 2 & -6 & -1 \\
 & -3 & -1 & -7 \\
 & -3 & -1 & -7 & -8
\end{array}
$$

The multiply-and-add recurrence begins with -3. At each subsequent column it multiplies by 1, then adds the original coefficient. The product row is -3, -1, -7; the resulting row is -3, -1, -7, -8. Reading it by powers gives Q(x)=-3x^2 - x - 7, while the final scalar is R=-8. Hence P(x)=(x-(1))Q(x)+R.

Set x=1 in the identity: the factor term vanishes and the equation reduces to P(1)=-8. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(1). If the original divisor were described as x+1, its corresponding trial number would be negative.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.30 Sign-Convention Practice

Worked example 30 — sign-convention practice. A candidate computation uses P(x)=4x^4 + x^2 - 2 at r=2. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
2 & 4 & 0 & 1 & 0 & -2 \\
 & 8 & 16 & 34 & 68 \\
 & 4 & 8 & 17 & 34 & 66
\end{array}
$$

Carry 4 down; use the current carry times 2 to form the products 8, 16, 34, 68; add columnwise to obtain 4, 8, 17, 34, 66. The quotient is Q(x)=4x^3 + 8x^2 + 17x + 34 and the remainder is R=66. Therefore the algebraic certificate is P(x)=(x-(2))(4x^3 + 8x^2 + 17x + 34)+(66), and P(2)=66 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(2) directly. A zero remainder establishes the factor x-(2); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.31 A Root Candidate That Is Not A Root

Worked example 31 — a root candidate that is not a root. The dividend is P(x)=-2x^5 + 3x^4 - 5x^3 + 5x - 3, and the proposed divisor is x-(3). The coefficient row, including any zeros, is -2, 3, -5, 0, 5, -3. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
3 & -2 & 3 & -5 & 0 & 5 & -3 \\
 & -6 & -9 & -42 & -126 & -363 \\
 & -2 & -3 & -14 & -42 & -121 & -366
\end{array}
$$

Bring down -2. The successive products are -6, -9, -42, -126, -363, and adding them to the next coefficients gives the bottom row -2, -3, -14, -42, -121, -366. Therefore Q(x)=-2x^4 - 3x^3 - 14x^2 - 42x - 121 and R=-366; the remainder theorem identifies P(3)=-366. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 3 gives -366. The complete identity is P(x)=(x-(3))(-2x^4 - 3x^3 - 14x^2 - 42x - 121)+(-366). When the result is used to test a root, the conclusion is conditional: 3 is a root only if this remainder is zero. Here the calculation reports -366, so the tableau does not certify a root unless that value is zero.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.32 A Sparse Polynomial

Worked example 32 — a sparse polynomial. Consider P(x)=5x^3 - 3x^2 + 2x - 6 and test r=-3. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^3 down to x^0; this makes clear that the first 3 bottom entries become coefficients of a polynomial of degree 2.

$$
\begin{array}{rrrrr}
-3 & 5 & -3 & 2 & -6 \\
 & -15 & 54 & -168 \\
 & 5 & -18 & 56 & -174
\end{array}
$$

The multiply-and-add recurrence begins with 5. At each subsequent column it multiplies by -3, then adds the original coefficient. The product row is -15, 54, -168; the resulting row is 5, -18, 56, -174. Reading it by powers gives Q(x)=5x^2 - 18x + 56, while the final scalar is R=-174. Hence P(x)=(x-(-3))Q(x)+R.

Set x=-3 in the identity: the factor term vanishes and the equation reduces to P(-3)=-174. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(-3). If the original divisor were described as x+3, its corresponding trial number would be negative.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.33 Independent Substitution

Worked example 33 — independent substitution. A candidate computation uses P(x)=-x^4 + 4x^3 - 4x^2 + x + 6 at r=-2. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrr}
-2 & -1 & 4 & -4 & 1 & 6 \\
 & 2 & -12 & 32 & -66 \\
 & -1 & 6 & -16 & 33 & -60
\end{array}
$$

Carry -1 down; use the current carry times -2 to form the products 2, -12, 32, -66; add columnwise to obtain -1, 6, -16, 33, -60. The quotient is Q(x)=-x^3 + 6x^2 - 16x + 33 and the remainder is R=-60. Therefore the algebraic certificate is P(x)=(x-(-2))(-x^3 + 6x^2 - 16x + 33)+(-60), and P(-2)=-60 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(-2) directly. A zero remainder establishes the factor x-(-2); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

### 4.34 Coefficient-Order Auditing

Worked example 34 — coefficient-order auditing. The dividend is P(x)=6x^5 + 3x^3 - 5x^2 + 5, and the proposed divisor is x-(-1). The coefficient row, including any zeros, is 6, 0, 3, -5, 0, 5. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrrrr}
-1 & 6 & 0 & 3 & -5 & 0 & 5 \\
 & -6 & 6 & -9 & 14 & -14 \\
 & 6 & -6 & 9 & -14 & 14 & -9
\end{array}
$$

Bring down 6. The successive products are -6, 6, -9, 14, -14, and adding them to the next coefficients gives the bottom row 6, -6, 9, -14, 14, -9. Therefore Q(x)=6x^4 - 6x^3 + 9x^2 - 14x + 14 and R=-9; the remainder theorem identifies P(-1)=-9. This is a 5-degree dividend, so the quotient degree is 4, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -1 gives -9. The complete identity is P(x)=(x-(-1))(6x^4 - 6x^3 + 9x^2 - 14x + 14)+(-9). When the result is used to test a root, the conclusion is conditional: -1 is a root only if this remainder is zero. Here the calculation reports -9, so the tableau does not certify a root unless that value is zero.

The computation also demonstrates degree reduction: division by a nonzero linear factor leaves a quotient one degree lower, regardless of whether the remainder is zero. Only a zero remainder makes the divisor an exact factor. Do not equate 'quotient produced' with 'factor found'; every division produces a quotient.

## 5. Mathematical Extensions, Limits, and Common Errors — Revision, numerical interpretation, and source checks

A reliable solution states the divisor, its trial value, a complete coefficient row, the bottom row, the quotient, the remainder, and an independent check. Explain what the remainder implies rather than stopping at the tableau. If decimals occur, distinguish exact polynomial identities from rounded evaluations. Fewer operations in nested form can reduce opportunities for error but cannot repair wrong coefficients.

The approved source extraction contains specific inconsistencies. For P=x^3-3x^2+5x+7 and r=2, the displayed remainder 13 and quotient x^2-x+3 are consistent, but one printed identity changes the constant to +17; the correct identity retains +7. For 2x^4-3x^2+3x-4 divided by x+2, r=-2 and the correct remainder is 10, not the corrupted value 1. The source also claims f(1)=-6 for x^3-2x^2+5; actual substitution gives 4. These are transcription or arithmetic errors, not mathematical variants.