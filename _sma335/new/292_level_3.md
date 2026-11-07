## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 Where the marks sit

This topic is examined in two distinct ways. The first is bookwork: the examiner asks for the standard form, for the derivation of the normal form, or for the exactness condition, and awards marks for the statements and the algebra that produces them. The second is computation: a specific equation with variable coefficients is given and must be solved by one of the four devices. Both kinds of question are predictable, and the marks are attached to identifiable steps.

The distribution below is what a typical paper looks like, and it dictates how much writing each part deserves.

| Question type | Typical marks | Typical time | Where the marks sit |
| --- | --- | --- | --- |
| State the standard form with hypotheses | 2 to 3 | 2 minutes | One for the form, one for naming $P$, $Q$, $R$, one for the condition on $a_{0}$ |
| Prove the change-of-variable coefficient formulas | 6 to 8 | 8 minutes | One for the first derivative, one for the product rule, one for the curvature term, three for the three coefficients |
| Derive the normal form from $y=uv$ | 7 to 9 | 9 minutes | Two for the derivatives of $y$, two for choosing $u$, three for the reduction of $S$, one for $T$ |
| State and prove the exactness condition | 4 to 6 | 5 minutes | One for the statement, two for the product rule, one for comparing coefficients |
| Reduce a given equation to normal form and solve it | 10 to 12 | 12 minutes | Two for $u$, two for $S$, one for $T$, six for solving and substituting back |
| Solve by a change of the independent variable | 10 to 12 | 12 minutes | One for standard form, two for the condition test, four for the coefficients, five for solving |
| Reduce the order given one solution | 8 to 10 | 9 minutes | One for verifying $y_{1}$, three for the substitution, four for the first-order equation, two for the final answer |
| Solve an exact equation | 6 to 8 | 6 minutes | Two for the test, two for the first integration, four for the first-order solution |

Two consequences follow. First, the derivations are worth as much as the computations, so a candidate who can only solve examples loses roughly half the available marks; the proofs must be learned as sequences of steps, not as formulae. Second, almost every computation contains an identifiable intermediate object, $u$ or $S$ or $z$ or $w$, and most marks sit on that object rather than on the final answer. Writing it down explicitly, in its own display, is worth marks; burying it inside a line of algebra is not.

### 1.2 The definitions to reproduce exactly

> **Definition (second-order linear equation with variable coefficients).** Let $a_{0}$, $a_{1}$, $a_{2}$, $f$ be functions of $x$ on an interval $I$ with $a_{0}(x)\neq 0$ on $I$. An equation
>
> $$
> a_{0}(x)\frac{d^{2}y}{dx^{2}}+a_{1}(x)\frac{dy}{dx}+a_{2}(x)y=f(x)
> $$
>
> is a second-order linear differential equation with variable coefficients.

Marking note: three points are being looked for. The highest derivative is the second, so the order is two. The unknown $y$ and its derivatives occur to the first power and are never multiplied together, so the equation is linear. The coefficients $a_{0}$, $a_{1}$, $a_{2}$ depend on $x$, so the coefficients are variable. An answer that says only "an equation with $x$ in the coefficients" has given the third point and lost the other two.

> **Definition (standard form).** The standard form is
>
> $$
> \frac{d^{2}y}{dx^{2}}+P\frac{dy}{dx}+Qy=R, \qquad P=\frac{a_{1}}{a_{0}}, \quad Q=\frac{a_{2}}{a_{0}}, \quad R=\frac{f}{a_{0}} .
> $$

Marking note: the phrase coefficient of the second derivative is unity is the statement being tested, and the three ratios are the evidence. Every formula in this topic assumes this form, so the division is the first written line of any solution.

> **Definition (normal form).** The normal form of a second-order linear equation is an equation of the shape
>
> $$
> \frac{d^{2}v}{dx^{2}}+Sv=T
> $$
>
> in which the first-derivative term is absent.

Marking note: the defining feature is the absence of the $v'$ term, not the letters used. An answer that produces $v''+P_{1}v'+Sv=T$ with $P_{1}$ not written as zero has not produced a normal form.

> **Definition (exact equation).** The equation $y''+Py'+Qy=R$ is exact if its left-hand side is the derivative of an expression of the form $y'+Ay$.

Marking note: the phrase derivative of a first-order expression is the content. The consequence, that the equation integrates once, is the reason exactness is worth testing.

> **Definition (reduction of order).** Reduction of order is the device that, given one non-zero solution $y_{1}$ of a homogeneous second-order equation, produces the general solution by means of the substitution $y=uy_{1}$.

### 1.3 The coefficient functions and their examination roles

Three functions carry the whole theory, and each is examined in a fixed way.

The coefficient $P$, the multiplier of the first derivative, is the object that Method II removes. Every question of the form "reduce to normal form" begins by extracting $P$ and computing $u=\exp\left(-\frac{1}{2}\int P\,dx\right)$. When $P$ is a power such as $-\frac{2}{x}$ or $-4x$, the integral is immediate and $u$ is a power or an exponential; when $P$ is $-\frac{1}{x}$, the multiplier is $\sqrt{x}$; when $P$ is $-2\tan x$, the multiplier is $\sec x$.

The coefficient $Q$, the multiplier of $y$, is the object that survives in the normal form and controls oscillation. It is also the object that the change of variable normalises, since $Q_{1}=Q/\left(\frac{dz}{dx}\right)^{2}$ and the choice $\frac{dz}{dx}=\sqrt{Q}$ makes $Q_{1}$ equal to one.

The right-hand side $R$ is divided by the same quantities as $Q$ in each transformation: by $u$ in the normal form, by $\left(\frac{dz}{dx}\right)^{2}$ in the change of variable. The most frequent loss of a particular-integral mark is the omission of that division.

### 1.4 The shapes of questions that are asked

| Wording of the question | What is being tested | Standard opening line |
| --- | --- | --- |
| "Write the equation in standard form" | Division by $a_{0}$ | "Divide throughout by the coefficient of $y''$" |
| "Show that the substitution ... reduces the equation to ..." | Chain rule or product rule, with the cancellation displayed | "Let $y=Y(z)$ and compute $\frac{dy}{dx}$ and $\frac{d^{2}y}{dx^{2}}$" |
| "Reduce to normal form and hence solve" | The normal-form theorem plus a constant-coefficient solution | "Here $P=\dots$, so $u=\dots$" |
| "Find the condition for the equation to be exact, and solve it" | The exactness test plus one integration | "Compare $\frac{dP}{dx}$ with $Q$" |
| "Given that $y_{1}$ is a solution, find the general solution" | Reduction of order | "Put $y=uy_{1}$ and differentiate twice" |
| "Show that $y_{1}$ is a solution and find the second solution" | Substitution, then reduction of order | "First verify $y_{1}$ by substitution" |
| "Reduce the equation to an equation with constant coefficients and solve" | Change of the independent variable | "Take $z=\int\sqrt{Q}\,dx$" |

The right-hand column is not decoration. Each opening line is worth its own mark on most schemes, because it demonstrates that the method was chosen rather than guessed, and it makes the subsequent algebra checkable.

### 1.5 The three diagnostics that open every answer

Before choosing a method, compute three quantities. Each costs one line and each is separately marked when it is used.

The exactness diagnostic is $\frac{dP}{dx}$ compared with $Q$. Equality means the equation integrates once and the question collapses; it is the cheapest possible route and must be checked first.

The change-of-variable diagnostic is $Q'+2PQ$, computed only when $Q>0$ and a change of variable is contemplated. Vanishing means the transformed equation is $Y''+Y=R_{1}$ with no first-derivative term at all.

The normal-form diagnostic is $S=Q-\frac{1}{4}P^{2}-\frac{1}{2}\frac{dP}{dx}$. Constant $S$ means the normal form is a constant-coefficient equation; this is the most commonly used diagnostic, because a constant $S$ occurs in a large family of examination questions built from $P$ linear or of the form $k/x$.

Recording the three values in the answer costs three lines and converts a guess into a decision. It also protects against the most expensive error in the topic, which is applying a method whose hypotheses fail and then producing an answer that satisfies nothing.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Theorem 1: the change of the independent variable

> **Theorem 1.** Let $P$, $Q$, $R$ be continuous on an interval $I$ and let $z=z(x)$ be twice continuously differentiable with $z'(x)\neq 0$ on $I$, mapping $I$ one-to-one onto $J$. Setting $y(x)=Y(z(x))$, the equation $y''+Py'+Qy=R$ on $I$ is equivalent to
>
> $$
> \frac{d^{2}Y}{dz^{2}}+P_{1}\frac{dY}{dz}+Q_{1}Y=R_{1}
> $$
>
> on $J$, where
>
> $$
> P_{1}=\frac{\frac{d^{2}z}{dx^{2}}+P\frac{dz}{dx}}{\left(\frac{dz}{dx}\right)^{2}}, \qquad Q_{1}=\frac{Q}{\left(\frac{dz}{dx}\right)^{2}}, \qquad R_{1}=\frac{R}{\left(\frac{dz}{dx}\right)^{2}} .
> $$

This theorem is bookwork worth six to eight marks, and the marks are distributed along the derivation rather than attached to the final display. The two formulas that carry most of the credit are the curvature term in $P_{1}$ and the square in the denominator of all three coefficients; both come from the product rule applied to $\frac{dY}{dz}\cdot\frac{dz}{dx}$.

### 2.2 Corollary: normalising the coefficient of the second-derivative term to one

> **Corollary 1.** Suppose $Q(x)>0$ on $I$ and put $z=\int\sqrt{Q}\,dx$. Then $Q_{1}=1$ and
>
> $$
> P_{1}=\frac{1}{2}\frac{Q'}{Q^{3/2}}+\frac{P}{\sqrt{Q}} .
> $$
>
> If $Q(x)<0$ on $I$, use $z=\int\sqrt{-Q}\,dx$; then $Q_{1}=-1$.

> **Proposition 1 (clean case).** With $z=\int\sqrt{Q}\,dx$ and $Q>0$, $P_{1}$ vanishes identically if and only if
>
> $$
> Q'+2PQ=0 \quad\text{on } I ,
> $$
>
> and then the transformed equation is
>
> $$
> \frac{d^{2}Y}{dz^{2}}+Y=\frac{R}{Q} .
> $$

The clean-case test has a form that is often quicker to verify. Because

$$
\frac{d}{dx}\left(Qe^{2\int P\,dx}\right)=e^{2\int P\,dx}\left(Q'+2PQ\right),
$$

the condition holds exactly when the product of $Q$ with $e^{2\int P\,dx}$ is constant. For an equation whose coefficients satisfy this, the question is essentially finished once $z$ is found.

### 2.3 Theorem 2: the normal form

> **Theorem 2.** Let $P$, $Q$, $R$ be continuous on $I$ and put $u=\exp\left(-\frac{1}{2}\int P\,dx\right)$, which is positive on $I$. Then $y=uv$ solves $y''+Py'+Qy=R$ if and only if $v$ solves
>
> $$
> \frac{d^{2}v}{dx^{2}}+Sv=T, \qquad S=Q-\frac{1}{4}P^{2}-\frac{1}{2}\frac{dP}{dx}, \quad T=\frac{R}{u} .
> $$

> **Corollary 2.** If $S$ is constant the normal form is a constant-coefficient equation and is solved by the characteristic equation together with a particular-integral rule.

Three facts about this theorem are examined repeatedly. The multiplier $u$ is unique up to a constant factor, so the constant of integration in $\int P\,dx$ may be taken as zero. The multiplier never vanishes, so the correspondence between $y$ and $v$ is a bijection and no solution is lost. The coefficient $S$ has three terms, and the third, $-\frac{1}{2}\frac{dP}{dx}$, is the one most often omitted; when it is omitted the resulting equation is wrong and its solutions satisfy neither the normal form nor the original equation.

### 2.4 Theorem 3: the exactness condition

> **Theorem 3.** The equation $y''+Py'+Qy=R$ is exact if and only if
>
> $$
> \frac{dP}{dx}=Q \quad\text{on } I .
> $$
>
> When the condition holds,
>
> $$
> \frac{d}{dx}\left(\frac{dy}{dx}+Py\right)=R ,
> $$
>
> so that
>
> $$
> \frac{dy}{dx}+Py=\int R\,dx+C ,
> $$
>
> which is a first-order linear equation solved by the integrating factor $e^{\int P\,dx}$.

For an equation presented as $a_{0}y''+a_{1}y'+a_{2}y=R$ the same test is

$$
\frac{d^{2}a_{0}}{dx^{2}}-\frac{da_{1}}{dx}+a_{2}=0 .
$$

> **Lemma (operator factorisation).** For differentiable $A$ and $B$,
>
> $$
> \left(D+A\right)\left(D+B\right)[y]=\frac{d^{2}y}{dx^{2}}+\left(A+B\right)\frac{dy}{dx}+\left(\frac{dB}{dx}+AB\right)y .
> $$

Exactness is the case $B=0$, in which the operator becomes $(D+P)D$ and its kernel is $\frac{dy}{dx}+Py=$ constant. The lemma is worth quoting when a question asks why exactness is a condition and not a general property: two conditions, $A+B=P$ and $B'+AB=Q$, are being imposed on two functions.

### 2.5 Theorem 4: reduction of order

> **Theorem 4.** Let $y_{1}$ be a solution of $y''+Py'+Qy=0$ on $I$ with $y_{1}(x)\neq 0$ there. Then $y=uy_{1}$ solves the equation if and only if $w=u'$ solves
>
> $$
> \frac{dw}{dx}+\left(\frac{2y_{1}'}{y_{1}}+P\right)w=0 ,
> $$
>
> and hence
>
> $$
> y=y_{1}\left(C_{1}+C_{2}\int\frac{e^{-\int P\,dx}}{y_{1}^{2}}\,dx\right) .
> $$

The hypothesis $y_{1}\neq 0$ is part of the theorem, not a technicality: the derivation divides by $y_{1}$. The closed formula is a useful check but a poor substitute for the derivation, because the first-order equation in $w$ is normally simpler to integrate than the displayed integral suggests, especially when $y_{1}$ is a power.

### 2.6 High-yield results with their mark values

| Result | Statement | Marks | When it appears |
| --- | --- | --- | --- |
| Standard form | $y''+Py'+Qy=R$ with $P=\frac{a_{1}}{a_{0}}$, $Q=\frac{a_{2}}{a_{0}}$, $R=\frac{f}{a_{0}}$ | 2 | Start of every computation |
| Chain rule pair | $\frac{dy}{dx}=\frac{dY}{dz}\frac{dz}{dx}$ and $\frac{d^{2}y}{dx^{2}}=\frac{d^{2}Y}{dz^{2}}\left(\frac{dz}{dx}\right)^{2}+\frac{dY}{dz}\frac{d^{2}z}{dx^{2}}$ | 2 | Any change of variable |
| Coefficient formulas | $P_{1}$, $Q_{1}$, $R_{1}$ as in Theorem 1 | 3 | Proof of Theorem 1 |
| Clean-case test | $Q'+2PQ=0$ | 2 | Deciding whether a change of variable will work |
| Multiplier | $u=\exp\left(-\frac{1}{2}\int P\,dx\right)$ | 2 | Any normal-form question |
| Coefficient of the normal form | $S=Q-\frac{1}{4}P^{2}-\frac{1}{2}P'$ | 2 | Any normal-form question |
| Forcing of the normal form | $T=\frac{R}{u}$ | 1 | Non-homogeneous normal-form question |
| Exactness test | $P'=Q$ | 2 | Any "is it exact" question |
| Reduction-of-order equation | $w'+\left(\frac{2y_{1}'}{y_{1}}+P\right)w=0$ | 2 | Any "given one solution" question |
| Reduction-of-order formula | $y=y_{1}\left(C_{1}+C_{2}\int\frac{e^{-\int P\,dx}}{y_{1}^{2}}\,dx\right)$ | 2 | When the quadrature is immediate |

The table is the revision list. Each row is a single display that must be reproducible from memory, and each carries the mark value shown. Together the rows account for the bookwork content of the topic.

### 2.7 The standard normal-form families

Most examination equations are built from a small number of coefficient patterns, and for each pattern the multiplier and the resulting $S$ can be written down at once. The table below is computed from $u=\exp\left(-\frac{1}{2}\int P\,dx\right)$ and $S=Q-\frac{1}{4}P^{2}-\frac{1}{2}P'$, with $Q$ left symbolic so that the pattern can be recognised from the coefficient of $y$.

| Pattern for $P$ | Multiplier $u$ | Coefficient $S$ of the normal form |
| --- | --- | --- |
| $P=\frac{a}{x}$ | $u=x^{-a/2}$ | $S=Q+\frac{2a-a^{2}}{4x^{2}}$ |
| $P=-\frac{2}{x}$ | $u=x$ | $S=Q-\frac{2}{x^{2}}$ |
| $P=-\frac{1}{x}$ | $u=\sqrt{x}$ | $S=Q-\frac{3}{4x^{2}}$ |
| $P=-4x$ | $u=e^{x^{2}}$ | $S=Q-4x^{2}+2$ |
| $P=2x$ | $u=e^{-x^{2}}$ | $S=Q-x^{2}-1$ |
| $P=-2\tan x$ | $u=\sec x$ | $S=Q+1$ |

The rows are not independent: each is a special case of the first, or a direct substitution into the formula. Two of them account for the majority of questions. The row with $P=-\frac{2}{x}$ occurs whenever the equation carries a term $-\frac{2}{x}y'$, and its multiplier is a single power, so the substituted equation is short. The row with $P=-4x$ or $P=2x$ occurs whenever a Gaussian factor appears in the forcing, and the division $T=R/u$ then cancels that factor exactly.

Reading the table backwards is the practical skill. If a question presents $Q=25+\frac{2}{x^{2}}$ together with $P=-\frac{2}{x}$, the third column gives $S=25+\frac{2}{x^{2}}-\frac{2}{x^{2}}=25$, a constant, so the normal form is $v''+25v=0$ and the answer is a cosine-sine pair multiplied by $x$. That single observation replaces several lines of computation and is the reason the table is worth memorising.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of Theorem 1, with the marks marked

Step 1. Let $y(x)=Y(z(x))$ and apply the chain rule once. *(1 mark)*

$$
\frac{dy}{dx}=\frac{dY}{dz}\cdot\frac{dz}{dx}
$$

Step 2. Differentiate this product with respect to $x$. *(1 mark)*

$$
\frac{d^{2}y}{dx^{2}}=\frac{d}{dx}\left(\frac{dY}{dz}\right)\frac{dz}{dx}+\frac{dY}{dz}\frac{d^{2}z}{dx^{2}}
$$

Step 3. Expand the first factor by the chain rule, since $\frac{dY}{dz}$ is a function of $z$. *(1 mark)*

$$
\frac{d}{dx}\left(\frac{dY}{dz}\right)=\frac{d^{2}Y}{dz^{2}}\frac{dz}{dx}
$$

Step 4. Combine Steps 2 and 3 into the single formula for the second derivative. *(1 mark for the curvature term)*

$$
\frac{d^{2}y}{dx^{2}}=\frac{d^{2}Y}{dz^{2}}\left(\frac{dz}{dx}\right)^{2}+\frac{dY}{dz}\frac{d^{2}z}{dx^{2}}
$$

Step 5. Substitute both derivatives into $y''+Py'+Qy=R$. *(1 mark)*

$$
\left(\frac{dz}{dx}\right)^{2}\frac{d^{2}Y}{dz^{2}}+\left(\frac{d^{2}z}{dx^{2}}+P\frac{dz}{dx}\right)\frac{dY}{dz}+QY=R
$$

Step 6. Divide by $\left(\frac{dz}{dx}\right)^{2}$, which is not zero because $z'\neq 0$. *(1 mark)*

$$
\frac{d^{2}Y}{dz^{2}}+\frac{\frac{d^{2}z}{dx^{2}}+P\frac{dz}{dx}}{\left(\frac{dz}{dx}\right)^{2}}\frac{dY}{dz}+\frac{Q}{\left(\frac{dz}{dx}\right)^{2}}Y=\frac{R}{\left(\frac{dz}{dx}\right)^{2}}
$$

Step 7. Identify the three coefficients. *(1 mark)*

$$
P_{1}=\frac{\frac{d^{2}z}{dx^{2}}+P\frac{dz}{dx}}{\left(\frac{dz}{dx}\right)^{2}}, \qquad Q_{1}=\frac{Q}{\left(\frac{dz}{dx}\right)^{2}}, \qquad R_{1}=\frac{R}{\left(\frac{dz}{dx}\right)^{2}}
$$

Total for the proof: 7 marks. The step that is most often lost is Step 3, because the differentiability of $\frac{dY}{dz}$ with respect to $x$ is easy to take for granted; the step that is most often wrong is Step 6, where the square is dropped.

### 3.2 Derivation of Corollary 1 and the clean case

Step 1. Set $Q_{1}=1$ in Theorem 1 and solve for the scale factor. *(1 mark)*

$$
\left(\frac{dz}{dx}\right)^{2}=Q, \qquad \frac{dz}{dx}=\sqrt{Q}
$$

Step 2. Integrate to obtain the new variable. *(1 mark)*

$$
z=\int\sqrt{Q}\,dx
$$

Step 3. Differentiate $\frac{dz}{dx}=\sqrt{Q}$ once more. *(1 mark)*

$$
\frac{d^{2}z}{dx^{2}}=\frac{Q'}{2\sqrt{Q}}
$$

Step 4. Substitute both into $P_{1}$ and simplify. *(2 marks)*

$$
P_{1}=\frac{\frac{Q'}{2\sqrt{Q}}+P\sqrt{Q}}{Q}=\frac{Q'}{2Q^{3/2}}+\frac{P}{\sqrt{Q}}
$$

Step 5. Impose $P_{1}=0$ and multiply by $2Q^{3/2}$. *(1 mark)*

$$
Q'+2PQ=0
$$

Step 6. State the transformed equation, with $Q_{1}=1$ and $P_{1}=0$. *(1 mark)*

$$
\frac{d^{2}Y}{dz^{2}}+Y=\frac{R}{Q}
$$

Total: 7 marks. Note that Step 6 requires $R_{1}=R/Q$ to be expressed in $z$ before the equation is usable, and that conversion is usually a separate mark in a computation question.

### 3.3 Proof of Theorem 2

Step 1. Write $y=uv$ and differentiate once. *(1 mark)*

$$
\frac{dy}{dx}=u\frac{dv}{dx}+v\frac{du}{dx}
$$

Step 2. Differentiate again. *(2 marks)*

$$
\frac{d^{2}y}{dx^{2}}=u\frac{d^{2}v}{dx^{2}}+2\frac{du}{dx}\frac{dv}{dx}+v\frac{d^{2}u}{dx^{2}}
$$

Step 3. Substitute into the standard form and group by derivatives of $v$. *(1 mark)*

$$
u\frac{d^{2}v}{dx^{2}}+\left(2\frac{du}{dx}+Pu\right)\frac{dv}{dx}+\left(\frac{d^{2}u}{dx^{2}}+P\frac{du}{dx}+Qu\right)v=R
$$

Step 4. Choose $u$ so that the coefficient of $\frac{dv}{dx}$ vanishes. *(1 mark for the choice, 1 for solving it)*

$$
2\frac{du}{dx}+Pu=0, \qquad u=\exp\left(-\frac{1}{2}\int P\,dx\right)
$$

Step 5. Divide by $u$, which is legitimate because $u>0$. *(1 mark)*

$$
\frac{d^{2}v}{dx^{2}}+\frac{1}{u}\left(\frac{d^{2}u}{dx^{2}}+P\frac{du}{dx}+Qu\right)v=\frac{R}{u}
$$

Step 6. Compute the derivatives of $u$ from the choice made in Step 4. *(1 mark)*

$$
\frac{du}{dx}=-\frac{P}{2}u, \qquad \frac{d^{2}u}{dx^{2}}=\left(\frac{P^{2}}{4}-\frac{P'}{2}\right)u
$$

Step 7. Substitute into the bracket and collect terms. *(2 marks)*

$$
\frac{d^{2}u}{dx^{2}}+P\frac{du}{dx}+Qu=u\left(Q-\frac{P^{2}}{4}-\frac{P'}{2}\right)
$$

Step 8. Divide by $u$ and read off $S$ and $T$. *(1 mark)*

$$
\frac{d^{2}v}{dx^{2}}+\left(Q-\frac{P^{2}}{4}-\frac{P'}{2}\right)v=\frac{R}{u}
$$

Total: 11 marks. The three marks in Steps 6 and 7 are the ones that separate a full-mark answer from a half-mark answer, because they are the algebra that produces the coefficient $S$ rather than merely quoting it.

### 3.4 Proof of the exactness condition

Step 1. Expand the derivative of a first-order expression. *(1 mark)*

$$
\frac{d}{dx}\left(\frac{dy}{dx}+Ay\right)=\frac{d^{2}y}{dx^{2}}+A\frac{dy}{dx}+\frac{dA}{dx}y
$$

Step 2. Compare coefficients with $y''+Py'+Qy$. *(2 marks)*

$$
A=P, \qquad \frac{dA}{dx}=Q
$$

Step 3. Eliminate $A$ to obtain the necessary condition. *(1 mark)*

$$
\frac{dP}{dx}=Q
$$

Step 4. Prove sufficiency by computing the derivative when the condition holds. *(1 mark)*

$$
\frac{d}{dx}\left(\frac{dy}{dx}+Py\right)=\frac{d^{2}y}{dx^{2}}+P\frac{dy}{dx}+Qy
$$

Step 5. Integrate once to obtain the equivalent first-order equation. *(1 mark)*

$$
\frac{dy}{dx}+Py=\int R\,dx+C
$$

Total: 6 marks. For the general form the comparison is made with $\frac{d}{dx}\left(a_{0}y'+By\right)$, giving $B=a_{1}-a_{0}'$ and then $a_{0}''-a_{1}'+a_{2}=0$; that variant is worth the same and is examined in the same way.

### 3.5 Derivation of reduction of order

Step 1. Put $y=uy_{1}$ and differentiate twice. *(2 marks)*

$$
\frac{dy}{dx}=u'y_{1}+uy_{1}', \qquad \frac{d^{2}y}{dx^{2}}=u''y_{1}+2u'y_{1}'+uy_{1}''
$$

Step 2. Substitute into the homogeneous equation and group. *(1 mark)*

$$
u''y_{1}+u'\left(2y_{1}'+Py_{1}\right)+u\left(y_{1}''+Py_{1}'+Qy_{1}\right)=0
$$

Step 3. Use the hypothesis on $y_{1}$ to kill the term in $u$. *(1 mark)*

$$
y_{1}''+Py_{1}'+Qy_{1}=0
$$

Step 4. Divide by $y_{1}$ and obtain an equation with no $u$ term. *(1 mark)*

$$
u''+\left(\frac{2y_{1}'}{y_{1}}+P\right)u'=0
$$

Step 5. Put $w=u'$ and separate. *(2 marks)*

$$
\frac{dw}{dx}+\left(\frac{2y_{1}'}{y_{1}}+P\right)w=0, \qquad w=\frac{C_{2}e^{-\int P\,dx}}{y_{1}^{2}}
$$

Step 6. Integrate once more and multiply by $y_{1}$. *(1 mark)*

$$
y=y_{1}\left(C_{1}+C_{2}\int\frac{e^{-\int P\,dx}}{y_{1}^{2}}\,dx\right)
$$

Total: 8 marks. The step worth the most is Step 5, because the integrating factor there is $\frac{1}{y_{1}^{2}}e^{-\int P\,dx}$ and the two factors are frequently separated incorrectly.

### 3.6 How to lay out an answer so that the marks are visible

For a "reduce to normal form and hence solve" question, the layout that scores is: standard form; the values of $P$, $Q$, $R$; the computation of $\frac{1}{2}\int P\,dx$ and the multiplier $u$; the computation of $P^{2}$ and $P'$; the computation of $S$ with its three terms visible; the computation of $T$; the normal form written out; the complementary function; the particular integral; the product $y=uv$; the verification.

For a "change the independent variable" question the layout is: standard form; $P$, $Q$, $R$; the test $Q'+2PQ$; the choice of $z$ and its derivatives; the three transformed coefficients; the transformed equation; its solution; the substitution back to $x$; the verification.

For a "given one solution" question the layout is: verification of $y_{1}$; the substitution and its two derivatives; the grouped equation; the cancellation displayed; the first-order equation in $w$; its solution; the integration to $u$; the final product; the count of constants.

In all three layouts the principle is the same: one display per algebraic stage, with the prose saying only what the stage does and why it is allowed. An examiner cannot award a mark for a step that is buried in a paragraph.

## 4. Representative Worked Examples and Solutions

### 4.1 Model solution A: reduce to normal form and solve (12 marks)

Solve

$$
\frac{d^{2}y}{dx^{2}}-4x\frac{dy}{dx}+\left(4x^{2}-3\right)y=xe^{x^{2}} .
$$

### 4.2 Solution: the multiplier is a Gaussian, and the normal form has $S=-1$

Step 1. The equation is already in standard form, so read off the three coefficient functions. *(1 mark)*

$$
P=-4x, \qquad Q=4x^{2}-3, \qquad R=xe^{x^{2}}
$$

Step 2. Compute the exponent of the multiplier. *(1 mark)*

$$
-\frac{1}{2}\int P\,dx=-\frac{1}{2}\int\left(-4x\right)dx=\int 2x\,dx=x^{2}
$$

Step 3. State the multiplier and the substitution. *(1 mark)*

$$
u=e^{x^{2}}, \qquad y=e^{x^{2}}v
$$

Step 4. Compute the two ingredients of $S$. *(1 mark)*

$$
P^{2}=16x^{2}, \qquad \frac{dP}{dx}=-4
$$

Step 5. Compute $S$ with all three terms visible. *(2 marks)*

$$
S=4x^{2}-3-\frac{16x^{2}}{4}-\frac{1}{2}\left(-4\right)=4x^{2}-3-4x^{2}+2=-1
$$

Step 6. Compute $T$, dividing the forcing by the multiplier. *(1 mark)*

$$
T=\frac{xe^{x^{2}}}{e^{x^{2}}}=x
$$

Step 7. Write the normal form. *(1 mark)*

$$
\frac{d^{2}v}{dx^{2}}-v=x
$$

Step 8. Solve the complementary function from $m^{2}-1=0$. *(1 mark)*

$$
v_{c}=c_{1}e^{x}+c_{2}e^{-x}
$$

Step 9. Find a particular integral by trying $v=ax$. *(2 marks)*

$$
0-ax=x\quad\text{for all }x, \qquad a=-1, \qquad v_{p}=-x
$$

Step 10. Assemble $v$ and multiply by $u$. *(1 mark)*

$$
y=e^{x^{2}}\left(c_{1}e^{x}+c_{2}e^{-x}-x\right)
$$

Step 11. Verify the particular integral in the original equation. With $y_{p}=-xe^{x^{2}}$ the derivatives are $y_{p}'=-e^{x^{2}}\left(1+2x^{2}\right)$ and $y_{p}''=-e^{x^{2}}\left(6x+4x^{3}\right)$, so *(1 mark)*

$$
-e^{x^{2}}\left(6x+4x^{3}\right)+4xe^{x^{2}}\left(1+2x^{2}\right)-x\left(4x^{2}-3\right)e^{x^{2}}=e^{x^{2}}\left(-6x+4x+3x\right)=xe^{x^{2}} .
$$

Total: 12 marks. The final display carries two arbitrary constants, as a second-order equation requires, and the verification confirms the particular integral exactly.

### 4.3 Model solution B: change the independent variable (12 marks)

Solve

$$
x\frac{d^{2}y}{dx^{2}}-\frac{dy}{dx}+4x^{3}y=x^{5}
$$

for $x>0$.

### 4.4 Solution: $z=x^{2}$ turns the equation into $Y''+Y=\frac{z}{4}$

Step 1. Put the equation in standard form. *(1 mark)*

$$
\frac{d^{2}y}{dx^{2}}-\frac{1}{x}\frac{dy}{dx}+4x^{2}y=x^{4}
$$

Step 2. Read off the coefficients. *(1 mark)*

$$
P=-\frac{1}{x}, \qquad Q=4x^{2}, \qquad R=x^{4}
$$

Step 3. Test the clean-case condition. *(2 marks)*

$$
Q'=8x, \qquad Q'+2PQ=8x+2\left(-\frac{1}{x}\right)\left(4x^{2}\right)=8x-8x=0
$$

Step 4. Choose the new variable from $\frac{dz}{dx}=\sqrt{Q}$. *(1 mark)*

$$
\frac{dz}{dx}=2x, \qquad z=x^{2}
$$

Step 5. Compute the squared scale factor and the curvature. *(1 mark)*

$$
\left(\frac{dz}{dx}\right)^{2}=4x^{2}, \qquad \frac{d^{2}z}{dx^{2}}=2
$$

Step 6. Compute $P_{1}$. *(2 marks)*

$$
P_{1}=\frac{2+\left(-\frac{1}{x}\right)\left(2x\right)}{4x^{2}}=\frac{2-2}{4x^{2}}=0
$$

Step 7. Compute $Q_{1}$ and $R_{1}$, expressing the latter in $z$. *(2 marks)*

$$
Q_{1}=\frac{4x^{2}}{4x^{2}}=1, \qquad R_{1}=\frac{x^{4}}{4x^{2}}=\frac{x^{2}}{4}=\frac{z}{4}
$$

Step 8. Write the transformed equation. *(1 mark)*

$$
\frac{d^{2}Y}{dz^{2}}+Y=\frac{z}{4}
$$

Step 9. Solve it: the complementary function has roots $\pm i$ and a linear particular integral works. *(1 mark for the complementary function, 1 for the particular integral)*

$$
Y=c_{1}\cos z+c_{2}\sin z+\frac{z}{4}
$$

Step 10. Return to the original variable. *(1 mark)*

$$
y=c_{1}\cos\left(x^{2}\right)+c_{2}\sin\left(x^{2}\right)+\frac{x^{2}}{4}
$$

Total: 12 marks. Verify the particular integral: with $y=\frac{x^{2}}{4}$ the derivatives are $\frac{x}{2}$ and $\frac{1}{2}$, so $x\cdot\frac{1}{2}-\frac{x}{2}+4x^{3}\cdot\frac{x^{2}}{4}=x^{5}$, as required. The complementary solutions satisfy the homogeneous equation because $-2x\sin\left(x^{2}\right)-4x^{2}\cos\left(x^{2}\right)$ from the second derivative is cancelled by the two remaining terms, a cancellation worth writing out in a long answer.

### 4.5 Model solution C: reduction of order (10 marks)

Given that $y=x^{3}$ is a solution of

$$
\frac{d^{2}y}{dx^{2}}-\frac{1}{x}\frac{dy}{dx}-\frac{3}{x^{2}}y=0 ,
$$

find the general solution for $x>0$.

### 4.6 Solution: the substitution leaves $u''+\frac{3}{x}u'=0$

Step 1. Verify the supplied solution. With $y_{1}=x^{3}$ the derivatives are $3x^{2}$ and $6x$, so *(1 mark)*

$$
6x-\frac{1}{x}\cdot 3x^{2}-\frac{3}{x^{2}}\cdot x^{3}=6x-3x-3x=0 .
$$

Step 2. Put $y=x^{3}u$ and differentiate twice. *(2 marks)*

$$
\frac{dy}{dx}=3x^{2}u+x^{3}u', \qquad \frac{d^{2}y}{dx^{2}}=6xu+6x^{2}u'+x^{3}u''
$$

Step 3. Substitute into the equation. *(1 mark)*

$$
6xu+6x^{2}u'+x^{3}u''-3xu-3x^{2}u'-\frac{3}{x^{2}}x^{3}u=0
$$

Step 4. Display the cancellation of the terms in $u$. *(1 mark)*

$$
\left(6x-3x-3x\right)u=0
$$

Step 5. Write the surviving equation. *(1 mark)*

$$
x^{3}u''+3x^{2}u'=0
$$

Step 6. Divide by $x^{3}$ and put $w=u'$. *(1 mark)*

$$
\frac{dw}{dx}+\frac{3}{x}w=0
$$

Step 7. Solve the first-order equation by separation. *(2 marks)*

$$
\frac{1}{w}\frac{dw}{dx}=-\frac{3}{x}, \qquad w=C_{2}x^{-3}
$$

Step 8. Integrate to obtain $u$ and multiply by $y_{1}$. *(1 mark)*

$$
u=C_{1}-\frac{C_{2}}{2x^{2}}, \qquad y=C_{1}x^{3}-\frac{C_{2}}{2x}
$$

Step 9. State the answer with the constants renamed. *(1 mark)*

$$
y=Ax^{3}+\frac{B}{x}
$$

Total: 10 marks. The second solution can be checked directly: with $y=\frac{1}{x}$ the derivatives are $-\frac{1}{x^{2}}$ and $\frac{2}{x^{3}}$, and $\frac{2}{x^{3}}+\frac{1}{x^{3}}-\frac{3}{x^{3}}=0$. The powers $3$ and $-1$ are the roots of the indicial equation $m(m-1)-m-3=0$, so the answer is consistent with the Euler structure of the equation.

### 4.7 Model solution D: exactness (8 marks)

Solve

$$
\frac{d^{2}y}{dx^{2}}+\frac{1}{x}\frac{dy}{dx}-\frac{1}{x^{2}}y=0
$$

for $x>0$.

### 4.8 Solution: the left side is the derivative of $y'+\frac{y}{x}$

Step 1. Read off $P$ and $Q$ and differentiate $P$. *(1 mark)*

$$
P=\frac{1}{x}, \qquad Q=-\frac{1}{x^{2}}, \qquad \frac{dP}{dx}=-\frac{1}{x^{2}}
$$

Step 2. Compare the derivative with $Q$ and state the conclusion. *(2 marks)*

$$
\frac{dP}{dx}=Q \quad\text{so the equation is exact}
$$

Step 3. Rewrite the equation as a single derivative. *(1 mark)*

$$
\frac{d}{dx}\left(\frac{dy}{dx}+\frac{1}{x}y\right)=0
$$

Step 4. Integrate once. *(1 mark)*

$$
\frac{dy}{dx}+\frac{1}{x}y=C_{1}
$$

Step 5. Multiply by the integrating factor $x$ and integrate again. *(2 marks)*

$$
\frac{d}{dx}\left(xy\right)=C_{1}x, \qquad xy=\frac{C_{1}}{2}x^{2}+C_{2}
$$

Step 6. Divide by $x$ and rename the constants. *(1 mark)*

$$
y=Ax+\frac{B}{x}
$$

Total: 8 marks. Both solutions check directly: for $y=x$ the left side is $0+\frac{1}{x}-\frac{1}{x}=0$, and for $y=\frac{1}{x}$ it is $\frac{2}{x^{3}}-\frac{1}{x^{3}}-\frac{1}{x^{3}}=0$.

### 4.9 Model solution E: a substitution question (6 marks)

Show that the substitution $y=xv$ reduces

$$
\frac{d^{2}y}{dx^{2}}-\frac{2}{x}\frac{dy}{dx}+\left(1+\frac{2}{x^{2}}\right)y=0
$$

to $v''+v=0$, and hence solve the equation.

### 4.10 Solution: differentiate the substitution and cancel

Step 1. State the coefficients and note that the required multiplier satisfies $\frac{u'}{u}=-\frac{P}{2}$. *(1 mark)*

$$
P=-\frac{2}{x}, \qquad \frac{u'}{u}=\frac{1}{x}, \qquad u=x
$$

Step 2. Differentiate $y=xv$ twice. *(1 mark)*

$$
\frac{dy}{dx}=v+xv', \qquad \frac{d^{2}y}{dx^{2}}=2v'+xv''
$$

Step 3. Substitute into the equation. *(1 mark)*

$$
2v'+xv''-\frac{2}{x}\left(v+xv'\right)+\left(1+\frac{2}{x^{2}}\right)xv=0
$$

Step 4. Expand and cancel the pairs with opposite signs. *(2 marks)*

$$
2v'+xv''-\frac{2v}{x}-2v'+xv+\frac{2v}{x}=0 \quad\text{gives}\quad xv''+xv=0
$$

Step 5. Divide by $x$ and solve. *(1 mark)*

$$
v''+v=0, \qquad v=c_{1}\cos x+c_{2}\sin x, \qquad y=x\left(c_{1}\cos x+c_{2}\sin x\right)
$$

Total: 6 marks. The point of the question is the cancellation in Step 4: the two terms in $v'$ and the two terms in $v$ over $x$ disappear in pairs, and displaying that cancellation is what earns the marks.

### 4.11 Model solution F: the logarithmic change of variable (10 marks)

Solve

$$
x^{2}\frac{d^{2}y}{dx^{2}}-3x\frac{dy}{dx}+4y=0
$$

for $x>0$ by changing the independent variable, and state why the answer has the shape it does.

### 4.12 Solution: $z=2\ln x$ produces a repeated root

Step 1. Put the equation in standard form and read off the coefficients. *(1 mark)*

$$
\frac{d^{2}y}{dx^{2}}-\frac{3}{x}\frac{dy}{dx}+\frac{4}{x^{2}}y=0, \qquad P=-\frac{3}{x}, \quad Q=\frac{4}{x^{2}}, \quad R=0
$$

Step 2. Note that $Q>0$ for $x>0$, take its square root and integrate to obtain the new variable. *(2 marks)*

$$
\frac{dz}{dx}=\sqrt{Q}=\frac{2}{x}, \qquad z=\int\frac{2}{x}\,dx=2\ln x
$$

Step 3. Compute the squared scale factor and the curvature of the new variable. *(1 mark)*

$$
\left(\frac{dz}{dx}\right)^{2}=\frac{4}{x^{2}}, \qquad \frac{d^{2}z}{dx^{2}}=-\frac{2}{x^{2}}
$$

Step 4. Compute $P_{1}$ from Theorem 1. *(2 marks)*

$$
P_{1}=\frac{-\frac{2}{x^{2}}+\left(-\frac{3}{x}\right)\left(\frac{2}{x}\right)}{\frac{4}{x^{2}}}=\frac{-\frac{8}{x^{2}}}{\frac{4}{x^{2}}}=-2
$$

Step 5. Compute $Q_{1}$ and note that it is a constant, so the new equation has constant coefficients. *(1 mark)*

$$
Q_{1}=\frac{\frac{4}{x^{2}}}{\frac{4}{x^{2}}}=1
$$

Step 6. Write the transformed equation. *(1 mark)*

$$
\frac{d^{2}Y}{dz^{2}}-2\frac{dY}{dz}+Y=0
$$

Step 7. Solve it. The characteristic equation is $m^{2}-2m+1=(m-1)^{2}=0$, a repeated root at $m=1$. *(1 mark)*

$$
Y=\left(c_{1}+c_{2}z\right)e^{z}
$$

Step 8. Return to $x$, using $z=2\ln x$ and $e^{z}=e^{2\ln x}=x^{2}$. *(1 mark)*

$$
y=x^{2}\left(c_{1}+2c_{2}\ln x\right)
$$

Step 9. Explain the shape of the answer and verify the logarithmic solution. The repeated root is what produces the factor $\ln x$, exactly as a repeated root produces a factor $z$ in the constant-coefficient case; substituting $y=x^{2}\ln x$ gives

$$
x^{2}\left(2\ln x+3\right)-3x\left(2x\ln x+x\right)+4x^{2}\ln x=\left(2-6+4\right)x^{2}\ln x+\left(3-3\right)x^{2}=0 .
$$

*(1 mark)*

Total: 10 marks. The general statement behind the computation is worth a line in any answer: for $x^{2}y''+axy'+by=0$ with $b>0$, the substitution $z=\sqrt{b}\ln x$ produces the constant-coefficient equation

$$
\frac{d^{2}Y}{dz^{2}}+\frac{a-1}{\sqrt{b}}\frac{dY}{dz}+Y=0 ,
$$

so an Euler equation is a constant-coefficient equation viewed through a logarithmic scale. Here $a=-3$ and $b=4$, so the middle coefficient is $\frac{-4}{2}=-2$, in agreement with Step 4.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The trap table

The errors below are the ones that actually cost marks, listed roughly in order of frequency. Every one of them has been produced by a candidate who knew the method; they are slips of execution, not gaps in understanding, which is why they are worth reading the night before the paper.

| Trap | What it looks like | Correct handling |
| --- | --- | --- |
| Applying a formula before dividing by $a_{0}$ | Using $Q=a_{2}$ in an equation with $a_{0}=2x^{2}$ | Divide first, then read $P$, $Q$, $R$ from the standard form |
| Omitting the curvature term | Writing $y''=\frac{d^{2}Y}{dz^{2}}\left(\frac{dz}{dx}\right)^{2}$ only | The product rule gives $\frac{dY}{dz}\frac{d^{2}z}{dx^{2}}$ as well |
| Dropping the square in $Q_{1}$ | Using $Q_{1}=\frac{Q}{z'}$ | The formula is $Q_{1}=\frac{Q}{\left(z'\right)^{2}}$ |
| Using the wrong sign in the exponent of $u$ | $u=\exp\left(+\frac{1}{2}\int P\,dx\right)$ | The exponent is $-\frac{1}{2}\int P\,dx$, which is what makes the $v'$ term vanish |
| Omitting $-\frac{1}{2}P'$ from $S$ | Writing $S=Q-\frac{1}{4}P^{2}$ | All three terms are required; the derivative term is nonzero whenever $P$ is not constant |
| Taking $T=R$ | Omitting the division by $u$ | $T=\frac{R}{u}$, and $u$ is an exponential or a power |
| Taking a real square root of a negative $Q$ | Writing $z=\int\sqrt{Q}\,dx$ when $Q<0$ | Use $z=\int\sqrt{-Q}\,dx$, which gives $Q_{1}=-1$ |
| Leaving the answer in $Y$ or $v$ | A final line containing $\cos z$ | The question asks for $y$ in terms of $x$ |
| Losing a constant | A second-order answer with one constant | Two integrations give two constants, one each |
| Treating exactness as automatic | Asserting the equation is exact without testing | Display $\frac{dP}{dx}$ and compare it with $Q$ |
| Dividing by $y_{1}$ without stating $y_{1}\neq 0$ | Reducing order in a question where $y_{1}$ vanishes at a point | State the interval on which $y_{1}$ is nonzero |
| Verifying at a point only | Substituting $x=0$ and concluding | Verification requires an identity in $x$ on the interval |
| Mixing the two methods in one step | Using $z$ and $u$ together without comment | The two devices are alternatives; choose one and say so |
| Forgetting to convert $R_{1}$ to $z$ | Writing $R_{1}=x^{4}/4$ in an equation in $z$ | Substitute $x^{2}=z$ to obtain $R_{1}=z/4$ |
| Reporting a constant $S$ without checking | Declaring $S$ constant after cancelling incorrectly | Recompute $S$ from its three terms before using Corollary 2 |

### 5.2 What the methods cannot do

The three devices are exact transformations, so they never produce a false solution; but they do not always produce a usable equation. A change of variable always gives a correct new equation, and that equation may be as hard as the original. The normal form always exists, and its coefficient $S$ is usually not a constant, in which case the normal form is not solvable by the characteristic equation. Exactness requires the identity $P'=Q$, which usually fails.

A worked comparison makes the boundary clear. For the equation of Section 4.3 the normal form coefficient is

$$
S=4x^{2}-\frac{3}{4x^{2}},
$$

which is not constant, so Method II would fail there; the change of variable $z=x^{2}$ solves the same equation immediately. For the equation of Section 4.1 the clean-case quantity is

$$
Q'+2PQ=8x-8x\left(4x^{2}-3\right),
$$

which is not zero, so Method I would fail there; the normal form has $S=-1$ and succeeds. The two methods divide the territory between them, and the diagnostics of Section 1.5 decide which side of the boundary a given equation lies on.

### 5.3 Revision checklist

Each item should take under a minute and corresponds to marks that are regularly lost.

- I can state the general form of a second-order linear equation with variable coefficients, naming the three coefficient functions and the condition on the leading coefficient.
- I can convert any given equation into standard form and justify the division.
- I can write the chain-rule formulas for $\frac{dy}{dx}$ and $\frac{d^{2}y}{dx^{2}}$ when $x$ is replaced by $z(x)$, including the curvature term.
- I can reproduce the formulas for $P_{1}$, $Q_{1}$, $R_{1}$ from memory.
- I can derive them from scratch in seven steps, and I know which step carries which mark.
- I can choose $z=\int\sqrt{Q}\,dx$, compute $P_{1}$, and decide whether the resulting equation has constant coefficients.
- I can test $Q'+2PQ=0$ and state what it gives.
- I can compute $u=\exp\left(-\frac{1}{2}\int P\,dx\right)$ for $P$ a power, a multiple of $x$, a tangent, or a sum.
- I can compute $S=Q-\frac{1}{4}P^{2}-\frac{1}{2}P'$ and $T=\frac{R}{u}$ without losing a term.
- I can solve $v''+Sv=T$ for constant $S$ in all three root cases.
- I can test exactness and integrate an exact equation once to a first-order equation.
- I can carry out reduction of order from a supplied solution, displaying the cancellation of the $u$ term.
- I can verify any final answer by substitution and count its constants against the order.
- I know the interval on which each answer is valid, including the sign condition on $x$ for logarithms.

### 5.4 Time strategy

The topic is usually worth between twelve and twenty marks on a paper, so it deserves between twelve and twenty minutes. A workable allocation for a twenty-mark question in two parts is as follows.

Spend two minutes reading the whole question and marking which parts are bookwork. Bookwork is answered first, because the marks are certain and because writing the derivation settles the notation for the computation.

Spend three minutes on a derivation if one is asked for. Seven lines for Theorem 1, eleven for Theorem 2: the count is known in advance, and writing one display per step prevents the compression that loses marks.

Spend one minute on the diagnostics. Write down $\frac{dP}{dx}$, $Q'+2PQ$, and $S$ before choosing a method. This minute is what distinguishes a chosen method from a guessed one, and it is frequently worth a mark by itself.

Spend eight minutes on the main computation. Compute $u$ or $z$, then the transformed coefficients, then the transformed equation, then its solution, then the substitution back. Do not skip the display of the transformed equation: it is usually a mark on its own, and it is the only check that the coefficients were assembled correctly.

Spend three minutes on the particular integral and the final assembly. A particular integral for a polynomial forcing is linear or quadratic, and for an exponential forcing it is a multiple of the exponential; decide the trial form from the forcing and substitute.

Spend the final three minutes checking. Substitute the final answer, or at least its particular integral, into the original equation; count the constants; confirm that the answer is written in $x$. These three minutes recover more marks than any amount of re-reading, because they catch the two errors that are otherwise invisible: a sign in the exponent of $u$, and an omitted term in $S$.

A final piece of strategy concerns partial credit. The marks are attached to displayed intermediates, so an unfinished solution written one step per display scores more than a finished one compressed into a paragraph. When time runs short, write the multiplier, the coefficient $S$, and the transformed equation rather than nothing at all.

### 5.5 The last-minute summary

Four devices, one diagnostic each. Exactness: does $\frac{dP}{dx}$ equal $Q$? If yes, integrate once. Change of variable: is $Q'+2PQ$ zero, or is $P_{1}$ constant for $z=\int\sqrt{Q}\,dx$? If yes, solve in $z$ and return to $x$. Normal form: is $S=Q-\frac{1}{4}P^{2}-\frac{1}{2}P'$ constant? If yes, take $u=\exp\left(-\frac{1}{2}\int P\,dx\right)$, solve $v''+Sv=\frac{R}{u}$, and multiply by $u$. Reduction of order: is one non-zero solution supplied? If yes, put $y=uy_{1}$ and solve the first-order equation for $u'$.

Whichever device is used, the same three sentences close the answer: the transformed equation is displayed, the solution in the original variable is written with two arbitrary constants, and one component of it is substituted back. Every mark in the topic is attached to one of those sentences or to the algebra that produces it.
