## 1. Foundational Concepts, Definitions, and Axioms — Polynomial language and the division problem

Imagine a staircase recipe: at each step, the current total is multiplied by the chosen input and then a coefficient is added. A polynomial is a finite arithmetic recipe made from whole-number powers of one variable and fixed coefficients. Synthetic division is the staircase calculation written as a compact row of additions and multiplications. It also answers a division question: dividing by a linear factor leaves a quotient polynomial and a single constant remainder. The method is valuable because one careful row can evaluate a polynomial, test a proposed root, and produce a factorization when the remainder is zero.

The approved Lesson 3 begins with short notes on polynomials and a point-form procedure for synthetic division. It does not ask this lesson to cover interpolation formulas or a general survey of numerical error. We therefore stay with polynomial vocabulary, the division identity, the remainder and factor theorems, roots, nested evaluation, and the sample computations. These ideas are the bridge into the next lesson, but they are taught here only where they clarify the present method.

Every example begins by writing powers in descending order and placing zero coefficients where terms are absent. That is not cosmetic: each column has a fixed power attached to it. A row shifted one column has become a different polynomial. Students should say the divisor aloud as x minus r before writing the test value r, then explain which entries of the bottom row belong to the quotient and which final entry is the remainder.

## 2. Theorems, Lemmas, and Analytical Properties — Division, remainder, factors, and roots

A polynomial has terms such as 3x^2, -2x, and 5. The coefficient is the number multiplying the power, the degree is the largest power with a nonzero coefficient, and a constant has power zero. Missing powers must still be represented by zero when a coefficient row is made. For example, 2x^4-3x^2+3x-4 has coefficient row (2,0,-3,3,-4). The zero says that no x^3 contribution is present.

For a divisor x-r, the division identity says P(x)=(x-r)Q(x)+R. The remainder has to be constant because it has degree less than the degree-one divisor. Substituting x=r removes the first term, so R=P(r). This is the remainder theorem. The factor theorem follows: r is a root exactly when R=0, because then P(x)=(x-r)Q(x). Synthetic division is the short row method for calculating these quantities.

Nested form rewrites the polynomial by repeatedly factoring out x. For example, x^3-6x^2+3x-0.14 becomes ((x-6)x+3)x-0.14. Its order of operations mirrors repeated multiply-and-add steps. The lesson notes that this reduces the relative error associated with a larger number of computations. It does not change the polynomial or its exact value.

## 3. Formal Proofs, Derivations, and Methods — From long division to the synthetic recurrence

Procedure: arrange every coefficient from highest power to constant; include zeros for absent powers; write r at left for divisor x-r; bring down the leading coefficient; multiply the current bottom entry by r; add to the next coefficient; repeat. All bottom entries except the last are quotient coefficients. The last is the remainder and equals P(r). To check, substitute r directly, or expand (x-r)Q+R.

For decimal evaluation, nested form follows the same multiply-and-add pattern. Begin with the leading coefficient; multiply by the chosen x and add the next coefficient; continue to the constant. Pause after every addition to compare the coefficient column. Never change the divisor’s sign convention halfway through.

## 4. Representative Worked Examples and Solutions — Checked synthetic-division and nested-form examples

### 4.1 Remainder Evaluation

Worked example 1 — remainder evaluation. The dividend is P(x)=-3x^3 - 1, and the proposed divisor is x-(-2). The coefficient row, including any zeros, is -3, 0, 0, -1. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrr}
-2 & -3 & 0 & 0 & -1 \\
 & 6 & -12 & 24 \\
 & -3 & 6 & -12 & 23
\end{array}
$$

Bring down -3. The successive products are 6, -12, 24, and adding them to the next coefficients gives the bottom row -3, 6, -12, 23. Therefore Q(x)=-3x^2 + 6x - 12 and R=23; the remainder theorem identifies P(-2)=23. This is a 3-degree dividend, so the quotient degree is 2, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -2 gives 23. The complete identity is P(x)=(x-(-2))(-3x^2 + 6x - 12)+(23). When the result is used to test a root, the conclusion is conditional: -2 is a root only if this remainder is zero. Here the calculation reports 23, so the tableau does not certify a root unless that value is zero.

Read the row aloud as a recipe: start at -3, multiply by -2, add the next coefficient, and continue until the last column. The last number, 23, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.2 Quotient Reconstruction

Worked example 2 — quotient reconstruction. Consider P(x)=4x^4 - 4x^3 + x^2 + 6x - 2 and test r=-1. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^4 down to x^0; this makes clear that the first 4 bottom entries become coefficients of a polynomial of degree 3.

$$
\begin{array}{rrrrrr}
-1 & 4 & -4 & 1 & 6 & -2 \\
 & -4 & 8 & -9 & 3 \\
 & 4 & -8 & 9 & -3 & 1
\end{array}
$$

The multiply-and-add recurrence begins with 4. At each subsequent column it multiplies by -1, then adds the original coefficient. The product row is -4, 8, -9, 3; the resulting row is 4, -8, 9, -3, 1. Reading it by powers gives Q(x)=4x^3 - 8x^2 + 9x - 3, while the final scalar is R=1. Hence P(x)=(x-(-1))Q(x)+R.

Set x=-1 in the identity: the factor term vanishes and the equation reduces to P(-1)=1. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(-1). If the original divisor were described as x+1, its corresponding trial number would be negative.

Read the row aloud as a recipe: start at 4, multiply by -1, add the next coefficient, and continue until the last column. The last number, 1, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.3 A Missing-Power Alignment Check

Worked example 3 — a missing-power alignment check. A candidate computation uses P(x)=-2x^5 + 3x^4 - 5x^3 + 5x - 3 at r=0. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrrr}
0 & -2 & 3 & -5 & 0 & 5 & -3 \\
 & 0 & 0 & 0 & 0 & 0 \\
 & -2 & 3 & -5 & 0 & 5 & -3
\end{array}
$$

Carry -2 down; use the current carry times 0 to form the products 0, 0, 0, 0, 0; add columnwise to obtain -2, 3, -5, 0, 5, -3. The quotient is Q(x)=-2x^4 + 3x^3 - 5x^2 + 5 and the remainder is R=-3. Therefore the algebraic certificate is P(x)=(x-(0))(-2x^4 + 3x^3 - 5x^2 + 5)+(-3), and P(0)=-3 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(0) directly. A zero remainder establishes the factor x-(0); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

Read the row aloud as a recipe: start at -2, multiply by 0, add the next coefficient, and continue until the last column. The last number, -3, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.4 Factor Certification

Worked example 4 — factor certification. The dividend is P(x)=5x^3 - 3x^2 + 2x - 6, and the proposed divisor is x-(1). The coefficient row, including any zeros, is 5, -3, 2, -6. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrr}
1 & 5 & -3 & 2 & -6 \\
 & 5 & 2 & 4 \\
 & 5 & 2 & 4 & -2
\end{array}
$$

Bring down 5. The successive products are 5, 2, 4, and adding them to the next coefficients gives the bottom row 5, 2, 4, -2. Therefore Q(x)=5x^2 + 2x + 4 and R=-2; the remainder theorem identifies P(1)=-2. This is a 3-degree dividend, so the quotient degree is 2, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 1 gives -2. The complete identity is P(x)=(x-(1))(5x^2 + 2x + 4)+(-2). When the result is used to test a root, the conclusion is conditional: 1 is a root only if this remainder is zero. Here the calculation reports -2, so the tableau does not certify a root unless that value is zero.

Read the row aloud as a recipe: start at 5, multiply by 1, add the next coefficient, and continue until the last column. The last number, -2, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.5 Nested Numerical Evaluation

Worked example 5 — nested numerical evaluation. Consider P(x)=-x^4 - 4x^2 + x + 6 and test r=2. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^4 down to x^0; this makes clear that the first 4 bottom entries become coefficients of a polynomial of degree 3.

$$
\begin{array}{rrrrrr}
2 & -1 & 0 & -4 & 1 & 6 \\
 & -2 & -4 & -16 & -30 \\
 & -1 & -2 & -8 & -15 & -24
\end{array}
$$

The multiply-and-add recurrence begins with -1. At each subsequent column it multiplies by 2, then adds the original coefficient. The product row is -2, -4, -16, -30; the resulting row is -1, -2, -8, -15, -24. Reading it by powers gives Q(x)=-x^3 - 2x^2 - 8x - 15, while the final scalar is R=-24. Hence P(x)=(x-(2))Q(x)+R.

Set x=2 in the identity: the factor term vanishes and the equation reduces to P(2)=-24. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(2). If the original divisor were described as x+2, its corresponding trial number would be negative.

Read the row aloud as a recipe: start at -1, multiply by 2, add the next coefficient, and continue until the last column. The last number, -24, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.6 Sign-Convention Practice

Worked example 6 — sign-convention practice. A candidate computation uses P(x)=6x^5 - 2x^4 + 3x^3 - 5x^2 + 5 at r=-2. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrrr}
-2 & 6 & -2 & 3 & -5 & 0 & 5 \\
 & -12 & 28 & -62 & 134 & -268 \\
 & 6 & -14 & 31 & -67 & 134 & -263
\end{array}
$$

Carry 6 down; use the current carry times -2 to form the products -12, 28, -62, 134, -268; add columnwise to obtain 6, -14, 31, -67, 134, -263. The quotient is Q(x)=6x^4 - 14x^3 + 31x^2 - 67x + 134 and the remainder is R=-263. Therefore the algebraic certificate is P(x)=(x-(-2))(6x^4 - 14x^3 + 31x^2 - 67x + 134)+(-263), and P(-2)=-263 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(-2) directly. A zero remainder establishes the factor x-(-2); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

Read the row aloud as a recipe: start at 6, multiply by -2, add the next coefficient, and continue until the last column. The last number, -263, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.7 A Root Candidate That Is Not A Root

Worked example 7 — a root candidate that is not a root. The dividend is P(x)=x^3 + 5x^2 - 3x + 2, and the proposed divisor is x-(-1). The coefficient row, including any zeros, is 1, 5, -3, 2. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrr}
-1 & 1 & 5 & -3 & 2 \\
 & -1 & -4 & 7 \\
 & 1 & 4 & -7 & 9
\end{array}
$$

Bring down 1. The successive products are -1, -4, 7, and adding them to the next coefficients gives the bottom row 1, 4, -7, 9. Therefore Q(x)=x^2 + 4x - 7 and R=9; the remainder theorem identifies P(-1)=9. This is a 3-degree dividend, so the quotient degree is 2, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -1 gives 9. The complete identity is P(x)=(x-(-1))(x^2 + 4x - 7)+(9). When the result is used to test a root, the conclusion is conditional: -1 is a root only if this remainder is zero. Here the calculation reports 9, so the tableau does not certify a root unless that value is zero.

Read the row aloud as a recipe: start at 1, multiply by -1, add the next coefficient, and continue until the last column. The last number, 9, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.8 A Sparse Polynomial

Worked example 8 — a sparse polynomial. Consider P(x)=-6x^4 - x^3 + 4x^2 - 4x + 1 and test r=0. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^4 down to x^0; this makes clear that the first 4 bottom entries become coefficients of a polynomial of degree 3.

$$
\begin{array}{rrrrrr}
0 & -6 & -1 & 4 & -4 & 1 \\
 & 0 & 0 & 0 & 0 \\
 & -6 & -1 & 4 & -4 & 1
\end{array}
$$

The multiply-and-add recurrence begins with -6. At each subsequent column it multiplies by 0, then adds the original coefficient. The product row is 0, 0, 0, 0; the resulting row is -6, -1, 4, -4, 1. Reading it by powers gives Q(x)=-6x^3 - x^2 + 4x - 4, while the final scalar is R=1. Hence P(x)=(x-(0))Q(x)+R.

Set x=0 in the identity: the factor term vanishes and the equation reduces to P(0)=1. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(0). If the original divisor were described as x+0, its corresponding trial number would be negative.

Read the row aloud as a recipe: start at -6, multiply by 0, add the next coefficient, and continue until the last column. The last number, 1, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.9 Independent Substitution

Worked example 9 — independent substitution. A candidate computation uses P(x)=x^5 - 2x^3 + 3x^2 - 5x at r=1. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrrr}
1 & 1 & 0 & -2 & 3 & -5 & 0 \\
 & 1 & 1 & -1 & 2 & -3 \\
 & 1 & 1 & -1 & 2 & -3 & -3
\end{array}
$$

Carry 1 down; use the current carry times 1 to form the products 1, 1, -1, 2, -3; add columnwise to obtain 1, 1, -1, 2, -3, -3. The quotient is Q(x)=x^4 + x^3 - x^2 + 2x - 3 and the remainder is R=-3. Therefore the algebraic certificate is P(x)=(x-(1))(x^4 + x^3 - x^2 + 2x - 3)+(-3), and P(1)=-3 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(1) directly. A zero remainder establishes the factor x-(1); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

Read the row aloud as a recipe: start at 1, multiply by 1, add the next coefficient, and continue until the last column. The last number, -3, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.10 Coefficient-Order Auditing

Worked example 10 — coefficient-order auditing. The dividend is P(x)=-5x^3 + 5x - 3, and the proposed divisor is x-(2). The coefficient row, including any zeros, is -5, 0, 5, -3. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrr}
2 & -5 & 0 & 5 & -3 \\
 & -10 & -20 & -30 \\
 & -5 & -10 & -15 & -33
\end{array}
$$

Bring down -5. The successive products are -10, -20, -30, and adding them to the next coefficients gives the bottom row -5, -10, -15, -33. Therefore Q(x)=-5x^2 - 10x - 15 and R=-33; the remainder theorem identifies P(2)=-33. This is a 3-degree dividend, so the quotient degree is 2, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 2 gives -33. The complete identity is P(x)=(x-(2))(-5x^2 - 10x - 15)+(-33). When the result is used to test a root, the conclusion is conditional: 2 is a root only if this remainder is zero. Here the calculation reports -33, so the tableau does not certify a root unless that value is zero.

Read the row aloud as a recipe: start at -5, multiply by 2, add the next coefficient, and continue until the last column. The last number, -33, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.11 A Decimal Input

Worked example 11 — a decimal input. Consider P(x)=2x^4 - 6x^3 - x^2 - 4 and test r=-2. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^4 down to x^0; this makes clear that the first 4 bottom entries become coefficients of a polynomial of degree 3.

$$
\begin{array}{rrrrrr}
-2 & 2 & -6 & -1 & 0 & -4 \\
 & -4 & 20 & -38 & 76 \\
 & 2 & -10 & 19 & -38 & 72
\end{array}
$$

The multiply-and-add recurrence begins with 2. At each subsequent column it multiplies by -2, then adds the original coefficient. The product row is -4, 20, -38, 76; the resulting row is 2, -10, 19, -38, 72. Reading it by powers gives Q(x)=2x^3 - 10x^2 + 19x - 38, while the final scalar is R=72. Hence P(x)=(x-(-2))Q(x)+R.

Set x=-2 in the identity: the factor term vanishes and the equation reduces to P(-2)=72. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(-2). If the original divisor were described as x+2, its corresponding trial number would be negative.

Read the row aloud as a recipe: start at 2, multiply by -2, add the next coefficient, and continue until the last column. The last number, 72, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.12 Degree Reduction

Worked example 12 — degree reduction. A candidate computation uses P(x)=-4x^5 + x^4 + 6x^3 - 2x^2 + 3x - 5 at r=-1. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrrr}
-1 & -4 & 1 & 6 & -2 & 3 & -5 \\
 & 4 & -5 & -1 & 3 & -6 \\
 & -4 & 5 & 1 & -3 & 6 & -11
\end{array}
$$

Carry -4 down; use the current carry times -1 to form the products 4, -5, -1, 3, -6; add columnwise to obtain -4, 5, 1, -3, 6, -11. The quotient is Q(x)=-4x^4 + 5x^3 + x^2 - 3x + 6 and the remainder is R=-11. Therefore the algebraic certificate is P(x)=(x-(-1))(-4x^4 + 5x^3 + x^2 - 3x + 6)+(-11), and P(-1)=-11 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(-1) directly. A zero remainder establishes the factor x-(-1); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

Read the row aloud as a recipe: start at -4, multiply by -1, add the next coefficient, and continue until the last column. The last number, -11, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.13 Remainder Evaluation

Worked example 13 — remainder evaluation. The dividend is P(x)=3x^3 + 5, and the proposed divisor is x-(0). The coefficient row, including any zeros, is 3, 0, 0, 5. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrr}
0 & 3 & 0 & 0 & 5 \\
 & 0 & 0 & 0 \\
 & 3 & 0 & 0 & 5
\end{array}
$$

Bring down 3. The successive products are 0, 0, 0, and adding them to the next coefficients gives the bottom row 3, 0, 0, 5. Therefore Q(x)=3x^2 and R=5; the remainder theorem identifies P(0)=5. This is a 3-degree dividend, so the quotient degree is 2, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 0 gives 5. The complete identity is P(x)=(x-(0))(3x^2)+(5). When the result is used to test a root, the conclusion is conditional: 0 is a root only if this remainder is zero. Here the calculation reports 5, so the tableau does not certify a root unless that value is zero.

Read the row aloud as a recipe: start at 3, multiply by 0, add the next coefficient, and continue until the last column. The last number, 5, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.14 Quotient Reconstruction

Worked example 14 — quotient reconstruction. Consider P(x)=-3x^4 + 2x^3 - 6x^2 - x + 4 and test r=1. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^4 down to x^0; this makes clear that the first 4 bottom entries become coefficients of a polynomial of degree 3.

$$
\begin{array}{rrrrrr}
1 & -3 & 2 & -6 & -1 & 4 \\
 & -3 & -1 & -7 & -8 \\
 & -3 & -1 & -7 & -8 & -4
\end{array}
$$

The multiply-and-add recurrence begins with -3. At each subsequent column it multiplies by 1, then adds the original coefficient. The product row is -3, -1, -7, -8; the resulting row is -3, -1, -7, -8, -4. Reading it by powers gives Q(x)=-3x^3 - x^2 - 7x - 8, while the final scalar is R=-4. Hence P(x)=(x-(1))Q(x)+R.

Set x=1 in the identity: the factor term vanishes and the equation reduces to P(1)=-4. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(1). If the original divisor were described as x+1, its corresponding trial number would be negative.

Read the row aloud as a recipe: start at -3, multiply by 1, add the next coefficient, and continue until the last column. The last number, -4, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.15 A Missing-Power Alignment Check

Worked example 15 — a missing-power alignment check. A candidate computation uses P(x)=4x^5 - 4x^4 + x^3 + 6x^2 - 2x + 3 at r=2. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrrr}
2 & 4 & -4 & 1 & 6 & -2 & 3 \\
 & 8 & 8 & 18 & 48 & 92 \\
 & 4 & 4 & 9 & 24 & 46 & 95
\end{array}
$$

Carry 4 down; use the current carry times 2 to form the products 8, 8, 18, 48, 92; add columnwise to obtain 4, 4, 9, 24, 46, 95. The quotient is Q(x)=4x^4 + 4x^3 + 9x^2 + 24x + 46 and the remainder is R=95. Therefore the algebraic certificate is P(x)=(x-(2))(4x^4 + 4x^3 + 9x^2 + 24x + 46)+(95), and P(2)=95 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(2) directly. A zero remainder establishes the factor x-(2); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

Read the row aloud as a recipe: start at 4, multiply by 2, add the next coefficient, and continue until the last column. The last number, 95, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.16 Factor Certification

Worked example 16 — factor certification. The dividend is P(x)=-2x^3 + 3x^2, and the proposed divisor is x-(-2). The coefficient row, including any zeros, is -2, 3, 0, 0. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrr}
-2 & -2 & 3 & 0 & 0 \\
 & 4 & -14 & 28 \\
 & -2 & 7 & -14 & 28
\end{array}
$$

Bring down -2. The successive products are 4, -14, 28, and adding them to the next coefficients gives the bottom row -2, 7, -14, 28. Therefore Q(x)=-2x^2 + 7x - 14 and R=28; the remainder theorem identifies P(-2)=28. This is a 3-degree dividend, so the quotient degree is 2, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -2 gives 28. The complete identity is P(x)=(x-(-2))(-2x^2 + 7x - 14)+(28). When the result is used to test a root, the conclusion is conditional: -2 is a root only if this remainder is zero. Here the calculation reports 28, so the tableau does not certify a root unless that value is zero.

Read the row aloud as a recipe: start at -2, multiply by -2, add the next coefficient, and continue until the last column. The last number, 28, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.17 Nested Numerical Evaluation

Worked example 17 — nested numerical evaluation. Consider P(x)=5x^4 + 2x^2 - 6x - 1 and test r=-1. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^4 down to x^0; this makes clear that the first 4 bottom entries become coefficients of a polynomial of degree 3.

$$
\begin{array}{rrrrrr}
-1 & 5 & 0 & 2 & -6 & -1 \\
 & -5 & 5 & -7 & 13 \\
 & 5 & -5 & 7 & -13 & 12
\end{array}
$$

The multiply-and-add recurrence begins with 5. At each subsequent column it multiplies by -1, then adds the original coefficient. The product row is -5, 5, -7, 13; the resulting row is 5, -5, 7, -13, 12. Reading it by powers gives Q(x)=5x^3 - 5x^2 + 7x - 13, while the final scalar is R=12. Hence P(x)=(x-(-1))Q(x)+R.

Set x=-1 in the identity: the factor term vanishes and the equation reduces to P(-1)=12. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(-1). If the original divisor were described as x+1, its corresponding trial number would be negative.

Read the row aloud as a recipe: start at 5, multiply by -1, add the next coefficient, and continue until the last column. The last number, 12, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.18 Sign-Convention Practice

Worked example 18 — sign-convention practice. A candidate computation uses P(x)=-x^5 + 4x^4 - 4x^3 + x^2 + 6x - 2 at r=0. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrrr}
0 & -1 & 4 & -4 & 1 & 6 & -2 \\
 & 0 & 0 & 0 & 0 & 0 \\
 & -1 & 4 & -4 & 1 & 6 & -2
\end{array}
$$

Carry -1 down; use the current carry times 0 to form the products 0, 0, 0, 0, 0; add columnwise to obtain -1, 4, -4, 1, 6, -2. The quotient is Q(x)=-x^4 + 4x^3 - 4x^2 + x + 6 and the remainder is R=-2. Therefore the algebraic certificate is P(x)=(x-(0))(-x^4 + 4x^3 - 4x^2 + x + 6)+(-2), and P(0)=-2 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(0) directly. A zero remainder establishes the factor x-(0); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

Read the row aloud as a recipe: start at -1, multiply by 0, add the next coefficient, and continue until the last column. The last number, -2, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.19 A Root Candidate That Is Not A Root

Worked example 19 — a root candidate that is not a root. The dividend is P(x)=6x^3 - 2x^2 + 3x - 5, and the proposed divisor is x-(1). The coefficient row, including any zeros, is 6, -2, 3, -5. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrr}
1 & 6 & -2 & 3 & -5 \\
 & 6 & 4 & 7 \\
 & 6 & 4 & 7 & 2
\end{array}
$$

Bring down 6. The successive products are 6, 4, 7, and adding them to the next coefficients gives the bottom row 6, 4, 7, 2. Therefore Q(x)=6x^2 + 4x + 7 and R=2; the remainder theorem identifies P(1)=2. This is a 3-degree dividend, so the quotient degree is 2, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 1 gives 2. The complete identity is P(x)=(x-(1))(6x^2 + 4x + 7)+(2). When the result is used to test a root, the conclusion is conditional: 1 is a root only if this remainder is zero. Here the calculation reports 2, so the tableau does not certify a root unless that value is zero.

Read the row aloud as a recipe: start at 6, multiply by 1, add the next coefficient, and continue until the last column. The last number, 2, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.20 A Sparse Polynomial

Worked example 20 — a sparse polynomial. Consider P(x)=x^4 + 5x^3 - 3x^2 + 2x - 6 and test r=2. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^4 down to x^0; this makes clear that the first 4 bottom entries become coefficients of a polynomial of degree 3.

$$
\begin{array}{rrrrrr}
2 & 1 & 5 & -3 & 2 & -6 \\
 & 2 & 14 & 22 & 48 \\
 & 1 & 7 & 11 & 24 & 42
\end{array}
$$

The multiply-and-add recurrence begins with 1. At each subsequent column it multiplies by 2, then adds the original coefficient. The product row is 2, 14, 22, 48; the resulting row is 1, 7, 11, 24, 42. Reading it by powers gives Q(x)=x^3 + 7x^2 + 11x + 24, while the final scalar is R=42. Hence P(x)=(x-(2))Q(x)+R.

Set x=2 in the identity: the factor term vanishes and the equation reduces to P(2)=42. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(2). If the original divisor were described as x+2, its corresponding trial number would be negative.

Read the row aloud as a recipe: start at 1, multiply by 2, add the next coefficient, and continue until the last column. The last number, 42, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.21 Independent Substitution

Worked example 21 — independent substitution. A candidate computation uses P(x)=-6x^5 + 4x^3 - 4x^2 + 6 at r=-2. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrrr}
-2 & -6 & 0 & 4 & -4 & 0 & 6 \\
 & 12 & -24 & 40 & -72 & 144 \\
 & -6 & 12 & -20 & 36 & -72 & 150
\end{array}
$$

Carry -6 down; use the current carry times -2 to form the products 12, -24, 40, -72, 144; add columnwise to obtain -6, 12, -20, 36, -72, 150. The quotient is Q(x)=-6x^4 + 12x^3 - 20x^2 + 36x - 72 and the remainder is R=150. Therefore the algebraic certificate is P(x)=(x-(-2))(-6x^4 + 12x^3 - 20x^2 + 36x - 72)+(150), and P(-2)=150 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(-2) directly. A zero remainder establishes the factor x-(-2); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

Read the row aloud as a recipe: start at -6, multiply by -2, add the next coefficient, and continue until the last column. The last number, 150, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.22 Coefficient-Order Auditing

Worked example 22 — coefficient-order auditing. The dividend is P(x)=x^3 + 6x^2 - 2x + 3, and the proposed divisor is x-(-1). The coefficient row, including any zeros, is 1, 6, -2, 3. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrr}
-1 & 1 & 6 & -2 & 3 \\
 & -1 & -5 & 7 \\
 & 1 & 5 & -7 & 10
\end{array}
$$

Bring down 1. The successive products are -1, -5, 7, and adding them to the next coefficients gives the bottom row 1, 5, -7, 10. Therefore Q(x)=x^2 + 5x - 7 and R=10; the remainder theorem identifies P(-1)=10. This is a 3-degree dividend, so the quotient degree is 2, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -1 gives 10. The complete identity is P(x)=(x-(-1))(x^2 + 5x - 7)+(10). When the result is used to test a root, the conclusion is conditional: -1 is a root only if this remainder is zero. Here the calculation reports 10, so the tableau does not certify a root unless that value is zero.

Read the row aloud as a recipe: start at 1, multiply by -1, add the next coefficient, and continue until the last column. The last number, 10, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.23 A Decimal Input

Worked example 23 — a decimal input. Consider P(x)=-5x^4 + 5x^2 - 3x + 2 and test r=0. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^4 down to x^0; this makes clear that the first 4 bottom entries become coefficients of a polynomial of degree 3.

$$
\begin{array}{rrrrrr}
0 & -5 & 0 & 5 & -3 & 2 \\
 & 0 & 0 & 0 & 0 \\
 & -5 & 0 & 5 & -3 & 2
\end{array}
$$

The multiply-and-add recurrence begins with -5. At each subsequent column it multiplies by 0, then adds the original coefficient. The product row is 0, 0, 0, 0; the resulting row is -5, 0, 5, -3, 2. Reading it by powers gives Q(x)=-5x^3 + 5x - 3, while the final scalar is R=2. Hence P(x)=(x-(0))Q(x)+R.

Set x=0 in the identity: the factor term vanishes and the equation reduces to P(0)=2. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(0). If the original divisor were described as x+0, its corresponding trial number would be negative.

Read the row aloud as a recipe: start at -5, multiply by 0, add the next coefficient, and continue until the last column. The last number, 2, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.24 Degree Reduction

Worked example 24 — degree reduction. A candidate computation uses P(x)=2x^5 - 6x^4 - x^3 + 4x^2 - 4x + 1 at r=1. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrrr}
1 & 2 & -6 & -1 & 4 & -4 & 1 \\
 & 2 & -4 & -5 & -1 & -5 \\
 & 2 & -4 & -5 & -1 & -5 & -4
\end{array}
$$

Carry 2 down; use the current carry times 1 to form the products 2, -4, -5, -1, -5; add columnwise to obtain 2, -4, -5, -1, -5, -4. The quotient is Q(x)=2x^4 - 4x^3 - 5x^2 - x - 5 and the remainder is R=-4. Therefore the algebraic certificate is P(x)=(x-(1))(2x^4 - 4x^3 - 5x^2 - x - 5)+(-4), and P(1)=-4 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(1) directly. A zero remainder establishes the factor x-(1); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

Read the row aloud as a recipe: start at 2, multiply by 1, add the next coefficient, and continue until the last column. The last number, -4, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.25 Remainder Evaluation

Worked example 25 — remainder evaluation. The dividend is P(x)=-4x^3 + 6x - 2, and the proposed divisor is x-(2). The coefficient row, including any zeros, is -4, 0, 6, -2. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrr}
2 & -4 & 0 & 6 & -2 \\
 & -8 & -16 & -20 \\
 & -4 & -8 & -10 & -22
\end{array}
$$

Bring down -4. The successive products are -8, -16, -20, and adding them to the next coefficients gives the bottom row -4, -8, -10, -22. Therefore Q(x)=-4x^2 - 8x - 10 and R=-22; the remainder theorem identifies P(2)=-22. This is a 3-degree dividend, so the quotient degree is 2, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 2 gives -22. The complete identity is P(x)=(x-(2))(-4x^2 - 8x - 10)+(-22). When the result is used to test a root, the conclusion is conditional: 2 is a root only if this remainder is zero. Here the calculation reports -22, so the tableau does not certify a root unless that value is zero.

Read the row aloud as a recipe: start at -4, multiply by 2, add the next coefficient, and continue until the last column. The last number, -22, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.26 Quotient Reconstruction

Worked example 26 — quotient reconstruction. Consider P(x)=3x^4 - 5x^3 - 3 and test r=-2. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^4 down to x^0; this makes clear that the first 4 bottom entries become coefficients of a polynomial of degree 3.

$$
\begin{array}{rrrrrr}
-2 & 3 & -5 & 0 & 0 & -3 \\
 & -6 & 22 & -44 & 88 \\
 & 3 & -11 & 22 & -44 & 85
\end{array}
$$

The multiply-and-add recurrence begins with 3. At each subsequent column it multiplies by -2, then adds the original coefficient. The product row is -6, 22, -44, 88; the resulting row is 3, -11, 22, -44, 85. Reading it by powers gives Q(x)=3x^3 - 11x^2 + 22x - 44, while the final scalar is R=85. Hence P(x)=(x-(-2))Q(x)+R.

Set x=-2 in the identity: the factor term vanishes and the equation reduces to P(-2)=85. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(-2). If the original divisor were described as x+2, its corresponding trial number would be negative.

Read the row aloud as a recipe: start at 3, multiply by -2, add the next coefficient, and continue until the last column. The last number, 85, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.27 A Missing-Power Alignment Check

Worked example 27 — a missing-power alignment check. A candidate computation uses P(x)=-3x^5 + 2x^4 - 6x^3 - x^2 + 4x - 4 at r=-1. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrrr}
-1 & -3 & 2 & -6 & -1 & 4 & -4 \\
 & 3 & -5 & 11 & -10 & 6 \\
 & -3 & 5 & -11 & 10 & -6 & 2
\end{array}
$$

Carry -3 down; use the current carry times -1 to form the products 3, -5, 11, -10, 6; add columnwise to obtain -3, 5, -11, 10, -6, 2. The quotient is Q(x)=-3x^4 + 5x^3 - 11x^2 + 10x - 6 and the remainder is R=2. Therefore the algebraic certificate is P(x)=(x-(-1))(-3x^4 + 5x^3 - 11x^2 + 10x - 6)+(2), and P(-1)=2 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(-1) directly. A zero remainder establishes the factor x-(-1); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

Read the row aloud as a recipe: start at -3, multiply by -1, add the next coefficient, and continue until the last column. The last number, 2, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.28 Factor Certification

Worked example 28 — factor certification. The dividend is P(x)=4x^3 - 4x^2 + x + 6, and the proposed divisor is x-(0). The coefficient row, including any zeros, is 4, -4, 1, 6. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrr}
0 & 4 & -4 & 1 & 6 \\
 & 0 & 0 & 0 \\
 & 4 & -4 & 1 & 6
\end{array}
$$

Bring down 4. The successive products are 0, 0, 0, and adding them to the next coefficients gives the bottom row 4, -4, 1, 6. Therefore Q(x)=4x^2 - 4x + 1 and R=6; the remainder theorem identifies P(0)=6. This is a 3-degree dividend, so the quotient degree is 2, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 0 gives 6. The complete identity is P(x)=(x-(0))(4x^2 - 4x + 1)+(6). When the result is used to test a root, the conclusion is conditional: 0 is a root only if this remainder is zero. Here the calculation reports 6, so the tableau does not certify a root unless that value is zero.

Read the row aloud as a recipe: start at 4, multiply by 0, add the next coefficient, and continue until the last column. The last number, 6, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.29 Nested Numerical Evaluation

Worked example 29 — nested numerical evaluation. Consider P(x)=-2x^4 - 5x^2 + 5 and test r=1. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^4 down to x^0; this makes clear that the first 4 bottom entries become coefficients of a polynomial of degree 3.

$$
\begin{array}{rrrrrr}
1 & -2 & 0 & -5 & 0 & 5 \\
 & -2 & -2 & -7 & -7 \\
 & -2 & -2 & -7 & -7 & -2
\end{array}
$$

The multiply-and-add recurrence begins with -2. At each subsequent column it multiplies by 1, then adds the original coefficient. The product row is -2, -2, -7, -7; the resulting row is -2, -2, -7, -7, -2. Reading it by powers gives Q(x)=-2x^3 - 2x^2 - 7x - 7, while the final scalar is R=-2. Hence P(x)=(x-(1))Q(x)+R.

Set x=1 in the identity: the factor term vanishes and the equation reduces to P(1)=-2. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(1). If the original divisor were described as x+1, its corresponding trial number would be negative.

Read the row aloud as a recipe: start at -2, multiply by 1, add the next coefficient, and continue until the last column. The last number, -2, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.30 Sign-Convention Practice

Worked example 30 — sign-convention practice. A candidate computation uses P(x)=5x^5 - 3x^4 + 2x^3 - 6x^2 - x + 4 at r=2. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrrr}
2 & 5 & -3 & 2 & -6 & -1 & 4 \\
 & 10 & 14 & 32 & 52 & 102 \\
 & 5 & 7 & 16 & 26 & 51 & 106
\end{array}
$$

Carry 5 down; use the current carry times 2 to form the products 10, 14, 32, 52, 102; add columnwise to obtain 5, 7, 16, 26, 51, 106. The quotient is Q(x)=5x^4 + 7x^3 + 16x^2 + 26x + 51 and the remainder is R=106. Therefore the algebraic certificate is P(x)=(x-(2))(5x^4 + 7x^3 + 16x^2 + 26x + 51)+(106), and P(2)=106 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(2) directly. A zero remainder establishes the factor x-(2); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

Read the row aloud as a recipe: start at 5, multiply by 2, add the next coefficient, and continue until the last column. The last number, 106, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.31 A Root Candidate That Is Not A Root

Worked example 31 — a root candidate that is not a root. The dividend is P(x)=-x^3 + 4x^2 + 1, and the proposed divisor is x-(-2). The coefficient row, including any zeros, is -1, 4, 0, 1. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrr}
-2 & -1 & 4 & 0 & 1 \\
 & 2 & -12 & 24 \\
 & -1 & 6 & -12 & 25
\end{array}
$$

Bring down -1. The successive products are 2, -12, 24, and adding them to the next coefficients gives the bottom row -1, 6, -12, 25. Therefore Q(x)=-x^2 + 6x - 12 and R=25; the remainder theorem identifies P(-2)=25. This is a 3-degree dividend, so the quotient degree is 2, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at -2 gives 25. The complete identity is P(x)=(x-(-2))(-x^2 + 6x - 12)+(25). When the result is used to test a root, the conclusion is conditional: -2 is a root only if this remainder is zero. Here the calculation reports 25, so the tableau does not certify a root unless that value is zero.

Read the row aloud as a recipe: start at -1, multiply by -2, add the next coefficient, and continue until the last column. The last number, 25, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.32 A Sparse Polynomial

Worked example 32 — a sparse polynomial. Consider P(x)=6x^4 - 2x^3 + 3x^2 - 5x and test r=-1. The question asks for the division data, not just for a numerical value. Label the coefficients by powers from x^4 down to x^0; this makes clear that the first 4 bottom entries become coefficients of a polynomial of degree 3.

$$
\begin{array}{rrrrrr}
-1 & 6 & -2 & 3 & -5 & 0 \\
 & -6 & 8 & -11 & 16 \\
 & 6 & -8 & 11 & -16 & 16
\end{array}
$$

The multiply-and-add recurrence begins with 6. At each subsequent column it multiplies by -1, then adds the original coefficient. The product row is -6, 8, -11, 16; the resulting row is 6, -8, 11, -16, 16. Reading it by powers gives Q(x)=6x^3 - 8x^2 + 11x - 16, while the final scalar is R=16. Hence P(x)=(x-(-1))Q(x)+R.

Set x=-1 in the identity: the factor term vanishes and the equation reduces to P(-1)=16. Direct substitution is a separate arithmetic check; it gives the same value. The sign of the trial number is not altered because the divisor has explicitly been written as x-(-1). If the original divisor were described as x+1, its corresponding trial number would be negative.

Read the row aloud as a recipe: start at 6, multiply by -1, add the next coefficient, and continue until the last column. The last number, 16, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.33 Independent Substitution

Worked example 33 — independent substitution. A candidate computation uses P(x)=x^5 - 3x^3 + 2x^2 - 6x - 1 at r=0. Before interpreting its bottom row, ask what the final number means. The algorithm is polynomial division by x-r, so its output must satisfy an identity for every x, not only at the selected point.

$$
\begin{array}{rrrrrrr}
0 & 1 & 0 & -3 & 2 & -6 & -1 \\
 & 0 & 0 & 0 & 0 & 0 \\
 & 1 & 0 & -3 & 2 & -6 & -1
\end{array}
$$

Carry 1 down; use the current carry times 0 to form the products 0, 0, 0, 0, 0; add columnwise to obtain 1, 0, -3, 2, -6, -1. The quotient is Q(x)=x^4 - 3x^2 + 2x - 6 and the remainder is R=-1. Therefore the algebraic certificate is P(x)=(x-(0))(x^4 - 3x^2 + 2x - 6)+(-1), and P(0)=-1 follows without expanding.

To audit, expand the product and compare the coefficient of each power, including powers that were absent in P. Then evaluate P(0) directly. A zero remainder establishes the factor x-(0); a nonzero remainder refutes that specific factor but does not say that P has no other roots. This distinction is the practical meaning of the remainder theorem.

Read the row aloud as a recipe: start at 1, multiply by 0, add the next coefficient, and continue until the last column. The last number, -1, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

### 4.34 Coefficient-Order Auditing

Worked example 34 — coefficient-order auditing. The dividend is P(x)=-6x^3 - x^2 + 4x - 4, and the proposed divisor is x-(1). The coefficient row, including any zeros, is -6, -1, 4, -4. This setup is deliberately written before the arithmetic: it prevents the common mistake of guessing the row from the visual spacing of the printed polynomial.

$$
\begin{array}{rrrrr}
1 & -6 & -1 & 4 & -4 \\
 & -6 & -7 & -3 \\
 & -6 & -7 & -3 & -7
\end{array}
$$

Bring down -6. The successive products are -6, -7, -3, and adding them to the next coefficients gives the bottom row -6, -7, -3, -7. Therefore Q(x)=-6x^2 - 7x - 3 and R=-7; the remainder theorem identifies P(1)=-7. This is a 3-degree dividend, so the quotient degree is 2, exactly as the division algorithm requires.

Independent check: direct Horner evaluation at 1 gives -7. The complete identity is P(x)=(x-(1))(-6x^2 - 7x - 3)+(-7). When the result is used to test a root, the conclusion is conditional: 1 is a root only if this remainder is zero. Here the calculation reports -7, so the tableau does not certify a root unless that value is zero.

Read the row aloud as a recipe: start at -6, multiply by 1, add the next coefficient, and continue until the last column. The last number, -7, is the leftover amount. This verbal description is useful for catching a skipped column before doing any more algebra.

## 5. Mathematical Extensions, Limits, and Common Errors — Revision, numerical interpretation, and source checks

For revision, keep four labels separate: dividend P, divisor x-r, quotient Q, and remainder R. The remainder equals P(r); a zero remainder means x-r is a factor. Insert zeros for missing powers, preserve descending order, and check by substitution. Nested form is repeated multiply-and-add, not a different polynomial.

Common errors include using -r instead of r for divisor x-r, treating the last bottom entry as a quotient coefficient, omitting a zero coefficient, and claiming a root from equal endpoint signs. A sign change guarantees a root for a continuous polynomial; no sign change does not rule one out. The source’s numerical examples should be recalculated rather than copied blindly.