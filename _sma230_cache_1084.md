## 1. Core Concept Overview & Intuition

The reciprocal set of vectors is a construction that, given a set of three non-coplanar vectors, produces a second set of three vectors with a very specific mutual relationship. The guiding geometric idea is stated plainly in the course material: reciprocal vectors are formed by choosing a vector perpendicular to two lattice vectors and of length reciprocal to the third lattice vector. In other words, each member of the reciprocal set is built so that it is orthogonal to the two vectors it is *not* paired with, while its length is controlled by the vector it *is* paired with.

The single-vector version of the idea is the simplest entry point. The vector which has the same direction as a given vector but has magnitude reciprocal to that of the given vector is called the reciprocal of that vector. So if a vector has length $5$, its reciprocal points the same way but has length $1/5$. This is a pure rescaling along a fixed direction, and it already contains the essential feature of the full construction: direction is preserved, magnitude is inverted.

The full reciprocal set extends this to three vectors simultaneously. Given a set of three vectors, the reciprocal set consists of three vectors chosen so that each one is perpendicular to the other two members of the original set and has magnitude equal to the reciprocal of the remaining member. The defining property that makes the construction useful is the pattern of dot products between the original set and the reciprocal set: each vector of the original set has a dot product of unity with its own reciprocal partner and a dot product of zero with the other two reciprocal vectors. This is the vector-algebra analogue of an orthonormal basis, except that the original vectors need not be orthogonal or of unit length.

Intuition for why such a set must exist: three non-coplanar vectors span all of three-dimensional space, so any vector can be written as a combination of them. The reciprocal set is precisely the set of vectors that "reads off" the coefficients in such a combination. If a vector is expressed as a sum of scalar multiples of the original three vectors, then dotting with the corresponding reciprocal vector isolates the matching coefficient, because all the other dot products vanish. This is the mechanism that makes reciprocal sets valuable in later applications, and it is the reason the course asks you to evaluate dot products between a vector and its reciprocal.

The construction is closely tied to the cross product and the scalar triple product, both of which are prior knowledge for this unit. The cross product of two vectors is perpendicular to both, which supplies the required perpendicularity; the scalar triple product of the three original vectors measures the volume they span and supplies the normalising factor that produces the reciprocal magnitudes. The whole evaluation therefore reduces to computing three cross products and dividing by one scalar triple product.

## 2. Mathematical Formalization & Core Definitions

> **Definition (Reciprocal of a single vector).** Let $\vec{a}$ be a non-zero vector. The vector which has the same direction as $\vec{a}$ but magnitude reciprocal to that of $\vec{a}$ is called the reciprocal of $\vec{a}$.

Writing $\lVert \vec{a} \rVert$ for the magnitude of $\vec{a}$, the reciprocal of $\vec{a}$ is the vector



$$
\frac{\vec{a}}{\lVert \vec{a} \rVert^{2}}
$$



because this vector is a positive scalar multiple of $\vec{a}$ (hence has the same direction) and its magnitude is



$$
\left\lVert \frac{\vec{a}}{\lVert \vec{a} \rVert^{2}} \right\rVert
=
\frac{\lVert \vec{a} \rVert}{\lVert \vec{a} \rVert^{2}}
=
\frac{1}{\lVert \vec{a} \rVert}
$$



which is the reciprocal of the magnitude of $\vec{a}$. The unit vector in the direction of $\vec{a}$ is $\hat{a}=\vec{a}/\lVert \vec{a} \rVert$, and the reciprocal of $\vec{a}$ can equally be written as $\hat{a}/\lVert \vec{a} \rVert$, confirming that direction is preserved and only the length is inverted.

> **Definition (Reciprocal set of vectors).** Let $\vec{a}$, $\vec{b}$, $\vec{c}$ be three non-coplanar vectors, so that their scalar triple product $\vec{a}\cdot(\vec{b}\times\vec{c})$ is non-zero. The reciprocal set is the triple $\vec{a}'$, $\vec{b}'$, $\vec{c}'$ defined by



$$
> \vec{a}'=\frac{\vec{b}\times\vec{c}}{\vec{a}\cdot(\vec{b}\times\vec{c})},
> \qquad
> \vec{b}'=\frac{\vec{c}\times\vec{a}}{\vec{a}\cdot(\vec{b}\times\vec{c})},
> \qquad
> \vec{c}'=\frac{\vec{a}\times\vec{b}}{\vec{a}\cdot(\vec{b}\times\vec{c})}.
$$



Each definition is read directly off the geometric description. The vector $\vec{a}'$ is proportional to $\vec{b}\times\vec{c}$, so it is perpendicular to both $\vec{b}$ and $\vec{c}$; its length is reciprocal to the length of $\vec{a}$ in the sense that the normalising denominator is the volume spanned by the three original vectors. The cyclic order of the cross products is what pairs each reciprocal vector with the correct original vector.

The symbols used throughout are as follows. The arrows denote vectors in three-dimensional space; $\times$ denotes the cross product; $\cdot$ denotes the dot product; $\lVert \vec{a} \rVert$ denotes magnitude; and $\vec{a}\cdot(\vec{b}\times\vec{c})$ denotes the scalar triple product, a real number equal to the signed volume of the parallelepiped spanned by the three vectors. The hats $\hat{i}$, $\hat{j}$, $\hat{k}$ denote the standard mutually perpendicular unit vectors along the coordinate axes.

> **Definition (Dot-product pairing property).** The reciprocal set satisfies



$$
> \vec{a}\cdot\vec{a}'=1,\quad \vec{b}\cdot\vec{b}'=1,\quad \vec{c}\cdot\vec{c}'=1,
$$



> and



$$
> \vec{a}\cdot\vec{b}'=\vec{a}\cdot\vec{c}'=\vec{b}\cdot\vec{a}'=\vec{b}\cdot\vec{c}'=\vec{c}\cdot\vec{a}'=\vec{c}\cdot\vec{b}'=0.
$$



This is the property the course discussion asks you to investigate: the dot product between a vector and its own reciprocal is unity, and the dot product between a vector and any other member of the reciprocal set is zero. It is the exact analogue of the Kronecker delta relation for an orthonormal basis, generalised to a non-orthogonal set.

## 3. Key Theorems & Essential Results

> **Theorem (Existence and uniqueness of the reciprocal set).** Let $\vec{a}$, $\vec{b}$, $\vec{c}$ be non-coplanar vectors. Then the reciprocal set exists, is unique, and is given by the cross-product formulas of the previous section.

The non-coplanarity condition is exactly the statement that the scalar triple product is non-zero, so the denominator in each formula is a non-zero real number and each reciprocal vector is well defined. Uniqueness follows because the perpendicularity and magnitude conditions pin down each reciprocal vector completely: a vector perpendicular to two non-parallel vectors must lie along their cross product, and the magnitude condition then fixes the scalar multiple.

> **Theorem (Pairing property).** For the reciprocal set defined above, the dot products satisfy $\vec{a}\cdot\vec{a}'=1$ and $\vec{a}\cdot\vec{b}'=\vec{a}\cdot\vec{c}'=0$, with the analogous statements obtained by cyclic permutation of $\vec{a}$, $\vec{b}$, $\vec{c}$.

The vanishing dot products are immediate from the perpendicularity built into the cross products: $\vec{b}'$ is proportional to $\vec{c}\times\vec{a}$, which is perpendicular to $\vec{a}$, so $\vec{a}\cdot\vec{b}'=0$. The unit dot product follows because the numerator $\vec{a}\cdot(\vec{b}\times\vec{c})$ cancels the identical denominator.

> **Theorem (Reciprocity is symmetric).** The original set is the reciprocal set of its reciprocal set. That is, applying the construction twice returns the vectors you started with.

This result is what justifies the word "reciprocal": the relationship between the two sets is mutual, not one-directional. It also explains why the construction is often described as producing a "dual" set.

> **Theorem (Expansion of a vector in a non-orthogonal basis).** Any vector $\vec{r}$ can be written as



$$
> \vec{r}=(\vec{r}\cdot\vec{a}')\,\vec{a}+(\vec{r}\cdot\vec{b}')\,\vec{b}+(\vec{r}\cdot\vec{c}')\,\vec{c}.
$$



This is the payoff of the pairing property. Because the reciprocal vectors isolate individual coefficients, the coefficients of $\vec{r}$ in the basis $\{\vec{a},\vec{b},\vec{c}\}$ are obtained by dotting $\vec{r}$ with the corresponding reciprocal vectors. This is the precise sense in which the reciprocal set "reads off" coordinates, and it is the reason the construction appears whenever a non-orthogonal basis must be used.

> **Theorem (Reciprocal of the standard unit vectors).** For the standard set $\hat{i}$, $\hat{j}$, $\hat{k}$, the reciprocal set is $\hat{i}$, $\hat{j}$, $\hat{k}$ itself.

The standard unit vectors are mutually perpendicular and of unit length, so their scalar triple product equals $1$ and each cross product of two of them returns the third. The construction therefore reproduces the same set, which is consistent with the symmetry theorem.

## 4. Worked Exemplar Problem with Step-by-Step Solution

The assessment task in the course material is to find a set of vectors reciprocal to a given set of three vectors. The standard unit vectors form the cleanest illustration of the method, and the same three steps apply to any non-coplanar set.

**Problem.** Find a set of vectors reciprocal to the set $\hat{i}$, $\hat{j}$, $\hat{k}$.

**Step 1: Compute the scalar triple product of the original set.**

The scalar triple product is



$$
\hat{i}\cdot(\hat{j}\times\hat{k})=\hat{i}\cdot\hat{i}=1.
$$



Since this is non-zero, the three vectors are non-coplanar and the reciprocal set exists.

**Step 2: Compute the three cross products in cyclic order.**



$$
\hat{j}\times\hat{k}=\hat{i},
\qquad
\hat{k}\times\hat{i}=\hat{j},
\qquad
\hat{i}\times\hat{j}=\hat{k}.
$$



**Step 3: Divide each cross product by the scalar triple product.**



$$
\hat{i}'=\frac{\hat{j}\times\hat{k}}{\hat{i}\cdot(\hat{j}\times\hat{k})}=\frac{\hat{i}}{1}=\hat{i},
$$





$$
\hat{j}'=\frac{\hat{k}\times\hat{i}}{\hat{i}\cdot(\hat{j}\times\hat{k})}=\frac{\hat{j}}{1}=\hat{j},
$$





$$
\hat{k}'=\frac{\hat{i}\times\hat{j}}{\hat{i}\cdot(\hat{j}\times\hat{k})}=\frac{\hat{k}}{1}=\hat{k}.
$$



**Conclusion.** The reciprocal set of $\{\hat{i},\hat{j},\hat{k}\}$ is $\{\hat{i},\hat{j},\hat{k}\}$ itself. This is the expected outcome, because the standard unit vectors already satisfy the pairing property: each has dot product $1$ with itself and $0$ with the other two. The example confirms that the construction is consistent and that it reduces to the identity on an orthonormal set.

**Verification of the pairing property.** As a check, the dot products between the original set and the reciprocal set are



$$
\hat{i}\cdot\hat{i}'=1,\quad \hat{j}\cdot\hat{j}'=1,\quad \hat{k}\cdot\hat{k}'=1,
$$



and every mixed dot product such as $\hat{i}\cdot\hat{j}'$ or $\hat{j}\cdot\hat{k}'$ equals $0$. The defining pattern holds exactly.

**A non-trivial variant.** To see the method do real work, take the set $\vec{a}=\hat{i}$, $\vec{b}=\hat{j}$, $\vec{c}=\hat{i}+\hat{k}$. The scalar triple product is



$$
\vec{a}\cdot(\vec{b}\times\vec{c})=\hat{i}\cdot\big(\hat{j}\times(\hat{i}+\hat{k})\big)=\hat{i}\cdot(\hat{j}\times\hat{i}+\hat{j}\times\hat{k})=\hat{i}\cdot(-\hat{k}+\hat{i})=1.
$$



The three cross products are



$$
\vec{b}\times\vec{c}=\hat{j}\times(\hat{i}+\hat{k})=-\hat{k}+\hat{i},
$$





$$
\vec{c}\times\vec{a}=(\hat{i}+\hat{k})\times\hat{i}=\hat{k}\times\hat{i}=\hat{j},
$$





$$
\vec{a}\times\vec{b}=\hat{i}\times\hat{j}=\hat{k}.
$$



Dividing each by the scalar triple product, which equals $1$, gives the reciprocal set



$$
\vec{a}'=\hat{i}-\hat{k},
\qquad
\vec{b}'=\hat{j},
\qquad
\vec{c}'=\hat{k}.
$$



Checking the pairing property: $\vec{a}\cdot\vec{a}'=\hat{i}\cdot(\hat{i}-\hat{k})=1$, $\vec{b}\cdot\vec{b}'=1$, $\vec{c}\cdot\vec{c}'=(\hat{i}+\hat{k})\cdot\hat{k}=1$, while $\vec{a}\cdot\vec{b}'=0$, $\vec{a}\cdot\vec{c}'=\hat{i}\cdot\hat{k}=0$, $\vec{b}\cdot\vec{a}'=0$, $\vec{b}\cdot\vec{c}'=0$, $\vec{c}\cdot\vec{a}'=(\hat{i}+\hat{k})\cdot(\hat{i}-\hat{k})=1-1=0$, and $\vec{c}\cdot\vec{b}'=0$. All nine dot products match the required pattern, so the reciprocal set is correct.

## 5. High-Yield Exam Takeaways & Common Pitfalls

**High-yield takeaways.**

- The reciprocal of a single vector preserves direction and inverts magnitude; it is $\vec{a}/\lVert \vec{a} \rVert^{2}$, equivalently $\hat{a}/\lVert \vec{a} \rVert$.
- The reciprocal set of $\{\vec{a},\vec{b},\vec{c}\}$ is built from the three cross products $\vec{b}\times\vec{c}$, $\vec{c}\times\vec{a}$, $\vec{a}\times\vec{b}$, each divided by the common scalar triple product $\vec{a}\cdot(\vec{b}\times\vec{c})$.
- The cyclic order matters: $\vec{a}'$ pairs with $\vec{a}$ and is built from the cross product of the *other two* vectors, $\vec{b}\times\vec{c}$.
- The defining test of a correct answer is the pairing property: $\vec{a}\cdot\vec{a}'=\vec{b}\cdot\vec{b}'=\vec{c}\cdot\vec{c}'=1$ and all six mixed dot products vanish. Always verify with this test.
- The construction requires a non-zero scalar triple product; if the three vectors are coplanar, the reciprocal set does not exist.
- The reciprocal set of an orthonormal set is itself, and applying the construction twice returns the original set.
- The pairing property gives the expansion $\vec{r}=(\vec{r}\cdot\vec{a}')\vec{a}+(\vec{r}\cdot\vec{b}')\vec{b}+(\vec{r}\cdot\vec{c}')\vec{c}$, which is the main use of reciprocal sets.

**Common pitfalls.**

- Using the wrong cross product for a given reciprocal vector, for example dividing $\vec{a}\times\vec{b}$ to obtain $\vec{a}'$ instead of $\vec{c}'$. The pairing must be checked against the dot-product test.
- Forgetting to divide by the scalar triple product, which leaves the magnitudes wrong even when the directions are correct.
- Computing the scalar triple product with the wrong sign or with a non-cyclic ordering; the value must be the same non-zero number used in all three divisions.
- Confusing the reciprocal of a vector with its unit vector. The unit vector has magnitude $1$; the reciprocal has magnitude $1/\lVert \vec{a} \rVert$ and is generally not a unit vector.
- Assuming the reciprocal vectors are mutually perpendicular to each other. They are perpendicular to members of the *original* set, not necessarily to one another.
- Attempting the construction on a coplanar set, where the scalar triple product is zero and the formulas are undefined.
- Omitting the verification step. A quick check of the nine dot products catches almost every arithmetic slip in the cross products or the normalising factor.