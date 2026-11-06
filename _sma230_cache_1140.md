## 1. Core Concept Overview & Intuition

Physical quantities fall into two broad classes. A **scalar** is fully specified by a single real number together with a unit: mass, length, time, temperature, and any real number are scalars. A **vector** requires both a magnitude and a direction: displacement, velocity, force, and acceleration are vectors. The whole of vector algebra is built on the single idea that a vector is an ordered geometric object — an arrow — and that arrows may be added, subtracted, and rescaled by numbers while obeying a small, consistent set of algebraic laws.

Geometrically, a vector is drawn as a directed line segment. The **length** of the segment encodes the magnitude according to a stated scale, the **orientation** of the segment encodes the direction, and the **arrowhead** encodes the sense. The point where the arrow begins is the **initial point**; the point where it ends is the **terminal point**. The vector from $O$ to $P$ is written $\overrightarrow{OP}$ or, analytically, as a single letter with an arrow, $\vec{A}$. Reversing the arrowhead gives $\overrightarrow{PO}$, which has the same magnitude as $\overrightarrow{OP}$ but the opposite sense, and is written $-\vec{A}$. Two vectors are **equal** precisely when they have the same magnitude and the same direction, regardless of where their initial points sit — so a vector may be translated anywhere in space without changing it.

Addition is the central operation. To add $\vec{a}$ and $\vec{b}$, draw them as a chain: start the second where the first ends. The **resultant** is the single vector joining the start of the first to the end of the second. In symbols, if $\overrightarrow{AB}=\vec{a}$ and $\overrightarrow{BC}=\vec{b}$, then $\overrightarrow{AC}=\vec{a}+\vec{b}$. Chaining many vectors $ \vec{a}+\vec{b}+\vec{c}+\vec{d} $ gives a single vector joining the start of the first to the end of the last. If the chain closes on itself — the end of the last vector coincides with the start of the first — the resultant has zero magnitude.

The intuition to carry into every examination is this: **addition of vectors is ordinary bookkeeping of displacements**. Walking $10$ m northwest, then $20$ m at $30^\circ$ north of east, then $35$ m due south leaves you at a single net displacement from your starting point, and that net displacement is the resultant. The magnitude of the resultant is found by the Pythagorean theorem when the components are perpendicular, and by resolving into perpendicular components in general.![the vector ⃗⃗⃗⃗⃗ has an initial point O and final point P and is analytically represented by a letter with an arrow over it, as.](/cdn/cloudflare/prep/visual-crops/2026/10/document-78861d46-43b4-4804-b6c3-11ae1fc63403-page-9-e84fe630.jpg)

## 2. Mathematical Formalization & Core Definitions

> **Definition (Vector and Scalar).** A vector is a quantity having both magnitude and direction, such as displacement, velocity, force, and acceleration. A scalar is a quantity having magnitude but no direction, such as mass, length, time, temperature, and any real number.

> **Definition (Vector Representation).** A vector quantity is represented graphically by a line drawn so that the length of the line denotes the magnitude according to a stated vector scale, the direction of the line denotes the direction in which the quantity acts, and an arrowhead indicates the sense. The vector $\overrightarrow{OP}$ has initial point $O$ and terminal point $P$ and is written analytically as $\vec{A}$; its magnitude is denoted $\lvert\vec{A}\rvert$ or simply $A$. The vector $\overrightarrow{PO}$ has the same magnitude but the opposite sense, so $\overrightarrow{PO}=-\vec{A}$.

> **Definition (Equality of Vectors).** Two vectors $\vec{A}$ and $\vec{B}$ are equal if they have the same magnitude and direction, regardless of the position of their initial points; thus $\vec{A}=\vec{B}$.

> **Definition (Addition of Vectors).** The sum of two vectors $\overrightarrow{AB}$ and $\overrightarrow{BC}$ is the single equivalent resultant vector $\overrightarrow{AC}$, that is $\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$, or $\vec{a}+\vec{b}=\vec{c}$. To add two vectors, draw them as a chain, starting the second where the first ends; the sum is the single vector joining the start of the first to the end of the second.

> **Definition (Components of a Vector).** Any vector $\vec{A}$ in three dimensions may be represented with initial point at the origin $O$ of a rectangular coordinate system. If $(A_1,A_2,A_3)$ are the rectangular coordinates of its terminal point, the vectors $A_1\hat{\imath}$, $A_2\hat{\jmath}$, $A_3\hat{k}$ are the component vectors of $\vec{A}$ in the $x$, $y$, and $z$ directions respectively, and the resultant is



$$
\vec{A}=A_1\hat{\imath}+A_2\hat{\jmath}+A_3\hat{k}.
$$



> **Definition (Magnitude).** The magnitude of $\vec{A}=A_1\hat{\imath}+A_2\hat{\jmath}+A_3\hat{k}$ is



$$
A=\lvert\vec{A}\rvert=\sqrt{A_1^{2}+A_2^{2}+A_3^{2}}.
$$



> In particular the position vector (radius vector) from $O$ to the point $(x,y,z)$ is $\vec{r}=x\hat{\imath}+y\hat{\jmath}+z\hat{k}$ with magnitude $\lvert\vec{r}\rvert=\sqrt{x^{2}+y^{2}+z^{2}}$.

> **Definition (Unit Vector).** A unit vector is a vector having unit magnitude. If $\vec{A}$ is a vector with magnitude $A\neq 0$, then



$$
\hat{a}=\frac{\vec{A}}{A}
$$



> is a unit vector having the same direction as $\vec{A}$.

> **Definition (Direction Cosines).** The direction of a vector in three dimensions is determined by the angles it makes with the three axes of reference. For $\overrightarrow{OP}=\vec{r}=a\hat{\imath}+b\hat{\jmath}+c\hat{k}$ with $\alpha,\beta,\gamma$ the angles made with the $x$, $y$, $z$ axes respectively,



$$
l=\cos\alpha=\frac{a}{r},\qquad m=\cos\beta=\frac{b}{r},\qquad n=\cos\gamma=\frac{c}{r},
$$



> where $r=\sqrt{a^{2}+b^{2}+c^{2}}$. The triple $[l,m,n]$ is called the direction cosines of $\overrightarrow{OP}$.

**Vector from one point to another.** If $P(x_1,y_1,z_1)$ and $Q(x_2,y_2,z_2)$ have position vectors $\vec{r}_1$ and $\vec{r}_2$, then $\vec{r}_1+\overrightarrow{PQ}=\vec{r}_2$, so



$$
\overrightarrow{PQ}=\vec{r}_2-\vec{r}_1=(x_2-x_1)\hat{\imath}+(y_2-y_1)\hat{\jmath}+(z_2-z_1)\hat{k},
$$



and its magnitude



$$
\lvert\overrightarrow{PQ}\rvert=\sqrt{(x_2-x_1)^{2}+(y_2-y_1)^{2}+(z_2-z_1)^{2}}
$$



is the distance between $P$ and $Q$. The order matters: the initial point's coordinates are subtracted from the terminal point's, so the vector always points from $P$ to $Q$. Reversing the order gives $\overrightarrow{QP}=\vec{r}_1-\vec{r}_2=-\overrightarrow{PQ}$, the same segment traversed in the opposite sense.

**The algebraic laws of addition.** If $\vec{A}$, $\vec{B}$, $\vec{C}$ are vectors and $m$, $n$ are scalars, then:

| Law | Statement | Meaning |
| --- | --- | --- |
| Commutative | $\vec{A}+\vec{B}=\vec{B}+\vec{A}$ | Order of addition is immaterial |
| Associative | $\vec{A}+(\vec{B}+\vec{C})=(\vec{A}+\vec{B})+\vec{C}$ | Grouping of addition is immaterial |

The commutative law follows from the parallelogram: with $\overrightarrow{OP}=\vec{A}$ and $\overrightarrow{PQ}=\vec{B}$ giving $\overrightarrow{OQ}=\vec{C}$, and with $\overrightarrow{OR}=\vec{B}$ and $\overrightarrow{RQ}=\vec{A}$ also giving $\overrightarrow{OQ}=\vec{C}$, both routes yield the same resultant. The associative law follows from a quadrilateral chain: $\overrightarrow{OP}+\overrightarrow{PQ}=\overrightarrow{OQ}=\vec{A}+\vec{B}$ and $\overrightarrow{PQ}+\overrightarrow{QR}=\overrightarrow{PR}=\vec{B}+\vec{C}$, and both $\overrightarrow{OP}+\overrightarrow{PR}$ and $\overrightarrow{OQ}+\overrightarrow{QR}$ equal $\overrightarrow{OR}=\vec{D}$. Hence the order of addition of any number of vectors is immaterial.

**Resolution into perpendicular components.** The practical engine of the topic is resolution. A displacement of magnitude $F$ at an angle $\theta$ measured from a reference axis contributes $F\cos\theta$ along that axis and $F\sin\theta$ perpendicular to it. Summing the contributions of every vector along each axis gives the components of the resultant, and the magnitude follows from the Pythagorean theorem. The direction is reported as an angle measured from a named axis, with the quadrant stated explicitly (for example, "south of east").

## 3. Key Theorems & Essential Results

> **Result (Magnitude of a Sum of Perpendicular Vectors).** If $\vec{p}$ and $\vec{q}$ are perpendicular, the magnitude of the resultant $\vec{r}=\vec{p}+\vec{q}$ satisfies



$$
r^{2}=p^{2}+q^{2},\qquad r=\sqrt{p^{2}+q^{2}}.
$$



> **Result (Unit Vector Parallel to a Resultant).** If $\vec{R}=\vec{r}_1+\vec{r}_2+\cdots$, then the unit vector parallel to $\vec{R}$ is



$$
\hat{r}=\frac{\vec{R}}{\lvert\vec{R}\rvert},
$$



> and it satisfies $\lvert\hat{r}\rvert=1$.

> **Result (Fundamental Identity for Direction Cosines).** For any vector with direction cosines $[l,m,n]$,



$$
l^{2}+m^{2}+n^{2}=1.
$$



> Indeed $a^{2}+b^{2}+c^{2}=r^{2}$ gives $r^{2}\cos^{2}\alpha+r^{2}\cos^{2}\beta+r^{2}\cos^{2}\gamma=r^{2}$, hence $\cos^{2}\alpha+\cos^{2}\beta+\cos^{2}\gamma=1$.

> **Result (Zero Resultant of a Closed Chain).** If a chain of vectors forms a closed figure, so that the end of the last vector coincides with the beginning of the first, the resultant sum is a vector with no magnitude, that is $\vec{a}+\vec{b}+\vec{c}+\cdots=\vec{0}$.

**Why the identity holds.** The direction cosines are the ratios of the components to the magnitude. Squaring each ratio and adding recovers the sum of the squared components divided by $r^{2}$, which is exactly $1$ because the squared components add to $r^{2}$. This identity is the standard check on any computed set of direction cosines.

## 4. Worked Exemplar Problem with Step-by-Step Solution

**Problem.** Find the sum or resultant of the following displacements: $A$: $10$ m Northwest; $B$: $20$ m at $30^\circ$ north of east; $C$: $35$ m due south. Report the magnitude and the direction of the resultant.

**Step 1 — Fix a convention.** Take east as the positive $x$-axis and north as the positive $y$-axis. A displacement of magnitude $F$ at angle $\theta$ measured from east contributes $F\cos\theta$ east and $F\sin\theta$ north; a southerly or westerly sense is recorded by the sign of the component. Northwest means $45^\circ$ north of west.

**Step 2 — Resolve each displacement.**

| Vector | Magnitude (m) | Direction | East component (m) | North component (m) |
| --- | --- | --- | --- | --- |
| $A$ | $10$ | Northwest | $-10\cos 45^\circ$ | $10\sin 45^\circ$ |
| $B$ | $20$ | $30^\circ$ north of east | $20\cos 30^\circ$ | $20\sin 30^\circ$ |
| $C$ | $35$ | due south | $0$ | $-35$ |

**Step 3 — Evaluate the components numerically.**



$$
A:\quad -10\cos 45^\circ=-7.07,\qquad 10\sin 45^\circ=7.07
$$





$$
B:\quad 20\cos 30^\circ=17.32,\qquad 20\sin 30^\circ=10.00
$$





$$
C:\quad 0.00,\qquad -35.00
$$



**Step 4 — Sum the components.**



$$
R_x=-7.07+17.32+0.00=10.25
$$





$$
R_y=7.07+10.00-35.00=-17.93
$$



**Step 5 — Compute the magnitude.**



$$
\lvert\vec{R}\rvert=\sqrt{(10.25)^{2}+(-17.93)^{2}}=\sqrt{105.06+321.48}=\sqrt{426.54}\approx 20.5\ \text{m}
$$



**Step 6 — Compute the direction.** The east component is positive and the north component is negative, so the resultant points south of east. The angle below the eastward axis is



$$
\theta=\tan^{-1}\!\left(\frac{17.93}{10.25}\right)\approx 60.2^\circ.
$$



The resultant therefore has magnitude approximately $20.5$ m in a direction approximately $60^\circ$ south of east, which is the standard answer $60^\circ$ south of east.

**Step 7 — Sanity check.** The southward pull of $C$ dominates the northward contributions of $A$ and $B$, while $B$ supplies the largest eastward contribution, so a resultant of about $20$ m pointing south-east is physically reasonable. Always state the quadrant explicitly; a bare angle is incomplete and loses marks.

**A second pattern: unit vector parallel to a resultant.** Given $\vec{r}_1=2\hat{\imath}+4\hat{\jmath}-5\hat{k}$ and $\vec{r}_2=\hat{\imath}+2\hat{\jmath}+3\hat{k}$, first form the resultant



$$
\vec{R}=\vec{r}_1+\vec{r}_2=(2+1)\hat{\imath}+(4+2)\hat{\jmath}+(-5+3)\hat{k}=3\hat{\imath}+6\hat{\jmath}-2\hat{k}.
$$



Its magnitude is



$$
\lvert\vec{R}\rvert=\sqrt{3^{2}+6^{2}+(-2)^{2}}=\sqrt{9+36+4}=\sqrt{49}=7.
$$



The unit vector parallel to $\vec{R}$ is therefore



$$
\hat{r}=\frac{\vec{R}}{\lvert\vec{R}\rvert}=\frac{1}{7}\left(3\hat{\imath}+6\hat{\jmath}-2\hat{k}\right).
$$



Verification that $\lvert\hat{r}\rvert=1$ is expected in a full answer: $\tfrac{1}{49}(9+36+4)=1$.

**A third pattern: direction cosines.** For $\vec{r}=3\hat{\imath}-2\hat{\jmath}+6\hat{k}$ we have $a=3$, $b=-2$, $c=6$ and



$$
r=\sqrt{9+4+36}=\sqrt{49}=7,
$$



so the direction cosines are



$$
l=\frac{3}{7},\qquad m=-\frac{2}{7},\qquad n=\frac{6}{7},
$$



and indeed $l^{2}+m^{2}+n^{2}=\tfrac{9+4+36}{49}=1$. Note the sign of $m$: a component in the negative $y$ direction produces an obtuse angle with the $y$-axis, and dropping that sign is a standard error.

## 5. High-Yield Exam Takeaways & Common Pitfalls

**What examiners repeatedly test.**

- The definitional distinction between scalar and vector, with correctly classified examples.
- The magnitude formula $\lvert\vec{A}\rvert=\sqrt{A_1^{2}+A_2^{2}+A_3^{2}}$ and the unit vector $\hat{a}=\vec{A}/A$.
- The vector between two points, $\overrightarrow{PQ}=\vec{r}_2-\vec{r}_1$, and its magnitude as the distance between them.
- The resultant of a set of displacements given as bearings or as "degrees north/south of east/west", requiring resolution into components.
- Direction cosines and the identity $l^{2}+m^{2}+n^{2}=1$.
- The commutative and associative laws of vector addition, with the parallelogram and quadrilateral chain justifications.

**Answer structure that earns full marks.**

1. State the coordinate convention (which axis is east, which is north) and the sign convention for southerly and westerly components.
2. Resolve every vector into its components, keeping the trigonometric factor explicit before evaluating numerically.
3. Sum the components axis by axis, showing the arithmetic.
4. Compute the magnitude with the Pythagorean formula and the direction with the tangent ratio, naming the quadrant.
5. For unit-vector questions, divide by the magnitude and verify that the result has unit magnitude.
6. For direction-cosine questions, compute $r$ first, then each ratio, and check $l^{2}+m^{2}+n^{2}=1$.

**Common pitfalls.**

- Reporting a bare angle without naming the axis or quadrant; this is incomplete and loses marks.
- Dropping the sign of a component that points south or west, which corrupts both the magnitude and the direction.
- Confusing the order in $\overrightarrow{PQ}=\vec{r}_2-\vec{r}_1$; reversing it gives $-\overrightarrow{PQ}$, the opposite vector.
- Forgetting to divide by the magnitude when forming a unit vector, or dividing by the wrong quantity such as the sum of the components.
- Writing a direction cosine without its sign, which misplaces the vector in the wrong octant.
- Treating the magnitude of a sum as the sum of the magnitudes; $\lvert\vec{A}+\vec{B}\rvert=\lvert\vec{A}\rvert+\lvert\vec{B}\rvert$ holds only when the vectors are parallel and in the same sense.