## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A savings account that keeps receiving deposits

Imagine a savings account whose balance grows because the bank pays interest continuously, and which also receives deposits from you at a steady trickle. Two things push the balance up at every instant: the interest, which is a fixed fraction of whatever is already in the account, and the deposits, which arrive from outside and do not care how much is there. If the balance is written $y$, the interest rate is a fixed number such as two percent per year, and the deposits arrive at a rate that may itself change with time, then the sentence "the balance grows at the interest rate plus the deposit rate" is a differential equation. It contains the unknown balance and its rate of change in the same statement.

That is the whole shape of the equations in this topic, and the reason they need a method of their own. An equation that mentions both a quantity and the speed at which that quantity changes cannot be solved by ordinary algebra, because algebra only rearranges numbers, and here the unknown is a whole curve of numbers. The method that works is to multiply the entire equation by one carefully chosen helper function. The helper function is chosen so that the left-hand side collapses into the derivative of a single product, after which both sides can simply be integrated. The helper is called the integrating factor, and finding it is the main skill of this lesson.

Picture a second version of the same idea, which is often easier to see. Suppose a hot cup of tea is cooling in a room, and at the same time someone keeps topping it up with hot water. The temperature falls because the tea loses heat in proportion to how much hotter it is than the room, and it rises because the added water is hot. Again two effects act at once, one proportional to the unknown temperature and one coming from outside. The same helper function, built out of the cooling rate, converts the problem into one where only the additions matter. Every example in this note is a variation on that single theme.

There is one more everyday picture worth keeping in mind, because it explains what the helper function actually does rather than merely how to compute it. When money earns interest, a sum of one hundred pounds today is worth more than the same hundred pounds next year. Converting a future amount into today's money is called discounting, and the conversion is a multiplication. If the interest rate is fixed, discounting multiplies the balance by a decaying exponential as time moves forward. In the discounted units the interest term disappears from the equation, exactly because the discounting has already accounted for it, and what remains says only that the discounted balance changes at the discounted rate of deposits. The integrating factor is precisely that change of units.

### 1.2 The standard form, one symbol at a time

Every first-order linear equation in this course can be written in the standard form

$$
\frac{dy}{dx}+P(x)\,y=Q(x) .
$$

Each ingredient deserves a name. The letter $x$ is the independent variable: it is the quantity we control or observe, such as time. The letter $y$ is the dependent variable: it is the unknown function of $x$ that we are trying to find, so $y$ really means $y(x)$. The symbol $\frac{dy}{dx}$ is the derivative of $y$ with respect to $x$, that is, the rate at which $y$ changes as $x$ changes. The symbol $P(x)$ is a known function of $x$ alone, called the coefficient function; it multiplies $y$ and is the part of the equation that acts proportionally to the unknown. The symbol $Q(x)$ is also a known function of $x$ alone, called the forcing function or the right-hand side; it does not contain $y$ at all.

The equation is called first order because the highest derivative appearing in it is the first derivative. It is called linear because the unknown $y$ and its derivative $\frac{dy}{dx}$ each appear to the first power, are never multiplied together, and are never placed inside a function such as a sine, a square root, or an exponential. That is the exact sense in which the word linear is used throughout the course, and it is a statement about how $y$ appears, not about how $x$ appears. The functions $P$ and $Q$ may be as complicated as we like in $x$; a term such as $x^{3}\sin x$ in the position of $Q$ does not disturb linearity, while a term such as $y^{2}$ does.

Two special names are attached to particular choices of $Q$. When $Q(x)=0$ for all $x$ in the interval of interest, the equation is called homogeneous. When $Q$ is not identically zero, the equation is called non-homogeneous, and $Q$ is the forcing term. The homogeneous case is the one in which the account receives no deposits, and it is always solvable by separating variables, which gives a useful check on the general method.

A concrete illustration with small numbers fixes the vocabulary. The equation

$$
\frac{dy}{dx}+2y=6
$$

has $P(x)=2$ and $Q(x)=6$, both constant. It is first order, it is linear, and it is non-homogeneous. The equation

$$
\frac{dy}{dx}+2xy=4x
$$

has $P(x)=2x$ and $Q(x)=4x$. Both depend on $x$, and both are perfectly legal, because neither contains $y$. The equation

$$
x\frac{dy}{dx}+y=x^{3}
$$

is not yet in standard form, because the derivative is multiplied by $x$. Dividing every term by $x$ produces $\frac{dy}{dx}+\frac{1}{x}y=x^{2}$, which is standard form with $P(x)=\frac{1}{x}$ and $Q(x)=x^{2}$. Bringing an equation to standard form is always the first move, and forgetting it is the most common single mistake in the topic.

### 1.3 The recognition test

Before any method is applied, the equation must be classified. The following four questions decide the matter, and they are asked in this order.

1. Is the highest derivative present the first derivative? If a second derivative appears, the equation belongs to a later lesson.
2. After clearing fractions on the derivative, do $y$ and $\frac{dy}{dx}$ each appear only to the first power?
3. Is the coefficient of $\frac{dy}{dx}$ a function of $x$ alone, so that dividing by it leaves a clean equation?
4. Once the equation is in the form $\frac{dy}{dx}+(\text{something})y=(\text{something})$, is the multiplier of $y$ free of $y$, and is the right-hand side free of $y$?

A yes to all four means the equation is linear and the integrating-factor method applies directly. A no to question two means it is non-linear, and either a substitution is needed or the equation is outside this topic.

The test is applied to a list of examples in the table below. The middle column records the verdict and the right-hand column records the reason, because the reason is what an examiner wants to see.

| Equation | Linear in standard form | Reason |
| --- | --- | --- |
| $\frac{dy}{dx}+3y=x^{2}$ | Yes | $y$ and its derivative are to the first power, coefficients depend on $x$ alone |
| $\frac{dy}{dx}=x-y$ | Yes | Rearranged it is $\frac{dy}{dx}+y=x$, with $P=1$ and $Q=x$ |
| $x\frac{dy}{dx}+2y=x^{3}$ | Yes | Dividing by $x$ gives $P=\frac{2}{x}$ and $Q=x^{2}$ |
| $\frac{dy}{dx}+y^{2}=x$ | No | The term $y^{2}$ is a non-linear power of the unknown |
| $y\frac{dy}{dx}=x$ | No | The unknown multiplies its own derivative |
| $\frac{dy}{dx}+\sin y=x$ | No | A non-linear function of $y$ appears |
| $\frac{dy}{dx}+xy=y^{3}$ | No | This is Bernoulli with $n=3$ and is reducible, not linear |
| $\frac{dy}{dx}+y=xe^{x}$ | Yes | The exponential involves $x$ only, so it sits in $Q$ |

The distinction between the fourth and the last two rows is worth stating plainly, since it is the entry point for the second half of the topic. An equation that fails the test may still be turned into a linear equation by a substitution. The equation $\frac{dy}{dx}+xy=y^{3}$ is not linear, but the substitution $v=y^{-2}$ makes it linear in $v$. That is the content of Bernoulli's method, discussed from Section 1.7 onwards.

### 1.4 What the two functions are allowed to be

The coefficient function $P$ and the forcing function $Q$ are given data. They may be constants, powers of $x$, exponentials, logarithms, trigonometric functions, or sums and products of these. They may also be zero. Three facts about them govern the behaviour of the solution and are worth memorising in words before any formula appears.

The sign of $P$ decides whether the homogeneous part of the solution grows or decays. When $P$ is a positive constant, the homogeneous solution carries the factor $e^{-Px}$ and dies away, so the equation is stable in the sense that the memory of the initial state fades. When $P$ is a negative constant, say $P=-3$, the homogeneous solution carries $e^{3x}$ and grows without bound, so the equation is unstable.

The size of $Q$ relative to $P$ decides the long-term level of the solution when both are constant. If $P=2$ and $Q=6$, the solution settles at the value $3$, which is the ratio of the forcing to the coefficient. That ratio is the equilibrium of the equation, the value at which the derivative would be zero.

The points where $P$ or $Q$ fails to be defined are points where the solution may fail to exist, and they must be excluded from the interval on which the answer is claimed. For example, $P(x)=\frac{1}{x}$ is undefined at the origin, so a solution involving $\frac{1}{x}$ can only be asserted on an interval that avoids the origin. This is not a technicality to be brushed aside; an answer valid on the whole real line and an answer valid only for positive $x$ are different answers.

### 1.5 What it means to solve such an equation

A solution of a first-order equation is a function $y$ which, when substituted into the equation together with its derivative, makes the two sides equal for every $x$ in some interval. The general solution is the whole family of such functions, and because the equation is first order the family contains exactly one arbitrary constant. Choosing a value for that constant gives a particular solution. Specifying the value of $y$ at one point, called an initial condition, selects exactly one member of the family, provided the coefficient functions are continuous near that point.

The count of constants is the cheapest available check on any answer. A first-order equation whose general solution contains no constant, or contains two constants, is wrong, and the error can be found before any substitution is attempted. In this topic the constant appears when both sides are integrated once, and it is conventionally written $C$.

Every answer should be checked by substitution. The check is mechanical: differentiate the proposed solution, add $P$ times the solution, and confirm that the result is $Q$. Because the calculation reuses the same derivative that produced the answer, it catches sign errors, dropped constants, and mis-integrated exponentials, which between them account for the great majority of lost marks in this topic.

### 1.6 The integrating factor in words

The left-hand side of the standard form, $\frac{dy}{dx}+Py$, is not quite the derivative of anything familiar. But the derivative of the product $my$, where $m$ is some function of $x$, is given by the product rule as

$$
\frac{d}{dx}\left(my\right)=m\frac{dy}{dx}+\frac{dm}{dx}\,y .
$$

Compare this with the left-hand side multiplied by $m$, which is $m\frac{dy}{dx}+mPy$. The first terms agree. The second terms agree precisely when

$$
\frac{dm}{dx}=mP .
$$

That is a separable equation for the helper $m$, and it is easy to solve: dividing by $m$ gives $\frac{1}{m}\frac{dm}{dx}=P$, and integrating gives $\ln m=\int P\,dx$, so

$$
m=e^{\int P\,dx} .
$$

This $m$ is the integrating factor. The name is descriptive: it is the factor that, once inserted, turns the sum of two terms into one exact derivative, which can then be integrated.

With small numbers the whole construction is transparent. For $P=2$ the condition is $\frac{dm}{dx}=2m$, whose solution is $m=e^{2x}$, since the derivative of $e^{2x}$ is $2e^{2x}$. Multiplying $\frac{dy}{dx}+2y=6$ by $e^{2x}$ gives

$$
e^{2x}\frac{dy}{dx}+2e^{2x}y=6e^{2x},
$$

and the left-hand side is exactly $\frac{d}{dx}\left(ye^{2x}\right)$, because the product rule produces $e^{2x}\frac{dy}{dx}+2e^{2x}y$. The equation has become

$$
\frac{d}{dx}\left(ye^{2x}\right)=6e^{2x},
$$

which can be integrated directly to give $ye^{2x}=3e^{2x}+C$, hence $y=3+Ce^{-2x}$. That is the entire method, and every later example is the same three moves with different functions in place of $2$ and $6$.

The phrase "an integrating factor" hides a small freedom which is worth naming early. If $m$ satisfies $\frac{dm}{dx}=mP$, then so does $5m$, because the constant multiplies both sides. Multiplying the equation by $5m$ instead of $m$ multiplies both sides by $5$, and a common factor cancels, so the solution is unchanged. In practice one always chooses the simplest positive representative, discarding any constant of integration inside the exponent. That discarding is legitimate and is not the same as ignoring a constant in the final answer.

### 1.7 Bernoulli equations in words

The second family of equations in this topic looks almost linear but is not. A Bernoulli equation has the form

$$
\frac{dy}{dx}+P(x)\,y=Q(x)\,y^{n},
$$

where $n$ is a fixed number. When $n=0$ the right-hand side is $Q(x)$, and the equation is already linear. When $n=1$ the right-hand side is $Q(x)y$, and the equation is separable. For every other value of $n$ the equation is genuinely non-linear, and the extra power of $y$ is exactly what defeats the integrating factor: the left-hand side can be made into a derivative, but the right-hand side still contains an unknown power of $y$, so the integration cannot be completed.

The cure is a change of variable that removes the offending power. Divide the whole equation by $y^{n}$. The result is

$$
y^{-n}\frac{dy}{dx}+P(x)\,y^{1-n}=Q(x).
$$

Now put $v=y^{1-n}$. Differentiating $v$ with respect to $x$ by the chain rule gives $\frac{dv}{dx}=(1-n)y^{-n}\frac{dy}{dx}$, so the combination $y^{-n}\frac{dy}{dx}$ is $\frac{1}{1-n}\frac{dv}{dx}$. Substituting both facts turns the equation into

$$
\frac{1}{1-n}\frac{dv}{dx}+P(x)\,v=Q(x),
$$

and multiplying by $1-n$ gives a first-order linear equation for $v$, namely

$$
\frac{dv}{dx}+(1-n)P(x)\,v=(1-n)Q(x) .
$$

The equation for $v$ is solved by the integrating-factor method of the previous subsection, and the answer is then translated back by replacing $v$ with $y^{1-n}$.

Small numbers make the substitution concrete. For $n=2$ we have $1-n=-1$, so $v=y^{-1}=\frac{1}{y}$; a Bernoulli equation with a square on the right becomes a linear equation in the reciprocal of $y$. For $n=3$ we have $v=y^{-2}$. For $n=5$ we have $v=y^{-4}$. For $n=-1$ we have $v=y^{2}$, and for $n=\frac{1}{2}$ we have $v=y^{1/2}$, which is the square root of $y$. The formula covers all of these with one rule.

One restriction must be stated at the moment of division. Dividing by $y^{n}$ is legitimate only where $y\neq 0$. If $y$ vanishes at some point, the division is invalid there, and any solution obtained by the method is asserted only on an interval where $y$ keeps a fixed sign. Moreover, when $n>0$ the function $y=0$ is itself a solution of the original equation, because both sides vanish, and this solution is usually not recovered from the general family. It is a genuine extra solution, not an artefact.

### 1.8 When $x$ is the better unknown

There is a third situation, common in exercises, in which the equation is not linear in $y$ but becomes linear if the roles of the variables are exchanged. Suppose the equation can be solved for $\frac{dx}{dy}$ rather than for $\frac{dy}{dx}$. Then $x$ is treated as the unknown function of $y$, and the standard form becomes

$$
\frac{dx}{dy}+P(y)\,x=Q(y) .
$$

This is the same equation with the letters swapped, so the same integrating factor $e^{\int P\,dy}$ and the same three steps apply. Nothing new has to be memorised; only the decision of which variable is independent has to be made.

A simple instance shows how the decision is taken. The equation

$$
\frac{dy}{dx}=\frac{y}{y-x}
$$

has $y$ inside a fraction on the right, so it is not linear in $y$. Taking reciprocals of both sides gives $\frac{dx}{dy}=\frac{y-x}{y}=1-\frac{x}{y}$, which rearranges to $\frac{dx}{dy}+\frac{1}{y}x=1$. That is linear in $x$ with $P(y)=\frac{1}{y}$ and $Q(y)=1$, and it is solved by the standard three steps. The lesson is that linearity is a property of a chosen pair of variables, not an absolute property of the equation.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Multiplying by a nowhere-zero factor preserves the solutions

> **Lemma (Equivalence under multiplication).** Let $m(x)$ be defined and non-zero on an interval $I$. Then on $I$ the equation $\frac{dy}{dx}+Py=Q$ and the equation $m\frac{dy}{dx}+mPy=mQ$ have exactly the same solutions.

The proof is a single observation with an important hypothesis. If $y$ satisfies the first equation, multiplying the identity by $m(x)$ gives the second at every point of $I$. Conversely, if $y$ satisfies the second, dividing by $m(x)$ gives the first, and division is permitted precisely because $m$ never vanishes on $I$. If $m$ were allowed to vanish somewhere, the two equations could differ at that point, and a solution of the multiplied equation need not solve the original there. This is why the integrating factor is always chosen positive: an exponential is positive everywhere, so the hypothesis is automatically satisfied and the equivalence is exact.

### 2.2 The product-rule identity

> **Theorem (The integrating factor makes the left side a derivative).** Let $P$ be continuous on an interval $I$ and let $m(x)=e^{\int P\,dx}$ be any positive antiderivative-based exponential. Then for every differentiable $y$,
>
> $$
> m\left(\frac{dy}{dx}+Py\right)=\frac{d}{dx}\left(my\right).
> $$

The statement is an identity, not an equation to be solved, and that is what makes it powerful: it holds for every function $y$, so it may be applied to the unknown without knowing the unknown. Written out, the right-hand side is $m\frac{dy}{dx}+m'y$ by the product rule, and $m'=mP$ by the defining property of $m$, so the two sides agree term by term. The proof is given in full in Section 3.1.

### 2.3 The solution formula

> **Theorem (General solution of the linear equation).** Let $P$ and $Q$ be continuous on an interval $I$. Then the general solution of $\frac{dy}{dx}+Py=Q$ on $I$ is
>
> $$
> y\,e^{\int P\,dx}=\int Q\,e^{\int P\,dx}\,dx+C ,
> $$
>
> equivalently
>
> $$
> y=e^{-\int P\,dx}\left(\int Q\,e^{\int P\,dx}\,dx+C\right),
> $$
>
> where the inner integral denotes any fixed antiderivative and $C$ is an arbitrary constant.

The formula is worth reading as a sentence rather than as a symbol string. It says: multiply the solution by the integrating factor, and what you get is the integral of the forcing function also multiplied by the integrating factor, plus a constant. The constant is the only place where the initial state enters, and the factor $e^{-\int P\,dx}$ in front converts the integrated quantity back to the original units.

The formula also contains the homogeneous case as a special case. When $Q=0$, the integral vanishes and the solution is $y=Ce^{-\int P\,dx}$, which is what separation of variables gives. When $Q$ is constant and $P$ is a non-zero constant, the integral produces a constant multiple of $e^{Px}$, which cancels the factor in front and leaves a constant particular solution together with the decaying homogeneous term.

### 2.4 The homogeneous case

> **Lemma (Zero forcing).** If $Q(x)=0$ on $I$, the general solution of $\frac{dy}{dx}+Py=0$ is
>
> $$
> y=C\,e^{-\int P\,dx} .
> $$

The lemma follows from the formula, but it also follows directly and more instructively by separating variables: $\frac{1}{y}\frac{dy}{dx}=-P$ gives $\ln|y|=-\int P\,dx+k$, and exponentiating gives $y=\pm e^{k}e^{-\int P\,dx}$, which is the stated form with $C=\pm e^{k}$. The absolute value and the sign both disappear into the single constant $C$, which may be positive or negative. The only solution not of this form is $y=0$, obtained by taking $C=0$.

### 2.5 One initial condition determines one solution

> **Theorem (Existence and uniqueness for the linear equation).** Let $P$ and $Q$ be continuous on an interval $I$ containing $x_{0}$, and let $y_{0}$ be any real number. Then the problem $\frac{dy}{dx}+Py=Q$ with $y(x_{0})=y_{0}$ has exactly one solution on $I$, namely
>
> $$
> y=e^{-\int_{x_{0}}^{x}P(t)\,dt}\left(y_{0}+\int_{x_{0}}^{x}Q(s)\,e^{\int_{x_{0}}^{s}P(t)\,dt}\,ds\right).
> $$

Two features of this statement matter in practice. First, the hypothesis is continuity of $P$ and $Q$ on the whole interval, which is a much weaker requirement than the corresponding hypothesis for non-linear equations; for linear equations continuity is enough, and no condition on $\frac{\partial f}{\partial y}$ is needed. Second, the definite-integral form removes the arbitrary constant entirely, so there is nothing left to determine after the formula is applied. That makes it the safest form for initial-value problems, especially when the integrals are awkward.

### 2.6 The Bernoulli reduction

> **Theorem (Reduction of Bernoulli's equation).** Let $n\neq 1$ be a real constant and let $P$ and $Q$ be continuous on $I$. On any subinterval where $y$ does not vanish, the substitution $v=y^{1-n}$ converts
>
> $$
> \frac{dy}{dx}+P(x)\,y=Q(x)\,y^{n}
> $$
>
> into the linear equation
>
> $$
> \frac{dv}{dx}+(1-n)P(x)\,v=(1-n)Q(x).
> $$

The hypothesis $n\neq 1$ is not decorative: when $n=1$ the exponent $1-n$ is zero, so $v=1$ identically and the substitution carries no information. That case is handled separately and is in fact separable. The hypothesis that $y$ does not vanish is also essential, because the derivation divides by $y^{n}$; where $y=0$ the transformation is undefined and the original equation must be examined on its own.

> **Lemma (The two degenerate exponents).** If $n=0$, Bernoulli's equation is linear and is solved by the integrating-factor method with $Q$ unchanged. If $n=1$, Bernoulli's equation is separable and its general solution is
>
> $$
> y=C\,e^{\int\left(Q-P\right)dx} .
> $$

For $n=1$ the equation is $\frac{dy}{dx}=(Q-P)y$, and dividing by $y$ and integrating gives the stated family on any interval where $y$ does not vanish, together with the zero solution. These two cases are examined first in any examination question, because a candidate who substitutes blindly into the Bernoulli formula when $n=1$ divides by zero.

### 2.7 Reduction by exchanging the variables

> **Lemma (Reciprocal form).** Suppose that on an interval the equation can be solved for $\frac{dx}{dy}$ in the form
>
> $$
> \frac{dx}{dy}+A(y)\,x=B(y),
> $$
>
> with $A$ and $B$ continuous. Then the general solution is
>
> $$
> x\,e^{\int A\,dy}=\int B\,e^{\int A\,dy}\,dy+C .
> $$

The lemma is not a new theorem; it is Theorem 2.3 with $x$ and $y$ interchanged. Its value is practical, because many equations that look hopeless in the form $\frac{dy}{dx}=f(x,y)$ become routine once $x$ is treated as the unknown. The hypothesis that the equation can be solved for $\frac{dx}{dy}$ requires $\frac{dy}{dx}\neq 0$, which again restricts the interval, and the restriction should be stated when the answer is given.

### 2.8 Behaviour of solutions when the coefficients are constant

> **Theorem (Constant-coefficient asymptotics).** Let $P=p\neq 0$ and $Q=q$ be constants. Then every solution of $\frac{dy}{dx}+py=q$ has the form
>
> $$
> y=\frac{q}{p}+C\,e^{-px},
> $$
>
> so $y\to\frac{q}{p}$ as $x\to+\infty$ when $p>0$, and the solution is unbounded when $p<0$ unless $C=0$.

The value $\frac{q}{p}$ is the equilibrium of the equation, the constant function that makes the derivative zero. The theorem says that when $p>0$ the equilibrium is attracting and every solution approaches it, and when $p<0$ it is repelling and every non-equilibrium solution runs away from it. This is the mathematical content of the savings-account picture: a positive interest rate corresponds to negative $p$ in the standard form, and the balance grows without bound, whereas a cooling body corresponds to positive $p$ and approaches room temperature.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Deriving the integrating factor from the product rule

The derivation begins with a wish rather than with a calculation. The left-hand side of the standard form is a sum of two terms, one containing the derivative of the unknown and one containing the unknown itself; such a sum cannot be integrated directly. But a sum of exactly that shape does appear in one familiar place, namely the product rule. If we can arrange for our sum to be the product rule applied to some product, then the sum becomes a single derivative and the impasse is broken.

So we ask: is there a function $m$, depending on $x$ alone, such that multiplying the left-hand side by $m$ produces the derivative of a product? Write the product as $m y$ and expand its derivative:

$$
\frac{d}{dx}\left(m y\right)=m\frac{dy}{dx}+\frac{dm}{dx}y .
$$

The left-hand side of the standard form, after multiplication by the same $m$, reads

$$
m\frac{dy}{dx}+m P y .
$$

Now compare the two expressions term by term. The first terms are identical. The second terms are identical exactly when

$$
\frac{dm}{dx}=mP .
$$

This is the condition we need, and it is a first-order equation for $m$ alone, with no $y$ in it. It is separable, so we solve it by dividing by $m$:

$$
\frac{1}{m}\frac{dm}{dx}=P .
$$

Integrating both sides with respect to $x$ gives

$$
\ln m=\int P\,dx+K ,
$$

where $K$ is a constant. Exponentiating gives $m=e^{K}e^{\int P\,dx}$. Since the constant factor $e^{K}$ cancels from both sides of the differential equation when we multiply through, we take the simplest choice $K=0$ and obtain

$$
m=e^{\int P\,dx} .
$$

This is the integrating factor. Note carefully what has been proved and what has not. We have proved that if $m$ is defined this way, then $m$ times the left-hand side is the derivative of $m y$. We have not yet used the right-hand side; that comes next.

### 3.2 The step that completes the solution

Multiply the whole equation $\frac{dy}{dx}+Py=Q$ by the integrating factor $m$. The equation becomes

$$
m\frac{dy}{dx}+mPy=mQ ,
$$

and by the identity just proved the left-hand side is $\frac{d}{dx}\left(my\right)$. Hence

$$
\frac{d}{dx}\left(my\right)=mQ .
$$

This is the decisive line. It says that the derivative of the single quantity $my$ is known explicitly, because $m$ and $Q$ are known functions. Integrating both sides with respect to $x$ recovers the quantity itself:

$$
m y=\int m Q\,dx+C .
$$

Dividing by $m$, which is legitimate because an exponential is never zero, gives the general solution

$$
y=e^{-\int P\,dx}\left(\int Q\,e^{\int P\,dx}\,dx+C\right).
$$

The structure of this formula repays a moment of attention. The factor $e^{\int P\,dx}$ appears inside the integral, multiplying the forcing function; that factor converts the forcing into the same units as the integrated quantity. The factor $e^{-\int P\,dx}$ outside converts the result back. The constant $C$ sits inside the bracket, so it is multiplied by the outside factor, and that is exactly how the homogeneous solution appears as part of the family.

### 3.3 Why the two integrals may be chosen freely

A point that confuses beginners is that the symbol $\int P\,dx$ appears to denote infinitely many functions, differing by constants, and the formula seems to depend on which one is chosen. It does not. Suppose we replace $\int P\,dx$ by $\int P\,dx+k$ for some constant $k$. The integrating factor becomes $e^{k}e^{\int P\,dx}$, a constant multiple of the previous one. The left-hand side $my$ is multiplied by $e^{k}$, and the right-hand side $\int mQ\,dx+C$ is multiplied by the same $e^{k}$ inside the integral, with the constant of integration absorbing the difference. Dividing through by $e^{k}$ returns precisely the original solution.

The same reasoning shows why we never write a constant of integration inside the exponent while computing. Writing $e^{\int P\,dx+C}$ is harmless but pointless, because the $e^{C}$ is a constant multiplier that cancels. Beginners who do write it usually end up with an extra constant in the final answer, which is then miscounted.

A worked miniature makes the cancellation visible. Take $P=2$ and choose the indefinite integral $2x+7$ instead of $2x$. The integrating factor is $e^{2x+7}$. Multiplying $\frac{dy}{dx}+2y=6$ by it gives $\frac{d}{dx}\left(ye^{2x+7}\right)=6e^{2x+7}$, so $ye^{2x+7}=3e^{2x+7}+C$, and dividing by $e^{2x+7}$ gives $y=3+Ce^{-2x-7}$. But $Ce^{-7}$ is just another constant, so this is the same family as $y=3+C'e^{-2x}$. The solution set is unchanged, which is exactly what the argument above predicts.

### 3.4 The three-step procedure

Every linear equation in this topic is solved by the same three steps, and the steps should be written down explicitly in an examination.

Step 1. Write the equation in standard form $\frac{dy}{dx}+Py=Q$ and identify $P$ and $Q$ as functions of $x$. If the derivative is multiplied by a coefficient, divide the whole equation by that coefficient first, and record any values of $x$ where the division fails.

Step 2. Compute $\int P\,dx$ and then the integrating factor $e^{\int P\,dx}$. Only the simplest antiderivative is needed, with no added constant.

Step 3. Write the solution as $\left(\text{integrating factor}\right)\cdot y=\int Q\cdot\left(\text{integrating factor}\right)dx+C$, perform the integral on the right, and divide by the integrating factor. State the answer in the simplest form and note the interval on which it is valid.

The order of the steps is not optional. Computing the integral of $Q$ before multiplying by the integrating factor is the single most common mechanical error, and it produces an answer that fails the substitution check immediately.

### 3.5 The Bernoulli procedure

Bernoulli equations need two preliminary moves before the three steps of the previous subsection can be applied.

Step 1. Identify $n$, the exponent on the right-hand side, and confirm that $n$ is neither $0$ nor $1$. If $n=0$ the equation is already linear; if $n=1$ it is separable.

Step 2. Divide the whole equation by $y^{n}$, and note that this is valid only where $y\neq 0$. Record that restriction, and separately record that $y=0$ is a solution when $n>0$.

Step 3. Substitute $v=y^{1-n}$, compute $\frac{dv}{dx}=(1-n)y^{-n}\frac{dy}{dx}$, and rewrite the equation as $\frac{dv}{dx}+(1-n)Pv=(1-n)Q$.

Step 4. Solve the resulting linear equation in $v$ by the three-step method, then replace $v$ by $y^{1-n}$ and, where possible, solve for $y$. Check by substituting into the original equation, not into the transformed one.

The fourth step is where marks are lost. Substituting back into the linearised equation only confirms that the algebra of the substitution was consistent; it does not confirm that the original non-linear equation is satisfied. The check must use the original equation.

### 3.6 The procedure when $x$ is the unknown

When the equation is not linear in $y$ but can be solved for $\frac{dx}{dy}$, the procedure is the same three steps with the letters exchanged.

Step 1. Rewrite the equation as $\frac{dx}{dy}+A(y)x=B(y)$ by taking reciprocals and rearranging.

Step 2. Compute the integrating factor $e^{\int A\,dy}$.

Step 3. Write $x e^{\int A\,dy}=\int B e^{\int A\,dy}\,dy+C$, evaluate, and divide. Then convert back to the original variables if the question asks for $y$ explicitly, or leave the answer as $x$ in terms of $y$ when that is cleaner.

### 3.7 The substitution check

The check for a linear equation is short enough that it should always be performed. Given a proposed solution $y=\phi(x)$, compute $\frac{dy}{dx}$ and form $\frac{dy}{dx}+P\phi$. If the algebra is correct, the terms involving the arbitrary constant cancel identically, and what remains is $Q$. The cancellation of the constant is the signature of a correct answer; if the constant survives, the integrating factor or its integral is wrong.

For a Bernoulli equation the same check is applied to the original equation, and it is worth noting that the check is often easier in the implicit form. If the answer is given as $\frac{1}{y^{2}}=x+\frac{1}{2}+Ce^{2x}$, differentiating both sides implicitly and substituting is faster than solving for $y$ first.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: solve $\frac{dy}{dx}+2y=6$

### 4.2 Solution: constant coefficients, three steps

Step 1. The equation is already in standard form, with $P=2$ and $Q=6$. Both are constants, so no division is needed and no point of the line has to be excluded.

Step 2. Compute the integral of the coefficient and then the integrating factor.

$$
\int P\,dx=\int 2\,dx=2x, \qquad e^{\int P\,dx}=e^{2x} .
$$

Step 3. Write the solution in the product form and evaluate the integral on the right.

$$
y e^{2x}=\int 6 e^{2x}\,dx
$$

The integral of $6e^{2x}$ is $3e^{2x}$, since differentiating $3e^{2x}$ returns $6e^{2x}$.

$$
y e^{2x}=3e^{2x}+C
$$

Step 4. Divide by the integrating factor to isolate $y$.

$$
y=3+C e^{-2x}
$$

Step 5. Check by substitution. Here $\frac{dy}{dx}=-2Ce^{-2x}$, so

$$
\frac{dy}{dx}+2y=-2Ce^{-2x}+2\left(3+Ce^{-2x}\right)=6 ,
$$

and the constant has cancelled as it must. The general solution is $y=3+Ce^{-2x}$, and it approaches the equilibrium value $3$ as $x$ grows.

### 4.3 Problem: solve $\frac{dy}{dx}+y=3$ subject to $y(0)=7$

### 4.4 Solution: find the family, then impose the condition

Step 1. In standard form, $P=1$ and $Q=3$. The integrating factor is

$$
e^{\int 1\,dx}=e^{x} .
$$

Step 2. Multiply through and integrate.

$$
y e^{x}=\int 3 e^{x}\,dx=3e^{x}+C
$$

Step 3. Divide by $e^{x}$ to obtain the general solution.

$$
y=3+C e^{-x}
$$

Step 4. Impose the condition at $x=0$, where $e^{0}=1$.

$$
7=3+C\cdot 1 \quad\text{so}\quad C=4
$$

Step 5. State the particular solution and check it at the initial point.

$$
y=3+4e^{-x}, \qquad y(0)=3+4=7
$$

Step 6. Check the equation itself. Since $\frac{dy}{dx}=-4e^{-x}$, we get $\frac{dy}{dx}+y=-4e^{-x}+3+4e^{-x}=3$, which is the required right-hand side. The solution is valid for all real $x$, because the coefficients are continuous everywhere.

### 4.5 Problem: solve $\frac{dy}{dx}+y=x$

### 4.6 Solution: the right-hand side needs integration by parts

Step 1. The equation is in standard form with $P=1$ and $Q=x$. The integrating factor is the same as in the previous example.

$$
e^{\int 1\,dx}=e^{x}
$$

Step 2. Multiply through, so that the left-hand side becomes one derivative.

$$
\frac{d}{dx}\left(y e^{x}\right)=x e^{x}
$$

Step 3. Integrate the right-hand side by parts. Take $u=x$ and $dv=e^{x}dx$, so that $du=dx$ and $v=e^{x}$. Then

$$
\int x e^{x}\,dx=x e^{x}-\int e^{x}\,dx=x e^{x}-e^{x} .
$$

Step 4. Insert the result and add the constant.

$$
y e^{x}=x e^{x}-e^{x}+C
$$

Step 5. Divide by $e^{x}$.

$$
y=x-1+C e^{-x}
$$

Step 6. Check. Here $\frac{dy}{dx}=1-Ce^{-x}$, so

$$
\frac{dy}{dx}+y=1-Ce^{-x}+x-1+Ce^{-x}=x ,
$$

and the constant cancels. The general solution is $y=x-1+Ce^{-x}$. Notice that the particular part $x-1$ is a polynomial of the same degree as $Q$, which is a useful sanity check when $Q$ is a polynomial and $P$ is constant.

### 4.7 Problem: solve $\frac{dy}{dx}+\frac{1}{x}y=3$ for $x>0$

### 4.8 Solution: a variable coefficient produces a variable factor

Step 1. The equation is in standard form with $P=\frac{1}{x}$ and $Q=3$. Since $P$ is undefined at the origin, we work on the interval $x>0$ where it is continuous.

Step 2. Compute the integral of the coefficient.

$$
\int \frac{1}{x}\,dx=\ln x
$$

On the interval $x>0$ no absolute value is needed, because $x$ is already positive.

Step 3. Form the integrating factor.

$$
e^{\ln x}=x
$$

Step 4. Multiply through and integrate.

$$
\frac{d}{dx}\left(xy\right)=3x
$$

$$
xy=\frac{3x^{2}}{2}+C
$$

Step 5. Divide by $x$.

$$
y=\frac{3x}{2}+\frac{C}{x}
$$

Step 6. Check. Differentiating gives $\frac{dy}{dx}=\frac{3}{2}-\frac{C}{x^{2}}$, and adding $\frac{1}{x}y$ gives

$$
\frac{3}{2}-\frac{C}{x^{2}}+\frac{3}{2}+\frac{C}{x^{2}}=3 ,
$$

so the equation holds for every $x>0$. The answer must be reported with the restriction $x>0$, since the solution has a pole at the origin and the coefficient is not defined there.

### 4.9 Problem: solve $\frac{dy}{dx}+2xy=0$

### 4.10 Solution: the homogeneous case by separation

Step 1. Here $Q=0$, so the equation is homogeneous. The integrating factor is still available, and it is

$$
e^{\int 2x\,dx}=e^{x^{2}} .
$$

Step 2. Multiply through; the right-hand side is zero, so the equation says that a derivative vanishes.

$$
\frac{d}{dx}\left(y e^{x^{2}}\right)=0
$$

Step 3. Integrate once.

$$
y e^{x^{2}}=C
$$

Step 4. Divide by the exponential.

$$
y=C e^{-x^{2}}
$$

Step 5. Confirm by separating variables instead. Dividing the original equation by $y$ gives $\frac{1}{y}\frac{dy}{dx}=-2x$, so $\ln|y|=-x^{2}+k$ and $y=\pm e^{k}e^{-x^{2}}$, which is the same family with $C=\pm e^{k}$. The value $C=0$ gives the zero solution, which separation loses when it divides by $y$.

Step 6. Check. With $\frac{dy}{dx}=-2Cxe^{-x^{2}}$ we get $\frac{dy}{dx}+2xy=-2Cxe^{-x^{2}}+2xC e^{-x^{2}}=0$, as required.

### 4.11 Problem: solve $\frac{dy}{dx}+y=y^{2}$

### 4.12 Solution: a Bernoulli equation with $n=2$

Step 1. Identify the type. The right-hand side is $y^{2}$, so this is Bernoulli with $P=1$, $Q=1$ and $n=2$. Since $n$ is neither $0$ nor $1$, the substitution is needed.

Step 2. Divide the whole equation by $y^{2}$, which is legitimate wherever $y\neq 0$.

$$
y^{-2}\frac{dy}{dx}+y^{-1}=1
$$

Step 3. Put $v=y^{1-n}=y^{-1}$. Differentiating by the chain rule gives

$$
\frac{dv}{dx}=-y^{-2}\frac{dy}{dx}, \qquad\text{so}\qquad y^{-2}\frac{dy}{dx}=-\frac{dv}{dx} .
$$

Step 4. Substitute into the divided equation.

$$
-\frac{dv}{dx}+v=1
$$

Step 5. Rearrange into standard form by multiplying by $-1$.

$$
\frac{dv}{dx}-v=-1
$$

Step 6. Solve this linear equation for $v$. Here the coefficient is $P=-1$ and the forcing is $Q=-1$, so the integrating factor is

$$
e^{\int(-1)\,dv}=e^{-x} .
$$

Step 7. Multiply through and integrate. Note that the integral is with respect to $x$, since $v$ is a function of $x$.

$$
\frac{d}{dx}\left(v e^{-x}\right)=-e^{-x}
$$

$$
v e^{-x}=e^{-x}+C
$$

Step 8. Divide by $e^{-x}$.

$$
v=1+C e^{x}
$$

Step 9. Translate back using $v=y^{-1}$.

$$
\frac{1}{y}=1+C e^{x}, \qquad\text{so}\qquad y=\frac{1}{1+C e^{x}}
$$

Step 10. Check in the original equation. Differentiating gives

$$
\frac{dy}{dx}=-\frac{C e^{x}}{\left(1+C e^{x}\right)^{2}},
$$

and adding $y$ gives

$$
\frac{dy}{dx}+y=\frac{-Ce^{x}+1+Ce^{x}}{\left(1+Ce^{x}\right)^{2}}=\frac{1}{\left(1+Ce^{x}\right)^{2}}=y^{2},
$$

which is exactly the right-hand side. The general solution is $y=\left(1+Ce^{x}\right)^{-1}$, valid on any interval where the denominator does not vanish. The solution $y=0$, lost when we divided by $y^{2}$, is also a solution of the original equation, and it corresponds to the limiting case in which the constant tends to infinity.

### 4.13 Problem: solve $\frac{dy}{dx}=\frac{y}{y-x}$

### 4.14 Solution: exchange the roles of the variables

Step 1. Attempt the recognition test. The right-hand side contains $y$ in the denominator, so the equation is not linear in $y$, and no Bernoulli power is present either.

Step 2. Take reciprocals. Since $\frac{dy}{dx}$ and $\frac{dx}{dy}$ are reciprocal on any interval where neither vanishes,

$$
\frac{dx}{dy}=\frac{y-x}{y}=1-\frac{x}{y} .
$$

Step 3. Rearrange into standard form with $x$ as the unknown and $y$ as the independent variable.

$$
\frac{dx}{dy}+\frac{1}{y}x=1
$$

Step 4. Identify $A(y)=\frac{1}{y}$ and $B(y)=1$, and compute the integrating factor, working on $y>0$.

$$
e^{\int \frac{1}{y}\,dy}=e^{\ln y}=y
$$

Step 5. Multiply through so that the left side becomes a derivative with respect to $y$.

$$
\frac{d}{dy}\left(xy\right)=y
$$

Step 6. Integrate with respect to $y$.

$$
xy=\frac{y^{2}}{2}+C
$$

Step 7. Divide by $y$.

$$
x=\frac{y}{2}+\frac{C}{y}
$$

Step 8. Check by differentiating with respect to $y$.

$$
\frac{dx}{dy}=\frac{1}{2}-\frac{C}{y^{2}}
$$

and

$$
\frac{1}{2}-\frac{C}{y^{2}}+\frac{1}{y}\left(\frac{y}{2}+\frac{C}{y}\right)=\frac{1}{2}-\frac{C}{y^{2}}+\frac{1}{2}+\frac{C}{y^{2}}=1 ,
$$

so the transformed equation holds. Since the transformed equation is equivalent to the original wherever both derivatives exist, the family $x=\frac{y}{2}+\frac{C}{y}$ solves the problem, with $y\neq 0$ required.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Extensions worth knowing

The first extension concerns what happens when the forcing function is itself a solution of the homogeneous equation. Take $P=1$ and $Q=e^{-x}$. The integrating factor is $e^{x}$, and the right-hand side of the product form is $e^{x}\cdot e^{-x}=1$, so the integral is simply $x$. The solution is therefore $y=e^{-x}\left(x+C\right)$, in which a polynomial factor has appeared. In general, when $Q$ is a multiple of $e^{-\int P\,dx}$, the integral produces a factor of $x$; this is the first-order analogue of resonance in second-order equations, and it is worth recognising because it is a favourite examination construction.

The second extension is the logistic equation. The equation $\frac{dy}{dx}=y-y^{2}$ is Bernoulli with $P=-1$, $Q=-1$ and $n=2$, and its solution is $y=\left(1+Ce^{-x}\right)^{-1}$, as computed in Section 4.11 with the sign of the exponent changed. That solution describes a population that starts near zero, grows rapidly, and then levels off at the carrying capacity, which is the value $1$ in this normalisation. The same calculation therefore covers both a pure mathematics exercise and a standard model in population biology, and this is a good illustration of why the substitution $v=y^{1-n}$ is worth knowing.

The third extension is the family of equations that become linear after a substitution chosen by inspection. An equation such as $\frac{dy}{dx}+y=\frac{x}{y}$ is not Bernoulli in the standard sense until it is multiplied through by $y$, which produces $y\frac{dy}{dx}+y^{2}=x$; writing $z=y^{2}$ converts it into a linear equation in $z$. The technique is the same as Bernoulli's, with the substitution chosen to match the powers that actually occur rather than to fit a formula. Recognising that the aim is to make the equation linear, rather than to apply a memorised recipe, is the real skill.

### 5.2 Where the method stops

The method of integrating factors applies to first-order linear equations and to equations that can be made linear. It does not apply to equations such as $\frac{dy}{dx}+y^{2}=x$, which is a Riccati equation; such equations can sometimes be linearised, but only after one particular solution is known, and the procedure is outside this topic. It does not apply to equations in which the unknown appears inside a transcendental function, such as $\frac{dy}{dx}+\sin y=x$, because no algebraic substitution removes a sine.

A second limit is imposed by the interval of validity. The formula is derived under the hypothesis that $P$ and $Q$ are continuous, and the answer is only claimed where that hypothesis holds. A coefficient such as $\frac{1}{x-1}$ forces the solution to be split into the regions $x<1$ and $x>1$, and a single formula cannot describe both, because the solution generally blows up at the excluded point. Similarly, a Bernoulli solution in the form $\frac{1}{y^{2}}=g(x)$ is only real where $g(x)>0$, and the interval must be restricted accordingly.

A third limit concerns the constant of integration. There is exactly one, it appears exactly once, and it must be present in the general solution. When an initial condition is imposed it disappears, but the particular solution should then be checked against the condition explicitly, because an arithmetic slip in solving for $C$ is otherwise invisible.

### 5.3 Common errors and misconceptions

The following mistakes account for most of the lost marks in this topic. Each is stated with the correction that prevents it.

- Treating $P$ and $Q$ as constants when they depend on $x$. The coefficient may be a function such as $\frac{2x}{1+x^{2}}$, and then the integrating factor is not a simple exponential in $x$ but the exponential of an integral that must be evaluated first.
- Using $e^{P}$ as the integrating factor instead of $e^{\int P\,dx}$. The definition requires the exponential of the integral, not the exponential of the coefficient, and the two coincide only in the trivial case $P=0$.
- Forgetting to divide by the coefficient of $\frac{dy}{dx}$. An equation such as $x\frac{dy}{dx}+y=x^{3}$ must first be divided by $x$; otherwise the integrating factor computed from $P=1$ is wrong.
- Integrating $Q$ before multiplying it by the integrating factor. The right-hand side of the product form is $\int Qm\,dx$, not $m\int Q\,dx$, and the two differ whenever $m$ is not constant.
- Adding a constant of integration inside the exponent of the integrating factor. It cancels, so it is harmless but wasteful, and it often leads to a double count of constants in the final answer.
- Losing the constant altogether when the right-hand side integrates to zero. The equation $\frac{d}{dx}\left(my\right)=0$ integrates to $my=C$, not to $my=0$.
- Dividing a Bernoulli equation by $y^{n}$ without recording the restriction $y\neq 0$. The division is invalid where $y$ vanishes, and the solution $y=0$ must be reported separately when $n>0$.
- Substituting $v=y^{1-n}$ and then forgetting the factor $1-n$. The term $\frac{dv}{dx}$ always carries the multiplier $\frac{1}{1-n}$ from the chain rule, and omitting it changes the coefficient of $v$ in the linearised equation.
- Applying the Bernoulli substitution when $n=1$. Then $v=y^{0}=1$ and the method collapses; the equation is separable and should be solved as such.
- Reporting an answer without its interval. A solution containing $\frac{1}{x}$ or $\ln x$ is not valid across the origin, and a complete answer states where it holds.
- Checking the solution in the transformed equation rather than the original. The transformed check verifies only the algebra of the substitution, and it cannot detect an error in the substitution itself.
- Confusing the two directions of the reciprocal trick. When $x$ is treated as a function of $y$, the derivative that appears is $\frac{dx}{dy}$, and the coefficient and forcing are functions of $y$, not of $x$.

### 5.4 What to carry forward

The two ideas in this note that recur throughout the subject are the construction of an integrating factor and the use of a substitution to reduce an equation to a known type. The first is a special case of a general principle in the theory of exact equations: a non-exact equation can often be made exact by multiplication by a suitable factor, and for the linear equation that factor can be written down explicitly. The second is the prototype of every reduction method that follows, including the substitutions that lower the order of second-order equations and the substitutions used for homogeneous equations. Mastery of the three-step procedure and of the Bernoulli substitution is therefore not an isolated skill but the foundation on which the rest of the course is built.