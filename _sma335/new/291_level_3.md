## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What the examiner is testing

Every question on this topic is one of six patterns, and identifying the pattern in the first thirty seconds is worth more than any formula. The patterns are: an exponential forcing away from resonance; an exponential forcing at resonance; a trigonometric forcing, with or without a surviving first derivative; a trigonometric forcing at resonance; a polynomial forcing, with or without a vanishing constant term; and a product forcing, either an exponential times a function or the variable times a function. A seventh pattern is a sum of the above, which is nothing more than several of the first six added.

The opening move is always the same: write the equation in the form $f(D)y=Q$, collect $f(D)$ as a polynomial, and note the constant term $f(0)$. The closing move is always the same: add the particular integral to the complementary function and substitute the particular integral back to confirm the coefficients. Between those two moves the work is arithmetic, and the arithmetic is where marks are lost.

The single most useful sentence in the whole topic is this: the shape of the particular integral is dictated by the shape of $Q$, and only when $Q$ already satisfies the homogeneous equation does the shape move one family further out, multiplied by $x$. Everything else is bookkeeping.

### 1.2 The symbols you will write

The operator $D$ means differentiate once with respect to $x$, so $Dy=\frac{dy}{dx}$ and $D^{2}y=\frac{d^{2}y}{dx^{2}}$. A polynomial in $D$ with constant coefficients is written $f(D)$, and its constant term is $f(0)$, which is the coefficient of $y$ in the original equation. The derivative of that polynomial with respect to the symbol $D$ is written $f'(D)$; for $f(D)=D^{2}-3D+2$ it is $2D-3$.

The particular integral is written $y_{p}$ and the complementary function $y_{c}$, and the general solution is $y=y_{c}+y_{p}$. The order of the equation equals the number of arbitrary constants in $y_{c}$, and the particular integral never contributes a constant.

Two numbers recur and should be computed before any algebra. The first is $f(a)$, obtained by putting the rate of an exponential into the polynomial. The second is the collapsed value obtained by replacing $D^{2}$ by $-a^{2}$ in a polynomial, which for $f(D)=D^{2}+3D-10$ at rate two gives the operator $3D-14$, and after clearing gives the number $-232$. When either computation returns zero, the forcing is resonant and the $x$ multiplier is required.

### 1.3 The architecture of a full answer

A complete answer to "solve" has four parts, and each earns marks separately.

The complementary function, with the roots of the auxiliary equation displayed and the correct number of constants: usually two marks.

The particular integral, with the rule identified and the condition tested before the rule is applied: usually two or three marks.

The assembled general solution: one mark.

The verification, or the application of initial conditions if any are given: one or two marks.

An answer that produces only the particular integral scores at most half. An answer that produces only the complementary function scores nothing for this topic. An answer whose particular integral is not checked is exposed to the most common single error in the subject, which is the sign in the wave rule.

### 1.4 The inverse operator in examination language

The symbol $\frac{Q}{f(D)}$ means a function which $f(D)$ sends to $Q$. It is defined only up to a solution of the homogeneous equation, so any two correct particular integrals differ by a complementary function. This has an examination consequence that is worth stating plainly: a printed answer is not the standard of correctness. The standard is substitution. If your particular integral is turned into $Q$ by $f(D)$, it is right, whatever a memorandum says.

The inverse operator is manipulated by three legal moves only. Constants factor out. Sums split. And the five rules below evaluate it on the five families. Anything else, in particular treating $\frac{1}{f(D)}$ as an ordinary fraction and cancelling symbols across it, is invalid.

### 1.5 Resonance stated once, properly

> **Definition (Resonance).** The forcing $Q$ is resonant with $f(D)$ when $Q$ solves the homogeneous equation $f(D)Q=0$.

For an exponential $e^{ax}$ this is the condition $f(a)=0$. For a wave of rate $a$ it is the condition $f\left(-a^{2}\right)=0$, equivalently that $\pm ia$ are roots of $f$. For a polynomial it is the condition $f(0)=0$, which means the forcing contains a constant and the constant solves the homogeneous equation.

The remedy has a definite size. If the resonance has depth $r$, meaning the relevant root has multiplicity $r$, the particular integral is multiplied by $x^{r}$ and divided by the $r$-th derivative of the polynomial evaluated at the root. The depth is read from the factorisation, never guessed.

### 1.6 What verification means for marks

Verification is not a re-reading of the working. It is a substitution, performed in a fixed order: differentiate the particular integral as many times as the order of the equation requires; form the combination prescribed by the coefficients; collect the coefficients of the independent pieces; confirm that each matches the forcing and that any piece absent from the forcing has coefficient zero.

Three errors survive every other check and are caught only by substitution: the sign in the collapse $D^{2}\to-a^{2}$, a missing factor of $x$ in a resonant case, and a missing correction term in the multiplier rule. A student who substitutes loses no marks on any of them, because the substitution detects all three.

### 1.7 The standard shapes of the answers

It helps to know in advance what the answer will look like, because a shape that looks wrong usually is wrong.

For an exponential forcing the particular integral is a multiple of the same exponential. For a wave forcing it is a combination of the sine and the cosine of the same argument, and it is a pure multiple of the forcing when the polynomial has no odd part. For a polynomial forcing of degree $n$ the particular integral is a polynomial of degree $n$, generally with every lower power present. For an exponential times a polynomial the particular integral is the same exponential times a polynomial of the same degree. For the variable times a function the particular integral is $x$ times the reply for the function, plus a lower-order correction. And in any resonant case an extra factor of $x$ appears, with the depth of the resonance as its exponent.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Result R1: the exponential rule, two marks

> **R1.** If $Q=e^{ax}$ and $f(a)\neq 0$, then $y_{p}=\frac{e^{ax}}{f(a)}$.

The mark is for evaluating $f$ at the exponent's rate and dividing. The check on the hypothesis is worth writing explicitly, because a zero result changes the whole method. Typical instance: for $f(D)=D^{2}-5D+6$ and $a=4$ the value is two, so $y_{p}=\frac{e^{4x}}{2}$.

The underlying identity is $f(D)e^{ax}=f(a)e^{ax}$, which is the statement that an exponential is an eigenfunction of every constant-coefficient operator.

### 2.2 Result R2: the exponential at resonance, three marks

> **R2.** If $a$ is a root of $f$ of multiplicity $r$, then $y_{p}=\frac{x^{r}e^{ax}}{f^{(r)}(a)}$.

For a simple root this is $y_{p}=\frac{xe^{ax}}{f'(a)}$; for a double root it is $y_{p}=\frac{x^{2}e^{ax}}{f''(a)}$. There is no additional factorial, since $f^{(r)}(a)$ already contains $r!$. The marks are for the exponent of $x$, for the correct derivative, and for the division.

The instance to memorise: for $\left(D^{2}-5D+6\right)y=e^{3x}$ the root three is simple and $f'(3)=1$, so $y_{p}=xe^{3x}$. For $\left(D-2\right)^{2}y=4e^{2x}$ the root is double and $f''(2)=2$, so $y_{p}=2x^{2}e^{2x}$.

### 2.3 Result R3: the wave rule, two marks

> **R3.** If $Q=\sin(ax+b)$ or $\cos(ax+b)$ and the polynomial has no odd part, and if $f\left(-a^{2}\right)\neq 0$, then $y_{p}=\frac{Q}{f\left(-a^{2}\right)}$, the value being computed by replacing $D^{2}$ by $-a^{2}$.

The sign is the whole result. Two differentiations of a wave of rate $a$ multiply it by $-a^{2}$, because $\left(ia\right)^{2}=-a^{2}$. Typical instance: for $\left(D^{2}+9\right)y=\sin 5x$ the collapse gives $-25+9=-16$, so $y_{p}=-\frac{\sin 5x}{16}$.

### 2.4 Result R4: a wave with a surviving first derivative, three marks

> **R4.** With $A$ and $B$ the collapsed even and odd parts of $f$ at $-a^{2}$, and $A^{2}+B^{2}a^{2}\neq 0$,

$$
y_{p}=\frac{\left(A-BD\right)Q}{A^{2}+B^{2}a^{2}} .
$$

The marks are for collapsing only the even powers, for clearing the surviving derivative correctly, and for the sign of the denominator. Typical instance: for $\left(D^{2}+3D-10\right)y=\sin 2x$ the collapse gives $A=-14$ and $B=3$, so $A^{2}+B^{2}a^{2}=196+36=232$ and $y_{p}=-\frac{7\sin 2x}{116}-\frac{3\cos 2x}{116}$.

The routine that always works is to multiply above and below by the companion $A-BD$, replace the resulting $D^{2}$ by $-a^{2}$, and simplify.

### 2.5 Result R5: a wave at resonance, three marks

> **R5.** If $f\left(-a^{2}\right)=0$ with multiplicity $r$ in the factor $D^{2}+a^{2}$, then the particular integral is $x^{r}$ times the reply for the same wave under $f^{(r)}(D)$ collapsed at $-a^{2}$.

For the usual simple case this reads $y_{p}=x\frac{Q}{f'(D)}$ with $D^{2}$ replaced by $-a^{2}$ afterwards. The marks are for recognising the resonance, for the factor of $x$, and for the division by the derivative rather than by the original polynomial.

Typical instance: for $\left(D^{2}+4\right)y=\cos 2x$ the collapse gives zero, $f'(D)=2D$, and $y_{p}=\frac{x\sin 2x}{4}$.

### 2.6 Result R6: the polynomial rule, four marks

> **R6.** If $Q=x^{n}$ and $f(0)\neq 0$, expand $\frac{1}{f(D)}$ in ascending powers of $D$ and apply the truncation up to $D^{n}$.

The marks are for factoring out the constant term correctly, for the expansion reaching the $n$-th power, for applying each derivative to $x^{n}$, and for the final simplification. Typical instance: for $\left(2D^{2}+2D+3\right)y=x^{2}$,

$$
y_{p}=\frac{x^{2}}{3}-\frac{4x}{9}-\frac{4}{27} .
$$

### 2.7 Result R7: the polynomial rule when $f(0)=0$, three marks

> **R7.** If $f(D)=D^{s}g(D)$ with $g(0)\neq 0$, compute $\frac{x^{n}}{g(D)}$ by R6 and then integrate $s$ times.

Typical instance: for $\left(D^{2}-D\right)y=x$ the factorisation gives $D\left(D-1\right)$, the inner quotient is $-\left(x+1\right)$, and one integration gives $y_{p}=-\frac{x^{2}}{2}-x$.

### 2.8 Result R8: the exponential shift, two marks

> **R8.** $\frac{e^{ax}u}{f(D)}=e^{ax}\frac{u}{f(D+a)}$.

The marks are for shifting every occurrence of $D$ by $+a$ and for then applying the appropriate rule to $u$ under the shifted polynomial. Typical instance: for $\left(D-4\right)y=x^{2}e^{3x}$ the shift gives $D+3-4=D-1$, the residual quotient is $-\left(x^{2}+2x+2\right)$, and $y_{p}=-e^{3x}\left(x^{2}+2x+2\right)$.

### 2.9 Result R9: the multiplier rule, four marks

> **R9.** $\frac{xu}{f(D)}=x\frac{u}{f(D)}-\frac{f'(D)}{\left[f(D)\right]^{2}}u$.

The marks are for both terms, for squaring the operator in the denominator, and for using $f'(D)$ rather than $f(D)$ in the numerator. Typical instance: for $\left(D^{2}-1\right)y=xe^{3x}$ the two terms are $\frac{xe^{3x}}{8}$ and $\frac{3e^{3x}}{32}$, so $y_{p}=\frac{xe^{3x}}{8}-\frac{3e^{3x}}{32}$.

When $u$ is an exponential, the shift rule R8 applied to $u=x$ gives the same answer by a different route, and doing both is a cheap self-check.

### 2.10 Result R10: superposition, one mark

> **R10.** A particular integral of a sum is the sum of the particular integrals of the parts.

The mark is for splitting a composite forcing before applying any rule, and for not attempting to treat two shapes with one shifted polynomial.

### 2.11 The one-line justifications

Each result has a one-line proof that is worth being able to reproduce, since a "state and prove" question is common.

For R1, $D^{k}e^{ax}=a^{k}e^{ax}$, so $f(D)e^{ax}=f(a)e^{ax}$. For R2, apply $f(D)$ to $e^{ax}\frac{x^{r}}{r!\,g(a)}$ where $f=(D-a)^{r}g$; the shift identity $\left(D-a\right)\left[e^{ax}w\right]=e^{ax}Dw$ reduces the verification to $D^{r}\frac{x^{r}}{r!}=1$. For R3 and R4, $D^{2}$ acts on a wave of rate $a$ as multiplication by $-a^{2}$, and the surviving first-order operator is cleared by its companion. For R6, the binomial series terminates because $D^{k}x^{n}=0$ for $k>n$. For R8, induction on $k$ in $D^{k}\left[e^{ax}u\right]=e^{ax}\left(D+a\right)^{k}u$. For R9, Leibniz's rule in the form $D^{k}\left[xu\right]=xD^{k}u+kD^{k-1}u$, summed against the coefficients.

### 2.12 Two shortcuts worth carrying

Two derived formulas save time in the examination hall and are safe because each is a special case of a stated rule.

The first is the second-order resonant exponential, $\frac{e^{ax}}{\left(D-a\right)^{2}}=\frac{x^{2}e^{ax}}{2}$. It is the case $f(D)=\left(D-a\right)^{2}$ of R2, and it is the formula behind every example in which the auxiliary equation has a repeated root equal to the exponent's rate. Written with a coefficient, $\frac{e^{ax}}{\left(D-a\right)^{2}}=\frac{x^{2}e^{ax}}{2}$ multiplied by whatever constant stands in front of the exponential.

The second is the reciprocal of a single linear factor, which is cleared rather than integrated: $\frac{Q}{D-\alpha}=\frac{\left(D+\alpha\right)Q}{D^{2}-\alpha^{2}}$, and the denominator becomes the real number $-\alpha^{2}-a^{2}$ once the wave's rate is inserted. For the machine $D-2$ and the wave $\sin x$ this gives $\frac{\cos x+2\sin x}{-1-4}$, which is $-\frac{\cos x+2\sin x}{5}$, a value that reappears in the multiplier-rule question of Section 4.

A third shortcut is structural rather than numerical: whenever the forcing is a product, ask whether the shift rule converts it into a problem of a shape already handled. If $u$ is a polynomial, the shifted problem is a polynomial problem; if $u$ is a wave, the shifted problem is a wave problem. Only when both fail is the two-term multiplier rule necessary.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 The decision table

The table is the fastest route from the forcing to the rule. Read the first column, test the condition in the second, and apply the third; if the condition fails, use the fourth.

| Form of $Q$ | Test to perform | Particular integral | If the test fails |
| --- | --- | --- | --- |
| $e^{ax}$ | compute $f(a)$ | $e^{ax}$ divided by $f(a)$ | $x^{r}e^{ax}$ divided by $f^{(r)}(a)$ |
| $\sin(ax+b)$ or $\cos(ax+b)$ | replace $D^{2}$ by $-a^{2}$ | apply R3 or R4 to the collapsed operator | $x$ times the reply under $f'(D)$ |
| $x^{n}$ | check $f(0)\neq 0$ | ascending expansion truncated at $D^{n}$ | divide out $D^{s}$ and integrate $s$ times |
| $e^{ax}u$ | none | $e^{ax}$ times the reply for $u$ under $f(D+a)$ | then apply this table to $u$ |
| $xu$ | none | $x$ times the reply for $u$ minus the correction | resolve any resonance in $u$ first |

Two reading rules for the table. The third column is applied to the collapsed operator, not to the original polynomial, whenever a wave is involved. And the fourth column is entered only after the second column has returned zero; multiplying by $x$ when the test succeeds is a definite error.

### 3.2 Sign discipline in the wave rule

The collapse is $D^{2}\to-a^{2}$, and the reason is one line of differentiation:

$$
D^{2}\sin(ax+b)=-a^{2}\sin(ax+b) .
$$

Three numeric probes catch a slip immediately, and they take five seconds each.

Probe one: for $D^{2}+9$ at rate two the collapse gives $-4+9=5$, a positive number, so the reply keeps the sign of the forcing. A positive collapse of $+4+9=13$ would give $\frac{\sin 2x}{13}$, which fails substitution by a factor.

Probe two: for $D^{2}+1$ at rate two the collapse gives $-4+1=-3$, so the reply is $-\frac{\sin 2x}{3}$. Substituting, $-4$ times the reply plus one times the reply is $-3$ times the reply, which is the forcing.

Probe three: for $D^{2}+4$ at rate two the collapse gives zero, which is the signal for resonance, not a number to divide by.

### 3.3 The working routine and its time budget

Step 1, thirty seconds: write $f(D)$, evaluate $f(0)$, factor if the factors are obvious.

Step 2, one minute: write the complementary function and count the constants against the order.

Step 3, thirty seconds: identify the shape of $Q$ and split a sum into its pieces.

Step 4, two minutes: perform the test in the second column of the table.

Step 5, two to three minutes: apply the rule, showing the substitution of the numbers before simplifying.

Step 6, one minute: assemble and verify by substitution.

For a ten-mark question the whole routine should take eight minutes, leaving two for the check. The temptation to skip the check is what converts an eight out of ten into a five.

### 3.4 The verification routine

Verification has its own fixed order, and following it prevents self-deception.

Differentiate the particular integral once per order of the equation, displaying each derivative separately. Form the combination prescribed by the coefficients. Collect the coefficients of the independent pieces, naming them, for example the coefficient of $e^{3x}$ and the coefficient of $xe^{3x}$. Confirm that each coefficient matches the forcing exactly, including the pieces whose coefficient should be zero.

In a resonant case the piece multiplied by $x$ must vanish from the result; if it does not, the exponent of $x$ is wrong. In a wave case the wrong sign in the collapse shows up as a coefficient of the opposite sign, which is why the sine and cosine coefficients must both be reported.

### 3.5 Compressed derivations of the five rules

The exponential rule. Since $D^{k}e^{ax}=a^{k}e^{ax}$, the polynomial acts as the number $f(a)$, so dividing by that number inverts the operator.

The repeated-root rule. Write $f=(D-a)^{r}g$ with $g(a)\neq 0$ and use $\left(D-a\right)\left[e^{ax}w\right]=e^{ax}Dw$ to reduce the verification to $D^{r}\frac{x^{r}}{r!}=1$, noting $f^{(r)}(a)=r!\,g(a)$.

The wave rule. Since $D^{2}$ acts as $-a^{2}$ on a wave of rate $a$, split $f$ into its even and odd parts, collapse both at $-a^{2}$, and clear the surviving first-order operator by multiplying by its companion, whose product with it becomes the real number $A^{2}+B^{2}a^{2}$ under the same collapse.

The polynomial rule. Factor out $f(0)$ and expand $\left(1+U\right)^{-1}=1-U+U^{2}-\cdots$ where $U$ raises the derivative order by at least one; the series terminates on $x^{n}$ after the $n$-th term because $D^{n+1}x^{n}=0$.

The shift and multiplier rules. Both follow from product identities: $D\left[e^{ax}u\right]=e^{ax}\left(D+a\right)u$ iterated, and $D^{k}\left[xu\right]=xD^{k}u+kD^{k-1}u$ summed with weights.

### 3.6 Combining several shapes

When $Q$ is a sum, split it and treat each piece independently, then add. Two rules keep this safe.

First, the split is by shape, not by factor: the sum $e^{3x}+x^{2}$ needs the exponential rule and the polynomial rule, applied separately. Second, each piece must be tested for resonance on its own, since $e^{3x}$ may be resonant while $x^{2}$ is not. A worked instance of exactly this kind is the last model solution in Section 4.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: an exponential forcing at resonance

Solve $\left(D^{2}-5D+6\right)y=e^{3x}$.

### 4.2 Solution: model solution with marking points

Step 1 (one mark). Write the auxiliary equation and factor it.

$$
m^{2}-5m+6=0, \qquad \left(m-3\right)\left(m-2\right)=0, \qquad m=3,\ 2
$$

Step 2 (one mark). Write the complementary function, with two constants because the order is two.

$$
y_{c}=c_{1}e^{3x}+c_{2}e^{2x}
$$

Step 3 (one mark). Test the exponent's rate in the polynomial and report the failure.

$$
f(3)=9-15+6=0
$$

Step 4 (one mark). State that the resonance has depth one, since $D-2$ does not vanish at three.

Step 5 (one mark). Compute the derivative of the polynomial and evaluate it.

$$
f'(D)=2D-5, \qquad f'(3)=1
$$

Step 6 (two marks). Apply the repeated-root rule.

$$
y_{p}=\frac{xe^{3x}}{f'(3)}=xe^{3x}
$$

Step 7 (one mark). Write the general solution.

$$
y=c_{1}e^{3x}+c_{2}e^{2x}+xe^{3x}
$$

Step 8 (one mark). Verify, collecting the coefficient of $xe^{3x}$ and the coefficient of $e^{3x}$ separately.

$$
y_{p}'=e^{3x}\left(1+3x\right), \qquad y_{p}''=e^{3x}\left(6+9x\right),
$$

$$
y_{p}''-5y_{p}'+6y_{p}=e^{3x}\left(6+9x-5-15x+6x\right)=e^{3x}
$$

The coefficient of $xe^{3x}$ is $9-15+6=0$ and the coefficient of $e^{3x}$ is $6-5=1$, so the reply is confirmed. Out of nine marks, the two most often lost are those in Step 4 and Step 6: the depth of the resonance must be justified, and the divisor is the first derivative evaluated at three, which happens to be one here.

### 4.3 Problem: a wave forcing with a surviving first derivative

Solve $\left(D^{2}+3D-10\right)y=\sin 2x$.

### 4.4 Solution: model solution with marking points

Step 1 (one mark). Factor the auxiliary polynomial.

$$
m^{2}+3m-10=0, \qquad \left(m-2\right)\left(m+5\right)=0, \qquad m=2,\ -5
$$

Step 2 (one mark). Write the complementary function.

$$
y_{c}=c_{1}e^{2x}+c_{2}e^{-5x}
$$

Step 3 (one mark). Split the polynomial into even and odd parts and collapse at $-a^{2}=-4$.

$$
f_{1}\left(D^{2}\right)=D^{2}-10, \qquad f_{2}\left(D^{2}\right)=3, \qquad A=-14, \qquad B=3
$$

Step 4 (one mark). Compute the denominator and check that it is not zero, which confirms that no resonance occurs.

$$
A^{2}+B^{2}a^{2}=196+36=232
$$

Step 5 (two marks). Apply the collapsed formula, differentiating the sine once to obtain the cosine.

$$
y_{p}=\frac{\left(A-BD\right)\sin 2x}{232}=\frac{-14\sin 2x-6\cos 2x}{232}=-\frac{7\sin 2x}{116}-\frac{3\cos 2x}{116}
$$

Step 6 (one mark). Write the general solution.

$$
y=c_{1}e^{2x}+c_{2}e^{-5x}-\frac{7\sin 2x}{116}-\frac{3\cos 2x}{116}
$$

Step 7 (two marks). Verify by substitution, reporting both coefficients.

$$
\left(-14A_{1}+6B_{1}\right)\cos 2x+\left(-6A_{1}-14B_{1}\right)\sin 2x=\sin 2x
$$

with $A_{1}=-\frac{3}{116}$ and $B_{1}=-\frac{7}{116}$: the cosine coefficient is $\frac{42}{116}-\frac{42}{116}=0$ and the sine coefficient is $\frac{18}{116}+\frac{98}{116}=1$. The check confirms the collapse and the clearing step, and it also confirms the relative sign of the two terms, which is where the marks are usually lost.

### 4.5 Problem: a polynomial forcing

Solve $\left(2D^{2}+2D+3\right)y=x^{2}$.

### 4.6 Solution: model solution with marking points

Step 1 (one mark). Record the constant term, which is the number that must not vanish.

$$
f(0)=3
$$

Step 2 (one mark). Factor out the constant term and write the operator in the form of a series.

$$
\frac{1}{2D^{2}+2D+3}=\frac{1}{3}\left(1+\frac{2}{3}D+\frac{2}{3}D^{2}\right)^{-1}
$$

Step 3 (two marks). Expand to second order, keeping the square of the first-order term.

$$
\left(1+U\right)^{-1}=1-U+U^{2}-\cdots, \qquad U=\frac{2}{3}D+\frac{2}{3}D^{2},
$$

$$
1-\frac{2}{3}D-\frac{2}{3}D^{2}+\frac{4}{9}D^{2}=1-\frac{2}{3}D-\frac{2}{9}D^{2}
$$

Step 4 (two marks). Apply the truncated operator, using $Dx^{2}=2x$ and $D^{2}x^{2}=2$.

$$
y_{p}=\frac{1}{3}\left[x^{2}-\frac{2}{3}\left(2x\right)-\frac{2}{9}\left(2\right)\right]=\frac{x^{2}}{3}-\frac{4x}{9}-\frac{4}{27}
$$

Step 5 (one mark). Write the complementary function from the roots of $2m^{2}+2m+3=0$.

$$
m=-\frac{1}{2}\pm\frac{\sqrt{5}}{2}i, \qquad y_{c}=e^{-x/2}\left(c_{1}\cos\frac{\sqrt{5}}{2}x+c_{2}\sin\frac{\sqrt{5}}{2}x\right)
$$

Step 6 (one mark). State the general solution.

$$
y=e^{-x/2}\left(c_{1}\cos\frac{\sqrt{5}}{2}x+c_{2}\sin\frac{\sqrt{5}}{2}x\right)+\frac{x^{2}}{3}-\frac{4x}{9}-\frac{4}{27}
$$

Step 7 (two marks). Verify, collecting the three powers separately.

$$
y_{p}'=\frac{2x}{3}-\frac{4}{9}, \qquad y_{p}''=\frac{2}{3},
$$

$$
2y_{p}''+2y_{p}'+3y_{p}=\frac{4}{3}+\frac{4x}{3}-\frac{8}{9}+x^{2}-\frac{4x}{3}-\frac{4}{9}=x^{2}
$$

The $x$ coefficient is $\frac{4}{3}-\frac{4}{3}=0$ and the constant is $\frac{4}{3}-\frac{8}{9}-\frac{4}{9}=0$, so the polynomial is reproduced exactly. The two marks most often dropped in this question are the square of $\frac{2}{3}D$ in Step 3 and the second derivative in Step 4.

### 4.7 Problem: an exponential multiplied by a power

Solve $\left(D-4\right)y=x^{2}e^{3x}$.

### 4.8 Solution: model solution with marking points

Step 1 (one mark). Apply the shift, adding three to the operator.

$$
\frac{x^{2}e^{3x}}{D-4}=e^{3x}\frac{x^{2}}{D+3-4}=e^{3x}\frac{x^{2}}{D-1}
$$

Step 2 (one mark). Rewrite the residual operator so that the expansion has the required form.

$$
\frac{1}{D-1}=-\left(1-D\right)^{-1}=-\left(1+D+D^{2}+\cdots\right)
$$

Step 3 (two marks). Apply it to $x^{2}$, reaching the second derivative.

$$
\frac{x^{2}}{D-1}=-\left(x^{2}+2x+2\right)
$$

Step 4 (one mark). Multiply the exponential back and write the complementary function, which is a single exponential because the order is one.

$$
y=c_{1}e^{4x}-e^{3x}\left(x^{2}+2x+2\right)
$$

Step 5 (two marks). Verify, collecting the three pieces.

$$
y_{p}'=-e^{3x}\left(3x^{2}+8x+8\right), \qquad y_{p}'-4y_{p}=e^{3x}\left(-3x^{2}-8x-8+4x^{2}+8x+8\right)=x^{2}e^{3x}
$$

The coefficients of $x^{2}$, of $x$ and of the constant all agree, which confirms that the shift was by $+3$ and not by $-3$. A shift by the wrong sign produces $e^{3x}\frac{x^{2}}{D-7}$ and a visibly different answer that fails this check.

### 4.9 Problem: the variable multiplied by an exponential

Solve $\left(D^{2}-1\right)y=xe^{3x}$.

### 4.10 Solution: model solution with marking points

Step 1 (one mark). Record the two ingredients of the multiplier rule.

$$
f(D)=D^{2}-1, \qquad f'(D)=2D, \qquad f(3)=8
$$

Step 2 (one mark). Write the first term.

$$
x\frac{e^{3x}}{8}
$$

Step 3 (two marks). Write the correction, squaring the operator in the denominator.

$$
\frac{f'(D)}{\left[f(D)\right]^{2}}e^{3x}=\frac{2D\,e^{3x}}{64}=\frac{6e^{3x}}{64}=\frac{3e^{3x}}{32}
$$

Step 4 (one mark). Subtract and add the complementary function.

$$
y=c_{1}e^{x}+c_{2}e^{-x}+\frac{xe^{3x}}{8}-\frac{3e^{3x}}{32}
$$

Step 5 (two marks). Verify by differentiating twice.

$$
y_{p}'=e^{3x}\left(\frac{3x}{8}-\frac{5}{32}\right), \qquad y_{p}''=e^{3x}\left(\frac{9x}{8}-\frac{3}{32}\right),
$$

$$
y_{p}''-y_{p}=e^{3x}\left(\frac{9x}{8}-\frac{3}{32}-\frac{x}{8}+\frac{3}{32}\right)=xe^{3x}
$$

Step 6 (one mark). Cross-check with the shift rule, which must agree.

$$
\frac{xe^{3x}}{D^{2}-1}=e^{3x}\frac{x}{D^{2}+6D+8}=\frac{e^{3x}}{8}\left(x-\frac{3}{4}\right)
$$

The two forms are identical after expansion, which is a complete confirmation of the arithmetic.

### 4.11 Problem: a sum of a resonant wave and a polynomial

Solve $\left(D^{2}+4\right)y=\cos 2x+x$.

### 4.12 Solution: model solution with marking points

Step 1 (one mark). Record the complementary function; the roots are $\pm 2i$.

$$
y_{c}=c_{1}\cos 2x+c_{2}\sin 2x
$$

Step 2 (one mark). Split the forcing into the wave and the polynomial, as the additivity theorem permits.

Step 3 (one mark). Collapse the polynomial at the wave's rate and observe the resonance.

$$
D^{2}\to -4, \qquad -4+4=0
$$

Step 4 (two marks). Apply the resonant wave rule to the cosine piece, using $f'(D)=2D$.

$$
y_{1}=x\cdot\frac{\cos 2x}{2D}=\frac{x\sin 2x}{4}
$$

Step 5 (two marks). Apply the polynomial rule to $x$, noting that $f(0)=4$ does not vanish.

$$
\frac{x}{D^{2}+4}=\frac{1}{4}\left(1+\frac{D^{2}}{4}\right)^{-1}x=\frac{1}{4}\left(x-0\right)=\frac{x}{4}
$$

Step 6 (one mark). Add the pieces and assemble the general solution.

$$
y=c_{1}\cos 2x+c_{2}\sin 2x+\frac{x\sin 2x}{4}+\frac{x}{4}
$$

Step 7 (one mark). Verify each piece separately, since the operator is linear.

$$
\left(D^{2}+4\right)\frac{x\sin 2x}{4}=\cos 2x, \qquad \left(D^{2}+4\right)\frac{x}{4}=x
$$

The first verification uses $y_{1}''=\cos 2x-x\sin 2x$, so $y_{1}''+4y_{1}=\cos 2x$. The second is immediate because the second derivative of $\frac{x}{4}$ is zero. The decisive observation, worth a mark in its own right, is that only the cosine piece is resonant: treating the polynomial as resonant would introduce a spurious factor of $x$ and fail the check.

### 4.13 Problem: prove the exponential shift theorem

Prove that $f(D)\left[e^{ax}u\right]=e^{ax}f(D+a)u$ for every polynomial $f$ with constant coefficients and every differentiable function $u$.

### 4.14 Solution: model proof with marking points

Step 1 (one mark). Establish the first-order case by the product rule.

$$
\frac{d}{dx}\left(e^{ax}u\right)=ae^{ax}u+e^{ax}\frac{du}{dx}=e^{ax}\left(a+D\right)u
$$

Step 2 (one mark). State the induction hypothesis precisely, for a general whole number $k$.

$$
D^{k}\left[e^{ax}u\right]=e^{ax}\left(D+a\right)^{k}u
$$

Step 3 (two marks). Perform the induction step, applying $D$ to the product and using the first-order case with $w=\left(D+a\right)^{k}u$.

$$
D^{k+1}\left[e^{ax}u\right]=D\left[e^{ax}\left(D+a\right)^{k}u\right]=e^{ax}\left(D+a\right)\left(D+a\right)^{k}u=e^{ax}\left(D+a\right)^{k+1}u
$$

Step 4 (one mark). Conclude that the identity holds for every whole number by induction.

Step 5 (one mark). Extend from powers to polynomials by linearity, writing $f(D)$ as a sum of coefficients times powers.

$$
f(D)\left[e^{ax}u\right]=\sum_{k}c_{k}D^{k}\left[e^{ax}u\right]=e^{ax}\sum_{k}c_{k}\left(D+a\right)^{k}u=e^{ax}f(D+a)u
$$

Step 6 (one mark). Draw the corollary for the inverse operator, dividing both sides by $f(D)$ and reading the identity backwards.

$$
\frac{e^{ax}u}{f(D)}=e^{ax}\frac{u}{f(D+a)}
$$

A proof question of this kind is marked on structure rather than on length: the base case, the stated hypothesis, the induction step with the reason for each equality, the extension by linearity, and the corollary. The two marks most often lost are in Step 2, where the hypothesis must be stated for a general $k$ rather than for a specific number, and in Step 5, where the step from powers to polynomials must be justified by linearity.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The trap table

| Trap | Why it is wrong | How to avoid it |
| --- | --- | --- |
| Replacing $D^{2}$ by $+a^{2}$ | the second derivative of a wave of rate $a$ is $-a^{2}$ times the wave | always write $D^{2}\to-a^{2}$ and test on $D^{2}+9$ at rate two |
| Collapsing a surviving $D$ as well | only even powers may be collapsed | split $f$ into even and odd parts before collapsing |
| Dividing by zero in a resonant case | the forcing lies in the nullspace, so no reply of that shape exists | multiply by $x^{r}$ and divide by $f^{(r)}$ |
| Multiplying by $x$ when nothing fails | the reply then belongs to the wrong family | evaluate the test first and record the value |
| Writing $\frac{x^{2}e^{ax}}{2f''(a)}$ | the divisor $f^{(r)}(a)$ already contains $r!$ | use $f^{(r)}(a)$ exactly as stated |
| Guessing the depth of resonance | the exponent of $x$ is the multiplicity of the root | factor the polynomial and read the multiplicity |
| Truncating the expansion at the wrong power | $D^{n}x^{n}=n!$ is the term that fixes the constant | expand to $D^{n}$ inclusive |
| Expanding in descending powers | only the ascending expansion annihilates the polynomial | start at the constant term and climb |
| Using the leading coefficient as the divisor | the constant term is $f(0)$, the coefficient of $y$ | collect the polynomial in standard form first |
| Omitting the correction term in R9 | the product rule contributes an extra derivative | keep $-\frac{f'(D)}{\left[f(D)\right]^{2}}u$ |
| Using $f(D)$ rather than $f'(D)$ in R9 | the numerator must be the derivative of the polynomial | differentiate $f$ with respect to $D$ first |
| Shifting by $D-a$ instead of $D+a$ | differentiating $e^{ax}u$ produces a factor $a$, not $-a$ | write the shift as $D+a$ and check by substitution |
| Dropping the complementary function | the particular integral carries no arbitrary constants | count constants against the order |
| Verifying by re-reading | only substitution detects a sign error | substitute and report every coefficient |

### 5.2 Sign discipline in three numbers

The single most reliable defence against the wave sign is to compute three numbers before writing any answer: the collapsed value, the denominator $A^{2}+B^{2}a^{2}$, and the value of the forcing's rate in the exponential case. If the collapsed value is not zero, the answer is that number dividing the forcing, with the sign of the number carried through. If the denominator is large, the answer is small, which is the physically sensible behaviour of a machine that responds weakly far from its natural rate.

A second discipline governs the exponential case: the sign of $f(a)$ decides the sign of the answer, and $f(a)$ must be computed with every coefficient in its original sign. For $f(D)=D^{2}-5D+6$ at four the value is $16-20+6=2$, not $16-20-6$.

### 5.3 Revision checklist

Before the examination, confirm that each of the following can be done from memory in under a minute.

The five statements R1 to R5 and R6 to R9, with their hypotheses. The factorisation of the auxiliary polynomial and the three forms of the complementary function: distinct real roots, repeated roots with the extra factor of $x$, and complex roots with the exponential envelope. The three tests for resonance and the size of the remedy in each case. The ascending expansion of $\left(1+U\right)^{-1}$ to second order, which is the expansion most questions need. The identity $\left(D-a\right)\left[e^{ax}w\right]=e^{ax}Dw$, which drives both the repeated-root proof and the shift rule. And the Leibniz identity $D^{k}\left[xu\right]=xD^{k}u+kD^{k-1}u$, which drives the multiplier rule.

Then confirm that each of the following can be performed without error on a chosen example: evaluating $f(a)$ with signs; collapsing an even polynomial at $-a^{2}$; clearing a surviving first-order operator by its companion; expanding $1/f(D)$ to the second power of $D$; and substituting a candidate particular integral back and reporting the coefficients of two independent pieces.

### 5.4 Time strategy

For a paper of two hours with six questions, allow ten minutes for any question whose forcing is an exponential or a polynomial without a product, twelve minutes for a wave with a surviving derivative, and fifteen minutes for a product forcing under the multiplier rule. Within any question, spend the first minute on the complementary function, because it is mechanical and guaranteed marks, and the last two minutes on the substitution check.

If a particular integral resists after four minutes, the diagnosis is almost always one of three things: the wrong test has been applied, a resonance has been missed, or the collapse has been performed on an odd power of $D$. Re-read the second column of the decision table, then start the piece again rather than patching the algebra, because a patched particular integral rarely survives substitution.

### 5.5 What costs the last two marks

The last two marks of a solution question are awarded for the verification and for the correct count of constants. Both are cheap and both are commonly lost. The verification must be a substitution with the coefficients collected; a sentence claiming that the answer satisfies the equation earns nothing. The count of constants must match the order, and the commonest failure is to write a second-order complementary function with one constant after a repeated root, forgetting the factor of $x$ on the second member.

A third, subtler loss occurs when the particular integral duplicates part of the complementary function in a resonant case. It is legitimate for the particular integral to contain such a term, but the complementary function must still display both independent members, and the two must not be merged into one term with a single constant.

### 5.6 Summary of the high-yield content

Five shapes and five rules, with three failure remedies. Exponentials are answered by evaluating the polynomial at the rate, and by differentiating the polynomial when that evaluation vanishes. Waves are answered by collapsing the even part at minus the square of the rate and clearing any surviving derivative, and by multiplying by $x$ when the collapse vanishes. Polynomials are answered by an ascending expansion truncated at the degree, and by dividing out a factor of $D$ and integrating when the constant term vanishes. An exponential times a function is answered by shifting the polynomial by the rate. The variable times a function is answered by two terms, the second of which is the correction for the product rule.

The marks are distributed predictably: the complementary function and the general solution take about half, the particular integral takes about a third, and the verification takes the remainder. A candidate who writes the polynomial, tests the condition, applies the rule, assembles the answer and substitutes has done everything the examiner is looking for, and the only remaining risk is arithmetic.

### 5.7 The question patterns, one by one

Six patterns account for almost every question set on this topic, and each rewards a different habit.

An exponential away from resonance rewards arithmetic discipline: compute $f(a)$ with all signs, divide, and check. A candidate who loses a mark here has usually dropped a sign when the polynomial was written down.

An exponential at resonance rewards the factorisation. The question is testing whether the candidate notices that the exponent's rate is a root, and whether the depth of the root is read correctly. The full marks require the multiplicity to be stated, not merely used.

A wave with an even polynomial rewards the sign discipline of the collapse. The whole question is decided by whether $D^{2}$ becomes $-a^{2}$ or $+a^{2}$, and the substitution check makes the difference visible.

A wave with a surviving first derivative rewards the extra step of clearing the operator. Many candidates collapse correctly and then divide by the operator as though it were a number, which is the single most expensive error in the topic.

A wave at resonance rewards recognising that the collapse has produced zero rather than a large number, and then applying the derivative rule with its factor of $x$.

A polynomial forcing rewards the expansion discipline: the constant term, the ascending order, and the truncation index. Questions of this kind are usually worth more marks than the others because they contain more independent algebraic steps.

A product forcing rewards knowing which of the two product rules applies. If the product is an exponential times a function, the shift rule is shorter and should be preferred; the multiplier rule is reserved for the case where the multiplier is the variable itself, or where the shift leaves a problem of a shape not yet handled.

In every pattern, the general solution is completed by adding the complementary function, and the free constants are fixed only if the question supplies conditions. A question that supplies no conditions is asking for the general solution, and an answer that fixes the constants arbitrarily has answered a different question.
