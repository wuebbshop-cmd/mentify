## 1. Core Concept Overview & Intuition

Physical quantities fall into two broad classes. A **scalar** is a quantity possessing magnitude only: mass, length, time, temperature, and any real number are scalars. A **vector** is a quantity possessing both magnitude and direction: displacement, velocity, force, and acceleration are vectors. The distinction is not cosmetic — scalars combine by ordinary arithmetic, whereas vectors combine by a geometry that respects direction.

The intuition for vector addition is the **chain rule of displacements**. To add two vectors $\mathbf{a}$ and $\mathbf{b}$, draw them as a chain, starting the second where the first ends; the sum $\mathbf{c}$ is the single vector joining the start of the first to the end of the second. If a body is displaced from $A$ to $B$ and then from $B$ to $C$, the net displacement is the single vector from $A$ to $C$, written $\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$, or $\mathbf{a}+\mathbf{b}=\mathbf{c}$. Extending the chain to four vectors $\mathbf{a},\mathbf{b},\mathbf{c},\mathbf{d}$ drawn head-to-tail, the successive partial sums are $\mathbf{a}+\mathbf{b}=\overrightarrow{AC}$, then $\overrightarrow{AC}+\mathbf{c}=\overrightarrow{AD}$, then $\overrightarrow{AD}+\mathbf{d}=\overrightarrow{AE}$; the total is the single vector joining the start of the first to the end of the last, namely $\overrightarrow{AE}$. If the chain closes on itself — the end of the last vector coincides with the beginning of the first — the resultant has no magnitude.

A vector is represented graphically by a line whose length denotes magnitude according to a stated vector scale and whose direction, marked by an arrowhead, denotes the direction of action. The vector $\overrightarrow{OP}$ has initial point $O$ and final point $P$ and is written analytically as $\mathbf{A}$; its magnitude is denoted $\lvert \mathbf{A} \rvert$. The reversed vector $\overrightarrow{PO}$ has the same magnitude but opposite sense, and is written $-\mathbf{A}$. Two vectors $\mathbf{A}$ and $\mathbf{B}$ are **equal** if they have the same magnitude and the same direction, regardless of the position of their initial points.

The central computational idea of this unit is **resolution into components**. Any vector in three dimensions can be placed with its initial point at the origin $O$ of a rectangular coordinate system. If $(A_1,A_2,A_3)$ are the rectangular coordinates of its terminal point, the vectors $A_1\hat{\imath}$, $A_2\hat{\jmath}$, $A_3\hat{k}$ are the component vectors of $\mathbf{A}$ in the $x$, $y$, and $z$ directions respectively, and their resultant is $\mathbf{A}$ itself. Once a vector is in component form, its magnitude follows from the three-dimensional Pythagorean relation, and its direction is captured by the direction cosines. These two constructions — magnitude and direction cosines — are the computational backbone of the entire unit.

## 2. Mathematical Formalization & Core Definitions

> **Definition (Vector and Scalar).** A vector is a quantity having both magnitude and direction, such as displacement, velocity, force, and acceleration. A scalar is a quantity having magnitude but no direction, e.g. mass, length, time, temperature, and any real number.

> **Definition (Vector Representation).** A vector quantity is represented graphically by a line drawn so that the length of the line denotes the magnitude of the quantity according to some stated vector scale, and the direction of the line denotes the direction in which the vector quantity acts. An arrowhead indicates the sense of the direction.

> **Definition (Equality of Vectors).** Two vectors $\mathbf{A}$ and $\mathbf{B}$ are equal if they have the same magnitude and direction regardless of the position of their initial points; thus $\mathbf{A}=\mathbf{B}$.

> **Definition (Addition of Vectors).** The sum of two vectors $\overrightarrow{AB}$ and $\overrightarrow{BC}$ is the single, equivalent, or resultant vector $\overrightarrow{AC}$; that is, $\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$, or $\mathbf{a}+\mathbf{b}=\mathbf{c}$.

> **Definition (Components of a Vector).** Let $\mathbf{A}$ have initial point at the origin $O$ of a rectangular coordinate system and terminal point with coordinates $(A_1,A_2,A_3)$. The vectors $A_1\hat{\imath}$, $A_2\hat{\jmath}$, $A_3\hat{k}$ are the component vectors of $\mathbf{A}$ in the $x$, $y$, and $z$ directions respectively, and
> 

$$
\mathbf{A}=A_1\hat{\imath}+A_2\hat{\jmath}+A_3\hat{k}.
$$

> **Definition (Position Vector).** The position vector or radius vector $\mathbf{r}$ from $O$ to the point $(x,y,z)$ is
> 

$$
\mathbf{r}=x\hat{\imath}+y\hat{\jmath}+z\hat{k},
$$

> and has magnitude
> 

$$
\lvert \mathbf{r} \rvert=r=\sqrt{x^{2}+y^{2}+z^{2}}.
$$

> **Definition (Unit Vector).** A unit vector is a vector having unit magnitude. If $\mathbf{A}$ is a vector with magnitude $A\neq 0$, then
> 

$$
\hat{\mathbf{a}}=\frac{\mathbf{A}}{A}
$$

> is a unit vector having the same direction as $\mathbf{A}$.

> **Definition (Direction Cosines).** The direction of a vector in three dimensions is determined by the angles it makes with the three axes of reference. For $\overrightarrow{OP}=\mathbf{r}=a\hat{\imath}+b\hat{\jmath}+c\hat{k}$, let $\alpha,\beta,\gamma$ be the angles the vector makes with the $x$, $y$, and $z$ axes. Then
> 

$$
l=\cos\alpha=\frac{a}{r},\qquad m=\cos\beta=\frac{b}{r},\qquad n=\cos\gamma=\frac{c}{r},
$$

> where $r=\sqrt{a^{2}+b^{2}+c^{2}}$. The triple $[l,m,n]$, written in square brackets, is called the direction cosines of $\overrightarrow{OP}$.

### 2.1 Magnitude of a Vector

The magnitude of a vector is shown by two vertical bars on either side of the vector, $\lvert \mathbf{a} \rvert$, and is computed using Pythagoras' theorem. For $\mathbf{A}=A_1\hat{\imath}+A_2\hat{\jmath}+A_3\hat{k}$,

$$
\lvert \mathbf{A} \rvert=A=\sqrt{A_1^{2}+A_2^{2}+A_3^{2}}.
$$

In two dimensions this reduces to $\sqrt{A_1^{2}+A_2^{2}}$, the hypotenuse of a right triangle with legs $A_1$ and $A_2$. The magnitude is always non-negative and is zero only for the zero vector.

### 2.2 The Unit Vector

Dividing a nonzero vector by its own magnitude produces a vector of unit length pointing in the same direction:

$$
\hat{\mathbf{a}}=\frac{\mathbf{A}}{\lvert \mathbf{A} \rvert}.
$$

The verification that $\hat{\mathbf{a}}$ has unit magnitude is immediate, since scaling a vector by $1/\lvert \mathbf{A} \rvert$ scales its magnitude by the same positive factor. A unit vector is the standard device for isolating *direction* from *magnitude*: any vector may be reconstructed as $\mathbf{A}=\lvert \mathbf{A} \rvert\,\hat{\mathbf{a}}$.

### 2.3 The Resultant of a Number of Vectors

The resultant of vectors $\mathbf{a}+\mathbf{b}+\mathbf{c}+\mathbf{d}+\cdots$ is obtained by drawing the vectors as a chain and taking the single vector joining the start of the first to the end of the last. In component form, addition is performed coordinatewise:

$$
\mathbf{R}=\mathbf{a}+\mathbf{b}+\mathbf{c}+\cdots=\left(\sum a_1\right)\hat{\imath}+\left(\sum a_2\right)\hat{\jmath}+\left(\sum a_3\right)\hat{k},
$$

where $a_1,a_2,a_3$ denote the $x$, $y$, $z$ components of each summand. The magnitude of the resultant is then $\lvert \mathbf{R} \rvert=\sqrt{R_1^{2}+R_2^{2}+R_3^{2}}$.

### 2.4 Vector from One Point to Another

Given $P(x_1,y_1,z_1)$ and $Q(x_2,y_2,z_2)$ with position vectors $\mathbf{r}_1=x_1\hat{\imath}+y_1\hat{\jmath}+z_1\hat{k}$ and $\mathbf{r}_2=x_2\hat{\imath}+y_2\hat{\jmath}+z_2\hat{k}$, the relation $\mathbf{r}_1+\overrightarrow{PQ}=\mathbf{r}_2$ gives

$$
\overrightarrow{PQ}=\mathbf{r}_2-\mathbf{r}_1=(x_2-x_1)\hat{\imath}+(y_2-y_1)\hat{\jmath}+(z_2-z_1)\hat{k},
$$

with magnitude

$$
\lvert \overrightarrow{PQ} \rvert=\sqrt{(x_2-x_1)^{2}+(y_2-y_1)^{2}+(z_2-z_1)^{2}},
$$

which is precisely the distance between $P$ and $Q$.

### 2.5 Direction Cosines and the Fundamental Identity

From $a=r\cos\alpha$, $b=r\cos\beta$, $c=r\cos\gamma$ and $a^{2}+b^{2}+c^{2}=r^{2}$, substituting the cosine expressions yields

$$
r^{2}\cos^{2}\alpha+r^{2}\cos^{2}\beta+r^{2}\cos^{2}\gamma=r^{2}.
$$

Dividing by $r^{2}\neq 0$ gives the fundamental identity

$$
\cos^{2}\alpha+\cos^{2}\beta+\cos^{2}\gamma=1,
$$

equivalently

$$
l^{2}+m^{2}+n^{2}=1.
$$

This identity is the standard consistency check on any computed triple of direction cosines, and it is the reason a direction in space has only two independent degrees of freedom.

## 3. Key Theorems & Essential Results

> **Theorem (Commutative Law of Addition).** If $\mathbf{A}$ and $\mathbf{B}$ are vectors, then

$$
\mathbf{A}+\mathbf{B}=\mathbf{B}+\mathbf{A}.
$$

> *Proof.* Construct the parallelogram with adjacent sides $\mathbf{A}=\overrightarrow{OP}$ and $\mathbf{B}=\overrightarrow{PQ}$, so that $\overrightarrow{OP}+\overrightarrow{PQ}=\overrightarrow{OQ}$, i.e. $\mathbf{A}+\mathbf{B}=\mathbf{C}$. Reading the same parallelogram along the other route, $\overrightarrow{OR}+\overrightarrow{RQ}=\overrightarrow{OQ}$, i.e. $\mathbf{B}+\mathbf{A}=\mathbf{C}$. Since both routes terminate at the same point $Q$, the two sums coincide. $\blacksquare$

> **Theorem (Associative Law of Addition).** If $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$ are vectors, then

$$
\mathbf{A}+(\mathbf{B}+\mathbf{C})=(\mathbf{A}+\mathbf{B})+\mathbf{C}.
$$

> *Proof.* Take points $O,P,Q,R$ with $\overrightarrow{OP}=\mathbf{A}$, $\overrightarrow{PQ}=\mathbf{B}$, $\overrightarrow{QR}=\mathbf{C}$. Then $\overrightarrow{OP}+\overrightarrow{PQ}=\overrightarrow{OQ}=\mathbf{A}+\mathbf{B}$ and $\overrightarrow{PQ}+\overrightarrow{QR}=\overrightarrow{PR}=\mathbf{B}+\mathbf{C}$. Grouping the first way, $\overrightarrow{OP}+\overrightarrow{PR}=\overrightarrow{OR}=\mathbf{D}$, i.e. $\mathbf{A}+(\mathbf{B}+\mathbf{C})=\mathbf{D}$. Grouping the second way, $\overrightarrow{OQ}+\overrightarrow{QR}=\overrightarrow{OR}=\mathbf{D}$, i.e. $(\mathbf{A}+\mathbf{B})+\mathbf{C}=\mathbf{D}$. Hence the two groupings agree. $\blacksquare$

> **Corollary.** The order of addition of any number of vectors is immaterial.

> **Theorem (Magnitude of a Component Vector).** For $\mathbf{A}=A_1\hat{\imath}+A_2\hat{\jmath}+A_3\hat{k}$,

$$
\lvert \mathbf{A} \rvert=\sqrt{A_1^{2}+A_2^{2}+A_3^{2}}.
$$

> **Theorem (Direction Cosine Identity).** For any nonzero vector with direction cosines $[l,m,n]$,

$$
l^{2}+m^{2}+n^{2}=1.
$$

> **Theorem (Unit Vector Normalization).** If $\mathbf{A}\neq \mathbf{0}$, then $\hat{\mathbf{a}}=\mathbf{A}/\lvert \mathbf{A} \rvert$ satisfies $\lvert \hat{\mathbf{a}} \rvert=1$ and points in the direction of $\mathbf{A}$.

> **Theorem (Diagonal Bisection in a Parallelogram).** The diagonals of a parallelogram bisect each other.
> *Proof.* Let the parallelogram have adjacent sides $\mathbf{a}$ and $\mathbf{b}$, so that $\overrightarrow{AC}=\mathbf{a}+\mathbf{b}$ and $\overrightarrow{BD}=\mathbf{b}-\mathbf{a}$. Let $P$ be the intersection of the diagonals and write $\overrightarrow{AP}=x\,\overrightarrow{AC}$ and $\overrightarrow{BP}=y\,\overrightarrow{BD}$. Since $\overrightarrow{AB}+\overrightarrow{BP}=\overrightarrow{AP}$, we obtain $\mathbf{a}+y(\mathbf{b}-\mathbf{a})=x(\mathbf{a}+\mathbf{b})$. Comparing coefficients of $\mathbf{a}$ and $\mathbf{b}$ on the left and right gives $x=y=\tfrac{1}{2}$, so $P$ is the midpoint of both diagonals. $\blacksquare$

> **Theorem (Equation of a Straight Line).** The line through points with position vectors $\mathbf{a}$ and $\mathbf{b}$ consists of all points with position vector

$$
\mathbf{r}=\mathbf{a}+t(\mathbf{b}-\mathbf{a}),
$$

> where $t$ is a scalar.
> *Proof.* For any point $P$ on the line, $\overrightarrow{OA}+\overrightarrow{AP}=\overrightarrow{OP}$ with $\overrightarrow{AP}=t\,\overrightarrow{AB}$ for some scalar $t$. Hence $\overrightarrow{OP}=\overrightarrow{OA}+t(\mathbf{b}-\mathbf{a})$. $\blacksquare$

> **Remark (Coefficient Sum Condition).** The line equation may be rewritten as

$$
\mathbf{r}=(1-t)\mathbf{a}+t\mathbf{b},
$$

> or equivalently as

$$
(1-t)\mathbf{a}+t\mathbf{b}-\mathbf{r}=\mathbf{0}.
$$

> In this form the sum of the coefficients of the position vectors is $(1-t)+t+(-1)=0$. This vanishing coefficient sum is the standard test that a linear relation among position vectors represents a straight line.

> **Theorem (Expansion in Two Non-Collinear Vectors).** Given two non-collinear vectors $\mathbf{a}$ and $\mathbf{b}$, any vector $\mathbf{r}$ lying in their plane can be expressed as

$$
\mathbf{r}=x\mathbf{a}+y\mathbf{b}
$$

> for scalars $x,y$; in three-dimensional space, any vector can be expressed as $\mathbf{r}=x\mathbf{a}+y\mathbf{b}+z\mathbf{c}$ for scalars $x,y,z$.

## 4. Worked Exemplar Problem with Step-by-Step Solution

**Problem.** Find the unit vector parallel to the resultant of the vectors

$$
\mathbf{r}_1=2\hat{\imath}+4\hat{\jmath}-5\hat{k},\qquad \mathbf{r}_2=\hat{\imath}+2\hat{\jmath}+3\hat{k}.
$$

**Step 1 — Form the resultant by coordinatewise addition.**

$$
\mathbf{R}=\mathbf{r}_1+\mathbf{r}_2=(2+1)\hat{\imath}+(4+2)\hat{\jmath}+(-5+3)\hat{k}=3\hat{\imath}+6\hat{\jmath}-2\hat{k}.
$$

**Step 2 — Compute the magnitude of the resultant.**

$$
\lvert \mathbf{R} \rvert=\sqrt{3^{2}+6^{2}+(-2)^{2}}=\sqrt{9+36+4}=\sqrt{49}=7.
$$

**Step 3 — Normalize to obtain the unit vector.**

$$
\hat{\mathbf{r}}=\frac{\mathbf{R}}{\lvert \mathbf{R} \rvert}=\frac{1}{7}\left(3\hat{\imath}+6\hat{\jmath}-2\hat{k}\right)=\frac{3}{7}\hat{\imath}+\frac{6}{7}\hat{\jmath}-\frac{2}{7}\hat{k}.
$$

**Step 4 — Verify unit magnitude.**

$$
\lvert \hat{\mathbf{r}} \rvert=\sqrt{\left(\frac{3}{7}\right)^{2}+\left(\frac{6}{7}\right)^{2}+\left(-\frac{2}{7}\right)^{2}}=\sqrt{\frac{9+36+4}{49}}=\sqrt{\frac{49}{49}}=1.
$$

The verification confirms the normalization is correct.

**Supplementary exemplar (direction cosines).** For $\mathbf{r}=3\hat{\imath}-2\hat{\jmath}+6\hat{k}$ we have $a=3$, $b=-2$, $c=6$, and

$$
r=\sqrt{9+4+36}=\sqrt{49}=7.
$$

Hence

$$
l=\frac{3}{7},\qquad m=-\frac{2}{7},\qquad n=\frac{6}{7},
$$

and the check $l^{2}+m^{2}+n^{2}=\frac{9+4+36}{49}=1$ holds.

**Supplementary exemplar (resultant of displacements).** Let $\mathbf{A}$ be $10$ m Northwest, $\mathbf{B}$ be $20$ m at $30^{\circ}$ north of east, and $\mathbf{C}$ be $35$ m due south. The resultant is $\mathbf{D}=\mathbf{A}+\mathbf{B}+\mathbf{C}$, formed by joining the initial point of $\mathbf{A}$ to the terminal point of $\mathbf{C}$. Working graphically on a scale of $5$ m per unit, the resultant measures $4.1$ units, i.e. a magnitude of $20.5$ m, in a direction $60^{\circ}$ south of east.

**Supplementary exemplar (right-angle forces).** Let $\mathbf{P}$ be a force of $5$ N acting due East and $\mathbf{Q}$ a force of $12$ N acting due North. Since the two directions are perpendicular, the magnitude of the resultant $\mathbf{r}$ follows from the Pythagorean relation $p^{2}+q^{2}=r^{2}$:

$$
25+144=169\quad\Longrightarrow\quad r=\sqrt{169}=13\ \text{N}.
$$

## 5. High-Yield Exam Takeaways & Common Pitfalls

**High-yield takeaways.**

- A vector carries magnitude *and* direction; a scalar carries magnitude only. State both attributes when defining a vector quantity.
- The resultant of a chain of vectors is the single vector from the start of the first to the end of the last; a closed chain has zero resultant.
- Addition is commutative and associative, so the order and grouping of any number of summands is immaterial.
- Component form converts vector geometry into coordinatewise arithmetic: add or subtract component by component, then take the square root of the sum of squares for magnitude.
- The vector from $P$ to $Q$ is $\mathbf{r}_2-\mathbf{r}_1$, and its magnitude is the distance between the points.
- The unit vector is $\mathbf{A}/\lvert \mathbf{A} \rvert$; always verify that the result has magnitude $1$.
- Direction cosines are $l=a/r$, $m=b/r$, $n=c/r$, and they must satisfy $l^{2}+m^{2}+n^{2}=1$.
- The line through position vectors $\mathbf{a}$ and $\mathbf{b}$ is $\mathbf{r}=\mathbf{a}+t(\mathbf{b}-\mathbf{a})$; the coefficient-sum condition identifies straight-line relations among position vectors.

**Common pitfalls.**

- Reversing the order of subtraction when forming $\overrightarrow{PQ}$: the correct vector is terminal minus initial, $\mathbf{r}_2-\mathbf{r}_1$, not $\mathbf{r}_1-\mathbf{r}_2$.
- Forgetting that the negative of a vector reverses its sense but preserves its magnitude.
- Dividing by a zero magnitude when normalizing; the unit vector is defined only for $\mathbf{A}\neq \mathbf{0}$.
- Sign errors in the components, especially when squaring negative components — the square removes the sign, so $(-2)^{2}=4$.
- Reporting direction cosines that fail the identity $l^{2}+m^{2}+n^{2}=1$; this check should always be performed.
- Treating the magnitude of a sum as the sum of magnitudes; in general $\lvert \mathbf{A}+\mathbf{B} \rvert\neq \lvert \mathbf{A} \rvert+\lvert \mathbf{B} \rvert$ unless the vectors are parallel and similarly directed.
- Confusing the graphical scale with the physical magnitude: the measured length must be multiplied by the stated scale factor to recover the physical result.
- Assuming that a vector's position in space matters for equality; equal vectors may have different initial points provided magnitude and direction agree.

**Assessment guidance.** Assessment in this unit targets the ability to (i) distinguish scalar from vector quantities, (ii) represent vectors graphically and in component form, (iii) compute magnitudes, unit vectors, and resultants of several vectors, (iv) compute the vector joining two points and the distance between them, and (v) determine and verify direction cosines. Worked problems should be presented with the resultant formed first, the magnitude computed second, and the normalization or direction-cosine check performed last.

**Recommended reading.** The standard references supporting this unit are the texts by Davis, H.; Lewis, P.; Spiegel, M.; and Tai, C., which treat vector representation, addition, components, magnitude, unit vectors, and direction cosines in the same sequence developed here.