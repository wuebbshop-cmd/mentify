## 1. Core Concept Overview & Intuition

### 1.1 Lesson Learning Outcomes

By the end of this unit, a learner should be able to:

- Explain, in plain words, the difference between a scalar quantity and a vector quantity.
- Represent a vector graphically by a directed line segment, and read its magnitude and direction from that line.
- Add two or more vectors by the chain (tip-to-tail) method and identify the resultant.
- State and use the commutative and associative laws of vector addition.
- Resolve a vector into components along the $x$, $y$ and $z$ axes and write it in the form $A = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}$.
- Compute the magnitude of a vector using the three-dimensional form of Pythagoras' theorem.
- Construct a unit vector in the direction of any given non-zero vector.
- Find the vector joining two given points and compute the distance between those points.
- Compute the direction cosines of a vector and verify the identity $l^2 + m^2 + n^2 = 1$.

### 1.2 The Everyday Idea Behind a Vector

Imagine you are giving a friend directions to a shop. It is not enough to say "walk $500$ metres." Your friend also needs to know which way to walk. The distance alone is a **scalar**: it has size but no direction. The instruction "walk $500$ metres due north" is a **vector**: it has both size and direction.

The same distinction appears everywhere. Mass, length, time and temperature are scalars — you can state them with a single number and a unit. Displacement, velocity, force and acceleration are vectors — a single number is not enough; a direction must accompany it.

Where the analogy stops being exact: in mathematics a vector is not tied to a physical journey. It is an abstract object with a length and a direction, and we are free to slide it anywhere in space without changing it, as long as we do not rotate it or stretch it.

### 1.3 Drawing a Vector

A vector is drawn as a straight line with an arrowhead. Three things are encoded in the drawing:

- The **length** of the line gives the magnitude, measured against some stated scale (for example, $1$ cm on paper represents $5$ m in reality).
- The **direction** of the line gives the line along which the vector acts.
- The **arrowhead** gives the sense — which of the two opposite ways along that line the vector points.

The point where the arrow starts is the **initial point**; the point where the arrowhead sits is the **terminal point**. A vector from $O$ to $P$ is written $\overrightarrow{OP}$ or simply $A$, and its magnitude is written $\lvert A \rvert$ or $A$. Reversing the arrow gives $\overrightarrow{PO}$, which has the same magnitude but the opposite sense, and is written $-A$.

Two vectors are **equal** if they have the same magnitude and the same direction, no matter where in space they are drawn. This is why we may slide a vector around freely when adding vectors.

### 1.4 Adding Vectors by Chaining

To add two vectors $a$ and $b$, draw $a$, then start $b$ where $a$ ends. The **resultant** $c$ is the single vector from the start of $a$ to the end of $b$. In symbols, if $a = \overrightarrow{AB}$ and $b = \overrightarrow{BC}$, then

$$
\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}
$$

or, more briefly, $a + b = c$.

For several vectors $a, b, c, d$, chain them one after another. The resultant is the single vector joining the start of the first to the end of the last. If the chain closes up into a closed figure — the end of the last vector coincides with the start of the first — then the resultant has no magnitude; it is the zero vector.

A useful special case: if two forces act at right angles, the size of their resultant is found by Pythagoras' theorem. A force of $5$ N due east and a force of $12$ N due north combine to give a resultant of size $13$ N, because $5^2 + 12^2 = 25 + 144 = 169$ and $\sqrt{169} = 13$.

### 1.5 Components: Breaking a Vector into Three Pieces

Any vector in three dimensions can be placed with its initial point at the origin $O$ of a rectangular coordinate system. If the terminal point has coordinates $(A_1, A_2, A_3)$, then the vector can be written as the sum of three pieces, one along each axis:

$$
A = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}
$$

Here $\hat{i}$, $\hat{j}$ and $\hat{k}$ are the unit vectors along the $x$, $y$ and $z$ axes respectively. The numbers $A_1$, $A_2$, $A_3$ are called the **components** of $A$, and the three vectors $A_1\hat{i}$, $A_2\hat{j}$, $A_3\hat{k}$ are called the **component vectors**.

The special vector from the origin to the point $(x, y, z)$ is called the **position vector** (or radius vector):

$$
r = x\hat{i} + y\hat{j} + z\hat{k}
$$

### 1.6 Magnitude, Unit Vector and Resultant — the Three Central Tools

These three ideas are the working tools of the whole unit, so it is worth stating each in one plain sentence before formalising them.

- The **magnitude** answers the question "how long is this vector?" It is a single non-negative number.
- A **unit vector** answers the question "which way does this vector point?" It is a vector of length exactly $1$ in the same direction.
- The **resultant** answers the question "what single vector has the same effect as all these vectors together?" It is the sum.

The rest of these notes builds each tool carefully, then shows them working together in a fully worked example.

## 2. Mathematical Formalization & Core Definitions

### 2.1 Scalars and Vectors

> **Definition (Vector).** A vector is a quantity having both magnitude and direction, such as displacement, velocity, force and acceleration.

> **Definition (Scalar).** A scalar is a quantity having magnitude but no direction, for example mass, length, time, temperature, and any real number.

### 2.2 Vector Representation and Equality

A vector quantity is represented graphically by a line drawn so that:

- the length of the line denotes the magnitude of the quantity, according to some stated vector scale;
- the direction of the line denotes the direction in which the vector quantity acts;
- an arrowhead indicates the sense of the direction.

The vector $\overrightarrow{OP}$ has initial point $O$ and terminal point $P$, and is written analytically as $A$. Its magnitude is denoted by $\lvert A \rvert$ or $A$. The vector $\overrightarrow{PO}$ has the same magnitude but the opposite sense, and is written $-A$.

> **Definition (Equal vectors).** Two vectors $A$ and $B$ are equal if they have the same magnitude and the same direction, regardless of the position of their initial points. Thus $A = B$.

### 2.3 Addition of Vectors

> **Definition (Sum of two vectors).** The sum of two vectors $\overrightarrow{AB}$ and $\overrightarrow{BC}$ is the single, equivalent, or resultant vector $\overrightarrow{AC}$:

> 

$$
> \overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}
>
$$

> or, in letters, $a + b = c$.

To find the sum of two vectors $a$ and $b$, draw them as a chain, starting the second where the first ends; the sum $c$ is the single vector joining the start of the first to the end of the second.

For a chain of several vectors $a + b + c + d$, proceed step by step:

$$
\begin{aligned}
a + b &= \overrightarrow{AC} \\
\overrightarrow{AC} + c &= \overrightarrow{AD} \\
\overrightarrow{AD} + d &= \overrightarrow{AE}
\end{aligned}
$$

so that $a + b + c + d = \overrightarrow{AE}$. The sum of all the vectors is the single vector joining the start of the first to the end of the last. If the vector diagram is a closed figure — the end of the last vector coincides with the beginning of the first — the resultant sum is a vector with no magnitude.

### 2.4 The Laws of Vector Algebra

If $A$, $B$ and $C$ are vectors and $m$ and $n$ are scalars, then:

> **Law 1 (Commutative law of addition).** $A + B = B + A$.

The justification is direct. With $O$, $P$, $Q$, $R$ forming a parallelogram, $\overrightarrow{OP} + \overrightarrow{PQ} = \overrightarrow{OQ}$, that is $A + B = C$; and $\overrightarrow{OR} + \overrightarrow{RQ} = \overrightarrow{OQ}$, that is $B + A = C$. Since both sums equal the same vector $C$, we have $A + B = B + A$.

> **Law 2 (Associative law of addition).** $A + (B + C) = (A + B) + C$.

The justification again uses a chain. With points $O$, $P$, $Q$, $R$ and $D$ arranged so that $\overrightarrow{OP} = A$, $\overrightarrow{PQ} = B$, $\overrightarrow{QR} = C$:

$$
\begin{aligned}
\overrightarrow{OP} + \overrightarrow{PQ} &= \overrightarrow{OQ} = A + B \\
\overrightarrow{PQ} + \overrightarrow{QR} &= \overrightarrow{PR} = B + C \\
\overrightarrow{OP} + \overrightarrow{PR} &= \overrightarrow{OR} = D \quad \text{so} \quad A + (B + C) = D \\
\overrightarrow{OQ} + \overrightarrow{QR} &= \overrightarrow{OR} = D \quad \text{so} \quad (A + B) + C = D
\end{aligned}
$$

Both groupings give the same vector $D$, hence $A + (B + C) = (A + B) + C$. Thus the order of addition of any number of vectors is immaterial.

### 2.5 Components of a Vector

Any vector $A$ in three dimensions can be represented with initial point at the origin $O$ of a rectangular coordinate system. Let $(A_1, A_2, A_3)$ be the rectangular coordinates of the terminal point of $A$. The vectors $A_1\hat{i}$, $A_2\hat{j}$ and $A_3\hat{k}$ are the component vectors of $A$ in the $x$, $y$ and $z$ directions respectively. The resultant of these three is $A$ itself:

$$
A = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}
$$

In particular, the position vector (radius vector) $r$ from $O$ to the point $(x, y, z)$ is

$$
r = x\hat{i} + y\hat{j} + z\hat{k}
$$

### 2.6 Magnitude of a Vector

The magnitude of a vector is shown by two vertical bars on either side of the vector. Given the vector $A = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}$, the magnitude is denoted by $\lvert A \rvert$ and is defined by applying Pythagoras' theorem twice — once in the base plane and once vertically:

$$
\lvert A \rvert = \sqrt{A_1^2 + A_2^2 + A_3^2}
$$

For the position vector $r = x\hat{i} + y\hat{j} + z\hat{k}$ this becomes

$$
\lvert r \rvert = r = \sqrt{x^2 + y^2 + z^2}
$$

### 2.7 Unit Vector

> **Definition (Unit vector).** A unit vector is a vector having unit magnitude. If $A$ is a vector with magnitude $\lvert A \rvert \neq 0$, then

> 

$$
> \hat{a} = \frac{A}{\lvert A \rvert}
>
$$

> is a unit vector having the same direction as $A$.

The construction is simply "divide the vector by its own length." The direction is unchanged because we divided by a positive number; the length becomes $1$ because $\lvert A \rvert / \lvert A \rvert = 1$.

### 2.8 Vector Joining Two Points and Distance Between Them

Let $P$ have coordinates $(x_1, y_1, z_1)$ and $Q$ have coordinates $(x_2, y_2, z_2)$. Their position vectors are

$$
\begin{aligned}
r_1 &= x_1\hat{i} + y_1\hat{j} + z_1\hat{k} \\
r_2 &= x_2\hat{i} + y_2\hat{j} + z_2\hat{k}
\end{aligned}
$$

Since $r_1 + \overrightarrow{PQ} = r_2$, we obtain

$$
\overrightarrow{PQ} = r_2 - r_1 = (x_2 - x_1)\hat{i} + (y_2 - y_1)\hat{j} + (z_2 - z_1)\hat{k}
$$

The magnitude of $\overrightarrow{PQ}$ is the distance between $P$ and $Q$:

$$
\lvert \overrightarrow{PQ} \rvert = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}
$$

### 2.9 Direction Cosines

The direction of a vector in three dimensions is determined by the angles it makes with the three axes of reference. Let

$$
\overrightarrow{OP} = r = a\hat{i} + b\hat{j} + c\hat{k}
$$

and let $\alpha$, $\beta$, $\gamma$ be the angles the vector makes with the $x$, $y$ and $z$ axes respectively. Then

$$
\begin{aligned}
\frac{a}{r} &= \cos\alpha \quad \text{so} \quad a = r\cos\alpha \\
\frac{b}{r} &= \cos\beta \quad \text{so} \quad b = r\cos\beta \\
\frac{c}{r} &= \cos\gamma \quad \text{so} \quad c = r\cos\gamma
\end{aligned}
$$

> **Definition (Direction cosines).** The numbers $[l, m, n]$ written in square brackets are called the direction cosines of the vector $\overrightarrow{OP}$; they are the cosines of the angles which the vector makes with the three axes of reference. For $r = a\hat{i} + b\hat{j} + c\hat{k}$,

> 

$$
> l = \frac{a}{r}, \qquad m = \frac{b}{r}, \qquad n = \frac{c}{r}
>
$$

> where $r = \sqrt{a^2 + b^2 + c^2}$.

## 3. Key Theorems & Essential Results

### 3.1 The Direction Cosine Identity

> **Theorem.** For any vector with direction cosines $l$, $m$, $n$,

> 

$$
> l^2 + m^2 + n^2 = 1
>
$$

**Proof.** Start from the component relations $a = r\cos\alpha$, $b = r\cos\beta$, $c = r\cos\gamma$ and from the magnitude relation $a^2 + b^2 + c^2 = r^2$. Substituting the component relations into the magnitude relation gives

$$
\begin{aligned}
r^2\cos^2\alpha + r^2\cos^2\beta + r^2\cos^2\gamma &= r^2 \\
\cos^2\alpha + \cos^2\beta + \cos^2\gamma &= 1
\end{aligned}
$$

Writing $l = \cos\alpha$, $m = \cos\beta$, $n = \cos\gamma$ yields $l^2 + m^2 + n^2 = 1$. $\blacksquare$

This identity is a powerful check: any triple of numbers offered as direction cosines must satisfy it, and any two of the three determine the third up to sign.

### 3.2 The Unit Vector Result

> **Result.** If $A$ is a non-zero vector, then $\hat{a} = A / \lvert A \rvert$ has magnitude $1$ and the same direction as $A$.

**Proof.** The magnitude of $\hat{a}$ is $\lvert A \rvert / \lvert A \rvert = 1$. Since $\lvert A \rvert > 0$, dividing by it does not reverse the direction. $\blacksquare$

### 3.3 The Resultant of a Chain

> **Result.** For vectors $a, b, c, d$ drawn as a chain, the resultant is the single vector joining the start of the first to the end of the last. If the chain closes, the resultant is the zero vector.

This follows by repeated application of the definition of vector addition, as shown in Section 2.3.

### 3.4 The Distance Formula

> **Result.** The distance between points $P(x_1, y_1, z_1)$ and $Q(x_2, y_2, z_2)$ is

> 

$$
> \lvert \overrightarrow{PQ} \rvert = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}
>
$$

This is the three-dimensional form of Pythagoras' theorem, obtained by taking the magnitude of the difference of the two position vectors.

### 3.5 The Parallelogram Diagonal Result

> **Result.** In a parallelogram with adjacent side vectors $a$ and $b$, the diagonals are $a + b$ and $b - a$, and the diagonals bisect each other.

**Proof.** Let the parallelogram have vertices with $\overrightarrow{AC} = a + b$ and $\overrightarrow{BD} = b - a$. Let $P$ be the point where the diagonals meet. Write $\overrightarrow{AP} = x\,\overrightarrow{AC}$ and $\overrightarrow{BP} = y\,\overrightarrow{BD}$ for scalars $x$ and $y$. Then

$$
\overrightarrow{AB} + \overrightarrow{BP} = \overrightarrow{AP}
$$

so that

$$
a + y(b - a) = x(a + b)
$$

Comparing coefficients of $a$ and of $b$ on the left and right gives $x = y = \tfrac{1}{2}$, so $P$ is the midpoint of both diagonals. $\blacksquare$

### 3.6 The Equation of a Straight Line Through Two Points

> **Result.** The straight line through points with position vectors $a$ and $b$ consists of all points with position vector

> 

$$
> r = a + t(b - a)
>
$$

> where $t$ is a scalar.

**Derivation.** Let $r$ be the position vector of any point $P$ on the line through $A$ and $B$. Then $\overrightarrow{OA} + \overrightarrow{AP} = \overrightarrow{OP}$, and since $\overrightarrow{AP} = t\,\overrightarrow{AB}$ for some scalar $t$,

$$
\begin{aligned}
\overrightarrow{OP} &= \overrightarrow{OA} + t\,\overrightarrow{AB} \\
r &= a + t(b - a)
\end{aligned}
$$

If the equation is written as $a - ta - tb - r = 0$, the sum of the coefficients of the vectors is zero, which is the standard test that the four vectors are coplanar in the sense of lying in one line configuration.

## 4. Worked Exemplar Problem with Step-by-Step Solution

### 4.1 The Problem

Find the unit vector parallel to the resultant of the vectors

$$
r_1 = 2\hat{i} + 4\hat{j} - 5\hat{k}, \qquad r_2 = \hat{i} + 2\hat{j} + 3\hat{k}
$$

### 4.2 Step 1 — Form the Resultant

Add the two vectors component by component: add the $\hat{i}$ parts together, the $\hat{j}$ parts together, and the $\hat{k}$ parts together.

$$
\begin{aligned}
R &= r_1 + r_2 \\
&= (2\hat{i} + 4\hat{j} - 5\hat{k}) + (\hat{i} + 2\hat{j} + 3\hat{k}) \\
&= 3\hat{i} + 6\hat{j} - 2\hat{k}
\end{aligned}
$$

In words: the $x$-component is $2 + 1 = 3$; the $y$-component is $4 + 2 = 6$; the $z$-component is $-5 + 3 = -2$.

### 4.3 Step 2 — Compute the Magnitude of the Resultant

Square each component, add the squares, and take the square root.

$$
\begin{aligned}
\lvert R \rvert &= \sqrt{3^2 + 6^2 + (-2)^2} \\
&= \sqrt{9 + 36 + 4} \\
&= \sqrt{49} \\
&= 7
\end{aligned}
$$

The resultant has length $7$.

### 4.4 Step 3 — Divide by the Magnitude

A unit vector in the direction of $R$ is obtained by dividing $R$ by its magnitude:

$$
\hat{r} = \frac{R}{\lvert R \rvert} = \frac{1}{7}\left(3\hat{i} + 6\hat{j} - 2\hat{k}\right)
$$

Equivalently, component by component,

$$
\hat{r} = \frac{3}{7}\hat{i} + \frac{6}{7}\hat{j} - \frac{2}{7}\hat{k}
$$

### 4.5 Step 4 — Verify the Answer

Check that the result really has length $1$:

$$
\begin{aligned}
\lvert \hat{r} \rvert &= \sqrt{\left(\frac{3}{7}\right)^2 + \left(\frac{6}{7}\right)^2 + \left(-\frac{2}{7}\right)^2} \\
&= \sqrt{\frac{9}{49} + \frac{36}{49} + \frac{4}{49}} \\
&= \sqrt{\frac{49}{49}} \\
&= 1
\end{aligned}
$$

The verification succeeds, so the unit vector is correct.

### 4.6 A Second Worked Example — Direction Cosines

Find the direction cosines $[l, m, n]$ of the vector $r = 3\hat{i} - 2\hat{j} + 6\hat{k}$.

Here $a = 3$, $b = -2$, $c = 6$. First compute the magnitude:

$$
\begin{aligned}
r &= \sqrt{3^2 + (-2)^2 + 6^2} \\
&= \sqrt{9 + 4 + 36} \\
&= \sqrt{49} \\
&= 7
\end{aligned}
$$

Then divide each component by the magnitude:

$$
l = \frac{3}{7}, \qquad m = -\frac{2}{7}, \qquad n = \frac{6}{7}
$$

As a check, $l^2 + m^2 + n^2 = \frac{9}{49} + \frac{4}{49} + \frac{36}{49} = \frac{49}{49} = 1$, as the identity requires.

### 4.7 A Third Worked Example — Vector Between Two Points

Find the vector with initial point $P(x_1, y_1, z_1)$ and terminal point $Q(x_2, y_2, z_2)$, and its magnitude.

The position vectors are $r_1 = x_1\hat{i} + y_1\hat{j} + z_1\hat{k}$ and $r_2 = x_2\hat{i} + y_2\hat{j} + z_2\hat{k}$. Since $r_1 + \overrightarrow{PQ} = r_2$,

$$
\overrightarrow{PQ} = r_2 - r_1 = (x_2 - x_1)\hat{i} + (y_2 - y_1)\hat{j} + (z_2 - z_1)\hat{k}
$$

and its magnitude, which is the distance between $P$ and $Q$, is

$$
\lvert \overrightarrow{PQ} \rvert = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}
$$

### 4.8 A Fourth Worked Example — Resultant of Displacements

Find the resultant of the displacements: $A$ of $10$ m northwest; $B$ of $20$ m at $30^\circ$ north of east; $C$ of $35$ m due south.

Draw the three displacements as a chain, using a stated scale such as $1$ cm representing $5$ m. Start $B$ where $A$ ends, and start $C$ where $B$ ends. The resultant $D$ is the single vector from the start of $A$ to the end of $C$, so $D = A + B + C$. Measuring the resultant against the scale gives a magnitude of about $4.1$ scale units, that is $20.5$ m, and a direction of about $60^\circ$ south of east.

The lesson here is that the chain method works for any number of vectors, and that a careful scale drawing gives both the magnitude and the direction of the resultant.

## 5. High-Yield Exam Takeaways & Common Pitfalls

### 5.1 High-Yield Takeaways

- **Scalar versus vector.** A scalar has magnitude only; a vector has magnitude and direction. Be ready to classify a list of physical quantities.
- **Equality of vectors.** Two vectors are equal when both magnitude and direction agree, regardless of where they are drawn. Sliding a vector does not change it; reversing it multiplies it by $-1$.
- **Chain rule for addition.** Place vectors tip to tail; the resultant runs from the first tail to the last tip. A closed chain gives the zero vector.
- **The two laws.** Addition is commutative, $A + B = B + A$, and associative, $A + (B + C) = (A + B) + C$. These justify adding vectors in any order.
- **Component form.** $A = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}$, and the position vector of $(x, y, z)$ is $r = x\hat{i} + y\hat{j} + z\hat{k}$.
- **Magnitude formula.** $\lvert A \rvert = \sqrt{A_1^2 + A_2^2 + A_3^2}$. This is Pythagoras' theorem applied twice.
- **Unit vector formula.** $\hat{a} = A / \lvert A \rvert$, valid only when $\lvert A \rvert \neq 0$.
- **Distance formula.** $\lvert \overrightarrow{PQ} \rvert = \sqrt{(x_2 - x_1)^)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$.
- **Direction cosines.** $l = a/r$, $m = b/r$, $n = c/r$ with $r = \sqrt{a^2 + b^2 + c^2}$, and always $l^2 + m^2 + n^2 = 1$.
- **Line through two points.** $r = a + t(b - a)$ with $t$ a scalar; the sum of the coefficients of the vectors in the rearranged form is zero.
- **Parallelogram diagonals.** The diagonals are $a + b$ and $b - a$, and they bisect each other at their common midpoint.

### 5.2 Common Pitfalls

- **Forgetting the direction.** Writing only "a force of $5$ N" is incomplete; a vector answer must state magnitude and direction, or be given in component form.
- **Sign errors in components.** A component such as $-5$ must be squared as $(-5)^2 = 25$, not $-25$. The magnitude is never negative.
- **Dropping the square root.** The magnitude is $\sqrt{A_1^2 + A_2^2 + A_3^2}$, not $A_1^2 + A_2^2 + A_3^2$. The squared quantity is the square of the length, not the length.
- **Dividing by zero.** A unit vector exists only for a non-zero vector. If $\lvert A \rvert = 0$, the expression $A/\lvert A \rvert$ is undefined.
- **Reversing the subtraction.** The vector from $P$ to $Q$ is $r_2 - r_1$, not $r_1 - r_2$. Reversing it gives the opposite direction.
- **Mixing up direction cosines with components.** The components are $a$, $b$, $c$; the direction cosines are $a/r$, $b/r$, $c/r$. They are not the same numbers unless $r = 1$.
- **Forgetting the identity check.** After computing direction cosines, always verify $l^2 + m^2 + n^2 = 1$. If it fails, an arithmetic slip has occurred.
- **Assuming a closed chain has a non-zero resultant.** If the end of the last vector meets the start of the first, the resultant is the zero vector, not the perimeter.
- **Adding magnitudes instead of vectors.** Two vectors of magnitudes $5$ and $12$ do not generally have resultant $17$; that happens only when they point the same way. At right angles the resultant is $13$.
- **Losing the scale in graphical work.** When a drawing is used, state the scale and measure both magnitude and direction; a magnitude without a direction is only half the answer.

### 5.3 Recommended Reading

The following standard texts support the material in this unit and are useful for further practice:

- Davis, H. — introductory treatments of vector representation, components and vector algebra.
- Lewis, P. — worked exercises on magnitude, unit vectors and resultants.
- Spiegel, M. — extensive solved problems on vectors and scalars, components and direction cosines.
- Tai, C. — vector methods with applications to geometry and mechanics.

### 5.4 Assessment Guidance

Assessment in this unit typically asks the learner to:

- define scalar and vector quantities and classify given physical quantities;
- draw a chain of vectors to a stated scale and read off the resultant;
- state and illustrate the commutative and associative laws of addition;
- express a vector in component form and compute its magnitude;
- find a unit vector parallel to a given vector or to a resultant;
- find the vector joining two points and the distance between them;
- compute direction cosines and verify the identity $l^2 + m^2 + n^2 = 1$;
- prove elementary geometric results such as the bisection of parallelogram diagonals, and derive the equation of a line through two points.

A sound strategy for any assessment item is to write the vectors in component form first, then apply the magnitude, unit vector or direction cosine formula, and finally verify the answer against the identity or by substitution.