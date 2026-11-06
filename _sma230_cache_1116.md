## 1. Core Concept Overview & Intuition

Think about a pair of shoes. Each shoe is useful on its own, but the pair is what you actually wear. In vector work, a set of three vectors can be paired with a second set of three vectors in a special way: each vector in the second set is built to "match" one vector in the first set, and the matching is measured by the dot product. The second set is called the **reciprocal set**.

The word *reciprocal* is used in ordinary life when two numbers multiply to give one, such as $2$ and $\tfrac{1}{2}$. The idea here is similar but a little richer. Instead of two numbers multiplying to one, we have two vectors whose dot product is one, and every other pairing gives zero.

A simple everyday picture helps. Imagine a room with three walls meeting at a corner. Each wall can be described by a vector lying along an edge. Now imagine a second set of three arrows, each one pointing straight out of one wall, perpendicular to the other two walls. That second set is the reciprocal set. Each new arrow is "blind" to two of the original arrows (dot product zero) and "aligned" with the third (dot product one).

The analogy stops being exact in one place: in the room, the walls are flat surfaces, while in vector algebra the vectors are just arrows with length and direction. The dot product is the only measuring tool we use, so the whole idea is really about dot products, not about physical walls.

The source material describes the idea in words: a reciprocal vector is formed by choosing a vector perpendicular to two of the given vectors and having a length that is reciprocal to the third. That single sentence is the heart of the lesson. Everything else is bookkeeping: how to compute such vectors reliably.

The lesson outcomes are short and clear. By the end of the lesson the learner should be able to evaluate the reciprocal set of vectors. The discussion task asks learners to study reciprocal sets and to discuss how to evaluate dot products between a vector and its reciprocal. That discussion is the natural check: if the dot products come out as one and zero in the right pattern, the reciprocal set is correct.

## 2. Mathematical Formalization & Core Definitions

### 2.1 The three given vectors

We start with three vectors in space, written $\vec{a}$, $\vec{b}$ and $\vec{c}$. Each is an arrow with a length and a direction. The only operation we need from earlier work is the **dot product**, written $\vec{a}\cdot\vec{b}$. The dot product of two vectors is a single number (a scalar), not a vector. It measures how much the two arrows point along each other.

Two facts about the dot product are used constantly:

- If two nonzero vectors are perpendicular, their dot product is zero.
- If a vector is dotted with itself, the result is the square of its length, so $\vec{a}\cdot\vec{a}=\lVert\vec{a}\rVert^{2}$.

Here $\lVert\vec{a}\rVert$ means the length (magnitude) of $\vec{a}$.

### 2.2 The definition of a reciprocal set

> **Definition (Reciprocal set of vectors).** Let $\vec{a}$, $\vec{b}$ and $\vec{c}$ be three given vectors. A set of three vectors $\vec{a}'$, $\vec{b}'$ and $\vec{c}'$ is called a reciprocal set to $\{\vec{a},\vec{b},\vec{c}\}$ if the dot products satisfy the pattern



$$
\vec{a}\cdot\vec{a}'=1,\qquad \vec{b}\cdot\vec{b}'=1,\qquad \vec{c}\cdot\vec{c}'=1,
$$



> and every "cross" dot product is zero:



$$
\vec{a}\cdot\vec{b}'=0,\qquad \vec{a}\cdot\vec{c}'=0,\qquad \vec{b}\cdot\vec{a}'=0,\qquad \vec{b}\cdot\vec{c}'=0,\qquad \vec{c}\cdot\vec{a}'=0,\qquad \vec{c}\cdot\vec{b}'=0.
$$



In plain words: each reciprocal vector is perpendicular to the two given vectors it is *not* paired with, and it is scaled so that its dot product with its own partner equals one.

The source states the single-vector version of this idea: the vector which has the same direction as a given vector but has magnitude reciprocal to that of the given vector is called the reciprocal of that vector. So for a single vector $\vec{a}$, the reciprocal in that narrow sense is a vector pointing the same way with length $1/\lVert\vec{a}\rVert$. The full reciprocal *set* generalises this to three vectors at once, using perpendicularity as the extra ingredient.

### 2.3 The perpendicularity condition in words

To build $\vec{a}'$, we need an arrow that is perpendicular to both $\vec{b}$ and $\vec{c}$. From earlier vector algebra, an arrow perpendicular to two given arrows is obtained from the cross product $\vec{b}\times\vec{c}$. So $\vec{a}'$ must point along $\vec{b}\times\vec{c}$, possibly scaled by some number. The scaling number is fixed by the requirement $\vec{a}\cdot\vec{a}'=1$.

The same reasoning gives $\vec{b}'$ pointing along $\vec{c}\times\vec{a}$ and $\vec{c}'$ pointing along $\vec{a}\times\vec{b}$.

### 2.4 The scaling constant

Write $\vec{a}'=k\,(\vec{b}\times\vec{c})$ for some number $k$. Then



$$
\begin{aligned}
\vec{a}\cdot\vec{a}' &= k\,\vec{a}\cdot(\vec{b}\times\vec{c}).
\end{aligned}
$$



The quantity $\vec{a}\cdot(\vec{b}\times\vec{c})$ is the **scalar triple product** of $\vec{a}$, $\vec{b}$ and $\vec{c}$. It is a single number, and it equals the volume of the parallelepiped (a slanted box) whose edges are the three vectors. Setting the dot product equal to one gives



$$
\begin{aligned}
k\,\vec{a}\cdot(\vec{b}\times\vec{c}) &= 1,
\end{aligned}
$$



so



$$
\begin{aligned}
k &= \frac{1}{\vec{a}\cdot(\vec{b}\times\vec{c})}.
\end{aligned}
$$



Therefore



$$
\begin{aligned}
\vec{a}' &= \frac{\vec{b}\times\vec{c}}{\vec{a}\cdot(\vec{b}\times\vec{c})}.
\end{aligned}
$$



By the same reasoning, cycling the letters,



$$
\begin{aligned}
\vec{b}' &= \frac{\vec{c}\times\vec{a}}{\vec{a}\cdot(\vec{b}\times\vec{c})},
\end{aligned}
$$





$$
\begin{aligned}
\vec{c}' &= \frac{\vec{a}\times\vec{b}}{\vec{a}\cdot(\vec{b}\times\vec{c})}.
\end{aligned}
$$



All three share the same denominator, the scalar triple product. This is the standard evaluation method for a reciprocal set.

### 2.5 Why the denominator must not be zero

If $\vec{a}\cdot(\vec{b}\times\vec{c})=0$, the three given vectors lie in one plane (or one of them is zero). The slanted box has zero volume. Then no reciprocal set exists, because we would be dividing by zero. In that case the three vectors are called **coplanar**, and the reciprocal set is undefined. This is the first thing to check in any problem.

### 2.6 The pattern of dot products, stated as a table

The defining dot products can be arranged in a small table. Rows are the given vectors, columns are the reciprocal vectors.

| | $\vec{a}'$ | $\vec{b}'$ | $\vec{c}'$ |
|---|---|---|---|
| $\vec{a}$ | $1$ | $0$ | $0$ |
| $\vec{b}$ | $0$ | $1$ | $0$ |
| $\vec{c}$ | $0$ | $0$ | $1$ |

The table is the quickest way to remember the definition: ones on the diagonal, zeros everywhere else. It is also the quickest way to check an answer.

### 2.7 The special case of the standard unit vectors

The assessment task in the source asks for a set of vectors reciprocal to the set of the three standard unit vectors. These are the arrows of length one pointing along the three coordinate directions. Call them $\hat{i}$, $\hat{j}$ and $\hat{k}$. Their dot products are simple: each has dot product one with itself and zero with the other two.

Applying the formula with $\vec{a}=\hat{i}$, $\vec{b}=\hat{j}$ and $\vec{c}=\hat{k}$:



$$
\begin{aligned}
\vec{a}' &= \frac{\hat{j}\times\hat{k}}{\hat{i}\cdot(\hat{j}\times\hat{k})}.
\end{aligned}
$$



Now $\hat{j}\times\hat{k}=\hat{i}$, and $\hat{i}\cdot\hat{i}=1$. Hence



$$
\begin{aligned}
\vec{a}' &= \hat{i}.
\end{aligned}
$$



In the same way $\vec{b}'=\hat{j}$ and $\vec{c}'=\hat{k}$. So the reciprocal set of the standard unit vectors is the standard unit vectors themselves. This makes sense: each unit vector is already perpendicular to the other two and already has dot product one with itself. The set is its own reciprocal.

## 3. Key Theorems & Essential Results

> **Result 1 (Existence).** A reciprocal set to $\{\vec{a},\vec{b},\vec{c}\}$ exists exactly when the scalar triple product $\vec{a}\cdot(\vec{b}\times\vec{c})$ is not zero. When it is nonzero, the reciprocal set is unique.

The reason is that the three formulas in Section 2.4 give explicit vectors, and the denominator is the only place where a problem can arise. Uniqueness follows because the perpendicularity conditions force each reciprocal vector to point along a fixed cross product, and the scaling condition then fixes its length.

> **Result 2 (The reciprocal formulas).** For three vectors with nonzero scalar triple product,



$$
\vec{a}'=\frac{\vec{b}\times\vec{c}}{\vec{a}\cdot(\vec{b}\times\vec{c})},\qquad \vec{b}'=\frac{\vec{c}\times\vec{a}}{\vec{a}\cdot(\vec{b}\times\vec{c})},\qquad \vec{c}'=\frac{\vec{a}\times\vec{b}}{\vec{a}\cdot(\vec{b}\times\vec{c})}.
$$



Notice the cyclic order: the numerator for $\vec{a}'$ uses the two vectors *other than* $\vec{a}$, taken in the order $\vec{b}$ then $\vec{c}$. The numerator for $\vec{b}'$ uses $\vec{c}$ then $\vec{a}$. The numerator for $\vec{c}'$ uses $\vec{a}$ then $\vec{b}$. Keeping this cycle straight prevents sign errors.

> **Result 3 (The dot-product check).** The reciprocal set satisfies



$$
\vec{a}\cdot\vec{a}'=\vec{b}\cdot\vec{b}'=\vec{c}\cdot\vec{c}'=1,
$$



> and all six cross dot products are zero.

This is the definition restated as a check. In an exam, after computing the three reciprocal vectors, always perform at least one diagonal check and one cross check. If either fails, the arithmetic is wrong.

> **Result 4 (Reciprocity is symmetric).** If $\{\vec{a}',\vec{b}',\vec{c}'\}$ is reciprocal to $\{\vec{a},\vec{b},\vec{c}\}$, then $\{\vec{a},\vec{b},\vec{c}\}$ is reciprocal to $\{\vec{a}',\vec{b}',\vec{c}'\}$.

The word *reciprocal* is well chosen: the relationship runs both ways. The dot-product table is unchanged if we swap the roles of the two sets, because the dot product itself does not care about order, $\vec{a}\cdot\vec{a}'=\vec{a}'\cdot\vec{a}$.

> **Result 5 (Same direction, reciprocal length, single vector).** For a single nonzero vector $\vec{a}$, the vector with the same direction as $\vec{a}$ and magnitude $1/\lVert\vec{a}\rVert$ is the reciprocal of $\vec{a}$ in the narrow sense. It equals $\vec{a}/\lVert\vec{a}\rVert^{2}$, since



$$
\vec{a}\cdot\frac{\vec{a}}{\lVert\vec{a}\rVert^{2}}=\frac{\vec{a}\cdot\vec{a}}{\lVert\vec{a}\rVert^{2}}=1.
$$



This is the source's own definition, written in symbols. It is the one-vector case of the general pattern, and it is worth remembering separately because it appears in the discussion task about dot products between a vector and its reciprocal.

## 4. Worked Exemplar Problem with Step-by-Step Solution

### 4.1 The assessment problem

The source assessment asks: find a set of vectors reciprocal to the set of the three standard unit vectors. We solve it slowly, then add a second, harder example so that the method is fully practised.

### 4.2 Solution to the assessment problem

**Step 1. Name the vectors.** Let



$$
\begin{aligned}
\vec{a} &= \hat{i}, \\
\vec{b} &= \hat{j}, \\
\vec{c} &= \hat{k}.
\end{aligned}
$$



Here $\hat{i}$, $\hat{j}$ and $\hat{k}$ are the unit vectors along the three coordinate directions. Each has length one, and each is perpendicular to the other two.

**Step 2. Check the denominator.** Compute the scalar triple product:



$$
\begin{aligned}
\vec{a}\cdot(\vec{b}\times\vec{c}) &= \hat{i}\cdot(\hat{j}\times\hat{k}).
\end{aligned}
$$



Since $\hat{j}\times\hat{k}=\hat{i}$ and $\hat{i}\cdot\hat{i}=1$, the denominator equals $1$. It is not zero, so a reciprocal set exists.

**Step 3. Compute the first reciprocal vector.**



$$
\begin{aligned}
\vec{a}' &= \frac{\vec{b}\times\vec{c}}{\vec{a}\cdot(\vec{b}\times\vec{c})} \\
&= \frac{\hat{j}\times\hat{k}}{1} \\
&= \hat{i}.
\end{aligned}
$$



**Step 4. Compute the second reciprocal vector.**



$$
\begin{aligned}
\vec{b}' &= \frac{\vec{c}\times\vec{a}}{\vec{a}\cdot(\vec{b}\times\vec{c})} \\
&= \frac{\hat{k}\times\hat{i}}{1} \\
&= \hat{j}.
\end{aligned}
$$



**Step 5. Compute the third reciprocal vector.**



$$
\begin{aligned}
\vec{c}' &= \frac{\vec{a}\times\vec{b}}{\vec{a}\cdot(\vec{b}\times\vec{c})} \\
&= \frac{\hat{i}\times\hat{j}}{1} \\
&= \hat{k}.
\end{aligned}
$$



**Step 6. Check with dot products.** The diagonal entries are $\hat{i}\cdot\hat{i}=1$, $\hat{j}\cdot\hat{j}=1$ and $\hat{k}\cdot\hat{k}=1$. The cross entries are all zero because the standard unit vectors are mutually perpendicular. The pattern is correct.

**Step 7. State the answer.** The reciprocal set is $\{\hat{i},\hat{j},\hat{k}\}$ itself. The set is its own reciprocal.

### 4.3 A second worked example with numbers

**Problem.** Find a set of vectors reciprocal to



$$
\begin{aligned}
\vec{a} &= \hat{i}, \\
\vec{b} &= \hat{j}, \\
\vec{c} &= \hat{i}+\hat{j}+\hat{k}.
\end{aligned}
$$



**Step 1. Check the denominator.** First compute $\vec{b}\times\vec{c}$:



$$
\begin{aligned}
\vec{b}\times\vec{c} &= \hat{j}\times(\hat{i}+\hat{j}+\hat{k}) \\
&= \hat{j}\times\hat{i}+\hat{j}\times\hat{j}+\hat{j}\times\hat{k} \\
&= -\hat{k}+0+\hat{i} \\
&= \hat{i}-\hat{k}.
\end{aligned}
$$



Then



$$
\begin{aligned}
\vec{a}\cdot(\vec{b}\times\vec{c}) &= \hat{i}\cdot(\hat{i}-\hat{k}) \\
&= 1-0 \\
&= 1.
\end{aligned}
$$



The denominator is $1$, so the reciprocal set exists.

**Step 2. First reciprocal vector.**



$$
\begin{aligned}
\vec{a}' &= \frac{\vec{b}\times\vec{c}}{1} \\
&= \hat{i}-\hat{k}.
\end{aligned}
$$



**Step 3. Second reciprocal vector.** Compute $\vec{c}\times\vec{a}$:



$$
\begin{aligned}
\vec{c}\times\vec{a} &= (\hat{i}+\hat{j}+\hat{k})\times\hat{i} \\
&= \hat{i}\times\hat{i}+\hat{j}\times\hat{i}+\hat{k}\times\hat{i} \\
&= 0-\hat{k}+\hat{j} \\
&= \hat{j}-\hat{k}.
\end{aligned}
$$



Hence



$$
\begin{aligned}
\vec{b}' &= \frac{\vec{c}\times\vec{a}}{1} \\
&= \hat{j}-\hat{k}.
\end{aligned}
$$



**Step 4. Third reciprocal vector.** Compute $\vec{a}\times\vec{b}$:



$$
\begin{aligned}
\vec{a}\times\vec{b} &= \hat{i}\times\hat{j} \\
&= \hat{k}.
\end{aligned}
$$



Hence



$$
\begin{aligned}
\vec{c}' &= \frac{\vec{a}\times\vec{b}}{1} \\
&= \hat{k}.
\end{aligned}
$$



**Step 5. Check the diagonal dot products.**



$$
\begin{aligned}
\vec{a}\cdot\vec{a}' &= \hat{i}\cdot(\hat{i}-\hat{k}) \\
&= 1.
\end{aligned}
$$





$$
\begin{aligned}
\vec{b}\cdot\vec{b}' &= \hat{j}\cdot(\hat{j}-\hat{k}) \\
&= 1.
\end{aligned}
$$





$$
\begin{aligned}
\vec{c}\cdot\vec{c}' &= (\hat{i}+\hat{j}+\hat{k})\cdot\hat{k} \\
&= 1.
\end{aligned}
$$



**Step 6. Check one cross dot product.**



$$
\begin{aligned}
\vec{a}\cdot\vec{b}' &= \hat{i}\cdot(\hat{j}-\hat{k}) \\
&= 0.
\end{aligned}
$$



The remaining cross dot products vanish by the same kind of calculation. The reciprocal set is



$$
\begin{aligned}
\vec{a}' &= \hat{i}-\hat{k}, \\
\vec{b}' &= \hat{j}-\hat{k}, \\
\vec{c}' &= \hat{k}.
\end{aligned}
$$



## 5. High-Yield Exam Takeaways & Common Pitfalls

### 5.1 High-yield takeaways

- The reciprocal set is defined by dot products: ones on the diagonal, zeros off the diagonal. Memorise the pattern, not just the formulas.
- The master formula uses the scalar triple product as a common denominator. Write the denominator once and reuse it for all three vectors.
- The numerator for $\vec{a}'$ is $\vec{b}\times\vec{c}$; for $\vec{b}'$ it is $\vec{c}\times\vec{a}$; for $\vec{c}'$ it is $\vec{a}\times\vec{b}$. Follow the cycle $\vec{a}\to\vec{b}\to\vec{c}\to\vec{a}$.
- Always check the denominator first. If $\vec{a}\cdot(\vec{b}\times\vec{c})=0$, the vectors are coplanar and no reciprocal set exists. Say so clearly instead of dividing by zero.
- The reciprocal relationship is symmetric: each set is reciprocal to the other.
- For a single vector, the reciprocal in the narrow sense is $\vec{a}/\lVert\vec{a}\rVert^{2}$, which points the same way and has length $1/\lVert\vec{a}\rVert$.
- The standard unit vectors are their own reciprocal set. This is the quickest sanity check of the whole method.
- After computing, verify at least one diagonal dot product equals one and one cross dot product equals zero. This catches most arithmetic slips.

### 5.2 Common pitfalls

- **Forgetting the denominator.** Writing $\vec{a}'=\vec{b}\times\vec{c}$ without dividing gives the right direction but the wrong length, and the diagonal dot product will not equal one.
- **Wrong cyclic order in the numerator.** Using $\vec{c}\times\vec{b}$ instead of $\vec{b}\times\vec{c}$ flips the sign and breaks the dot-product pattern.
- **Dividing by zero without noticing.** If the three vectors lie in one plane, the triple product is zero. The correct response is to state that no reciprocal set exists, not to force a division.
- **Confusing the reciprocal set with the cross-product set.** The three cross products $\vec{b}\times\vec{c}$, $\vec{c}\times\vec{a}$ and $\vec{a}\times\vec{b}$ are only the *directions* of the reciprocal vectors. The scaling by the triple product is what makes them reciprocal.
- **Mixing up the narrow single-vector reciprocal with the full set.** The single-vector reciprocal keeps the same direction; the set version uses perpendicular directions. Keep the two ideas separate.
- **Skipping the check.** A quick dot-product check takes seconds and confirms the answer. Omitting it is the most common cause of lost marks.

### 5.3 Source references for further reading

The approved reading list for this topic is:

- Davis, H. F. and Snider, A. D., *Introduction to Vector Analysis*, 7th ed., Boston: Allyn & Bacon (1995).
- Lewis, P. E. and Ward, J. P., *Vector Analysis for Engineers and Scientists*, Reading, MA: Addison-Wesley (1989).
- http://www.bhojvirtualuniversity.com/slm/bsc1_maths3.pdf

These approved sources treat reciprocal sets alongside the scalar triple product, so reading the triple-product material first makes the reciprocal formulas feel natural.