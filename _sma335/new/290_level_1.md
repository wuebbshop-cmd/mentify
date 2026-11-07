## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A swing, a push, and two motions added together

Imagine a child on a swing that somebody has pushed once and then stepped away from. The swing keeps moving by itself, back and forth, and because of friction and air the swinging slowly dies down. Nothing is forcing it any more. It is simply following its own natural habit until the habit runs out of energy.

Now picture the same swing while a second person stands beside it and gives a small push every time the swing comes back towards them. Two separate things are happening at once. The swing still has its own natural sway, and it also has the rhythm that the regular pushes impose on it. What you actually see is those two motions laid on top of one another. At every instant the position of the seat is the position the natural sway would have produced, plus the extra displacement created by the pushes.

That picture is the whole of this note. Some rules about change describe a system left alone, and the answer to such a rule contains a part that fades away or oscillates by itself. Other rules add a push from outside, and then a second part of the answer appears, a part that follows the push rather than the system's own habits. The complete description is always those two parts added together.

Think of a second scene, a bath with the plug in and the tap running. The water level rises because water is arriving from outside. But the final level is not decided by the tap alone: the shape of the bath, the width of its base, and the depth already present all affect how fast the level climbs for a given flow. The bath's own character and the outside supply combine to produce the level you actually observe. The outside supply plays the role of the push, and the bath's character plays the role of the system's natural behaviour.

Here is a third scene that is closer to the algebra. Picture a small boat on a lake, pushed steadily sideways by a gust of wind. The boat first rocks in its own way, and then it settles into a lean that the wind holds in place. The rocking is the natural part; the steady lean is the forced part. When a student says that the total behaviour is the rocking plus the lean, that student has already understood the central idea of this topic.

The rest of this section gives names to the pieces of that picture, and shows how each piece is found.

### 1.2 Naming the pieces of the picture

Let $y$ stand for the quantity we want to know. It might be a distance, a charge, a temperature, or the height of water in a bath. Let $x$ stand for the quantity that drives the change, usually time. The letter $y$ is called the dependent variable because its value depends on $x$, and $x$ is called the independent variable because it is chosen freely and is not determined by the equation.

The symbols that describe change are read as follows. The expression $\frac{dy}{dx}$ is the rate at which $y$ changes as $x$ changes; think of it as the steepness of the curve that shows $y$ against $x$. The expression $\frac{d^{2}y}{dx^{2}}$ is the rate at which that steepness itself changes. When the steepness is increasing, the second expression is positive; when the steepness is decreasing, it is negative. In the swing picture, the first expression is the speed of the seat and the second is related to the force pulling the seat back towards the middle.

> **Definition (second-order nonhomogeneous linear equation with constant coefficients).** An equation of the form
>
> $$
> a_{0}\frac{d^{2}y}{dx^{2}}+a_{1}\frac{dy}{dx}+a_{2}y=Q(x),
> $$
>
> where $a_{0}$, $a_{1}$ and $a_{2}$ are fixed numbers with $a_{0}\ne 0$, and where $Q(x)$ is a known function of $x$, is called a second-order nonhomogeneous linear equation with constant coefficients.

Every word in that definition earns its place. Second-order means that the highest derivative present is the second derivative. Linear means that $y$ and its derivatives appear only to the first power and never multiplied together. Constant coefficients means that $a_{0}$, $a_{1}$ and $a_{2}$ are ordinary numbers, not functions of $x$. Nonhomogeneous means that the right-hand side $Q(x)$ is not the zero function.

The function $Q(x)$ has several names in common use: the forcing term, the forcing function, the input, or the nonhomogeneous term. All four names describe the same object, namely the outside push.

Take a small concrete equation with small numbers:

$$
\frac{d^{2}y}{dx^{2}}+3\frac{dy}{dx}+2y=6 .
$$

Read it aloud in words: the rate at which the steepness changes, plus three times the steepness, plus two times the value itself, equals six. Here $a_{0}=1$, $a_{1}=3$, $a_{2}=2$, and the push is the constant six.

> **Definition (homogeneous equation).** The equation obtained by replacing $Q(x)$ with zero,
>
> $$
> a_{0}\frac{d^{2}y}{dx^{2}}+a_{1}\frac{dy}{dx}+a_{2}y=0 ,
> $$
>
> is called the corresponding homogeneous equation.

The homogeneous equation describes the system with the push switched off. Its solution is called the complementary function, and it is the natural part of the first section's picture.

### 1.3 The answer always has two parts

The single most important sentence in this topic is the following one.

> **Theorem (shape of the general solution).** The general solution of the nonhomogeneous equation is
>
> $$
> y=y_{c}+y_{p},
> $$
>
> where $y_{c}$ is the general solution of the corresponding homogeneous equation and $y_{p}$ is any one solution of the nonhomogeneous equation.

Three definitions make that sentence usable.

> **Definition (complementary function).** The complementary function, written $y_{c}$, is the general solution of the homogeneous equation $a_{0}y''+a_{1}y'+a_{2}y=0$. It contains two arbitrary constants.

> **Definition (particular integral).** A particular integral, written $y_{p}$, is any single function that satisfies the nonhomogeneous equation. It contains no arbitrary constants.

> **Definition (general solution).** The general solution of the nonhomogeneous equation is the family $y=y_{c}+y_{p}$, containing exactly two arbitrary constants.

So the work splits into two independent jobs. Find the natural part by solving a homogeneous equation, which is a problem already familiar from the previous lesson. Then find one forced part by any method at all. Add them, and the answer is complete.

The word integral in particular integral is old-fashioned. It means the result of integrating, that is, the function obtained from the equation, and it does not mean that an integral sign must appear in the answer.

### 1.4 Finding the natural part with small numbers

The natural part comes from the homogeneous equation. Substituting the trial shape $y=e^{mx}$ into $a_{0}y''+a_{1}y'+a_{2}y=0$ produces the auxiliary equation

$$
a_{0}m^{2}+a_{1}m+a_{2}=0 .
$$

Its two roots decide the shape of $y_{c}$. For the small example above, with $a_{0}=1$, $a_{1}=3$ and $a_{2}=2$, the auxiliary equation is

$$
m^{2}+3m+2=0 ,
$$

which factorises as $(m+1)(m+2)=0$, so the roots are $m=-1$ and $m=-2$. The complementary function is therefore

$$
y_{c}=c_{1}e^{-x}+c_{2}e^{-2x},
$$

in which $c_{1}$ and $c_{2}$ are arbitrary constants. Two constants appear because the equation is of second order; the previous lesson established that this count is not optional.

Two other shapes of root occur and are worth naming here, because they matter in Section 5. If the two roots coincide, the complementary function carries an extra factor of $x$; for instance the equation with auxiliary equation $(m-2)^{2}=0$ has

$$
y_{c}=(c_{1}+c_{2}x)e^{2x}.
$$

If the roots are complex, the complementary function is built from a cosine and a sine; for instance the equation with auxiliary equation $m^{2}+1=0$ has

$$
y_{c}=c_{1}\cos x+c_{2}\sin x .
$$

### 1.5 Finding the forced part: guess the shape, then fix the numbers

The forced part is one single function that satisfies the equation with the push switched on. The method used throughout this course is called the method of undetermined coefficients, and it has a simple logic. Because the equation is linear with constant coefficients, a trial function of the right shape reproduces that same shape when it is differentiated twice and substituted. So we write down the shape with unknown numbers in it, substitute, and let the equation determine the numbers.

Start with the smallest possible case. For

$$
\frac{d^{2}y}{dx^{2}}+3\frac{dy}{dx}+2y=6 ,
$$

the push is the constant six, so try the constant $A$, that is, try $y=A$. Its derivatives are both zero, because a constant does not change. Substituting gives

$$
0+3\cdot 0+2A=6 ,
$$

so $A=3$. The particular integral is $y_{p}=3$, and the general solution is

$$
y=c_{1}e^{-x}+c_{2}e^{-2x}+3 .
$$

The check is immediate. Putting $y=3$ into the left-hand side gives $2\cdot 3=6$, which is exactly the push. That is all a particular integral has to do.

Notice the division of labour. The constants $c_{1}$ and $c_{2}$ are not determined, because the natural part is free to be any member of its family. The number $A$ is completely determined, because the forced part must match the push exactly.

### 1.6 Why a guess is allowed at all

A beginner often objects that guessing is not mathematics. The objection is fair in general but not here, and the reason is worth stating plainly. Differentiating a constant gives zero, which is again a constant-shaped object. Differentiating $e^{kx}$ gives a multiple of $e^{kx}$, which is the same shape. Differentiating a cosine gives a sine and differentiating a sine gives a cosine, so the pair of them together reproduces the pair. Differentiating a polynomial of degree two gives a polynomial of degree one, and differentiating again gives a constant, so a polynomial trial reproduces a polynomial-shaped result of no higher degree.

In every case the left-hand side of the equation produces the same family of shapes as the trial. Matching the two sides is then a matter of comparing the numbers in front of each shape, which is ordinary algebra. This is why the method is reliable rather than lucky: the shapes are closed under the operation the equation performs.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The adding rule

> **Theorem (adding a natural solution to a forced solution).** If $y_{p}$ satisfies the nonhomogeneous equation and $y_{c}$ satisfies the homogeneous equation, then $y_{c}+y_{p}$ satisfies the nonhomogeneous equation.

In words: adding any natural motion to one working forced motion produces another working forced motion. The reason is visible at once. The equation is built from additions and from multiplications by fixed numbers, and such an equation treats a sum by treating each piece and adding the results. The piece $y_{p}$ supplies the push; the piece $y_{c}$ supplies nothing at all, because the push is zero for it.

Two consequences follow, and both are used constantly.

The first consequence is that there are infinitely many particular integrals. If one is known, adding any natural solution produces another. The general solution therefore records all of them at once through the constants $c_{1}$ and $c_{2}$.

The second consequence is that a wrong particular integral cannot be repaired by adjusting constants. If the forced part does not match the push, no choice of $c_{1}$ and $c_{2}$ will rescue it, because those constants only ever contribute zero to the left-hand side.

### 2.2 The counting property

A second-order equation needs two conditions to pin down one answer, and the general solution must therefore contain exactly two arbitrary constants. In the shape $y=y_{c}+y_{p}$ the count comes entirely from $y_{c}$, since $y_{p}$ carries none. That gives a quick and reliable audit: if a proposed general solution contains one constant or three, it is wrong, whatever else may be right about it.

The rule also explains why the duplicated guess must be multiplied by $x$. Multiplying by $x$ does not introduce a new constant; it changes the shape so that the forced part is no longer a copy of a natural solution. The count of two constants is unaffected, which is exactly what should happen.

### 2.3 The table of trial shapes

The shape of the trial is read off from the shape of the push. The following table covers every case in this course.

| The push $Q(x)$ looks like | The trial for $y_{p}$ looks like | Unknown numbers to find |
| --- | --- | --- |
| a constant, such as $6$ | $A$ | one |
| a linear expression, such as $4x+1$ | $Ax+B$ | two |
| a quadratic, such as $3x^{2}-x$ | $Ax^{2}+Bx+C$ | three |
| an exponential, such as $e^{2x}$ | $Ae^{2x}$ | one |
| a sine or cosine, such as $\cos x$ | $A\cos x+B\sin x$ | two |
| a sum, such as $6+e^{2x}$ | the sum of the two trials | added separately |
| a product, such as $xe^{2x}$ | $(Ax+B)e^{2x}$ | two |

Two entries in that table surprise beginners, so they are worth emphasising. A push that is a cosine alone still requires both a cosine and a sine in the trial, because differentiating a cosine produces a sine, and the equation will generally leave a sine term behind that has to be cancelled. A push that is a product of a polynomial and an exponential keeps the whole polynomial, with one unknown number for every power present.

### 2.4 The rule for a guess that duplicates a natural solution

> **Theorem (multiplying by $x$).** If the trial shape chosen from the table already appears in the complementary function, multiply the trial by $x$. If it still appears, multiply by $x$ again.

The reason is easy to see with a small example. Solve

$$
\frac{d^{2}y}{dx^{2}}-y=e^{x}.
$$

The homogeneous equation has auxiliary equation $m^{2}-1=0$ with roots $1$ and $-1$, so the complementary function is $c_{1}e^{x}+c_{2}e^{-x}$, which already contains $e^{x}$. A trial $Ae^{x}$ is therefore a natural solution, and substituting it into the left-hand side must give zero, never $e^{x}$. The trial is multiplied by $x$, so write $y=Axe^{x}$, and the equation then determines $A$, as Section 4.9 shows in full. The answer turns out to be $y_{p}=\frac{x}{2}e^{x}$.

The number of multiplications equals the number of times the shape is repeated in the complementary function. A simple root needs one factor of $x$; a double root needs two. No other adjustment is ever required.

### 2.5 The checking property

> **Lemma (substitution is decisive).** A proposed particular integral is correct exactly when substituting it into the left-hand side reproduces the push identically.

This lemma turns every answer into something self-marking. There is no need to trust the algebra: substitute, simplify, and compare with the right-hand side. If the comparison fails, the trail of work contains an error, and the comparison usually shows where it is, because a leftover term in the wrong shape points at the wrong trial or at a missing coefficient.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Method: the order of the work

The work is always done in the same order, and the order saves time.

1. Write the equation in the standard form $a_{0}y''+a_{1}y'+a_{2}y=Q(x)$ and read off the three coefficients and the push.
2. Form the auxiliary equation $a_{0}m^{2}+a_{1}m+a_{2}=0$ and find its two roots.
3. Write the complementary function from the roots.
4. Choose the trial shape from the shape of the push, checking whether it duplicates a natural solution.
5. Substitute the trial, compare coefficients, and solve for the unknown numbers.
6. Write $y=y_{c}+y_{p}$ and, if conditions are given, use them to fix $c_{1}$ and $c_{2}$.
7. Check the particular integral by substitution.

Doing step 2 before step 4 is not a formality. The shape of the complementary function decides whether the trial must be multiplied by $x$, so the two steps cannot be interchanged.

### 3.2 Method: the complementary function in three cases

The auxiliary equation is quadratic, so its roots fall into three cases, and the complementary function follows immediately.

Distinct real roots $m_{1}$ and $m_{2}$ give

$$
y_{c}=c_{1}e^{m_{1}x}+c_{2}e^{m_{2}x}.
$$

A repeated root $m$ gives

$$
y_{c}=(c_{1}+c_{2}x)e^{mx}.
$$

Complex roots $\alpha\pm i\beta$ give

$$
y_{c}=e^{\alpha x}\left(c_{1}\cos\beta x+c_{2}\sin\beta x\right).
$$

For example, the equation $y''-4y'+4y=0$ has auxiliary equation $(m-2)^{2}=0$ with the repeated root $2$, so $y_{c}=(c_{1}+c_{2}x)e^{2x}$. The equation $y''+4y=0$ has auxiliary equation $m^{2}+4=0$ with roots $\pm 2i$, so $y_{c}=c_{1}\cos 2x+c_{2}\sin 2x$.

### 3.3 Method: substituting a trial and matching coefficients

Write the trial with unknown letters, differentiate it twice, substitute into the left-hand side, and gather the result into the same shapes as the push. Then compare the number in front of each shape on the two sides.

A small illustration makes the pattern concrete. Solve $y''-y=e^{2x}$. The complementary function is $c_{1}e^{x}+c_{2}e^{-x}$, and the push $e^{2x}$ is not among those shapes, so the trial is $Ae^{2x}$. Its second derivative is $4Ae^{2x}$, its first derivative is $2Ae^{2x}$, and substituting gives

$$
4Ae^{2x}-Ae^{2x}=3Ae^{2x}.
$$

The left-hand side must equal $e^{2x}$, so $3A=1$ and $A=\frac{1}{3}$. The general solution is

$$
y=c_{1}e^{x}+c_{2}e^{-x}+\frac{1}{3}e^{2x}.
$$

### 3.4 Method: multiplying by $x$ when the trial collapses

When the trial duplicates a natural solution, substitution returns zero instead of the push. The remedy is to multiply the whole trial by $x$ and try again, and to repeat if the duplication persists. The method is shown on the equation $y''-y=e^{x}$ in Section 4.9, where the correct trial is $Axe^{x}$ and the coefficient turns out to be $\frac{1}{2}$.

A useful diagnostic: if substitution makes every term cancel and leaves $0$ equal to the push, the trial duplicated a natural solution. If substitution leaves a single unmatched shape, one coefficient is wrong. The two symptoms are different, and telling them apart saves a lot of time.

### 3.5 Method: handling a push with several pieces

When the push is a sum, treat each piece as a separate problem, find a particular integral for each, and add the results. This is legitimate because the equation is linear: the left-hand side applied to a sum is the sum of the left-hand sides applied to the pieces.

For the equation $y''+y=2+e^{2x}$ the natural part is $c_{1}\cos x+c_{2}\sin x$. For the constant piece, try $y=A$ and get $A=2$. For the exponential piece, try $y=Be^{2x}$, substitute, and get $4B+B=5B=1$, so $B=\frac{1}{5}$. The general solution is

$$
y=c_{1}\cos x+c_{2}\sin x+2+\frac{1}{5}e^{2x}.
$$

### 3.6 Method: using the starting information

When initial conditions are supplied, they are applied to the complete solution, never to the particular integral alone. Two conditions are needed, because two constants are waiting to be found.

For the equation $y''-3y'+2y=6$ with $y(0)=2$ and $y'(0)=1$, the general solution is $y=c_{1}e^{x}+c_{2}e^{2x}+3$. The first condition gives $c_{1}+c_{2}+3=2$, so $c_{1}+c_{2}=-1$. The derivative is $y'=c_{1}e^{x}+2c_{2}e^{2x}$, and the second condition gives $c_{1}+2c_{2}=1$. Subtracting the first equation from the second gives $c_{2}=2$, and then $c_{1}=-3$. The solution of the initial value problem is therefore

$$
y=-3e^{x}+2e^{2x}+3 .
$$

The check is quick: at $x=0$ this equals $-3+2+3=2$, and its derivative at $x=0$ is $-3+4=1$, so both conditions hold.

### 3.7 Method: the final check

Every completed example ends with one of two checks, and a student should never skip it. Check the particular integral by substituting it into the nonhomogeneous equation: the result must be the push exactly. Check the constants, when conditions were given, by substituting the two condition values into the finished solution and its derivative.
## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a constant push

Solve $y''-4y=3$.

### 4.2 Solution: a constant trial, then two exponentials

Step 1. Write the homogeneous equation and its auxiliary equation, remembering that the middle coefficient is zero.

$$
m^{2}-4=0
$$

Step 2. Factorise and read off the two roots, which are distinct and real.

$$
(m-2)(m+2)=0, \qquad m=2,\quad m=-2
$$

Step 3. Write the complementary function from the two roots.

$$
y_{c}=c_{1}e^{2x}+c_{2}e^{-2x}
$$

Step 4. The push is the constant $3$, so try the constant $A$. A constant has zero first and second derivatives, so substituting leaves only the $y$ term.

$$
0-4A=3
$$

Step 5. Solve the one unknown number.

$$
A=-\frac{3}{4}
$$

Step 6. Write the general solution and check the forced part. Substituting $y=-\frac{3}{4}$ into the left-hand side gives $-4\cdot\left(-\frac{3}{4}\right)=3$, which is the push.

$$
y=c_{1}e^{2x}+c_{2}e^{-2x}-\frac{3}{4}
$$

### 4.3 Problem: an exponential push

Solve $y''+y=4e^{x}$.

### 4.4 Solution: an exponential trial with one unknown number

Step 1. The auxiliary equation and its roots.

$$
m^{2}+1=0, \qquad m=\pm i
$$

Step 2. Complex roots give a cosine and a sine, with no exponential factor because the real part of the root is zero.

$$
y_{c}=c_{1}\cos x+c_{2}\sin x
$$

Step 3. The push is $4e^{x}$, and $e^{x}$ is not one of the natural shapes, so the trial is $Ae^{x}$. Every derivative of $Ae^{x}$ is $Ae^{x}$, so substitution collects the coefficients.

$$
y_{p}''+y_{p}=Ae^{x}+Ae^{x}=2Ae^{x}
$$

Step 4. Match the number in front of $e^{x}$ on both sides.

$$
2A=4, \qquad A=2
$$

Step 5. Write the general solution and check. With $y=2e^{x}$ the left-hand side is $2e^{x}+2e^{x}=4e^{x}$, which is the push.

$$
y=c_{1}\cos x+c_{2}\sin x+2e^{x}
$$

### 4.5 Problem: a linear push

Solve $y''-y'-2y=4x$.

### 4.6 Solution: a linear trial with two unknown numbers

Step 1. The auxiliary equation factorises with small whole numbers.

$$
m^{2}-m-2=(m-2)(m+1)=0, \qquad m=2,\quad m=-1
$$

Step 2. The complementary function.

$$
y_{c}=c_{1}e^{2x}+c_{2}e^{-x}
$$

Step 3. The push is a linear expression, so the trial must be linear as well, with two unknown numbers. Write $y=Ax+B$, so that the first derivative is $A$ and the second derivative is zero.

$$
0-A-2(Ax+B)=-2Ax-A-2B
$$

Step 4. Compare the coefficient of $x$ on the two sides and then the constant term, giving two equations in the two unknowns.

$$
-2A=4, \qquad -A-2B=0
$$

Step 5. Solve the pair. The first equation gives $A=-2$; substituting into the second gives $2-2B=0$, so $B=1$.

$$
A=-2, \qquad B=1
$$

Step 6. Write the general solution and check. For $y=-2x+1$ the derivatives are $-2$ and $0$, and the left-hand side is $0+2-2(-2x+1)=4x$, which is the push.

$$
y=c_{1}e^{2x}+c_{2}e^{-x}-2x+1
$$

### 4.7 Problem: a cosine push

Solve $y''+4y=\cos x$.

### 4.8 Solution: a cosine trial that also carries a sine

Step 1. The auxiliary equation and its complex roots.

$$
m^{2}+4=0, \qquad m=\pm 2i
$$

Step 2. The complementary function uses the frequency two, not the frequency one of the push.

$$
y_{c}=c_{1}\cos 2x+c_{2}\sin 2x
$$

Step 3. The push has frequency one, which does not match the natural frequency, so no multiplication by $x$ is needed. The trial carries both a cosine and a sine, because differentiating one produces the other. Write $y=A\cos x+B\sin x$, so that the second derivative is $-A\cos x-B\sin x$.

$$
-A\cos x-B\sin x+4A\cos x+4B\sin x=3A\cos x+3B\sin x
$$

Step 4. Match the cosine coefficient to one and the sine coefficient to zero.

$$
3A=1, \qquad 3B=0
$$

Step 5. Solve for the two numbers.

$$
A=\frac{1}{3}, \qquad B=0
$$

Step 6. The sine coefficient vanishing is a genuine result, not a mistake: this particular push happens to need no sine. Write the general solution and check by substitution, which returns $\cos x$.

$$
y=c_{1}\cos 2x+c_{2}\sin 2x+\frac{1}{3}\cos x
$$

### 4.9 Problem: a push that repeats a natural solution

Solve $y''-y=e^{x}$.

### 4.10 Solution: multiply the trial by $x$

Step 1. The auxiliary equation and its roots, which are one and minus one.

$$
m^{2}-1=0, \qquad m=1,\quad m=-1
$$

Step 2. The complementary function already contains $e^{x}$, so a trial $Ae^{x}$ would give zero on the left-hand side.

$$
y_{c}=c_{1}e^{x}+c_{2}e^{-x}
$$

Step 3. Multiply the trial by $x$ and differentiate carefully, using the product rule. The first derivative is $A(1+x)e^{x}$ and the second is $A(2+x)e^{x}$.

$$
y=Axe^{x}, \qquad y'=A(1+x)e^{x}, \qquad y''=A(2+x)e^{x}
$$

Step 4. Substitute into the left-hand side. The two copies of $Axe^{x}$ cancel, and only the extra exponential survives.

$$
A(2+x)e^{x}-Axe^{x}=2Ae^{x}
$$

Step 5. Match with the push.

$$
2A=1, \qquad A=\frac{1}{2}
$$

Step 6. Write the general solution and check. Substituting $y=\frac{x}{2}e^{x}$ gives $\frac{1}{2}(2+x)e^{x}-\frac{x}{2}e^{x}=e^{x}$, which is the push.

$$
y=c_{1}e^{x}+c_{2}e^{-x}+\frac{x}{2}e^{x}
$$

### 4.11 Problem: a push with starting information

Solve $y''-3y'+2y=6$ subject to $y(0)=2$ and $y'(0)=1$.

### 4.12 Solution: complete the general solution first, then fit the constants

Step 1. The auxiliary equation and its roots.

$$
m^{2}-3m+2=(m-1)(m-2)=0, \qquad m=1,\quad m=2
$$

Step 2. The complementary function.

$$
y_{c}=c_{1}e^{x}+c_{2}e^{2x}
$$

Step 3. The push is the constant six, so the trial is the constant $A$, and substitution gives $2A=6$.

$$
y_{p}=3
$$

Step 4. Assemble the complete solution before using any condition. Applying a condition to the forced part alone is the commonest error at this stage.

$$
y=c_{1}e^{x}+c_{2}e^{2x}+3
$$

Step 5. Differentiate the complete solution, because the second condition involves the derivative.

$$
y'=c_{1}e^{x}+2c_{2}e^{2x}
$$

Step 6. Impose the first condition at $x=0$ and then the second.

$$
c_{1}+c_{2}+3=2, \qquad c_{1}+2c_{2}=1
$$

Step 7. Subtract the first equation from the second to get $c_{2}=2$, and then $c_{1}=-3$.

$$
c_{1}=-3, \qquad c_{2}=2
$$

Step 8. Write the answer and verify both conditions. At $x=0$ the value is $-3+2+3=2$, and the derivative there is $-3+4=1$, so both conditions hold.

$$
y=-3e^{x}+2e^{2x}+3
$$

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Beginner misconceptions to unlearn

The following mistakes appear in almost every first attempt at this topic. Each is paired with the correction that removes it.

- Adding the particular integral twice. The complementary function already contains every natural motion, so the forced part is added once and then absorbed into the family through the constants.
- Applying the initial conditions to $y_{p}$ alone. The conditions describe the whole answer, so they must be imposed after $y_{c}$ and $y_{p}$ have been added.
- Forgetting the sine when the push is a cosine. Differentiating a cosine produces a sine, so the sine term is needed to absorb what differentiation leaves behind.
- Keeping only the exponential when the push is $xe^{2x}$. The product rule creates a term without $x$, so the trial needs the full expression $(Ax+B)e^{2x}$.
- Multiplying by $x$ when there is no duplication. Extra factors of $x$ create shapes that the left-hand side cannot cancel, and the coefficients then have no solution.
- Treating the constants $c_{1}$ and $c_{2}$ as part of the particular integral. A particular integral carries no arbitrary constants at all.
- Checking nothing. A substitution check takes under a minute and catches almost every algebraic slip, including sign errors in the trial.
- Believing that the method guesses the answer. It guesses only the shape; the numbers are computed exactly by matching coefficients.

### 5.2 What this method cannot do

The method of undetermined coefficients works because the standard shapes reproduce themselves under differentiation. That is a real restriction. A push such as $\tan x$, $\sec x$, $\ln x$ or $\frac{1}{x}$ does not reproduce its own shape, and no finite combination of the shapes in the table can match it. Such equations are handled by a different technique, in which the constants in the complementary function are allowed to vary, and the resulting integrals are usually not elementary.

Even inside the standard catalogue there is a limit of a different kind. If the push is a product of a polynomial and a trigonometric function, the trial must carry a full polynomial multiplying both the cosine and the sine, and the algebra grows quickly. The method still works, but the arithmetic becomes the main difficulty rather than the idea.

### 5.3 Extensions worth knowing about

Three extensions follow naturally from what has been built here.

The first is the interpretation of the duplication case. When the push has the same frequency or the same exponential rate as a natural solution, the response grows without bound as $x$ increases. This is the mathematical statement of resonance, and it is why a swing pushed in time with its own rhythm swings higher and higher. The growing factor $x$ in the particular integral is the mark of resonance on the page.

The second is the extension to higher order. An equation of order three needs three natural solutions and hence three arbitrary constants, and the same logic applies: find the natural part, find one forced part, add them. The trial table is unchanged; only the number of times a duplication may need multiplying by $x$ can increase.

The third is the extension to equations whose coefficients are not constant. There the natural solutions are usually not exponentials, the trial table no longer applies in its simple form, and the method of undetermined coefficients must be replaced. The structure $y=y_{c}+y_{p}$, however, survives every one of these changes, because it depends only on linearity.

### 5.4 The five-line summary

Every problem in this topic is answered in five lines. State the standard form and identify the push. Solve the auxiliary equation and write the complementary function with two constants. Choose the trial shape from the shape of the push, multiplying by $x$ if the shape already appears among the natural solutions. Substitute, match coefficients, and record the particular integral. Add the two parts, impose any conditions, and check by substitution.

### 5.5 A last look at the swing

Return to the swing. The natural sway dies away, and the pushed motion remains. In the language of this note, the complementary function is the part that fades, and the particular integral is the steady response that the pushes maintain. When the pushing matches the natural rhythm, the response no longer settles but grows, and the factor of $x$ records that growth. The whole theory of this topic is a precise version of that one observation, and the algebra of undetermined coefficients is simply the bookkeeping that makes the observation exact.
### 4.13 Problem: a push that is a product

Solve $y''+y=xe^{x}$.

### 4.14 Solution: keep the whole product in the trial

Step 1. The auxiliary equation and its roots.

$$
m^{2}+1=0, \qquad m=\pm i
$$

Step 2. The complementary function.

$$
y_{c}=c_{1}\cos x+c_{2}\sin x
$$

Step 3. The push is a product of a linear expression and an exponential. Because of the product rule, a trial with only $Ax$ would create a term with no $x$ at all, so the trial must be the whole product with two unknown numbers. Write $y=(Ax+B)e^{x}$ and differentiate twice.

$$
y'=(Ax+A+B)e^{x}, \qquad y''=(Ax+2A+B)e^{x}
$$

Step 4. Substitute into the left-hand side and gather the result into a multiple of $e^{x}$ with a linear factor.

$$
(Ax+2A+B)e^{x}+(Ax+B)e^{x}=\left(2Ax+2A+2B\right)e^{x}
$$

Step 5. Compare with $xe^{x}$: the coefficient of $x$ must be one and the constant term must be zero.

$$
2A=1, \qquad 2A+2B=0
$$

Step 6. Solve the pair, which gives $A=\frac{1}{2}$ and then $B=-\frac{1}{2}$.

$$
A=\frac{1}{2}, \qquad B=-\frac{1}{2}
$$

Step 7. Write the general solution. The check substitutes $y=\frac{1}{2}(x-1)e^{x}$ and returns $xe^{x}$, so the forced part is correct.

$$
y=c_{1}\cos x+c_{2}\sin x+\frac{1}{2}(x-1)e^{x}
$$

### 4.15 Problem: a push that repeats a natural solution with a different number

Solve $y''+3y'+2y=4e^{-x}$.

### 4.16 Solution: one factor of $x$ is enough for a simple root

Step 1. The auxiliary equation and its roots.

$$
m^{2}+3m+2=(m+1)(m+2)=0, \qquad m=-1,\quad m=-2
$$

Step 2. The complementary function contains $e^{-x}$, so a trial $Ae^{-x}$ would vanish under the left-hand side.

$$
y_{c}=c_{1}e^{-x}+c_{2}e^{-2x}
$$

Step 3. Multiply by $x$ and differentiate, taking care with the signs that the minus sign in the exponent produces.

$$
y=Axe^{-x}, \qquad y'=A(1-x)e^{-x}, \qquad y''=A(x-2)e^{-x}
$$

Step 4. Substitute and collect. The terms in $x$ cancel in pairs and a single exponential is left over.

$$
A\left[(x-2)+3(1-x)+2x\right]e^{-x}=Ae^{-x}
$$

Step 5. Match with $4e^{-x}$.

$$
A=4
$$

Step 6. Write the general solution and check. Substituting $y=4xe^{-x}$ returns $4e^{-x}$, which is the push, so the forced part is correct.

$$
y=c_{1}e^{-x}+c_{2}e^{-2x}+4xe^{-x}
$$

### 4.17 Problem: a push that repeats a natural solution twice over

Solve $y''-2y'+y=e^{x}$.

### 4.18 Solution: multiply by $x$ twice

Step 1. The auxiliary equation is a perfect square, so the two roots coincide.

$$
m^{2}-2m+1=(m-1)^{2}=0, \qquad m=1
$$

Step 2. A repeated root puts a factor of $x$ into the complementary function itself.

$$
y_{c}=(c_{1}+c_{2}x)e^{x}
$$

Step 3. The trial $Ae^{x}$ duplicates a natural solution, so multiply by $x$; but $xe^{x}$ is also a natural solution, so multiply by $x$ again. The trial is therefore $Ax^{2}e^{x}$.

$$
y=Ax^{2}e^{x}, \qquad y'=A\left(2x+x^{2}\right)e^{x}, \qquad y''=A\left(2+4x+x^{2}\right)e^{x}
$$

Step 4. Substitute and collect. Everything in $x$ and everything in $x^{2}$ cancels, leaving a constant multiple of $e^{x}$.

$$
A\left[(2+4x+x^{2})-(4x+2x^{2})+x^{2}\right]e^{x}=2Ae^{x}
$$

Step 5. Match with $e^{x}$.

$$
2A=1, \qquad A=\frac{1}{2}
$$

Step 6. Write the general solution and check. Substituting $y=\frac{1}{2}x^{2}e^{x}$ returns $e^{x}$, so the forced part is correct.

$$
y=(c_{1}+c_{2}x)e^{x}+\frac{1}{2}x^{2}e^{x}
$$

### 5.6 How to read a finished answer

A finished answer to a nonhomogeneous problem has a very characteristic appearance, and learning to read it is worth as much as learning to produce it.

Every answer contains a group of terms with letters such as $c_{1}$ and $c_{2}$ in front of them. That group is the complementary function. Every answer also contains a group of terms with no letters in front of them at all, or with numbers only, and that group is the particular integral. If two groups cannot be distinguished, something has gone wrong, most often because a constant was left undetermined inside the forced part.

The complementary function always has the same shapes as the roots of the auxiliary equation. Two distinct real roots give two exponentials; a double root gives an exponential multiplied by a linear expression; complex roots give a cosine and a sine, possibly with an exponential factor. The forced part, by contrast, has the shape of the push, altered only by a possible factor of $x$. Comparing the two groups in a finished answer is therefore a quick test of both.

A numerical example makes the reading concrete. The answer

$$
y=c_{1}e^{x}+c_{2}e^{2x}+3
$$

carries the natural group $c_{1}e^{x}+c_{2}e^{2x}$, which matches the roots one and two, and the forced group $3$, which matches a constant push. If the question had asked for the equation and the push, both could be recovered from the answer: the roots give the auxiliary equation $(m-1)(m-2)=0$, hence $y''-3y'+2y=Q(x)$, and the forced group $3$ gives $Q(x)=2\cdot 3=6$.

### 5.7 Where the two parts appear in a real system

The two parts of the answer are not an algebraic curiosity. They describe two genuinely different physical effects, and the names used by engineers reflect that.

The complementary function is often called the transient part. In a mechanical system it describes the vibration that the system makes on its own; friction and damping eventually remove it, so it matters only for a short time after the motion starts. In an electrical circuit it describes the current that flows while the components exchange energy among themselves; resistance eventually turns that energy into heat.

The particular integral is often called the steady state part. It describes the response that the outside supply maintains for as long as the supply continues. In the swing picture this is the steady motion caused by regular pushes; in the bath picture it is the level that the running tap eventually holds.

The initial conditions decide how much of the transient is present, and nothing else. Since the forced part is fixed by the push, the constants $c_{1}$ and $c_{2}$ can only adjust the natural part. That is why two different starting positions of the same swing, pushed in the same regular way, settle into the same steady motion after a while but differ at the beginning.

There is one important exception, and it is the duplication case. When the push has exactly the natural rhythm, the forced part is not steady at all: it grows in proportion to $x$. Physically the pushes then add energy in step with the motion already present, and the amplitude climbs without limit until some effect outside the model intervenes. The factor of $x$ in the particular integral is the algebraic trace of that unbounded growth, and recognising it is the reason the duplication case is treated as a separate rule rather than as an accident.

### 5.8 Questions to ask yourself before moving on

Four questions catch almost every error in this topic. What are the two roots of the auxiliary equation, and have I written the complementary function in the correct one of the three forms? What is the shape of the push, and does my trial reproduce that shape after two differentiations? Does my trial duplicate a natural solution, and if so have I multiplied by $x$ exactly as many times as the duplication requires? Do my two conditions give two independent equations, and have I checked the finished answer by substitution?

A student who can answer those four questions has understood the topic. The algebra that follows is routine, and the method never fails inside the catalogue of shapes treated here.
