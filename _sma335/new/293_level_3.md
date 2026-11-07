## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What is actually being examined

Questions on this topic are almost never open-ended. They follow a small number of templates, and each template has a fixed sequence of steps that earns a fixed sequence of marks. The marks are awarded for identifiable acts: writing the equation in the correct normalised form, producing the correct operator identity, factoring the auxiliary polynomial correctly, writing the complementary function with the right number of constants, producing a particular integral of the right shape, and assembling and checking the final answer. A candidate who knows the templates and performs the acts in order will score well even if the arithmetic is slow. A candidate who improvises will lose marks in places that are easy to predict, and the trap table in Section 5.1 lists those places explicitly.

Three families of equation appear on every paper: the constant-coefficient equation of order three or more, the Cauchy–Euler equation of order two, three or four, and Legendre's equation, usually of order two. The last two are solved by the same reduction, so the work of learning them overlaps heavily, and the examinable difference between them is a single factor.

### 1.2 The definition, in the form that earns marks

> **Definition (Linear equation of order n).** A linear differential equation of order n is one that can be written with the unknown function and its first n derivatives each multiplied by a coefficient depending on x alone, the sum equal to a prescribed function of x, with the coefficient of the highest derivative nonzero.

$$
a_{0}(x)\frac{d^{n}y}{dx^{n}}+a_{1}(x)\frac{d^{n-1}y}{dx^{n-1}}+\cdots+a_{n-1}(x)\frac{dy}{dx}+a_{n}(x)y=Q(x)
$$

The definition question is worth two marks and expects three things to be said: the highest derivative present is the n-th, every term is of the first degree in y and its derivatives with no products, and the coefficients are functions of x alone or constants. When Q is zero the equation is called homogeneous; otherwise it is non-homogeneous, and Q is the non-homogeneous term.

Two remarks routinely earn the second mark. First, $a_{0}\neq 0$ is required, otherwise the order is not n. Second, "linear" refers to the unknown, not to the coefficients: the equation with coefficients $x^{3}$ and $\ln x$ is still linear, while the equation with $y^{2}$ or $y y'$ is not.

### 1.3 The operator form and where the difficulty lives

With $D=\frac{d}{dx}$, a linear equation with constant coefficients is written $P(D)y=Q(x)$, where $P$ is a polynomial of degree n. Every question on the constant-coefficient case is then a question about the roots of $P$.

$$
P(D)=a_{0}D^{n}+a_{1}D^{n-1}+\cdots+a_{n-1}D+a_{n}
$$

The difficulty moves from calculus to algebra: factorise $P$, list the roots with multiplicity, and translate. The complementary function is a direct transcription of the root list, and the particular integral is a single evaluation of $P$, or of a derivative of $P$ when the forcing term is resonant.

For the two variable-coefficient families the same structure survives, but the operator must first be converted. That conversion is where marks are lost, and it is the subject of the next two subsections.

### 1.4 The Cauchy–Euler equation: recognition and normalisation

> **Definition (Cauchy–Euler equation of order n).** The equation is of Cauchy–Euler type when the k-th derivative is multiplied by a constant times $x^{k}$, for every k from 0 to n.

$$
x^{n}\frac{d^{n}y}{dx^{n}}+a_{1}x^{n-1}\frac{d^{n-1}y}{dx^{n-1}}+\cdots+a_{n-1}x\frac{dy}{dx}+a_{n}y=f(x)
$$

The operator form collects the same information and is the form in which the substitution is applied.

$$
\left(a_{0}x^{n}D^{n}+a_{1}x^{n-1}D^{n-1}+\cdots+a_{n-1}xD+a_{n}\right)y=f(x)
$$

Two normalisation habits save marks. First, if the leading coefficient is $2x^{3}$ rather than $x^{3}$, divide the whole equation by two before writing the operator identities; otherwise the coefficient two must be carried through every subsequent line and is easily dropped. Second, if the leading term is $x^{3}y''$ the equation is not of Euler type at all, and no amount of substitution will rescue it; say so and stop.

Recognition takes about ten seconds and is worth marks of its own, because candidates who misidentify the type produce a solution by the wrong method and receive nothing for the subsequent work.

### 1.5 Legendre's equation: recognition and the factor a to the power k

> **Definition (Legendre's linear equation of order n).** The equation is of Legendre type when the k-th derivative is multiplied by a constant times the k-th power of the affine expression ax plus b, with a nonzero.

$$
(ax+b)^{n}\frac{d^{n}y}{dx^{n}}+a_{1}(ax+b)^{n-1}\frac{d^{n-1}y}{dx^{n-1}}+\cdots+a_{n-1}(ax+b)\frac{dy}{dx}+a_{n}y=f(x)
$$

The Cauchy–Euler equation is the case a equal to one and b equal to zero. The substitution is the same substitution applied to the affine expression.

$$
ax+b=e^{t}, \qquad t=\ln(ax+b), \qquad \theta=\frac{d}{dt}
$$

The dictionary that must be reproduced exactly, with the factor a present in every entry, is the following.

$$
(ax+b)D=a\theta
$$

$$
(ax+b)^{2}D^{2}=a^{2}\theta(\theta-1)
$$

$$
(ax+b)^{3}D^{3}=a^{3}\theta(\theta-1)(\theta-2)
$$

Each entry earns a mark in a "show that the equation reduces to" question, and the factor a is the single most frequently omitted piece of the entire topic. When a equals one the entries agree with the Euler dictionary, which is why Legendre practice is often mistaken for Euler practice; the error shows up the moment a is not one.

### 1.6 The mark-bearing structure of a typical answer

Almost every solution in this topic is assembled from four blocks, and the marks are distributed across the blocks rather than across the lines. The table shows the usual allocation for a ten-mark question.

| Block | What is produced | Usual marks |
| --- | --- | --- |
| Reduction | the operator identities, with the factor a where applicable, and the transformed equation | 2 to 3 |
| Complementary function | auxiliary polynomial factored, roots listed with multiplicity, correct number of constants | 3 to 4 |
| Particular integral | correct rule chosen, resonance handled, one function obtained with no arbitrary constant | 2 to 3 |
| Assembly and check | general solution in x, substitution verification | 1 to 2 |

Two consequences follow. A candidate who reaches a correct complementary function but no particular integral typically earns half the marks, so the particular integral must never be abandoned. A candidate who produces a beautiful complementary function with the wrong number of constants loses marks inside the second block even though the algebra was perfect, because the marker is checking the count as a separate act.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 High-yield results and what they are worth

The results below are the ones that recur. The mark column records the value of the result when it is asked for directly, as in a "state" or "show that" question.

| Result | Statement in words | Usual marks |
| --- | --- | --- |
| Definition of order n linearity | the standard five-part form, with $a_{0}\neq 0$ | 2 |
| Superposition | sums and constant multiples of solutions of the homogeneous equation are solutions | 1 to 2 |
| Constant count | the general solution of order n has exactly n independent constants | 1 |
| Auxiliary equation | replace D by m and set the polynomial to zero | 1 |
| Three root cases | distinct, repeated, complex conjugate | 3 |
| Euler operator identity | $x^{k}D^{k}$ equals the falling factorial in theta | 2 to 3 |
| Euler reduction | the transformed constant-coefficient equation | 3 |
| Legendre identity | the same with the factor a to the power k | 3 |
| Particular integral rule | evaluate P at the exponent, or differentiate P when resonant | 2 |
| Resonance correction | multiply by the power of t, or of the logarithm | 2 |

### 2.2 The three root cases, stated for transcription

For a constant-coefficient equation with auxiliary polynomial $P$:

A real root m of multiplicity one contributes $c e^{mx}$.

A real root m of multiplicity r contributes the exponential multiplied by a polynomial of degree r minus one.

$$
\left(c_{1}+c_{2}x+\cdots+c_{r}x^{r-1}\right)e^{mx}
$$

A complex pair with real part p and imaginary part q, each of multiplicity r, contributes an exponential $e^{px}$ multiplied by polynomials of degree r minus one in x, one multiplying a cosine of qx and one multiplying a sine of qx.

$$
e^{px}\left[\left(A_{0}+A_{1}x+\cdots\right)\cos qx+\left(B_{0}+B_{1}x+\cdots\right)\sin qx\right]
$$

For the Cauchy–Euler equation the same three cases hold with x raised to the root replacing the exponential, and the natural logarithm of x replacing x in the polynomial factors.

$$
\left(c_{1}+c_{2}\ln x+\cdots+c_{r}(\ln x)^{r-1}\right)x^{m}
$$

$$
x^{p}\left[\left(A_{0}+A_{1}\ln x+\cdots\right)\cos(q\ln x)+\left(B_{0}+B_{1}\ln x+\cdots\right)\sin(q\ln x)\right]
$$

### 2.3 The theta table, exactly as it must be quoted

The identity in general form is the following, with exactly k factors on the right and the last factor equal to theta minus k plus one.

$$
x^{k}D^{k}=\theta(\theta-1)(\theta-2)\cdots(\theta-k+1)
$$

Expanded, the entries that appear in questions are these.

$$
xD=\theta
$$

$$
x^{2}D^{2}=\theta^{2}-\theta
$$

$$
x^{3}D^{3}=\theta^{3}-3\theta^{2}+2\theta
$$

$$
x^{4}D^{4}=\theta^{4}-6\theta^{3}+11\theta^{2}-6\theta
$$

The coefficients one, one, one-three-two and one-six-eleven-six are not binomial coefficients. They are the unsigned Stirling numbers of the first kind, and no expansion of a binomial will ever reproduce them.

### 2.4 The Legendre dictionary

Every entry of the Euler dictionary is multiplied by the matching power of a.

$$
(ax+b)^{k}D^{k}=a^{k}\theta(\theta-1)(\theta-2)\cdots(\theta-k+1)
$$

The right-hand member must also be rewritten, since x equals the quantity $e^{t}$ minus b, all divided by a. A question that supplies a right-hand member already written as a power of ax plus b has done that work in advance, and the exponent of that power is the number at which the auxiliary polynomial is evaluated.

### 2.5 The two particular-integral rules

> **Rule (Non-resonant case).** If the forcing term is $x^{r}$ in the Euler case, or $(ax+b)^{r}$ in the Legendre case, and r is not a root of the auxiliary polynomial P, then a particular integral is that power divided by P evaluated at r.

$$
y_{p}=\frac{x^{r}}{P(r)}, \qquad y_{p}=\frac{(ax+b)^{r}}{P(r)}
$$

> **Rule (Resonant case).** If r is a root of P of multiplicity s, a particular integral is the power multiplied by the s-th power of the logarithm, divided by the s-th derivative of P evaluated at r.

$$
y_{p}=\frac{x^{r}(\ln x)^{s}}{P^{(s)}(r)}, \qquad y_{p}=\frac{(ax+b)^{r}\left(\ln(ax+b)\right)^{s}}{P^{(s)}(r)}
$$

For s equal to one, which is the case that appears in almost every examination, the formula reads: power times logarithm, divided by P prime at r. For the constant-coefficient equation the same rule reads: exponential times x to the power s, divided by the s-th derivative of P at the exponent, and the factorial is absorbed in the derivative.

### 2.6 The question patterns

The phrasing of a question reveals which block of work is being tested, and reading the phrasing before starting saves time.

A question beginning "State the order and degree" or "Define a linear equation of order n" is worth two marks and requires only the definition.

A question beginning "Show that the substitution x equals $e^{t}$ transforms" supplies marks for the three operator identities and for the transformed equation, and nothing else.

A question ending "hence solve" requires the full four blocks, and the word hence forbids solving from scratch by another method.

A question beginning "Find the complementary function of" stops at the second block and does not want a particular integral; producing one wastes time and can introduce an error that costs a mark.

A question beginning "Find a particular integral of" wants only the third block and expects the resonance decision to be visible.

A question that supplies a proposed solution and asks to verify it wants differentiation and substitution, with the variable coefficients preserved, and no solving at all.

### 2.7 Reading the instruction words

The word hence means the previous part must be used; a solution that ignores it usually cannot earn the later marks. The word show that, applied to a reduced equation, means the reduced equation is given and may be quoted thereafter. The word hence or otherwise permits a fresh method but never rewards one. The word verify means substitute, do not solve. These conventions are worth marks in themselves because they determine what the marker expects to see on the page.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Deriving the first two identities under examination conditions

The derivation is short and should be reproduced in four lines. With $x=e^{t}$ and $t=\ln x$, the chain rule gives the rate of change of t with respect to x as one over x.

$$
\frac{dy}{dx}=\frac{dy}{dt}\cdot\frac{dt}{dx}=\frac{1}{x}\theta y
$$

Multiplying by x gives the first identity.

$$
x\frac{dy}{dx}=\theta y
$$

For the second, differentiate the product of one over x and the derivative of y with respect to t.

$$
\frac{d^{2}y}{dx^{2}}=-\frac{1}{x^{2}}\theta y+\frac{1}{x^{2}}\theta^{2}y
$$

Multiplying by $x^{2}$ and factoring gives the second identity.

$$
x^{2}\frac{d^{2}y}{dx^{2}}=\theta(\theta-1)y
$$

The minus sign in the middle line is the whole content of the result, and it should be pointed at when writing the answer, because a marker looks for it.

### 3.2 The general identity by induction

The claim is $x^{k}D^{k}=\theta^{\underline{k}}$, where $\theta^{\underline{k}}$ denotes the product of k descending factors. Equivalently $D^{k}=x^{-k}\theta^{\underline{k}}$.

The case k equal to one is Section 3.1. Assume the claim for k and apply D to the product $x^{-k}\theta^{\underline{k}}y$, using the product rule.

$$
D^{k+1}y=-kx^{-k-1}\theta^{\underline{k}}y+x^{-k}\cdot\frac{1}{x}\theta\,\theta^{\underline{k}}y
$$

Because $\theta^{\underline{k}}$ is a polynomial in theta with constant coefficients it commutes with theta, so the second term is $x^{-k-1}\theta^{\underline{k}+1}y$. Factoring out $x^{-k-1}$ leaves the product of k plus one descending factors.

$$
D^{k+1}y=x^{-k-1}\left(\theta-k\right)\theta^{\underline{k}}y=x^{-k-1}\theta^{\underline{k+1}}y
$$

Multiply by $x^{k+1}$ and the induction closes. The proof is worth three marks when it is asked for, and the essential line is the one in which the factor theta minus k appears; that factor is the reason the coefficients are Stirling numbers and not binomial coefficients.

### 3.3 The Legendre identity and its factor

With $u=ax+b$ and $t=\ln u$, the chain rule gives the rate of change of t with respect to x as a divided by u.

$$
\frac{dy}{dx}=\frac{a}{u}\theta y
$$

Multiplying by u gives the first Legendre identity, with the factor a present.

$$
(ax+b)\frac{dy}{dx}=a\theta y
$$

Differentiating again and repeating the same product-rule step produces one more factor of a, and the pattern continues.

$$
(ax+b)^{2}\frac{d^{2}y}{dx^{2}}=a^{2}\theta(\theta-1)y
$$

The same result is obtained by the two-stage view: write $u=ax+b$ so that differentiation with respect to x is a times differentiation with respect to u, which supplies $a^{k}$ immediately, and then apply the Euler identity in the variable u.

### 3.4 The reduction, with the mark allocation visible

For the Euler case, substitute each identity into the equation. The terms in the operator form are replaced one at a time, from the highest order downward.

$$
\left[\theta^{\underline{n}}+a_{1}\theta^{\underline{n-1}}+\cdots+a_{n-1}\theta+a_{n}\right]y=f(e^{t})
$$

Three acts earn the marks here: replacing each operator with its polynomial, carrying the forcing term across as a function of t, and stating the resulting constant-coefficient equation in a single collected line. For the Legendre case each polynomial carries its power of a, and the forcing term is written with x replaced by the quantity $e^{t}$ minus b, all over a.

A useful habit is to state the reduced equation with the auxiliary polynomial already collected in descending powers of theta. The next step is then purely algebraic, and the marker can see the polynomial that is about to be factored.

### 3.5 The particular-integral decision tree

The decision takes three questions and about thirty seconds.

First, is the forcing term a power, an exponential, a polynomial, or a sum of these? If it is a sum, split it and treat each piece separately.

Second, if it is a power or exponential with exponent r, evaluate P at r. A nonzero value means the particular integral is the power divided by that value, and the work is finished in one line.

Third, if the value is zero, find the multiplicity s of r as a root, differentiate P exactly s times, evaluate at r, and multiply the power by the s-th power of the logarithm before dividing.

For forcing terms that are not powers, such as a logarithm or a sine of the logarithm, solve the reduced equation directly by undetermined coefficients in the variable t. The trial function is chosen to match the forcing term: a logarithm needs a linear function of t, a sine of t needs a combination of a sine and a cosine of t.

### 3.6 The verification protocol

Verification in this topic is not optional, because the variable coefficients make sign errors invisible. The protocol has three steps.

Differentiate the claimed particular integral with respect to x, using the chain rule where an affine expression appears, and record every derivative before substituting.

Substitute into the original left-hand side, keeping each coefficient attached to the derivative it multiplies. Never substitute into the reduced equation, which is a different equation and will not detect an error in the reduction itself.

Simplify and compare with the right-hand member, and state the comparison in words.

For a claimed complementary function, one substitution of the most awkward member is enough; the simplest member is usually an exponential or a power that is obviously correct.

### 3.7 Speed algebra worth practising

Factorisation is where time is lost. Three techniques cover almost every auxiliary polynomial in this topic.

Test the divisors of the constant term first, beginning with one and minus one. Most examination polynomials have at least one small integer root.

For a cubic with leading coefficient one, once one root r is found, the remaining quadratic is obtained by synthetic division, and its discriminant decides between two real roots and a complex pair.

For an even polynomial in theta, such as a quartic containing only even powers, substitute w for theta squared and factor in w. Complex roots then arrive in pairs of conjugate pairs, and each contributes a cosine-sine pair with logarithmic argument.

## 4. Representative Worked Examples and Solutions

### 4.1 Model solution one: a third-order Cauchy–Euler equation with resonance

Find the general solution of

$$
x^{3}\frac{d^{3}y}{dx^{3}}-3x^{2}\frac{d^{2}y}{dx^{2}}+6x\frac{dy}{dx}-6y=x^{2}, \qquad x>0 .
$$

### 4.2 Solution: standard reduction, then the resonant power rule

Step 1. Quote the three operator identities. This is the reduction mark.

$$
x^{3}D^{3}=\theta^{3}-3\theta^{2}+2\theta, \qquad x^{2}D^{2}=\theta^{2}-\theta, \qquad xD=\theta
$$

Step 2. Substitute and collect, working downward through the orders. This is the second reduction mark.

$$
\left(\theta^{3}-3\theta^{2}+2\theta\right)-3\left(\theta^{2}-\theta\right)+6\theta-6
$$

Step 3. Simplify to a single polynomial in theta. This is the third reduction mark.

$$
\theta^{3}-6\theta^{2}+11\theta-6
$$

Step 4. Rewrite the right-hand member, since $x^{2}=e^{2t}$, and state the reduced equation. One mark.

$$
\left(\theta^{3}-6\theta^{2}+11\theta-6\right)y=e^{2t}
$$

Step 5. Write the auxiliary equation and find one root by inspection, testing one. One mark.

$$
m^{3}-6m^{2}+11m-6=0, \qquad m=1 \text{ since } 1-6+11-6=0
$$

Step 6. Divide out the factor m minus one and factor the remaining quadratic. Two marks.

$$
m^{3}-6m^{2}+11m-6=(m-1)(m-2)(m-3)
$$

Step 7. Transcribe the three distinct real roots into the complementary function, with three constants. Two marks; a missing constant costs one of them.

$$
y_{c}=c_{1}x+c_{2}x^{2}+c_{3}x^{3}
$$

Step 8. Test the exponent two against the auxiliary polynomial. It is a root, so the non-resonant rule cannot be used. One mark for the recognition.

$$
P(2)=8-24+22-6=0
$$

Step 9. Differentiate the auxiliary polynomial and evaluate at two. One mark.

$$
P'(\theta)=3\theta^{2}-12\theta+11, \qquad P'(2)=12-24+11=-1
$$

Step 10. Apply the resonant rule with s equal to one: the power, multiplied by the logarithm, divided by P prime at the exponent. Two marks.

$$
y_{p}=\frac{x^{2}\ln x}{P'(2)}=-x^{2}\ln x
$$

Step 11. Assemble the general solution in x, with three constants for an equation of order three. One mark.

$$
y=c_{1}x+c_{2}x^{2}+c_{3}x^{3}-x^{2}\ln x
$$

Step 12. Verify the particular integral. The derivatives are these.

$$
y'=-2x\ln x-x, \qquad y''=-2\ln x-3, \qquad y'''=-\frac{2}{x}
$$

Step 13. Substitute into the original left-hand side, keeping each power of x with its own derivative.

$$
x^{3}\left(-\frac{2}{x}\right)-3x^{2}\left(-2\ln x-3\right)+6x\left(-2x\ln x-x\right)-6\left(-x^{2}\ln x\right)
$$

Step 14. Expand and collect the coefficients of $x^{2}$ and of $x^{2}\ln x$ separately.

$$
-2x^{2}+6x^{2}\ln x+9x^{2}-12x^{2}\ln x-6x^{2}+6x^{2}\ln x
$$

$$
x^{2}\left(-2+9-6\right)+x^{2}\ln x\left(6-12+6\right)=x^{2}
$$

Step 15. The check gives exactly the required right-hand member, so the answer is confirmed. Total for the question: fifteen marks, of which five belong to the reduction and factorisation, five to the complementary function, four to the particular integral, and one to the assembly.

### 4.3 Model solution two: a Legendre equation with a power forcing

Find the general solution of

$$
(2x+1)^{2}\frac{d^{2}y}{dx^{2}}-4(2x+1)\frac{dy}{dx}+8y=(2x+1)^{3}.
$$

### 4.4 Solution: the factor a squared must appear in the second-derivative term

Step 1. Identify the affine expression, with a equal to two and b equal to one, and state the substitution. One mark.

$$
2x+1=e^{t}, \qquad \theta=\frac{d}{dt}
$$

Step 2. Quote the Legendre identities with the factors of two. One mark, and this is the mark most often lost.

$$
(2x+1)D=2\theta, \qquad (2x+1)^{2}D^{2}=4\theta(\theta-1)
$$

Step 3. Substitute into the left-hand side. One mark.

$$
4\theta(\theta-1)-4\left(2\theta\right)+8
$$

Step 4. Simplify and collect. One mark.

$$
4\theta^{2}-4\theta-8\theta+8=4\theta^{2}-12\theta+8
$$

Step 5. Rewrite the forcing term, since $(2x+1)^{3}=e^{3t}$, and state the reduced equation divided by four. One mark.

$$
\left(\theta^{2}-3\theta+2\right)y=\frac{e^{3t}}{4}
$$

Step 6. Write and factor the auxiliary equation. Two marks.

$$
m^{2}-3m+2=(m-1)(m-2)=0
$$

Step 7. Transcribe the two distinct real roots, remembering that the exponential in t becomes a power of 2x plus 1. Two marks.

$$
y_{c}=c_{1}(2x+1)+c_{2}(2x+1)^{2}
$$

Step 8. Evaluate the auxiliary polynomial at the exponent three. One mark.

$$
P(3)=9-9+2=2
$$

Step 9. Apply the non-resonant rule, using the divided equation. One mark.

$$
y_{p}=\frac{e^{3t}}{4P(3)}=\frac{e^{3t}}{8}
$$

Step 10. Return to x and state the general solution. One mark.

$$
y=c_{1}(2x+1)+c_{2}(2x+1)^{2}+\frac{(2x+1)^{3}}{8}
$$

Step 11. Verify the particular integral. Writing u for 2x plus 1 and y as u cubed over eight, the derivatives are these.

$$
y'=\frac{3u^{2}\cdot 2}{8}=\frac{3u^{2}}{4}, \qquad y''=\frac{6u\cdot 2}{4}=3u
$$

Step 12. Substitute into the original left-hand side.

$$
u^{2}\left(3u\right)-4u\left(\frac{3u^{2}}{4}\right)+8\left(\frac{u^{3}}{8}\right)
$$

Step 13. Simplify; the total is exactly the required power.

$$
3u^{3}-3u^{3}+u^{3}=u^{3}=(2x+1)^{3}
$$

Step 14. Note what the check proves. Had the factor four been omitted in Step 2, the second-derivative term would have contributed only one quarter of its true amount and the check would have failed by a visible margin.

### 4.5 Model solution three: a third-order Cauchy–Euler equation with complex roots and a logarithmic forcing

Find the general solution of

$$
x^{3}\frac{d^{3}y}{dx^{3}}+2x^{2}\frac{d^{2}y}{dx^{2}}+x\frac{dy}{dx}-y=\ln x, \qquad x>0 .
$$

### 4.6 Solution: a complex pair in the complementary function and a linear particular integral

Step 1. Quote the identities and substitute. Two marks.

$$
\left[\left(\theta^{3}-3\theta^{2}+2\theta\right)+2\left(\theta^{2}-\theta\right)+\theta-1\right]y=\ln x
$$

Step 2. Collect into a single polynomial. One mark.

$$
\theta^{3}-\theta^{2}+\theta-1
$$

Step 3. Factor by grouping: take theta squared out of the first two terms and one out of the last two, then factor the common bracket. Two marks.

$$
\theta^{2}(\theta-1)+(\theta-1)=(\theta-1)\left(\theta^{2}+1\right)
$$

Step 4. Rewrite the forcing term, since $\ln x=t$, and state the reduced equation. One mark.

$$
(\theta-1)\left(\theta^{2}+1\right)y=t
$$

Step 5. List the roots: one, and plus or minus i. One mark.

Step 6. Transcribe the complementary function, using x to the one for the real root and the logarithm in the argument of the cosine and sine. Three marks.

$$
y_{c}=c_{1}x+c_{2}\cos(\ln x)+c_{3}\sin(\ln x)
$$

Step 7. Choose a trial particular integral. Since the right-hand side is linear in t and the operator contains no factor that annihilates a linear function, a linear function of t is the right shape. One mark.

$$
y_{p}=At+B
$$

Step 8. Apply the quadratic factor first, which does nothing to a linear function.

$$
\left(\theta^{2}+1\right)(At+B)=At+B
$$

Step 9. Apply the remaining factor theta minus one.

$$
(\theta-1)(At+B)=A-At-B=-At+(A-B)
$$

Step 10. Match coefficients against the right-hand side t, that is one times t plus zero. Two marks.

$$
-A=1, \qquad A-B=0 \qquad\Longrightarrow\qquad A=-1,\quad B=-1
$$

Step 11. So the particular integral is the negative of t minus one, and the general solution follows. One mark.

$$
y=c_{1}x+c_{2}\cos(\ln x)+c_{3}\sin(\ln x)-\ln x-1
$$

Step 12. Verify the particular integral. For y equal to minus the logarithm minus one, the derivatives are these.

$$
y'=-\frac{1}{x}, \qquad y''=\frac{1}{x^{2}}, \qquad y'''=-\frac{2}{x^{3}}
$$

Step 13. Substitute into the original left-hand side.

$$
x^{3}\left(-\frac{2}{x^{3}}\right)+2x^{2}\left(\frac{1}{x^{2}}\right)+x\left(-\frac{1}{x}\right)-\left(-\ln x-1\right)
$$

Step 14. Simplify term by term; the constants cancel and the logarithm survives.

$$
-2+2-1+\ln x+1=\ln x
$$

Step 15. Confirm the count: three constants for an equation of order three, and the answer is complete. Fourteen marks in total, of which three belong to the reduction, six to the complementary function, four to the particular integral, and one to the assembly.

### 4.7 Model solution four: a repeated root with an exponential forcing

Find the general solution of

$$
\frac{d^{3}y}{dx^{3}}-6\frac{d^{2}y}{dx^{2}}+12\frac{dy}{dx}-8y=e^{2x}.
$$

### 4.8 Solution: a triple root and a forcing term that resonates with it

Step 1. Write the operator and recognise the binomial cube. Two marks.

$$
D^{3}-6D^{2}+12D-8=(D-2)^{3}
$$

Step 2. The auxiliary equation has the single root two with multiplicity three. One mark.

$$
(m-2)^{3}=0
$$

Step 3. A root of multiplicity three contributes a quadratic polynomial in x times the exponential. Two marks.

$$
y_{c}=\left(c_{1}+c_{2}x+c_{3}x^{2}\right)e^{2x}
$$

Step 4. Test the exponent two; it is a root of multiplicity three. One mark.

$$
P(2)=0, \qquad P'(2)=0, \qquad P''(2)=0
$$

Step 5. The third derivative of the polynomial is the constant six, since P is the cube of D minus two multiplied by one. One mark.

$$
P'''(\theta)=6, \qquad P'''(2)=6
$$

Step 6. Apply the resonant rule with s equal to three: the exponential multiplied by x cubed, divided by the third derivative at the exponent. Two marks.

$$
y_{p}=\frac{x^{3}e^{2x}}{6}
$$

Step 7. State the general solution. One mark.

$$
y=\left(c_{1}+c_{2}x+c_{3}x^{2}\right)e^{2x}+\frac{x^{3}e^{2x}}{6}
$$

Step 8. Verify by applying the operator three times in succession, which is much faster than expanding the cube. For the proposed particular integral, the first application gives the following.

$$
(D-2)\left(\frac{x^{3}e^{2x}}{6}\right)=e^{2x}\cdot\frac{3x^{2}}{6}=\frac{x^{2}e^{2x}}{2}
$$

Step 9. Apply the operator a second time.

$$
(D-2)\left(\frac{x^{2}e^{2x}}{2}\right)=e^{2x}\cdot\frac{2x}{2}=xe^{2x}
$$

Step 10. Apply the operator a third time.

$$
(D-2)\left(xe^{2x}\right)=e^{2x}
$$

Step 11. The result is exactly the right-hand member, so the answer is confirmed. Nine marks in total, of which three belong to the factorisation and complementary function, four to the particular integral, one to the assembly, and one to the check.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The trap table

The following errors are the ones that appear most often in marked scripts. Each row records the wrong move, the consequence, and the correct practice.

| Trap | What goes wrong | Correct practice |
| --- | --- | --- |
| Writing $x^{2}D^{2}=\theta^{2}$ | the first-derivative term is lost, so the auxiliary polynomial has the wrong roots | always use $\theta^{2}-\theta$ |
| Writing $x^{3}D^{3}=\theta^{3}-3\theta^{2}+3\theta-1$ | that is the expansion of $(\theta-1)^{3}$, not of the falling factorial | use $\theta^{3}-3\theta^{2}+2\theta$ |
| Writing $x^{4}D^{4}$ with binomial coefficients | the Stirling numbers are replaced by the wrong numbers | use $\theta^{4}-6\theta^{3}+11\theta^{2}-6\theta$ |
| Treating $D$ and $\theta$ as the same operator | the factor x that links them is discarded | write $xD=\theta$ and keep the x |
| Omitting $a^{k}$ in a Legendre reduction | one term is scaled wrongly and the root pattern changes | attach the matching power of a to every term |
| Leaving the forcing term in x | the particular integral is computed at the wrong exponent | rewrite $f(x)$ as $f(e^{t})$ before solving |
| Applying the non-resonant rule when the exponent is a root | division by zero produces an infinite or undefined expression | test P at the exponent first, then apply the resonant rule |
| Omitting the logarithm in the resonant case | the trial function duplicates a complementary-function term and no coefficients can be found | multiply by $(\ln x)^{s}$ or by $x^{s}$ as appropriate |
| Omitting the factorial-type divisor $P^{(s)}(r)$ | the particular integral is out by a constant factor | differentiate P exactly s times and evaluate |
| Writing a complex exponential in the final answer | the answer is not real, and the marker deducts for an unfinished conversion | combine the pair into a cosine and a sine |
| Giving fewer constants than the order | the answer is not general and loses a mark in the complementary-function block | count the constants against the order before moving on |
| Using the Euler method on a non-Euler equation | the reduced equation still has variable coefficients and cannot be solved this way | check that every derivative carries the matching power |
| Applying the substitution without requiring $x>0$ | the logarithm is undefined and the interval is unstated | state $x>0$, or use the logarithm of the absolute value of x |
| Substituting only into the reduced equation as a check | an error in the reduction itself goes undetected | substitute into the original equation with the variable coefficients |

Two rows of that table deserve a second sentence. The theta rows account for more lost marks than everything else combined, because the wrong expansion still produces a polynomial that factors, and the resulting answer looks entirely plausible until it is substituted back. The resonance rows account for the second largest group, because the failure is not an arithmetic error but a structural one: the trial function has the wrong shape and the system of equations for its coefficients is inconsistent, which candidates often respond to by inventing a coefficient rather than by correcting the shape.

### 5.2 When the substitution fails, and how to recognise it in advance

The substitution converts the equation into one with constant coefficients only when the coefficient of the k-th derivative is a constant multiple of the k-th power of the same expression. Four failures are examinable.

The first is a mismatched power: the coefficient of the second derivative is $x^{2}$ but the coefficient of the first derivative is a constant. After the substitution the first-derivative term becomes a multiple of $e^{-t}\theta$, and the reduced equation is not constant-coefficient.

The second is a coefficient that is not a power at all, such as a coefficient of $\ln x$ or of $\sin x$ multiplying a derivative. No substitution of this family removes such a factor.

The third is a missing highest-order power. If the leading term is $x^{3}y''$ rather than $x^{2}y''$, the equation is not normalised, and dividing by x leaves a coefficient $x^{2}$ on the second derivative with a coefficient x on the first derivative and no constant coefficient on the function; after division one must re-examine whether the pattern now holds.

The fourth is a non-constant coefficient inside the affine expression that is not of the form ax plus b, for instance $(x^{2}+1)^{2}y''$. The Legendre substitution requires the inner expression to be affine, because only then does the chain rule produce a factor that is a constant multiple of the same expression.

In each case the correct response is to say that the equation is not of Euler or Legendre type and to name the appropriate alternative method. Saying so earns the recognition mark; forcing the substitution earns nothing and usually consumes the time available for the rest of the paper.

### 5.3 Revision checklist

The checklist below is ordered from the results that cost least time to memorise to those that cost most.

Definitions and recognition. State the definition of a linear equation of order n with the nonzero leading coefficient, and distinguish the Euler and Legendre forms by their coefficient patterns. Two marks each.

The theta table. Reproduce the four expanded identities without consulting anything, and reproduce the general falling-factorial statement with the correct number of factors.

The Legendre dictionary. Reproduce the three entries with the factors a, $a^{2}$ and $a^{3}$, and state the substitution $ax+b=e^{t}$ with the resulting expression for x.

The three root cases. Write the contribution of a distinct real root, a real root of multiplicity r, and a complex pair of multiplicity r, in both the exponential form and the power-of-x form.

The particular-integral rules. State the non-resonant rule, the resonant rule with the multiplicity, and the divisors $P(r)$ and $P^{(s)}(r)$.

The verification protocol. Differentiate, substitute into the original equation, simplify, and state the comparison in words.

The trap table. Be able to name the three theta traps and the two resonance traps without prompting, and be able to correct each one.

Practise in this order: two constant-coefficient questions of order three, two Euler questions of order two, one Euler question of order three with a repeated root, one Euler question with a complex pair, one Legendre question with a not equal to one, and one resonance question in each family. That sequence covers every template that appears.

### 5.4 Time strategy

A ten-mark question of this kind should take about fifteen minutes, and the time divides as follows.

Three minutes for recognition and reduction: identify the family, write the substitution, write the operator identities, and state the reduced equation. Do not start solving before the reduced equation is written in a single collected line.

Four minutes for the complementary function: factorisation, root list with multiplicity, and transcription. Check the constant count immediately.

Four minutes for the particular integral: apply the decision tree, and if the exponent is a root, differentiate the polynomial and record the value before writing the answer.

Two minutes for assembly and the check: write the general solution, then verify the particular integral by substitution. If time is short, verify only the hardest term.

Two minutes of reserve, used for the arithmetic that inevitably goes wrong once.

Three habits protect the reserve. Always write the operator identities on the page before using them, so a slip is visible. Always test the exponent against the auxiliary polynomial before applying the particular-integral rule, since that test is one line and prevents the most expensive error. Always verify the particular integral rather than the whole answer, because the whole answer has constants that cannot be checked.

If a question is going badly, the marks are still recoverable in a fixed order: the definition, the reduction, and the complementary function together are usually worth more than the particular integral, so secure those three blocks first and let the particular integral take whatever time remains. A script with a correct complementary function and no particular integral scores roughly half; a script with neither scores nothing, however elegant the attempt.

### 5.5 Looking beyond the examination

Two extensions are worth a moment's thought because they explain the pattern of the results rather than merely restating it.

The first is the presence of logarithms. A repeated root of multiplicity r contributes the powers of the logarithm up to r minus one, and the mechanism is always the same: differentiating the family $x^{m}$ with respect to the parameter m produces a logarithm, and at a repeated root the first derivative of the auxiliary polynomial vanishes, so the logarithm survives into the solution. The same mechanism produces the logarithm in the resonant particular integral, with the multiplicity of the exponent as a root playing the role of the multiplicity of the indicial root. One idea, two appearances.

The second is the scope of the method. A general linear equation with variable coefficients cannot be solved by elementary means, and the Euler and Legendre families are the two important exceptions because their coefficients are exactly the ones for which a logarithmic change of variable produces constant coefficients. Beyond them one needs series solutions, and the indicial equation of those methods is the same polynomial encountered here, obtained by the same trial function $x^{m}$. A student who understands why the substitution works in these two families therefore already understands the first step of the general theory.
