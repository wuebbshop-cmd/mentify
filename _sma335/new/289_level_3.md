## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What the examiner is testing

Every question on this topic reduces to four separable skills, and the marks are distributed among them in a stable pattern. The first skill is recognition: deciding whether an equation is homogeneous, whether it is linear, and whether its coefficients are constant. The second is translation: writing the characteristic equation with the signs copied exactly from the differential equation. The third is classification: deciding from the discriminant whether the roots are real distinct, real repeated, or a conjugate pair, and writing the matching general solution. The fourth is the initial value problem: imposing two conditions and solving a two-by-two system for the constants.

The object around which everything is organised is

$$
a_0\frac{d^{2}y}{dx^{2}}+a_1\frac{dy}{dx}+a_2y=0 ,
$$

with $a_0\neq 0$ and $a_0$, $a_1$, $a_2$ constants. Its characteristic equation is

$$
a_0m^{2}+a_1m+a_2=0 ,
$$

and the three possible answers are

$$
y=c_1e^{m_1x}+c_2e^{m_2x} \quad \left(m_1\neq m_2\right),
$$

$$
y=\left(c_1+c_2x\right)e^{mx} \quad \left(m \text{ repeated}\right),
$$

$$
y=e^{ax}\left(c_1\cos bx+c_2\sin bx\right) \quad \left(m=a\pm ib\right).
$$

Those four displayed objects, used correctly, are worth almost every mark in the topic. Sections 2 and 3 supply the statements and the derivations that the bookwork parts of a paper test; Section 4 gives complete model solutions with the marks shown step by step; Section 5 gives the trap table, the revision checklist and the timing plan.

### 1.2 The high-yield results and their mark values

The table lists the results examined directly, with the marks typically attached in a first-year course. The values are indicative, but the relative weighting is stable: derivations and complete solutions carry more than statements, and the characteristic equation itself is usually a single mark.

| Result | Statement | Typical marks |
| --- | --- | --- |
| Definition of homogeneity | Every term of first degree in $y$; no forcing term | 1 to 2 |
| Three tests for linearity | First powers, coefficients in $x$ only, no products | 2 |
| Characteristic equation | $a_0m^{2}+a_1m+a_2=0$ | 1 |
| Exact roots | Factorise, or quadratic formula with exact surds | 2 |
| Case classification | Sign of $\Delta=a_1^{2}-4a_0a_2$ | 1 |
| General solution, distinct | $y=c_1e^{m_1x}+c_2e^{m_2x}$ | 2 |
| General solution, repeated | $y=\left(c_1+c_2x\right)e^{mx}$ | 2 |
| General solution, complex | $y=e^{ax}\left(c_1\cos bx+c_2\sin bx\right)$ | 2 to 3 |
| Initial conditions | Two equations, two constants | 2 to 3 |
| Wronskian test | $W=y_1y_2'-y_2y_1'\neq 0$ | 2 |
| Bookwork: the $xe^{mx}$ device | Full reduction-of-order derivation | 4 to 6 |
| Higher order | Factorise, apply multiplicity rules | 3 to 5 |
| Verification | Substitute back and simplify to zero | 1 to 2 |

Two conclusions follow. First, the characteristic equation and the case classification are cheap marks that must never be lost, because they occupy the first two lines of any solution. Second, the reduction-of-order derivation is the single most heavily weighted piece of bookwork, so it must be reproducible from memory, including the two identities $a_0m^{2}+a_1m+a_2=0$ and $2a_0m+a_1=0$ that make the calculation collapse.

### 1.3 The six question shapes

The questions asked on this topic fall into six shapes, and each shape has a fixed opening move.

Shape one asks for a classification: given an equation, state whether it is homogeneous or non-homogeneous, linear or non-linear, and with constant or variable coefficients. The opening move is to check the three linearity conditions and then look at the right-hand side.

Shape two asks for the characteristic equation only, perhaps as the first part of a longer question. The opening move is to write the quadratic immediately, with signs copied, and to quote the discriminant.

Shape three asks for the general solution. The opening move is to solve the quadratic exactly and then classify. This shape carries marks for the roots, the classification, and the assembled answer.

Shape four adds two initial conditions. The opening move is to complete the general solution first, then differentiate it once, then impose both conditions. Attempting the conditions before the general solution is finished is the most common source of wasted time.

Shape five asks for a higher-order solution, usually third order and usually with integer roots. The opening move is to find one root by testing $m=1$, $m=-1$, $m=2$, and then divide out the factor.

Shape six is bookwork: derive the characteristic equation from the trial $y=e^{mx}$, or prove that the repeated-root case needs $xe^{mx}$, or show that a stated pair of solutions is independent. The opening move is to write the substitution clearly and to display every differentiation, because the marks are awarded for the visible steps rather than for the conclusion.

### 1.4 The definition and its three failure modes

> **Definition.** The equation $a_0\frac{d^{2}y}{dx^{2}}+a_1\frac{dy}{dx}+a_2y=0$ with $a_0\neq 0$ and constant coefficients is a second-order homogeneous linear equation with constant coefficients.

Non-homogeneity is the presence of a forcing term. The equation

$$
2\frac{d^{2}y}{dx^{2}}+5\frac{dy}{dx}-6y=xe^{x}
$$

is non-homogeneous, and so is

$$
\frac{d^{2}y}{dx^{2}}-3\frac{dy}{dx}+7y=\sin x+x^{2} ,
$$

whereas

$$
\frac{d^{2}y}{dx^{2}}-3\frac{dy}{dx}+7y=0
$$

is homogeneous.

Non-linearity fails one of three conditions, and a classification question usually offers one example of each. A derivative raised to a power fails the first condition, as in

$$
3\frac{d^{2}y}{dx^{2}}-2\left(\frac{dy}{dx}\right)^{2}+8y=\ln x .
$$

A coefficient containing $y$ fails the second condition, as in

$$
5x\frac{d^{3}y}{dx^{3}}+8xy\frac{d^{2}y}{dx^{2}}-9\frac{dy}{dx}+xy=xe^{x} ,
$$

where the second derivative is multiplied by $y$. A right-hand side containing $y$ fails the second condition on the forcing term, as in

$$
5\frac{d^{2}y}{dx^{2}}-8x\frac{dy}{dx}+2y=xy ,
$$

which may equally be seen as producing a coefficient of $y$ depending on $y$ once the term is moved to the left.

A fourth, frequently missed failure is a non-linear function of the unknown, as in $\frac{d^{2}y}{dx^{2}}+\sin y=0$. The word linear describes the unknown and its derivatives, not the coefficients of the independent variable.

### 1.5 The characteristic equation and the discriminant

Replace the second derivative with $m^{2}$, the first derivative with $m$, and the function with one. For

$$
\frac{d^{2}y}{dx^{2}}-5\frac{dy}{dx}+6y=0
$$

this gives

$$
m^{2}-5m+6=0 .
$$

The discriminant

$$
\Delta=a_1^{2}-4a_0a_2
$$

decides the case before any root is computed, and writing it down is a cheap mark. For the example above, $\Delta=25-24=1>0$, so the roots are real and distinct, and factoring gives $m=2$ and $m=3$.

Two identities give a free check on any pair of roots. The sum of the roots is $-\frac{a_1}{a_0}$ and the product is $\frac{a_2}{a_0}$. For the example the sum must be $5$ and the product $6$, and the pair $2$, $3$ satisfies both.

### 1.6 The three cases at a glance

| Sign of $\Delta$ | Roots | General solution | Constants |
| --- | --- | --- | --- |
| $\Delta>0$ | real, distinct $m_1$, $m_2$ | $y=c_1e^{m_1x}+c_2e^{m_2x}$ | 2 |
| $\Delta=0$ | real, repeated $m$ | $y=\left(c_1+c_2x\right)e^{mx}$ | 2 |
| $\Delta<0$ | $a\pm ib$ with $b\neq 0$ | $y=e^{ax}\left(c_1\cos bx+c_2\sin bx\right)$ | 2 |

The table is the whole answer to the computational part of the topic. What varies between questions is only the arithmetic that produces $m_1$, $m_2$ or $a\pm ib$.

### 1.7 What a full-mark answer contains

A full-mark answer has six visible elements. It writes the characteristic equation with the signs copied from the differential equation. It records the discriminant, or states the factorisation that makes the roots evident. It names the case in words, for example "the roots are real and equal". It writes the general solution with the correct structure and both constants. It applies each initial condition in a separate displayed line, so that the marker can see both equations. It finishes with an explicit statement of the particular solution and a substitution check.

Presentation matters more here than in most topics, because the mark scheme is written against these six elements. A correct answer written as an unbroken paragraph loses marks even when the mathematics is right.

### 1.8 The vocabulary that earns marks

Three sentences recur in mark schemes and should be used deliberately. "The characteristic equation is $m^{2}+\dots=0$, whose discriminant is $\Delta=\dots$" establishes the translation. "The roots are real and distinct, so the general solution is $y=\dots$" establishes the classification. "Applying $y(0)=\dots$ gives one equation, and applying $y'(0)=\dots$ gives the second" establishes the initial value work.

A fourth sentence is needed for independence questions: "The Wronskian is $W=\dots$, which is non-zero, so the solutions are linearly independent and the general solution is complete."

Writing these sentences, rather than only performing the algebra, is what allows a marker to award the method marks that the algebra alone does not earn.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Statement and proof of superposition

> **Theorem.** If $L$ is a linear operator with constant coefficients and $L[y_1]=L[y_2]=0$, then $L[c_1y_1+c_2y_2]=0$ for all constants $c_1$, $c_2$.

Proof. Because differentiation is linear, $D^{k}\left(c_1y_1+c_2y_2\right)=c_1D^{k}y_1+c_2D^{k}y_2$ for $k=0,1,2$. Multiplying by $a_{2-k}$ and summing gives

$$
L\left[c_1y_1+c_2y_2\right]=c_1L[y_1]+c_2L[y_2]=0 .
$$

This completes the proof.

The examiner's use of this theorem is to justify writing a blend rather than a single function, and to justify verifying only the basic solutions instead of the whole general solution. Both economies are legitimate consequences of the theorem, and quoting it earns the mark that a bare assertion does not.

### 2.2 The three-case theorem

> **Theorem.** Let $a_0\frac{d^{2}y}{dx^{2}}+a_1\frac{dy}{dx}+a_2y=0$ with $a_0\neq 0$ and real constant coefficients, and let $m_1$, $m_2$ be the roots of $a_0m^{2}+a_1m+a_2=0$.
>
> If $m_1\neq m_2$ are real, every solution is $y=c_1e^{m_1x}+c_2e^{m_2x}$.
>
> If $m_1=m_2=m$ is real, every solution is $y=\left(c_1+c_2x\right)e^{mx}$.
>
> If $m_1=a+ib$, $m_2=a-ib$ with $b\neq 0$, every solution is $y=e^{ax}\left(c_1\cos bx+c_2\sin bx\right)$.

The word every is the part that carries the marks in a proof question. It asserts that no solution has been lost, and it is justified by the dimension argument of Section 2.3 together with the independence proofs of Section 3.

### 2.3 Two dimensions, two constants

> **Theorem.** If $p$, $q$ are continuous on an interval $I$, the solution space of $y''+py'+qy=0$ on $I$ is two-dimensional.

Proof. For each pair $\left(y_0,y_1\right)$ and each $x_0$ in $I$ there is exactly one solution with $y(x_0)=y_0$ and $y'(x_0)=y_1$. The evaluation map $y\mapsto\left(y(x_0),y'(x_0)\right)$ is linear, injective by uniqueness and surjective by existence, hence an isomorphism onto $\mathbb{R}^{2}$. This completes the proof.

The practical consequence is the counting rule that the examiner tests constantly: a second-order equation has exactly two arbitrary constants, a third-order equation exactly three, and an answer with the wrong count is wrong regardless of how plausible the functions look.

### 2.4 Independence and the Wronskian

> **Theorem.** Two solutions $y_1$, $y_2$ of $y''+py'+qy=0$ on $I$ are linearly independent if and only if their Wronskian $W=y_1y_2'-y_2y_1'$ is non-zero at some point of $I$.

The three computations below are the ones that appear in examinations, and they should be memorised as results rather than rederived.

| Fundamental set | Wronskian | Non-zero because |
| --- | --- | --- |
| $e^{m_1x}$, $e^{m_2x}$ | $\left(m_2-m_1\right)e^{\left(m_1+m_2\right)x}$ | $m_1\neq m_2$ |
| $e^{mx}$, $xe^{mx}$ | $e^{2mx}$ | exponential never vanishes |
| $e^{ax}\cos bx$, $e^{ax}\sin bx$ | $be^{2ax}$ | $b\neq 0$ |

Each row is a two-line computation. For the first,

$$
W=e^{m_1x}\cdot m_2e^{m_2x}-e^{m_2x}\cdot m_1e^{m_1x}=\left(m_2-m_1\right)e^{\left(m_1+m_2\right)x} .
$$

For the second,

$$
W=e^{mx}\left(e^{mx}+mxe^{mx}\right)-xe^{mx}\cdot me^{mx}=e^{2mx} ,
$$

where the two terms containing $x$ cancel. For the third,

$$
W=e^{2ax}\left[\cos bx\left(a\sin bx+b\cos bx\right)-\sin bx\left(a\cos bx-b\sin bx\right)\right]=be^{2ax} .
$$

### 2.5 Abel's identity and why the Wronskian cannot vanish once

> **Lemma.** For solutions of $y''+py'+qy=0$, $W(x)=W(x_0)\exp\left(-\int_{x_0}^{x}p\,dt\right)$.

Proof. Since $y_1''=-py_1'-qy_1$ and $y_2''=-py_2'-qy_2$,

$$
W'=y_1y_2''-y_2y_1''=-p\left(y_1y_2'-y_2y_1'\right)=-pW ,
$$

so $W$ solves a first-order linear equation whose solution is the stated exponential. This completes the proof.

The lemma is what makes the Wronskian test decisive from a single point: for a pair of solutions the Wronskian is a never-vanishing exponential multiple, so testing one convenient value of $x$ settles the whole interval. For constant coefficients $p=-\frac{a_1}{a_0}$, and the Wronskian is a multiple of $e^{a_1x/a_0}$.

### 2.6 Reduction of order

> **Theorem.** If $y_1$ is a non-zero solution of $y''+py'+qy=0$ on $I$, a second independent solution is
>
> $$
> y_2=y_1\int\frac{\exp\left(-\int p\,dx\right)}{y_1^{2}}\,dx .
> $$

Proof. Put $y=vy_1$. Then $y'=v'y_1+vy_1'$ and $y''=v''y_1+2v'y_1'+vy_1''$. Substituting and using $y_1''+py_1'+qy_1=0$ gives

$$
v''y_1+\left(2y_1'+py_1\right)v'=0 .
$$

Writing $u=v'$ gives the separable equation $u'+\left(\frac{2y_1'}{y_1}+p\right)u=0$, whose solution is

$$
u=\frac{\exp\left(-\int p\,dx\right)}{y_1^{2}} ,
$$

and one integration produces $y_2$. This completes the proof.

For a repeated root the coefficients satisfy $p=-2m$, so the integrand is $e^{2mx}/e^{2mx}=1$ and the integral is $x$. This is the shortest route to the $xe^{mx}$ device, and it is the route that examiners expect when the question says "obtain a second independent solution".

### 2.7 The multiplicity rules for higher order

> **Theorem.** For $a_0y^{(n)}+\cdots+a_ny=0$ with constant real coefficients, a real root $m$ of multiplicity $k$ contributes $e^{mx}$, $xe^{mx}$, …, $x^{k-1}e^{mx}$, and a conjugate pair $a\pm ib$ of multiplicity $k$ contributes $x^{j}e^{ax}\cos bx$ and $x^{j}e^{ax}\sin bx$ for $j=0,\dots,k-1$. The functions collected number $n$ and are independent.

The counting clause is the examinable part. A fourth-order equation whose characteristic polynomial is $\left(m-1\right)^{2}\left(m^{2}+1\right)$ must produce exactly four functions, and a candidate who produces three has lost one.

### 2.8 Initial value problems

> **Theorem.** If $p$, $q$ are continuous on an interval containing $x_0$, the problem $y''+py'+qy=0$ with $y(x_0)=A$ and $y'(x_0)=B$ has exactly one solution there.

In matrix form the constants satisfy

$$
\begin{aligned}
c_1y_1(x_0)+c_2y_2(x_0) &= A ,\\
c_1y_1'(x_0)+c_2y_2'(x_0) &= B ,
\end{aligned}
$$

whose determinant is $W(x_0)$, non-zero for a fundamental set. The system therefore has exactly one solution, which is why two conditions always suffice and never overdetermine the problem.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 The derivation examiners ask for

> **Derivation.** Obtain the characteristic equation of $a_0\frac{d^{2}y}{dx^{2}}+a_1\frac{dy}{dx}+a_2y=0$ by seeking exponential solutions.

Step 1. Seek a solution of the form

$$
y=e^{mx}
$$

with $m$ a constant to be determined. The motivation is that derivatives of an exponential are constant multiples of the same exponential, so substitution cannot change the shape of the function.

Step 2. Differentiate twice.

$$
\frac{dy}{dx}=me^{mx}, \qquad \frac{d^{2}y}{dx^{2}}=m^{2}e^{mx} .
$$

Step 3. Substitute into the equation.

$$
a_0m^{2}e^{mx}+a_1me^{mx}+a_2e^{mx}=0
$$

Step 4. Factor out the exponential.

$$
\left(a_0m^{2}+a_1m+a_2\right)e^{mx}=0
$$

Step 5. Since $e^{mx}\neq 0$, divide by it.

$$
a_0m^{2}+a_1m+a_2=0
$$

Step 6. Conclude. This is the characteristic equation, and $y=e^{mx}$ solves the differential equation exactly when $m$ solves it. This is worth the full bookwork allocation, provided every step is displayed.

### 3.2 The repeated-root derivation

> **Derivation.** Show that when the characteristic equation has a repeated root $m$, the function $xe^{mx}$ is also a solution.

Step 1. Record the two consequences of a repeated root, namely that $m$ is a root and that $m$ is a root of the derivative of the characteristic polynomial.

$$
a_0m^{2}+a_1m+a_2=0, \qquad 2a_0m+a_1=0
$$

Step 2. Put $y=ve^{mx}$ with $v$ an unknown function of $x$. This is the standard substitution for a second solution, and it keeps the known exponential factor.

Step 3. Differentiate once.

$$
\frac{dy}{dx}=e^{mx}\left(v'+mv\right)
$$

Step 4. Differentiate again.

$$
\frac{d^{2}y}{dx^{2}}=e^{mx}\left(v''+2mv'+m^{2}v\right)
$$

Step 5. Substitute into the differential equation and factor out $e^{mx}$.

$$
a_0\left(v''+2mv'+m^{2}v\right)+a_1\left(v'+mv\right)+a_2v=0
$$

Step 6. Collect the terms in $v''$, in $v'$ and in $v$.

$$
a_0v''+\left(2a_0m+a_1\right)v'+v\left(a_0m^{2}+a_1m+a_2\right)=0
$$

Step 7. Use the two identities from Step 1 to delete the last two terms.

$$
a_0v''=0
$$

Step 8. Since $a_0\neq 0$, $v''=0$, so two integrations give $v=c_2x+c_1$.

Step 9. Write the solution.

$$
y=\left(c_1+c_2x\right)e^{mx}
$$

Step 10. Confirm independence by the Wronskian, which equals $e^{2mx}$ and never vanishes. The device $xe^{mx}$ is therefore not an inspired guess but a consequence of the repeated root.

### 3.3 The complex case and the appearance of sine and cosine

Step 1. With roots $a+ib$ and $a-ib$, write the two formal exponentials.

$$
e^{\left(a+ib\right)x}=e^{ax}e^{ibx}, \qquad e^{\left(a-ib\right)x}=e^{ax}e^{-ibx}
$$

Step 2. Combine them with arbitrary constants.

$$
y=e^{ax}\left(c_1e^{ibx}+c_2e^{-ibx}\right)
$$

Step 3. Apply Euler's formulas.

$$
e^{ibx}=\cos bx+i\sin bx, \qquad e^{-ibx}=\cos bx-i\sin bx
$$

Step 4. Collect cosine and sine.

$$
y=e^{ax}\left[\left(c_1+c_2\right)\cos bx+i\left(c_1-c_2\right)\sin bx\right]
$$

Step 5. Rename the two combinations as fresh arbitrary constants.

$$
y=e^{ax}\left(A\cos bx+B\sin bx\right)
$$

Step 6. Conclude with the reading rule: the real part of the root becomes the exponential rate, and the imaginary part becomes the angular frequency. Confusing the two is the most expensive error in the topic.

### 3.4 Method for the distinct-real case, with marking points

1. Write the characteristic equation. One mark.
2. Factorise or apply the quadratic formula, keeping surds exact. Two marks.
3. State that the roots are real and distinct. One mark.
4. Write the general solution with both exponentials and two constants. Two marks.
5. Check the sum and product of the roots against the coefficients. No marks, but it catches slips.

### 3.5 Method for the repeated case, with marking points

1. Write the characteristic equation. One mark.
2. Show that the discriminant is zero, or exhibit a perfect square. One mark.
3. State the repeated root and its multiplicity. One mark.
4. Write the solution with the factor $\left(c_1+c_2x\right)$ and the exponential outside. Two marks, of which the factor of $x$ is usually one on its own.
5. If independence is asked for, compute the Wronskian as $e^{2mx}$. Two marks.

### 3.6 Method for the complex case, with marking points

1. Write the characteristic equation. One mark.
2. Compute the discriminant and state that it is negative. One mark.
3. Apply the quadratic formula and split the result into real and imaginary parts. Two marks.
4. Write the answer with an exponential factor and a cosine and sine of the correct frequency. Two to three marks.
5. Verify by substituting the cosine solution back. One mark.

### 3.7 Method for an initial value problem, with marking points

1. Solve the homogeneous equation completely. Marks as above.
2. Differentiate the general solution and display the derivative. One mark.
3. Substitute $x=x_0$ into the function and equate to $y_0$. One mark.
4. Substitute $x=x_0$ into the derivative and equate to $y_1$. One mark.
5. Solve the two-by-two system and display both constants. One mark.
6. State the particular solution with the constants inserted. One mark.
7. Verify both conditions numerically, and substitute back into the differential equation. One mark.

The order matters. Differentiating before the general solution is complete is the single largest time-waster in the topic, because the derivative then has to be recomputed once the constants change.

### 3.8 Method for higher order, with marking points

1. Write the characteristic equation of degree $n$. One mark.
2. Find one root by testing small integers. One to two marks.
3. Divide out the corresponding factor and display the quotient. Two marks.
4. Factorise the quotient completely. One mark.
5. Apply the multiplicity rules, counting the functions produced. Two marks.
6. Check the count against the order. No marks, but a wrong count is always wrong.

### 3.9 The ninety-second reverse check

At the end of any solution, read the answer backwards. From the exponential factors, recover the roots; from the trigonometric frequency, recover the imaginary part; from any factor of $x$, recover the multiplicity. Then compare with the coefficients through the sum and product identities.

For example, an answer $y=e^{-2x}\left(c_1\cos 5x+c_2\sin 5x\right)$ claims roots $-2\pm 5i$, hence a characteristic polynomial $m^{2}+4m+29$, hence an equation $y''+4y'+29y=0$. If that is not the equation in the question, the answer is wrong, and the discrepancy is usually a sign or a frequency. The check costs under a minute and detects almost every error.

## 4. Representative Worked Examples and Solutions

The model solutions below are written in the form expected in an examination, with numbered steps and the marks shown for each step. The marks add to a realistic total for each question.

### 4.1 Problem: distinct real roots with an initial value problem

Solve $y''-y'-12y=0$ subject to $y(0)=3$ and $y'(0)=5$.

### 4.2 Solution: characteristic equation, roots, constants, check

Step 1. Write the characteristic equation, copying the signs. [1 mark]

$$
m^{2}-m-12=0
$$

Step 2. Factorise, seeking two numbers with product $-12$ and sum $-1$. [2 marks]

$$
\left(m-4\right)\left(m+3\right)=0
$$

Step 3. State the roots and classify them. [1 mark]

$$
m_1=4, \qquad m_2=-3 \quad \text{(real and distinct)}
$$

Step 4. Write the general solution. [2 marks]

$$
y=c_1e^{4x}+c_2e^{-3x}
$$

Step 5. Impose $y(0)=3$. [1 mark]

$$
c_1+c_2=3
$$

Step 6. Differentiate the general solution. [1 mark]

$$
y'=4c_1e^{4x}-3c_2e^{-3x}
$$

Step 7. Impose $y'(0)=5$. [1 mark]

$$
4c_1-3c_2=5
$$

Step 8. Solve the pair of equations by elimination. [1 mark]

$$
4c_1+4c_2=12 \quad \text{and} \quad 4c_1-3c_2=5 \quad \text{give} \quad 7c_2=7 ,
$$

$$
c_2=1, \qquad c_1=2 .
$$

Step 9. State the particular solution. [1 mark]

$$
y=2e^{4x}+e^{-3x}
$$

Step 10. Verify both conditions. [1 mark]

$$
y(0)=2+1=3, \qquad y'(0)=8-3=5 .
$$

Step 11. Verify the differential equation for each basic solution.

$$
16-4-12=0, \qquad 9+3-12=0
$$

Both vanish, so the answer is correct.

### 4.3 Problem: repeated root with an initial value problem

Solve $4y''+4y'+y=0$ subject to $y(0)=1$ and $y'(0)=0$.

### 4.4 Solution: perfect square, factor of $x$, constants, check

Step 1. Write the characteristic equation. [1 mark]

$$
4m^{2}+4m+1=0
$$

Step 2. Compute the discriminant. [1 mark]

$$
\Delta=16-16=0
$$

Step 3. Factorise as a perfect square and state the repeated root. [1 mark]

$$
\left(2m+1\right)^{2}=0, \qquad m=-\frac{1}{2} \quad \text{(twice)}
$$

Step 4. Write the general solution with the factor $\left(c_1+c_2x\right)$. [2 marks]

$$
y=\left(c_1+c_2x\right)e^{-x/2}
$$

Step 5. Impose $y(0)=1$. [1 mark]

$$
c_1=1
$$

Step 6. Differentiate, using the product rule. [1 mark]

$$
y'=-\frac{1}{2}\left(c_1+c_2x\right)e^{-x/2}+c_2e^{-x/2}
$$

Step 7. Impose $y'(0)=0$. [1 mark]

$$
0=-\frac{1}{2}c_1+c_2 \qquad \text{so} \qquad c_2=\frac{1}{2}
$$

Step 8. State the particular solution. [1 mark]

$$
y=\left(1+\frac{1}{2}x\right)e^{-x/2}
$$

Step 9. Verify the conditions.

$$
y(0)=1, \qquad y'(0)=-\frac{1}{2}+\frac{1}{2}=0 .
$$

Step 10. Verify the equation for the repeated-root member. Take $y=xe^{-x/2}$, whose derivatives are

$$
y'=e^{-x/2}-\frac{1}{2}xe^{-x/2}, \qquad y''=-\frac{1}{2}e^{-x/2}-\frac{1}{2}e^{-x/2}+\frac{1}{4}xe^{-x/2} .
$$

Step 11. Substitute and collect the constant part and the $x$-dependent part.

$$
4\left(-1\right)+4\left(1\right)+1\left(0\right)=0, \qquad 4\left(\frac{1}{4}\right)+4\left(-\frac{1}{2}\right)+1\left(1\right)=1-2+1=0 .
$$

Both parts vanish, so the repeated-root structure is correct.

### 4.5 Problem: conjugate complex roots with an initial value problem

Solve $y''-6y'+25y=0$ subject to $y(0)=-3$ and $y'(0)=-1$.

### 4.6 Solution: negative discriminant, real and imaginary parts, constants, check

Step 1. Write the characteristic equation. [1 mark]

$$
m^{2}-6m+25=0
$$

Step 2. Compute the discriminant and note its sign. [1 mark]

$$
\Delta=36-100=-64<0
$$

Step 3. Apply the quadratic formula, writing $\sqrt{-64}=8i$. [2 marks]

$$
m=\frac{6\pm 8i}{2}=3\pm 4i
$$

Step 4. Identify the real part and the imaginary part. [1 mark]

$$
a=3, \qquad b=4
$$

Step 5. Write the general solution. [2 marks]

$$
y=e^{3x}\left(c_1\cos 4x+c_2\sin 4x\right)
$$

Step 6. Impose $y(0)=-3$. [1 mark]

$$
c_1=-3
$$

Step 7. Differentiate, remembering that the product rule produces two groups of terms. [1 mark]

$$
y'=e^{3x}\left[3\left(c_1\cos 4x+c_2\sin 4x\right)-4c_1\sin 4x+4c_2\cos 4x\right]
$$

Step 8. Impose $y'(0)=-1$. [1 mark]

$$
-1=3c_1+4c_2
$$

Step 9. Substitute $c_1=-3$ and solve. [1 mark]

$$
-1=-9+4c_2 \qquad \text{so} \qquad 4c_2=8 \qquad \text{and} \qquad c_2=2
$$

Step 10. State the particular solution. [1 mark]

$$
y=e^{3x}\left(-3\cos 4x+2\sin 4x\right)
$$

Step 11. Verify both conditions directly.

$$
y(0)=-3, \qquad y'(0)=3\left(-3\right)+4\left(2\right)=-9+8=-1 .
$$

Step 12. Check the differential equation for $y=e^{3x}\cos 4x$, whose second derivative is

$$
y''=e^{3x}\left(\left(9-16\right)\cos 4x-24\sin 4x\right)=e^{3x}\left(-7\cos 4x-24\sin 4x\right) .
$$

Step 13. Substitute into the left-hand side and collect cosine and sine coefficients.

$$
-7-6\cdot 3+25=0, \qquad -24-6\cdot\left(-4\right)+0=0
$$

Both vanish, so the fundamental set is correct and the particular solution follows. Note that the frequency four came from the imaginary part of the root and the rate three from the real part; reversing the two would produce $\cos 3x$ and $\sin 3x$, and the checks in this step would fail.

### 4.7 Problem: fourth order with a repeated complex pair

Solve $\left(D^{2}+2D+5\right)^{2}y=0$.

### 4.8 Solution: solve the repeated quadratic, then apply the multiplicity rule

Step 1. Write the characteristic equation, treating the squared operator as a repeated quadratic factor. [1 mark]

$$
\left(m^{2}+2m+5\right)^{2}=0
$$

Step 2. Solve the quadratic factor. [2 marks]

$$
m^{2}+2m+5=0, \qquad m=\frac{-2\pm\sqrt{4-20}}{2}=-1\pm 2i
$$

Step 3. Note that each root occurs twice, so the pair $\left(-1\pm 2i\right)$ has multiplicity two. [1 mark]

Step 4. Write the general solution, with a factor of $x$ accompanying the second copy of each trigonometric term. [3 marks]

$$
y=e^{-x}\left[\left(c_1+c_2x\right)\cos 2x+\left(c_3+c_4x\right)\sin 2x\right]
$$

Step 5. Check the count: four constants for an equation of order four. [1 mark]

Step 6. Verify that $y=e^{-x}\cos 2x$ solves the first-order operator equation. Its derivatives are

$$
y'=e^{-x}\left(-\cos 2x-2\sin 2x\right), \qquad y''=e^{-x}\left(-3\cos 2x+4\sin 2x\right) .
$$

Step 7. Assemble $y''+2y'+5y$ and simplify.

$$
e^{-x}\left[\left(-3-2+5\right)\cos 2x+\left(4-4\right)\sin 2x\right]=0
$$

Step 8. Compute the action of $D^{2}+2D+5$ on the extra member $y=xe^{-x}\cos 2x$. Since the operator annihilates $e^{-x}\cos 2x$, the product rule leaves

$$
\left(D^{2}+2D+5\right)\left[xf\right]=x\left(D^{2}+2D+5\right)f+2f'+2f
$$

where $f=e^{-x}\cos 2x$. The first term is zero.

Step 9. Evaluate the remainder, using $f'=e^{-x}\left(-\cos 2x-2\sin 2x\right)$.

$$
2f'+2f=2e^{-x}\left(-\cos 2x-2\sin 2x\right)+2e^{-x}\cos 2x=-4e^{-x}\sin 2x
$$

Step 10. Apply the operator once more. Since $e^{-x}\sin 2x$ also lies in the null space of the operator, the result is zero.

$$
\left(D^{2}+2D+5\right)\left(-4e^{-x}\sin 2x\right)=-4\cdot 0=0
$$

The factor of $x$ is therefore required, and the general solution is complete.

### 4.9 Problem: third order with three distinct roots

Solve $y'''-6y''+11y'-6y=0$.

### 4.10 Solution: inspect for a root, divide, then count

Step 1. Write the characteristic equation. [1 mark]

$$
m^{3}-6m^{2}+11m-6=0
$$

Step 2. Test $m=1$, since the coefficients sum to zero. [1 mark]

$$
1-6+11-6=0
$$

Step 3. Divide out the factor $m-1$ and display the quotient. [2 marks]

$$
m^{3}-6m^{2}+11m-6=\left(m-1\right)\left(m^{2}-5m+6\right)
$$

Step 4. Factorise the quadratic. [1 mark]

$$
m^{2}-5m+6=\left(m-2\right)\left(m-3\right)
$$

Step 5. State all three roots. [1 mark]

$$
m=1, \qquad m=2, \qquad m=3
$$

Step 6. Write the general solution with three constants. [2 marks]

$$
y=c_1e^{x}+c_2e^{2x}+c_3e^{3x}
$$

Step 7. Check the count against the order. [1 mark]

Step 8. Verify by substitution for the root three.

$$
27-6\cdot 9+11\cdot 3-6=27-54+33-6=0
$$

The check succeeds.

### 4.11 Problem: an equation with a purely imaginary pair

Solve $\left(D^{3}+4D\right)y=0$.

### 4.12 Solution: factor out $D$ first

Step 1. Write the characteristic equation. [1 mark]

$$
m^{3}+4m=0
$$

Step 2. Factor out $m$. [1 mark]

$$
m\left(m^{2}+4\right)=0
$$

Step 3. Read the roots: zero from the linear factor, and a pair from the quadratic. [2 marks]

$$
m=0, \qquad m=\pm 2i
$$

Step 4. Write the solution, translating the zero root into a constant and the pair into a cosine and a sine with no exponential factor. [3 marks]

$$
y=c_1+c_2\cos 2x+c_3\sin 2x
$$

Step 5. Check the count: three constants for an equation of order three. [1 mark]

Step 6. Verify the constant solution, for which the first and third derivatives vanish.

$$
D^{3}\left(c_1\right)+4D\left(c_1\right)=0+0=0
$$

Step 7. Verify the cosine term properly. For $y=\cos 2x$,

$$
y'=-2\sin 2x, \qquad y''=-4\cos 2x, \qquad y'''=8\sin 2x ,
$$

so

$$
y'''+4y'=8\sin 2x-8\sin 2x=0 .
$$

The check succeeds.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The trap table

The table below lists the errors that actually cost marks, together with the symptom that reveals them and the repair. Reading it once before an examination is worth more than re-reading the worked examples.

| Trap | How it appears | Symptom that reveals it | Repair |
| --- | --- | --- | --- |
| Sign copied wrongly | $m^{2}+5m+6=0$ from $y''-5y'+6y=0$ | Roots of the wrong sign | Sum of roots must equal $-\frac{a_1}{a_0}$ |
| Repeated root treated as distinct | $y=c_1e^{mx}+c_2e^{mx}$ | Only one constant survives | Use $\left(c_1+c_2x\right)e^{mx}$ |
| Real part and imaginary part swapped | $\cos 2x$ for roots $3\pm 4i$ | Frequency does not match the root | Frequency is the imaginary part |
| Non-zero exponential for a purely imaginary pair | $e^{0x}$ written as $e^{x}$ | Spurious growth factor | A zero real part gives no exponential |
| Constant placed in the exponent | $e^{mx+C}$ used as a basic solution | Two constants inside one term | Constants multiply the basic solutions |
| Constants determined from one condition twice | Same equation solved twice | Impossible or underdetermined system | Use $y$ and $y'$ separately |
| Derivative of a product mis-expanded | Missing $e^{ax}$ factor in $y'$ | Verification fails at $x=0$ | Differentiate with the product rule explicitly |
| Quadratic formula sign slip | $m=\frac{-b\pm\sqrt{\Delta}}{2}$ written with $+b$ | Roots fail the sum test | Check $m_1+m_2=-\frac{a_1}{a_0}$ |
| Surd rounded | $2.414$ instead of $2+\sqrt{2}$ | Answer cannot be verified exactly | Keep surds exact |
| Wrong number of constants | Three constants for a second-order equation | Count mismatch | Count the roots, not the terms |
| Higher-order factor dropped | Cubic quoted with two roots | Count below the order | Divide out and factorise fully |
| Homogeneity ignored | Particular solution added when none is needed | Extra term with no counterpart | Check the right-hand side first |

Three traps deserve expansion because they recur every year. The sign trap is caught instantly by the sum identity, which costs one line. The repeated-root trap is caught by counting: two equal exponentials form one function, so the answer carries only one constant and is visibly incomplete. The real-and-imaginary trap is caught by the reverse check of Section 3.9, which recovers the roots from the answer and compares them with the coefficients.

### 5.2 Extension: the homogeneous answer inside a non-homogeneous question

The results of this topic are the first half of every non-homogeneous question. For

$$
y''-5y'+6y=e^{x}
$$

the characteristic roots are two and three, so the complementary function is

$$
y_h=c_1e^{2x}+c_2e^{3x} .
$$

A particular solution is found by trying $y=ke^{x}$, which gives $k-5k+6k=2k$, so $k=\frac{1}{2}$ and the general solution is

$$
y=c_1e^{2x}+c_2e^{3x}+\frac{1}{2}e^{x} .
$$

The rule that matters for this topic is the resonance rule: if the forcing term duplicates a member of the complementary function, the trial must be multiplied by $x$. For $y''-5y'+6y=e^{2x}$ the trial $ke^{2x}$ fails, and the correct trial is $kxe^{2x}$, exactly because two is a repeated occurrence of a complementary-function rate. The same device that repairs the repeated characteristic root repairs the resonant forcing term, and for the same reason.

### 5.3 Extension: the physical reading of the three cases

The three cases describe three behaviours, and a question that asks for an interpretation is answered by naming the behaviour.

Real distinct roots of the same sign give a non-oscillating response; the root closer to zero dominates eventually. Real roots of opposite sign give an unstable response, since one mode grows without bound. A repeated root gives the borderline response, in which the amplitude grows linearly as well as exponentially. A conjugate pair with negative real part gives a decaying oscillation, with the real part controlling the decay and the imaginary part controlling the frequency; a purely imaginary pair gives oscillation of constant amplitude, which is simple harmonic motion.

That last reading explains why $y''+\omega^{2}y=0$ has the solution $A\cos\omega x+B\sin\omega x$. The characteristic roots are $\pm i\omega$, the imaginary part is the angular frequency, and the period is $\frac{2\pi}{\omega}$.

### 5.4 Extension: changing the independent variable

Some variable-coefficient equations become constant-coefficient after a change of variable, and then the method of this topic applies unchanged. The standard instance is the equation

$$
x^{2}\frac{d^{2}y}{dx^{2}}+ax\frac{dy}{dx}+by=0 ,
$$

for which the substitution $x=e^{t}$ converts the equation into one with constant coefficients in the variable $t$. The conversion is not part of this topic, but the recognition is: an equation whose coefficient of the second derivative is $x^{2}$ and whose coefficient of the first derivative is a multiple of $x$ is a candidate for this treatment, not for the characteristic equation directly.

### 5.5 Limit of the method

The characteristic equation exists because the coefficients are constants. With a single factor of $x$ in a coefficient the trial $y=e^{mx}$ leaves a factor that depends on $x$ and cannot vanish identically, and the reduction to a polynomial collapses. An examiner who asks "why does the method fail here" is testing exactly that observation, and the answer is that the common factor $e^{mx}$ no longer reduces to a constant polynomial.

The method also says nothing about non-homogeneous equations beyond supplying the complementary function, and nothing about non-linear equations at all, since superposition is unavailable there and the operator $L$ does not exist.

### 5.6 Revision checklist

Work through the following list and tick each item only when it can be done without notes.

1. State the definition of a second-order homogeneous linear equation with constant coefficients, including the condition $a_0\neq 0$.
2. Give one example each of a homogeneous and a non-homogeneous second-order equation.
3. State the three conditions for linearity and give one non-linear example failing each.
4. Write a given equation in operator notation, in the forms $5D^{2}y-3Dy+8y=0$ and $\left(5D^{2}-3D+8\right)y=0$.
5. Derive the characteristic equation from $y=e^{mx}$, displaying every substitution.
6. Prove that a repeated root produces $xe^{mx}$, by the substitution $y=ve^{mx}$.
7. State the three-case theorem with the exact form of each general solution.
8. Compute the Wronskian in each of the three cases and state why it is non-zero.
9. Solve an initial value problem of each of the three types, including the differentiation step.
10. Solve a third-order equation by inspection and division, and a fourth-order equation with a repeated quadratic factor.
11. Apply the multiplicity rules for a repeated root of higher order.
12. Perform the ninety-second reverse check on any answer.

### 5.7 Time strategy in the examination

A question of this type is usually worth between eight and fifteen marks, and the work divides predictably.

The first minute should be spent writing the characteristic equation and its discriminant. These are certain marks and they anchor the rest of the answer.

The next two or three minutes go on the roots. Factorising is faster than the quadratic formula when the roots are rational, and the sum and product check should be done immediately, because it costs ten seconds and prevents the most common error.

The next two minutes produce the general solution and the classification sentence. Writing "the roots are real and equal, so the general solution is …" earns the method marks that a bare formula may not.

If initial conditions are given, allow four minutes: one to differentiate, one to substitute both conditions, one to solve the pair, one to state and verify. The differentiation should be written with the product rule displayed, because a marker awards the step marks for visible structure.

If a derivation is asked for, allow five or six minutes and display every line of the substitution. Derivations are marked line by line, and a compressed derivation loses most of the marks even when the conclusion is right.

Finally, reserve one minute for the reverse check and for confirming that the number of constants equals the order. In a timed paper that minute is the difference between a correct answer and a correct answer that has lost its final mark to a misplaced sign.

### 5.8 Consolidated summary

A second-order homogeneous linear equation with constant coefficients is translated into the characteristic equation $a_0m^{2}+a_1m+a_2=0$ by the trial $y=e^{mx}$, and the discriminant decides which of three answers applies. Distinct real roots give two exponentials. A repeated root gives an exponential times a linear factor, a device forced by reduction of order rather than chosen. A conjugate pair gives an exponential times a cosine and a sine, with the real part as rate and the imaginary part as frequency.

The solution space is two-dimensional, so two independent solutions always span it and two conditions always determine the constants. Independence is certified by a non-zero Wronskian, which in the three cases equals $\left(m_2-m_1\right)e^{\left(m_1+m_2\right)x}$, $e^{2mx}$ and $be^{2ax}$ respectively.

For higher order the same rules apply with multiplicity: each extra repetition of a root adds one power of $x$. The count of arbitrary constants must equal the order, and the reverse check — recovering the roots from the answer and comparing their sum and product with the coefficients — is the fastest available defence against error.
