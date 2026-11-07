## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A workshop that answers with shapes

Imagine a workshop bench with a machine on it. You feed one signal into the machine and one reply comes out. The machine is not clever. At every instant it measures three things about the signal it was given: the size of the signal, the speed at which that size is changing, and the speed at which that speed is itself changing. It then mixes the three measurements in fixed proportions, set once by three dials that never move.

Suppose the three dials are set to one, minus three and two. Feed in a signal that doubles every second, and the reply is also a signal that doubles every second, with a different size. Feed in a wave that rises and falls evenly, and the reply is a wave with exactly the same rhythm, again with a different size. Feed in a ramp, and the reply is a ramp, possibly tilted and possibly shifted up or down. The machine never invents a new shape. It answers in the vocabulary of whatever it is handed.

Think of the body of a guitar. Strike a string and the body returns a sound at the pitch of that string. The body changes the loudness and the colour of the note, but the pitch comes from the input, never from the wood. The machine on the bench behaves in the same way, and this one observation is what makes the whole of this topic short: to predict the reply, look at the shape of the input and then work out a single number, or a couple of numbers, that fix the size.

Picture a child on a swing. Push once and the swing rocks at its own natural rhythm and slowly settles. Push again and again in time with that natural rhythm, and something different happens: the swing goes higher on each push, and the size of the motion grows in proportion to the number of pushes, that is, in proportion to time. That is the second idea of the topic. When the input already matches the machine's natural rhythm, the ordinary reply is not available, and the reply grows by a factor of the input variable instead.

The mathematical name for the machine is a linear differential operator with constant coefficients, and the name for the reply is a particular integral. The rest of this section gives every symbol a plain meaning.

### 1.2 The letters on the machine

The input variable is written $x$ and stands for the independent quantity, usually time or distance along an axis. The unknown function is written $y$, and it stands for the rule that assigns a number to every $x$; in the workshop language, $y$ is the reply.

The first derivative $\frac{dy}{dx}$ is the speed at which the reply changes as $x$ changes. The second derivative $\frac{d^{2}y}{dx^{2}}$ is the rate at which that speed changes. The symbol $D$ is a shorthand for the instruction differentiate once. So $Dy$ means $\frac{dy}{dx}$, and $D^{2}y$ means $\frac{d^{2}y}{dx^{2}}$.

A machine with fixed dials is written as a polynomial in $D$. With dials one, minus three and two the machine is

$$
D^{2}-3D+2 .
$$

The instruction $D^{2}-3D+2$ means: differentiate twice, subtract three times the first derivative, and add twice the function. Written in the older notation the same instruction is

$$
\frac{d^{2}y}{dx^{2}}-3\frac{dy}{dx}+2y .
$$

An equation is a statement that the machine's reply equals a prescribed input. If the prescribed input is written $Q$, the equation reads

$$
\left(D^{2}-3D+2\right)y=Q .
$$

The letter $Q$ stands for the driving term, the signal fed in. Everything in this topic is about one question: given the machine and given $Q$, produce one reply $y$ that makes the statement true.

### 1.3 Two questions, and the two halves of the answer

There are two questions a machine can be asked, and they are different.

The first question is which inputs make the machine answer zero. Those inputs are called the complementary function, and for a machine of order two there are always exactly two basic ones, so the full answer is a blend of two with two free numbers in it. With dials one, minus three and two the two basic zero-answer signals are the one that grows like $e^{2x}$ and the one that grows like $e^{x}$, so the blend is $c_{1}e^{2x}+c_{2}e^{x}$ where $c_{1}$ and $c_{2}$ are free numbers.

The second question is which input makes the machine answer a prescribed signal $Q$. Any single reply that works is called a particular integral.

The two questions fit together because the machine is linear: if a signal produces the answer zero, adding it to a signal that produces $Q$ changes nothing about the $Q$. Hence every solution of the equation is a particular integral plus the whole zero-answer family. In symbols,

$$
y=\text{complementary function}+\text{particular integral}.
$$

The complementary function is found from the roots of the dial polynomial, which is a separate calculation of its own. This note is about the second half only: how to manufacture one reply quickly when $Q$ has one of five standard shapes.

### 1.4 The inverse operator

Dividing by the machine is the natural way to write the reply. If the machine instruction is written $f(D)$, then the equation is $f(D)y=Q$, and the reply is written

$$
y=\frac{Q}{f(D)} .
$$

The symbol $\frac{1}{f(D)}$ is not an ordinary fraction. It is an instruction meaning find a function that the machine turns into $Q$. It is called the inverse operator. Two facts about it matter.

First, the instruction is only defined up to a zero-answer signal. If $y$ is a reply to $Q$ and $z$ makes the machine answer zero, then $y+z$ is also a reply to $Q$. This is why the word particular is used: an inverse operator delivers one reply out of infinitely many, and any one will do.

Second, the instruction can often be carried out without any integration at all. If $Q$ is an exponential, a wave, a power of $x$, an exponential multiplied by a function, or $x$ multiplied by a function, then the reply can be written down by substitution and algebra. These five shortcuts are the short methods.

### 1.5 The five shapes worth knowing

Only five shapes of driving term are needed, and each has its own shortcut.

The first shape is the pure exponential $e^{ax}$, where $a$ is a fixed number and $e$ is the number about two and seven tenths. The second shape is a wave, either $\sin(ax+b)$ or $\cos(ax+b)$, where $a$ fixes how fast the wave repeats and $b$ fixes where it starts. The third shape is a power of the input, $x^{n}$, with $n$ a whole number such as one, two or three. The fourth shape is an exponential multiplied by any function, written $e^{ax}u$ with $u$ standing for the function. The fifth shape is the input variable multiplied by any function, written $xu$.

Every one of the five is handled by the same three-part strategy: identify which shape you have, apply the matching rule, and check the answer by putting it back into the machine. The check is not optional, because the rules are easy to apply with one sign wrong.

### 1.6 A first reply computed in full

Take the machine with dials one, minus three and two and feed in the exponential $e^{3x}$. The equation is

$$
\left(D^{2}-3D+2\right)y=e^{3x} .
$$

The rule for an exponential says: evaluate the dial polynomial at the number in the exponent, and divide the input by the result. At the number three the polynomial gives nine minus nine plus two, which is two. So the reply is

$$
y=\frac{e^{3x}}{2} .
$$

The check is a substitution. Differentiating once multiplies by three and differentiating twice multiplies by nine, so the machine sees

$$
\frac{9e^{3x}}{2}-\frac{3\cdot 3e^{3x}}{2}+\frac{2e^{3x}}{2}=\frac{e^{3x}}{2}\left(9-9+2\right)=e^{3x} .
$$

The reply is correct. Notice what happened: no integration was performed, and the shape of the input reappeared unchanged in the answer. The only work was arithmetic with the number three.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The exponential rule

> **Theorem 1 (exponential input).** If $Q=e^{ax}$ and the number $a$ is not a root of the dial polynomial, so that $f(a)\neq 0$, then a particular integral is $y=\frac{e^{ax}}{f(a)}$.

In words: put the number from the exponent into the dial polynomial, and divide. The hypothesis matters. It says the exponent's number must not already be one of the numbers that make the machine answer zero. When it is, the rule has no value to divide by, and the swing effect of Section 1.1 takes over.

A second example uses three dials. With the machine $(D+2)(D+3)(D-4)$ and input $e^{5x}$, the number five gives seven, eight and one, whose product is fifty-six, so the reply is $e^{5x}$ divided by fifty-six.

### 2.2 The wave rule

> **Theorem 2 (wave input).** If $Q=\sin(ax+b)$ or $Q=\cos(ax+b)$, and if the dial polynomial, after every occurrence of $D^{2}$ is replaced by $-a^{2}$, is a non-zero number, then a particular integral is that same wave divided by that number.

The recipe is often written as a single instruction: replace $D^{2}$ by $-a^{2}$. The sign is the whole content of the rule. Differentiating a wave twice returns the wave multiplied by minus the square of its rate, so $D^{2}$ acting on a wave of rate $a$ is the same as multiplying by $-a^{2}$. Replacing $D^{2}$ by $+a^{2}$ is the single most common mistake in the topic.

A small instance: with the machine $D^{2}+9$ and input $\sin 2x$, the rate is two, so $D^{2}$ becomes $-4$, the polynomial becomes $-4+9=5$, and the reply is $\frac{\sin 2x}{5}$. Check it by differentiating twice: the second derivative of the reply is $-4$ times the reply, so the machine sees $-4$ parts plus nine parts, that is five parts, of the reply, and five parts of one fifth of the input is the input.

### 2.3 The power rule

> **Theorem 3 (power input).** If $Q=x^{n}$, and if the dial polynomial has a non-zero constant term, then a particular integral is found by expanding $\frac{1}{f(D)}$ in ascending powers of $D$ and applying the result to $x^{n}$, stopping at the power $D^{n}$.

Ascending powers means the expansion proceeds one derivative at a time, like a series that starts with the number one. The reason stopping is legitimate is that the $(n+1)$-th derivative of $x^{n}$ is zero, so every later term contributes nothing at all.

A small instance: with the machine $D^{2}+1$ and input $x^{2}$, the inverse instruction is $\frac{1}{1+D^{2}}$, and the expansion of $\frac{1}{1+t}$ in ascending powers of $t$ is one minus $t$ plus $t$ squared and so on. Replacing $t$ by $D^{2}$ gives one minus $D^{2}$ plus $D^{4}$ and so on. Applied to $x^{2}$ the first term gives $x^{2}$, the second gives minus two, and every later term gives zero. So the reply is

$$
y=x^{2}-2 .
$$

The check: differentiating $x^{2}-2$ twice gives two, and two plus the function itself is two plus $x^{2}$ minus two, which is $x^{2}$.

### 2.4 The exponential shift rule

> **Theorem 4 (exponential multiplied by a function).** If $Q=e^{ax}u$, where $u$ is any function of $x$, then a particular integral is $y=e^{ax}$ multiplied by a particular integral of $u$ with the machine's dials shifted by $a$.

The shift means every $D$ in the dial polynomial is replaced by $D+a$. So the rule reads

$$
\frac{e^{ax}u}{f(D)}=e^{ax}\frac{u}{f(D+a)} .
$$

The exponential passes straight through the machine and leaves a new machine behind it, whose dials have all been moved up by the number $a$. The remaining problem is a smaller one, with the same five shortcuts available.

A small instance: with the machine $D-1$ and input $xe^{2x}$, the dial is shifted from $D-1$ to $D+2-1$, which is $D+1$. The remaining problem asks for a particular integral of $x$ under the machine $D+1$, and the power rule gives $x-1$. So the reply is $e^{2x}(x-1)$.

### 2.5 The multiplier rule

> **Theorem 5 (input multiplied by the variable).** If $Q=xu$, where $u$ is any function of $x$, then a particular integral is $x$ times a particular integral of $u$, minus a correction term built from the derivative of the dial polynomial.

Written out, the rule is

$$
\frac{xu}{f(D)}=x\frac{u}{f(D)}-\frac{f'(D)}{\left[f(D)\right]^{2}}u .
$$

Here $f'(D)$ means the derivative of the dial polynomial taken with respect to $D$ and then read as an instruction; for the machine $D^{2}-1$ it is $2D$. The correction term is what pays for the product rule: multiplying by $x$ creates an extra derivative at every stage, and the second term cancels it.

A small instance: with the machine $D^{2}-1$ and input $xe^{2x}$, the number two is not a root because four minus one is three. The first piece is $x$ times $e^{2x}$ over three. The correction is $2D$ applied to $e^{2x}$, which is $4e^{2x}$, divided by three squared, which is nine. So

$$
y=\frac{xe^{2x}}{3}-\frac{4e^{2x}}{9} .
$$

### 2.6 What happens when a rule refuses

Each of the first three rules carries a condition, and each condition can fail. When the exponential rule fails, the number in the exponent is a root of the dial polynomial, which means the input duplicates part of the zero-answer family. When the wave rule fails, the rate of the wave corresponds to a root, and again the input duplicates part of that family. When the power rule fails, the constant term of the dial polynomial is zero, so the machine has a factor of $D$ and cannot be inverted on polynomials directly.

In each of the first two failures the remedy is the swing: multiply the input by $x$, divide by the derivative of the dial polynomial evaluated in the same way, and if the derivative is also zero, multiply by $x$ again and divide by the second derivative. In the third failure the remedy is to divide out the factor of $D$ and integrate the result as many times as that factor required.

### 2.7 Sums of inputs

> **Theorem (superposition over the input).** If $y_{1}$ is a particular integral for the input $Q_{1}$ and $y_{2}$ is a particular integral for the input $Q_{2}$, then $y_{1}+y_{2}$ is a particular integral for the input $Q_{1}+Q_{2}$.

The proof is one line. The machine is linear, so applying it to a sum applies it to each piece and adds the results. Each piece is turned into its own input, and the two inputs add to the prescribed total.

The practical consequence is that a driving term made of several shapes is handled one shape at a time, with no interaction between the pieces. A sum of an exponential, a wave and a power is answered by adding three separate replies, and each reply is checked separately if the examiner asks for a full verification. Mixing the pieces, for instance by trying to shift the dials by the rate of one shape while the input contains a power, is a reliable way to lose marks.

The theorem also explains why the general solution looks the way it does. The complementary function is a particular integral for the input zero, and the particular integral is a particular integral for the input $Q$; adding them gives a particular integral for the input zero plus $Q$, which is $Q$. The two halves are not two competing answers but two pieces of one answer.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Why the exponential rule is true

The whole proof is one line of differentiation. Differentiating an exponential multiplies it by the number in the exponent, and doing so twice multiplies by the square of that number. So for any whole number $k$,

$$
D^{k}e^{ax}=a^{k}e^{ax} .
$$

Every term of the dial polynomial therefore returns the same exponential, multiplied by the corresponding power of $a$. Adding the terms gives

$$
f(D)e^{ax}=f(a)e^{ax} .
$$

Dividing both sides by the non-zero number $f(a)$ shows that the function $\frac{e^{ax}}{f(a)}$ is turned into $e^{ax}$ by the machine, which is exactly what a particular integral must be. If $f(a)$ is zero, the division is impossible and the proof says nothing, which is why the hypothesis cannot be dropped.

### 3.2 Why the wave rule is true

Differentiating a wave twice returns the same wave multiplied by minus the square of its rate. For the sine,

$$
D^{2}\sin(ax+b)=-a^{2}\sin(ax+b),
$$

and the same identity holds for the cosine. So anywhere a $D^{2}$ appears it may be replaced by the number $-a^{2}$, and the machine acts on the wave exactly as multiplication by the number obtained from the dial polynomial.

If the dial polynomial contains only even powers of $D$, that replacement finishes the job, because the whole instruction has collapsed to a single number. If a plain $D$ survives, the replacement is still valid but leaves a first-order instruction, and one further step is needed to turn it into a number. That step is developed in the next level.

### 3.3 Why the ascending expansion is true

Write the dial polynomial with the number last as $f(D)=a+bD+cD^{2}$, where $a$ is the constant term and is not zero. Factoring out that constant term gives

$$
f(D)=a\left(1+\frac{b}{a}D+\frac{c}{a}D^{2}\right).
$$

The bracket is a number plus a small instruction, and the expansion $\frac{1}{1+t}=1-t+t^{2}-\cdots$ may be applied with $t$ standing for the instruction. The result is a series in powers of $D$. Applying the series to $x^{n}$ kills every power of $D$ beyond the $n$-th, since the $(n+1)$-th derivative of a polynomial of degree $n$ is zero. What remains is a finite sum of derivatives, and the reply is a polynomial of the same degree. Dividing by the constant term at the end produces the answer.

### 3.4 The method in five steps

Every question in this topic is answered by the same five steps.

Step 1. Write the equation in operator form, with the machine collected as a polynomial in $D$.

Step 2. Find the complementary function from the roots of the dial polynomial, so that the count of free numbers matches the order.

Step 3. Identify the shape of $Q$ and check the condition attached to the matching rule.

Step 4. Apply the rule, using the failure remedy if the condition is not met, and add the pieces if $Q$ is a sum of several shapes.

Step 5. Add the particular integral to the complementary function and check by substitution.

### 3.5 The method for a wave with a plain derivative term

When the dial polynomial has an odd part, the replacement of $D^{2}$ by $-a^{2}$ leaves an instruction of the form a number plus a multiple of $D$. That instruction is cleared by multiplying above and below by its companion, in which the sign of the $D$ term is reversed. The product below becomes a number, because the $D^{2}$ in it is again replaced by $-a^{2}$, and the numerator is a combination of a sine and a cosine.

The summary of the five rules, with the condition attached to each, is the following table.

| Shape of the input | Condition to check | Particular integral |
| --- | --- | --- |
| $e^{ax}$ | $f(a)\neq 0$ | $e^{ax}$ divided by $f(a)$ |
| $\sin(ax+b)$ or $\cos(ax+b)$ | $f(-a^{2})\neq 0$ | the same wave divided by $f(-a^{2})$ |
| $x^{n}$ | constant term of $f$ not zero | expand in ascending powers of $D$ to $D^{n}$ |
| $e^{ax}u$ | none | $e^{ax}$ times the reply for $u$ with dials shifted by $a$ |
| $xu$ | none | $x$ times the reply for $u$, minus a correction |

### 3.6 The method for checking a reply

A particular integral is checked by substitution, and the substitution should be done in a fixed order so that nothing is skipped.

First, differentiate the claimed reply exactly as many times as the machine's order requires. Second, form the combination prescribed by the dials, keeping each term in its own line of working. Third, collect the coefficients of the distinct pieces, such as the exponential and the exponential multiplied by $x$, and confirm that the coefficient of each piece matches the input. Fourth, confirm that any piece which does not appear in the input has coefficient zero; a leftover piece means the complementary function has been mixed into the particular integral, which is harmless only when it is a genuine zero-answer function.

The check is worth more than it costs, because the five rules have only three places where mistakes concentrate: a sign in the wave rule, a missing factor in the failure case, and an omitted correction in the multiplier rule. A substitution finds all three immediately, whereas re-reading the working usually does not.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: an exponential input with a clean evaluation

Solve $\left(D^{2}-3D+2\right)y=e^{3x}$.

### 4.2 Solution: evaluate the dial polynomial at three

Step 1. Write the dial polynomial and evaluate it at the number in the exponent.

$$
f(D)=D^{2}-3D+2, \qquad f(3)=9-9+2=2 .
$$

Step 2. Divide the input by that value, since the condition $f(3)\neq 0$ holds.

$$
y_{p}=\frac{e^{3x}}{2}
$$

Step 3. Find the complementary function. The dial polynomial factors as $(D-1)(D-2)$, so the roots are one and two.

$$
y_{c}=c_{1}e^{x}+c_{2}e^{2x}
$$

Step 4. Add the two halves, because the machine is linear.

$$
y=c_{1}e^{x}+c_{2}e^{2x}+\frac{e^{3x}}{2}
$$

Step 5. Check the particular integral by substitution.

$$
\frac{9e^{3x}}{2}-3\cdot\frac{3e^{3x}}{2}+2\cdot\frac{e^{3x}}{2}=\frac{e^{3x}}{2}\left(9-9+2\right)=e^{3x}
$$

The check succeeds, and the answer carries exactly two free numbers, matching the order two.

### 4.3 Problem: a wave input

Solve $\left(D^{2}+9\right)y=\sin 2x$.

### 4.4 Solution: replace $D^{2}$ by minus four

Step 1. Note the rate of the wave and replace $D^{2}$ by the negative square of that rate.

$$
D^{2}\to -4
$$

Step 2. Evaluate the collapsed dial polynomial.

$$
-4+9=5
$$

Step 3. Divide the wave by that number, since it is not zero.

$$
y_{p}=\frac{\sin 2x}{5}
$$

Step 4. Write the complementary function, whose roots are the two imaginary numbers that make $D^{2}+9$ vanish, giving waves of rate three.

$$
y_{c}=c_{1}\cos 3x+c_{2}\sin 3x
$$

Step 5. State the general solution and check the particular integral by differentiating twice.

$$
y=c_{1}\cos 3x+c_{2}\sin 3x+\frac{\sin 2x}{5}
$$

The second derivative of the particular integral is $-4$ times itself, so the machine returns five fifths of the input, which is the input.

### 4.5 Problem: a power input under a first-order machine

Solve $\left(D+1\right)y=x^{2}$.

### 4.6 Solution: expand in ascending powers

Step 1. Rewrite the inverse instruction by factoring out the constant term, which is one.

$$
\frac{1}{1+D}=\left(1+D\right)^{-1}
$$

Step 2. Expand in ascending powers of $D$, keeping terms up to $D^{2}$ because the input is a square.

$$
\left(1+D\right)^{-1}=1-D+D^{2}-\cdots
$$

Step 3. Apply the truncated series to the input, differentiating as each power requires.

$$
y_{p}=x^{2}-\frac{d}{dx}\left(x^{2}\right)+\frac{d^{2}}{dx^{2}}\left(x^{2}\right)=x^{2}-2x+2
$$

Step 4. Add the complementary function, which is a single exponential since the order is one.

$$
y=c_{1}e^{-x}+x^{2}-2x+2
$$

Step 5. Check by substitution.

$$
\frac{d}{dx}\left(x^{2}-2x+2\right)+\left(x^{2}-2x+2\right)=\left(2x-2\right)+\left(x^{2}-2x+2\right)=x^{2}
$$

The check succeeds. Notice that the reply is a polynomial of the same degree as the input, tilted once and shifted once, exactly as the workshop picture predicted.

### 4.7 Problem: an exponential multiplied by the variable, first order

Solve $\left(D-1\right)y=xe^{2x}$.

### 4.8 Solution: shift the dials by two

Step 1. Apply the shift rule, moving every $D$ to $D+2$.

$$
\frac{xe^{2x}}{D-1}=e^{2x}\frac{x}{D+2-1}=e^{2x}\frac{x}{D+1}
$$

Step 2. Expand the remaining instruction in ascending powers and apply it to $x$.

$$
\frac{1}{1+D}=1-D+\cdots, \qquad \left(1-D\right)x=x-1
$$

Step 3. Multiply the exponential back on.

$$
y_{p}=e^{2x}\left(x-1\right)
$$

Step 4. Add the complementary function, one exponential because the order is one, and check.

$$
y=c_{1}e^{x}+e^{2x}\left(x-1\right)
$$

Step 5. Substitute the particular integral back.

$$
\frac{d}{dx}\left[e^{2x}\left(x-1\right)\right]-e^{2x}\left(x-1\right)=e^{2x}\left(2x-2+1\right)-e^{2x}\left(x-1\right)=e^{2x}x
$$

The check succeeds, so the shift rule has been applied correctly.

### 4.9 Problem: the input variable times a function, second order

Solve $\left(D^{2}-1\right)y=xe^{2x}$.

### 4.10 Solution: the multiplier rule with one correction term

Step 1. Record the dial polynomial, the number in the exponent, and the derivative of the dial polynomial.

$$
f(D)=D^{2}-1, \qquad a=2, \qquad f'(D)=2D
$$

Step 2. Evaluate the dial polynomial at two to confirm the condition holds.

$$
f(2)=4-1=3
$$

Step 3. Write the first piece of the rule.

$$
x\frac{e^{2x}}{3}
$$

Step 4. Build the correction. The derivative instruction applied to the exponential gives four times the exponential, and the square of the dial value is nine.

$$
\frac{2D\,e^{2x}}{9}=\frac{4e^{2x}}{9}
$$

Step 5. Subtract the correction and add the complementary function.

$$
y=c_{1}e^{x}+c_{2}e^{-x}+\frac{xe^{2x}}{3}-\frac{4e^{2x}}{9}
$$

Step 6. Check by substitution, displaying the two derivatives.

$$
y_{p}'=e^{2x}\left(\frac{1+2x}{3}-\frac{8}{9}\right)=\frac{e^{2x}\left(6x-5\right)}{9}, \qquad y_{p}''=\frac{e^{2x}\left(12x-4\right)}{9}
$$

$$
y_{p}''-y_{p}=\frac{e^{2x}\left(12x-4\right)}{9}-\frac{e^{2x}\left(3x-4\right)}{9}=\frac{e^{2x}\left(9x\right)}{9}=xe^{2x}
$$

The coefficient of $xe^{2x}$ is one and the constant coefficient is zero, so the correction term has done its job.

### 4.11 Problem: a repeated root and the x multiplier

Solve $\left(D-2\right)^{2}y=4e^{2x}$.

### 4.12 Solution: multiply by $x$ twice and use the second derivative

Step 1. Test the number two in the dial polynomial.

$$
f(2)=0
$$

Step 2. Since the polynomial is a perfect square, the failure is of order two, so the reply needs $x$ squared and the second derivative of the dial polynomial.

Step 3. Compute that second derivative and assemble the reply.

$$
f(D)=D^{2}-4D+4, \qquad f''(D)=2, \qquad f''(2)=2, \qquad y_{p}=\frac{4x^{2}e^{2x}}{f''(2)}=2x^{2}e^{2x}
$$

Step 4. Add the complementary function, which also duplicates the failing shape and therefore carries an extra factor of $x$.

$$
y=c_{1}e^{2x}+c_{2}xe^{2x}+2x^{2}e^{2x}
$$

Step 5. Check by applying the machine twice in succession.

$$
\left(D-2\right)\left(2x^{2}e^{2x}\right)=4xe^{2x}, \qquad \left(D-2\right)\left(4xe^{2x}\right)=4e^{2x}
$$

The check succeeds. The divisor by $f''(2)$ is essential: leaving it out would give four times the input.

### 4.13 Problem: a wave that duplicates the zero-answer family

Solve $\left(D^{2}+4\right)y=\cos 2x$.

### 4.14 Solution: multiply the wave by $x$

Step 1. Replace $D^{2}$ by the negative square of the rate and observe the result.

$$
D^{2}\to -4, \qquad -4+4=0
$$

Step 2. The replacement has produced zero, so the wave duplicates the zero-answer family and the ordinary rule is unavailable. Record the derivative of the dial polynomial.

$$
f'(D)=2D
$$

Step 3. Multiply the input by $x$ and divide by the derivative instruction, remembering that one integration of a cosine produces a sine divided by the rate.

$$
y_{p}=x\cdot\frac{\cos 2x}{2D}=x\cdot\frac{\sin 2x}{4}=\frac{x\sin 2x}{4}
$$

Step 4. Add the complementary function, whose waves also have rate two.

$$
y=c_{1}\cos 2x+c_{2}\sin 2x+\frac{x\sin 2x}{4}
$$

Step 5. Check by differentiating the particular integral twice.

$$
\frac{d^{2}}{dx^{2}}\left(\frac{x\sin 2x}{4}\right)=\cos 2x-x\sin 2x
$$

Step 6. Add four times the particular integral and confirm the input appears.

$$
\cos 2x-x\sin 2x+4\cdot\frac{x\sin 2x}{4}=\cos 2x
$$

The check succeeds. The reply is not a wave of fixed size but a wave whose size grows with $x$, which is exactly the swing behaviour described at the start.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Why the swing grows

The failure case is not a trick of notation; it is the mathematical content of resonance. When the input matches the machine's natural rhythm, the ordinary reply cannot exist, because the input already belongs to the zero-answer family. What saves the situation is that the reply becomes proportional to the input variable, and a factor of $x$ is exactly the statement that the response accumulates over time.

The order of the growth matches the depth of the duplication. A single duplication, which happens when the number in the exponent is a simple root, produces one factor of $x$ and a divisor equal to the first derivative of the dial polynomial at that root. A double duplication produces $x$ squared and a divisor equal to the second derivative. A triple duplication produces $x$ cubed and a divisor equal to the third derivative. For a pure power such as $(D-a)^{2}$ the second derivative at the root is two, and for $(D-a)^{3}$ the third derivative is six, which is where the factorial numbers appear; if the dial polynomial carries extra factors, those factors also contribute to the divisor.

### 5.2 What the short methods cannot do

The short methods rely on three properties that must be stated honestly. First, the dials must be constant. If a coefficient multiplies $y$ or a derivative and itself depends on $x$, then $D$ cannot be shuffled as though it were a number, and the whole approach collapses. Second, the input must have one of the five shapes, or be a sum of such shapes, because only then does the reply stay inside a small family of functions. Third, the machine's order fixes how many free numbers the final answer carries, and the particular integral never supplies those numbers.

The rules are also silent about the interval on which a solution is valid. For constant coefficients and well-behaved inputs the answer is valid everywhere, but the moment a solution is matched to data at a point, the interval has to be named.

### 5.3 Common beginner misconceptions

- **Replacing $D^{2}$ by $+a^{2}$ in a wave problem.** The correct replacement is the negative square of the rate, because a wave differentiated twice returns minus itself scaled by the square of its rate. Using the positive square changes the sign of the whole answer and fails every substitution check.
- **Using the exponential rule when the number is a root.** Dividing by zero is not a shortcut; it is a signal that the input duplicates the zero-answer family and that a factor of $x$ is required.
- **Multiplying by $x$ when nothing fails.** The multiplier is a remedy for duplication only. Applying it when the condition holds produces a function that does not satisfy the equation.
- **Forgetting that the divisor grows with the depth of the failure.** Two duplications call for $x$ squared and a divisor equal to the second derivative of the dial polynomial at the root; three call for $x$ cubed and the third derivative.
- **Stopping the power expansion too early.** For input $x^{2}$ the expansion must reach the second derivative. Stopping at the first derivative loses the constant that makes the substitution work.
- **Expanding in descending powers.** The expansion must start at the number one and climb in powers of $D$, because the higher powers eventually annihilate the polynomial input.
- **Dropping the complementary function.** A particular integral alone is not the general solution; the free numbers come from the zero-answer family and the order fixes how many there must be.
- **Shifting the dials the wrong way.** The exponential shift moves $D$ to $D+a$ because differentiating the product produces a term with the exponential's own rate. Replacing $D$ by $D-a$ is a sign error that fails the check.
- **Forgetting the correction term in the multiplier rule.** Multiplying by $x$ creates an extra derivative, and the correction term is what removes it. Without the correction the answer misses the input by a simple multiple.
- **Treating a particular integral as unique.** Any two particular integrals differ by a zero-answer function, so there are many correct answers. The substitution check, not equality with a printed answer, decides correctness.

### 5.4 A checklist for every question

Ask four questions in order. What is the shape of the input? Which rule matches that shape? Does the condition attached to the rule hold? And does the finished reply survive substitution?

If the shape is an exponential or a wave and the condition fails, multiply by $x$, divide by the derivative of the dial polynomial, and repeat if the derivative also vanishes. If the shape is a power and the constant term is zero, divide out the factor of $D$ and integrate as many times as needed. If the shape is an exponential times a function, pass the exponential through and shift the dials. If the shape is the variable times a function, apply the two-term rule and keep both terms.

### 5.5 Where the topic leads

Two ideas introduced here recur constantly. The first is that a linear machine converts a family of inputs into the same family, with a numerical factor attached; that idea becomes the Laplace transform in later work, where the factor is a function of a new variable rather than a number. The second is resonance, the phenomenon in which an input at the natural rhythm produces growth in time; it explains why a bridge can be destroyed by marching soldiers and why a radio receiver responds so strongly to one frequency.

A third idea is more practical. The short methods are algorithms, and algorithms can be checked. Every rule in this note was proved by differentiating and every example was verified by substitution, which is the standard a mathematics answer must meet. A student who checks every particular integral will find, within a few questions, that the sign in the wave rule and the divisor in the failure case are the only two places where marks are usually lost.

### 5.6 The whole note in one paragraph

Five shapes, five rules, one strategy. An exponential is answered by evaluating the dial polynomial at the number in the exponent, provided that number is not a root. A wave is answered by replacing the squared derivative with the negative square of its rate, provided the collapse does not produce zero. A power is answered by expanding the inverse instruction in ascending powers of the derivative and stopping once the powers exceed the degree. An exponential times a function is answered by passing the exponential through and shifting the dials. The variable times a function is answered by multiplying the ordinary reply by $x$ and subtracting a correction built from the derivative of the dial polynomial. When a condition fails, the reply acquires a factor of $x$ and a divisor given by the next derivative of the dial polynomial, which is the algebraic form of the swing that grows.

Around those five rules sit three habits. Write the machine as a polynomial before doing anything. Keep the complementary function separate and count its free numbers against the order. Verify every reply by substitution, collecting coefficients of the distinct pieces. A student who keeps those three habits will not be surprised by the two failure cases, because a failed condition announces itself as a zero in the denominator, and a zero in the denominator is precisely the signal that the input has strayed into the zero-answer family.
