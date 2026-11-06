## 1. Conceptual Overview

The real number system $\mathbb{R}$ is the setting for limits, sequences, continuity, and calculus. In this lesson the focus is its internal structure: the algebraic operations, the order relation, rational and irrational numbers, intervals, bounded sets, supremum and infimum, completeness, and density of the rationals.

The central conclusion is that $\mathbb{R}$ is a **complete ordered field**. These three words summarize distinct properties:

- A **field** supports addition, subtraction, multiplication, and division by nonzero numbers with the usual algebraic laws.
- An **ordered field** has a consistent order compatible with those operations.
- **Completeness** says that bounded sets of real numbers have least upper bounds and greatest lower bounds in $\mathbb{R}$.

The distinction between $\mathbb{Q}$ and $\mathbb{R}$ is not merely that the second contains more numbers. The rationals are dense in the reals, but they are not complete: some nonempty rational sets that are bounded above have no rational supremum. The real system fills the gaps required by the completeness axiom.

## 2. Definitions and Notation

### 2.1 Number sets and rationality

The integers are denoted by $\mathbb{Z}$, the natural numbers by $\mathbb{N}$, the rational numbers by $\mathbb{Q}$, and the real numbers by $\mathbb{R}$. A rational number can be written as $m/n$, where $m,n\in\mathbb{Z}$ and $n\ne0$. It can be reduced so that the numerator and denominator have no common factor other than 1. An irrational real number is not rational; therefore

$$
\mathbb{R}=\mathbb{Q}\cup\mathbb{Q}^{c},
$$

where $\mathbb{Q}^{c}$ here means the irrationals within $\mathbb{R}$.

For $a<b$, the common intervals are

$$
(a,b)=\{x\in\mathbb{R}:a<x<b\},\qquad
[a,b]=\{x\in\mathbb{R}:a\le x\le b\},
$$

$$
(a,b]=\{x:a<x\le b\},\qquad
[a,b)=\{x:a\le x<b\}.
$$

Round brackets exclude an endpoint; square brackets include it. This matters when identifying whether a bound belongs to a set.

### 2.2 Field structure

For all $x,y,z\in\mathbb{R}$:

- **Closure:** $x+y\in\mathbb{R}$ and $xy\in\mathbb{R}$.
- **Commutativity:** $x+y=y+x$ and $xy=yx$.
- **Associativity:** $(x+y)+z=x+(y+z)$ and $(xy)z=x(yz)$.
- **Distributivity:** $x(y+z)=xy+xz$.
- **Identities:** $x+0=x$ and $x\cdot1=x$, with $0\ne1$.
- **Additive inverse:** each $x$ has $-x$ with $x+(-x)=0$.
- **Multiplicative inverse:** each $x\ne0$ has $x^{-1}$ with $xx^{-1}=1$.

These laws make $\mathbb{R}$ a field. In particular, division is defined only by a nonzero number. The inverse axiom does not assert that zero has a multiplicative inverse.

### 2.3 Order and order compatibility

The order relation $\le$ compares real numbers. It is reflexive, antisymmetric, and transitive, and any two real numbers are comparable. Compatibility with the field operations means:

$$
x\le y\Longrightarrow x+z\le y+z,
$$

and if $0\le z$, then

$$
x\le y\Longrightarrow xz\le yz.
$$

If $z<0$, multiplying an inequality by $z$ reverses its direction. This is a consequence of the ordered-field rules and is essential in inequality proofs.

### 2.4 Bounds, supremum, and infimum

A nonempty set $S\subseteq\mathbb{R}$ is **bounded above** if some $u$ satisfies $s\le u$ for every $s\in S$. Such a $u$ is an upper bound. The **supremum** $\sup S$ is the least upper bound: it is an upper bound and is no greater than any other upper bound.

A set is **bounded below** if some $l$ satisfies $l\le s$ for every $s\in S$. The **infimum** $\inf S$ is the greatest lower bound: it is a lower bound and is no less than any other lower bound.

A supremum need not belong to $S$. If it does belong, it is the maximum. Likewise, an infimum that belongs to $S$ is the minimum. The endpoint distinction is visible in

$$
S=[-2,3]:\quad \sup S=\max S=3,\quad \inf S=\min S=-2,
$$

whereas for $S=(1,3)$, $\sup S=3$ and $\inf S=1$, but neither endpoint is a maximum or minimum because neither belongs to the interval.

A useful epsilon characterization is: $u=\sup S$ exactly when $u$ is an upper bound and, for every $\varepsilon>0$, there is an $s\in S$ with $u-\varepsilon<s\le u$. Every neighborhood immediately below the supremum therefore contains set elements. Similarly, $l=\inf S$ when it is a lower bound and for every $\varepsilon>0$ some $s\in S$ satisfies $l\le s<l+\varepsilon$.

## 3. Theorems and Core Results

### 3.1 Rational and irrational numbers

The source proves that $\sqrt{2}$ is irrational by contradiction. Suppose $\sqrt{2}=m/n$ in lowest terms, with integers $m,n$ and $n\ne0$. Squaring gives $m^2=2n^2$, so $m^2$ is even. The square of an odd integer is odd, so $m$ must be even; write $m=2r$. Then

$$
4r^2=2n^2\quad\Longrightarrow\quad n^2=2r^2,
$$

so $n$ is also even. Thus $m$ and $n$ share a factor 2, contradicting the assumption that the fraction was in lowest terms. Therefore $\sqrt{2}\notin\mathbb{Q}$.

This proof illustrates a general strategy: assume a rational representation in lowest terms, use the equation to show numerator and denominator share a prime factor, and obtain a contradiction. It also shows why the real numbers contain more than the rationals.

### 3.2 Completeness axiom

The completeness axiom states:

> Every nonempty subset of $\mathbb{R}$ that is bounded above has a supremum in $\mathbb{R}$. Equivalently, every nonempty subset bounded below has an infimum in $\mathbb{R}$.

The real numbers are therefore a complete ordered field. Completeness is not one more algebraic operation; it is a property of the whole ordered set.

The rational numbers fail this property. Consider

$$
S=\{q\in\mathbb{Q}:q\ge0,\ q^2<2\}.
$$

The set is nonempty and bounded above in $\mathbb{Q}$, but its least upper bound in $\mathbb{R}$ is $\sqrt2$, which is not rational. Hence $S$ has no supremum in $\mathbb{Q}$. The missing rational limit is one of the gaps filled by completing the number system.

### 3.3 Density of the rationals

The rationals are dense in $\mathbb{R}$: if $x<y$, there is a rational $r$ with $x<r<y$. The interval can be arbitrarily short; no two distinct real numbers are so close that every rational is excluded.

A standard proof uses the Archimedean property. Choose $n\in\mathbb{N}$ so large that $1/n<y-x$. Then the interval $(nx,ny)$ has length greater than 1, so it contains an integer $m$. Dividing by $n>0$ gives

$$
x<\frac{m}{n}<y,
$$

and $m/n$ is rational. The point is to scale the interval until it is wide enough to contain an integer, then scale back.

The source also states that irrationals are dense. One way to see this is to apply rational density to the interval $(x/\sqrt2,y/\sqrt2)$ and choose a nonzero rational $r$ inside it. Then $r\sqrt2$ lies between $x$ and $y$ and is irrational: if $r\sqrt2$ were rational, dividing by nonzero rational $r$ would make $\sqrt2$ rational, a contradiction.

## 4. Worked Examples

### 4.1 Bounds, supremum, infimum, maximum, and minimum

For $S=[-2,3]$, every element is at most 3 and at least -2. Thus 3 is an upper bound and -2 is a lower bound. They are the least upper and greatest lower bounds, respectively. Since both endpoints lie in the closed interval, they are also the maximum and minimum.

For $T=(1,3)$, 3 is still an upper bound and 1 is still a lower bound. No number below 3 can be an upper bound: if $u<3$, an interval endpoint sufficiently close to 3 contains some $t\in T$ with $u<t<3$. Thus $\sup T=3$. Similarly, $\inf T=1$. However, 3 and 1 are not elements of $T$, so $T$ has no maximum or minimum. This example prevents the common mistake of assuming every supremum is attained.

For $U=\{1/n:n\in\mathbb{N}\}$, the number 1 is the maximum and supremum. Zero is a lower bound. For every $\varepsilon>0$, the Archimedean property gives $n$ with $1/n<\varepsilon$, so the set contains elements arbitrarily close to zero from above. Hence $\inf U=0$, but $0\notin U$ and there is no minimum.

### 4.2 Applying the epsilon test

Let $T=(1,3)$ and test whether 3 is its supremum. First, $t<3$ for every $t\in T$, so 3 is an upper bound. Second, take any $\varepsilon>0$. Choose a positive $\delta<\min(\varepsilon,2)$ and set $t=3-\delta$. Then $1<t<3$ and $3-\varepsilon<t$. Therefore every interval just below 3 contains a point of $T$. Together these conditions establish $\sup T=3$.

The epsilon test is not a claim that the set contains its supremum. It says that no smaller number can still bound the set. Membership is a separate question, which is why the open interval has a supremum but no maximum.

## 5. Revision Summary and Common Errors

- A field has the algebraic laws; an ordered field adds a compatible order; a complete ordered field also satisfies the least-upper-bound property.
- A rational number is a ratio of integers with nonzero denominator; an irrational real is not such a ratio.
- $\sup S$ is the least upper bound; it may or may not lie in $S$. If it lies in $S$, it is the maximum. The corresponding statements hold for infimum and minimum.
- Completeness applies to every nonempty bounded-above subset of $\mathbb{R}$; the analogous infimum statement follows by reversing signs.
- Density means a rational lies strictly between every pair $x<y$; it does not mean every real is rational.

Common errors include treating an upper bound as automatically the supremum, confusing maximum with supremum, claiming $(1,3)$ has a maximum, forgetting the denominator restriction in $m/n$, assuming $\sqrt2$ is rational because it is a real number, and invoking completeness for a set that is empty or not bounded above. In proof questions, state the set and each property being checked, show the epsilon step for least/greatest bounds, and identify whether the bound belongs to the set.