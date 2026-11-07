## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What the examiner is testing

Every question on this topic is built from three separable skills, and the marks are allocated to them in a predictable way. The first skill is recognition: deciding whether the equation is linear, Bernoulli, or reducible by exchanging the variables. The second is the construction of the integrating factor, which is a short computation with a single point of failure, namely the integral of the coefficient. The third is the execution of the integration that produces the solution, together with the imposition of any initial condition and the statement of the interval.

The standard form around which everything is organised is

$$
\frac{dy}{dx}+P(x)\,y=Q(x),
$$

with $P$ and $Q$ continuous on the interval of interest. The integrating factor is

$$
\mu(x)=e^{\int P(x)\,dx},
$$

and the solution is obtained from

$$
\mu y=\int \mu Q\,dx+C .
$$

Those three displayed lines, correctly used, are worth most of the marks on any question in the topic. What follows in this section is the recognition apparatus; Sections 2 and 3 supply the results and their justification; Section 4 gives complete model solutions with the marks shown step by step; Section 5 gives the trap table, the revision checklist and the timing plan.

### 1.2 The high-yield results and their mark values

The table lists the results that are examined directly, with the marks typically attached to them in a first-year course. The mark values are indicative rather than universal, but the relative weighting is stable: derivations and complete solutions carry more than statements, and the integrating factor itself is usually a single mark.

| Result | Statement | Typical marks |
| --- | --- | --- |
| Recognition of standard form | Write $\frac{dy}{dx}+Py=Q$ and name $P$ and $Q$ | 1 to 2 |
| Integrating factor | $\mu=e^{\int P\,dx}$ | 1 to 2 |
| Product form | $\frac{d}{dx}\left(\mu y\right)=\mu Q$ | 1 |
| General solution | $\mu y=\int \mu Q\,dx+C$ | 2 to 3 |
| Bernoulli reduction | $v=y^{1-n}$ gives $v'+(1-n)Pv=(1-n)Q$ | 3 to 5 |
| Degenerate cases | $n=0$ linear, $n=1$ separable | 1 to 2 |
| Zero solution | $y\equiv 0$ solves when $n>0$ | 1 |
| Reciprocal form | $x$ as unknown gives $x'+Ax=B$ | 2 |
| Initial condition | Determine $C$ and state the interval | 1 to 2 |
| Verification | Substitute back and simplify | 1 to 3 |

Two conclusions follow from the table. First, the integrating factor is cheap but indispensable: losing it costs the whole question. Second, the Bernoulli reduction is the single most heavily weighted piece of bookwork, so it must be reproducible from memory, including the factor $1-n$.

### 1.3 Recognition in ten seconds

The recognition test has four questions, and the answer to each is a single word.

- Is the highest derivative the first? If not, the question is not from this topic.
- Is the coefficient of $\frac{dy}{dx}$ free of $y$? If not, the equation may still be linear in $x$ after taking reciprocals.
- Does $y$ appear only to the first power, and never multiplied by its derivative? If yes, the equation is linear.
- Does a single power $y^{n}$ appear on the right, with no other occurrence of $y$? If yes, the equation is Bernoulli.

Three examples show how fast the classification can be made. The equation $\frac{dy}{dx}+\frac{2}{x}y=x^{3}$ is linear, with $P=\frac{2}{x}$ and $Q=x^{3}$. The equation $\frac{dy}{dx}-\frac{y}{x}=y^{2}\ln x$ is Bernoulli with $n=2$, because the right-hand side is $Qy^{2}$ with $Q=\ln x$. The equation $\frac{dy}{dx}=\frac{1}{x+y^{2}}$ is neither, until the reciprocal is taken, after which it reads $\frac{dx}{dy}-x=y^{2}$ and is linear in $x$.

A fourth pattern deserves separate mention because it is often missed. An equation such as $\frac{dy}{dx}+y=\frac{x}{y}$ is not Bernoulli as written, since the right-hand side is not of the form $Qy^{n}$ with a single power. Multiplying through by $y$ gives $y\frac{dy}{dx}+y^{2}=x$, and the substitution $z=y^{2}$ converts it to $\frac{1}{2}\frac{dz}{dx}+z=x$, which is linear. The classification is therefore not always a matter of reading the equation; sometimes one multiplication is needed to reveal it.

### 1.4 The Bernoulli substitution and the exponent table

A Bernoulli equation is one of the form

$$
\frac{dy}{dx}+P(x)\,y=Q(x)\,y^{n},
$$

with $n$ a real constant. For $n\neq 1$ the substitution is

$$
v=y^{1-n},
$$

and the reduced equation is

$$
\frac{dv}{dx}+(1-n)P(x)\,v=(1-n)Q(x).
$$

The table lists the cases that occur in exercises, together with the substitution and the reduced coefficient. Memorising this table removes most of the algebra from the start of a Bernoulli question.

| Exponent $n$ | Substitution $v$ | Reduced coefficient of $v$ | Reduced forcing |
| --- | --- | --- | --- |
| $0$ | already linear | $P$ | $Q$ |
| $1$ | separable, no substitution | not applicable | not applicable |
| $2$ | $v=y^{-1}$ | $-P$ | $-Q$ |
| $3$ | $v=y^{-2}$ | $-2P$ | $-2Q$ |
| $4$ | $v=y^{-3}$ | $-3P$ | $-3Q$ |
| $5$ | $v=y^{-4}$ | $-4P$ | $-4Q$ |
| $-1$ | $v=y^{2}$ | $2P$ | $2Q$ |
| $-\frac{1}{2}$ | $v=y^{3/2}$ | $\frac{3}{2}P$ | $\frac{3}{2}Q$ |
| $\frac{1}{2}$ | $v=y^{1/2}$ | $\frac{1}{2}P$ | $\frac{1}{2}Q$ |

The pattern in the table is the source of the sign errors that dominate this topic. When $n>1$ the factor $1-n$ is negative, so every coefficient changes sign; when $n<1$ the factor is positive and no sign changes. A candidate who writes the reduced equation with the wrong sign will usually find that the solution fails the check, and the check is therefore not optional.

### 1.5 The three standard reductions

The following three reductions cover every question in the topic that is not already in standard form. Each is worth learning as a single move rather than as a sequence of algebra.

The first reduction clears a coefficient on the derivative. From $a(x)\frac{dy}{dx}+b(x)y=c(x)$ with $a\neq 0$, divide by $a$ to obtain $P=\frac{b}{a}$ and $Q=\frac{c}{a}$.

The second reduction is the Bernoulli substitution, described in Section 1.4. It applies when exactly one power $y^{n}$ appears in addition to the linear terms.

The third reduction exchanges the variables. If the equation can be solved for $\frac{dx}{dy}$, then $x$ becomes the unknown and the equation takes the form

$$
\frac{dx}{dy}+A(y)\,x=B(y),
$$

which is solved with the integrating factor $e^{\int A\,dy}$. The reduction requires $\frac{dy}{dx}\neq 0$ on the arc considered, and that hypothesis should be stated.

### 1.6 What a complete answer looks like

A complete answer contains five elements, and each is worth marks. The standard form should be displayed, so that $P$ and $Q$ are visible. The integrating factor should be displayed as a simplified function, not as an unsimplified exponential. The product form should be written before the integral is evaluated, which makes the logic of the method visible. The final solution should be solved for $y$ where possible, or left in a clean implicit form if that is clearer. And the interval of validity should be stated, together with the restriction $y\neq 0$ and the separate zero solution when the equation is Bernoulli with $n>0$.

The conventions for constants matter for full marks. One constant is introduced at the single integration, and it is written $C$. A constant introduced inside the exponent of the integrating factor is not counted and should be suppressed. When an initial condition is imposed, the constant is evaluated explicitly and the particular solution is displayed.

### 1.7 The vocabulary that earns marks

Three phrases recur in mark schemes and should be used deliberately. "This is of the form $\frac{dy}{dx}+Py=Q$ with $P=\dots$ and $Q=\dots$" establishes recognition. "The integrating factor is $\mu=e^{\int P\,dx}=\dots$" establishes the key construction. "This is a Bernoulli equation with $n=\dots$, so put $v=y^{1-n}=\dots$" establishes the reduction. Writing these three sentences, rather than merely performing the algebra, is what allows a marker to award the method marks even when a later slip occurs.

### 1.8 The three forcing patterns

The right-hand side $Q$ determines how much integration is needed, and three patterns account for nearly every examination example. Recognising the pattern in advance tells the candidate how long the question will take and which integrals will be required.

The first pattern is $Q=0$. The equation is homogeneous, the product form has zero on the right, and the solution is

$$
y=C\,e^{-\int P\,dx} .
$$

The coefficient still has to be integrated, so the pattern saves the integration of $Q$ but not the integrating factor. An example is $\frac{dy}{dx}+2xy=0$, whose factor is $e^{x^{2}}$ and whose solution is $y=Ce^{-x^{2}}$.

The second pattern is constant $Q$ with constant $P=p$. The equilibrium is $\frac{Q}{p}$ and the solution is

$$
y=\frac{Q}{p}+C\,e^{-px},
$$

so the integration is elementary and the answer has a predictable shape. An example is $\frac{dy}{dx}+2y=6$, whose solution is $y=3+Ce^{-2x}$; the value $3$ is the equilibrium and the exponential is the transient.

The third pattern is a forcing that requires integration by parts. If $Q$ is a polynomial and $P$ is constant, the particular solution is a polynomial of the same degree, and the number of parts equals the degree of $Q$. If $Q$ is a polynomial times an exponential, parts may be avoided when the exponential cancels the integrating factor; for example, $\frac{dy}{dx}+2y=xe^{-2x}$ gives $\frac{d}{dx}\left(ye^{2x}\right)=x$, so that $y=e^{-2x}\left(\frac{x^{2}}{2}+C\right)$ with no parts at all.

The three patterns are worth one mark each when they are identified correctly, because the identification justifies the method that follows. They also provide a check on the answer: a constant forcing with constant coefficient should produce a constant particular solution, and a polynomial forcing should produce a polynomial particular solution of the same degree, so an answer that violates either expectation contains an error.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The integrating-factor identity

> **Theorem.** Let $P$ be continuous on an interval $I$ and let $\mu=e^{\int P\,dx}$ be positive there. Then for every differentiable $y$ on $I$,
>
> $$
> \mu\left(\frac{dy}{dx}+Py\right)=\frac{d}{dx}\left(\mu y\right).
> $$

This is the result that makes the method work, and it is examined both as a statement and as a derivation. In a "show that" question it is worth three to four marks, and the expected answer is the product-rule expansion together with the observation $\mu'=P\mu$.

### 2.2 The solution formula

> **Theorem.** With $P,Q$ continuous on $I$, the general solution of $\frac{dy}{dx}+Py=Q$ is
>
> $$
> y=e^{-\int P\,dx}\left(\int Q\,e^{\int P\,dx}\,dx+C\right).
> $$

The formula is quoted in the mark scheme as the general solution and is worth two to three marks when applied correctly. Two variants are examined. The indefinite form above is used when the answer is wanted as a formula. The definite form

$$
y=e^{-\int_{x_{0}}^{x}P}\left(y_{0}+\int_{x_{0}}^{x}Q\,e^{\int P}\right)
$$

is used when an initial condition is given, and it removes the need to determine $C$.

### 2.3 The Bernoulli reduction theorem

> **Theorem.** Let $n\neq 1$ and let $P,Q$ be continuous. On any interval where $y\neq 0$, the substitution $v=y^{1-n}$ converts
>
> $$
> \frac{dy}{dx}+Py=Qy^{n}
> $$
>
> into
>
> $$
> \frac{dv}{dx}+(1-n)Pv=(1-n)Q .
> $$

The derivation is worth five marks and is the single most commonly examined piece of bookwork in the topic. The three steps that earn the marks are: dividing by $y^{n}$, differentiating $v=y^{1-n}$ to obtain $\frac{dv}{dx}=(1-n)y^{-n}\frac{dy}{dx}$, and clearing the factor $1-n$.

### 2.4 The degenerate cases

> **Lemma.** If $n=0$ the equation is linear and is solved with $P$ and $Q$ unchanged. If $n=1$ the equation is separable and its general solution is
>
> $$
> y=C\,e^{\int\left(Q-P\right)dx}
> $$
>
> on any interval where $y\neq 0$.

The case $n=1$ is worth one or two marks and is a standard trap. Substituting $v=y^{0}$ is meaningless, and a candidate who writes $v=1$ and then attempts to solve a differential equation for a constant has lost the thread of the question.

### 2.5 The zero solution

> **Lemma.** If $n>0$ then $y\equiv 0$ is a solution of the Bernoulli equation. If $n<0$ it is not defined as a solution, and if $n=0$ it solves the equation only when $Q\equiv 0$.

This is worth a single mark, and it is awarded only when the zero solution is stated separately from the general family. The general family obtained by the substitution never contains $y=0$, because the derivation divided by $y^{n}$.

### 2.6 The reciprocal-form theorem

> **Theorem.** If the equation can be written as $\frac{dx}{dy}+A(y)x=B(y)$ with $A,B$ continuous, then its general solution is
>
> $$
> x=e^{-\int A\,dy}\left(\int B\,e^{\int A\,dy}\,dy+C\right).
> $$

The result is not usually quoted by name, but the transformation that produces it is worth two marks, and the condition $\frac{dy}{dx}\neq 0$ is worth a further mark when the question asks for justification.

### 2.7 Existence, uniqueness, and the initial condition

> **Theorem.** If $P$ and $Q$ are continuous on an interval $I$ containing $x_{0}$, the problem $\frac{dy}{dx}+Py=Q$, $y(x_{0})=y_{0}$, has exactly one solution on $I$.

The practical content is that exactly one constant has to be determined, and that the answer is unique. In an examination this justifies the statement "the solution is" rather than "a solution is", and it also justifies rejecting a second apparently valid expression.

### 2.8 Asymptotics for constant coefficients

> **Theorem.** If $P=p\neq 0$ and $Q=q$ are constants, then
>
> $$
> y=\frac{q}{p}+\left(y_{0}-\frac{q}{p}\right)e^{-p(x-x_{0})},
> $$
>
> so the solution approaches the equilibrium $\frac{q}{p}$ exponentially when $p>0$.

The equilibrium value $\frac{q}{p}$ is frequently asked for as a one-mark part, and the qualitative statement "the solution tends to $\frac{q}{p}$ as $x\to\infty$" is worth another mark. The result also explains the shape of every solution curve with constant coefficients: a single exponential transient added to a constant level.

### 2.9 The integrals that actually appear

The following table collects the coefficient integrals that occur in exercises together with the resulting integrating factor. Recognising these pairs on sight saves several minutes per question.

| Coefficient $P(x)$ | $\int P\,dx$ | Integrating factor $\mu$ | Valid on |
| --- | --- | --- | --- |
| $k$ constant | $kx$ | $e^{kx}$ | all $x$ |
| $\frac{1}{x}$ | $\ln x$ | $x$ | $x>0$ |
| $\frac{2}{x}$ | $2\ln x$ | $x^{2}$ | $x>0$ |
| $2x$ | $x^{2}$ | $e^{x^{2}}$ | all $x$ |
| $\frac{2x}{1+x^{2}}$ | $\ln\left(1+x^{2}\right)$ | $1+x^{2}$ | all $x$ |
| $\cot x$ | $\ln\left(\sin x\right)$ | $\sin x$ | $0<x<\pi$ |
| $\tan x$ | $-\ln\left(\cos x\right)$ | $\sec x$ | $-\frac{\pi}{2}<x<\frac{\pi}{2}$ |
| $-1$ | $-x$ | $e^{-x}$ | all $x$ |
| $\frac{1}{1+x}$ | $\ln\left(1+x\right)$ | $1+x$ | $x>-1$ |
| $-\frac{1}{y}$ with $y$ independent | $-\ln y$ | $\frac{1}{y}$ | $y>0$ |

The last row is not a coefficient in $x$ at all; it is included because the reciprocal-form questions use exactly that pattern, with $y$ as the independent variable. Reading the table by pattern rather than by memorising each entry is the intended use: in each case the coefficient is the logarithmic derivative of the integrating factor.

### 2.10 A structural property worth quoting

> **Lemma.** If $y_{1}$ and $y_{2}$ both solve $\frac{dy}{dx}+Py=Q$ on $I$, then $y_{1}-y_{2}=Ce^{-\int P\,dx}$ for some constant $C$.

The lemma is the uniqueness statement in a form that is easy to quote, and it is useful in "show that the solution is unique" parts. It also supplies a check: two correct solutions must differ by a homogeneous solution, so if two candidate answers differ by something that is not a multiple of $e^{-\int P\,dx}$, at least one of them is wrong.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Derivation of the integrating factor (4 marks)

The derivation is examined as bookwork and is also the fastest way to remember the formula. It begins from the product rule, because the aim is to convert a sum into a single derivative.

Step 1. Expand the derivative of the product $\mu y$, where $\mu$ is a positive function of $x$ still to be chosen.

$$
\frac{d}{dx}\left(\mu y\right)=\mu\frac{dy}{dx}+\mu' y
$$

Step 2. Multiply the left-hand side of the standard equation by the same $\mu$ and compare the two expressions term by term.

$$
\mu\left(\frac{dy}{dx}+Py\right)=\mu\frac{dy}{dx}+\mu P y
$$

Step 3. The first terms already agree, so the second terms must agree, which gives the condition on $\mu$.

$$
\mu'=P\mu
$$

Step 4. Solve the condition by separating variables.

$$
\frac{\mu'}{\mu}=P \quad\Longrightarrow\quad \ln\mu=\int P\,dx \quad\Longrightarrow\quad \mu=e^{\int P\,dx}
$$

Step 5. State the conclusion: multiplying by this $\mu$ turns the left-hand side into the derivative of a single product, so the equation becomes integrable. No constant of integration is needed in step 4, because a constant multiple of $\mu$ cancels from both sides of the equation.

The five steps are worth four marks in the usual allocation: one for the product-rule expansion, one for the comparison, one for the condition $\mu'=P\mu$, one for the solution of that condition. A candidate who writes "the integrating factor is $e^{\int P\,dx}$" with no derivation earns the formula mark only, and that is typically one of the two marks available for the statement part.

### 3.2 Proof that the factor makes the equation exact (6 marks)

The second derivation is examined less often but appears in questions that ask why the method works. Write the equation as a differential form and test it for exactness.

Step 1. Rearrange $\frac{dy}{dx}+Py=Q$ into a form in $dx$ and $dy$.

$$
\left(Py-Q\right)dx+dy=0
$$

Step 2. Identify the coefficients and compute the exactness test.

$$
M=Py-Q,\qquad N=1,\qquad \frac{\partial M}{\partial y}=P,\qquad \frac{\partial N}{\partial x}=0
$$

The test fails unless $P\equiv 0$, so the form is not exact in general.

Step 3. Multiply the form by $\mu$ and recompute.

$$
\widetilde{M}=\mu\left(Py-Q\right),\qquad \widetilde{N}=\mu,\qquad \frac{\partial \widetilde{M}}{\partial y}=\mu P,\qquad \frac{\partial \widetilde{N}}{\partial x}=\mu'
$$

Step 4. Impose exactness and solve the resulting condition.

$$
\mu P=\mu' \quad\Longrightarrow\quad \mu=e^{\int P\,dx}
$$

Step 5. Construct the potential function. Since $\frac{\partial F}{\partial y}=\mu$, integration with respect to $y$ at fixed $x$ gives $F=\mu y+g(x)$, and then

$$
\frac{\partial F}{\partial x}=\mu' y+g'(x)=\mu\left(Py-Q\right)
$$

Step 6. Use $\mu'=\mu P$ to cancel the terms in $y$, leaving $g'(x)=-\mu Q$, so that

$$
F(x,y)=\mu y-\int \mu Q\,dx .
$$

Step 7. The solutions are the level curves $F=c$, which gives $\mu y=\int \mu Q\,dx+C$, the solution formula.

The step that carries the most weight in the mark scheme is step 4, because it identifies the integrating factor with the multiplier that repairs exactness. The construction in steps 5 to 7 is worth two marks and is the part most often omitted; when it is omitted the derivation shows only that a multiplier exists, not that it produces the solution.

### 3.3 Derivation of the Bernoulli substitution (5 marks)

Step 1. Divide the equation by $y^{n}$, which requires $y\neq 0$ and must be stated.

$$
y^{-n}\frac{dy}{dx}+P y^{1-n}=Q
$$

Step 2. State the substitution and its range of validity.

$$
v=y^{1-n},\qquad n\neq 1
$$

Step 3. Differentiate the substitution.

$$
\frac{dv}{dx}=\left(1-n\right)y^{-n}\frac{dy}{dx}
$$

Step 4. Solve for the combination that appears in the equation.

$$
y^{-n}\frac{dy}{dx}=\frac{1}{1-n}\frac{dv}{dx}
$$

Step 5. Substitute and clear the fraction.

$$
\frac{1}{1-n}\frac{dv}{dx}+Pv=Q \quad\Longrightarrow\quad \frac{dv}{dx}+\left(1-n\right)Pv=\left(1-n\right)Q
$$

Step 6. State the conclusion: the equation in $v$ is linear, has continuous coefficients, and is solved by the integrating factor

$$
e^{\int\left(1-n\right)P\,dx}=\left(e^{\int P\,dx}\right)^{1-n}=\mu^{1-n}.
$$

Step 7. State the inverse substitution $y=v^{1/(1-n)}$, which maps solutions of the linear equation back to solutions of the Bernoulli equation on the interval where $v$ has the appropriate sign.

The mark allocation is typically one mark for the division, one for the differentiation of $v$, one for the substitution, one for clearing the factor, and one for the statement of the reduced linear equation. Step 6 is a bonus result that is often worth a mark in its own right, because it shows that no new integration is needed.

### 3.4 The linear equation in examination order

The following sequence is the one to write, because it matches the mark scheme line by line.

1. Write "This is of the form $\frac{dy}{dx}+Py=Q$ with $P=\dots$ and $Q=\dots$" and display both functions. If a coefficient multiplies the derivative, divide it out first and state the restricted interval.
2. Compute $\int P\,dx$ in a display line, then state $\mu$ as a simplified function in a second display line. Simplification is worth a mark: writing $\mu=e^{\ln x}$ without reducing it to $x$ is treated as incomplete.
3. Multiply the equation by $\mu$ and write the result in the form $\frac{d}{dx}\left(\mu y\right)=\mu Q$. This line is where the method is demonstrated.
4. Integrate both sides with respect to $x$ and add the single constant $C$. If the integral needs parts, show the parts calculation.
5. Divide by $\mu$ and simplify. If the answer can be written explicitly for $y$, do so.
6. If an initial condition is given, substitute it and solve for $C$ in a display line, then display the particular solution.
7. State the interval and, where relevant, any restriction such as $y\neq 0$. Finish with the verification.

### 3.5 The Bernoulli equation in examination order

1. Write "This is a Bernoulli equation with $n=\dots$". If $n=0$ or $n=1$, say so and use the appropriate method instead.
2. Divide every term by $y^{n}$ and state that this requires $y\neq 0$.
3. Write the substitution $v=y^{1-n}$, differentiate it, and solve for $y^{-n}\frac{dy}{dx}$.
4. Substitute to obtain the linear equation in $v$, then multiply through by $1-n$ so that the coefficient of $\frac{dv}{dx}$ is one. Display the equation in standard form and name the new $P$ and $Q$.
5. Solve the linear equation by the steps of Section 3.4, using the integrating factor $\mu^{1-n}$ if it is already known.
6. Replace $v$ by $y^{1-n}$ and solve for $y$ where possible. If the answer is cleaner implicitly, leave it as an equation in $y$ and say so.
7. Add the zero solution when $n>0$, state the interval where $y\neq 0$, and verify by substitution into the original equation.

Step 4 is the one that must not be rushed. The commonest error in the whole topic is to substitute correctly and then forget to multiply by $1-n$, which produces a linear equation with coefficients off by a constant factor and a solution that fails the check.

### 3.6 The reciprocal form in examination order

1. Check that the equation cannot be linearised in $y$ by a power substitution. If it cannot, take reciprocals to obtain $\frac{dx}{dy}$.
2. Rearrange into $\frac{dx}{dy}+A(y)x=B(y)$ and display $A$ and $B$.
3. Compute the integrating factor $e^{\int A\,dy}$ and simplify.
4. Multiply through, integrate with respect to $y$, add $C$, and divide.
5. State that the result holds where $\frac{dy}{dx}\neq 0$, and convert back to $y$ as a function of $x$ only if the question requires it.

### 3.7 The verification routine

Verification is worth explicit marks in most schemes, and it has a fixed form. Given $y=\phi(x)$, compute $\phi'(x)$, then form

$$
\phi'(x)+P(x)\phi(x)
$$

and simplify. Every term containing $C$ must cancel, and the remainder must equal $Q(x)$. If an initial condition was given, evaluate $\phi$ at the initial abscissa and compare with the stated value. If the answer was obtained by a Bernoulli substitution, the check must be performed in the original equation, because the transformed equation is automatically satisfied by construction and therefore tests nothing.

A check that fails usually indicates one of four faults: the integral of $P$ is wrong, the integral of $\mu Q$ is wrong, the sign of $P$ was changed in transit, or the constant was misplaced. Working backwards from the failed check to the display line where the fault occurred is much faster than redoing the whole question.

### 3.8 Integrals that must be ready

Four integration techniques cover essentially every question in the topic, and each should be practised until it can be performed without commentary.

The first is direct integration of a polynomial times an exponential, which requires parts once for a linear factor and twice for a quadratic factor. For a constant $k\neq 0$,

$$
\int x e^{kx}\,dx=\frac{e^{kx}}{k}\left(x-\frac{1}{k}\right), \qquad \int x^{2}e^{kx}\,dx=\frac{e^{kx}}{k}\left(x^{2}-\frac{2x}{k}+\frac{2}{k^{2}}\right).
$$

The second is the integral of a polynomial times a trigonometric function, which also requires parts and produces a polynomial of the same degree. The third is the logarithmic pattern, in which the coefficient is the derivative of the logarithm of some function; the integral is then that logarithm, and the integrating factor is the function itself. The fourth is the trigonometric pattern with $\cot$ and $\tan$, where the integral is a logarithm of a sine or cosine and the integrating factor is that sine or cosine, possibly inverted.

The fourth pattern is worth a warning. Since

$$
\int\cot x\,dx=\ln\left(\sin x\right), \qquad \int\tan x\,dx=-\ln\left(\cos x\right),
$$

the integrating factors are $\sin x$ and $\sec x$ respectively, and the sign in the second case is easily lost. A quick check is to differentiate the proposed integrating factor: the derivative of $\sec x$ is $\sec x\tan x$, which equals $\mu P$ with $P=\tan x$, confirming the choice.

### 3.9 Presentation rules that protect marks

Three presentation habits protect marks that would otherwise be lost. Display the standard form, the integrating factor, and the product form as separate display equations, because markers award method marks by locating those lines. Keep the arbitrary constant visible until it is evaluated, since a constant that disappears in the middle of a computation is usually a sign that it was absorbed into an integrating factor. And state the interval in words at the end, because a correct formula with no interval is an incomplete answer whenever the coefficients have a singularity.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: solve $\frac{dy}{dx}+y\cot x=\csc x$ with $y\left(\frac{\pi}{2}\right)=1$ on $0<x<\pi$ (9 marks)

### 4.2 Solution: model answer with marking points

1. The equation is already of the form $\frac{dy}{dx}+Py=Q$ with $P=\cot x$ and $Q=\csc x$, both continuous on $0<x<\pi$. [1 mark: recognition]

2. Compute the coefficient integral, using the logarithmic pattern.

$$
\int\cot x\,dx=\int\frac{\cos x}{\sin x}\,dx=\ln\left(\sin x\right)
$$

[1 mark: correct integral]

3. Form the integrating factor and simplify it.

$$
\mu=e^{\ln\left(\sin x\right)}=\sin x
$$

[1 mark: integrating factor]

4. Multiply through by $\sin x$ and write the left side as a derivative.

$$
\frac{d}{dx}\left(y\sin x\right)=\csc x\cdot\sin x=1
$$

[1 mark: product form with the right side simplified]

5. Integrate with respect to $x$.

$$
y\sin x=x+C
$$

[1 mark: integration]

6. Divide by $\sin x$ to obtain the general solution.

$$
y=\left(x+C\right)\csc x
$$

[1 mark: solved for $y$]

7. Impose the condition at $x=\frac{\pi}{2}$, where $\sin\frac{\pi}{2}=1$.

$$
1=\left(\frac{\pi}{2}+C\right)\cdot 1 \quad\Longrightarrow\quad C=1-\frac{\pi}{2}
$$

[1 mark: constant determined]

8. State the particular solution.

$$
y=\left(x+1-\frac{\pi}{2}\right)\csc x
$$

[1 mark: particular solution]

9. Verify and state the interval. Differentiating gives

$$
\frac{dy}{dx}=\frac{\sin x-\left(x+1-\frac{\pi}{2}\right)\cos x}{\sin^{2}x},
$$

and

$$
y\cot x=\frac{\left(x+1-\frac{\pi}{2}\right)\cos x}{\sin^{2}x},
$$

so the sum is $\frac{\sin x}{\sin^{2}x}=\csc x$. The solution holds on $0<x<\pi$, and the check at $x=\frac{\pi}{2}$ gives $y=\frac{\pi}{2}+1-\frac{\pi}{2}=1$. [1 mark: verification and interval]

### 4.3 Problem: solve $\frac{dy}{dx}+\frac{1}{x}y=y^{2}$ with $y(1)=1$ (10 marks)

### 4.4 Solution: model answer with marking points

1. This is a Bernoulli equation with $n=2$, $P=\frac{1}{x}$ and $Q=1$. Since $n\neq 0,1$ a substitution is required. [1 mark: classification]

2. Divide every term by $y^{2}$, valid for $y\neq 0$.

$$
y^{-2}\frac{dy}{dx}+\frac{1}{x}y^{-1}=1
$$

[1 mark: division by $y^{2}$]

3. Put $v=y^{1-2}=y^{-1}$ and differentiate.

$$
\frac{dv}{dx}=-y^{-2}\frac{dy}{dx} \quad\Longrightarrow\quad y^{-2}\frac{dy}{dx}=-\frac{dv}{dx}
$$

[1 mark: substitution and derivative]

4. Substitute into the divided equation.

$$
-\frac{dv}{dx}+\frac{1}{x}v=1
$$

[1 mark: correct substitution]

5. Multiply by $-1$ to reach standard form.

$$
\frac{dv}{dx}-\frac{1}{x}v=-1
$$

[1 mark: standard form in $v$]

6. The coefficient is $-\frac{1}{x}$ and the forcing is $-1$, so the integrating factor is

$$
\mu=e^{\int-\frac{1}{x}dx}=e^{-\ln x}=\frac{1}{x}
$$

on $x>0$. [1 mark: integrating factor]

7. Multiply through and integrate.

$$
\frac{d}{dx}\left(\frac{v}{x}\right)=-\frac{1}{x}
$$

$$
\frac{v}{x}=-\ln x+C
$$

[1 mark: correct integral]

8. Divide by $\frac{1}{x}$, that is multiply by $x$.

$$
v=x\left(C-\ln x\right)
$$

[1 mark: solved for $v$]

9. Impose the condition. Since $y(1)=1$ we have $v(1)=1$, so

$$
1=1\cdot\left(C-0\right) \quad\Longrightarrow\quad C=1
$$

[1 mark: constant determined]

10. Translate back and state the answer, including the interval.

$$
\frac{1}{y}=x\left(1-\ln x\right) \quad\Longrightarrow\quad y=\frac{1}{x\left(1-\ln x\right)}, \qquad 0<x<e
$$

The interval is the largest one containing $x=1$ on which $y\neq 0$ and $1-\ln x>0$. The zero solution, excluded by the division, also satisfies the original equation because $n=2>0$. [1 mark: back-substitution and interval]

11. Verify. With $v=x\left(1-\ln x\right)$ we have

$$
\frac{dv}{dx}=1-\ln x-1=-\ln x,
$$

and

$$
\frac{dv}{dx}-\frac{1}{x}v=-\ln x-\left(1-\ln x\right)=-1,
$$

which is the equation for $v$; by the reduction theorem the original equation is satisfied on the stated interval.

### 4.5 Problem: solve $\frac{dy}{dx}+y=xy^{3}$ (10 marks)

### 4.6 Solution: model answer with marking points

1. This is a Bernoulli equation with $n=3$, $P=1$ and $Q=x$. [1 mark: classification]

2. Divide by $y^{3}$, valid for $y\neq 0$.

$$
y^{-3}\frac{dy}{dx}+y^{-2}=x
$$

[1 mark: division]

3. Put $v=y^{-2}$ and differentiate.

$$
\frac{dv}{dx}=-2y^{-3}\frac{dy}{dx} \quad\Longrightarrow\quad y^{-3}\frac{dy}{dx}=-\frac{1}{2}\frac{dv}{dx}
$$

[1 mark: substitution and derivative]

4. Substitute and clear the fraction.

$$
-\frac{1}{2}\frac{dv}{dx}+v=x \quad\Longrightarrow\quad \frac{dv}{dx}-2v=-2x
$$

[2 marks: substitution and standard form]

5. The integrating factor for the $v$ equation is $e^{-2x}$, so

$$
\frac{d}{dx}\left(v e^{-2x}\right)=-2x e^{-2x}
$$

[1 mark: integrating factor and product form]

6. Integrate by parts with $u=x$ and $dv=e^{-2x}dx$.

$$
\int x e^{-2x}\,dx=-\frac{1}{2}xe^{-2x}-\frac{1}{4}e^{-2x}
$$

[1 mark: parts correctly performed]

7. Insert the factor $-2$ and add the constant.

$$
v e^{-2x}=xe^{-2x}+\frac{1}{2}e^{-2x}+C
$$

[1 mark: integration complete]

8. Divide by $e^{-2x}$.

$$
v=x+\frac{1}{2}+Ce^{2x}
$$

[1 mark: solved for $v$]

9. Translate back to $y$ and state the restriction.

$$
\frac{1}{y^{2}}=x+\frac{1}{2}+Ce^{2x}, \qquad y^{2}=\frac{1}{x+\frac{1}{2}+Ce^{2x}}
$$

The solution is real only where the denominator is positive, and $y=0$ is a solution because $n=3>0$. [1 mark: back-substitution and zero solution]

10. Verify in the original equation. From $v=x+\frac{1}{2}+Ce^{2x}$ we get $v'=1+2Ce^{2x}$, hence

$$
v'-2v=1+2Ce^{2x}-2x-1-2Ce^{2x}=-2x,
$$

so the equation for $v$ holds and the original equation is satisfied wherever $y\neq 0$.

### 4.7 Problem: solve $\frac{dy}{dx}=\frac{1}{x+y^{2}}$ with $x(0)=0$ (10 marks)

### 4.8 Solution: model answer with marking points

1. The equation is not linear in $y$, since $y$ appears squared inside the denominator; nor is it Bernoulli. Take reciprocals, valid where $\frac{dy}{dx}\neq 0$. [1 mark: decision to invert]

2. Perform the inversion.

$$
\frac{dx}{dy}=x+y^{2}
$$

[1 mark: reciprocal taken correctly]

3. Rearrange into standard form with $x$ as the unknown.

$$
\frac{dx}{dy}-x=y^{2}
$$

[1 mark: standard form, with $A(y)=-1$ and $B(y)=y^{2}$]

4. Compute the integrating factor.

$$
e^{\int(-1)\,dy}=e^{-y}
$$

[1 mark: integrating factor]

5. Multiply through to obtain a derivative.

$$
\frac{d}{dy}\left(x e^{-y}\right)=y^{2}e^{-y}
$$

[1 mark: product form]

6. Integrate by parts twice.

$$
\int y^{2}e^{-y}\,dy=-y^{2}e^{-y}-2ye^{-y}-2e^{-y}
$$

[2 marks: both parts steps correct]

7. Insert and divide by $e^{-y}$.

$$
x e^{-y}=-e^{-y}\left(y^{2}+2y+2\right)+C \quad\Longrightarrow\quad x=-\left(y^{2}+2y+2\right)+Ce^{y}
$$

[1 mark: general solution]

8. Impose $x(0)=0$.

$$
0=-2+C \quad\Longrightarrow\quad C=2
$$

[1 mark: constant determined]

9. State the particular solution and verify.

$$
x=2e^{y}-y^{2}-2y-2
$$

Differentiating with respect to $y$ gives $\frac{dx}{dy}=2e^{y}-2y-2$, while $x+y^{2}=2e^{y}-2y-2$, so the transformed equation holds and $x(0)=-2+2=0$. [1 mark: verification and condition]

### 4.9 Problem: solve $\frac{dy}{dx}+2y=x^{2}$ with $y(0)=1$ (7 marks)

### 4.10 Solution: model answer with marking points

1. In standard form, $P=2$ and $Q=x^{2}$, both continuous everywhere. [1 mark: recognition]

2. The integrating factor is $\mu=e^{2x}$. [1 mark]

3. Multiply through.

$$
\frac{d}{dx}\left(y e^{2x}\right)=x^{2}e^{2x}
$$

[1 mark: product form]

4. Integrate by parts twice.

$$
\int x^{2}e^{2x}\,dx=e^{2x}\left(\frac{x^{2}}{2}-\frac{x}{2}+\frac{1}{4}\right)
$$

[2 marks: two applications of parts]

5. Divide by $e^{2x}$ to obtain the general solution.

$$
y=\frac{x^{2}}{2}-\frac{x}{2}+\frac{1}{4}+Ce^{-2x}
$$

[1 mark: general solution]

6. Impose $y(0)=1$ and state the answer.

$$
1=\frac{1}{4}+C \quad\Longrightarrow\quad C=\frac{3}{4}, \qquad y=\frac{x^{2}}{2}-\frac{x}{2}+\frac{1}{4}+\frac{3}{4}e^{-2x}
$$

[1 mark: constant and particular solution]

7. Verify. The derivative is $x-\frac{1}{2}-\frac{3}{2}e^{-2x}$, and

$$
\frac{dy}{dx}+2y=x-\frac{1}{2}-\frac{3}{2}e^{-2x}+x^{2}-x+\frac{1}{2}+\frac{3}{2}e^{-2x}=x^{2},
$$

so the equation holds for all $x$. The solution tends to the parabola $\frac{x^{2}}{2}-\frac{x}{2}+\frac{1}{4}$ as $x\to\infty$, because the exponential term decays.

## 5. Mathematical Extensions, Limits, and Common Errors

The material in this section is arranged for the last stage of revision. The trap table collects the mistakes that appear most often in scripts, the pattern table shows how the standard question types are worded and what each is worth, and the extensions record the places where the method stops or changes character. The revision checklist and the timing plan at the end are meant to be used in the final days before an examination, not read once and forgotten.

### 5.1 The trap table

| Trap | How it appears in a script | Cost | Correction |
| --- | --- | --- | --- |
| Factor is $e^{P}$ | Writing $\mu=e^{2x}$ for $P=2x$ | Whole question | Always integrate first, then exponentiate |
| Coefficient not cleared | Using $P=1$ in $x\frac{dy}{dx}+y=x^{3}$ | 2 to 3 marks | Divide by $x$ before reading off $P$ |
| Forcing integrated alone | Writing $y\mu=\mu\int Q\,dx$ | 2 marks | Multiply $Q$ by $\mu$ inside the integral |
| Constant in the exponent | Writing $e^{\int P\,dx+C}$ and then adding $C$ again | 1 mark | Use the simplest antiderivative |
| Constant omitted | Writing $y e^{2x}=3e^{2x}$ instead of $+C$ | 1 to 2 marks | Integrate with $+C$ every time |
| Lost zero solution | Reporting only the family for $n>0$ | 1 mark | Add $y=0$ explicitly |
| Missing $1-n$ factor | Writing $v'+Pv=Q$ after the substitution | 3 marks | Differentiate $v$ and carry the factor |
| Wrong sign in the reduced equation | Signs reversed when $n>1$ | 2 to 3 marks | Multiply through by $1-n$ carefully |
| Substitution with $n=1$ | Writing $v=y^{0}=1$ | Whole question | Treat as separable instead |
| Interval omitted | Formula with $\frac{1}{x}$ and no restriction | 1 mark | State the largest interval of continuity |
| Reciprocal taken wrongly | Writing $\frac{dx}{dy}=-x-y^{2}$ from $\frac{dy}{dx}=x+y^{2}$ | Whole question | Reciprocate, do not negate |
| Check in the reduced equation | Verifying only the equation for $v$ | 1 mark | Check in the original equation |

The pattern behind the table is that almost every trap is a failure to carry something through: the integral is dropped, the coefficient is not cleared, the factor $1-n$ is forgotten, the constant is lost, the interval is left out. Careful bookkeeping, rather than deeper understanding, prevents most of these losses, and the bookkeeping is cheap: each display line should contain exactly the symbols the next line needs.

### 5.2 Question patterns and their mark profile

| Pattern | Typical wording | Marks | Fast route |
| --- | --- | --- | --- |
| Solve a linear equation | "Solve $\frac{dy}{dx}+Py=Q$" | 5 to 7 | Three steps with the integrating factor |
| Initial-value problem | "Given that $y(x_{0})=y_{0}$, find $y$" | 6 to 8 | General solution, then determine $C$ |
| Derive the integrating factor | "Show that multiplying by $e^{\int P\,dx}$ makes the left side exact" | 4 to 6 | Product rule, then the exactness test |
| Bernoulli reduction | "Show that the substitution $v=y^{1-n}$ reduces the equation to linear form" | 4 to 5 | Divide, differentiate, substitute, clear |
| Solve a Bernoulli equation | "Hence solve $\frac{dy}{dx}+Py=Qy^{n}$" | 8 to 10 | Reduction, linear solve, back-substitute |
| Reciprocal form | "Solve $\frac{dy}{dx}=f(x,y)$ by treating $x$ as a function of $y$" | 8 to 9 | Invert, rearrange, integrate in $y$ |
| Steady-state or limit | "Find the value approached as $x\to\infty$" | 1 to 2 | Equilibrium $\frac{q}{p}$ for constant coefficients |
| Verification | "Verify that your solution satisfies the equation" | 1 to 3 | Substitute and cancel the constant |

The pattern table is also a planning tool. A question worth ten marks on a Bernoulli equation has roughly three marks for the reduction, four for the linear solution, two for the back-substitution and one for the interval and check. If time is short, the reduction marks are the cheapest, because they require no integration; the linear solution is where the time goes.

### 5.3 Extensions that examine the boundaries of the method

The first extension is resonance, in which the forcing is a multiple of the homogeneous solution. For

$$
\frac{dy}{dx}+y=e^{-x},
$$

the integrating factor is $e^{x}$ and the product form is

$$
\frac{d}{dx}\left(ye^{x}\right)=1,
$$

so

$$
y=e^{-x}\left(x+C\right).
$$

The factor $x$ appears because the forcing matches the natural mode. In a Bernoulli problem the same phenomenon can occur after the reduction, since the reduced equation is linear and may have a forcing proportional to its own homogeneous solution.

The second extension is the logistic equation, which is Bernoulli with $n=2$ and constant coefficients. For

$$
\frac{dy}{dx}=ay-by^{2},
$$

the substitution $v=y^{-1}$ gives $v'+av=b$, so

$$
v=\frac{b}{a}+Ce^{-ax}, \qquad y=\frac{1}{\frac{b}{a}+Ce^{-ax}},
$$

and the solution approaches the carrying capacity $\frac{a}{b}$ as $x\to\infty$ when $a>0$. The equilibrium $\frac{a}{b}$ is obtained by setting the derivative to zero, which gives $y\left(a-by\right)=0$ and hence the two constant solutions $y=0$ and $y=\frac{a}{b}$.

The third extension is periodic forcing, where the solution settles into a periodic response. For

$$
\frac{dy}{dx}+y=\sin x,
$$

the integrating factor is $e^{x}$ and

$$
\int e^{x}\sin x\,dx=\frac{e^{x}}{2}\left(\sin x-\cos x\right),
$$

so

$$
y=\frac{1}{2}\left(\sin x-\cos x\right)+Ce^{-x}.
$$

The transient decays and the periodic term remains, which is the first-order analogue of a forced oscillation. The amplitude of the remaining term is $\frac{1}{\sqrt{2}}$, smaller than the amplitude of the forcing, and the phase is shifted by a quarter period relative to a pure sine.

The fourth extension concerns singular points. The solution of

$$
\frac{dy}{dx}+\frac{1}{x}y=1
$$

is computed from $xy=x+C$ and is $y=1+\frac{C}{x}$, which is undefined at the origin. The answer is therefore valid on $x>0$ or on $x<0$, and the choice is fixed by the initial condition. A question that asks for the solution on an interval containing the origin has no answer, and saying so is worth a mark.

The fifth extension is the Riccati connection. The equation

$$
\frac{dy}{dx}=A(x)+B(x)y+C(x)y^{2}
$$

is not solvable by quadratures in general, but if one solution $y_{1}$ is known, the substitution $y=y_{1}+\frac{1}{u}$ linearises it. The Bernoulli equation is the case $A=0$, for which $y_{1}=0$ is known, and the substitution reduces to $y=\frac{1}{u}$, which is the Bernoulli substitution with $n=2$. This explains why Bernoulli equations are solvable and why the method does not extend to the general Riccati equation.

### 5.4 Revision checklist

The checklist is arranged so that each item can be tested in under two minutes. A tick means the item can be performed without notes.

- Write the standard form from memory and name $P$ and $Q$ in a given equation.
- Apply the four-question recognition test to a list of ten equations in one minute.
- Derive the integrating factor in five lines, starting from the product rule.
- Prove that the integrating factor makes the equation exact, using the test $\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}$.
- Reproduce the solution formula in both the indefinite and the definite forms.
- Solve a constant-coefficient equation with constant forcing and state its equilibrium.
- Solve an equation with $P=\frac{1}{x}$ and state the interval.
- Solve an equation with $P=\cot x$ or $P=\tan x$ and simplify the integrating factor.
- Perform $\int x e^{kx}dx$ and $\int x^{2}e^{kx}dx$ by parts without error.
- Recognise a Bernoulli equation and identify $n$ in under ten seconds.
- Derive the reduced equation in five lines, keeping the factor $1-n$.
- Solve a Bernoulli equation with $n=2$, $n=3$ and $n=-1$.
- State the degenerate cases $n=0$ and $n=1$ and solve the $n=1$ case by separation.
- State and justify the zero solution for $n>0$.
- Convert an equation to reciprocal form and solve it in $y$.
- Verify a solution in the original equation, not the reduced one.
- State the interval of validity for every answer that involves a singularity.

Two items on the list are commonly skipped and commonly examined: the exactness proof, and the reciprocal form. Both are short, and both are worth as much as an entire routine exercise.

### 5.5 Time strategy

| Phase of a ten-mark question | Target time | What must be on the page |
| --- | --- | --- |
| Recognition and standard form | 1 minute | The displayed standard form with $P$ and $Q$ named |
| Integrating factor | 2 minutes | The integral and the simplified factor |
| Reduction, if Bernoulli | 2 minutes | Division, substitution, reduced linear equation |
| Solving the linear equation | 3 minutes | Product form, integral, division, constant |
| Initial condition | 1 minute | Substitution and the value of $C$ |
| Interval and check | 1 minute | The interval in words and the substitution |

The allocation assumes a ten-mark question and should be adjusted proportionally. Three habits make the plan work in practice. First, write the standard form before doing anything else, because the rest of the question depends on it and the marks for recognition are unconditional. Second, never spend more than three minutes on an integral; if it is not resolving, check whether the integrating factor simplified wrongly, since a correct factor usually makes the integral elementary. Third, reserve the final minute for the interval and the check, because those are the marks most often lost and the least often attempted.

In a longer paper the ordering advice is to attempt the linear questions before the Bernoulli ones and the Bernoulli ones before the reciprocal ones. The reason is not difficulty but diagnosability: a linear question that goes wrong is usually wrong in one identifiable place, whereas a reciprocal question that goes wrong may be wrong in the inversion, the rearrangement, or the integration.

### 5.6 The errors that matter most

The errors in the trap table are mechanical, and mechanical errors are fixed by practice. Three errors are conceptual and deserve separate mention, because no amount of practice removes them unless the underlying idea is repaired.

The first is the belief that the integrating factor can be guessed. It cannot; it is determined by the coefficient through the condition $\mu'=P\mu$, and the only freedom is a positive multiplicative constant. A candidate who tries to guess a factor for $P=\frac{2x}{1+x^{2}}$ will usually produce $e^{2x}$ or $1+2x$, neither of which works.

The second is the belief that the Bernoulli substitution is optional bookkeeping. It is a change of variables that must be invertible on the interval considered, and its validity depends on $y\neq 0$. The zero solution and the restriction on the interval are consequences of that dependence, not extra decorations.

The third is the belief that a formula is an answer. A solution is a function on an interval together with the statement of that interval, and a formula that is correct algebraically but asserted on the wrong interval is wrong. The interval is part of the mathematics, and the examiners mark it as such.
