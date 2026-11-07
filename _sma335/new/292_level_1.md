## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A staircase with uneven steps

Imagine climbing a staircase whose steps are all different heights. The first step is two centimetres high, the second is six, the third is ten, the fourth is fourteen, and so on, each step taller than the one before. Counting how far you have climbed is awkward, because height and step number are no longer the same thing. But suppose someone hands you a second ruler, marked not in centimetres but in steps. On that ruler the staircase is perfectly even: each mark is one step, and counting is trivial again. Nothing about the staircase has changed. Only the ruler has.

That is the first idea of this topic. A differential equation with variable coefficients is a staircase with uneven steps: the rule that governs the unknown function changes as you move along the axis. If you measure along a different axis, chosen cleverly, the rule can become even again, and the equation becomes one you already know how to solve. Choosing that better ruler is called changing the independent variable, and it is the course's Method I.

Think of a second everyday situation. A photograph taken with the camera tilted makes a level horizon look slanted. Nothing in the scene is slanted; only the frame is. Rotate the frame until the horizon is level, and the picture becomes easy to describe. In the same way, an equation may contain an extra term, the term involving the first derivative, that merely records the tilt of the frame. Multiply the unknown function by a suitable factor, and that term disappears, leaving a simpler equation with the same solutions in disguise. This is called removing the first derivative, or reducing the equation to its normal form, and it is the course's Method II.

Picture a third situation, which will matter in the last part of the note. You are told one exact height on the staircase, say the height at the tenth step. From that single fact plus the rule of the staircase you can work out the whole staircase, because the rule supplies the rest. In the same way, one known solution of a second-order equation is often enough to produce the general solution. This is called reduction of order.

Each of these three pictures will be made precise in what follows. None of them involves guessing. All three are systematic, and all three follow from the same rule for differentiating a function of a function.

### 1.2 What the equation looks like, and what every symbol means

An equation is called a differential equation when it contains derivatives of an unknown function. It is called second order when the highest derivative present is the second derivative. It is called linear when the unknown function and its derivatives appear only to the first power and are never multiplied together.

> **Definition (second order linear equation with variable coefficients).** Let $a_{0}$, $a_{1}$, $a_{2}$ and $f$ be functions of the variable $x$, with $a_{0}$ never equal to zero. An equation of the form
>
> $$
> a_{0}(x)\frac{d^{2}y}{dx^{2}}+a_{1}(x)\frac{dy}{dx}+a_{2}(x)y=f(x)
> $$
>
> is a second order linear differential equation with variable coefficients.

Read that formula one symbol at a time. The letter $y$ is the unknown, a function of the single variable $x$. The symbol $\frac{dy}{dx}$ is the first derivative of $y$, the rate at which $y$ changes as $x$ increases. The symbol $\frac{d^{2}y}{dx^{2}}$ is the second derivative, the rate at which the first derivative itself changes. The letters $a_{0}$, $a_{1}$, $a_{2}$ stand for three functions of $x$: for each value of $x$ they give three numbers, and those numbers are the coefficients multiplying the second derivative, the first derivative and the function itself. The letter $f$ stands for the prescribed right-hand side, again a function of $x$. The condition that $a_{0}$ is never zero guarantees that the second derivative is genuinely present everywhere on the interval under discussion.

The word variable in the name refers to the coefficients $a_{0}$, $a_{1}$, $a_{2}$, not to $x$. Constant coefficients would mean the three numbers never change as $x$ moves; variable coefficients mean they do change, so the equation is a different equation at every point.

Dividing the whole equation by $a_{0}(x)$ puts it in the form used by every formula in this topic. This division is allowed at every point where $a_{0}$ is not zero, which is exactly the condition already imposed.

> **Definition (standard form).** The standard form of a second order linear equation is
>
> $$
> \frac{d^{2}y}{dx^{2}}+P\frac{dy}{dx}+Qy=R ,
> $$
>
> where $P$ is $a_{1}$ divided by $a_{0}$, $Q$ is $a_{2}$ divided by $a_{0}$, and $R$ is $f$ divided by $a_{0}$. All three of $P$, $Q$, $R$ are functions of $x$.

Here is a small example of the division. Take the equation

$$
3x^{2}\frac{d^{2}y}{dx^{2}}-6x\frac{dy}{dx}+9y=x .
$$

Dividing every term by $3x^{2}$, which is allowed for $x$ not zero, gives

$$
\frac{d^{2}y}{dx^{2}}-\frac{2}{x}\frac{dy}{dx}+\frac{3}{x^{2}}y=\frac{1}{3x^{2}} .
$$

Comparing with the standard form, $P$ is $-\frac{2}{x}$, the function whose value at each $x$ is minus two divided by $x$; $Q$ is $\frac{3}{x^{2}}$; and $R$ is $\frac{1}{3x^{2}}$. Nothing has been solved yet. The equation has merely been put in the shape that the theorems require, and that reshaping is the first step of every question.

### 1.3 The three coefficient functions and what each one does

Although $P$, $Q$ and $R$ look alike in the formula, they play completely different roles, and knowing the role of each is what allows you to choose a method.

The function $Q$ measures how strongly the equation pulls the solution back towards zero. In the constant-coefficient equation $y''+9y=0$, whose solutions are sines and cosines of frequency three, the number $9$ is precisely this coefficient. In the variable case it may be $\frac{3}{x^{2}}$ or $4x^{2}$ or $25+\frac{2}{x^{2}}$, and it is this function that decides the frequency of the oscillation and how that frequency changes along the axis.

The function $P$ measures a drift or a damping. In the constant-coefficient equation $y''+2y'+9y=0$ the number $2$ is this coefficient, and it makes the oscillations die away. In the variable case $P$ can make them die away in some regions and grow in others. It is the only one of the three that can be removed by multiplying the unknown by a factor, which is why Method II is entirely about $P$.

The function $R$ is the applied force, the prescribed right-hand side. It does not affect the family of solutions of the homogeneous equation at all; it only adds one extra solution of its own kind. When $R$ is zero the equation is called homogeneous, and when $R$ is not zero it is called non-homogeneous. The word refers to the right-hand side and to nothing else.

Two more words are needed before the methods can be stated.

> **Definition (solution and general solution).** A function $y$ is a solution of the equation on an interval if substituting it, together with its first and second derivatives, into the equation produces an identity for every $x$ in that interval. The general solution is the family of all such solutions, and for a second order equation that family contains exactly two independent arbitrary constants.

The count of two is not a convention. Two differentiations have been performed to build the equation, so two integrations are needed to undo them, and each integration contributes one constant. A second order answer with one constant is incomplete, and a second order answer with three constants is wrong.

### 1.4 The two things that can be changed, and the one thing that can be spotted

Every method in this topic is a change of something, and it helps to be clear about what may be changed and what may not.

The variable $x$ may be replaced by a new variable, usually written $z$. The unknown function is then regarded as a function of $z$, and the derivatives with respect to $x$ must be rewritten in terms of derivatives with respect to $z$ using the chain rule. The equation keeps its solutions, but its coefficients are expressed in the new variable, and with a good choice they become constants.

The unknown function $y$ may be replaced by a product, usually written $y=uv$. The two factors are not symmetric: $u$ is chosen by us, in a formula that depends only on the coefficient $P$, and $v$ is the new unknown. The equation for $v$ has no first-derivative term, and it is called the normal form.

The equation itself may sometimes be recognised as a derivative in disguise. If the whole left-hand side is the derivative of something simpler, then the equation says that this simpler thing is constant, and one integration reduces the problem from second order to first order. This is called exactness, and it is spotted by checking one identity among the coefficients.

These three devices are usually called, respectively, Method I, Method II, and the exact case. A fourth device, reduction of order, is used when the question supplies one solution and asks for the rest.

### 1.5 A first look at why a variable coefficient changes the shape of the answer

Before any formula, it is worth seeing with small numbers why a variable coefficient produces an unfamiliar answer.

The constant-coefficient equation

$$
\frac{d^{2}y}{dx^{2}}+y=0
$$

has solutions $\cos x$ and $\sin x$: waves whose crests are equally spaced. Now add a variable coefficient and one extra term, and consider

$$
\frac{d^{2}y}{dx^{2}}-\frac{1}{x}\frac{dy}{dx}+4x^{2}y=0 .
$$

Its solutions are $\cos\left(x^{2}\right)$ and $\sin\left(x^{2}\right)$, which can be checked by substituting, and the check is carried out below. As $x$ grows, the argument $x^{2}$ grows faster and faster, so the waves become more and more tightly packed. The coefficient of $y$ has told the equation that the natural frequency increases with distance, and the solution obeys.

Now notice something encouraging. If $z$ stands for $x^{2}$, then those two solutions are simply $\cos z$ and $\sin z$. In the $z$ variable they are ordinary, evenly spaced waves. The messiness was entirely an artefact of measuring along $x$. Measuring along $z$ restores order. That single observation is Method I.

The same observation can be checked by differentiation, and the check is worth doing once by hand because it uses only the chain rule. Let $Y$ be any function of one variable, and let $y$ be the function of $x$ defined by $y=Y\left(x^{2}\right)$. Then

$$
\frac{dy}{dx}=2x\,Y'\left(x^{2}\right) ,
$$

because the derivative of the inside function $x^{2}$ is $2x$. Differentiating again, this time by the product rule applied to the two factors $2x$ and $Y'\left(x^{2}\right)$, gives

$$
\frac{d^{2}y}{dx^{2}}=2Y'\left(x^{2}\right)+4x^{2}Y''\left(x^{2}\right) .
$$

Substituting these two expressions into the left-hand side of that equation produces

$$
2Y'+4x^{2}Y''-2Y'+4x^{2}Y=4x^{2}\left(Y''+Y\right) .
$$

The two terms in $Y'$ cancel exactly, and what survives is a multiple of $Y''+Y$. Since $4x^{2}$ is not zero for $x$ not zero, the original equation is satisfied exactly when $Y''+Y=0$ is satisfied. The variable coefficient has been absorbed, and the problem has become the constant-coefficient equation of the first line of this subsection.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Method I: the change of variable theorem

> **Theorem 1 (changing the independent variable).** Suppose the equation is in standard form, with coefficient functions $P$, $Q$ and right-hand side $R$. Let $z$ be a function of $x$ whose derivative is never zero, so that $z$ may be used as a new variable. Write the unknown as a function of $z$, that is $y=Y(z)$. Then the equation becomes
>
> $$
> \frac{d^{2}Y}{dz^{2}}+P_{1}\frac{dY}{dz}+Q_{1}Y=R_{1},
> $$
>
> where the three new coefficient functions are
>
> $$
> P_{1}=\frac{\frac{d^{2}z}{dx^{2}}+P\frac{dz}{dx}}{\left(\frac{dz}{dx}\right)^{2}}, \qquad Q_{1}=\frac{Q}{\left(\frac{dz}{dx}\right)^{2}}, \qquad R_{1}=\frac{R}{\left(\frac{dz}{dx}\right)^{2}} .
> $$

Read the three formulas in words. The new coefficient of $Y$ is the old $Q$ divided by the square of the rate at which $z$ changes with $x$. The new right-hand side is the old $R$ divided by that same square. The new coefficient of the first derivative is the old $P$ plus the curvature of $z$, again divided by that square.

The square appears everywhere for one reason: two differentiations with respect to $x$ are being traded for two differentiations with respect to $z$, and each trade brings one factor of $\frac{dz}{dx}$.

### 2.2 The choice of ruler that makes the coefficient of $Y$ equal to one

The formula for $Q_{1}$ shows that we are free to normalise the coefficient of $Y$ to any convenient value, because we may choose $\frac{dz}{dx}$ as we please. The convenient value is one.

If $Q$ is positive on the interval, define

$$
\frac{dz}{dx}=\sqrt{Q} ,
$$

the positive square root. Then $\left(\frac{dz}{dx}\right)^{2}=Q$, and therefore $Q_{1}$ equals one and the formula for $P_{1}$ becomes

$$
P_{1}=\frac{\frac{Q'}{2\sqrt{Q}}+P\sqrt{Q}}{Q}=\frac{Q'}{2Q^{3/2}}+\frac{P}{\sqrt{Q}} .
$$

Integrating the defining relation gives the new variable itself,

$$
z=\int\sqrt{Q}\,dx .
$$

So the recipe is short: take the square root of $Q$, integrate it, and use the result as the new variable. In the example of Section 1.5, $Q$ was $4x^{2}$, its square root was $2x$, and the integral was $x^{2}$.

Whether the method then succeeds depends on $P_{1}$. If $P_{1}$ happens to be a constant, the transformed equation has constant coefficients and is solved by the usual characteristic equation. The cleanest case is $P_{1}=0$, and it occurs exactly when

$$
Q'+2PQ=0
$$

on the interval. That identity is a one-line test on the coefficients, and it is the first thing to check in a Method I question.

When $Q$ is negative on the interval, its square root is not real. The repair is to use $z=\int\sqrt{-Q}\,dx$, which makes $Q_{1}$ equal to minus one. The transformed equation is then $\frac{d^{2}Y}{dz^{2}}+P_{1}\frac{dY}{dz}-Y=R_{1}$, still with constant coefficients whenever $P_{1}$ is constant.

### 2.3 Method II: the normal form theorem

> **Theorem 2 (removal of the first derivative).** Define the multiplier
>
> $$
> u=\exp\left(-\frac{1}{2}\int P\,dx\right),
> $$
>
> which is positive for every $x$. Write the unknown as a product $y=uv$. Then the equation is satisfied exactly when $v$ satisfies
>
> $$
> \frac{d^{2}v}{dx^{2}}+Sv=T ,
> $$
>
> where
>
> $$
> S=Q-\frac{1}{4}P^{2}-\frac{1}{2}\frac{dP}{dx}, \qquad T=\frac{R}{u} .
> $$

The equation $v''+Sv=T$ is called the normal form. It has no term containing the first derivative, and that absence is its whole point: with no first-derivative term, the equation can be solved by the characteristic equation whenever $S$ is a constant, and its solutions can be discussed qualitatively even when $S$ is not.

Three practical remarks make the theorem usable.

First, the multiplier $u$ is never zero, since an exponential is always positive. Multiplying by it and dividing by it are therefore always legitimate, which is why the two equations have precisely the same solutions after the substitution.

Second, the multiplier is unique up to a constant factor, and the constant factor cancels in the product $y=uv$. It is therefore standard to take the constant of integration in $\int P\,dx$ to be zero, and that is what makes the exponent look tidy in the examples.

Third, the coefficient $S$ has three parts and the derivative part is the one most often forgotten. When $P$ is a number, its derivative is zero and the third part vanishes. When $P$ is a function of $x$, the derivative must be computed, and getting its sign wrong changes $S$ completely.

### 2.4 What the normal form buys you

The normal form does three things that the original equation does not.

It turns any equation with constant $S$ into a constant-coefficient problem. The equation $v''-v=x$, for instance, is solved by the characteristic equation $m^{2}-1=0$ together with a linear particular integral. Once $S$ has been computed, no new technique is required.

It makes the qualitative behaviour visible. When $S$ is positive, the solutions of $v''+Sv=0$ behave like sines and cosines and oscillate without limit. When $S$ is negative, they behave like real exponentials and cross zero at most once. Because $u$ never vanishes, the zeros of $y$ are exactly the zeros of $v$, so the original equation inherits this behaviour. That is why a single number $S$ can answer questions about how often a solution crosses zero.

It isolates the part of the equation that cannot be removed. The term in $P$ is a drift that can always be absorbed into the multiplier; what remains after the absorption is $S$, and $S$ contains the irreducible content of the equation. Two equations with the same $S$ differ only by a drift and are, in this sense, the same equation.

### 2.5 The exactness test

> **Theorem 3 (exactness).** The equation $y''+Py'+Qy=R$ is exact if and only if
>
> $$
> \frac{dP}{dx}=Q
$$
>
> on the interval. When this holds, the equation is equivalent to the first order equation
>
> $$
> \frac{dy}{dx}+Py=\int R\,dx+C ,
> $$
>
> which is solved by multiplying through by the integrating factor $e^{\int P\,dx}$.

The idea behind the test is the product rule. The derivative of the expression $y'+Py$ is

$$
\frac{d}{dx}\left(\frac{dy}{dx}+Py\right)=\frac{d^{2}y}{dx^{2}}+P\frac{dy}{dx}+\frac{dP}{dx}y .
$$

Compare that with the left-hand side $y''+Py'+Qy$. The first two terms agree whatever $Q$ is. The third terms agree exactly when the derivative of $P$ equals $Q$, and that is the test. When the test passes, the whole left-hand side is one derivative, the equation reads "the derivative of something is $R$", and one integration finishes the second-order part of the problem.

The test is a single differentiation and a single comparison, and it costs less than a minute. It is worth doing first, because when it passes the question collapses.

### 2.6 Reduction of order: one solution is enough for two

> **Theorem 4 (reduction of order).** Suppose the equation is homogeneous and suppose $y_{1}$ is a known solution that is not zero on the interval. Write $y=uy_{1}$ with $u$ the new unknown. Then $y$ is a solution exactly when $w=\frac{du}{dx}$ satisfies the first order linear equation
>
> $$
> \frac{dw}{dx}+\left(\frac{2}{y_{1}}\frac{dy_{1}}{dx}+P\right)w=0 ,
> $$
>
> and the general solution is
>
> $$
> y=y_{1}\left(C_{1}+C_{2}\int\frac{e^{-\int P\,dx}}{y_{1}^{2}}\,dx\right) .
> $$

The mechanism is a cancellation. When $y=uy_{1}$ is substituted into the equation, the terms that contain $u$ but not its derivatives collect into the expression $y_{1}''+Py_{1}'+Qy_{1}$ multiplied by $u$. That expression is zero, because $y_{1}$ is a solution. What is left involves only $u'$ and $u''$, so the equation has become first order in the unknown $w=u'$.

The formula at the end of the theorem is worth remembering, but it is not necessary: the substitution $y=uy_{1}$, carried out with the product rule, produces the first-order equation directly, and that is the safer route in an examination because each step can be checked.

### 2.7 A table of the four devices

The four devices differ in what is changed and in what must be true before they can be used. The table collects the information.

| Device | What is changed | Test on the coefficients | Resulting equation |
| --- | --- | --- | --- |
| Change of variable | $x$ becomes $z$ | $Q>0$, and $Q'+2PQ=0$ or $P_{1}$ constant | $Y''+P_{1}Y'+Q_{1}Y=R_{1}$ |
| Normal form | $y$ becomes $uv$ | $S$ is a constant | $v''+Sv=T$ |
| Exactness | nothing | $P'=Q$ | $y'+Py=\int R\,dx+C$ |
| Reduction of order | $y$ becomes $uy_{1}$ | one non-zero solution given | $w'+\left(\frac{2y_{1}'}{y_{1}}+P\right)w=0$ |

The second column answers the question "what am I allowed to touch", the third answers "does this method apply here", and the fourth answers "what do I get". Reading the table from left to right is a decision procedure.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Deriving the change of variable formula

Step 1. Start from the standard form and choose a new variable $z$ that depends on $x$.

$$
\frac{d^{2}y}{dx^{2}}+P\frac{dy}{dx}+Qy=R
$$

Step 2. Regard $y$ as a function of $z$. The chain rule gives the first derivative.

$$
\frac{dy}{dx}=\frac{dY}{dz}\cdot\frac{dz}{dx}
$$

Step 3. Differentiate again, treating the right-hand side as a product of two factors.

$$
\frac{d^{2}y}{dx^{2}}=\frac{d}{dx}\left(\frac{dY}{dz}\right)\cdot\frac{dz}{dx}+\frac{dY}{dz}\cdot\frac{d^{2}z}{dx^{2}}
$$

Step 4. The first factor needs the chain rule once more, because $\frac{dY}{dz}$ is a function of $z$ and $z$ is a function of $x$.

$$
\frac{d}{dx}\left(\frac{dY}{dz}\right)=\frac{d^{2}Y}{dz^{2}}\cdot\frac{dz}{dx}
$$

Step 5. Insert Step 4 into Step 3.

$$
\frac{d^{2}y}{dx^{2}}=\frac{d^{2}Y}{dz^{2}}\left(\frac{dz}{dx}\right)^{2}+\frac{dY}{dz}\cdot\frac{d^{2}z}{dx^{2}}
$$

Step 6. Substitute the expressions of Steps 2 and 5 into the equation.

$$
\left(\frac{dz}{dx}\right)^{2}\frac{d^{2}Y}{dz^{2}}+\left(\frac{d^{2}z}{dx^{2}}+P\frac{dz}{dx}\right)\frac{dY}{dz}+QY=R
$$

Step 7. Divide through by the square of $\frac{dz}{dx}$, which is not zero because $z$ was chosen with non-zero derivative.

$$
\frac{d^{2}Y}{dz^{2}}+\frac{\frac{d^{2}z}{dx^{2}}+P\frac{dz}{dx}}{\left(\frac{dz}{dx}\right)^{2}}\frac{dY}{dz}+\frac{Q}{\left(\frac{dz}{dx}\right)^{2}}Y=\frac{R}{\left(\frac{dz}{dx}\right)^{2}}
$$

Step 8. Name the three divided quantities $P_{1}$, $Q_{1}$ and $R_{1}$. That is the theorem.

The one step that is easy to lose is Step 4. If the first factor of Step 3 is treated as a constant, the term containing the curvature of $z$ disappears and the resulting coefficients are wrong. The curvature term is exactly what allows a good change of variable to cancel the old first-derivative coefficient, so losing it destroys the method.

### 3.2 Carrying out the derivation with the small example

Step 1. Take the equation of Section 1.5 in standard form.

$$
\frac{d^{2}y}{dx^{2}}-\frac{1}{x}\frac{dy}{dx}+4x^{2}y=0
$$

Step 2. Identify the three coefficient functions.

$$
P=-\frac{1}{x}, \qquad Q=4x^{2}, \qquad R=0
$$

Step 3. Apply the recipe: take the square root of $Q$ and integrate.

$$
\frac{dz}{dx}=\sqrt{4x^{2}}=2x, \qquad z=\int 2x\,dx=x^{2}
$$

Step 4. Compute the two ingredients needed in the formulas.

$$
\left(\frac{dz}{dx}\right)^{2}=4x^{2}, \qquad \frac{d^{2}z}{dx^{2}}=2
$$

Step 5. Compute $P_{1}$ by substituting into its formula.

$$
P_{1}=\frac{2+\left(-\frac{1}{x}\right)\left(2x\right)}{4x^{2}}=\frac{2-2}{4x^{2}}=0
$$

Step 6. Compute $Q_{1}$.

$$
Q_{1}=\frac{4x^{2}}{4x^{2}}=1
$$

Step 7. Compute $R_{1}$, which is zero because $R$ is zero.

$$
R_{1}=\frac{0}{4x^{2}}=0
$$

Step 8. Write the transformed equation.

$$
\frac{d^{2}Y}{dz^{2}}+Y=0
$$

Step 9. Solve it. The characteristic equation is $m^{2}+1=0$ with roots $m=\pm i$, so

$$
Y=c_{1}\cos z+c_{2}\sin z .
$$

Step 10. Return to $x$ by putting $z=x^{2}$.

$$
y=c_{1}\cos\left(x^{2}\right)+c_{2}\sin\left(x^{2}\right)
$$

Step 11. Confirm the result by direct substitution, which was already done in Section 1.5: the two terms in $Y'$ cancel and what remains is $4x^{2}\left(Y''+Y\right)$, which is zero. The derivation and the check agree.

### 3.3 Deriving the normal form with a concrete multiplier

The general derivation is given with symbols in Section 3.5; here it is carried out with numbers, which is the quickest way to see the mechanism.

Step 1. Take the equation

$$
\frac{d^{2}y}{dx^{2}}-\frac{2}{x}\frac{dy}{dx}+\left(1+\frac{2}{x^{2}}\right)y=0 .
$$

Step 2. Read off the coefficient of the first derivative.

$$
P=-\frac{2}{x}
$$

Step 3. Compute half of its integral, with the sign required by the theorem.

$$
-\frac{1}{2}\int\left(-\frac{2}{x}\right)dx=\int\frac{1}{x}dx=\ln x
$$

Step 4. Exponentiate to obtain the multiplier. Since the exponential of $\ln x$ is $x$, the multiplier is a single power.

$$
u=e^{\ln x}=x
$$

Step 5. Announce the substitution $y=xv$, and differentiate it twice using the product rule.

$$
\frac{dy}{dx}=v+x\frac{dv}{dx}, \qquad \frac{d^{2}y}{dx^{2}}=2\frac{dv}{dx}+x\frac{d^{2}v}{dx^{2}}
$$

Step 6. Substitute these into the equation of Step 1.

$$
2v'+xv''-\frac{2}{x}\left(v+xv'\right)+\left(1+\frac{2}{x^{2}}\right)xv=0
$$

Step 7. Expand the bracket.

$$
2v'+xv''-\frac{2v}{x}-2v'+xv+\frac{2v}{x}=0
$$

Step 8. Cancel the terms that appear with both signs. The two terms in $v'$ cancel, and the two terms in $\frac{v}{x}$ cancel.

$$
xv''+xv=0
$$

Step 9. Divide by $x$, which is not zero on the interval of interest.

$$
\frac{d^{2}v}{dx^{2}}+v=0
$$

Step 10. Compare with the normal form. Here $S=1$ and $T=0$, which agrees with the formula, because with $P=-\frac{2}{x}$ one finds $P^{2}=\frac{4}{x^{2}}$ and $\frac{dP}{dx}=\frac{2}{x^{2}}$, so

$$
S=\left(1+\frac{2}{x^{2}}\right)-\frac{1}{4}\cdot\frac{4}{x^{2}}-\frac{1}{2}\cdot\frac{2}{x^{2}}=1+\frac{2}{x^{2}}-\frac{1}{x^{2}}-\frac{1}{x^{2}}=1 .
$$

Step 11. Solve the normal form.

$$
v=c_{1}\cos x+c_{2}\sin x
$$

Step 12. Multiply by the multiplier to obtain $y$.

$$
y=x\left(c_{1}\cos x+c_{2}\sin x\right)
$$

Step 13. Check one solution in the original equation. Take $y=x\cos x$, whose derivatives are $y'=\cos x-x\sin x$ and $y''=-2\sin x-x\cos x$. Then

$$
-2\sin x-x\cos x-\frac{2}{x}\left(\cos x-x\sin x\right)+x\cos x+2\frac{\cos x}{x}=0 ,
$$

because $-2\sin x+2\sin x=0$, $-x\cos x+x\cos x=0$ and $-\frac{2\cos x}{x}+\frac{2\cos x}{x}=0$. The solution is confirmed.

### 3.4 Deriving the exactness test and using it

Step 1. Compute the derivative of the combination $y'+Py$ by the product rule.

$$
\frac{d}{dx}\left(\frac{dy}{dx}+Py\right)=\frac{d^{2}y}{dx^{2}}+P\frac{dy}{dx}+\frac{dP}{dx}y
$$

Step 2. Compare with the left-hand side of the equation.

$$
\frac{d^{2}y}{dx^{2}}+P\frac{dy}{dx}+Qy
$$

Step 3. Observe that the two agree for every function $y$ exactly when the coefficients of $y$ agree, that is when

$$
\frac{dP}{dx}=Q .
$$

Step 4. Conclude both directions. If the identity holds, the left-hand side is a derivative. If the left-hand side is a derivative of the form $\frac{d}{dx}\left(y'+Ay\right)$, then expanding shows $A$ must be $P$ and then $Q$ must be the derivative of $P$. So the condition is necessary and sufficient.

Step 5. Use it. If the condition holds, integrate once.

$$
\frac{dy}{dx}+Py=\int R\,dx+C
$$

Step 6. Multiply by the integrating factor, which is the exponential of the integral of $P$.

$$
\frac{d}{dx}\left(ye^{\int P\,dx}\right)=e^{\int P\,dx}\left(\int R\,dx+C\right)
$$

Step 7. Integrate once more to obtain $y$. The equation has become two quadratures instead of a second-order problem.

### 3.5 The general derivation of the normal form

Step 1. Write $y=uv$ and differentiate once.

$$
\frac{dy}{dx}=u\frac{dv}{dx}+v\frac{du}{dx}
$$

Step 2. Differentiate again, applying the product rule to each piece.

$$
\frac{d^{2}y}{dx^{2}}=u\frac{d^{2}v}{dx^{2}}+2\frac{du}{dx}\frac{dv}{dx}+v\frac{d^{2}u}{dx^{2}}
$$

Step 3. Substitute into the standard form and group the result by $v''$, $v'$ and $v$.

$$
u\frac{d^{2}v}{dx^{2}}+\left(2\frac{du}{dx}+Pu\right)\frac{dv}{dx}+\left(\frac{d^{2}u}{dx^{2}}+P\frac{du}{dx}+Qu\right)v=R
$$

Step 4. Kill the term in $v'$ by demanding

$$
2\frac{du}{dx}+Pu=0 .
$$

Step 5. Separate and integrate that demand.

$$
\frac{1}{u}\frac{du}{dx}=-\frac{P}{2}, \qquad u=\exp\left(-\frac{1}{2}\int P\,dx\right)
$$

Step 6. Divide the equation of Step 3 by $u$, which is legitimate because the exponential is never zero.

$$
\frac{d^{2}v}{dx^{2}}+\frac{1}{u}\left(\frac{d^{2}u}{dx^{2}}+P\frac{du}{dx}+Qu\right)v=\frac{R}{u}
$$

Step 7. Compute the derivatives of $u$ from Step 5 and simplify the bracket.

$$
\frac{du}{dx}=-\frac{P}{2}u, \qquad \frac{d^{2}u}{dx^{2}}=\left(\frac{P^{2}}{4}-\frac{P'}{2}\right)u
$$

Step 8. Substitute those two expressions into the bracket and collect.

$$
\frac{d^{2}u}{dx^{2}}+P\frac{du}{dx}+Qu=u\left(\frac{P^{2}}{4}-\frac{P'}{2}-\frac{P^{2}}{2}+Q\right)=u\left(Q-\frac{P^{2}}{4}-\frac{P'}{2}\right)
$$

Step 9. Divide by $u$ and name the bracket $S$.

$$
\frac{d^{2}v}{dx^{2}}+Sv=\frac{R}{u}
$$

Step 10. Name the right-hand side $T$. That is the theorem, and every step was reversible.

The derivation shows why the three parts of $S$ appear. The $Q$ comes straight through from the original equation. The $-\frac{1}{4}P^{2}$ comes from the second derivative of the multiplier. The $-\frac{1}{2}P'$ comes from the first derivative of the multiplier, and it is the part that vanishes only when $P$ is constant.

### 3.6 Deriving reduction of order with a known solution

Step 1. Take the homogeneous equation and a known non-zero solution $y_{1}$.

$$
\frac{d^{2}y}{dx^{2}}+P\frac{dy}{dx}+Qy=0
$$

Step 2. Substitute $y=uy_{1}$ and differentiate twice.

$$
\frac{dy}{dx}=u'y_{1}+uy_{1}', \qquad \frac{d^{2}y}{dx^{2}}=u''y_{1}+2u'y_{1}'+uy_{1}''
$$

Step 3. Put both into the equation and group by $u''$, $u'$ and $u$.

$$
u''y_{1}+u'\left(2y_{1}'+Py_{1}\right)+u\left(y_{1}''+Py_{1}'+Qy_{1}\right)=0
$$

Step 4. The bracket multiplying $u$ is zero, because $y_{1}$ is a solution. That single fact is the whole trick.

$$
u''y_{1}+u'\left(2y_{1}'+Py_{1}\right)=0
$$

Step 5. Divide by $y_{1}$, which is allowed since $y_{1}$ is not zero.

$$
u''+\left(\frac{2y_{1}'}{y_{1}}+P\right)u'=0
$$

Step 6. Put $w=u'$. The equation is now first order in $w$.

$$
\frac{dw}{dx}+\left(\frac{2y_{1}'}{y_{1}}+P\right)w=0
$$

Step 7. Separate and integrate, using that the integral of $\frac{y_{1}'}{y_{1}}$ is the logarithm of $y_{1}$.

$$
w=\frac{C_{2}e^{-\int P\,dx}}{y_{1}^{2}}
$$

Step 8. Integrate once more to get $u$, then multiply by $y_{1}$.

$$
y=y_{1}\left(C_{1}+C_{2}\int\frac{e^{-\int P\,dx}}{y_{1}^{2}}\,dx\right)
$$

Step 9. Count the constants. There are two, one from each integration, matching the order of the equation.

### 3.7 The order in which to try the devices

A reliable routine for any question is to put the equation in standard form, then compute three quick diagnostics and let them choose the method.

Compute the derivative of $P$. If it equals $Q$, the equation is exact, and the fastest route is to integrate once.

Compute $Q'+2PQ$. If it is zero, the change of variable $z=\int\sqrt{Q}\,dx$ produces $Y''+Y=R_{1}$, which is solved by inspection of a cosine-sine complementary function.

Compute $S=Q-\frac{1}{4}P^{2}-\frac{1}{2}P'$. If it is a constant, the normal form has constant coefficients, and the multiplier $u$ together with a single particular integral finishes the question.

If none of the three succeeds and the question supplies one solution, use reduction of order. If none succeeds and no solution is supplied, the equation is not solvable in elementary terms by these devices, and the expected answer is a statement to that effect together with a series or numerical approach.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: put an equation in standard form and read off the coefficients

Write

$$
4x^{2}\frac{d^{2}y}{dx^{2}}-8x\frac{dy}{dx}+12y=4
$$

in standard form on the interval $x>0$, and state the three coefficient functions.

### 4.2 Solution: divide by the coefficient of the second derivative

Step 1. Identify the coefficient to be divided out, which is $4x^{2}$.

Step 2. Divide every term, which is legitimate for $x$ not zero.

$$
\frac{d^{2}y}{dx^{2}}-\frac{2}{x}\frac{dy}{dx}+\frac{3}{x^{2}}y=\frac{1}{x^{2}}
$$

Step 3. Read the coefficients by comparison with the standard form.

$$
P=-\frac{2}{x}, \qquad Q=\frac{3}{x^{2}}, \qquad R=\frac{1}{x^{2}}
$$

Step 4. Check the division by multiplying back. Multiplying the standard form by $4x^{2}$ returns the original equation term by term, so the division was correct.

Step 5. Note the diagnostics for later use. The derivative of $P$ is $\frac{2}{x^{2}}$, which is not equal to $Q$, so the equation is not exact. The quantity $Q'+2PQ$ is $-\frac{6}{x^{3}}+2\left(-\frac{2}{x}\right)\frac{3}{x^{2}}=-\frac{18}{x^{3}}$, which is not zero, so the clean case of the change of variable does not apply directly. The coefficient $S$ is $\frac{3}{x^{2}}-\frac{1}{x^{2}}-\frac{1}{2}\left(\frac{2}{x^{2}}\right)=\frac{3}{x^{2}}-\frac{1}{x^{2}}-\frac{1}{x^{2}}=\frac{1}{x^{2}}$, which is not constant either. This equation therefore needs one of the other devices, and stating that is the correct end point of a classification question.

### 4.3 Problem: solve by changing the variable to $z=x^{2}$

Solve the equation of Section 3.2,

$$
\frac{d^{2}y}{dx^{2}}-\frac{1}{x}\frac{dy}{dx}+4x^{2}y=0 ,
$$

on $x>0$.

### 4.4 Solution: use the ruler that makes the coefficient equal to one

Step 1. Note the three coefficient functions, $P=-\frac{1}{x}$, $Q=4x^{2}$ and $R=0$.

Step 2. Take the square root of $Q$ and integrate it to obtain the new variable.

$$
z=\int 2x\,dx=x^{2}
$$

Step 3. Compute the two ingredients of the formulas: the square of the rate of change of $z$ and the curvature of $z$.

$$
\left(\frac{dz}{dx}\right)^{2}=4x^{2}, \qquad \frac{d^{2}z}{dx^{2}}=2
$$

Step 4. Compute the new first-derivative coefficient.

$$
P_{1}=\frac{2+\left(-\frac{1}{x}\right)\left(2x\right)}{4x^{2}}=0
$$

Step 5. Compute the new coefficient of $Y$.

$$
Q_{1}=\frac{4x^{2}}{4x^{2}}=1
$$

Step 6. Write the transformed equation.

$$
\frac{d^{2}Y}{dz^{2}}+Y=0
$$

Step 7. Solve it with the characteristic equation $m^{2}+1=0$.

$$
Y=c_{1}\cos z+c_{2}\sin z
$$

Step 8. Return to the original variable.

$$
y=c_{1}\cos\left(x^{2}\right)+c_{2}\sin\left(x^{2}\right)
$$

Step 9. Verify by substitution. With $y=\sin\left(x^{2}\right)$ the derivatives are $2x\cos\left(x^{2}\right)$ and $2\cos\left(x^{2}\right)-4x^{2}\sin\left(x^{2}\right)$, so

$$
2\cos\left(x^{2}\right)-4x^{2}\sin\left(x^{2}\right)-\frac{1}{x}\cdot 2x\cos\left(x^{2}\right)+4x^{2}\sin\left(x^{2}\right)=0 ,
$$

because $2\cos-2\cos=0$ and $-4x^{2}\sin+4x^{2}\sin=0$. The answer is confirmed and carries two constants.

### 4.5 Problem: remove the first derivative

Reduce

$$
\frac{d^{2}y}{dx^{2}}-\frac{2}{x}\frac{dy}{dx}+\left(1+\frac{2}{x^{2}}\right)y=0
$$

to normal form and hence solve it on $x>0$.

### 4.6 Solution: the multiplier is $x$

Step 1. Read off the coefficient of the first derivative, $P=-\frac{2}{x}$.

Step 2. Compute the exponent of the multiplier.

$$
-\frac{1}{2}\int\left(-\frac{2}{x}\right)dx=\ln x
$$

Step 3. Write the multiplier and the substitution.

$$
u=x, \qquad y=xv
$$

Step 4. Differentiate the substitution twice.

$$
\frac{dy}{dx}=v+xv', \qquad \frac{d^{2}y}{dx^{2}}=2v'+xv''
$$

Step 5. Substitute into the equation and expand.

$$
2v'+xv''-\frac{2v}{x}-2v'+xv+\frac{2v}{x}=0
$$

Step 6. Cancel the two terms in $v'$ and the two terms in $v$ over $x$.

$$
xv''+xv=0
$$

Step 7. Divide by $x$ to obtain the normal form.

$$
\frac{d^{2}v}{dx^{2}}+v=0
$$

Step 8. Solve it.

$$
v=c_{1}\cos x+c_{2}\sin x
$$

Step 9. Multiply by the multiplier.

$$
y=x\left(c_{1}\cos x+c_{2}\sin x\right)
$$

Step 10. Confirm that the coefficient $S$ in the normal form is what the formula predicts. With $P=-\frac{2}{x}$ we have $P^{2}=\frac{4}{x^{2}}$ and $P'=\frac{2}{x^{2}}$, so

$$
S=1+\frac{2}{x^{2}}-\frac{1}{x^{2}}-\frac{1}{x^{2}}=1 .
$$

Step 11. Confirm the solution $y=x\sin x$ by substitution, as was done in Step 13 of Section 3.3. The three groups of terms cancel, so the answer is correct.

### 4.7 Problem: use exactness

Solve

$$
\frac{d^{2}y}{dx^{2}}+\frac{1}{x}\frac{dy}{dx}-\frac{1}{x^{2}}y=0
$$

on $x>0$.

### 4.8 Solution: integrate once because the left side is a derivative

Step 1. Read off $P=\frac{1}{x}$ and $Q=-\frac{1}{x^{2}}$.

Step 2. Differentiate $P$ and compare with $Q$.

$$
\frac{dP}{dx}=-\frac{1}{x^{2}}=Q
$$

Step 3. Conclude that the equation is exact, and rewrite the left side as one derivative.

$$
\frac{d}{dx}\left(\frac{dy}{dx}+\frac{1}{x}y\right)=0
$$

Step 4. Integrate once.

$$
\frac{dy}{dx}+\frac{1}{x}y=C_{1}
$$

Step 5. Multiply by $x$ to make the left side a derivative of a product.

$$
x\frac{dy}{dx}+y=C_{1}x
$$

Step 6. Rewrite the left side.

$$
\frac{d}{dx}\left(xy\right)=C_{1}x
$$

Step 7. Integrate again.

$$
xy=\frac{C_{1}}{2}x^{2}+C_{2}
$$

Step 8. Divide by $x$ and rename the constant.

$$
y=Ax+\frac{B}{x}
$$

Step 9. Check the first solution $y=x$. Its derivatives are $1$ and $0$, so the left side is $0+\frac{1}{x}-\frac{1}{x^{2}}\cdot x=0$.

Step 10. Check the second solution $y=\frac{1}{x}$. Its derivatives are $-\frac{1}{x^{2}}$ and $\frac{2}{x^{3}}$, so the left side is $\frac{2}{x^{3}}-\frac{1}{x^{3}}-\frac{1}{x^{3}}=0$. Both are confirmed, and the two constants match the order.

### 4.9 Problem: reduce the order from one known solution

Given that $y=x$ is a solution of

$$
\frac{d^{2}y}{dx^{2}}-\frac{2}{x}\frac{dy}{dx}+\frac{2}{x^{2}}y=0 ,
$$

find the general solution on $x>0$.

### 4.10 Solution: substitute $y=xu$

Step 1. Check the supplied solution. With $y=x$ the derivatives are $1$ and $0$, so the left side is $0-\frac{2}{x}+\frac{2}{x^{2}}\cdot x=-\frac{2}{x}+\frac{2}{x}=0$, and $y=x$ is indeed a solution.

Step 2. Put $y=xu$ and differentiate twice.

$$
\frac{dy}{dx}=u+xu', \qquad \frac{d^{2}y}{dx^{2}}=2u'+xu''
$$

Step 3. Substitute into the equation.

$$
2u'+xu''-\frac{2}{x}\left(u+xu'\right)+\frac{2}{x^{2}}xu=0
$$

Step 4. Expand and collect.

$$
2u'+xu''-\frac{2u}{x}-2u'+\frac{2u}{x}=0
$$

Step 5. Cancel the terms that appear with both signs.

$$
xu''=0
$$

Step 6. Divide by $x$ and integrate twice.

$$
u''=0, \qquad u=Ax+B
$$

Step 7. Multiply by $y_{1}=x$.

$$
y=Ax^{2}+Bx
$$

Step 8. Check the new solution $y=x^{2}$. Its derivatives are $2x$ and $2$, so the left side is $2-\frac{2}{x}\cdot 2x+\frac{2}{x^{2}}x^{2}=2-4+2=0$. Confirmed.

Step 9. Observe the pattern. The two powers $x$ and $x^{2}$ are exactly the two solutions of an equation of Euler type, and the reduction of order has produced the second one without any guesswork.

### 4.11 Problem: test a proposed substitution

Decide whether the substitution $y=x^{2}v$ removes the first-derivative term from the equation of Section 4.4.

### 4.12 Solution: differentiate, substitute, and inspect the coefficients

Step 1. Differentiate the substitution twice, using the product rule.

$$
\frac{dy}{dx}=2xv+x^{2}v', \qquad \frac{d^{2}y}{dx^{2}}=2v+4xv'+x^{2}v''
$$

Step 2. Substitute into the standard form $y''-\frac{1}{x}y'+4x^{2}y=0$.

$$
2v+4xv'+x^{2}v''-\frac{1}{x}\left(2xv+x^{2}v'\right)+4x^{2}\cdot x^{2}v=0
$$

Step 3. Expand the bracket.

$$
2v+4xv'+x^{2}v''-2v-xv'+4x^{4}v=0
$$

Step 4. Cancel the terms in $v$ that carry no derivative.

$$
4xv'+x^{2}v''-xv'+4x^{4}v=0
$$

Step 5. Collect the remaining terms in $v'$.

$$
x^{2}v''+3xv'+4x^{4}v=0
$$

Step 6. Divide by $x^{2}$ and read the result.

$$
\frac{d^{2}v}{dx^{2}}+\frac{3}{x}\frac{dv}{dx}+4x^{2}v=0
$$

Step 7. Interpret. The first-derivative term has not disappeared, because the multiplier $x^{2}$ is not the one the theorem prescribes. The working shows a real first-derivative coefficient of $\frac{3}{x}$ in place of the original $-\frac{1}{x}$, so the substitution has changed the drift rather than removed it.

Step 8. State the lesson. A substitution only removes the first-derivative term if the multiplier satisfies $u'/u=-\frac{P}{2}$; here that condition would require $u'/u=\frac{1}{2x}$, whose solution is $\sqrt{x}$, not $x^{2}$. Trying a plausible power without checking the condition is a common and costly error.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 What the methods guarantee and what they do not

Each theorem in Section 2 is an equivalence. When the hypotheses hold, the new equation has exactly the same solutions as the old one, so no solution is lost and none is invented. That guarantee is worth stating in an answer, because it is the reason a transformed equation may be solved with confidence and the answer then translated back.

What the theorems do not guarantee is that the new equation is easy. A change of variable always produces a correct equation, but the new coefficients may be as complicated as the old ones. The normal form always exists, but its coefficient $S$ may be a function such as $\frac{1}{x^{2}}$ or $4x^{2}-\frac{3}{4x^{2}}$, in which case the normal form is no easier to solve than the equation we started with. Exactness is a genuine shortcut, but it requires the identity $P'=Q$, which usually fails.

This is why the diagnostics matter. They cost a line each and they tell you, before any algebra, whether the method you are about to use will lead anywhere. An answer that computes a change of variable for an equation where the clean case fails, and then stops, has wasted the working; an answer that checks the condition first and chooses the method that applies has done the mathematics properly.

### 5.2 The interval, the sign of $Q$, and the multiplier

Three conditions are easy to forget and each has a visible effect on the answer.

The equation must be considered on an interval on which the coefficient of the second derivative does not vanish, because the standard form divides by it. For an equation with $x^{2}$ as that coefficient, the interval is either the positive half-line or the negative half-line, and answers containing $\ln x$ are meaningful only on the positive one.

The square root of $Q$ must be real, which requires $Q$ to have a constant sign. When $Q$ is positive the new variable is $z=\int\sqrt{Q}\,dx$ and the coefficient $Q_{1}$ equals one. When $Q$ is negative the new variable is $z=\int\sqrt{-Q}\,dx$ and $Q_{1}$ equals minus one. When $Q$ changes sign inside the interval no single real change of variable works, and the method must be applied separately on each side of the change.

The multiplier $u$ is an exponential and is therefore never zero. That is what allows it to be multiplied and divided freely, and it is why the correspondence between solutions of the original equation and solutions of the normal form is exact.

### 5.3 Where these ideas lead

The normal form is the doorway to the qualitative theory of second-order equations. Because $v''+Sv=0$ contains only the coefficient $S$, questions about how often a solution crosses zero reduce to questions about the sign of $S$. When $S$ is a positive constant the solutions are waves with evenly spaced zeros; when $S$ is a negative constant they cross zero at most once; and when $S$ varies, the zeros accumulate where $S$ is large and spread out where $S$ is small. Since the multiplier never vanishes, the same statements hold for the original equation.

The exactness condition is the second-order version of a first-order idea. Every first-order linear equation $y'+Py=R$ can be integrated after multiplying by $e^{\int P\,dx}$; doing the same to a second-order equation brings it to the self-adjoint form in which the second and first derivative terms combine into one derivative. That form is available for every $P$ and is the shape in which second-order equations are studied in more advanced courses.

Reduction of order is the tool that makes a single lucky observation worth two arbitrary constants. It fails for third-order equations, where one known solution still leaves a second-order problem, and it needs the known solution to be non-zero on the interval, since the whole construction divides by it.

### 5.4 Beginner misconceptions

- **"Variable coefficients make the equation non-linear."** Linearity concerns the unknown function, not the coefficients. The equation $y''+x^{2}y=0$ is linear, because $y$ and its derivatives appear only to the first power; the coefficient $x^{2}$ does not spoil anything.
- **"There must be a characteristic equation."** A characteristic equation exists only when the coefficients are constants. With variable coefficients there is no polynomial whose roots give the answer, and looking for one wastes the whole question.
- **"The change of variable only renames the letter $x$."** A change of variable changes the scale along the axis, so derivatives must be rewritten by the chain rule. Renaming without transforming the derivatives produces a wrong equation.
- **"The second derivative transforms as $Y$ differentiated twice."** It does not. The second derivative brings an extra term containing $\frac{d^{2}z}{dx^{2}}$, and that term is what makes the method work.
- **"Any multiplier removes the first derivative."** Only $u$ with $u'/u=-\frac{P}{2}$ does. Section 4.11 shows a plausible multiplier that fails.
- **"$S$ is just $Q$."** The coefficient of the normal form is $Q-\frac{1}{4}P^{2}-\frac{1}{2}P'$, and dropping the last two parts gives a wrong equation even when $P$ looks harmless.
- **"The forcing in the normal form is $R$."** It is $R$ divided by $u$. Since $u$ is an exponential, forgetting the division changes the particular integral completely.
- **"Exactness always holds if the coefficients are smooth."** It requires the identity $P'=Q$, which is a coincidence of the coefficients and usually fails.
- **"One solution is only half an answer."** For a second-order homogeneous equation, one solution plus reduction of order gives the general solution. It is the whole answer, provided the second integration is carried out.
- **"Two constants can be added anywhere."** The constants must arise from the integrations. Adding a constant to $u$ in the middle of a calculation is not the same as integrating twice.
- **"A check at one point verifies a solution."** A solution must satisfy the equation for every $x$ in the interval. Substituting $x=0$ and getting zero proves nothing.
- **"The answer may be left in terms of $z$ or $v$."** The question is about $y$ as a function of $x$, so the final display must be in $x$.

### 5.5 A checklist and a routine

Before finishing any question on this topic, check the following.

The equation is in standard form, with the coefficient of the second derivative equal to one, and the interval is stated. The derivative of $P$ has been compared with $Q$ to test exactness, and the comparison is displayed. The quantity $Q'+2PQ$ has been computed if a change of variable is being considered. The coefficient $S$ has been computed with all three of its parts if the normal form is being used. The substitution has been differentiated twice, with the product rule applied where it is needed. The final answer is in terms of $x$ and contains exactly two arbitrary constants. At least one component of the answer has been substituted back into the original equation.

A routine that satisfies all of these takes about the same time as a careless attempt and scores far more. The three diagnostics are the part that beginners skip and the part that examiners look for, because they show that the method was chosen rather than guessed.
