[[1]]
### 1.7 Examination interpretation of the basic tasks

Most examination questions in this lesson can be classified by the requested object before any arithmetic begins. “Find the resultant” calls for vector addition. “Find its magnitude” calls for a norm after the resultant has been calculated. “Find a unit vector in its direction” calls for normalization of that same resultant. “Find the displacement from $P$ to $Q$” calls for terminal position minus initial position. “Find the distance” calls for the magnitude of that displacement. Treating these as separate verbs prevents a correct intermediate answer from being mistaken for the final one.

Write vectors in a consistent component order throughout a solution. If a vector is represented in the order $x,y,z$, retain that order in every sum, subtraction, magnitude, and check. A well-presented answer makes the sign and order of each component visible; a compressed single line hides the exact place where a minus sign may have been lost.

[[2]]
### 2.10 A reliable calculation sequence

For a multi-part problem, define each given vector in components first. Add or subtract the vectors before computing the magnitude. If the requested unit direction is based on a resultant, use the resultant's magnitude—not the magnitude of one of its addends—as the divisor. If the question gives points, form the directed displacement with a labelled endpoint subtraction before writing its length.

Keep exact values through the work. For a magnitude such as $\sqrt{44}$, either $\sqrt{44}$ or the simplified form $2\sqrt{11}$ is exact; a decimal is only an approximation. If direction cosines are requested, calculate each as a signed component divided by the positive magnitude. Do not report only an unsigned angle or a magnitude where the problem requests the complete vector.

### 2.11 Independent checks that earn clarity

A unit-vector answer can be checked by squaring and adding its components. A point-to-point distance can be checked by reversing the endpoints and confirming the same magnitude. A resultant can be checked by re-adding one coordinate column at a time. Direction cosines can be checked using their squared identity. These checks should be short and relevant; they are not substitutes for showing the main method.

### 2.12 Exact and approximate forms

Magnitude answers should normally remain exact unless the question requests a decimal. For example, $\sqrt{29}$ is an exact magnitude; a rounded decimal is an approximation that may slightly alter normalized components. If a unit vector is requested, divide by the exact norm first and round the resulting components only at the end. Include sufficient precision so their squared sum remains recognizably one.

When a magnitude is given and direction cosines are supplied, reconstruct components by multiplication, not division: each component is magnitude times its cosine. Conversely, when components are given, divide each by the positive magnitude to find the cosines. Writing one of these two directions explicitly avoids switching a ratio unintentionally.

### 2.13 How to show a resultant efficiently

For three or more addends, write one aligned component sum per coordinate. For example, a resultant's $x$ component should visibly show every signed $x$ contribution. This layout reduces sign loss and makes it straightforward to award method credit. A small table may be used, but the final vector should be stated outside the table so the answer is unmistakable.

If a question contains a point displacement followed by another displacement, preserve the order of the chain. For $P\to Q$ and then $Q\to R$, the sum is $\overrightarrow{PQ}+\overrightarrow{QR}=\overrightarrow{PR}$. The middle point cancels in component form. If the arrows are listed in the reverse order, do not assume they represent the same route; each displacement has a direction and a specified start and end.

[[3]]
### 3.11 Diagnostic checks for sign and scale

Suppose a calculated direction cosine has magnitude greater than one. Since it is a component of a unit vector, this is impossible; the likely error is an incorrect norm or a numerator taken from the wrong component. If the squared sum of the three cosines is not one, recompute the magnitude and retain the component signs. If a supposed unit vector is zero, a nonzero vector may have been divided incorrectly or cancellation may have occurred before the direction was defined.

For a point displacement, adding the result to the initial position must recover the terminal position. This check is especially effective when negative coordinates appear. For a resultant, subtract one addend from the result and verify that the remaining sum equals the other addends. These inverse operations test the original arithmetic rather than merely repeating it.

[[4]]
### 4.18 Worked example: build an exam answer in stages

Given $A=(4,-1,2)$, $B=(-2,3,1)$, and $C=(1,2,-5)$, find the resultant and direction cosines. Show each coordinate total:

$$R=(4-2+1,\ -1+3+2,\ 2+1-5)=(3,4,-2).$$

Then $|R|=\sqrt{9+16+4}=\sqrt{29}$. The direction cosines are $3/\sqrt{29},4/\sqrt{29},-2/\sqrt{29}$. Their squared sum is one. Preserve the negative third component; the vector has a negative projection on the third positive axis.

If the question also asks for a unit vector, it is the same signed triple because unit-vector components are direction cosines. If the question asks for angles, apply inverse cosine to each signed value and report the correct angle range. Do not write the magnitude as a direction cosine or confuse the three requested results.

### 4.19 Worked example: locate the error in a proposed solution

Suppose a student adds $(2,-3,1)$ and $(-5,1,4)$ but reports the resultant $(7,-2,5)$. The second and third components are correct, but the first component should be $2+(-5)=-3$, not seven. A sign error has changed a westward net component into an eastward one. The corrected resultant is $(-3,-2,5)$ and its magnitude is $\sqrt{9+4+25}=\sqrt{38}$.

The direction check is immediate: the first vector contributes two units in the positive first direction, while the second contributes five in the negative direction, so the net must be negative. This illustrates how geometric interpretation can catch a purely arithmetic error before a later normalization spreads it.

### 4.20 Worked example: interpreting an unknown magnitude constraint

If $v=(x,2,-1)$ has magnitude $\sqrt{14}$, then $x=\pm3$. A complete response gives both roots and explicitly notes that length alone cannot choose between them. If a separate condition says $v$ lies in the positive first-coordinate half-space, retain $x=3$. The criterion is the sign of the first component, not the magnitude equation.

The same logic applies to unknown direction cosines. The squared identity determines a square; geometric orientation or an explicit sign condition determines the sign. A clean solution separates these two logical stages.

### 4.21 A point-displacement check with negative coordinates

For $P=(2,-1,3)$ and $Q=(-2,5,0)$, $\overrightarrow{PQ}=(-4,6,-3)$. Adding this vector to $P$ recovers $Q$. Its magnitude is $\sqrt{61}$; reversing the arrow gives $(4,-6,3)$ and preserves that magnitude. Showing both the reconstruction check and the reverse-distance check may be useful when the question tests both displacement and distance.

[[5]]
### 5.9 Efficient time allocation by mathematical dependency

The dependencies in a multi-part vector-algebra question are fixed: obtain correct components before a norm, and obtain a nonzero norm before normalization. Spend effort on the early signed arithmetic because every later answer depends on it. Use exact radicals and fractions until the last step. A brief final check—unit length, endpoint recovery, or direction-cosine identity—provides more value than repeating the entire calculation.

### 5.10 Final response format for common prompts

For “find the resultant,” write a labelled vector with its components. For “find the magnitude,” show the square root of the component squares and give a nonnegative scalar. For “find the unit vector,” show the divisor and preserve each sign. For “find direction cosines,” give the signed ratios and optionally show their squared sum. For “find the vector from $P$ to $Q$,” explicitly use $Q-P$. For “find the distance,” take the magnitude and do not leave the answer as a directed vector.

This response format is concise but distinguishes every requested quantity. In a multi-part question, label the outputs so that a correct magnitude is not accidentally presented as the whole answer. If the task requests a decimal, retain the exact form during the calculation and round once at the end.

### 5.11 A completed three-part answer

For the resultant $R=(3,6,-2)$, report: (i) resultant vector $R=3\hat i+6\hat j-2\hat k$; (ii) magnitude $|R|=7$; (iii) unit vector in its direction $\widehat R=(3/7)\hat i+(6/7)\hat j-(2/7)\hat k$. The three outputs are internally consistent because multiplying the unit vector by seven recovers the resultant and the unit vector has squared magnitude one. This is the level of verification appropriate when all three parts are asked, while a shorter question needs only the requested portion.
[[3]]
### 3.9 Conditions for uniqueness

A vector's magnitude fixes a sphere of possible directions, so magnitude alone never determines a unique nonzero vector in three dimensions. A vector's direction cosines together with a positive magnitude determine its components uniquely. A magnitude equation involving an unknown component generally yields two roots; a direction statement may select one but should not be inferred from a sketch unless the problem states the orientation.

The zero vector is a special case: it has a well-defined component representation and magnitude zero, but no direction cosines or unit vector. Any proof or solution that divides by a vector's magnitude must state or use that the vector is nonzero. This is a mathematical condition, not a stylistic detail.

### 3.10 A second route to the norm check

For a proposed unit vector $u=(u_1,u_2,u_3)$, the definition is $|u|=1$. Squaring both sides gives the equivalent test $u_1^2+u_2^2+u_3^2=1$, since magnitude is nonnegative. This avoids evaluating a square root during verification. For a direction cosine triple, the same sum-of-squares test applies because those cosines are precisely the components of a unit vector.

[[4]]
### 4.14 Examination problem: reconstruct and verify a unit direction

The vectors $r_1=2\hat i+4\hat j-5\hat k$ and $r_2=\hat i+2\hat j+3\hat k$ have resultant $R=3\hat i+6\hat j-2\hat k$. Calculate $|R|=7$, then divide every component by seven to obtain $\widehat R=(3/7,6/7,-2/7)$.

**Expected reasoning:** component addition must be shown before normalization. The norm calculation must include the negative third component squared, $(-2)^2=4$. The normalized vector should retain the negative third sign. A direct check is $9/49+36/49+4/49=1$. Reporting $(3,6,-2)$ alone answers only the resultant part; reporting seven alone answers only the magnitude part.

### 4.15 Examination problem: a vector with a constrained length

Let $v=(x,2,-1)$ and suppose $|v|=\sqrt{14}$. The norm equation is $x^2+2^2+(-1)^2=14$, hence $x^2=9$ and $x=\pm3$. State both solutions unless an orientation condition is supplied. If $v$ is said to point toward positive $x$, take the positive root. Check each candidate by substitution into the original squared norm.

**Marking structure:** establish the norm equation, simplify without dropping the square on the unknown, solve both roots, apply any direction information, and verify. Taking only the positive square root without explaining a given sign condition is an unsupported choice.

### 4.16 Examination problem: detect impossible direction cosines

Test $(2/3,1/3,2/3)$. The squared sum is one, so the triple is consistent with a direction. Test $(2/3,1/3,1)$. Its squared sum is $14/9$, so it cannot be a direction-cosine triple. This decision requires no inverse trigonometric calculation.

### 4.17 Examination problem: endpoint subtraction and reverse check

Let $P=(2,-1,3)$ and $Q=(-2,5,0)$. Then $\overrightarrow{PQ}=(-4,6,-3)$. Its magnitude is $\sqrt{16+36+9}=\sqrt{61}$. To check the vector, add it to $P$: $(2,-1,3)+(-4,6,-3)=(-2,5,0)=Q$. The reverse directed vector is $(4,-6,3)$, with the same magnitude.

This addition check is often faster and more informative than recomputing the subtraction. It confirms endpoint order as well as arithmetic and makes explicit that the displacement carries direction while the distance does not.

[[5]]
### 5.7 Common partial-credit losses

An answer can be numerically close and still be incomplete if it omits the requested vector or direction. Include the vector in component form, the scalar norm, or the unit vector as separate labelled outputs. For direction cosines, state the signed triple; inverse-cosine angles are a different representation. If a decimal is used, mark it as approximate.

A second avoidable loss comes from writing a formula but never substituting the data. A clear solution displays the component totals or endpoint differences, then the norm evaluation. This makes method marks available even if one arithmetic value is wrong. Keep enough intermediate work to reveal the method, but do not repeat the same formula after every arithmetic line.

### 5.8 Topic boundary and timed solution plan

This lesson ends with componentwise vector operations, resultants, magnitudes, unit vectors, and direction cosines. If the examiner asks whether two vectors are perpendicular, use the dot product from the next topic; if asked for a normal to a plane or an area, use the cross product. Recognizing the boundary selects the right method and avoids an irrelevant calculation.

Under time pressure, classify the requested quantity first, write the vector components, perform the necessary operation, and finish with one verification. For a resultant-plus-unit-direction question, the order cannot be safely reversed: addition precedes magnitude, and magnitude precedes normalization. A compact but labelled sequence is both faster to check and easier to award marks.
[[3]]
### 3.7 Derivation of the coordinate laws

For $A=(a_1,a_2,a_3)$ and $B=(b_1,b_2,b_3)$, define addition by the parallelogram or head-to-tail resultant. The projection of the resultant onto each coordinate axis is the sum of the projections of its two addends, which gives $(a_1+b_1,a_2+b_2,a_3+b_3)$. This coordinate rule explains why vectors with the same components are equal and why addition can be computed without drawing the geometry at every step.

Associativity follows by applying associativity of real addition to each coordinate. It justifies grouping a long resultant as convenient, but does not permit changing a vector's direction or order of subtraction. The additive identity is $(0,0,0)$, and the inverse of $A$ is $-A$. These facts explain cancellation in closed vector chains and supply the algebraic foundation for solving vector equations.

For two-point displacement, the chain relation is $r_P+\overrightarrow{PQ}=r_Q$. Subtracting $r_P$ yields the endpoint formula. Taking its magnitude yields distance because the Euclidean norm depends on squared component differences. This two-stage argument makes explicit why displacement is directed while distance is not.

### 3.8 Proof checks for normalization and direction

If $A\ne0$ and $u=A/\lVert A\rVert$, then by homogeneity of the norm, $\lVert u\rVert=\lVert A\rVert/\lVert A\rVert=1$. The divisor is positive, so $u$ points in the same direction as $A$. If the divisor were negative, the orientation would reverse; if $A=0$, the operation would be undefined. State the nonzero condition whenever the definition is used in a proof.

With direction cosines $l=a_1/r$, $m=a_2/r$, $n=a_3/r$, where $r^2=a_1^2+a_2^2+a_3^2$, the identity follows by summing their squares. The signs remain attached to the components, although squaring removes them in the identity. Therefore the identity alone checks consistency but does not uniquely determine all component signs.

[[4]]
### 4.9 Examination problem: combined resultant and unit direction

Let $A=(4,-1,2)$, $B=(-2,3,1)$, and $C=(1,2,-5)$. Find the resultant $R$, its magnitude, and its direction cosines.

**Mark-worthy setup:** state that the resultant is the vector sum and group components by axis. The $x$ component is $4-2+1=3$, the $y$ component is $-1+3+2=4$, and the $z$ component is $2+1-5=-2$. Thus $R=(3,4,-2)$.

**Magnitude:** $|R|=\sqrt{3^2+4^2+(-2)^2}=\sqrt{29}$. Retaining the radical avoids avoidable approximation. **Direction cosines:** $(3/\sqrt{29},4/\sqrt{29},-2/\sqrt{29})$. Their squared sum is $(9+16+4)/29=1$. The negative third component is essential: it shows that the resultant has an obtuse angle with the positive $z$ axis.

**Presentation check:** distinguish the vector $R$ from the scalar $|R|$. A response that gives only $\sqrt{29}$ answers the magnitude part but not the resultant-vector part. A response that gives $R$ but no normalized components omits the direction-cosine request.

### 4.10 Examination problem: displacement, reverse displacement, and distance

Let $P=(1,-4,2)$ and $Q=(-3,2,8)$. Then $\overrightarrow{PQ}=(-4,6,6)$ and $\overrightarrow{QP}=(4,-6,-6)$. The first is terminal minus initial; the second reverses every sign. The distance is

$$PQ=\sqrt{(-4)^2+6^2+6^2}=\sqrt{88}=2\sqrt{22}.$$

To earn clear method marks, show the coordinate subtraction before taking the square root. A common incorrect method is to compute $Q-P$ in one coordinate and $P-Q$ in another. Label the direction once, then apply it uniformly.

### 4.11 Examination problem: unknown component from a length condition

Suppose $A=(x,2,-1)$ is required to have magnitude $\sqrt{14}$. Squaring both sides of $|A|=\sqrt{14}$ gives $x^2+4+1=14$, so $x^2=9$ and $x=3$ or $x=-3$. Both satisfy the length because magnitude loses sign information. If the question also states that the vector has a positive $x$ component, select $x=3$; otherwise retain both possibilities.

This example shows why taking a square root of an equation in a variable must include both signs unless a direction condition removes one. Substituting either candidate back into the magnitude equation verifies it. A correct solution states whether the information determines a unique vector or two possible vectors.

### 4.12 Examination problem: testing whether supplied direction data are possible

Suppose three claimed direction cosines are $2/3$, $1/3$, and $2/3$. Their squared sum is $4/9+1/9+4/9=1$, so the set is consistent with a direction. If instead the third value is $1$, the squared sum is greater than one; no vector has all three claims as direction cosines. This check should be performed before using the values to construct components.

### 4.13 Short marking rubric for vector algebra

For a resultant, allocate working to the signed component totals and identify the final vector. For a magnitude, show the sum of squares and the square root. For a unit vector, show both the magnitude used and the componentwise division, followed by a unit-length check when the calculation is substantial. For a displacement, write the endpoint labels and subtraction order; for distance, take its norm and state the scalar result. This order makes the reasoning auditable and helps locate partial credit when an arithmetic slip occurs.

[[5]]
### 5.5 Common exam errors and their repairs

**Adding magnitudes instead of components.** This computes a path-length bound, not the vector resultant. Repair it by making a three-column component table and summing signed entries.

**Normalizing an addend rather than the resultant.** If the question asks for a unit vector along the net effect, first calculate the net vector, then its magnitude, then divide. A unit vector along one input is a different answer.

**Reversing point order.** Write $\overrightarrow{PQ}=Q-P$ beside the calculation. If the question asks only for distance, the sign eventually disappears, but the directed vector still needs the correct orientation.

**Dropping a negative component in a magnitude.** Keep parentheses, then square: $(-3)^2=9$. Replacing $-3$ by $3$ in the vector itself may change the direction even though the magnitude calculation happens to be unaffected.

**Rounding too early.** Keep radicals and fractions exact through normalization. Round only to the precision requested, and check that the approximate unit-vector length is close to one.

### 5.6 Limits of the answer and efficient finish

An algebraic resultant does not by itself provide the path taken, and a magnitude does not provide orientation. State exactly which object each part requests. This unit's central output is a vector in components and its magnitude or normalized direction; questions about angle between two vectors, area, coplanarity, or a normal direction require the products treated in the next topic.

In a timed solution, the safest order is still the mathematical order: label components, compute the vector, calculate its norm, normalize if needed, and perform one check matched to the requested result. Skipping the vector stage to save space often causes sign errors and makes the final work difficult to mark.
