## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 Imagine you are walking on a hillside

Imagine you are walking on a hillside, and you carry a map printed with contour lines. Every contour line is a path along which your height above sea level never changes. If you walk along a contour, you may travel a long way, but your height reading stays exactly the same from the first step to the last.

Now suppose you take a small step that is partly eastwards and partly northwards. Your height changes for two separate reasons: the ground rises or falls as you move east, and it also rises or falls as you move north. The total change in your height is the eastward change plus the northward change. That is the whole idea of this topic, and everything that follows is that one sentence written in the shorthand that mathematicians use.

Picture the same thing in a different setting. Think of the temperature in a room. It is warmer near the radiator and cooler near the window, and it is also warmer near the ceiling than near the floor. If you move a short distance to the right and a short distance upwards, the thermometer changes for two reasons, one coming from the sideways move and one coming from the upward move. The total change is again the sum of the two contributions.

Both pictures describe the same mathematical object: a quantity that depends on two numbers at once, together with the rule for how that quantity changes when the two numbers are nudged. The hillside and the room are two costumes worn by the same idea.

### 1.2 The same idea written in symbols

We need names for the two things we are allowed to change. Let the first be the sideways position and the second be the upward position. In mathematics these are usually called the two independent variables, and they are written as the letters $x$ and $y$. A point in the plane is the pair of them, written as $(x,y)$.

The quantity we are watching, the height or the temperature, is a function of those two numbers. Its name is a letter too, and the usual choice is capital $F$. So the sentence the height is a function of the sideways position and the upward position is written as

$$
F(x,y) .
$$

A small change in the first number is written as $dx$, and a small change in the second number is written as $dy$. The letter $d$ in front of a quantity always means a small change in that quantity. This is the only meaning of $d$ in this note; it is not a multiplication sign and it is not a number.

Now come the two separate rates of change. Hold the second number fixed and change only the first: the rate at which $F$ responds is written with a curly d, like this:

$$
\frac{\partial F}{\partial x} .
$$

The curly symbol is pronounced partial, and it means the rate of change when only the named variable is allowed to move. Holding the first number fixed and changing only the second gives the other rate of change:

$$
\frac{\partial F}{\partial y} .
$$

A shorter way to write the same two objects is $F_{x}$ and $F_{y}$. The subscript names the variable that was allowed to move. So $F_{x}$ means the rate of change of $F$ when $x$ moves and $y$ stays still, and $F_{y}$ means the rate of change when $y$ moves and $x$ stays still.

With those names, the sentence from the hillside becomes an equation. The total change in the height, written $dF$, is the change caused by the sideways step plus the change caused by the upward step:

$$
dF=\frac{\partial F}{\partial x}\,dx+\frac{\partial F}{\partial y}\,dy .
$$

This is called the total differential of $F$. It is the central formula of the topic, and it is nothing more than the two contributions added together.

### 1.3 Four small examples of a total differential

Take the simplest possible function of two variables, the sum of the two positions:

$$
F(x,y)=x+y .
$$

Changing only $x$ changes $F$ at rate one, so $\frac{\partial F}{\partial x}=1$. Changing only $y$ also changes $F$ at rate one, so $\frac{\partial F}{\partial y}=1$. Therefore

$$
dF=1\cdot dx+1\cdot dy=dx+dy .
$$

Take the next simplest, one position plus twice the other:

$$
F(x,y)=x+2y .
$$

The rate with respect to $x$ is $1$, and the rate with respect to $y$ is $2$, so

$$
dF=dx+2\,dy .
$$

Take the product of the two positions. This one repays careful reading, because it is used more often than any other formula in the topic:

$$
F(x,y)=xy .
$$

If $x$ is held still then $F$ is a constant times $y$, so the rate with respect to $y$ is that constant, namely $x$. If $y$ is held still then $F$ is a constant times $x$, so the rate with respect to $x$ is $y$. Hence

$$
d(xy)=y\,dx+x\,dy .
$$

Read that equation slowly, in words: the change in a product is the first number times the change in the second, plus the second number times the change in the first. It is the product rule of ordinary calculus, seen from a new angle.

One more example, because it is the pattern behind the hillside. Take

$$
F(x,y)=x^{2}+y^{2} .
$$

The rate with respect to $x$ is $2x$, and the rate with respect to $y$ is $2y$, so

$$
d\left(x^{2}+y^{2}\right)=2x\,dx+2y\,dy .
$$

The number $x^{2}+y^{2}$ is the square of the distance from the origin, so this formula says how the squared distance changes when the point moves a little.

### 1.4 The kind of equation this topic studies

A first order differential equation can be written in a very symmetric way. Instead of writing the slope as a formula, we write a balance between two coefficients, one attached to $dx$ and one attached to $dy$:

$$
M(x,y)\,dx+N(x,y)\,dy=0 .
$$

Here $M$ is the coefficient of $dx$, a function of the two positions, and $N$ is the coefficient of $dy$, also a function of the two positions. In the hillside language, $M$ is the eastward slope and $N$ is the northward slope, and the equation says that the total change in height is zero. Zero total change means the walker stays on a contour line.

That is the definition we need.

> **Definition (Exact equation).** The equation $M\,dx+N\,dy=0$ is called exact when there exists a function $F$ of the two variables such that

$$
\frac{\partial F}{\partial x}=M \qquad \text{and} \qquad \frac{\partial F}{\partial y}=N .
$$

When such a function exists it is called a potential function, and the equation can be written as the single statement $dF=0$.

So an exact equation is one whose left-hand side is already the total differential of some height function. The two coefficients are not arbitrary; they are the two slopes of one and the same surface. That is a strong statement, and most pairs of coefficients fail it.

### 1.5 What the answer looks like

If the equation is exact, then it says that the height does not change. A walk on which the height never changes is a walk along a contour. Therefore the solutions of the equation are exactly the contour lines of the height function, and a contour line is described by saying the height equals some fixed number:

$$
F(x,y)=C .
$$

The letter $C$ stands for a constant, the height of the contour you are on. Different values of $C$ give different contours, and between them they make up the whole family of solutions. A first order equation is allowed exactly one arbitrary constant, and here that constant is the height.

This is why answers in this topic are usually written as an equation in $x$ and $y$ rather than as a formula for $y$. The relation $F(x,y)=C$ is the honest description of a contour, and trying to solve it for $y$ often makes things worse rather than better. For example, the contour of a circle is best left as $x^{2}+y^{2}=C$.

### 1.6 The test that decides everything

How can you tell, without hunting for the height function, whether the coefficients $M$ and $N$ really do come from one surface? There is a very short test.

Compute the rate of change of $M$ with respect to $y$, written $M_{y}$, and the rate of change of $N$ with respect to $x$, written $N_{x}$. If the two are equal, the equation is exact. If they are not equal, the equation is not exact.

In symbols, the test is

$$
M_{y}=N_{x} .
$$

Notice carefully which way round it goes. The coefficient of $dx$ is differentiated with respect to $y$, and the coefficient of $dy$ is differentiated with respect to $x$. The variables cross over. This crossing over is the single most commonly reversed detail in the whole topic, so it is worth repeating in words: differentiate each coefficient with respect to the variable it is not multiplied by.

A tiny example makes the test concrete. Take

$$
2y\,dx+3x\,dy=0 .
$$

Here $M=2y$ and $N=3x$. Differentiating $M$ with respect to $y$ gives $2$, and differentiating $N$ with respect to $x$ gives $3$. Since $2$ is not $3$, this equation is not exact. But if the equation had been

$$
2y\,dx+2x\,dy=0 ,
$$

then $M_{y}=2$ and $N_{x}=2$, and the test passes. Indeed $2y\,dx+2x\,dy$ is twice $d(xy)$, so it is the total differential of $2xy$.

### 1.7 When the test fails: integrating factors

Most equations fail the test. The next idea is to multiply the whole equation by a helper function and try again, in the hope that the multiplied equation passes.

> **Definition (Integrating factor).** A function $\mu(x,y)$ is an integrating factor for $M\,dx+N\,dy=0$ if the new equation

$$
\mu M\,dx+\mu N\,dy=0
$$

is exact. The Greek letter $\mu$ is pronounced mew.

Multiplying an equation by a helper changes how it looks but not what it means, as long as the helper is finite and not zero. If $\mu$ is not zero at a point, then $\mu$ times a quantity is zero exactly when the quantity itself is zero. So the solution curves are unchanged. The places where $\mu$ is zero or infinite must be examined separately, because there the multiplication can hide a solution or invent one.

The helper is found by one of three routes, and the next section states them. For now, one example shows how cheap the idea is. Take

$$
2y\,dx+x\,dy=0 .
$$

The test gives $M_{y}=2$ and $N_{x}=1$, so the equation is not exact. Multiply everything by $x$. The equation becomes

$$
2xy\,dx+x^{2}\,dy=0 .
$$

The test now gives $M_{y}=2x$ and $N_{x}=2x$, which agree, so the multiplied equation is exact, and the helper $x$ has done its job.

### 1.8 Four combinations worth knowing by heart

Some combinations of $dx$ and $dy$ appear so often that their differentials should be recognised instantly, the way a reader recognises a whole word rather than spelling out the letters.

The first is $y\,dx+x\,dy$, which is the change in the product:

$$
d(xy)=y\,dx+x\,dy .
$$

The second is $x\,dy-y\,dx$, which is the change in the ratio of the two numbers after a division by the square of the first. In symbols,

$$
d\left(\frac{y}{x}\right)=\frac{x\,dy-y\,dx}{x^{2}} .
$$

The third is the same combination divided by the sum of the squares, which measures the change in the angle of the point from the first axis:

$$
d\left(\arctan\frac{y}{x}\right)=\frac{x\,dy-y\,dx}{x^{2}+y^{2}} .
$$

The fourth is the product combination divided by the product itself, which measures the change in the logarithm of the product:

$$
d\left(\ln(xy)\right)=\frac{y\,dx+x\,dy}{xy} .
$$

Each of these four is an exact differential waiting to be used. If an equation contains one of the four combinations on the left, the corresponding division turns the equation into something that can be integrated at once. That is the practical value of the list, and Section 2 extends it into a short table.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The exactness test, stated properly

> **Theorem (Test for an exact equation).** Suppose the four functions $M$, $N$, the partial derivative of $M$ with respect to $y$, and the partial derivative of $N$ with respect to $x$ are all continuous on a rectangle of the plane. Then the equation $M\,dx+N\,dy=0$ is exact on that rectangle exactly when

$$
M_{y}=N_{x}
$$

at every point of the rectangle.

The phrase exactly when means two things at once, and both are useful. If the equation is exact then the two partial derivatives must agree, so a failure of the test proves that no potential exists. And if the two partial derivatives agree then a potential does exist, so passing the test is a licence to go looking for it.

The words in a rectangle are not decoration. They say the region has no holes in it, which is what allows the potential to be built everywhere inside. Almost every question in this course lives on a rectangle or on the whole plane, so the subtlety rarely bites, but it is the reason the theorem is not stated for completely arbitrary regions.

### 2.2 Why the test must hold

> **Lemma (The two partial derivatives must agree).** If a potential function $F$ exists with $F_{x}=M$ and $F_{y}=N$, then $M_{y}=N_{x}$.

Here is the reason in plain words. Starting from $F$, there are two ways to compute the mixed rate of change: differentiate first with respect to $x$ and then with respect to $y$, or the other way round. For the kind of smooth functions met in this course, the two orders give the same answer. So the two mixed rates are equal.

But the two mixed rates can be read in terms of $M$ and $N$. Differentiating $F_{x}=M$ with respect to $y$ gives $M_{y}$. Differentiating $F_{y}=N$ with respect to $x$ gives $N_{x}$. Since the two mixed rates are equal, so are $M_{y}$ and $N_{x}$.

This is the necessity half of the test, and Section 3.1 writes it out with all the symbols in place. It says that the equality is a footprint left behind by the potential. If no footprint is visible, no potential can be there.

### 2.3 Why the test is enough

> **Theorem (The test is sufficient).** If $M_{y}=N_{x}$ throughout a rectangle, then a potential function exists, and it can be written down as an integral.

The proof is a construction rather than an argument, and the construction is short. Choose any starting point $(x_{0},y_{0})$ inside the rectangle. Walk horizontally from that point to $(x,y)$, adding up the coefficient $M$ along the way. Then walk vertically from $(x_{0},y_{0})$ to $(x_{0},y)$, adding up the coefficient $N$ along the way. The sum of the two accumulations is the potential:

$$
F(x,y)=\int_{x_{0}}^{x}M(t,y)\,dt+\int_{y_{0}}^{y}N(x_{0},s)\,ds .
$$

The letters $t$ and $s$ are dummy names for the running variable inside an integral; they are used so as not to clash with the endpoint names $x$ and $y$. Differentiating this expression with respect to $x$ recovers $M$, and differentiating it with respect to $y$ recovers $N$, provided $M_{y}=N_{x}$. Section 3.2 carries out both differentiations.

The important consequence for problem solving is that the potential always exists when the test passes, so a student who passes the test and then fails to find the potential has made an algebraic mistake, not a conceptual one.

### 2.4 The two routes to an integrating factor of one variable

The three routes to an integrating factor are stated here and proved in Section 3. The first two are called the classical tests.

> **Theorem (Helper depending on the first variable only).** If the fraction

$$
\frac{M_{y}-N_{x}}{N}
$$

simplifies to an expression containing no $y$, call it $f(x)$, then

$$
\mu=\exp\left(\int f(x)\,dx\right)
$$

is an integrating factor, provided $N$ is not zero on the region.

> **Theorem (Helper depending on the second variable only).** If the fraction

$$
\frac{N_{x}-M_{y}}{M}
$$

simplifies to an expression containing no $x$, call it $g(y)$, then

$$
\mu=\exp\left(\int g(y)\,dy\right)
$$

is an integrating factor, provided $M$ is not zero on the region.

The symbol $\exp$ means the exponential function, the one whose value at zero is one. The instruction inside the theorem is: integrate the simplified fraction, then put the result in the exponent of $e$. So if the fraction simplifies to $1/x$, the integral is $\ln x$ and the helper is $e^{\ln x}$, which is just $x$. That is exactly what happened in the small example of Section 1.7.

Read the two fractions side by side. The top line is the same difference, but with the order reversed and the sign changed. The bottom line is the coefficient that the other one was paired with. The first fraction is divided by $N$, the second by $M$. Both facts follow from one calculation, which is done in Section 3.3, and deriving them once is far safer than memorising them.

One warning deserves a separate sentence. These tests are conditions that work when they are met; they are not conditions that must be met. If both fractions contain both variables, the conclusion is only that no helper of either simple shape exists. Some other helper may still exist, and the third route may find it.

### 2.5 Homogeneous equations and the third route

> **Definition (Homogeneous pair).** The coefficients $M$ and $N$ are called homogeneous of the same degree if multiplying both $x$ and $y$ by the same positive number $t$ multiplies each coefficient by the same power of $t$.

For example, $x^{2}+xy$ and $3y^{2}$ are both homogeneous of degree two, because replacing $x$ by $tx$ and $y$ by $ty$ multiplies the first by $t^{2}$ and the second by $t^{2}$. On the other hand $x^{2}+xy$ and $3y$ are not of the same degree, and the next theorem does not apply to the pair.

> **Theorem (Helper for a homogeneous pair).** If $M$ and $N$ are homogeneous of the same degree and the combination $Mx+Ny$ is not identically zero, then

$$
\mu=\frac{1}{Mx+Ny}
$$

is an integrating factor for $M\,dx+N\,dy=0$.

This route is the cheapest of the three because it needs no integration at all. The denominator is formed by multiplying each coefficient by the variable that goes with it and adding: $M$ goes with $x$, $N$ goes with $y$. Then the whole thing is turned upside down. Section 3.6 verifies that the exactness test passes after this multiplication.

### 2.6 The table of important differentials

The table records the combinations that recur, together with the helper that turns each into a clean differential. The middle columns are the ones to learn; the last column shows why the entry is true, by displaying the identity that justifies it.

| Combination | Helper | Result | Identity |
|---|---|---|---|
| $y\,dx+x\,dy$ | $1$ | $xy$ | $d(xy)=y\,dx+x\,dy$ |
| $y\,dx+x\,dy$ | $\frac{1}{xy}$ | $\ln(xy)$ | $d\left(\ln(xy)\right)=\frac{y\,dx+x\,dy}{xy}$ |
| $x\,dy-y\,dx$ | $\frac{1}{x^{2}}$ | $\frac{y}{x}$ | $d\left(\frac{y}{x}\right)=\frac{x\,dy-y\,dx}{x^{2}}$ |
| $y\,dx-x\,dy$ | $\frac{1}{y^{2}}$ | $\frac{x}{y}$ | $d\left(\frac{x}{y}\right)=\frac{y\,dx-x\,dy}{y^{2}}$ |
| $x\,dy-y\,dx$ | $\frac{1}{x^{2}+y^{2}}$ | $\arctan\left(\frac{y}{x}\right)$ | $d\left(\arctan\frac{y}{x}\right)=\frac{x\,dy-y\,dx}{x^{2}+y^{2}}$ |
| $x\,dy-y\,dx$ | $\frac{1}{xy}$ | $\ln\left(\frac{y}{x}\right)$ | $d\left(\ln\frac{y}{x}\right)=\frac{x\,dy-y\,dx}{xy}$ |
| $x\,dx+y\,dy$ | $1$ | $\frac{1}{2}\left(x^{2}+y^{2}\right)$ | $d\left(\frac{x^{2}+y^{2}}{2}\right)=x\,dx+y\,dy$ |
| $x\,dx+y\,dy$ | $\frac{1}{x^{2}+y^{2}}$ | $\frac{1}{2}\ln\left(x^{2}+y^{2}\right)$ | $d\left(\ln\sqrt{x^{2}+y^{2}}\right)=\frac{x\,dx+y\,dy}{x^{2}+y^{2}}$ |
| $y\,dx+x\,dy$ | $-\frac{1}{x^{2}y^{2}}$ | $\frac{1}{xy}$ | $d\left(\frac{1}{xy}\right)=-\frac{y\,dx+x\,dy}{x^{2}y^{2}}$ |

Three readings of the table are worth practising. First, the top row says that $y\,dx+x\,dy$ is already exact, with potential $xy$; no helper is needed. Second, the third row says that dividing the antisymmetric combination by the square of the first variable produces the differential of the ratio $y$ over $x$; that single entry solves a surprising number of questions. Third, the fifth row says that dividing the same antisymmetric combination by the sum of the squares produces the differential of an angle, which is why rotations and circles appear in this subject at all.

The table must be used with its conditions. Every logarithm needs a positive argument, so the rows producing logarithms are used on the region where both variables are positive. The arctangent row needs the first variable to be non-zero, because of the division inside the arctangent.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 The necessity proof, written out

Suppose the equation is exact, so that a potential $F$ exists with

$$
F_{x}=M \qquad \text{and} \qquad F_{y}=N .
$$

Differentiate the first identity with respect to $y$. The left side becomes the mixed derivative of $F$, taken first in $x$ and then in $y$, and the right side becomes $M_{y}$:

$$
M_{y}=\frac{\partial^{2}F}{\partial y\,\partial x} .
$$

Differentiate the second identity with respect to $x$. The left side becomes the mixed derivative of $F$ taken in the other order, and the right side becomes $N_{x}$:

$$
N_{x}=\frac{\partial^{2}F}{\partial x\,\partial y} .
$$

For a smooth function the two mixed derivatives are equal, as the lemma of Section 2.2 states. Therefore the two right-hand sides are equal:

$$
M_{y}=N_{x} .
$$

That is the whole proof, and it uses only one idea: the order of two differentiations does not matter.

### 3.2 The sufficiency proof, written out

Suppose instead that $M_{y}=N_{x}$ throughout a rectangle, and build the candidate

$$
F(x,y)=\int_{x_{0}}^{x}M(t,y)\,dt+\int_{y_{0}}^{y}N(x_{0},s)\,ds .
$$

Step 1. Differentiate with respect to $x$. The second integral has no $x$ in it at all, so it contributes nothing. The first integral is an accumulation up to the moving endpoint $x$, and the rate at which such an accumulation grows is the value of the integrand at that endpoint. Hence

$$
F_{x}=M(x,y) .
$$

Step 2. Differentiate with respect to $y$. Now both integrals matter. The second produces $N(x_{0},y)$, and the first must be differentiated under the integral sign, which gives the integral of $M_{y}$:

$$
F_{y}=\int_{x_{0}}^{x}M_{y}(t,y)\,dt+N(x_{0},y) .
$$

Step 3. Use the hypothesis to replace $M_{y}$ by $N_{x}$.

$$
F_{y}=\int_{x_{0}}^{x}N_{x}(t,y)\,dt+N(x_{0},y)
$$

Step 4. Recognise that the integral of a derivative returns the function. The integral of $N_{x}$ with respect to the first argument, from $x_{0}$ to $x$, is $N(x,y)-N(x_{0},y)$:

$$
F_{y}=N(x,y)-N(x_{0},y)+N(x_{0},y) .
$$

Step 5. Cancel the last two terms.

$$
F_{y}=N(x,y)
$$

Steps 1 and 5 give both of the required identities, so the candidate really is a potential. This proof is a recipe as well as an argument: it shows that the potential can always be assembled from two ordinary integrals along straight lines.

### 3.3 Where the two classical tests come from

An integrating factor $\mu$ must make the multiplied equation exact, so the test must hold for the multiplied coefficients:

$$
\frac{\partial}{\partial y}\left(\mu M\right)=\frac{\partial}{\partial x}\left(\mu N\right) .
$$

Expand both sides with the product rule, remembering that each side differentiates a product of two functions:

$$
\mu_{y}M+\mu M_{y}=\mu_{x}N+\mu N_{x} .
$$

Now suppose the helper depends on $x$ only. Then it does not change when $y$ moves, so $\mu_{y}=0$, and its $x$-derivative is the ordinary derivative $\mu'$. The equation collapses to

$$
\mu M_{y}=\mu' N+\mu N_{x} .
$$

Move the $\mu$ terms together:

$$
\mu\left(M_{y}-N_{x}\right)=\mu' N .
$$

Divide by $\mu N$:

$$
\frac{\mu'}{\mu}=\frac{M_{y}-N_{x}}{N} .
$$

The left side depends on $x$ only, because the helper depends on $x$ only. So the right side must also depend on $x$ only, which is exactly the condition in the first theorem. When that condition holds, the equation for $\mu$ is a simple separable one, and integrating both sides gives $\ln\mu$ equal to the integral of the fraction, hence the helper is the exponential of that integral.

The second test comes from the same expansion with the assumption reversed. Suppose the helper depends on $y$ only, so $\mu_{x}=0$ and the $y$-derivative is $\mu'$. The expanded equation reads

$$
\mu' M+\mu M_{y}=\mu N_{x} ,
$$

which rearranges to

$$
\mu' M=\mu\left(N_{x}-M_{y}\right) ,
$$

and division by $\mu M$ gives

$$
\frac{\mu'}{\mu}=\frac{N_{x}-M_{y}}{M} .
$$

Again the left side is a function of one variable, so the right side must be too, and the helper is the exponential of the integral of that fraction.

The two derivations differ by exactly one sign, and that sign is the reason the second fraction is written with $N_{x}$ first. Anyone who derives the fractions instead of memorising them will never reverse them.

### 3.4 The four-step method for an exact equation

This is the routine that solves every exact equation. It is called the two-step method because the two integrations are the heart of it.

Step 1. Write the equation as $M\,dx+N\,dy=0$, identify $M$ and $N$, and check $M_{y}=N_{x}$.

Step 2. Integrate $M$ with respect to $x$, treating $y$ as a constant. Instead of adding a plain constant of integration, add an unknown function of $y$, written $\varphi(y)$. The reason is that any function of $y$ alone has zero derivative with respect to $x$, so it would have been invisible during the integration. We must leave room for it.

Step 3. Differentiate the result with respect to $y$ and set it equal to $N$. Everything that depends on $x$ should cancel, leaving an equation for $\varphi'(y)$, the derivative of the unknown function. Solve it and integrate to find $\varphi(y)$.

Step 4. Put $\varphi(y)$ back, and write the answer as $F(x,y)=C$. No extra constant is needed at this stage, because the final answer already carries the arbitrary constant $C$.

The check at the end is to differentiate the claimed $F$ with respect to each variable in turn and confirm that the two answers are $M$ and $N$. Two lines of work, and they catch almost every slip.

### 3.5 The method for an integrating factor

Step 1. Test exactness. If the test passes, no helper is needed.

Step 2. Compute $M_{y}-N_{x}$ and divide by $N$. Simplify. If no $y$ survives, use the first test and exponentiate the integral with respect to $x$.

Step 3. Otherwise compute $N_{x}-M_{y}$ and divide by $M$. Simplify. If no $x$ survives, use the second test and exponentiate the integral with respect to $y$.

Step 4. Otherwise check whether $M$ and $N$ are homogeneous of the same degree. If they are, form $Mx+Ny$ and turn it upside down.

Step 5. Otherwise look for one of the combinations in the table, divide the whole equation by the suggested quantity, and integrate the result.

Step 6. In every case, multiply out, verify that the new equation passes the exactness test, then solve it by the four-step method.

The order matters. The first three steps are divisions and one multiplication, and they are cheap. The last two need judgement, and judgement is what runs out first in an examination.

### 3.6 Checking the homogeneous helper

Take $M$ and $N$ homogeneous of the same degree, and write $D$ for the combination $Mx+Ny$. The claimed helper is $\mu=1/D$. To verify the claim, the test must be applied to $\mu M$ and $\mu N$.

The two cross partial derivatives are computed with the quotient rule, since $\mu$ is a reciprocal. The result of the computation is that the difference between them is a fraction whose denominator is $D^{2}$ and whose numerator is

$$
x\left(N M_{x}-M N_{x}\right)+y\left(N M_{y}-M N_{y}\right) .
$$

Now comes the fact that makes the whole thing work. For a homogeneous function of degree $n$, Euler's relation says that multiplying each partial derivative by the matching variable and adding gives $n$ times the function. Applied to $M$ and to $N$, and remembering that the two degrees are equal, the two relations read

$$
xN M_{x}+yN M_{y}=nMN, \qquad xM N_{x}+yM N_{y}=nMN .
$$

The right-hand sides are identical, so subtracting one relation from the other gives zero, and the numerator above is exactly that difference. The numerator vanishes, the two cross partials are equal, and the helper is genuine.

### 3.7 Checking the table entries

Each row of the table is checked by differentiating the claimed result. Three checks show the pattern.

For the product, differentiating $xy$ with respect to $x$ gives $y$ and with respect to $y$ gives $x$, so the differential is $y\,dx+x\,dy$. The first row is confirmed.

For the ratio, differentiating $y$ over $x$ with respect to $x$ gives minus $y$ over $x^{2}$, and with respect to $y$ gives $1$ over $x$. Multiplying the first by $dx$ and the second by $dy$ and putting them over the common denominator $x^{2}$ gives

$$
\frac{-y\,dx+x\,dy}{x^{2}} ,
$$

which is the third row.

For the angle, the derivative of the arctangent of $y$ over $x$ with respect to $x$ is minus $y$ over the sum of the squares, and with respect to $y$ it is $x$ over the sum of the squares. Combining the two contributions gives

$$
\frac{-y\,dx+x\,dy}{x^{2}+y^{2}} ,
$$

which is the fifth row.

The remaining rows are checked in the same way, and doing so once by hand fixes them in memory better than reading them does.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a first exact equation with small numbers

Show that

$$
\left(2x+4y\right)dx+\left(4x+6y\right)dy=0
$$

is exact, and solve it.

### 4.2 Solution: test, integrate, match

Step 1. Identify the two coefficients.

$$
M=2x+4y, \qquad N=4x+6y
$$

Step 2. Compute the two cross partials. When differentiating $M$ with respect to $y$, the term $2x$ is a constant and disappears, leaving $4$. When differentiating $N$ with respect to $x$, the term $6y$ is a constant and disappears, leaving $4$.

$$
M_{y}=4, \qquad N_{x}=4
$$

Step 3. The two are equal, so the equation is exact.

Step 4. Integrate $M$ with respect to $x$, holding $y$ fixed, and add an unknown function of $y$.

$$
F(x,y)=\int\left(2x+4y\right)dx=x^{2}+4xy+\varphi(y)
$$

Step 5. Differentiate with respect to $y$ and set the result equal to $N$.

$$
4x+\varphi'(y)=4x+6y
$$

Step 6. The $x$-terms cancel, which is the expected sign that the work is going well. What remains involves $y$ only.

$$
\varphi'(y)=6y
$$

Step 7. Integrate to find the unknown function.

$$
\varphi(y)=3y^{2}
$$

Step 8. Write the potential and the answer.

$$
F(x,y)=x^{2}+4xy+3y^{2}, \qquad x^{2}+4xy+3y^{2}=C
$$

Step 9. Check by differentiating back. The $x$-derivative of the answer is $2x+4y$, which is $M$, and the $y$-derivative is $4x+6y$, which is $N$. Both match, so the answer is right.

### 4.3 Problem: a second exact equation

Solve

$$
\left(2x+y\right)dx+\left(x+2y\right)dy=0 .
$$

### 4.4 Solution: the same routine

Step 1. Identify the coefficients and test.

$$
M=2x+y, \qquad N=x+2y, \qquad M_{y}=1, \qquad N_{x}=1
$$

Step 2. The test passes, so the equation is exact.

Step 3. Integrate $M$ with respect to $x$.

$$
F(x,y)=x^{2}+xy+\varphi(y)
$$

Step 4. Differentiate with respect to $y$ and match to $N$.

$$
x+\varphi'(y)=x+2y
$$

Step 5. Cancel the $x$-terms.

$$
\varphi'(y)=2y, \qquad \varphi(y)=y^{2}
$$

Step 6. Write the answer and check.

$$
x^{2}+xy+y^{2}=C, \qquad F_{x}=2x+y, \qquad F_{y}=x+2y
$$

Both partial derivatives match the original coefficients, so the answer is confirmed.

### 4.5 Problem: an exact equation with a product term

Solve

$$
\left(2xy+3\right)dx+\left(x^{2}+1\right)dy=0 .
$$

### 4.6 Solution: differentiate carefully with respect to each variable

Step 1. Identify the coefficients.

$$
M=2xy+3, \qquad N=x^{2}+1
$$

Step 2. Differentiate $M$ with respect to $y$. The constant $3$ disappears and the term $2xy$ gives $2x$. Differentiate $N$ with respect to $x$; the constant $1$ disappears and the term $x^{2}$ gives $2x$.

$$
M_{y}=2x, \qquad N_{x}=2x
$$

Step 3. The test passes.

Step 4. Integrate $M$ with respect to $x$.

$$
F(x,y)=\int\left(2xy+3\right)dx=x^{2}y+3x+\varphi(y)
$$

Step 5. Differentiate with respect to $y$ and match.

$$
x^{2}+\varphi'(y)=x^{2}+1
$$

Step 6. Cancel and integrate.

$$
\varphi'(y)=1, \qquad \varphi(y)=y
$$

Step 7. Write the answer and check.

$$
x^{2}y+3x+y=C, \qquad F_{x}=2xy+3, \qquad F_{y}=x^{2}+1
$$

Both match, so the answer stands.

### 4.7 Problem: a first integrating factor

Solve

$$
2y\,dx+x\,dy=0 .
$$

### 4.8 Solution: find the helper, then solve

Step 1. Test the equation as it stands.

$$
M=2y, \qquad N=x, \qquad M_{y}=2, \qquad N_{x}=1
$$

Since $2$ is not $1$, the equation is not exact.

Step 2. Form the fraction for the first test and simplify.

$$
\frac{M_{y}-N_{x}}{N}=\frac{2-1}{x}=\frac{1}{x}
$$

Step 3. The result contains no $y$, so a helper depending on $x$ alone exists. Integrate and exponentiate.

$$
\mu=\exp\left(\int\frac{1}{x}\,dx\right)=e^{\ln x}=x
$$

Step 4. Multiply the whole equation by $x$.

$$
2xy\,dx+x^{2}\,dy=0
$$

Step 5. Test the new equation.

$$
\frac{\partial}{\partial y}\left(2xy\right)=2x, \qquad \frac{\partial}{\partial x}\left(x^{2}\right)=2x
$$

The test passes, so the helper has worked.

Step 6. Integrate the new coefficient of $dx$ with respect to $x$.

$$
F(x,y)=\int 2xy\,dx=x^{2}y+\varphi(y)
$$

Step 7. Differentiate with respect to $y$ and match to the new coefficient of $dy$.

$$
x^{2}+\varphi'(y)=x^{2}, \qquad \varphi'(y)=0
$$

Step 8. A zero derivative means the unknown function is a constant, and the constant is absorbed into the answer.

$$
x^{2}y=C
$$

Step 9. Check. The $x$-derivative of $x^{2}y$ is $2xy$ and the $y$-derivative is $x^{2}$, which are the multiplied coefficients, so the potential is correct.

Step 10. Cross-check by separation. Dividing the original equation by $xy$ gives $2\,dx/x+dy/y=0$, whose integral is $2\ln x+\ln y$ equal to a constant, that is $x^{2}y$ equal to a constant. The two methods agree.

### 4.9 Problem: the classic ratio equation

Solve

$$
y\,dx-x\,dy=0 .
$$

### 4.10 Solution: divide by the square of the first variable

Step 1. Test the equation.

$$
M=y, \qquad N=-x, \qquad M_{y}=1, \qquad N_{x}=-1
$$

The equation is not exact.

Step 2. Form the fraction for the first test.

$$
\frac{M_{y}-N_{x}}{N}=\frac{1-\left(-1\right)}{-x}=-\frac{2}{x}
$$

Step 3. The result contains no $y$, so the helper depends on $x$ alone. Integrate and exponentiate.

$$
\mu=\exp\left(\int-\frac{2}{x}\,dx\right)=e^{-2\ln x}=\frac{1}{x^{2}}
$$

Step 4. Multiply through by the helper.

$$
\frac{y}{x^{2}}\,dx-\frac{1}{x}\,dy=0
$$

Step 5. Test the new equation.

$$
\frac{\partial}{\partial y}\left(\frac{y}{x^{2}}\right)=\frac{1}{x^{2}}, \qquad \frac{\partial}{\partial x}\left(-\frac{1}{x}\right)=\frac{1}{x^{2}}
$$

The test passes.

Step 6. Recognise the result instead of integrating from scratch. The table says that the differential of the ratio $y$ over $x$ is

$$
d\left(\frac{y}{x}\right)=\frac{x\,dy-y\,dx}{x^{2}}=\frac{dy}{x}-\frac{y\,dx}{x^{2}} .
$$

Our combination is the negative of that, so

$$
\frac{y}{x^{2}}\,dx-\frac{1}{x}\,dy=-d\left(\frac{y}{x}\right) .
$$

Step 7. Integrate once.

$$
-\frac{y}{x}=C, \qquad \frac{y}{x}=C', \qquad y=C'x .
$$

The minus sign is absorbed into the arbitrary constant, so the family of solutions is unchanged. It is a family of straight lines through the origin.

Step 8. Check. With $y=C'x$ the derivative is $C'$, and substituting into the original form gives $C'x\,dx-x\cdot C'\,dx=0$, which is satisfied for every $x$. The answer is confirmed.

### 4.11 Problem: the product differential

Solve

$$
y\,dx+x\,dy=0 .
$$

### 4.12 Solution: no helper needed at all

Step 1. Test the equation.

$$
M=y, \qquad N=x, \qquad M_{y}=1, \qquad N_{x}=1
$$

The test passes, so the equation is already exact.

Step 2. Recognise the combination. The whole left-hand side is the differential of the product, by the first row of the table.

$$
y\,dx+x\,dy=d(xy)
$$

Step 3. Integrate once.

$$
xy=C
$$

Step 4. See what a different helper does. Multiplying by $1$ over $xy$ gives

$$
\frac{dx}{x}+\frac{dy}{y}=0 ,
$$

whose integral is $\ln x+\ln y$ equal to a constant, that is $\ln(xy)$ equal to a constant, which is the same family $xy=C$. The two helpers produce two different potentials but the same curves, and this is the standard illustration that helpers are never unique.

### 4.13 Problem: an exact equation with a starting condition

Solve $\left(2x+y\right)dx+\left(x+2y\right)dy=0$ given that $y=3$ when $x=0$.

### 4.14 Solution: general answer first, then the constant

Step 1. The general solution was found in Section 4.4 and is

$$
x^{2}+xy+y^{2}=C .
$$

Step 2. Substitute the given point. At $x=0$ and $y=3$ the left side is $0+0+9$, which is $9$.

$$
C=9
$$

Step 3. State the particular answer.

$$
x^{2}+xy+y^{2}=9
$$

Step 4. Check. The partial derivatives of the left side are $2x+y$ and $x+2y$, matching the coefficients, and the point with $x=0$ and $y=3$ does satisfy $0+0+9=9$. The answer is confirmed.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Beginner misconceptions

The list below collects the mistakes that beginners make most often, together with the correction. Reading it before an examination is worth more than re-reading the worked examples.

- Misconception: the letters $dx$ and $dy$ are numbers that can be moved about freely. Correction: they are small changes, and the algebra of the topic is justified by the chain rule and by integration, not by treating them as ordinary numbers. The formula for the total differential is a definition, not a manipulation.
- Misconception: the test is $M_{x}=N_{y}$. Correction: the variables cross over. The coefficient of $dx$ is differentiated with respect to $y$, and the coefficient of $dy$ with respect to $x$. Writing the test the wrong way round makes almost every exact equation look non-exact.
- Misconception: if the test passes, the answer is the test. Correction: passing the test only licenses the search for a potential. The answer is $F(x,y)=C$, and the marks are mostly in the integration.
- Misconception: the constant of integration after integrating $M$ is a number. Correction: it is a function of $y$, because any function of $y$ alone has zero derivative with respect to $x$ and would have been lost. If a number is written instead, the next step usually fails.
- Misconception: a second constant must be added at the end. Correction: one constant is enough, and a first order equation is entitled to exactly one. The unknown function contributes no constant because the final constant absorbs it.
- Misconception: if both fractions contain both variables, no integrating factor exists. Correction: only two special shapes have been ruled out. The homogeneous route or the table may still succeed.
- Misconception: an integrating factor is unique. Correction: multiplying a valid helper by a non-zero function of the potential gives another valid helper. Different correct answers look different and produce different potentials for the same curves.
- Misconception: multiplying by a helper is always harmless. Correction: it is harmless where the helper is finite and non-zero. Where the helper vanishes or blows up, solutions can be gained or lost, and the excluded points should be mentioned.
- Misconception: the answer must be solved for $y$. Correction: a contour is a perfectly good answer. Most contours cannot be written as a formula for $y$, and trying to force one wastes time.
- Misconception: the equation must be rearranged into slope form first. Correction: the differential form is the natural setting. Converting to slope form is useful only when the equation is linear in one variable.

### 5.2 Where the method stops

The method finds a potential only when one exists. Most forms are not exact, and the three routes do not cover every non-exact form either. When none of the routes applies, the equation may still be solvable, but by a different technique such as recognising a linear equation in disguise or separating variables after a substitution. The exactness method is a powerful special case, not a universal method.

There is also a limit to how far the answer can be simplified. An exact equation hands over an implicit relation, and converting it to an explicit formula is possible only in special cases, such as when the relation is linear or quadratic in $y$. The implicit relation is the answer, and it should be presented as an equation with the constant isolated on one side or absorbed into the right-hand side.

A third limit is the shape of the region. On a region with a hole in it, the test can pass while no single-valued potential exists. The standard example is the angle form on the plane with the origin removed, whose local potentials are arctangents and whose value changes by a full turn when you walk round the hole. The course avoids such regions, but the caveat explains why the theorem is stated for a rectangle.

### 5.3 A short revision list

1. Write the total differential of a function of two variables and explain each symbol in words.
2. State the test in symbols and in words, including which variable is held fixed in each differentiation.
3. Prove that the test must hold, using the equality of the two mixed derivatives.
4. Describe the construction of the potential as two accumulations along straight lines.
5. Carry out the four-step method on an exact equation without referring to notes.
6. Derive the fraction for the helper depending on $x$, and the fraction for the helper depending on $y$.
7. Form the homogeneous helper from $Mx+Ny$ and say when the theorem applies.
8. Reproduce the table of standard differentials, including the four combinations for the product, the ratio, the angle and the logarithm.
9. Check every claimed potential by differentiating it back to the two coefficients.
10. State the conditions attached to each helper, especially the excluded points.

### 5.4 A closing summary in words

An exact equation is a contour map in disguise. The two coefficients are the two slopes of an unknown height function, and the equation says that the height does not change, so its solutions are the contour lines. The test for exactness compares the two cross partials, because a genuine height function has mixed derivatives that do not depend on the order of differentiation; and the test is enough as well as necessary, because a height function can always be built by accumulating the first coefficient sideways and the second coefficient upwards.

When the test fails, the equation is multiplied by a helper chosen so that the test then passes. The helper comes from one of three cheap routes: the fraction with the cross-partial difference over the second coefficient, which works when the result involves the first variable only; the fraction with the reversed difference over the first coefficient, which works when the result involves the second variable only; and the reciprocal of $Mx+Ny$, which works when the two coefficients are homogeneous of the same degree. A short table of standard differentials covers the remaining cases, in which the equation contains a recognised combination and only needs a division.

The whole subject therefore reduces to four habits: test before searching, integrate once and remember the unknown function of $y$, check by differentiating back, and state the constant explicitly. A student who does those four things in that order will solve every exact equation put in front of them.
