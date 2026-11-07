## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A road with a damaged patch

Imagine a long straight road that you have to describe to someone who has never seen it. Most of the road is perfectly smooth, and over those smooth stretches a single simple rule describes the surface: the height of the road above sea level is, say, two metres plus three times the distance from the start. One rule, one straight line, no surprises.

Now suppose there is a damaged patch somewhere along the road. At that patch the surface buckles, and the simple rule stops working. The road still exists, and a driver still needs to know what happens there, but the description must change. If the damage is a clean crack, the surface still has an orderly shape, and a slightly modified rule describes it: the same straight line, but shifted or steepened by the crack. If the damage is a crater, with the surface dropping away without limit, no simple rule describes it at all, and the best you can do is warn the driver.

That picture is the whole of this topic. A differential equation is a rule that describes an unknown function, just as the straight-line rule described the road. At most points along the axis the rule is well behaved and a simple kind of answer is available: an infinite sum of powers, which behaves like a very long polynomial. At certain special points the rule breaks down. Some of those breakdowns are mild, and a slightly modified version of the same kind of answer still works. Others are severe, and nothing of that kind can be promised.

Think of a second everyday situation that makes the mild case concrete. A recipe written for four people can be scaled to six by multiplying every quantity by one and a half; the recipe is "regular" in the sense that a small change of scale changes the answer in an orderly way. A recipe that says "add salt until it tastes right" cannot be scaled at all, because the instruction has no fixed quantity to multiply. The mild breakdown is the scalable recipe; the severe breakdown is the instruction that resists scaling.

Picture a third situation, which explains why we bother with infinite sums in the first place. A calculator cannot store the exact value of a sine, so it stores a long sum of powers and adds up as many terms as it needs. The sum is the answer, written in a form the machine can handle. A power series solution of a differential equation is exactly that: an answer written as a long sum of powers, because no short formula exists.

None of these pictures involves guessing. The method is systematic, and the theory in this note exists to tell you, before you compute anything, which of the three situations you are in.

### 1.2 What a power series solution is

An ordinary equation such as $3x+2=8$ asks for a number. A differential equation asks for a function, and the function is written $y$, depending on a variable written $x$. The symbol $y'$ means the derivative of $y$, that is, the rate at which $y$ changes as $x$ increases, and $y''$ means the derivative of $y'$, the rate at which the slope itself changes.

Some differential equations can be solved with short formulas. The equation $y''+y=0$ is solved by the sine and the cosine, two familiar functions. Many equations cannot be solved that way, and for those the answer is written as an infinite sum.

> **Definition (power series solution).** A power series solution about a point $x_{0}$ is a function of the form
>
> $$
> y=C_{0}+C_{1}\left(x-x_{0}\right)+C_{2}\left(x-x_{0}\right)^{2}+C_{3}\left(x-x_{0}\right)^{3}+\cdots
> $$
>
> where $C_{0},C_{1},C_{2},\dots$ are fixed numbers, the sum continues without end, and the result satisfies the differential equation on some interval around $x_{0}$.

Take the formula apart one symbol at a time. The letter $x$ is the variable, the input of the function. The number $x_{0}$ is the centre, a fixed point about which the powers are taken; in most of this note the centre is the number zero, which makes every bracket equal to plain $x$. The bracket $\left(x-x_{0}\right)$ is the distance from the centre, and its square, cube and higher powers are the successive terms. The number $C_{0}$ is the value the sum takes when $x$ equals $x_{0}$, because every bracket then vanishes. The number $C_{1}$ is the slope of the sum at the centre, $C_{2}$ controls how the slope bends, and in general $C_{n}$ controls the term of degree $n$. The word solution means that substituting the whole infinite sum into the equation gives an identity, true for every $x$ in the interval; stopping after finitely many terms gives an approximation, not a solution.

Here is a short sum written out, to fix the shape.

$$
y=2+3x+5x^{2}-x^{3}
$$

This is a polynomial, and it is a power series that happens to stop. Its centre is zero, its constant term is two, its coefficient of $x$ is three, its coefficient of $x^{2}$ is five, and its coefficient of $x^{3}$ is minus one. Every power series with finitely many nonzero coefficients looks like this; an infinite power series simply keeps going.

The method for finding such a solution has six steps, and it is worth learning them in order because every worked example follows them.

1. Assume the answer has the sum form, with unknown numbers as coefficients.
2. Differentiate the sum once and twice, term by term.
3. Substitute the sum and its two derivatives into the equation.
4. Rewrite the sums so that every term carries the same power of the bracket.
5. Set the total coefficient of each power equal to zero; this gives a rule, called a recurrence, linking each coefficient to earlier ones.
6. Solve the recurrence, name the two numbers that remain free, and state the interval on which the sum converges.

A short example shows the machinery and shows why the last step matters. Take

$$
y''+y=0
$$

and assume $y=C_{0}+C_{1}x+C_{2}x^{2}+C_{3}x^{3}+\cdots$. Differentiating twice gives

$$
y''=2C_{2}+6C_{3}x+12C_{4}x^{2}+\cdots
$$

because the constant term disappears on the first differentiation and the linear term disappears on the second. Substituting into the equation and collecting by powers of $x$ gives three statements from the first three powers:

$$
2C_{2}+C_{0}=0, \qquad 6C_{3}+C_{1}=0, \qquad 12C_{4}+C_{2}=0 .
$$

The first says $C_{2}$ is minus one half of $C_{0}$, the second says $C_{3}$ is minus one sixth of $C_{1}$, and the third continues the pattern. Two numbers, $C_{0}$ and $C_{1}$, were never determined, which is exactly right for a second-order equation: two free constants, two solutions to combine. Choosing $C_{0}=1$ and $C_{1}=0$ gives

$$
y=1-\frac{x^{2}}{2}+\frac{x^{4}}{24}-\cdots ,
$$

and choosing $C_{0}=0$ and $C_{1}=1$ gives

$$
y=x-\frac{x^{3}}{6}+\frac{x^{5}}{120}-\cdots .
$$

The first is the cosine and the second is the sine, which is a pleasant check, but the point of the exercise is that we found them without knowing in advance that sines and cosines were involved. The same six steps work when the coefficients of the equation are functions of $x$ rather than constants, and that is the case this note is really about.

### 1.3 Analytic functions: the property that makes the method legal

The method of the previous section assumes a sum, differentiates it term by term, and treats the result as trustworthy. That is only legal if the function really is a sum of that kind, and the technical name for being a sum of that kind is analytic.

> **Definition (analytic at a point).** A function $f$ is analytic at the point $x_{0}$ if there is a positive number $R$ and a list of numbers $a_{0},a_{1},a_{2},\dots$ such that
>
> $$
> f(x)=a_{0}+a_{1}\left(x-x_{0}\right)+a_{2}\left(x-x_{0}\right)^{2}+\cdots
> $$
>
> for every $x$ whose distance from $x_{0}$ is less than $R$.

In plain words: near the point, and on a genuine interval around it, the function equals a power series. The numbers $a_{0},a_{1},\dots$ are not free to be chosen; they are the values of the function and its derivatives at the point, divided by factorials. So a function has at most one such series about a given centre, and being analytic says that this one series really does add up to the function.

The number $R$ is called the radius of convergence. Inside it the sum adds up to a finite number and may be differentiated as often as we like; outside it the sum either fails to add up or adds up to something else. For a function given by a formula, the radius is the distance from the centre to the nearest point where the formula breaks down.

Four examples cover the range.

A polynomial is analytic everywhere, with radius infinity, because a polynomial is already a finite power series.

The function

$$
\frac{1}{1-x}=1+x+x^{2}+x^{3}+\cdots
$$

is analytic at the centre zero with radius one, because the formula breaks down at $x=1$, at distance one.

The function

$$
e^{x}=1+x+\frac{x^{2}}{2}+\frac{x^{3}}{6}+\cdots
$$

is analytic everywhere, with radius infinity, because the exponential never breaks down.

The function

$$
\frac{1}{x}
$$

is not analytic at the centre zero, because it becomes infinite there, and no power series can reproduce an infinite value.

Two warnings save a great deal of trouble later. First, being differentiable once is not enough for analyticity; the function $x\left|x\right|$ has a derivative at zero but no second derivative, so it is not analytic at zero. Second, being finite at a point is not enough either; the function that equals $e^{-1/x^{2}}$ away from zero and zero at zero is perfectly finite, yet its power series about zero is the zero series and does not reproduce the function. What is true, and what matters for classification, is the one-way implication: an analytic function is finite at the point, so a function that becomes infinite at a point is certainly not analytic there.

### 1.4 The normalised form

Every formula in this topic refers to one standard shape of equation, so the first task in any question is to put the equation into that shape.

> **Definition (normalised form).** Take a second-order linear equation written with the second derivative multiplied by some function, say
>
> $$
> a_{0}(x)y''+a_{1}(x)y'+a_{2}(x)y=0 ,
> $$
>
> where $a_{0}$ is not zero on the interval being studied. Dividing every term by $a_{0}(x)$ gives
>
> $$
> y''+P(x)y'+Q(x)y=0 ,
> $$
>
> with $P(x)$ equal to $a_{1}(x)$ divided by $a_{0}(x)$, and $Q(x)$ equal to $a_{2}(x)$ divided by $a_{0}(x)$. This is the normalised form.

The symbols again. The function $a_{0}$ multiplies the second derivative, $a_{1}$ multiplies the first derivative, and $a_{2}$ multiplies the unknown function; all three depend on $x$. The words second-order linear mean that the highest derivative is the second and that the unknown function and its derivatives appear only to the first power, never multiplied together. The functions $P$ and $Q$ are the two quotients, and they are the only objects the classification looks at. The word normalised refers to the fact that the coefficient of $y''$ is now the number one.

A small example fixes the arithmetic. Take

$$
\left(x^{2}-4\right)y''+3xy'+y=0 .
$$

The coefficient of $y''$ is zero at $x=2$ and at $x=-2$, so the division is performed separately on the three intervals cut out by those two numbers. On any one of them,

$$
y''+\frac{3x}{x^{2}-4}y'+\frac{1}{x^{2}-4}y=0 ,
$$

so

$$
P(x)=\frac{3x}{x^{2}-4}, \qquad Q(x)=\frac{1}{x^{2}-4} .
$$

Both quotients are well behaved except at $x=2$ and $x=-2$, and those two numbers are the only places where anything can go wrong.

The order of the steps matters. Divide first, simplify second, and only then look for trouble. If you look at the raw coefficients instead, you will sometimes see a factor that cancels and conclude that there is a problem where there is none.

### 1.5 Ordinary points and singular points

> **Definition (ordinary point).** The point $x_{0}$ is an ordinary point of the normalised equation if both $P$ and $Q$ are analytic at $x_{0}$.

> **Definition (singular point).** The point $x_{0}$ is a singular point of the normalised equation if it is not an ordinary point, that is, if $P$ or $Q$ or both fail to be analytic at $x_{0}$.

The two definitions are exact opposites, so every point is one or the other. The word ordinary suggests nothing special happens there, and that is precisely right: at an ordinary point the six-step method of Section 1.2 always succeeds.

Here are two quick examples. The equation

$$
y''+(x-2)y'+y=0
$$

is already normalised, with $P(x)=x-2$ and $Q(x)=1$. Both are polynomials, so both are analytic everywhere, and the equation has no singular points at all. The equation

$$
\left(x^{2}-4\right)y''+3xy'+y=0
$$

has

$$
P(x)=\frac{3x}{x^{2}-4}, \qquad Q(x)=\frac{1}{x^{2}-4},
$$

and both quotients become infinite at $x=2$ and at $x=-2$. Those two numbers are singular points; every other number is ordinary.

One caution is worth stating early, because it is the most common slip in the whole topic. A number that makes $a_{0}$ vanish is only a candidate. Consider

$$
\left(x^{2}-4\right)y''+(x-2)y'=0 .
$$

The coefficient of $y''$ vanishes at $x=2$, yet after division

$$
P(x)=\frac{x-2}{x^{2}-4}=\frac{1}{x+2}, \qquad Q(x)=0 ,
$$

and the quotient $\frac{1}{x+2}$ is perfectly well behaved at $x=2$, where it equals one quarter. So $x=2$ is an ordinary point, not a singular point. The factor cancelled, and with it the problem.

### 1.6 Regular singular points and irregular singular points

Singular points come in two strengths, and the strength is measured by how fast the coefficients blow up.

> **Definition (regular singular point).** Let $x_{0}$ be a singular point. It is called a regular singular point if both products
>
> $$
> \left(x-x_{0}\right)P(x) \qquad \text{and} \qquad \left(x-x_{0}\right)^{2}Q(x)
> $$
>
> are analytic at $x_{0}$.

> **Definition (irregular singular point).** A singular point is called irregular if it is not regular, that is, if at least one of those two products fails to be analytic at $x_{0}$.

The idea is simple. Multiplying by one bracket cancels one factor of the kind that caused the blow-up in $P$, and multiplying by two brackets cancels two such factors in $Q$. If the blow-up is no worse than one bracket can fix in $P$ and two can fix in $Q$, the point is regular; otherwise it is irregular.

Because analyticity at a point is the same as having a finite limit there, the test is usually performed with limits.

> **Rule (the two tests).** A singular point $x_{0}$ is regular if and only if both of these limits exist and are finite:
>
> $$
> \lim_{x\to x_{0}}\left(x-x_{0}\right)P(x), \qquad \lim_{x\to x_{0}}\left(x-x_{0}\right)^{2}Q(x) .
> $$

Both must be finite. One infinite limit makes the point irregular, and success in the other test never makes up for it.

A tiny example shows both outcomes. For the equation

$$
y''+\frac{1}{x}y'+\frac{1}{x^{2}}y=0
$$

at the point zero, the first product is $\frac{1}{x}$ times $x$, which equals one, and the second is $\frac{1}{x^{2}}$ times $x^{2}$, which also equals one. Both are finite, so zero is a regular singular point. For the equation

$$
y''+\frac{1}{x}y'+\frac{1}{x^{3}}y=0
$$

at the point zero, the first product is again one, but the second is $\frac{1}{x}$, which has no finite limit. One failure is enough, so zero is an irregular singular point.

Why those particular powers, one for $P$ and two for $Q$? Because a solution near a singular point is expected to look like a power $\left(x-x_{0}\right)^{r}$. Differentiating that twice lowers the power by two, so the second-derivative term carries the power $r-2$; for the other terms to match it, $P$ may contribute at worst one inverse power and $Q$ at worst two. If $P$ contributed two inverse powers, its term would sit at a lower power than everything else and could never be cancelled.

### 1.7 The three kinds of point together

The whole classification fits in one table. In it, the letter $t$ stands for the distance $x-x_{0}$ from the point being examined.

| Kind of point | What is required of $P$ and $Q$ | What is guaranteed near the point | A standard equation |
| --- | --- | --- | --- |
| Ordinary | $P$ and $Q$ both analytic | two independent sums of powers of $t$ | $y''+xy=0$ at zero |
| Regular singular | the point is singular, and $tP$ and $t^{2}Q$ are analytic | at least one sum of powers of $t$ multiplied by $t^{r}$ | $2x^{2}y''-xy'+(x-5)y=0$ at zero |
| Irregular singular | the point is singular, and $tP$ or $t^{2}Q$ is not analytic | nothing at all | $x^{2}y''+y'+y=0$ at zero |

The third row deserves care. It does not say that no solution exists. It says that this theory makes no promise, so a series of either of the two forms cannot be assumed. Sometimes such an equation does have a series solution, and sometimes it does not; what is certain is that the answer must be justified by a separate argument.

The table also explains the order of the work. Normalise, then find the singular points, then classify each singular point. Running the two tests at a point that has not been shown to be singular is pointless, because at an ordinary point both products are automatically well behaved and every point would be wrongly labelled regular singular.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Good behaviour is preserved by arithmetic

The classification looks at two quotients, so the first fact needed is that ordinary arithmetic does not create problems where none existed.

> **Theorem (sums, products and quotients).** If two functions are analytic at a point, then their sum, their product and any constant multiple of either are analytic at that point. If the second function is not zero at the point, then the quotient is analytic there as well.

The proof is what one would expect: each analytic function is a convergent power series near the point, and adding, multiplying or dividing two such series produces another convergent power series. Dividing requires the divisor to be nonzero at the centre so that its constant term is nonzero.

The practical consequence is that every polynomial is analytic everywhere, and every ratio of polynomials is analytic everywhere except where its denominator vanishes. All the equations in this course are of that kind, so finding the singular points reduces to finding where denominators vanish, after cancellation.

> **Corollary (radius of a quotient).** If a function is a quotient of two polynomials, its radius of convergence about a point is the distance from that point to the nearest zero of the denominator, after cancellation.

This is why the expansion of $\frac{1}{1-x}$ about zero has radius one: the denominator vanishes at one. It is also why a series solution of an equation cannot be trusted beyond the nearest singular point of the equation.

### 2.2 The regularity test

> **Theorem (test for a regular singular point).** Let $x_{0}$ be a singular point of $y''+P(x)y'+Q(x)y=0$. Then $x_{0}$ is regular if and only if the two products
>
> $$
> \left(x-x_{0}\right)P(x), \qquad \left(x-x_{0}\right)^{2}Q(x)
> $$
>
> are both analytic at $x_{0}$. Equivalently, $x_{0}$ is regular if and only if both limits
>
> $$
> \lim_{x\to x_{0}}\left(x-x_{0}\right)P(x), \qquad \lim_{x\to x_{0}}\left(x-x_{0}\right)^{2}Q(x)
> $$
>
> exist and are finite.

The equivalence of the two versions rests on one principle: if a function is analytic except at a single point, then it becomes analytic at that point exactly when it has a finite limit there. A finite limit means the bad point can be filled in; an infinite limit or no limit means it cannot.

There is one condition hidden in the statement that must never be forgotten. The point $x_{0}$ must already be known to be singular. If it is ordinary, both products are automatically analytic, because a polynomial times an analytic function is analytic. So the tests cannot be used to tell ordinary from regular singular; they can only split the singular points into two groups.

### 2.3 The existence theorem

The theorem below is the centre of the topic. It says what kind of answer each of the three kinds of point promises.

> **Theorem (existence and the nature of the solution).** Consider the normalised equation $y''+P(x)y'+Q(x)y=0$ and a point $x_{0}$.
>
> (i) If $x_{0}$ is an ordinary point, the equation has two independent solutions of the form
>
> $$
> y=\sum_{n=0}^{\infty}C_{n}\left(x-x_{0}\right)^{n},
> $$
>
> and every solution near $x_{0}$ is a combination of these two. The sums converge at least out to the nearest singular point.
>
> (ii) If $x_{0}$ is a regular singular point, the equation has at least one nontrivial solution of the form
>
> $$
> y=\left(x-x_{0}\right)^{r}\sum_{n=0}^{\infty}C_{n}\left(x-x_{0}\right)^{n}, \qquad C_{0}\neq0,
> $$
>
> valid on some deleted interval $0<\left|x-x_{0}\right|<R$ around $x_{0}$. The number $r$ is a root of a quadratic called the indicial equation.
>
> (iii) If $x_{0}$ is an irregular singular point, the equation is not assured of any solution of either form. It may have one, and it may not.

Part (i) is the strongest promise: two solutions, both ordinary power series, and a definite interval of validity. Part (ii) is weaker in three ways: only one solution is promised, the factor $\left(x-x_{0}\right)^{r}$ is allowed to spoil the behaviour at the point itself, and the interval is a deleted interval because the solution may be infinite at $x_{0}$. Part (iii) promises nothing.

When the exponents at a regular singular point differ by a whole number, or coincide, a second solution may contain a logarithm. The equation

$$
x^{2}y''+3xy'+y=0
$$

illustrates this: its two exponents coincide, and its two solutions are $\frac{1}{x}$ and $\frac{\ln x}{x}$. Both are infinite at zero, which is exactly why the ordinary-point theorem could never apply there.

### 2.4 The indicial equation and the exponents

> **Lemma (indicial equation).** Suppose $x_{0}$ is a regular singular point and put $t=x-x_{0}$. Let $p_{0}$ be the finite limit of $tP$ and $q_{0}$ the finite limit of $t^{2}Q$ as $t$ tends to zero. If a solution $y=t^{r}\sum C_{n}t^{n}$ with $C_{0}\neq0$ exists, then
>
> $$
> r(r-1)+p_{0}r+q_{0}=0 .
> $$

The two limits are the numbers the tests produce, so they are already computed when the classification is done. The quadratic has two roots, and those roots are the possible exponents. Three cases follow.

If the roots are real and do not differ by a whole number, two independent solutions of the promised form exist. If the roots coincide, one solution has the bare power form and the other carries a logarithm. If the roots differ by a whole number, one solution always exists in the promised form and the other may need a logarithm. Complex roots are allowed, and they signal oscillation together with growth or decay.

The roots also say how the solution behaves as $x$ approaches $x_{0}$. A negative real part means the solution grows without bound; a positive real part means it shrinks to zero; a zero real part means it stays of moderate size. None of these things can happen at an ordinary point, where every solution is analytic and therefore finite.

### 2.5 The three standard equations

Three equations appear so often that their classifications are worth memorising, with the understanding that each must still be justified by the tests in an examination.

> **Theorem (Legendre's equation).** For
>
> $$
> \left(1-x^{2}\right)y''-2xy'+p(p+1)y=0 ,
> $$
>
> every point except $x=1$ and $x=-1$ is ordinary, and both $x=1$ and $x=-1$ are regular singular points.

> **Theorem (Bessel's equation).** For
>
> $$
> x^{2}y''+xy'+\left(x^{2}-n^{2}\right)y=0 ,
> $$
>
> every nonzero point is ordinary and $x=0$ is a regular singular point, with exponents $r=n$ and $r=-n$.

> **Theorem (hypergeometric equation).** For
>
> $$
> x(1-x)y''+\left[c-(a+b+1)x\right]y'-aby=0 ,
> $$
>
> the points $x=0$ and $x=1$ are regular singular points and every other finite point is ordinary. The exponents at $x=0$ are $0$ and $1-c$.

The pattern is that these classical equations have only finitely many singular points, and all of them are regular. Equations with that property are called Fuchsian, and they are the ones for which the theory of this note is at its most complete.

### 2.6 Radii and the limits of the promise

> **Theorem (radius at an ordinary point).** If $x_{0}$ is an ordinary point, the two power series solutions converge at least for every $x$ closer to $x_{0}$ than the nearest singular point, distances being measured in the plane of complex numbers.

Two consequences are worth remembering. First, a series solution cannot be blamed for failing beyond a singular point; the theory never promised it there. Second, a function may look perfectly well behaved along the real line and still have a finite radius, because the nearest obstruction may be off the real line.

The radius is often computed directly from the coefficients. If the coefficient of $x^{n}$ is written $C_{n}$, then

$$
R=\lim_{n\to\infty}\left|\frac{C_{n}}{C_{n+1}}\right|
$$

whenever this limit exists. For the equation $y''+y=0$ the coefficients behave like the reciprocals of factorials, the ratio tends to infinity, and the radius is infinite, which matches the fact that sine and cosine are defined for every number.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Why the equation is divided by the coefficient of the second derivative

The classification compares $P$ and $Q$ with the powers one and two. That comparison only makes sense when the second derivative stands alone, because the size of the coefficient of $y''$ would otherwise change the balance between the three terms.

Suppose the equation is $a_{0}y''+a_{1}y'+a_{2}y=0$. Divide every term by $a_{0}$, which is allowed wherever $a_{0}$ is not zero:

$$
y''+\frac{a_{1}}{a_{0}}y'+\frac{a_{2}}{a_{0}}y=0 .
$$

Now all information about the size of the terms sits in the two quotients $P$ and $Q$, and the three terms of the equation have comparable status: one second derivative, one first derivative, one function. A blow-up in $a_{0}$ is shared equally by $P$ and $Q$, which is exactly what the two tests are designed to measure.

The same calculation shows why cancellation must be performed before classification. If $a_{1}$ and $a_{0}$ share a factor, the quotient $P$ has that factor removed, and a point where $a_{0}$ vanishes may turn out to be perfectly ordinary.

### 3.2 Where the powers one and two come from

Put $t=x-x_{0}$ and imagine a solution that behaves like $t^{r}$ near the singular point. Its derivatives behave like

$$
\frac{dy}{dt}=rt^{r-1}, \qquad \frac{d^{2}y}{dt^{2}}=r(r-1)t^{r-2} .
$$

Multiply the whole equation by $t^{2}$, which changes nothing except the appearance:

$$
t^{2}\frac{d^{2}y}{dt^{2}}+t^{2}P\frac{dy}{dt}+t^{2}Qy=0 .
$$

For the three terms to be of comparable size, the combination $t^{2}P$ must not blow up, and the combination $t^{2}Q$ must not blow up either. Since $t^{2}P$ is $t$ times $tP$, the condition on $P$ is that $tP$ stay finite, which is the first test. Since $t^{2}Q$ is $t^{2}Q$, the condition on $Q$ is that $t^{2}Q$ stay finite, which is the second test.

Now suppose $P$ blows up like $\frac{1}{t^{2}}$ instead. Then the middle term behaves like $t^{2}\cdot\frac{1}{t^{2}}\cdot rt^{r-1}$, that is like $t^{r-1}$, while the first term behaves like $t^{r}$. The middle term is one power lower than everything else and cannot be cancelled by any choice of $r$. The equation cannot be balanced, and the point is irregular. This is the precise sense in which irregular means too severe.

### 3.3 Deriving the indicial equation

Take a regular singular point, put $t=x-x_{0}$, and write the two coefficients in the form that the tests guarantee:

$$
P=\frac{p_{0}}{t}+\text{(something analytic)}, \qquad Q=\frac{q_{0}}{t^{2}}+\text{(something analytic)} .
$$

Assume the solution has the form

$$
y=t^{r}\left(C_{0}+C_{1}t+C_{2}t^{2}+\cdots\right), \qquad C_{0}\neq0 .
$$

Substituting and multiplying by $t^{2}$ gives three sums. The first is

$$
t^{2}y''=\sum_{n=0}^{\infty}(n+r)(n+r-1)C_{n}t^{n+r},
$$

the second begins

$$
t^{2}Py'=\sum_{n=0}^{\infty}p_{0}(n+r)C_{n}t^{n+r}+\cdots ,
$$

and the third begins

$$
t^{2}Qy=\sum_{n=0}^{\infty}q_{0}C_{n}t^{n+r}+\cdots .
$$

All three contain the power $t^{r}$ when $n=0$, and no lower power appears. Adding the three and setting the coefficient of $t^{r}$ to zero gives

$$
C_{0}\left[r(r-1)+p_{0}r+q_{0}\right]=0 .
$$

Since $C_{0}$ is not zero by assumption, the bracket must vanish. That is the indicial equation, and its two roots are the two exponents.

The simplest case makes the formula obvious. For the equation

$$
t^{2}y''+3ty'+y=0
$$

substituting $y=t^{r}$ gives

$$
\left[r(r-1)+3r+1\right]t^{r}=0 ,
$$

so $r^{2}+2r+1=0$ and $r=-1$ twice. The two solutions are then $\frac{1}{t}$ and $\frac{\ln t}{t}$, the second appearing because the root is repeated.

### 3.4 Method: classifying the points of an equation

The following six steps answer every classification question, and skipping a step is the usual reason for losing marks.

1. Divide the equation by the coefficient of $y''$, and write $P$ and $Q$ separately.
2. Cancel every common factor in $P$ and in $Q$.
3. List the numbers at which $P$ or $Q$ is not analytic; these are the candidates.
4. Check that each candidate really is singular, that is, that at least one of $P$ and $Q$ becomes infinite there.
5. At each singular point, form $\left(x-x_{0}\right)P$ and $\left(x-x_{0}\right)^{2}Q$, simplify them, and take the two limits.
6. Report the classification, and add the form of solution that the existence theorem guarantees.

Step 5 must be written out in full. A conclusion without the simplified products and the two computed limits is not a proof of anything.

### 3.5 Method: deciding the radius

Three short rules cover the questions asked in this course.

The ratio rule: for a series whose coefficients are known, compute the limit of the ratio of consecutive coefficients and take its reciprocal. The distance rule: at an ordinary point the radius is at least the distance to the nearest singular point. The denominator rule: for a quotient of two polynomials, the radius is the distance to the nearest zero of the denominator, after cancellation.

For example, Legendre's equation has singular points at $1$ and $-1$, so a series about the centre zero converges at least while $\left|x\right|<1$. Bessel's equation has its only singular point at zero, so a series about the centre one converges at least while $\left|x-1\right|<1$.

### 3.6 Method: saying what kind of solution exists

The last step of every question is a sentence about the solution, and the sentence must match the classification.

At an ordinary point: two independent solutions of the plain power series kind exist, and their radius is at least the distance to the nearest singular point. At a regular singular point: at least one solution of the form $\left(x-x_{0}\right)^{r}$ times a power series exists, on a deleted interval. At an irregular singular point: no solution of either form is guaranteed.

Writing a stronger sentence than the theorem allows is the mistake that costs the most marks, because it turns a correct classification into an unjustified claim.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: classify the points of a simple equation

Classify the points $x=2$, $x=-2$ and $x=0$ for

$$
\left(x^{2}-4\right)y''+3xy'+y=0 .
$$

### 4.2 Solution: normalise first, then test each candidate

Step 1. Divide every term by $x^{2}-4$.

$$
y''+\frac{3x}{x^{2}-4}y'+\frac{1}{x^{2}-4}y=0
$$

Step 2. Write down the two coefficients and factor the denominator, since $x^{2}-4=(x-2)(x+2)$.

$$
P(x)=\frac{3x}{(x-2)(x+2)}, \qquad Q(x)=\frac{1}{(x-2)(x+2)}
$$

Step 3. Note that both coefficients blow up at $x=2$ and at $x=-2$, and nowhere else. So those two numbers are singular, and every other number, including zero, is ordinary.

Step 4. Test $x=2$. Multiply $P$ by $x-2$, which cancels one factor.

$$
(x-2)P(x)=\frac{3x}{x+2}
$$

At $x=2$ this equals three times two divided by four, that is $\frac{6}{4}=\frac{3}{2}$, a finite number, and the expression is perfectly well behaved near $x=2$. Next multiply $Q$ by $(x-2)^{2}$.

$$
(x-2)^{2}Q(x)=\frac{(x-2)^{2}}{(x-2)(x+2)}=\frac{x-2}{x+2}
$$

At $x=2$ this equals zero, again finite. Both tests pass, so $x=2$ is a regular singular point.

Step 5. Test $x=-2$ in the same way.

$$
(x+2)P(x)=\frac{3x}{x-2}, \qquad (x+2)^{2}Q(x)=\frac{x+2}{x-2}
$$

The first equals $-6$ divided by $-4$, that is $\frac{3}{2}$, and the second equals zero. Both are finite, so $x=-2$ is a regular singular point.

Step 6. Report the answer. The points $x=2$ and $x=-2$ are regular singular; the point $x=0$ is ordinary; every other number is ordinary.

Step 7. State the solution guaranteed at each singular point, say at $x=2$. Since the point is regular singular, at least one solution of the form

$$
y=(x-2)^{r}\sum_{n=0}^{\infty}C_{n}(x-2)^{n}, \qquad C_{0}\neq0,
$$

exists on a deleted interval around $x=2$. The exponent is found from the indicial equation, whose coefficients are the two limits we just computed.

### 4.3 Problem: classify the point zero for Bessel's equation

Classify $x=0$ for

$$
x^{2}y''+xy'+\left(x^{2}-1\right)y=0 ,
$$

and state the two exponents.

### 4.4 Solution: two products, two limits, one quadratic

Step 1. Divide by $x^{2}$.

$$
y''+\frac{1}{x}y'+\frac{x^{2}-1}{x^{2}}y=0
$$

Step 2. Read off the coefficients.

$$
P(x)=\frac{1}{x}, \qquad Q(x)=\frac{x^{2}-1}{x^{2}}=1-\frac{1}{x^{2}}
$$

Step 3. Both blow up at zero, so zero is singular.

Step 4. Apply the first test.

$$
xP(x)=x\cdot\frac{1}{x}=1
$$

The answer is the constant one, which is finite, so the first test passes.

Step 5. Apply the second test.

$$
x^{2}Q(x)=x^{2}\left(1-\frac{1}{x^{2}}\right)=x^{2}-1
$$

At $x=0$ this equals $-1$, a finite number, so the second test passes too. Hence $x=0$ is a regular singular point.

Step 6. Write the indicial equation with $p_{0}=1$ and $q_{0}=-1$.

$$
r(r-1)+r-1=r^{2}-1=0
$$

The roots are $r=1$ and $r=-1$. They differ by two, a whole number, so one solution is always available in the promised form and the second may need a logarithm.

Step 7. Interpret. Near zero the two solutions behave roughly like $x$ and like $\frac{1}{x}$. The first is finite at the origin, the second is not, which is why the interval of validity has to exclude the point itself.

### 4.5 Problem: classify the points of Legendre's equation

For $p=1$, classify the points of

$$
\left(1-x^{2}\right)y''-2xy'+2y=0 .
$$

### 4.6 Solution: an ordinary centre and two regular singular endpoints

Step 1. Divide by $1-x^{2}$ and factor, using $1-x^{2}=-(x-1)(x+1)$.

$$
P(x)=\frac{-2x}{1-x^{2}}=\frac{2x}{(x-1)(x+1)}, \qquad Q(x)=\frac{2}{1-x^{2}}=\frac{-2}{(x-1)(x+1)}
$$

Step 2. The only places where these functions misbehave are $x=1$ and $x=-1$, so those are the singular points and every other number is ordinary.

Step 3. Test $x=1$.

$$
(x-1)P(x)=\frac{2x}{x+1}, \qquad (x-1)^{2}Q(x)=\frac{-2(x-1)}{x+1}
$$

At $x=1$ the first equals one and the second equals zero. Both functions are well behaved near one, so $x=1$ is a regular singular point.

Step 4. Test $x=-1$.

$$
(x+1)P(x)=\frac{2x}{x-1}, \qquad (x+1)^{2}Q(x)=\frac{-2(x+1)}{x-1}
$$

At $x=-1$ the first equals one and the second equals zero, so $x=-1$ is also a regular singular point.

Step 5. Observe that $x=0$ is ordinary, so the theorem promises two plain power series solutions about zero. Their radius is at least the distance from zero to the nearest singular point, which is one.

Step 6. Check the promise on a known solution. The function $y=x$ is a solution, because

$$
\left(1-x^{2}\right)\cdot 0-2x\cdot 1+2x=0 .
$$

A polynomial is a power series with radius infinity, which is certainly at least one, so the example is consistent with the theorem.

### 4.7 Problem: an irregular point

Classify $x=0$ for

$$
y''+\frac{1}{x}y'+\frac{1}{x^{3}}y=0 .
$$

### 4.8 Solution: the first test passes and the second fails

Step 1. The equation is already normalised, with

$$
P(x)=\frac{1}{x}, \qquad Q(x)=\frac{1}{x^{3}} .
$$

Step 2. Both blow up at zero, so zero is singular.

Step 3. Apply the first test.

$$
xP(x)=1
$$

This is finite, so the first test passes.

Step 4. Apply the second test.

$$
x^{2}Q(x)=x^{2}\cdot\frac{1}{x^{3}}=\frac{1}{x}
$$

This has no finite limit at zero, so the second test fails.

Step 5. Conclude. One failure is enough, so $x=0$ is an irregular singular point. No power series solution of either promised form can be assumed, even though the first test looked perfectly healthy.

### 4.9 Problem: a repeated exponent and a logarithm

Classify $x=0$ for $x^{2}y''+3xy'+y=0$ and find both solutions.

### 4.10 Solution: test, solve the quadratic, then verify by substitution

Step 1. Divide by $x^{2}$.

$$
y''+\frac{3}{x}y'+\frac{1}{x^{2}}y=0
$$

Step 2. Form the products.

$$
xP(x)=3, \qquad x^{2}Q(x)=1
$$

Both are constants, so both are finite at zero and the point is regular singular, with $p_{0}=3$ and $q_{0}=1$.

Step 3. Solve the indicial equation.

$$
r(r-1)+3r+1=r^{2}+2r+1=(r+1)^{2}=0
$$

The root is $r=-1$, twice. A repeated root means a logarithm appears in the second solution.

Step 4. Try the first solution $y=\frac{1}{x}$. Its derivatives are $y'=-\frac{1}{x^{2}}$ and $y''=\frac{2}{x^{3}}$, and substituting gives

$$
x^{2}\cdot\frac{2}{x^{3}}+3x\cdot\left(-\frac{1}{x^{2}}\right)+\frac{1}{x}=\frac{2}{x}-\frac{3}{x}+\frac{1}{x}=0 .
$$

Step 5. Try the second solution $y=\frac{\ln x}{x}$. Its derivatives are

$$
y'=\frac{1-\ln x}{x^{2}}, \qquad y''=\frac{2\ln x-3}{x^{3}} .
$$

Step 6. Substitute and collect.

$$
x^{2}\cdot\frac{2\ln x-3}{x^{3}}+3x\cdot\frac{1-\ln x}{x^{2}}+\frac{\ln x}{x}=\frac{2\ln x-3}{x}+\frac{3-3\ln x}{x}+\frac{\ln x}{x}
$$

Adding the three fractions gives

$$
\frac{(2-3+1)\ln x+(-3+3)}{x}=0 ,
$$

so the second solution is confirmed.

Step 7. Report. The point is regular singular with repeated exponent $r=-1$, and the two independent solutions are $\frac{1}{x}$ and $\frac{\ln x}{x}$, both infinite at the origin.

### 4.11 Problem: exponents that differ by a fraction

Show that $x=0$ is a regular singular point of $2x^{2}y''-xy'+(x-5)y=0$ and find the two exponents.

### 4.12 Solution: test the point, then solve the quadratic

Step 1. Divide by $2x^{2}$.

$$
y''-\frac{1}{2x}y'+\frac{x-5}{2x^{2}}y=0
$$

Step 2. Form the products and simplify.

$$
xP(x)=-\frac{1}{2}, \qquad x^{2}Q(x)=\frac{x-5}{2}
$$

Both are finite at zero, so the point is regular singular, with $p_{0}=-\frac{1}{2}$ and $q_{0}=-\frac{5}{2}$.

Step 3. Write the indicial equation.

$$
r(r-1)-\frac{1}{2}r-\frac{5}{2}=0
$$

Step 4. Multiply by two to clear the fractions.

$$
2r^{2}-3r-5=0
$$

Step 5. Solve the quadratic. The discriminant is nine plus forty, that is forty-nine, so

$$
r=\frac{3\pm 7}{4},
$$

which gives $r=\frac{5}{2}$ and $r=-1$.

Step 6. Interpret. The exponents differ by $\frac{7}{2}$, which is not a whole number, so two independent series solutions are guaranteed, one beginning with $x^{5/2}$ and the other with $x^{-1}$.

### 4.13 Problem: one equation with both kinds of singular point

Classify the singular points of

$$
\left(x^{4}-2x^{3}+x^{2}\right)y''+2(x-1)y'+x^{2}y=0 .
$$

### 4.14 Solution: factor, cancel, then test each point separately

Step 1. Factor the coefficient of $y''$.

$$
x^{4}-2x^{3}+x^{2}=x^{2}(x-1)^{2}
$$

Step 2. Divide and cancel.

$$
P(x)=\frac{2(x-1)}{x^{2}(x-1)^{2}}=\frac{2}{x^{2}(x-1)}, \qquad Q(x)=\frac{x^{2}}{x^{2}(x-1)^{2}}=\frac{1}{(x-1)^{2}}
$$

Step 3. The singular points are $x=0$ and $x=1$.

Step 4. Test $x=0$.

$$
xP(x)=\frac{2}{x(x-1)}, \qquad x^{2}Q(x)=\frac{x^{2}}{(x-1)^{2}}
$$

The second is finite at zero, equal to zero. The first is not: its denominator vanishes at zero while its numerator does not, so it grows without limit. Hence $x=0$ is irregular.

Step 5. Test $x=1$.

$$
(x-1)P(x)=\frac{2}{x^{2}}, \qquad (x-1)^{2}Q(x)=1
$$

At $x=1$ these equal two and one, both finite, so $x=1$ is a regular singular point.

Step 6. Report. One equation can have an irregular point and a regular point at the same time; the classification is always a statement about one point, never about the equation as a whole.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 What the classification does and does not settle

The classification answers a question about the form of the answer, not about its value. Knowing that a point is ordinary tells you that two power series exist and roughly how far they reach; it does not tell you what their coefficients are, and it does not tell you how many terms are needed for a given accuracy. Knowing that a point is regular singular tells you that one series with a factor $\left(x-x_{0}\right)^{r}$ exists; it does not tell you the radius, and it does not tell you whether the second solution needs a logarithm.

There is also a boundary to the theory. Every result in this note assumes that the two coefficient functions are analytic on a punctured neighbourhood of the point, which is automatic when the coefficients of the original equation are analytic and the coefficient of $y''$ has an isolated zero. If the coefficient of $y''$ vanished on a whole interval, or if a coefficient had a singularity of a kind that is not isolated, the three labels would not cover all possibilities and the tests would produce limits that do not exist. Such equations lie outside the course, and it is enough to recognise that they do.

A third limit concerns the point at infinity. Questions about behaviour far away are handled by the substitution $x=\frac{1}{t}$, which turns the far distance into the point $t=0$. Applied to Legendre's equation, this substitution produces an equation whose coefficients at $t=0$ pass both tests, so infinity is a regular singular point of Legendre's equation. The three standard equations of Section 2.5 have only regular singular points, even when infinity is counted, and this is what makes them the model examples of the subject.

### 5.2 Beginner misconceptions

- **"A singular point is a point where the equation has no solution."** Not at all. A singular point is a point where the coefficients are not analytic. Solutions usually exist near it; what changes is their form.
- **"A regular singular point is the same as a singular point."** No. Regular and irregular are two kinds of singular point. Every singular point is one or the other, and the tests decide which.
- **"If one test gives a finite limit, the point is regular."** Both tests must give finite limits. The equation of Section 4.7 passes the first and fails the second, and it is irregular.
- **"A number that makes the coefficient of $y''$ vanish is a singular point."** It is only a candidate. If the factor cancels, as in the example of Section 1.5, the point is ordinary.
- **"The tests can be used to find the ordinary points."** The tests are automatic successes at ordinary points, so they cannot distinguish ordinary from regular singular. First find the singular points, then classify them.
- **"At a regular singular point there are always two series solutions."** Only one is guaranteed. The second may contain a logarithm, as in Section 4.9.
- **"An irregular singular point has no solution at all."** The theorem promises nothing, which is different from denying everything. Some irregular points do admit series solutions.
- **"The exponent $r$ must be a whole number."** It may be negative, fractional or even complex. The examples of Sections 4.11 and 4.13 show a fraction and a complex pair.
- **"The series about an ordinary point works for every $x$."** It works out to the nearest singular point. Legendre's series about zero stops being guaranteed at distance one.
- **"The coefficient of $y''$ can be ignored when testing."** The tests are applied to the two quotients after division, and using the raw coefficients gives wrong answers whenever a factor cancels.

### 5.3 A procedure to follow every time

1. Divide by the coefficient of $y''$ and write $P$ and $Q$ separately.
2. Cancel common factors.
3. Find every number at which $P$ or $Q$ misbehaves.
4. Check that each such number really is singular.
5. At each singular point, simplify $\left(x-x_{0}\right)P$ and $\left(x-x_{0}\right)^{2}Q$ and take the two limits.
6. Classify: regular if both limits are finite, irregular otherwise.
7. State the form of solution the theorem guarantees, and give the radius when a series about an ordinary point is asked for.

### 5.4 Summary of the topic

The topic answers one question about one point at a time. If both coefficients of the normalised equation are analytic at the point, the point is ordinary and the equation has two independent power series solutions there, reaching at least as far as the nearest singular point. If either coefficient misbehaves, the point is singular, and the severity of the misbehaviour decides the rest. When one factor cancels the trouble in the first coefficient and two factors cancel it in the second, the point is a regular singular point, and at least one solution exists in the form of a power of the distance multiplied by a power series, with the exponent read from a quadratic. When the trouble is worse than that, the point is irregular, and no such solution is promised.

The three standard equations of the course show every case. Legendre's equation has two regular singular points and an ordinary centre; Bessel's equation has one regular singular point and every other point ordinary; the hypergeometric equation has two regular singular points and is the model of an equation whose singular points are all mild. The work in an examination is always the same: normalise, locate, simplify the two products, take the two limits, and then write one sentence about the solution that is guaranteed.


