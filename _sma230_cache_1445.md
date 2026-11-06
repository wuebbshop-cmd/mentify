## 1. Core Concept Overview & Intuition

Physical quantities fall into two broad classes. A **scalar** is a quantity possessing magnitude only, such as mass, length, time, temperature, or any real number. A **vector** is a quantity possessing both magnitude and direction, such as displacement, velocity, force, and acceleration. The distinction is not cosmetic: scalars combine by ordinary arithmetic, whereas vectors combine by a geometric law of addition that respects direction.

A vector is represented graphically by a directed line segment. The length of the segment encodes the magnitude according to a stated vector scale, the orientation of the segment encodes the direction of action, and an arrowhead encodes the sense. The vector from initial point $O$ to terminal point $P$ is written $\overrightarrow{OP}$ or $\vec{A}$, and its magnitude is written $\lvert\overrightarrow{OP}\rvert$ or $\lvert\vec{A}\rvert$. The reversed segment $\overrightarrow{PO}$ represents a vector of equal magnitude but opposite sense, denoted $-\vec{A}$. Two vectors $\vec{A}$ and $\vec{B}$ are **equal**, written $\vec{A}=\vec{B}$, precisely when they have the same magnitude and the same direction, regardless of where their initial points are placed.

The central intuition of vector algebra is the **chain rule of addition**: to add vectors, place them head to tail, and the resultant is the single vector joining the start of the first to the end of the last. This construction is the engine behind every calculation in this unit — magnitudes via Pythagoras, unit vectors via normalization, and resultants of many displacements via successive chaining.

## 2. Mathematical Formalization & Core Definitions

> **Definition (Vector and Scalar).** A vector is a quantity having both magnitude and direction. A scalar is a quantity having magnitude but no direction.

> **Definition (Equality of Vectors).** Two vectors $\vec{A}$ and $\vec{B}$ are equal if they have the same magnitude and direction, regardless of the position of their initial points.

> **Definition (Addition of Vectors).** The sum of two vectors $\overrightarrow{AB}$ and $\overrightarrow{BC}$ is the single equivalent vector $\overrightarrow{AC}$, that is $\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$, or in letter notation $\vec{a}+\vec{b}=\vec{c}$.

The chain construction extends to any finite number of vectors. Drawing $\vec{a},\vec{b},\vec{c},\vec{d}$ head to tail gives



$$
\begin{aligned}
\vec{a}+\vec{b} &= \overrightarrow{AC}, \\
\overrightarrow{AC}+\vec{c} &= \overrightarrow{AD}, \\
\overrightarrow{AD}+\vec{d} &= \overrightarrow{AE}.
\end{aligned}
$$



Hence $\vec{a}+\vec{b}+\vec{c}+\vec{d}=\overrightarrow{AE}$, the single vector joining the start of the first to the end of the last. If the chain closes on itself — the end of the last vector coinciding with the beginning of the first — the resultant has no magnitude.

### Components of a Vector

Any vector $\vec{A}$ in three dimensions may be placed with initial point at the origin $O$ of a rectangular coordinate system. If $(A_1,A_2,A_3)$ are the rectangular coordinates of the terminal point, the vectors $A_1\hat{\imath}$, $A_2\hat{\jmath}$, $A_3\hat{k}$ are the **component vectors** of $\vec{A}$ in the $x$, $y$, and $z$ directions respectively, and their resultant is $\vec{A}$:



$$
\vec{A}=A_1\hat{\imath}+A_2\hat{\jmath}+A_3\hat{k}.
$$



The **magnitude** of $\vec{A}$ is obtained by applying Pythagoras' theorem twice (once in the base plane, once vertically):



$$
\lvert\vec{A}\rvert=\sqrt{A_1^{2}+A_2^{2}+A_3^{2}}.
$$



In particular, the **position vector** (radius vector) from $O$ to the point $(x,y,z)$ is



$$
\vec{r}=x\hat{\imath}+y\hat{\jmath}+z\hat{k},
\qquad
\lvert\vec{r}\rvert=\sqrt{x^{2}+y^{2}+z^{2}}.
$$



> **Definition (Unit Vector).** A unit vector is a vector having unit magnitude. If $\vec{A}$ is a vector with magnitude $\lvert\vec{A}\rvert\neq 0$, then $\hat{a}=\dfrac{\vec{A}}{\lvert\vec{A}\rvert}$ is a unit vector having the same direction as $\vec{A}$.

The operation $\vec{A}\mapsto\vec{A}/\lvert\vec{A}\rvert$ is called **normalization**. It rescales the vector to length one while preserving direction, and it is the standard device for extracting a pure direction from a computed resultant.

### Vector from One Point to Another

Let $P(x_1,y_1,z_1)$ and $Q(x_2,y_2,z_2)$ have position vectors



$$
\vec{r}_1=x_1\hat{\imath}+y_1\hat{\jmath}+z_1\hat{k},
\qquad
\vec{r}_2=x_2\hat{\imath}+y_2\hat{\jmath}+z_2\hat{k}.
$$



Since $\vec{r}_1+\overrightarrow{PQ}=\vec{r}_2$, the displacement from $P$ to $Q$ is



$$
\overrightarrow{PQ}=\vec{r}_2-\vec{r}_1=(x_2-x_1)\hat{\imath}+(y_2-y_1)\hat{\jmath}+(z_2-z_1)\hat{k},
$$



with magnitude



$$
\lvert\overrightarrow{PQ}\rvert=\sqrt{(x_2-x_1)^{2}+(y_2-y_1)^{2}+(z_2-z_1)^{2}},
$$



which is exactly the distance between $P$ and $Q$.

### Direction Cosines

The direction of a vector in three dimensions is fixed by the angles it makes with the three coordinate axes. Let $\vec{r}=a\hat{\imath}+b\hat{\jmath}+c\hat{k}$ with magnitude $r=\lvert\vec{r}\rvert$, and let $\alpha,\beta,\gamma$ be the angles made with the $x$, $y$, and $z$ axes respectively. Then



$$
\frac{a}{r}=\cos\alpha,\qquad \frac{b}{r}=\cos\beta,\qquad \frac{c}{r}=\cos\gamma.
$$



Squaring and adding, and using $a^{2}+b^{2}+c^{2}=r^{2}$,



$$
\begin{aligned}
r^{2}\cos^{2}\alpha+r^{2}\cos^{2}\beta+r^{2}\cos^{2}\gamma &= r^{2}, \\
\cos^{2}\alpha+\cos^{2}\beta+\cos^{2}\gamma &= 1.
\end{aligned}
$$



Writing $l=\cos\alpha$, $m=\cos\beta$, $n=\cos\gamma$, the triple $[l,m,n]$ is called the set of **direction cosines** of $\vec{r}$, and



$$
l^{2}+m^{2}+n^{2}=1,
\qquad
l=\frac{a}{r},\quad m=\frac{b}{r},\quad n=\frac{c}{r}.
$$



## 3. Key Theorems & Essential Results

> **Theorem (Commutative Law of Addition).** For any vectors $\vec{A}$ and $\vec{B}$, $\vec{A}+\vec{B}=\vec{B}+\vec{A}$.

*Proof.* Construct the parallelogram with adjacent sides $\vec{A}$ and $\vec{B}$. Along one route $\overrightarrow{OP}+\overrightarrow{PQ}=\overrightarrow{OQ}$, i.e. $\vec{A}+\vec{B}=\vec{C}$. Along the other route $\overrightarrow{OR}+\overrightarrow{RQ}=\overrightarrow{OQ}$, i.e. $\vec{B}+\vec{A}=\vec{C}$. Both routes terminate at the same point, hence $\vec{A}+\vec{B}=\vec{B}+\vec{A}$. $\square$

> **Theorem (Associative Law of Addition).** For any vectors $\vec{A},\vec{B},\vec{C}$, $\vec{A}+(\vec{B}+\vec{C})=(\vec{A}+\vec{B})+\vec{C}$.

*Proof.* Take points $O,P,Q,R$ with $\overrightarrow{OP}=\vec{A}$, $\overrightarrow{PQ}=\vec{B}$, $\overrightarrow{QR}=\vec{C}$, and let $\overrightarrow{OR}=\vec{D}$. Then $\overrightarrow{OP}+\overrightarrow{PQ}=\overrightarrow{OQ}=\vec{A}+\vec{B}$ and $\overrightarrow{PQ}+\overrightarrow{QR}=\overrightarrow{PR}=\vec{B}+\vec{C}$. Grouping the first way, $\overrightarrow{OP}+\overrightarrow{PR}=\overrightarrow{OR}=\vec{D}$, i.e. $\vec{A}+(\vec{B}+\vec{C})=\vec{D}$. Grouping the second way, $\overrightarrow{OQ}+\overrightarrow{QR}=\overrightarrow{OR}=\vec{D}$, i.e. $(\vec{A}+\vec{B})+\vec{C}=\vec{D}$. Hence the two groupings agree. $\square$

Consequently the order of addition of any number of vectors is immaterial, and a sum may be regrouped or reordered at will.

> **Result (Magnitude of a Resultant).** If $\vec{R}=\vec{r}_1+\vec{r}_2+\cdots+\vec{r}_n$ with $\vec{R}=R_1\hat{\imath}+R_2\hat{\jmath}+R_3\hat{k}$, then $\lvert\vec{R}\rvert=\sqrt{R_1^{2}+R_2^{2}+R_3^{2}}$, and a unit vector parallel to $\vec{R}$ is $\hat{r}=\vec{R}/\lvert\vec{R}\rvert$.

> **Result (Right-Angled Resultant).** If two vectors of magnitudes $p$ and $q$ act at right angles, the magnitude of their resultant satisfies $p^{2}+q^{2}=r^{2}$, so $r=\sqrt{p^{2}+q^{2}}$.

> **Result (Direction Cosine Identity).** For any nonzero vector, $l^{2}+m^{2}+n^{2}=1$.

> **Result (Collinearity and Coplanarity of Position Vectors).** Any vector $\vec{r}$ lying in the plane of two non-collinear vectors $\vec{a}$ and $\vec{b}$ can be written $\vec{r}=x\vec{a}+y\vec{b}$ for scalars $x,y$; in three-dimensional space, any vector can be written $\vec{r}=x\vec{a}+y\vec{b}+z\vec{c}$ for scalars $x,y,z$. Comparing coefficients of independent vectors on the two sides of an identity is a valid method of solution.

> **Result (Closed Vector Chain).** If a chain of vectors returns to its starting point, so that the terminal point of the last vector coincides with the initial point of the first, the resultant sum is a vector of zero magnitude.

## 4. Worked Exemplar Problem with Step-by-Step Solution

**Problem.** Find the unit vector parallel to the resultant of $\vec{r}_1=2\hat{\imath}+4\hat{\jmath}-5\hat{k}$ and $\vec{r}_2=\hat{\imath}+2\hat{\jmath}+3\hat{k}$, and verify that the resulting vector has unit magnitude.

**Step 1 — Form the resultant by componentwise addition.**



$$
\begin{aligned}
\vec{R} &= \vec{r}_1+\vec{r}_2 \\
&= (2\hat{\imath}+4\hat{\jmath}-5\hat{k})+(\hat{\imath}+2\hat{\jmath}+3\hat{k}) \\
&= 3\hat{\imath}+6\hat{\jmath}-2\hat{k}.
\end{aligned}
$$



**Step 2 — Compute the magnitude of the resultant.**



$$
\begin{aligned}
\lvert\vec{R}\rvert &= \sqrt{3^{2}+6^{2}+(-2)^{2}} \\
&= \sqrt{9+36+4} \\
&= \sqrt{49} \\
&= 7.
\end{aligned}
$$



**Step 3 — Normalize to obtain the unit vector.**



$$
\hat{r}=\frac{\vec{R}}{\lvert\vec{R}\rvert}=\frac{1}{7}\left(3\hat{\imath}+6\hat{\jmath}-2\hat{k}\right).
$$



**Step 4 — Verify unit magnitude.**



$$
\begin{aligned}
\lvert\hat{r}\rvert &= \sqrt{\left(\tfrac{3}{7}\right)^{2}+\left(\tfrac{6}{7}\right)^{2}+\left(-\tfrac{2}{7}\right)^{2}} \\
&= \frac{1}{7}\sqrt{9+36+4} \\
&= \frac{7}{7} \\
&= 1.
\end{aligned}
$$



The verification confirms the normalization is correct.

**Companion calculation (direction cosines).** For $\vec{r}=3\hat{\imath}-2\hat{\jmath}+6\hat{k}$ we have $a=3$, $b=-2$, $c=6$ and



$$
r=\sqrt{9+4+36}=\sqrt{49}=7,
$$



so the direction cosines are



$$
l=\frac{3}{7},\qquad m=-\frac{2}{7},\qquad n=\frac{6}{7},
$$



and indeed $l^{2}+m^{2}+n^{2}=\tfrac{9}{49}+\tfrac{4}{49}+\tfrac{36}{49}=1$.

**Companion calculation (right-angled resultant).** A force of $5\,\text{N}$ due East and a force of $12\,\text{N}$ due North act at right angles. By Pythagoras' theorem,



$$
\begin{aligned}
p^{2}+q^{2} &= r^{2}, \\
25+144 &= 169, \\
r &= \sqrt{169}=13\,\text{N}.
\end{aligned}
$$



**Companion calculation (resultant of several displacements).** For displacements $A$ of $10\,\text{m}$ Northwest, $B$ of $20\,\text{m}$ at $30^{\circ}$ north of east, and $C$ of $35\,\text{m}$ due south, the resultant is $\vec{D}=\vec{A}+\vec{B}+\vec{C}$, formed by joining the initial point of $A$ to the terminal point of $C$. Measured graphically on a scale of $5\,\text{m}$ per unit, the resultant has magnitude $4.1$ units, i.e. $20.5\,\text{m}$, and direction $60^{\circ}$ south of east.

**Companion calculation (displacement between two points).** For $P(x_1,y_1,z_1)$ and $Q(x_2,y_2,z_2)$,



$$
\overrightarrow{PQ}=(x_2-x_1)\hat{\imath}+(y_2-y_1)\hat{\jmath}+(z_2-z_1)\hat{k},
$$



whose magnitude is the distance between the points.

## 5. High-Yield Exam Takeaways & Common Pitfalls

### Lesson Learning Outcomes

By the end of this unit the student should be able to: distinguish scalar from vector quantities and classify physical examples of each; represent a vector graphically with a stated scale and analytically in component form; add any number of vectors by the chain construction and state the commutative and associative laws; compute the magnitude of a vector and of a resultant; normalize a vector to obtain a unit vector in a prescribed direction; compute the displacement vector between two points and its magnitude; and determine the direction cosines of a vector and verify the identity $l^{2}+m^{2}+n^{2}=1$.

### Magnitude, Unit Vector and Resultant — Calculation Checklist

| Task | Formula | Guard condition |
| --- | --- | --- |
| Magnitude in 3D | $\lvert\vec{A}\rvert=\sqrt{A_1^{2}+A_2^{2}+A_3^{2}}$ | none |
| Magnitude in 2D | $\lvert\vec{A}\rvert=\sqrt{A_1^{2}+A_2^{2}}$ | none |
| Unit vector | $\hat{a}=\vec{A}/\lvert\vec{A}\rvert$ | requires $\lvert\vec{A}\rvert\neq 0$ |
| Resultant | $\vec{R}=\sum_i\vec{r}_i$ componentwise | add like components only |
| Distance $PQ$ | $\lvert\overrightarrow{PQ}\rvert=\sqrt{(x_2-x_1)^{2}+(y_2-y_1)^{2}+(z_2-z_1)^{2}}$ | subtract in consistent order |
| Direction cosines | $l=a/r,\ m=b/r,\ n=c/r$ | check $l^{2}+m^{2}+n^{2}=1$ |
| Right-angled resultant | $r=\sqrt{p^{2}+q^{2}}$ | only for perpendicular components |

### Assessment

Assessment in this unit targets the following recurring question types: computing the resultant of a set of displacements given as bearings and distances, and reporting both magnitude and direction; finding a unit vector parallel to a computed resultant and verifying unit magnitude; finding the vector joining two given points together with its magnitude; extracting direction cosines from a component form; and proving elementary geometric facts by expressing position vectors in terms of two or three independent vectors and comparing coefficients. Marks are awarded for correct componentwise addition, correct magnitude evaluation, correct normalization, and explicit verification steps.

### Common Pitfalls

- **Adding magnitudes instead of vectors.** The magnitude of a sum is not the sum of magnitudes; $\lvert\vec{A}+\vec{B}\rvert\neq\lvert\vec{A}\rvert+\lvert\vec{B}\rvert$ in general. Always add componentwise first, then take the magnitude.
- **Sign errors in components.** A component directed along the negative axis carries a minus sign; squaring removes it in the magnitude but not in the direction cosines, where $m=-\tfrac{2}{7}$ must retain its sign.
- **Forgetting the guard condition.** Normalization is undefined for the zero vector; a closed vector chain has zero resultant and admits no unit vector.
- **Mixing up initial and terminal points.** The displacement is $\vec{r}_2-\vec{r}_1$, not $\vec{r}_1-\vec{r}_2$; the reversed order gives the opposite sense.
- **Omitting the verification.** When asked for a unit vector, always square and add the components to confirm the result equals one.
- **Treating direction cosines as angles.** The direction cosines are the cosines of the angles, not the angles themselves, and they satisfy $l^{2}+m^{2}+n^{2}=1$.
- **Assuming a graphical scale is exact.** Graphical construction gives an approximate magnitude and bearing; state the scale and round consistently with it.

### Prescribed Reading

The prescribed reading for this unit is the course material itself, whose opening chapter develops vector representation, addition of vectors, vector algebra, components of a vector, unit vectors and direction cosines, together with the worked examples on resultants of forces and displacements and on the displacement between two points. Students should work through that chapter's definitions and examples in full, since the definitions of scalar and vector quantities, the chain and parallelogram constructions, the component formalism and the direction-cosine identity used throughout this unit are all developed there.