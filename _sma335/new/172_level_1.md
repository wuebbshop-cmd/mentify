## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 An everyday picture of the whole topic

Imagine you are asked to sort a mixed heap of laundry into two baskets, one for shirts and one for socks. The job looks messy while everything is jumbled together, but it becomes easy the moment each item sits in its own basket: you can then fold each basket separately without thinking about the other one. Every method in this topic is a way of getting a messy mixture into two tidy baskets.

A differential equation can arrive in a messy mixed form, with the two variables tangled together on the same side. When the mixing is only a product, the sorting is possible, and once it is done each side can be integrated on its own. That is the first method, called separation of variables.

Some equations cannot be sorted directly, but can be made sortable by renaming one of the unknowns. Picture a shelf of jars whose labels are all written in the wrong language: the contents are fine, only the names are wrong. Rewriting the label does not change the contents, yet suddenly every jar makes sense. In this topic the renaming is a substitution, and the most important one replaces the unknown function by a new letter equal to its ratio to the other variable. That is the second method, for homogeneous equations.

Finally, some equations are almost homogeneous, spoiled only by a constant number added to each of two straight-line expressions. Think of a photograph of a grid of streets taken slightly off-centre: the pattern of the streets is regular, but the origin of the grid is in the wrong place. Slide the photograph until the crossing point of two chosen streets sits under the centre mark, and the pattern becomes perfectly regular again. That sliding is the third method, and it turns a spoiled equation into a homogeneous one.

The rest of this section names the pieces of that picture, and every symbol is explained in words before it is used.

### 1.2 What the symbols mean

The letter $x$ stands for the input variable, usually thought of as a position along a horizontal axis. The letter $y$ stands for the output, the unknown function of $x$ that we are trying to find. The two letters are linked by an equation, and solving the equation means finding the rule that produces $y$ from $x$.

The symbol $\frac{dy}{dx}$ is a single symbol, read as the derivative of $y$ with respect to $x$. In words it is the rate at which $y$ changes as $x$ increases by a tiny amount. It is not a fraction made of two separate numbers, even though it is written like one. A capital letter $C$ stands for an arbitrary constant, a fixed number whose value is not yet known. Because one integration is performed in each method of this topic, exactly one such constant appears in the answer.

The letters $M$ and $N$ are used for the two coefficient expressions when an equation is written with both differentials on the same side. The letter $v$ is reserved for the ratio of $y$ to $x$, that is for $y$ divided by $x$, and it is a function of $x$, not a fixed number. The letter $z$ is reserved for a combination such as $ax+by$, where $a$ and $b$ are fixed numbers. The capital letters $X$ and $Y$ stand for new coordinates after the origin has been moved, and the small letters $h$ and $k$ give the amount by which each axis is shifted.

One more word needs care. In this topic the word homogeneous is used in a special technical sense that has nothing to do with the everyday meaning of "all the same". A homogeneous equation here means that the slope prescribed by the equation depends only on the ratio of $y$ to $x$, so that it is the same at every point of a ray drawn from the origin.

### 1.3 The first method: separating the variables

The first method applies when the right-hand side of the equation is a product of two separate pieces, one piece depending only on $x$ and the other depending only on $y$.

> **Definition (Separable equation).** An equation is separable when it can be written with a factor depending on $y$ alone multiplied by the derivative on the left, and a function of $x$ alone on the right,
>
> $$
> g(y)\,\frac{dy}{dx} = h(x).
> $$

In words: the left side mentions only $y$ and its rate of change, and the right side mentions only $x$. When that shape has been achieved, both sides can be integrated, the left with respect to $y$ and the right with respect to $x$, and one constant is added at the end.

A tiny example makes the shape clear. Consider the equation

$$
\frac{dy}{dx} = \frac{2x}{y}.
$$

The right-hand side is the product of the piece $2x$, which mentions only $x$, and the piece $1/y$, which mentions only $y$. Multiplying both sides by $y$ produces $y\frac{dy}{dx} = 2x$, which is the shape of the definition with $g(y) = y$ and $h(x) = 2x$.

Not every product-shaped right-hand side factors so easily, and not every expression factors at all. The expression $x^{2}+y^{2}$ is a sum, not a product, and it cannot be rewritten as a function of $x$ times a function of $y$. An equation whose right-hand side is that expression is simply not separable, and no rearrangement will make it so. The test is always the same: try to factor, and believe the result of the attempt.

Sometimes the factoring is hidden behind common terms. The fraction

$$
\frac{2xy^{2}+2x}{2yx^{2}+2y}
$$

looks tangled, but the top has the common factor $2x$ and the bottom has the common factor $2y$, so the fraction equals $\frac{x\left(1+y^{2}\right)}{y\left(1+x^{2}\right)}$, which is a product of a piece in $x$ and a piece in $y$. The equation is therefore separable, and the tidying was the whole difficulty.

### 1.4 The idea of a homogeneous expression

The second method needs the idea of an expression that behaves well when both letters are multiplied by the same number.

> **Definition (Homogeneous of degree n).** An expression in $x$ and $y$ is homogeneous of degree $n$ when multiplying both letters by a number $k$ multiplies the whole expression by the power $k^{n}$,
>
> $$
> f(kx,ky) = k^{n}f(x,y).
> $$

In words: scale the picture by a factor $k$, and the expression scales by a predictable power of that same factor. The number $n$ is called the degree, and it must be one single number that works for every choice of the point and every choice of the scale.

Three small examples fix the idea.

The expression $x^{2}+3xy$ becomes $k^{2}x^{2}+3k^{2}xy$ after scaling, which is $k^{2}$ times the original, so its degree is two. Every term has total degree two, and that is the pattern for sums of powers.

The expression $\frac{xy}{x^{2}+y^{2}}$ becomes $\frac{k^{2}xy}{k^{2}x^{2}+k^{2}y^{2}}$, and the factor $k^{2}$ appears in the top and in the bottom and cancels, so the expression is unchanged. Its degree is zero, meaning the power $k^{0}$, which always equals one.

The expression $x+y^{2}$ becomes $kx+k^{2}y^{2}$ after scaling, and no single power of $k$ can be pulled out, because the first term wants the first power and the second term wants the second power. This expression has no degree at all, and the honest answer to a question about its degree is that no degree exists.

### 1.5 The second method: homogeneous equations

> **Definition (Homogeneous equation of first order).** A first-order equation is homogeneous when its right-hand side is homogeneous of degree zero, so that scaling both letters by the same factor leaves the slope unchanged,
>
> $$
> f(kx,ky) = f(x,y).
> $$

The reason degree zero is the right choice is worth saying in plain words. A slope compares a change in height with a change in sideways distance. If the whole picture is enlarged by the same factor in both directions, then the height change and the sideways change are both multiplied by that factor, and their ratio is untouched. An equation whose right-hand side also survives the enlargement unchanged therefore prescribes the same slope everywhere along a ray drawn from the origin. The slope depends on direction only, not on distance.

That single observation is what makes the second method work. If the slope depends only on direction, then the natural new letter to use is the ratio that measures direction, namely $y$ divided by $x$. Calling that ratio $v$ and writing $y = vx$ renames the unknown function, and the equation, which depended on two letters, ends up depending on the one letter $v$ together with $x$.

> **Definition (Homogeneous equation in the other form).** When the equation is written as
>
> $$
> M\,dx + N\,dy = 0,
> $$
>
> it is homogeneous if the two coefficient expressions $M$ and $N$ are homogeneous of the same degree.

The practical test that follows from this is short. Work out the degree of the expression multiplying $dx$, work out the degree of the expression multiplying $dy$, and compare the two answers. If the degrees agree, the equation is homogeneous. If they disagree, it is not. For instance, in the equation

$$
\left(x^{3}+y^{3}\right)dx - 3xy^{2}\,dy = 0
$$

the first coefficient has degree three because both of its terms have total degree three, and the second coefficient also has degree three because $xy^{2}$ has total degree three. The degrees agree, so the equation is homogeneous and the method applies.

### 1.6 The third method: equations that are almost homogeneous

The third family has a fraction of two straight-line expressions on the right,

$$
\frac{dy}{dx} = \frac{ax+by+c}{px+qy+r},
$$

with fixed numbers $a$, $b$, $c$, $p$, $q$, $r$. When the added numbers $c$ and $r$ are both zero the fraction is homogeneous and the second method applies unchanged. When they are not zero the fraction is spoiled, and the cure depends on how the two straight lines lie in the plane.

> **Definition (The deciding number).** For the fraction above, form the number $D$ equal to $a$ times $q$ minus $b$ times $p$. If $D$ is not zero the two straight lines cross at a single point. If $D$ is zero the two straight lines are parallel or coincide.

The number $D$ is a single test with two outcomes, and each outcome has its own cure.

When $D$ is not zero, the two lines cross. Find the crossing point, call its coordinates $h$ and $k$, and then measure every position from that point instead of from the original origin. In the new measurements the added constants disappear, as the photograph analogy promised, and the equation becomes homogeneous. That is the third method.

When $D$ is zero, the two lines never cross. Then both the top and the bottom of the fraction are built from the same combination $ax+by$, differing only by a multiplying number and an added number. Naming that combination $z$ turns the whole equation into a separable one, which is the first method again.

### 1.7 What a solution looks like and what a constant does

A solution of a first-order equation is a function that satisfies the equation at every point of some interval. Because one integration is carried out in each method, the answer always contains exactly one arbitrary constant, and different values of that constant give different curves.

The constant may be renamed freely. Replacing $C$ by $2C$, or by $C-5$, changes nothing, because the collection of numbers the symbol can take is the same collection. This freedom is what allows a final answer to be tidied into a neat polynomial relation.

When integration produces logarithms, a helpful bookkeeping device is to write the constant as the logarithm of a positive number. Doing so lets two logarithmic terms be combined into one, which usually turns the answer into a simple algebraic equation. The device is not a trick; every real number is the logarithm of exactly one positive number, so nothing is lost.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Result 1: separation works because both sides can be integrated

> **Result 1.** If an equation can be written as $g(y)\frac{dy}{dx} = h(x)$, then its solutions satisfy
>
> $$
> \int g(y)\,dy = \int h(x)\,dx + C .
> $$

The justification is short. Take any solution, integrate the left side with respect to $x$ by reversing the chain rule, integrate the right side directly, and observe that two functions with the same derivative differ only by a constant. Nothing about the symbols $dy$ and $dx$ as separate numbers is being assumed; the equality of derivatives is what carries the argument.

The result says that a separable equation is never harder than two integrations. It promises nothing about whether those integrations can be performed in terms of familiar functions, and that is a separate matter discussed later.

### 2.2 Result 2: a degree-zero expression depends on one ratio only

> **Result 2.** If an expression satisfies $f(kx,ky) = f(x,y)$ for every positive scale factor, then there is a function $F$ of one variable with
>
> $$
> f(x,y) = F\!\left(\frac{y}{x}\right).
> $$

The proof is a single substitution. Choose the scale factor $k$ to be $1/x$, so that the first letter becomes exactly one and the second letter becomes $y/x$. Since the expression is unchanged by scaling, its value at the point is the same as its value at the point with first letter one and second letter equal to the ratio. That value depends on the ratio and on nothing else.

This is the reason the substitution $y = vx$ must work. The equation, once written in terms of the ratio, no longer contains two independent letters. There is nothing left to separate it from.

### 2.3 Result 3: the two-degree test

> **Result 3.** If the two coefficient expressions in $M\,dx + N\,dy = 0$ are homogeneous of the same degree, then the equation is homogeneous.

The reason is that the equation can be rearranged to give the slope as minus $M$ divided by $N$. Dividing two expressions of the same degree cancels the scale factor completely, since the power of $k$ in the top matches the power of $k$ in the bottom. What remains is unchanged by scaling, which is precisely degree zero.

The result also explains the failure mode. If the top has degree three and the bottom has degree two, the quotient keeps one leftover power of $k$ after cancelling, so it does not survive scaling unchanged, and the equation is not homogeneous.

### 2.4 Result 4: the substitution turns a homogeneous equation into a separable one

> **Result 4.** Put $y = vx$ in a homogeneous equation whose right-hand side is $F$ of the ratio. The equation becomes
>
> $$
> x\frac{dv}{dx} = F(v)-v ,
> $$
>
> which separates into $\frac{dv}{F(v)-v} = \frac{dx}{x}$.

Two facts are needed, and both are one line long. The first is that the derivative of $y = vx$ is $v + x\frac{dv}{dx}$, obtained by the product rule, because $v$ is itself a function of $x$ and not a constant. The second is that the right-hand side, being degree zero, is a function of the ratio alone by Result 2.

Substituting both facts gives $v + x\frac{dv}{dx} = F(v)$. Subtracting $v$ from both sides leaves the derivative term alone on the left and a function of $v$ alone on the right, while the left side also carries the factor $x$. A function of $v$ on one side and a function of $x$ on the other is exactly the separable shape of Result 1.

The conclusion deserves emphasis: the method does not solve the equation by cleverness, it converts one type of equation into another type already solved. That is the pattern of every substitution method in the subject.

### 2.5 Result 5: the two outcomes of the deciding number

> **Result 5.** For $\frac{dy}{dx} = \frac{ax+by+c}{px+qy+r}$ with $D = aq-bp$, the case $D \neq 0$ is cured by moving the origin to the crossing point of the two lines, and the case $D = 0$ is cured by naming the repeated combination $ax+by$.

When $D$ is not zero, the two lines cross at exactly one point, because two straight lines with different directions always meet once. Measuring from that point means writing $x$ as the new first coordinate plus $h$ and $y$ as the new second coordinate plus $k$. Expanding the top of the fraction produces the old top plus the number $ah+bk+c$, and that number is zero precisely because the crossing point lies on the line. The added numbers therefore vanish from both the top and the bottom, leaving a fraction of two homogeneous expressions of degree one, which is homogeneous of degree zero.

When $D$ is zero, the two coefficient pairs are proportional, so the bottom is a multiple of the top's variable part plus a number. The fraction therefore depends only on the single combination $ax+by$. Naming that combination $z$ gives an equation linking $z$ and $x$, and since the derivative of $z$ is a fixed number plus a fixed multiple of the derivative of $y$, the equation becomes separable in $z$ and $x$.

There is no third outcome, because a number is either zero or not zero. A student who cannot decide the case has simply not computed $D$.

### 2.6 Result 6: a straight ray can be a solution, and can be lost

> **Result 6.** If the function $F$ of the ratio satisfies $F(v_{0}) = v_{0}$ for some fixed number $v_{0}$, then the straight line $y = v_{0}x$ is a solution of the homogeneous equation, and it disappears when the variables are separated.

Along that line the slope is constantly $v_{0}$, and the right-hand side, evaluated at the ratio $v_{0}$, is also $v_{0}$, so the line satisfies the equation exactly. But the separation step divides by $F(v)-v$, which is zero at $v_{0}$, so the line is excluded from the integrated formula. It must be recorded separately.

The simplest case is the equation in which the slope equals the ratio itself. There the reduced equation reads $x\frac{dv}{dx} = 0$, so $v$ is constant and every straight line through the origin is a solution. In that example the "lost" value is not lost at all, because the whole family consists of such lines.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Derivation of the derivative of $y = vx$

Start from the substitution itself, in which $v$ is a function of $x$.

$$
y = vx
$$

Differentiate both sides with respect to $x$, using the product rule on the right.

$$
\frac{dy}{dx} = \frac{dv}{dx}\cdot x + v\cdot 1
$$

Rearrange the two terms into the order used everywhere afterwards.

$$
\frac{dy}{dx} = v + x\frac{dv}{dx}
$$

The second term is the one that beginners forget. If $v$ were a constant, that term would vanish and the substitution would carry no information, which is a sign that the second term is the whole point.

### 3.2 Derivation of the reduced homogeneous equation

Write the homogeneous equation with the right-hand side expressed as a function of the ratio.

$$
\frac{dy}{dx} = F\!\left(\frac{y}{x}\right)
$$

Substitute $y = vx$ and the derivative just derived.

$$
v + x\frac{dv}{dx} = F(v)
$$

Subtract $v$ from both sides.

$$
x\frac{dv}{dx} = F(v)-v
$$

Divide by $F(v)-v$ and by $x$, which is legitimate wherever neither is zero.

$$
\frac{dv}{F(v)-v} = \frac{dx}{x}
$$

The left side now mentions only $v$ and the right side only $x$, so the first method applies and one integration finishes the job.

### 3.3 Derivation of the translation that removes the constants

Suppose the two straight lines cross at the point whose coordinates are $h$ and $k$, so that both of these statements hold.

$$
ah + bk + c = 0
$$

$$
ph + qk + r = 0
$$

Now replace each old coordinate by a new coordinate plus the shift.

$$
x = X + h, \qquad y = Y + k
$$

Substitute into the top of the fraction and group the terms.

$$
a\left(X+h\right) + b\left(Y+k\right) + c = aX + bY + \left(ah+bk+c\right)
$$

The bracket is zero by the first of the two crossing-point statements, so the top becomes $aX+bY$. Repeating the same step for the bottom gives $pX+qY$. Since the shifts are constants, the differentials are unchanged, so the equation in the new letters is homogeneous.

### 3.4 Derivation of the parallel reduction

Suppose the deciding number is zero, so the two coefficient pairs are proportional. Then the equation has the shape in which both the top and the bottom depend on the same combination $ax+by$.

$$
\frac{dy}{dx} = G\!\left(ax+by\right)
$$

Name that combination $z$ and differentiate with respect to $x$.

$$
z = ax+by, \qquad \frac{dz}{dx} = a + b\frac{dy}{dx}
$$

Substitute the expression for the slope from the equation into the derivative of $z$.

$$
\frac{dz}{dx} = a + b\,G(z)
$$

The right side mentions only $z$, so separating gives a left side in $z$ alone and a right side equal to $dx$, and one integration finishes the job.

### 3.5 Method card: separation of variables

1. Write the equation so that the slope is alone on the left.
2. Factor the right-hand side completely, looking for a piece in $x$ times a piece in $y$.
3. Move the $y$-piece to the left by dividing, and move $dx$ to the right, recording every value at which the division is illegal.
4. Integrate both sides and add exactly one constant.
5. Make the answer explicit if the algebra allows it; otherwise leave it in implicit form and say so.
6. Use any given initial condition to fix the constant.
7. Differentiate the answer and check that it reproduces the original equation.

### 3.6 Method card: homogeneous equations

1. Test the right-hand side by scaling both letters; if a single power of the scale factor comes out, note its exponent.
2. If the exponent is zero, rewrite the right side as a function of the ratio by dividing top and bottom by a suitable power of $x$.
3. Substitute $y = vx$ and the two-term derivative.
4. Subtract $v$ and simplify over a single denominator.
5. Separate, recording the values of $v$ for which the denominator vanishes.
6. Integrate, combining logarithms where they appear.
7. Replace $v$ by $y$ divided by $x$ and clear fractions.
8. Differentiate the answer and check it against the original equation, and check whether any recorded value gives an extra straight-line solution.

### 3.7 Method card: equations that are almost homogeneous

1. Compute the deciding number $D$ equal to $a$ times $q$ minus $b$ times $p$.
2. If $D$ is not zero, solve the two crossing-point equations for $h$ and $k$.
3. Replace $x$ by the new coordinate plus $h$ and $y$ by the new coordinate plus $k$.
4. Confirm that the added numbers have vanished, then solve the resulting homogeneous equation by the previous card.
5. Translate the answer back into the original letters and expand if a neat polynomial form is wanted.
6. If $D$ is zero, name the repeated combination $ax+by$ as $z$ and express the slope in terms of $z$.
7. Separate in $z$ and $x$, integrate, and put the combination back.
8. Differentiate the answer and check it against the original equation.

### 3.8 Why the answer always has one constant

Each method performs exactly one integration: the separated equation is integrated once, and the substitutions change letters without integrating anything. One integration produces one arbitrary constant, so the answer is a one-parameter family of curves, matching the order of the equation.

If a computation seems to produce two constants, one of two things has happened. Either an integral was split into two pieces and each piece was given its own constant, in which case the two must be combined into one, or an integration was performed twice by mistake. Counting the constants at the end is a reliable check on the whole calculation.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a separable equation with a starting value

Solve $\frac{dy}{dx} = \frac{2x}{y}$ with the starting value $y = 2$ when $x = 0$.

### 4.2 Solution: sort, integrate, fix the constant, check

Step 1. Look at the right side. It is $2x$ times $1/y$, a piece in $x$ times a piece in $y$, so the equation is separable.

Step 2. Multiply both sides by $y$ so that all the $y$ material sits on the left.

$$
y\frac{dy}{dx} = 2x
$$

Step 3. Integrate both sides. The left is integrated with respect to $y$ and the right with respect to $x$.

$$
\int y\,dy = \int 2x\,dx
$$

Step 4. Carry out both integrations and add one constant.

$$
\frac{y^{2}}{2} = x^{2} + C
$$

Step 5. Multiply by two to clear the fraction.

$$
y^{2} = 2x^{2} + C'
$$

Step 6. Use the starting value. When $x$ is zero the value of $y$ is two, so four equals zero plus the constant.

$$
4 = 0 + C', \qquad C' = 4
$$

Step 7. Write the answer.

$$
y^{2} = 2x^{2} + 4
$$

Step 8. Choose the branch. The curve starts at a positive value, so the positive square root is intended.

$$
y = \sqrt{2x^{2}+4}
$$

Step 9. Check. Differentiating the squared relation gives $2y\frac{dy}{dx} = 4x$, so the slope is $2x$ divided by $y$, which is exactly the original right-hand side. At $x$ equal to zero the value is the square root of four, which is two, as required.

### 4.3 Problem: a separable equation that produces an exponential

Solve $\frac{dy}{dx} = y$ with the starting value $y = 3$ when $x = 0$.

### 4.4 Solution: divide by $y$, integrate, exponentiate, check

Step 1. The right side is $y$ itself, which is a piece in $y$ times the constant piece $1$ in $x$. So the equation is separable.

Step 2. Divide both sides by $y$, which is legal wherever $y$ is not zero.

$$
\frac{1}{y}\frac{dy}{dx} = 1
$$

Step 3. Integrate both sides.

$$
\int \frac{1}{y}\,dy = \int 1\,dx
$$

Step 4. Carry out the integrations and add one constant.

$$
\ln|y| = x + C
$$

Step 5. Undo the logarithm by exponentiating both sides, and write the positive number $e^{C}$ as a single new constant.

$$
|y| = e^{C}e^{x}
$$

Step 6. Allow for the sign by letting a single constant carry it.

$$
y = Ae^{x}
$$

Step 7. Use the starting value. When $x$ is zero the exponential equals one, so the constant is three.

$$
3 = A
$$

Step 8. Write the answer.

$$
y = 3e^{x}
$$

Step 9. Check. The derivative of the answer is $3e^{x}$, which equals the answer itself, and the value at $x$ equal to zero is three. Both parts of the problem are satisfied.

Step 10. Note the excluded case. Dividing by $y$ excluded the function that is zero everywhere, and that function does satisfy the original equation, so it is a genuine solution that the family reaches only in the limit as the constant tends to zero.

### 4.5 Problem: an easy homogeneous equation

Solve $\frac{dy}{dx} = \frac{y}{x} + 1$ with the starting value $y = 2$ when $x = 1$.

### 4.6 Solution: test, substitute, separate, restore the ratio, check

Step 1. Test the right side by scaling. Scaling both letters by $k$ turns the right side into $\frac{ky}{kx} + 1$, and the fraction is unchanged because the scale factor cancels. So the right side is homogeneous of degree zero.

Step 2. Note that the right side is already written as a function of the ratio, with the function being the identity plus one.

Step 3. Substitute $y = vx$ together with the two-term derivative.

$$
v + x\frac{dv}{dx} = v + 1
$$

Step 4. Subtract $v$ from both sides.

$$
x\frac{dv}{dx} = 1
$$

Step 5. Separate the letters.

$$
dv = \frac{dx}{x}
$$

Step 6. Integrate both sides and add one constant.

$$
v = \ln x + C
$$

Step 7. Put the ratio back in place of $v$.

$$
\frac{y}{x} = \ln x + C
$$

Step 8. Multiply by $x$ to obtain the general answer.

$$
y = x\ln x + Cx
$$

Step 9. Use the starting value. At $x$ equal to one the logarithm is zero and $x$ is one, so two equals the constant.

$$
2 = 0 + C, \qquad C = 2
$$

Step 10. Write the answer.

$$
y = x\ln x + 2x
$$

Step 11. Check. Differentiating gives the slope as the logarithm of $x$ plus one plus two. The right side of the original equation is the answer divided by $x$, plus one, which is the logarithm of $x$ plus two, plus one. The two expressions agree, and the value at $x$ equal to one is two.

### 4.7 Problem: a homogeneous equation with squares

Solve $\frac{dy}{dx} = \frac{x^{2}+y^{2}}{xy}$.

### 4.8 Solution: degree test, substitution, a short integral, restore, check

Step 1. Test the degrees. The top is a sum of two terms each of total degree two, so its degree is two. The bottom is $xy$, of total degree two. The degrees agree, so the equation is homogeneous.

Step 2. Divide top and bottom by $x^{2}$ to expose the ratio.

$$
\frac{dy}{dx} = \frac{1+\left(y/x\right)^{2}}{y/x}
$$

Step 3. Substitute $y = vx$ and the two-term derivative.

$$
v + x\frac{dv}{dx} = \frac{1+v^{2}}{v}
$$

Step 4. Subtract $v$ and simplify. The right side becomes one over $v$ plus $v$, and the $v$ cancels.

$$
x\frac{dv}{dx} = \frac{1}{v}
$$

Step 5. Separate the letters.

$$
v\,dv = \frac{dx}{x}
$$

Step 6. Integrate both sides and add one constant.

$$
\frac{v^{2}}{2} = \ln x + c
$$

Step 7. Put the ratio back and clear the fraction.

$$
\frac{y^{2}}{2x^{2}} = \ln x + c
$$

Step 8. Multiply by two times $x^{2}$ and relabel the constant.

$$
y^{2} = 2x^{2}\ln x + Cx^{2}
$$

Step 9. Check. Differentiating the relation gives $2y\frac{dy}{dx}$ equal to four times $x$ times the logarithm of $x$, plus two times $x$, plus two times the constant times $x$. Dividing by $2y$ and comparing with the original right side, which is the top over the bottom, both reduce to the same expression. The answer therefore satisfies the equation, and it carries one constant as a first-order answer must.

### 4.9 Problem: an equation whose two straight lines are parallel

Solve $\frac{dy}{dx} = \frac{x+y+1}{x+y-1}$.

### 4.10 Solution: decide the case, name the combination, separate, restore, check

Step 1. Compute the deciding number. Here $a$ and $b$ are both one, and $p$ and $q$ are both one, so the number is one times one minus one times one, which is zero. The two straight lines are therefore parallel and the first cure applies.

Step 2. Notice the repeated combination. Both the top and the bottom are built from $x+y$, with an added number in each.

Step 3. Name the combination $z$ and differentiate it.

$$
z = x+y, \qquad \frac{dz}{dx} = 1 + \frac{dy}{dx}
$$

Step 4. Solve for the slope in terms of the derivative of $z$.

$$
\frac{dy}{dx} = \frac{dz}{dx} - 1
$$

Step 5. Substitute into the equation, with the right side written in terms of $z$.

$$
\frac{dz}{dx} - 1 = \frac{z+1}{z-1}
$$

Step 6. Add one to both sides and combine over a single denominator.

$$
\frac{dz}{dx} = \frac{z+1}{z-1} + 1 = \frac{z+1+z-1}{z-1} = \frac{2z}{z-1}
$$

Step 7. Separate the letters by turning the fraction over.

$$
\frac{z-1}{2z}\,dz = dx
$$

Step 8. Split the left side into two easy pieces.

$$
\frac{1}{2}\left(1 - \frac{1}{z}\right)dz = dx
$$

Step 9. Integrate both sides and add one constant.

$$
\frac{1}{2}\left(z - \ln|z|\right) = x + c
$$

Step 10. Multiply by two.

$$
z - \ln|z| = 2x + C
$$

Step 11. Put the combination back.

$$
x + y - \ln|x+y| = 2x + C
$$

Step 12. Tidy the linear terms into a single answer.

$$
y - x - \ln|x+y| = C
$$

Step 13. Check. Differentiate the answer, remembering that the derivative of the logarithm of $x+y$ is one plus the slope, divided by $x+y$.

$$
\frac{dy}{dx} - 1 - \frac{1+\frac{dy}{dx}}{x+y} = 0
$$

Step 14. Multiply through by $x+y$ and collect the slope terms.

$$
\left(\frac{dy}{dx}-1\right)\left(x+y\right) = 1 + \frac{dy}{dx}, \qquad \frac{dy}{dx}\left(x+y-1\right) = x+y+1
$$

Step 15. Solve for the slope and compare with the original equation.

$$
\frac{dy}{dx} = \frac{x+y+1}{x+y-1}
$$

The check succeeds, so the answer is correct. The logarithm requires that $x+y$ is not zero, so the solution lives on one side of the line where $x+y$ vanishes.

### 4.11 Problem: an equation whose two straight lines cross

Solve $\frac{dy}{dx} = \frac{x+y-3}{x-y-1}$.

### 4.12 Solution: decide the case, find the crossing point, shift the origin, solve, check

Step 1. Compute the deciding number. Here $a$ is one, $b$ is one, $p$ is one and $q$ is minus one, so the number is one times minus one minus one times one, which is minus two. It is not zero, so the two straight lines cross and the second cure applies.

Step 2. Find the crossing point by setting both the top and the bottom equal to zero.

$$
x + y - 3 = 0, \qquad x - y - 1 = 0
$$

Step 3. Add the two equations, which cancels $y$ and gives twice $x$ equal to four, so $x$ is two. Substituting back gives $y$ equal to one.

$$
h = 2, \qquad k = 1
$$

Step 4. Check the crossing point in both equations: two plus one minus three is zero, and two minus one minus one is zero. Both hold.

Step 5. Measure from the crossing point by writing each old coordinate as a new coordinate plus the shift.

$$
x = X + 2, \qquad y = Y + 1
$$

Step 6. Substitute into the top of the fraction and watch the numbers cancel.

$$
\left(X+2\right) + \left(Y+1\right) - 3 = X + Y
$$

Step 7. Substitute into the bottom, where the numbers also cancel.

$$
\left(X+2\right) - \left(Y+1\right) - 1 = X - Y
$$

Step 8. Write the equation in the new letters; the shifts are constants, so the differentials are unchanged.

$$
\frac{dY}{dX} = \frac{X+Y}{X-Y}
$$

Step 9. Divide top and bottom by $X$ to expose the ratio, and substitute $Y = vX$.

$$
v + X\frac{dv}{dX} = \frac{1+v}{1-v}
$$

Step 10. Subtract $v$ and simplify.

$$
X\frac{dv}{dX} = \frac{1+v-v+v^{2}}{1-v} = \frac{1+v^{2}}{1-v}
$$

Step 11. Separate the letters.

$$
\frac{1-v}{1+v^{2}}\,dv = \frac{dX}{X}
$$

Step 12. Split the left side into two standard pieces, one of which is the derivative of the arctangent.

$$
\int\frac{dv}{1+v^{2}} - \int\frac{v\,dv}{1+v^{2}} = \int\frac{dX}{X}
$$

Step 13. Integrate both sides.

$$
\arctan v - \frac{1}{2}\ln\left(1+v^{2}\right) = \ln X + c
$$

Step 14. Move the logarithmic piece to the right and combine, using that the logarithm of one plus $v$ squared is the logarithm of $X^{2}+Y^{2}$ minus twice the logarithm of $X$.

$$
\arctan v = \frac{1}{2}\ln\left(X^{2}+Y^{2}\right) + c
$$

Step 15. Replace $v$ by $Y$ divided by $X$ and then put the original letters back.

$$
\arctan\left(\frac{y-1}{x-2}\right) = \frac{1}{2}\ln\left(\left(x-2\right)^{2}+\left(y-1\right)^{2}\right) + c
$$

Step 16. Check, using the shifted letters to keep the algebra short. Write $w$ for $x-2$ and $u$ for $y-1$, and differentiate the relation with respect to $w$.

$$
\frac{wu'-u}{w^{2}+u^{2}} = \frac{w+uu'}{w^{2}+u^{2}}
$$

Step 17. Multiply by the common denominator and collect the slope terms.

$$
wu' - u = w + uu', \qquad u'\left(w-u\right) = w+u, \qquad u' = \frac{w+u}{w-u}
$$

Step 18. Translate the result back. The numerator $w+u$ is $x+y-3$ and the denominator $w-u$ is $x-y-1$, so the recovered slope is exactly the right side of the original equation. The answer is confirmed.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 What the methods promise and what they do not

Separation of variables promises that the problem reduces to two integrations. It does not promise that those integrations can be done with familiar functions. An equation such as $\frac{dy}{dx} = e^{-y^{2}}$ separates perfectly, yet the resulting integral has no formula built from powers, exponentials, logarithms and trigonometric functions. The honest response is to present the solution as a definite integral and to say that no elementary formula exists.

The homogeneous method promises that a homogeneous equation becomes separable. It does not promise that the separated integral is pleasant; the integral of one over $F(v)-v$ may be a long partial-fraction calculation, as in the harder examples. The method has still done its job, because it has converted an unfamiliar problem into two integrations.

Recognising this division of labour prevents a common kind of despair. A student who reaches a difficult integral has not made a mistake; the method merely stops where integration begins.

### 5.2 The straight-line solutions that hide in a division

Every separation step divides by something. In the homogeneous method the divisor is $F(v)-v$, and the values of $v$ that make it zero correspond to straight rays through the origin that solve the equation but are excluded from the integrated formula.

The habit that catches these is simple. Before integrating, write down the values at which the division is illegal, and at the end test each one in the original equation. If it satisfies the equation, add it to the answer as a separate case. If it does not, say that it is not a solution and nothing has been lost.

### 5.3 Beginner misconceptions, one by one

- **"Multiplying by $dx$ is fine because $dx$ is a tiny number."** The symbol $\frac{dy}{dx}$ is one derivative, not a fraction of two small numbers. The separation step is legitimate because both sides can be integrated and the chain rule justifies the change of variable, not because $dx$ may be shuffled about.
- **"Once $y = vx$ is written, $v$ is a constant."** This is the most damaging error in the whole topic. The letter $v$ stands for a function of $x$, so the derivative of $y$ is $v$ plus $x$ times the derivative of $v$. Dropping the second term turns the method into an identity.
- **"In the differential form the derivative of $y = vx$ is just $v\,dx$."** The differential is $v\,dx$ plus $x\,dv$, and the extra term carries all the information about how $v$ changes.
- **"Homogeneous means the right-hand side is zero."** That is a different use of the word, belonging to the theory of linear equations. In this topic homogeneous means the slope is unchanged when both letters are scaled, which is a statement about degree zero.
- **"I checked the degrees of the top and bottom and they were both two, so the whole fraction has degree two."** A quotient of two expressions of degree two has degree zero, because the scale factors cancel. The degree of the fraction is the difference of the degrees.
- **"The deciding number tells me nothing; I can just try both methods."** Trying the wrong method wastes time and usually produces an equation that will not separate. Computing the deciding number takes one line and settles the case.
- **"The shift $h$ and $k$ can be any convenient numbers."** They are forced. They are the coordinates of the crossing point, found by solving the two straight-line equations, and any other choice leaves at least one added number in place.
- **"After the substitution I can stop once I have an answer in $v$ or in $z$."** An answer in the wrong letters is not an answer. Every substitution must be undone and the final relation written in the original letters.
- **"Two constants appeared, so this must be a second-order problem."** One integration gives one constant. If two appear, they must be merged, or an integration has been duplicated.
- **"The absolute value in a logarithm can be dropped at once."** It can be dropped only when the sign is absorbed into the arbitrary constant, and the sign must then be accounted for. Dropping it silently narrows the answer.
- **"Checking is optional if I am confident."** Checking costs a few lines and catches sign errors, wrong powers and algebraic slips, which are the errors that actually occur. An unchecked answer in this topic is an unfinished answer.
- **"The interval of validity is a technicality."** A solution involving the logarithm of $x+y$ simply does not exist where $x+y$ is zero or negative, and a solution involving one over $1-x$ stops at $x$ equal to one. Stating the interval is part of solving the problem.

### 5.4 Where these ideas are used next

The habit of testing an expression by scaling recurs throughout the subject. The same test decides whether an equation is suitable for the substitution used here, and it reappears when equations are classified by other kinds of scaling, for instance when a power of $x$ is used as the scale factor in more advanced substitutions.

The technique of renaming the unknown to simplify an equation is the prototype of a whole family of substitutions. Each later method in the course begins by looking for a renaming that converts the equation into one already solved, and the substitution used here is the first and clearest example of that strategy.

Moving the origin is another idea that keeps returning. Recognising that a pattern becomes regular once the origin is placed at a particular point turns up in the study of conic sections, in the simplification of quadratic expressions, and in the analysis of linear systems. The shift used here is the two-dimensional version of completing the square.

### 5.5 A short checklist before submitting an answer

1. State the type of the equation and the test that established it.
2. Show the substitution explicitly, including the derivative of the substituted quantity.
3. Show the separation step and record every value excluded by a division.
4. Integrate once and add exactly one constant.
5. Undo every substitution, so that the final answer is written in the original letters.
6. Check by differentiating, and confirm any starting value.
7. State the interval on which the answer is valid.

### 5.6 A closing summary in plain words

The topic contains four ideas and they fit together in a fixed order.

The first idea is sorting. If the equation can be written with everything in $y$ on one side and everything in $x$ on the other, two integrations finish the problem, and the difficulty is entirely in the factoring.

The second idea is scaling. If the slope prescribed by the equation is unchanged when both letters are stretched by the same factor, then the slope depends only on the direction from the origin. Naming that direction as the ratio of $y$ to $x$ reduces the equation to the sorting case, and the reduction is the substitution that turns the old equation into two integrals.

The third idea is shifting. If the equation is a fraction of two straight-line expressions whose constant terms spoil the scaling, then either the lines cross, in which case the origin is moved to the crossing point and the spoiling numbers vanish, or the lines are parallel, in which case the repeated combination is named and the equation sorts itself.

The fourth idea is checking. Every answer in this topic can be tested by differentiating it, and the test is quick, decisive and independent of the route taken. An answer that survives the check is correct; an answer that fails it is wrong, whatever the route looked like.
