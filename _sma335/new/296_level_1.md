## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A box of measuring spoons

Imagine a box of measuring spoons nested one inside another. The largest holds one cup, the next holds half a cup, the next a quarter, the next an eighth, and the nesting continues as far as you like. No single spoon can measure three quarters of a cup, but three quarters of a cup is one half plus one quarter, so two spoons combine to make it. With the whole box you can measure almost any amount you will ever need, and you can get as close as you like to any awkward quantity by using enough of the small spoons.

That is the first idea of this topic. A complicated function is like an awkward quantity: no single simple function measures it. But simple functions of the form one, then the variable, then the variable squared, then the variable cubed, and so on, are like the nested spoons. Each is smaller than the one before whenever the variable is a small number, and by adding them in the right amounts you can reproduce the complicated function as closely as you like. The amounts you add are called coefficients, and the whole sum is called a power series.

Think of a second everyday situation, which explains why the small variable matters. A wide paintbrush lays down a broad stripe; a narrower brush adds a thinner line; a fine brush adds a hairline. Near the edge of a shape only the fine brush matters, because the broad stripe is already in place. In the same way, when the variable is close to zero, the first power is tiny, the second power is tinier, and the third power is tinier still, so each correction refines the answer without disturbing it. This is why the method of this note works near a chosen point and why its accuracy degrades as you move away from that point.

Picture a third situation, which explains the variety of answers. Suppose you are given a recipe for a sauce and told only that it contains flour, butter and milk. If the recipe says the flour is ordinary plain flour, you can follow it. If it says the flour is a strange unfamiliar kind, you must first understand that ingredient before you can proceed. Differential equations are like that. Some points of the equation are ordinary and cooperative, and a plain power series is enough there. Other points are singular, and then the flavour of the flour changes: sometimes a small adjustment makes everything work, and sometimes nothing works at all.

### 1.2 What a differential equation is

An equation such as four times a number plus one equals nine is an equation about a number, and its solution is a number. A differential equation is an equation about a function, and its solution is a function. The equation says how fast the function changes, and the answer must be a function whose rate of change obeys that statement everywhere on an interval.

The simplest example is

$$
\frac{dy}{dx}=2x .
$$

Read it one symbol at a time. The letter $x$ is the input, an ordinary number that we are free to choose. The letter $y$ is the output, a number that depends on $x$, so $y$ is a function of $x$. The symbol $\frac{dy}{dx}$ means the derivative of $y$ with respect to $x$, that is, the rate at which the output changes as the input increases. The right-hand side is twice the input. The equation therefore says: the rate at which the output grows is twice the current input. Its solution is $y=x^{2}+C$, where $C$ is any fixed number, because the derivative of $x^{2}$ is $2x$ and the derivative of a constant is zero.

The word order counts how many derivatives appear. If the highest derivative in the equation is the first derivative, as above, the equation has order one. If the highest derivative is the second derivative, written $\frac{d^{2}y}{dx^{2}}$, the equation has order two. The second derivative measures how the rate of change itself changes, so a second-order equation describes not just the speed of something but the way the speed is being altered.

The word linear means that the unknown function and its derivatives appear only to the first power and are never multiplied together. The equation

$$
\frac{d^{2}y}{dx^{2}}+y=0
$$

is linear, because $y$ appears alone and to the first power. The equation $\frac{d^{2}y}{dx^{2}}+y^{2}=0$ is not linear, because $y$ is squared. This note deals only with linear equations, and that restriction is what makes the series method work so cleanly.

### 1.3 What a power series is

A power series about the point zero is a sum of the form

$$
y=a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+a_{4}x^{4}+\cdots ,
$$

where $a_{0}$ is a fixed number called the constant term, $a_{1}$ is a fixed number called the coefficient of $x$, $a_{2}$ is the coefficient of $x^{2}$, and so on. The numbers $a_{0},a_{1},a_{2},\dots$ do not depend on $x$; they are the amounts of each spoon. The dots at the end mean that the pattern continues without stopping.

A concrete example makes the sizes clear. Take every coefficient equal to one:

$$
1+x+x^{2}+x^{3}+x^{4}+\cdots .
$$

At $x=0.1$ this becomes

$$
1+0.1+0.01+0.001+0.0001+\cdots=1.1111\cdots ,
$$

and the terms shrink so quickly that after five terms the rest contributes less than a ten-thousandth. At $x=1$ the same series becomes $1+1+1+1+\cdots$, whose terms do not shrink at all, and the sum is infinite. At $x=2$ the terms grow and the sum is worse than infinite. So the same list of coefficients can be useful at one value of $x$ and useless at another, and the range of values where it is useful is called its interval of convergence.

The exponential function is the standard example of a series that works everywhere:

$$
e^{x}=1+x+\frac{x^{2}}{2}+\frac{x^{3}}{6}+\frac{x^{4}}{24}+\cdots .
$$

The denominators $2,6,24$ are the numbers $2$, $2$ times $3$, and $2$ times $3$ times $4$; they grow fast enough to beat any fixed power of $x$. This series is the model for almost everything in this note, and a great deal of the work consists of showing that other equations produce the same kind of answer with different coefficients.

> **Definition (power series solution).** A power series solution of a differential equation is a series whose terms are multiples of powers of the variable, which satisfies the equation when it is substituted, on some interval of values of the variable.

### 1.4 Three kinds of points: nice, mildly bad, and bad

Every second-order linear equation can be rearranged so that the second derivative stands alone, with coefficient one. Suppose that after this rearrangement the equation reads

$$
\frac{d^{2}y}{dx^{2}}+p(x)\frac{dy}{dx}+q(x)y=0 .
$$

Here $p(x)$ is whatever function ends up multiplying the first derivative, and $q(x)$ is whatever function ends up multiplying $y$ itself. These two functions decide everything. The classification is made by looking at them near the point of interest, which for simplicity we always take to be the point zero.

A point is called ordinary when both $p$ and $q$ can be written as power series near it, that is, when neither of them becomes infinite there. A point is called singular when at least one of them does become infinite there. Among the singular points there is a further split, and the test uses two products.

The mild kind of singular point is called regular. It is mild when the product of $x$ with $p(x)$, and the product of $x^{2}$ with $q(x)$, both stay finite and can be written as power series near zero. Multiplying by $x$ once, and by $x^{2}$ twice, is exactly enough to cancel the kind of blow-up that a simple division by $x$ creates.

The bad kind is called irregular. It is bad when even those products still blow up, which means the equation's coefficient is more singular than a single factor of $x$ can repair.

Three small examples fix the idea.

The equation

$$
\frac{d^{2}y}{dx^{2}}+xy=0
$$

has $p(x)=0$ and $q(x)=x$. Both are polynomials, so neither blows up anywhere, and every point including zero is ordinary.

The equation

$$
2x^{2}\frac{d^{2}y}{dx^{2}}-x\frac{dy}{dx}+\left(1-x^{2}\right)y=0
$$

becomes, after dividing by $2x^{2}$,

$$
\frac{d^{2}y}{dx^{2}}-\frac{1}{2x}\frac{dy}{dx}+\frac{1-x^{2}}{2x^{2}}y=0 .
$$

Here $p(x)$ is minus one divided by twice $x$, which blows up at zero, so zero is singular. But $x$ times $p(x)$ is the constant $-\frac{1}{2}$, and $x^{2}$ times $q(x)$ is $\frac{1-x^{2}}{2}$, both perfectly finite, so the point is a regular singular point.

The equation

$$
x^{3}\frac{d^{2}y}{dx^{2}}+y=0
$$

becomes $y''$ plus $y$ divided by $x^{3}$, so $q(x)$ is one over $x^{3}$. Multiplying by $x^{2}$ leaves one over $x$, which still blows up, so this point is irregular and the methods of this note do not apply at zero.

### 1.5 The two recipes

There are exactly two shapes of answer, and choosing the right one is the first decision of every problem.

The first recipe is used at an ordinary point:

$$
y=a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+\cdots .
$$

Every power is a whole number power, starting at zero, and the first two coefficients $a_{0}$ and $a_{1}$ are free. Free means that they are not determined by the equation; they stay as arbitrary numbers, and every choice gives a different solution. Since two numbers are free, the answer contains two independent families, which is exactly what a second-order equation requires.

The second recipe is used at a regular singular point, and it carries the name of the mathematician Frobenius:

$$
y=x^{r}\left(a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+\cdots\right).
$$

The new symbol $r$ is a number, possibly a fraction, possibly negative, which is not yet known. Multiplying the whole series by $x^{r}$ allows the first power to be something like $x^{1/2}$, which ordinary polynomials cannot produce. The condition is that $a_{0}$ is not zero, because if $a_{0}$ were zero we could factor out one more power of $x$ and absorb it into $r$, so the recipe would be describing the same thing twice.

The number $r$ is found from a small equation called the indicial equation, which is built from the values of $x$ times $p(x)$ and $x^{2}$ times $q(x)$ at the point. For the example of Section 1.4, the first of those values is $-\frac{1}{2}$ and the second is $\frac{1}{2}$, and the indicial equation turns out to be

$$
r\left(r-1\right)-\frac{r}{2}+\frac{1}{2}=0 ,
$$

whose two solutions are $r=1$ and $r=\frac{1}{2}$. Both are allowed, and each produces one family of solutions.

### 1.6 Three conditions for a first-order equation

For a first-order equation written as $\frac{dy}{dx}$ equals some expression $f(x,y)$ in the input and the output, the classical theorem gives three conditions that guarantee exactly one solution through each point.

The first condition is that the expression is continuous and single valued: at each point of the region it gives one definite number, with no jumps. The second is that the expression is bounded: its size never runs away to infinity inside the region. The third is that the derivative of the expression with respect to the output exists and is continuous.

The three conditions have plain meanings. The first says the slope is defined everywhere. The second says the slope never becomes vertical, so a solution cannot turn straight up and leave the region. The third prevents two solutions from meeting and splitting apart, which is the behaviour that would destroy uniqueness.

When the expression is a polynomial, all three conditions hold automatically on the whole plane, because polynomials are continuous, bounded on any bounded region, and have polynomial derivatives. That is why the first worked example of this note needs no preliminary discussion: the equation there is about as well behaved as an equation can be.

### 1.7 What the method actually does

The method is a fixed sequence of five moves, and it is the same five moves in every problem.

The first move is to decide where to expand, and to classify that point. If the point is ordinary, we use the first recipe; if it is a regular singular point, we use the second.

The second move is to differentiate the chosen series as many times as the equation requires. A second-order equation needs the first derivative and the second derivative.

The third move is to substitute everything into the equation and multiply out, so that the equation becomes a statement about a list of powers of $x$.

The fourth move is to line up the powers. When two sums are added, they must be written with the same power in each term before their coefficients can be compared. This lining up is called shifting the index, and it is the only step where beginners go wrong.

The fifth move is to compare coefficients, obtain a rule that gives each coefficient from earlier ones, and then use that rule repeatedly. The rule is called a recurrence relation.

Once the recurrence is known, the rest is arithmetic. No cleverness is required, no guessing, and no integration. That is the great virtue of the method: it converts a calculus problem into a bookkeeping problem, and bookkeeping can be checked.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The rule for shifting the index

The single most used rule in the topic says that the same series can be written in more than one way, provided the powers and the starting point move together.

> **Lemma (shifting the index).** For any whole number start $N$, and any fixed whole number $k$,
>
> $$
> \sum_{n=N}^{\infty}A_{n}x^{n+k}=\sum_{m=N+k}^{\infty}A_{m-k}x^{m} .
> $$

In words: if you take a term with power $n+k$ and decide instead to call the power $m$, then $m$ equals $n+k$, so $n$ equals $m-k$, and the starting value of $m$ is the starting value of $n$ plus $k$. The letter used for counting is irrelevant; what matters is that the power and the starting value move together.

A small numerical illustration makes this concrete. Consider the series

$$
x^{2}+x^{3}+x^{4}+\cdots ,
$$

which is the sum of $x^{n}$ for $n$ starting at two. Rewrite it as a sum of powers $x^{m}$ starting at zero by taking out a factor $x^{2}$:

$$
x^{2}+x^{3}+x^{4}+\cdots=x^{2}\left(1+x+x^{2}+\cdots\right).
$$

The factor $x^{2}$ has been moved outside, and the counting inside now starts at zero. Nothing has been added or removed; the same terms are present. This is the whole content of the lemma, and the practical rule is: when you take a power out of a sum, the starting value goes down by the same amount; when you put a power in, the starting value goes up.

### 2.2 The rule for comparing coefficients

> **Lemma (comparing coefficients).** If two power series agree for every value of $x$ in some interval around zero, then their coefficients agree one by one.

The reason is that the constant term is the value at zero, so the two constant terms must be equal; subtracting them and dividing by $x$ shows that the coefficients of $x$ must be equal; and so on. This is the rule that turns one differential equation into infinitely many small equations. Without it the method would have no engine.

### 2.3 The rule for differentiating a series

> **Lemma (differentiating a series).** A power series may be differentiated term by term inside its interval of convergence, and the derivative is again a power series with the same interval.

Differentiating $a_{n}x^{n}$ gives $n a_{n}x^{n-1}$: the power drops by one and the coefficient is multiplied by the old power. Differentiating twice gives $n\left(n-1\right)a_{n}x^{n-2}$. This is why the second derivative of a series begins with a constant term only if the series contains an $x^{2}$ term, and why the first two coefficients of the series are untouched by differentiation in a way that leaves them free.

### 2.4 The ordinary point theorem

> **Theorem (two solutions at an ordinary point).** If zero is an ordinary point of the equation, then the equation has two solutions of the form of a plain power series, and every solution on the interval is a combination of them with two arbitrary constants.

The theorem is the guarantee that the first recipe always works at an ordinary point. It also tells us how many free constants to expect: exactly two, one multiplying each of the two solutions.

A companion fact concerns the interval. If the nearest singular point of the equation is at distance $R$ from zero, then the two series are guaranteed to converge at least for all $x$ with size less than $R$. For the equation of Section 1.4 whose singular points are at $1$ and $-1$, that distance is one, so the series is guaranteed only on the interval from $-1$ to $1$, even though the solution may exist further out.

### 2.5 The Frobenius theorem

> **Theorem (one solution at a regular singular point).** If zero is a regular singular point, then the equation has at least one solution of the Frobenius form with $a_{0}$ not zero, where the power $r$ is one of the two roots of the indicial equation.

The theorem promises one solution, not two, and the word at least is the honest part. The second solution may need a logarithm, and the next result describes when.

### 2.6 The indicial equation

> **Lemma (indicial equation).** Suppose that $x$ times $p(x)$ equals $p_{0}$ plus higher powers at zero, and that $x^{2}$ times $q(x)$ equals $q_{0}$ plus higher powers at zero. Then the allowed powers $r$ satisfy
>
> $$
> r\left(r-1\right)+p_{0}r+q_{0}=0 .
> $$

The two numbers $p_{0}$ and $q_{0}$ are constants, found by putting $x=0$ in the two products. The equation is quadratic in $r$, so there are two roots, counted with repetition. The roots decide which powers of $x$ can appear at the front of the solution, and they also decide whether a logarithm appears.

### 2.7 The three cases for the two roots

> **Theorem (the shape of the second solution).** Let the two roots be $r_{1}$ and $r_{2}$, with $r_{1}$ the larger.
>
> In the first case, the difference of the roots is not a whole number. Then both solutions have the Frobenius form, one beginning with $x^{r_{1}}$ and the other with $x^{r_{2}}$, and no logarithm appears.
>
> In the second case, the two roots are equal. Then one solution has the Frobenius form, and the second is that solution multiplied by the logarithm of $x$, plus a Frobenius series.
>
> In the third case, the difference of the roots is a whole number. Then one solution has the Frobenius form, and the second has the form of the smaller-root series plus a multiple of the first solution times the logarithm of $x$, where the multiple may turn out to be zero.

The three cases are not three separate techniques. They are three answers to a single question: when the recipe asks us to divide by a certain quantity, does that quantity ever become zero as we work upwards? If it never does, both series are plain. If it becomes zero at the very first step, the roots are equal and a logarithm is forced. If it becomes zero later on, at a step decided by the difference of the roots, a logarithm may or may not appear.

### 2.8 The non-homogeneous case

A non-homogeneous equation is one whose right-hand side is not zero, such as

$$
\frac{d^{2}y}{dx^{2}}-y=x .
$$

> **Theorem (adding a particular solution).** If $y_{p}$ satisfies the non-homogeneous equation, and $y_{h}$ satisfies the corresponding equation with zero on the right, then $y_{p}+y_{h}$ satisfies the non-homogeneous equation. Every solution of the non-homogeneous equation is of this form.

In practice this means that the work splits into two parts. The homogeneous part supplies the two free constants and is solved by the ordinary-point method. The right-hand side supplies one extra solution, which can be found either by continuing the same series calculation with the right-hand side included, or by a formula called variation of parameters.

### 2.9 A practical corollary

> **Corollary (recognition).** If a computed series is recognised as the series of a familiar function, then that function is the solution.

This corollary is the best check available. A first-order calculation that produces one plus $x$ plus $x^{2}$ over two plus $x^{3}$ over six must be producing the exponential function. A second-order calculation on the equation with $y''$ equal to $y$ that produces one plus $x^{2}$ over two plus $x^{4}$ over twenty-four must be producing the hyperbolic cosine. If the terms do not match a function known to solve the equation, the recurrence is wrong.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Why shifting the index is safe

Take the series written out with a few terms,

$$
A_{0}+A_{1}x+A_{2}x^{2}+A_{3}x^{3}+\cdots ,
$$

and multiply it by $x^{2}$. Every term moves up by two powers:

$$
A_{0}x^{2}+A_{1}x^{3}+A_{2}x^{4}+A_{3}x^{5}+\cdots .
$$

The first term now has power two, whereas before it had power zero. If we want to describe this new sum as a sum of powers $x^{m}$ starting at $m$ equal to zero, then the coefficient of $x^{0}$ is now zero, the coefficient of $x^{1}$ is zero, the coefficient of $x^{2}$ is $A_{0}$, the coefficient of $x^{3}$ is $A_{1}$, and in general the coefficient of $x^{m}$ is $A_{m-2}$. So

$$
x^{2}\sum_{n=0}^{\infty}A_{n}x^{n}=\sum_{m=0}^{\infty}B_{m}x^{m}\qquad\text{with }B_{0}=B_{1}=0,\ B_{m}=A_{m-2}\ \text{for }m\ge 2 .
$$

Writing the same thing with the sum starting at $m$ equal to two gives

$$
x^{2}\sum_{n=0}^{\infty}A_{n}x^{n}=\sum_{m=2}^{\infty}A_{m-2}x^{m},
$$

and the two descriptions agree because the extra terms in the first description are the two zeros. This is the lemma, and the proof is nothing but the observation that multiplying by $x^{2}$ moves every term up two places.

The rule to remember in practice is: the exponent and the starting value are tied together. If a term such as $xy$ is written as a sum over $n$ with power $n+1$, then when the power is renamed $m$ the sum must start at $m$ equal to one, not zero. Forgetting the change of starting value deletes the term $a_{0}x$, which is a genuine term of the answer.

### 3.2 Why comparing coefficients is safe

Suppose a series equals zero for every $x$ in some interval around zero:

$$
a_{0}+a_{1}x+a_{2}x^{2}+\cdots=0\qquad\text{for all small }x .
$$

Put $x=0$. Every term containing $x$ disappears, leaving $a_{0}=0$. Now the series reads $a_{1}x+a_{2}x^{2}+\cdots=0$, and for $x$ not zero we may divide by $x$, giving $a_{1}+a_{2}x+\cdots=0$ for all small $x$ except possibly zero. Putting $x=0$ in this new statement, and using the fact that a power series is continuous, gives $a_{1}=0$. Repeating the argument gives $a_{2}=0$, then $a_{3}=0$, and so on.

Two series that agree everywhere therefore have equal coefficients, because their difference is a series that vanishes everywhere. This is the licence for the fourth move of the method.

### 3.3 Deriving the recurrence for the equation $y'=y$

Step 1. Write the unknown as a series with unknown coefficients.

$$
y=a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+a_{4}x^{4}+\cdots
$$

Step 2. Differentiate term by term. The derivative of $a_{0}$ is zero, the derivative of $a_{1}x$ is $a_{1}$, the derivative of $a_{2}x^{2}$ is $2a_{2}x$, the derivative of $a_{3}x^{3}$ is $3a_{3}x^{2}$, and the derivative of $a_{4}x^{4}$ is $4a_{4}x^{3}$.

$$
\frac{dy}{dx}=a_{1}+2a_{2}x+3a_{3}x^{2}+4a_{4}x^{3}+\cdots
$$

Step 3. The equation says the two displayed expressions are the same function. Writing them one above the other, with the powers lined up:

$$
a_{1}+2a_{2}x+3a_{3}x^{2}+\cdots=a_{0}+a_{1}x+a_{2}x^{2}+\cdots
$$

Step 4. Compare the constant terms, then the coefficients of $x$, then the coefficients of $x^{2}$, and so on.

$$
a_{1}=a_{0},\qquad 2a_{2}=a_{1},\qquad 3a_{3}=a_{2},\qquad 4a_{4}=a_{3}
$$

Step 5. Notice that each line has the same shape: the coefficient of $x^{n}$ on the left is $n+1$ times the next coefficient, and on the right is $a_{n}$. So in general

$$
(n+1)a_{n+1}=a_{n}\qquad\text{which is}\qquad a_{n+1}=\frac{a_{n}}{n+1}.
$$

This is the recurrence relation. It says that each coefficient is the previous one divided by the next whole number.

Step 6. Run the recurrence from the bottom. The number $a_{0}$ is not determined by anything, so it stays free. Then

$$
a_{1}=\frac{a_{0}}{1}=a_{0},\qquad a_{2}=\frac{a_{0}}{2},\qquad a_{3}=\frac{a_{0}}{6},\qquad a_{4}=\frac{a_{0}}{24},\qquad a_{5}=\frac{a_{0}}{120}.
$$

Step 7. Write the answer and read it.

$$
y=a_{0}\left(1+x+\frac{x^{2}}{2}+\frac{x^{3}}{6}+\frac{x^{4}}{24}+\frac{x^{5}}{120}+\cdots\right)=a_{0}e^{x}
$$

The bracket is the exponential series, so the series method has recovered the answer that separation of variables gives, and the free coefficient $a_{0}$ is the value of the solution at zero.

### 3.4 Deriving the recurrence for the equation $y''=y$

Step 1. Write the series and differentiate twice. The first derivative was written in the previous subsection; differentiating again multiplies each coefficient by the power and lowers the power once more.

$$
\frac{d^{2}y}{dx^{2}}=2a_{2}+6a_{3}x+12a_{4}x^{2}+20a_{5}x^{3}+\cdots
$$

The numbers $2,6,12,20$ are the products one times two, two times three, three times four and four times five, so the general term is $n+2$ times $n+1$ times $a_{n+2}$.

Step 2. Line up the two sides of the equation.

$$
2a_{2}+6a_{3}x+12a_{4}x^{2}+\cdots=a_{0}+a_{1}x+a_{2}x^{2}+\cdots
$$

Step 3. Compare coefficients.

$$
2a_{2}=a_{0},\qquad 6a_{3}=a_{1},\qquad 12a_{4}=a_{2},\qquad 20a_{5}=a_{3}
$$

Step 4. Write the general rule, which is the same statement with $n$ in place of the particular numbers.

$$
(n+2)(n+1)a_{n+2}=a_{n}
$$

Step 5. Run it from the bottom, keeping $a_{0}$ and $a_{1}$ free.

$$
a_{2}=\frac{a_{0}}{2},\qquad a_{3}=\frac{a_{1}}{6},\qquad a_{4}=\frac{a_{2}}{12}=\frac{a_{0}}{24},\qquad a_{5}=\frac{a_{3}}{20}=\frac{a_{1}}{120}
$$

Step 6. Separate the two families. The even coefficients all come from $a_{0}$ and the odd ones all come from $a_{1}$, so

$$
y=a_{0}\left(1+\frac{x^{2}}{2}+\frac{x^{4}}{24}+\cdots\right)+a_{1}\left(x+\frac{x^{3}}{6}+\frac{x^{5}}{120}+\cdots\right).
$$

Step 7. Recognise the two brackets. The first is the hyperbolic cosine and the second is the hyperbolic sine, so the answer is a combination of them, with the two free constants that a second-order equation requires.

Step 8. Observe the role of the divisor. In both this example and the previous one, the divisor of the recurrence is a product of positive whole numbers and can never vanish, which is exactly why both coefficients $a_{0}$ and $a_{1}$ survive to the end. This is the ordinary-point behaviour, and it is the behaviour we lose at a singular point.

### 3.5 Deriving the indicial equation for a regular singular point

Step 1. Take the example

$$
2x^{2}\frac{d^{2}y}{dx^{2}}-x\frac{dy}{dx}+\left(1-x^{2}\right)y=0 .
$$

Dividing by $2x^{2}$ shows that the coefficient of the first derivative is minus one over twice $x$, and the coefficient of $y$ is $\frac{1-x^{2}}{2x^{2}}$. At zero both blow up, so zero is a singular point. But $x$ times the first is the constant $-\frac{1}{2}$, and $x^{2}$ times the second is $\frac{1-x^{2}}{2}$, which is finite, so the point is regular.

Step 2. Use the Frobenius recipe with the unknown power $r$.

$$
y=x^{r}\left(a_{0}+a_{1}x+a_{2}x^{2}+\cdots\right)=a_{0}x^{r}+a_{1}x^{r+1}+a_{2}x^{r+2}+\cdots
$$

Step 3. Differentiate once and twice. Each term loses a power, but the factor $x^{r}$ stays.

$$
\frac{dy}{dx}=a_{0}r x^{r-1}+a_{1}(r+1)x^{r}+a_{2}(r+2)x^{r+1}+\cdots
$$

$$
\frac{d^{2}y}{dx^{2}}=a_{0}r(r-1)x^{r-2}+a_{1}(r+1)r x^{r-1}+a_{2}(r+2)(r+1)x^{r}+\cdots
$$

Step 4. Multiply by the coefficients in the equation. Multiplying the second derivative by $2x^{2}$ raises every power by two; multiplying the first derivative by $-x$ raises every power by one; the term with $y$ itself stays as it is; and multiplying by $-x^{2}$ raises every power by two.

$$
2x^{2}y''=2a_{0}r(r-1)x^{r}+2a_{1}(r+1)r x^{r+1}+2a_{2}(r+2)(r+1)x^{r+2}+\cdots
$$

$$
-xy'=-a_{0}r x^{r}-a_{1}(r+1)x^{r+1}-a_{2}(r+2)x^{r+2}-\cdots
$$

$$
y=a_{0}x^{r}+a_{1}x^{r+1}+a_{2}x^{r+2}+\cdots
$$

$$
-x^{2}y=-a_{0}x^{r+2}-a_{1}x^{r+3}-\cdots
$$

Step 5. Add the first three lines, collecting the coefficient of each power separately. For the power $x^{r}$ the coefficient is

$$
a_{0}\left[2r(r-1)-r+1\right],
$$

and for the power $x^{r+1}$ it is

$$
a_{1}\left[2(r+1)r-(r+1)+1\right].
$$

Step 6. Simplify each bracket. For the first,

$$
2r(r-1)-r+1=2r^{2}-3r+1=\left(2r-1\right)\left(r-1\right).
$$

For the second, putting $r+1$ in place of $r$ in the same expression gives $\left(2r+1\right)r$. In general, at the power $x^{r+n}$ the bracket is $\left(2(r+n)-1\right)\left(r+n-1\right)$.

Step 7. The equation now reads: a multiple of $x^{r}$ plus a multiple of $x^{r+1}$ plus and so on equals the term $a_{0}x^{r+2}$ plus further terms. The lowest power on the left is $x^{r}$ and the lowest power on the right is $x^{r+2}$, so the coefficient of $x^{r}$ must vanish by itself, since nothing on the right can cancel it.

$$
\left(2r-1\right)\left(r-1\right)a_{0}=0
$$

Step 8. Use the fact that $a_{0}$ is not zero, by the definition of the recipe, so the bracket itself must vanish. This is the indicial equation.

$$
\left(2r-1\right)\left(r-1\right)=0\qquad\text{so}\qquad r=\frac{1}{2}\ \text{or}\ r=1 .
$$

Step 9. Read the coefficient of $x^{r+1}$, which gives the first coefficient after $a_{0}$.

$$
\left(2r+1\right)r a_{1}=0\qquad\text{so}\qquad a_{1}=0,
$$

because neither $2r+1$ nor $r$ is zero at either root.

Step 10. Read the coefficient of $x^{r+n}$ for $n$ at least two, which is where the right-hand side begins to contribute.

$$
\left(2(n+r)-1\right)\left(n+r-1\right)a_{n}=a_{n-2}\qquad\text{so}\qquad a_{n}=\frac{a_{n-2}}{\left(2(n+r)-1\right)\left(n+r-1\right)} .
$$

Step 11. Put $r=1$ and compute. The denominator at $n=2$ is five times two, at $n=4$ it is nine times four, and each step uses only the coefficient two places before.

$$
a_{2}=\frac{a_{0}}{10},\qquad a_{4}=\frac{a_{2}}{36}=\frac{a_{0}}{360}
$$

Step 12. Put $r=\frac{1}{2}$ and compute in the same way. The denominator at $n=2$ is four times one and a half, which is six, and at $n=4$ it is eight times three and a half, which is twenty-eight.

$$
a_{2}=\frac{a_{0}}{6},\qquad a_{4}=\frac{a_{2}}{28}=\frac{a_{0}}{168}
$$

Step 13. Write the two solutions.

$$
y_{1}=x\left(1+\frac{x^{2}}{10}+\frac{x^{4}}{360}+\cdots\right),\qquad y_{2}=x^{1/2}\left(1+\frac{x^{2}}{6}+\frac{x^{4}}{168}+\cdots\right)
$$

Step 14. Note why both were available. The two roots differ by one half, which is not a whole number, so the divisor in the recurrence never becomes zero at either root, and both recipes produce a full family. This is the first of the three cases.

### 3.6 What happens when the two roots are equal

Step 1. Take the simple example

$$
4x^{2}\frac{d^{2}y}{dx^{2}}+y=0 .
$$

Dividing by $4x^{2}$ gives the coefficient of $y$ as one over four $x^{2}$, so $x$ times the first-derivative coefficient is zero and $x^{2}$ times the second is one quarter. The indicial equation is therefore

$$
r(r-1)+\frac{1}{4}=0 ,
$$

which is $r^{2}-r+\frac{1}{4}=0$, that is $\left(r-\frac{1}{2}\right)^{2}=0$. There is one root, repeated: $r=\frac{1}{2}$.

Step 2. Try the recipe with $r=\frac{1}{2}$. The coefficient of $x^{r+n}$ turns out to be $4n^{2}$ times $a_{n}$, because four times $\left(n+\frac{1}{2}\right)\left(n-\frac{1}{2}\right)$ is $4n^{2}-1$ and the term with $y$ itself adds the missing one. The equation therefore forces $4n^{2}a_{n}=0$ for every $n$ at least one, so every coefficient after $a_{0}$ is zero.

$$
y_{1}=a_{0}x^{1/2}
$$

Step 3. Check the answer.

$$
y=x^{1/2}\quad\Longrightarrow\quad \frac{dy}{dx}=\frac{1}{2}x^{-1/2}\quad\Longrightarrow\quad \frac{d^{2}y}{dx^{2}}=-\frac{1}{4}x^{-3/2}
$$

$$
4x^{2}\frac{d^{2}y}{dx^{2}}+y=4x^{2}\left(-\frac{1}{4}x^{-3/2}\right)+x^{1/2}=-x^{1/2}+x^{1/2}=0
$$

So the first family is confirmed, but it contains only one free constant, and a second-order equation needs two.

Step 4. The missing family cannot be found by the plain recipe, because both roots give the same starting power. The second family in this situation necessarily contains the logarithm of $x$. Try the function $x^{1/2}$ times the logarithm.

$$
y=x^{1/2}\ln x
$$

Step 5. Differentiate it twice.

$$
\frac{dy}{dx}=\frac{1}{2}x^{-1/2}\ln x+x^{-1/2},\qquad \frac{d^{2}y}{dx^{2}}=-\frac{1}{4}x^{-3/2}\ln x+\frac{1}{2}x^{-3/2}-\frac{1}{2}x^{-3/2}=-\frac{1}{4}x^{-3/2}\ln x
$$

Step 6. Substitute.

$$
4x^{2}\left(-\frac{1}{4}x^{-3/2}\ln x\right)+x^{1/2}\ln x=-x^{1/2}\ln x+x^{1/2}\ln x=0
$$

Step 7. State the general solution and the moral.

$$
y=x^{1/2}\left(A+B\ln x\right)
$$

When the indicial equation has a repeated root, the second solution always carries a logarithm, and the two families are $x^{r}$ times a series and that same thing multiplied by the logarithm plus another series. This is the second of the three cases.

### 3.7 What happens when the difference of the roots is a whole number

Step 1. Take the example

$$
x^{2}\frac{d^{2}y}{dx^{2}}-2x\frac{dy}{dx}+\left(2-x\right)y=0 .
$$

Dividing by $x^{2}$ gives the first-derivative coefficient as minus two over $x$ and the second as $\frac{2-x}{x^{2}}$. So $x$ times the first is minus two and $x^{2}$ times the second is $2-x$, both finite, and the point is regular.

Step 2. Write the indicial equation.

$$
r(r-1)-2r+2=r^{2}-3r+2=\left(r-1\right)\left(r-2\right)=0\qquad\text{so}\qquad r=2\ \text{or}\ r=1 .
$$

The roots differ by one, a whole number.

Step 3. Use the larger root $r=2$. The recurrence is available at every step, and the coefficients are

$$
a_{n}=\frac{a_{n-1}}{n(n+1)},\qquad a_{1}=\frac{a_{0}}{2},\qquad a_{2}=\frac{a_{0}}{12},\qquad a_{3}=\frac{a_{0}}{144}.
$$

Step 4. Write the first solution.

$$
y_{1}=a_{0}x^{2}\left(1+\frac{x}{2}+\frac{x^{2}}{12}+\frac{x^{3}}{144}+\cdots\right)
$$

Step 5. Try the smaller root $r=1$. The coefficient of $a_{n}$ in the recurrence is $n(n-1)$, and at $n=1$ this is zero, so the recurrence reads

$$
0\cdot a_{1}=a_{0},
$$

which is impossible because $a_{0}$ is not zero. The smaller root therefore produces no second family: the recipe fails at the very step where the difference of the roots shows itself.

Step 6. Conclude. Here the difference of the roots is a whole number and the logarithm is genuinely needed, because the coefficient that the reduction formula produces is not zero. But the appearance of a logarithm is not automatic: in the equation $x^{2}y''+xy'-4y=0$ the roots are $2$ and $-2$, which differ by a whole number, and yet the two solutions are the plain powers $x^{2}$ and $x^{-2}$ with no logarithm at all. The difference is whether the coefficient in front of the logarithm happens to vanish, which can only be settled by computing it. This is the third of the three cases.

### 3.8 The steps of the ordinary-point method

The following list is the order in which the work should be written.

1. Divide the equation by the coefficient of the second derivative, and write down the two coefficient functions.
2. Decide whether the chosen point is ordinary; if it is, note the nearest singular point and hence the guaranteed interval.
3. Write the plain series, and say that the first two coefficients are free.
4. Differentiate once and twice.
5. Substitute all three series into the equation and multiply out every term.
6. Shift each term so that all powers agree, taking care that the starting value moves with the power.
7. Treat the constant term and the coefficient of $x$ as separate equations, because they receive fewer contributions than the general case.
8. Write the general recurrence and run it.
9. Collect the terms multiplying the first free coefficient and the terms multiplying the second, and write two explicit series.
10. Check by substituting the first few terms back into the equation, or by recognising a familiar function.

### 3.9 The steps of the Frobenius method

1. Divide the equation by the coefficient of the second derivative, and identify the singular point.
2. Compute $x$ times the first coefficient and $x^{2}$ times the second, and check that both are finite at the point. If they are not, the point is irregular and the method stops.
3. Read off the two constants: the value of the first product at zero is $p_{0}$, and of the second is $q_{0}$.
4. Write and solve the indicial equation $r(r-1)+p_{0}r+q_{0}=0$, naming the larger root first.
5. Write the Frobenius recipe with the unknown power $r$, and differentiate it once and twice keeping the factor $x^{r}$ visible.
6. Substitute, multiply out, and collect the coefficient of $x^{r+n}$ for each $n$.
7. Read the coefficient of $x^{r}$ as the indicial equation, which should reproduce the roots already found.
8. Read the coefficient of $x^{r+1}$, which usually forces the first coefficient after $a_{0}$ to vanish.
9. Read the coefficient of $x^{r+n}$ for $n$ at least two, which gives the recurrence; note carefully the divisor, because its zeros are what create the three cases.
10. Work through the larger root completely, then the smaller root, and finish by writing the general solution with the factor $x^{r}$ included.

### 3.10 The non-homogeneous equation in slow motion

Step 1. Consider

$$
\frac{d^{2}y}{dx^{2}}-y=x .
$$

The left-hand side is a second-order expression, and the right-hand side is the simple polynomial $x$. Zero is an ordinary point, since the coefficient functions are zero and minus one, so the plain recipe applies.

Step 2. Substitute the series and its second derivative.

$$
\left(2a_{2}+6a_{3}x+12a_{4}x^{2}+20a_{5}x^{3}+\cdots\right)-\left(a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+\cdots\right)=x
$$

Step 3. Line up the powers and compare, remembering that the right-hand side has coefficient one for $x$ and coefficient zero for every other power.

$$
2a_{2}-a_{0}=0,\qquad 6a_{3}-a_{1}=1,\qquad 12a_{4}-a_{2}=0,\qquad 20a_{5}-a_{3}=0
$$

Step 4. Notice that only the second line is affected by the right-hand side, because the right-hand side has no constant term and no $x^{2}$ term and no higher term.

$$
a_{2}=\frac{a_{0}}{2},\qquad a_{3}=\frac{a_{1}+1}{6},\qquad a_{4}=\frac{a_{2}}{12},\qquad a_{5}=\frac{a_{3}}{20}
$$

Step 5. Continue the pattern, which is the same as the homogeneous recurrence for every power from $x^{2}$ upwards.

$$
a_{4}=\frac{a_{0}}{24},\qquad a_{5}=\frac{a_{1}+1}{120},\qquad a_{6}=\frac{a_{0}}{720},\qquad a_{7}=\frac{a_{1}+1}{5040}
$$

Step 6. Assemble and interpret.

$$
y=a_{0}\left(1+\frac{x^{2}}{2}+\frac{x^{4}}{24}+\frac{x^{6}}{720}+\cdots\right)+a_{1}\left(x+\frac{x^{3}}{6}+\frac{x^{5}}{120}+\frac{x^{7}}{5040}+\cdots\right)+\left(\frac{x^{3}}{6}+\frac{x^{5}}{120}+\frac{x^{7}}{5040}+\cdots\right)
$$

The first two brackets are the homogeneous solutions, cosine-like and sine-like in hyperbolic form, and the third bracket is the extra piece contributed by the right-hand side. Adding the third bracket to the second is legitimate, since both are odd series, and doing so produces the tidy answer $A\cosh x+B\sinh x-x$. That tidy answer can be checked in two lines. Differentiating once gives $A\sinh x+B\cosh x-1$, and differentiating again gives $A\cosh x+B\sinh x$. Subtracting the function itself therefore leaves

$$
\left(A\cosh x+B\sinh x\right)-\left(A\cosh x+B\sinh x-x\right)=x ,
$$

which is the equation, so the tidy answer is confirmed.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a first-order equation with a starting value

Solve the equation $\frac{dy}{dx}=y$ subject to the condition that $y$ equals $2$ when $x$ equals $0$, giving at least four terms of the series.

### 4.2 Solution: run the recurrence, then use the starting value

Step 1. Check that the recipe is allowed. The right-hand side is the output itself, which is a polynomial, so it is continuous, bounded on any bounded region, and has a continuous derivative with respect to the output. The three conditions therefore hold, and a power series solution exists.

Step 2. Write the series with unknown coefficients, and say that the value at zero is the constant term.

$$
y=a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+a_{4}x^{4}+\cdots
$$

$$
y(0)=a_{0}\qquad\text{so}\qquad a_{0}=2
$$

Step 3. Differentiate and line up the two sides, exactly as in Section 3.3.

$$
a_{1}+2a_{2}x+3a_{3}x^{2}+4a_{4}x^{3}+\cdots=a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+\cdots
$$

Step 4. Compare coefficients to obtain the recurrence.

$$
(n+1)a_{n+1}=a_{n}\qquad\text{so}\qquad a_{n+1}=\frac{a_{n}}{n+1}
$$

Step 5. Compute, starting from $a_{0}=2$.

$$
a_{1}=\frac{2}{1}=2,\qquad a_{2}=\frac{2}{2}=1,\qquad a_{3}=\frac{1}{3},\qquad a_{4}=\frac{1}{12}
$$

Step 6. Write the answer.

$$
y=2+2x+x^{2}+\frac{x^{3}}{3}+\frac{x^{4}}{12}+\cdots
$$

Step 7. Check by differentiating and comparing term by term.

$$
\frac{dy}{dx}=2+2x+x^{2}+\frac{x^{3}}{3}+\cdots
$$

The derivative is exactly the series for $y$, term for term, so the equation is satisfied. The value at zero is $2$, so the starting condition is satisfied as well.

Step 8. Recognise the answer. The series is twice the exponential series, so $y=2e^{x}$, and indeed its derivative is itself with value $2$ at zero.

### 4.3 Problem: a first-order equation with a repeated factor

Solve $\frac{dy}{dx}=2xy$ subject to $y(0)=1$, giving at least five non-zero terms.

### 4.4 Solution: the odd coefficients are forced to vanish

Step 1. Write the series and its derivative.

$$
y=a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+a_{4}x^{4}+\cdots,\qquad \frac{dy}{dx}=a_{1}+2a_{2}x+3a_{3}x^{2}+4a_{4}x^{3}+\cdots
$$

Step 2. Multiply the series for $y$ by $2x$, which raises every power by one and doubles every coefficient.

$$
2xy=2a_{0}x+2a_{1}x^{2}+2a_{2}x^{3}+2a_{3}x^{4}+\cdots
$$

Step 3. Line up the two sides, noting that the right-hand side has no constant term at all.

$$
a_{1}+2a_{2}x+3a_{3}x^{2}+4a_{4}x^{3}+5a_{5}x^{4}+\cdots=2a_{0}x+2a_{1}x^{2}+2a_{2}x^{3}+2a_{3}x^{4}+\cdots
$$

Step 4. Compare the constant terms. The right side has nothing there, so the left side must vanish.

$$
a_{1}=0
$$

Step 5. Compare the coefficients of $x^{n}$ for $n$ at least one, which links each coefficient to the one two places before it.

$$
(n+1)a_{n+1}=2a_{n-1}\qquad\text{so}\qquad a_{n+1}=\frac{2a_{n-1}}{n+1}
$$

Step 6. Use the starting value $a_{0}=1$, and run the recurrence.

$$
a_{2}=\frac{2a_{0}}{2}=1,\qquad a_{3}=\frac{2a_{1}}{3}=0,\qquad a_{4}=\frac{2a_{2}}{4}=\frac{1}{2},\qquad a_{5}=0,\qquad a_{6}=\frac{2a_{4}}{6}=\frac{1}{6}
$$

Step 7. Write the answer.

$$
y=1+x^{2}+\frac{x^{4}}{2}+\frac{x^{6}}{6}+\frac{x^{8}}{24}+\cdots
$$

Step 8. Check. The derivative of the series is $2x+\frac{4x^{3}}{2}+\frac{6x^{5}}{6}+\cdots$, which is $2x+2x^{3}+x^{5}+\cdots$. The product $2xy$ is $2x+2x^{3}+x^{5}+\cdots$, the same series. The starting value is the constant term, which is one. Both statements hold.

Step 9. Recognise the answer: the coefficients are one over the factorial of half the power, so the series is the exponential of $x^{2}$.

$$
y=\sum_{k=0}^{\infty}\frac{x^{2k}}{k!}=e^{x^{2}}
$$

Step 10. Interpret the pattern. The odd coefficients vanish because the equation links each coefficient to the one two places before it, and the starting values of the two chains are $a_{0}=1$ and $a_{1}=0$. A chain that starts at zero stays at zero, so only the even powers survive.

### 4.5 Problem: a second-order equation at a cooperative point

Find the general power series solution of

$$
\frac{d^{2}y}{dx^{2}}+y=0
$$

about the point zero, giving four terms of each family, and identify the two families.

### 4.6 Solution: two free constants, two series

Step 1. Classify the point. After dividing by the coefficient of the second derivative, which is one, the coefficient of the first derivative is zero and the coefficient of $y$ is one. Both are constants, hence polynomials, hence perfectly regular everywhere, so zero is an ordinary point. The two solution families are guaranteed.

Step 2. Write the series and its second derivative.

$$
y=a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+a_{4}x^{4}+\cdots,\qquad \frac{d^{2}y}{dx^{2}}=2a_{2}+6a_{3}x+12a_{4}x^{2}+20a_{5}x^{3}+\cdots
$$

Step 3. Add the two sides of the equation, lining up the powers.

$$
2a_{2}+a_{0}+\left(6a_{3}+a_{1}\right)x+\left(12a_{4}+a_{2}\right)x^{2}+\left(20a_{5}+a_{3}\right)x^{3}+\cdots=0
$$

Step 4. Compare coefficients. Every bracket must vanish.

$$
2a_{2}+a_{0}=0,\qquad 6a_{3}+a_{1}=0,\qquad 12a_{4}+a_{2}=0,\qquad 20a_{5}+a_{3}=0
$$

Step 5. Write the general rule with the numbers replaced by letters.

$$
(n+2)(n+1)a_{n+2}+a_{n}=0\qquad\text{so}\qquad a_{n+2}=-\frac{a_{n}}{(n+1)(n+2)}
$$

Step 6. Run the recurrence, keeping $a_{0}$ and $a_{1}$ free.

$$
a_{2}=-\frac{a_{0}}{2},\qquad a_{3}=-\frac{a_{1}}{6},\qquad a_{4}=-\frac{a_{2}}{12}=\frac{a_{0}}{24},\qquad a_{5}=-\frac{a_{3}}{20}=\frac{a_{1}}{120}
$$

Step 7. Continue to the next two coefficients, to show the alternating sign.

$$
a_{6}=-\frac{a_{4}}{30}=-\frac{a_{0}}{720},\qquad a_{7}=-\frac{a_{5}}{42}=-\frac{a_{1}}{5040}
$$

Step 8. Write the general solution, grouping by the free constants.

$$
y=a_{0}\left(1-\frac{x^{2}}{2}+\frac{x^{4}}{24}-\frac{x^{6}}{720}+\cdots\right)+a_{1}\left(x-\frac{x^{3}}{6}+\frac{x^{5}}{120}-\frac{x^{7}}{5040}+\cdots\right)
$$

Step 9. Recognise the two brackets. The first is the series of the cosine and the second is the series of the sine, so

$$
y=a_{0}\cos x+a_{1}\sin x .
$$

Step 10. Check. The second derivative of the cosine is minus the cosine and the second derivative of the sine is minus the sine, so each bracket satisfies the equation; the first bracket equals one at zero with zero derivative, and the second equals zero at zero with derivative one, so the constants are the starting values of the function and of its slope.

### 4.7 Problem: a complete Frobenius calculation

Find the general solution of

$$
2x^{2}\frac{d^{2}y}{dx^{2}}-x\frac{dy}{dx}+\left(1-x^{2}\right)y=0
$$

about the point zero, giving three non-zero terms of each solution and checking the first solution.

### 4.8 Solution: classify, find the two powers, then recur

Step 1. Divide by $2x^{2}$ and read off the two coefficient functions.

$$
\frac{d^{2}y}{dx^{2}}-\frac{1}{2x}\frac{dy}{dx}+\frac{1-x^{2}}{2x^{2}}y=0
$$

Step 2. Check the two products at zero. The first is minus one half and the second is one half, both finite, so the point is a regular singular point and the Frobenius recipe applies.

Step 3. Write the indicial equation, using the two constants just found.

$$
r(r-1)-\frac{r}{2}+\frac{1}{2}=0\qquad\Longrightarrow\qquad 2r^{2}-3r+1=0\qquad\Longrightarrow\qquad r=\frac{1}{2}\ \text{or}\ r=1
$$

Step 4. The roots differ by one half, which is not a whole number, so this is the first of the three cases: two plain Frobenius series, no logarithm. The details of the recurrence were derived in Section 3.5 and are used here.

$$
a_{n}=\frac{a_{n-2}}{\left(2(n+r)-1\right)\left(n+r-1\right)},\qquad a_{1}=0
$$

Step 5. Use the larger root $r=1$. The denominators are five times two at the first step and nine times four at the second step.

$$
a_{2}=\frac{a_{0}}{10},\qquad a_{4}=\frac{a_{2}}{36}=\frac{a_{0}}{360}
$$

$$
y_{1}=a_{0}x\left(1+\frac{x^{2}}{10}+\frac{x^{4}}{360}+\cdots\right)
$$

Step 6. Use the smaller root $r=\frac{1}{2}$. The denominators are four times one and a half at the first step, which is six, and eight times three and a half at the second, which is twenty-eight.

$$
a_{2}=\frac{a_{0}}{6},\qquad a_{4}=\frac{a_{2}}{28}=\frac{a_{0}}{168}
$$

$$
y_{2}=b_{0}x^{1/2}\left(1+\frac{x^{2}}{6}+\frac{x^{4}}{168}+\cdots\right)
$$

Step 7. Write the general solution.

$$
y=Ax\left(1+\frac{x^{2}}{10}+\frac{x^{4}}{360}+\cdots\right)+Bx^{1/2}\left(1+\frac{x^{2}}{6}+\frac{x^{4}}{168}+\cdots\right)
$$

Step 8. Check the first solution by substitution, keeping three terms. Take $y=x+\frac{x^{3}}{10}+\frac{x^{5}}{360}$ and compute the three pieces of the equation separately.

$$
2x^{2}\frac{d^{2}y}{dx^{2}}=\frac{6x^{3}}{5}+\frac{x^{5}}{9}
$$

$$
-x\frac{dy}{dx}=-x-\frac{3x^{3}}{10}-\frac{x^{5}}{72}
$$

$$
\left(1-x^{2}\right)y=x+\frac{x^{3}}{10}+\frac{x^{5}}{360}-x^{3}-\frac{x^{5}}{10}
$$

Step 9. Add the three pieces and read the coefficients. The coefficient of $x$ is $-1+1$, which is zero. The coefficient of $x^{3}$ is $\frac{6}{5}-\frac{3}{10}-\frac{9}{10}$, which is zero. The coefficient of $x^{5}$ is

$$
\frac{1}{9}-\frac{1}{72}+\frac{1}{360}-\frac{1}{10}=0 .
$$

So all three retained powers cancel, and the first surviving power is beyond the terms kept, which confirms the recurrence.

Step 10. Interpret. The solution beginning with $x$ is perfectly smooth near zero; the solution beginning with $x^{1/2}$ is not differentiable at zero, because its derivative contains $x^{-1/2}$. Both are genuine solutions for positive $x$, and the square root warns us that the second one lives only on the positive side or only on the negative side, not across the origin.

### 4.9 Problem: a second-order equation with a right-hand side

Solve

$$
\frac{d^{2}y}{dx^{2}}-y=x
$$

in powers of $x$, taking the first free coefficient to be one and the second to be zero, and check the answer.

### 4.10 Solution: the right-hand side alters one line only

Step 1. Classify the point. The equation is already in the required form, with both coefficient functions constant, so zero is an ordinary point.

Step 2. Substitute the series and its second derivative.

$$
\left(2a_{2}+6a_{3}x+12a_{4}x^{2}+20a_{5}x^{3}+\cdots\right)-\left(a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+\cdots\right)=x
$$

Step 3. Compare coefficients. The right-hand side has coefficient one at the power $x$ and zero at every other power, so exactly one line is changed.

$$
2a_{2}-a_{0}=0,\qquad 6a_{3}-a_{1}=1,\qquad 12a_{4}-a_{2}=0,\qquad 20a_{5}-a_{3}=0
$$

Step 4. Solve each line, with $a_{0}=1$ and $a_{1}=0$.

$$
a_{2}=\frac{1}{2},\qquad a_{3}=\frac{1}{6},\qquad a_{4}=\frac{a_{2}}{12}=\frac{1}{24},\qquad a_{5}=\frac{a_{3}}{20}=\frac{1}{120}
$$

Step 5. Continue one step further to see the pattern clearly.

$$
a_{6}=\frac{a_{4}}{30}=\frac{1}{720},\qquad a_{7}=\frac{a_{5}}{42}=\frac{1}{5040}
$$

Step 6. Write the answer.

$$
y=1+\frac{x^{2}}{2}+\frac{x^{3}}{6}+\frac{x^{4}}{24}+\frac{x^{5}}{120}+\frac{x^{6}}{720}+\frac{x^{7}}{5040}+\cdots
$$

Step 7. Group the terms. The even powers form the hyperbolic cosine series, the odd powers form the hyperbolic sine series, and there is one extra piece.

$$
y=\left(1+\frac{x^{2}}{2}+\frac{x^{4}}{24}+\frac{x^{6}}{720}+\cdots\right)+\left(x+\frac{x^{3}}{6}+\frac{x^{5}}{120}+\frac{x^{7}}{5040}+\cdots\right)-x
$$

Step 8. Check by differentiation. The first bracket differentiates twice to itself, and so does the second, while the extra piece $-x$ differentiates twice to zero. Therefore

$$
\frac{d^{2}y}{dx^{2}}-y=\left(\cosh x+\sinh x\right)-\left(\cosh x+\sinh x-x\right)=x ,
$$

so the equation holds. The other choice of the free coefficients simply adds a multiple of the homogeneous solutions, which is the general case.

Step 9. Interpret. The right-hand side of a non-homogeneous equation changes the equations for a few low coefficients but leaves the shape of the recurrence untouched. That is the practical meaning of the theorem of Section 2.8: the homogeneous part supplies the two free constants, and the right-hand side supplies one fixed extra solution.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 How far the answer can be trusted

Every series produced in this note is valid only on an interval, and the interval is decided by the equation rather than by the answer. The rule of thumb is that the series about a point is guaranteed to work up to the nearest singular point.

For the equation of Section 4.7, the only singular point is zero itself, so the two series converge for every positive $x$, and the only restriction is the sign of $x$ forced by the square root. For an equation such as $\left(1-x^{2}\right)y''+y=0$, whose singular points are at $1$ and $-1$, a series about zero is guaranteed only for $x$ between $-1$ and $1$, even though the answer may be meaningful further out.

There is a subtlety worth knowing. The distance to a singular point is measured in the complex plane, so an equation with no real singular point at all can still have a series whose interval stops short. The equation $\left(1+x^{2}\right)y''+y=0$ has singularities at the imaginary numbers $i$ and $-i$, both at distance one from zero, so its series about zero cannot reach beyond $x$ equal to $1$ or $-1$. Nothing on the real line explains the barrier, which is why the complex view is needed.

### 5.2 What happens at a bad point

At an irregular singular point the whole approach collapses, and no amount of algebra repairs it. The example

$$
x^{3}\frac{d^{2}y}{dx^{2}}+y=0
$$

has its singular point at zero, and the product of $x^{2}$ with the coefficient of $y$ is one over $x$, which still blows up. If the Frobenius recipe is tried, the lowest power in the equation comes out as $x^{r-1}$ with coefficient $a_{0}$, which can only vanish if $a_{0}$ is zero, contradicting the requirement that it is not. The recipe therefore produces nothing.

The true solutions of such an equation behave in a way that no power series can imitate: they grow or decay extremely fast as the point is approached, like an exponential of a reciprocal power. Describing them requires a different theory, using what are called asymptotic expansions, which are finite sums with a controlled error rather than infinite convergent series. That theory belongs to a later course, and it is enough here to be able to recognise the situation and say that the method does not apply.

### 5.3 What the method is good for

The first use is the one in the examples: obtaining a solution when no formula exists. The second is obtaining a formula when one does exist but is hard to guess, as with the exponential in Section 4.1. The third, and in practice the most important, is the definition of the classical special functions. Legendre's equation, Bessel's equation and Hermite's equation all have solutions that are not elementary, and those solutions are defined by their series. The Legendre polynomials, the Bessel functions and the Hermite polynomials are not mysterious objects brought in from outside; they are exactly the series that the recurrences of this topic produce.

The fourth use is numerical. Truncating a series after a few terms gives a polynomial that approximates the solution, and for small values of the variable the approximation is excellent because the terms shrink quickly. This is what a calculator or a computer algebra system does when it reports a series solution, and the recurrence derived here is the algorithm behind it.

### 5.4 Beginner misconceptions

The following mistakes are so common that each deserves a name and a cure.

1. **"The series is an approximation."** It is not. A convergent power series equals the function exactly on its interval. Truncating it gives an approximation, but the infinite sum does not. The cure is to say "the truncated series approximates" and never "the series approximates".

2. **"Any equation has a power series solution."** Only at an ordinary point, or at a regular singular point with the modified recipe. At an irregular point there is none, as Section 5.2 shows. The cure is always to classify the point first, before writing any series.

3. **"I can start the sum wherever I like."** The starting value is tied to the power. If a term is written with power $n+1$, the sum starts at one when rewritten with power $m$. The cure is to write the change of letter explicitly and to move the starting value at the same time.

4. **"The general recurrence works at the first step too."** It usually does not, because the lowest powers receive fewer contributions. The coefficient of the constant term and of $x$ must be treated as separate equations. The cure is to write those two lines before the general rule.

5. **"The first two coefficients are always free."** They are free at an ordinary point. At a regular singular point the first coefficient after $a_{0}$ is often forced to be zero, and the free quantity is the power $r$ together with $a_{0}$. The cure is to read each coefficient relation from the equation rather than from memory.

6. **"A fractional power is impossible because the answer must be a polynomial."** Fractional powers are exactly what the Frobenius recipe is designed to produce, and the example of Section 4.7 produces $x^{1/2}$ legitimately. The cure is to remember that the series is a solution where it is defined, which may be only for positive $x$.

7. **"Logarithms never appear."** They appear whenever the indicial equation has a repeated root, and they can appear when the roots differ by a whole number. The cure is to compute the difference of the roots and to check the divisor of the recurrence.

8. **"If the roots differ by a whole number, a logarithm is certain."** Not certain. In the equation $x^{2}y''+xy'-4y=0$ the roots differ by four and the solutions are the plain powers $x^{2}$ and $x^{-2}$. The logarithm appears only when a certain coefficient turns out to be non-zero, which must be computed.

9. **"The two roots always give two independent solutions."** At a repeated root they give the same family, and the second solution has to be found separately. The cure is to compare the roots before assuming two series.

10. **"Once the recurrence is found, the problem is finished."** The answer must still be assembled with the correct factor $x^{r}$, the two families must be shown to be independent, and the interval must be stated. The cure is to finish with a check, either by substituting the first terms back or by recognising the series.

11. **"The interval of convergence is infinite because the answer looks like an exponential."** The interval is decided by the coefficients of the equation, not by the appearance of the answer. The cure is to locate the singular points before quoting an interval.

12. **"A series solution is only valid at the point of expansion."** It is valid on a whole interval around that point, of a length determined by the nearest singular point. The cure is to state the interval explicitly.

### 5.5 Key takeaways

The topic can be summarised in six sentences, and a student who can say all six has understood it.

First, a power series represents a function exactly on its interval, and a differential equation determines the coefficients one after another.

Second, the point of expansion must be classified before anything else, because the classification decides which of the two recipes is used.

Third, at an ordinary point the plain series always works and the first two coefficients are free, which is why the answer has the two constants a second-order equation needs.

Fourth, at a regular singular point the series is multiplied by an unknown power, and that power is found from the indicial equation built out of the two limit values of the coefficient functions.

Fifth, the roots of the indicial equation decide whether a second plain series exists, whether a logarithm is forced, or whether a logarithm may appear and must be computed.

Sixth, the right-hand side of a non-homogeneous equation changes only a few coefficient relations, so the homogeneous machinery is reused almost without alteration and one extra particular solution is added at the end.

None of this requires cleverness. It requires the discipline of writing each step out, keeping the powers and the starting values together, and checking the answer at the end by substitution.
