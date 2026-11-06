import os
import re
import runpy

r = runpy.run_path("_sma330_repair2.py")

def prose_word_count(text):
    text = re.sub(r"(?s)\$\$.*?\$\$", " ", text)
    text = re.sub(r"(?s)\\\[.*?\\\]", " ", text)
    text = re.sub(r"(?s)\\\(.*?\\\)", " ", text)
    text = re.sub(r"(?s)\$[^$]*\$", " ", text)
    text = re.sub(r"(?m)^#{1,6}\s.*$", " ", text)
    text = re.sub(r"(?m)^\s*\|.*$", " ", text)
    return len(re.findall(r"\b[\w’'-]+\b", text))

add={}
add[(203,"level_1")]=r'''### From a line segment to a composite trapezoid

The trapezoidal rule can be derived by replacing the curve on a short interval by the straight line joining its endpoint values. The area under that segment is the width multiplied by the average of the two ordinates. On [a,b] this gives (b−a)[f(a)+f(b)]/2. For a uniform partition with spacing h, adding the panel areas gives the composite formula: h times one half of the two endpoint values plus the full sum of the interior ordinates.

The derivation explains why interior values receive coefficient one and endpoints coefficient one half. Each interior ordinate is shared by the panel to its left and the panel to its right, so it contributes half a panel width twice. The two outer ordinates occur only once. This bookkeeping is a useful way to reconstruct the formula rather than memorize it.

If f is twice continuously differentiable, the leading composite trapezoidal error is proportional to h² and involves f'' over the interval. This means halving h often reduces the leading error by a factor near four when the asymptotic regime has been reached. It is an expectation justified by the error expansion, not a guarantee for every coarse partition or nonsmooth integrand. A sharp feature or endpoint singularity can defeat the smoothness assumptions.

Simpson's one-third rule follows a different local model: fit a parabola through three equally spaced ordinates. Its integral over the pair of subintervals is h/3 times the weighted combination 1,4,1. On a composite uniform grid, adjacent pairs overlap, creating the familiar alternating coefficients 1,4,2,4,...,2,4,1. The number of subintervals must be even. The source's composite formula and Romberg sequence rely on preserving this spacing and indexing.

### Why error order matters in extrapolation

Richardson extrapolation removes a known leading error term by combining estimates computed with different step sizes. If a method has an expansion I(h)=I+c h^p+ higher-order terms, then I(h/2) has leading error c h^p/2^p. A weighted combination cancels c. For the trapezoidal rule p=2, so the coarse and fine estimates are combined with factors 4 and 1, then divided by 3. This is the first Romberg extrapolation column.

Romberg integration repeats this process in a triangular table. Each new diagonal value uses a pair of estimates whose leading errors differ by a known power of two. The table is not a collection of unrelated approximations; each column is designed to eliminate another even-power error term under smoothness assumptions. The increasingly accurate diagonal values depend on both correct arithmetic and an error expansion that applies to the integrand.

For the source integral ∫_1^2 dx/x, the exact answer is ln 2. A trapezoidal approximation can be refined by halving h, and the first extrapolation should move the value closer to ln 2. The exact integral is a benchmark for checking the table, not a value used to construct it. If a table entry moves in the wrong direction or fails to improve plausibly, inspect the h indexing and the denominator 4^j−1 in the recurrence.

### Reading a Romberg table responsibly

The first column contains composite trapezoidal estimates at successively halved mesh widths. The entry R_(k,j) is formed from two entries in the preceding column. Rows correspond to refinement levels; columns correspond to extrapolation order. Only entries whose predecessors are available can be computed, so the table is triangular rather than rectangular.

When presenting a calculation, define which row represents h, h/2, or h/2^k. Then write the recurrence with those indices substituted. This avoids a frequent ambiguity in which R_(k,0) is called either the first or the zeroth level. Keep more digits in the input estimates than in the displayed final result, because the extrapolation subtracts nearby numbers and can magnify rounding.

Convergence of successive diagonal entries is useful evidence but does not automatically certify an error bound. If the smoothness assumptions fail, the nominal error expansion may not describe the behavior. A practical report can show the last diagonal values and their difference, while distinguishing this empirical stabilization from a rigorous remainder estimate. When a closed-form integral such as ln 2 is available, compare to it independently.

### Method choice for a definite integral

Use composite trapezoidal or Simpson formulas when equally spaced function values are provided, when a simple rule is required, or when local panel contributions are useful. Use Romberg when function evaluations can be generated at nested uniform grids and smoothness supports extrapolation. A nested grid reuses old ordinates: halving the mesh adds only the new midpoint values, which makes the sequence more efficient than recomputing every point.

If data are tabulated with nonuniform spacing, the standard composite formulas cannot be applied without adaptation. If the integrand is nonsmooth, splitting the interval at a change point or using a locally refined method is often more defensible than assuming high-order extrapolation will behave normally. Always identify what information is available and whether it meets the rule's spacing and smoothness assumptions.
'''

add[(203,"level_2")]=r'''### Deriving the composite trapezoidal error structure

On one panel [x_i,x_(i+1)] of width h, the trapezoidal estimate is the integral of the linear interpolant through the endpoint values. For a smooth f, Taylor expansion about the midpoint shows that the odd terms integrate to zero over the symmetric panel, while the leading discrepancy depends on the second derivative and is proportional to h^3 locally. Summing approximately (b−a)/h panels gives a global error of order h². This local-to-global scaling explains why a refinement by two reduces the leading global error by approximately four.

Simpson's formula integrates the quadratic interpolant through three equally spaced points. Its leading error involves the fourth derivative and scales as h^5 on each pair of panels, yielding a global O(h^4) error over a fixed interval. The composite rule requires an even number of equal subintervals so that the panels can be grouped in pairs. A missing or extra ordinate changes the weight pattern and invalidates the formula.

These orders are asymptotic statements under smoothness conditions. They do not mean every halving will reduce actual error by exactly four or sixteen. Higher-order terms, cancellation, roundoff, endpoint behavior, and nonsmoothness can alter the observed ratio. The error model is most useful when interpreted alongside computed refinement results.

### Richardson cancellation and the Romberg recurrence

Suppose a trapezoidal estimate has an expansion I(h)=I+c_2h^2+c_4h^4+\cdots. At half step, I(h/2)=I+c_2h^2/4+c_4h^4/16+\cdots. Forming [4I(h/2)−I(h)]/3 cancels c_2h^2, leaving an error of order h^4. Repeating the cancellation with further refinement produces Romberg's higher columns.

The denominator 4^j−1 in the general tableau recurrence arises because an error term h^(2j) changes by a factor 2^(−2j)=4^(−j) when the step is halved. Combining the fine and coarse estimates with the corresponding ratio removes that term. This derivation explains both the recurrence and why the power of four, rather than two, appears.

The extrapolation requires that the underlying estimates share a smooth even-power expansion. A discontinuity, a singular endpoint, or an irregular grid can invalidate that model. A table may still produce numbers, but its high-order columns then lack the usual theoretical interpretation. One should verify the assumptions before describing a Romberg diagonal as guaranteed higher order.

### Worked logarithm check and table diagnostics

For I=∫_1^2 dx/x=ln 2, the one-panel trapezoid is 3/4. The two-panel estimate uses ordinates at 1, 1.5, and 2. Since h=1/2, the composite formula gives

$$
T_2=\frac{h}{2}\left[f(1)+2f(1.5)+f(2)\right]
=\frac14\left(1+\frac43+\frac12\right)
=\frac{17}{24}\approx0.7083333.
$$

The exact value is ln 2≈0.6931472. Since 1/x is convex on [1,2], its secant segments lie above the curve, so the trapezoidal estimate overestimates the integral. The computed value is slightly above ln 2, consistent with that geometric check.

This correction illustrates why formulas should be checked against both direct substitution and qualitative behavior. The value 25/48 would result from an incorrectly weighted interior term. A diagnostic uses the composite trapezoidal pattern: the endpoints are halved, while every interior ordinate is counted fully inside the bracket before multiplying by h. Convexity predicts overestimation; an answer below the exact integral signals an arithmetic or formula error.

For Romberg, use the same consistent T_1 and T_2 values in the first extrapolation, [4T_2−T_1]/3. Since T_1=3/4 and T_2=17/24, this gives [17/6−3/4]/3=25/24/3? Compute common denominator: 17/6−3/4=34/12−9/12=25/12; divide by three gives 25/36≈0.6944444, close to ln 2. The extrapolated result is slightly above ln 2, which is plausible for this first correction.

The arithmetic check exposes a critical lesson: never preserve a derived number just because it appears in a polished table. Recompute the weights, panel width, endpoint coefficients, and exact reference independently. The two-panel trapezoid and first extrapolation are 17/24 and 25/36. Use exact fractions until the last step; they make transcription errors easier to detect.
'''

add[(203,"level_3")]=r'''### Composite rules as interpolatory formulas

The composite trapezoidal and Simpson formulas can be understood as sums of local interpolatory quadrature rules. On each trapezoidal panel, linear interpolation reproduces constants and linear functions exactly. On each Simpson pair, a quadratic interpolant reproduces polynomials through degree two locally; symmetry and the coefficient pattern raise the composite rule's exactness properties under the uniform-grid construction. This viewpoint explains why each rule has a distinct polynomial precision and error order.

For the trapezoidal rule, the global coefficient on an interior node is one full h because two neighboring panels each contribute h/2 times that ordinate. Endpoints receive only h/2. For Simpson, adjacent pairs overlap at shared nodes, producing the alternating 4 and 2 coefficients. Re-deriving a coefficient from panel contributions is an effective defense against table-layout mistakes.

The assumptions of uniform spacing are essential to these simple coefficients. If the spacing varies, the local widths differ and a single h cannot be factored out. Applying the uniform formula to nonuniform data silently changes the mathematical approximation. One must instead derive a rule for the actual nodes or interpolate and integrate with an appropriate method.

### Error expansions and Richardson extrapolation

For a sufficiently smooth integrand, the composite trapezoidal estimates at nested steps can be expanded as I(h)=I+c_2h^2+c_4h^4+c_6h^6+.... The absence of odd powers is tied to the symmetry and structure of the rule. Halving h scales the first error term by 1/4, the next by 1/16, and so on. The first Romberg transformation cancels c_2h^2 and leaves a leading term proportional to h^4.

The next transformation cancels the h^4 term between two already extrapolated estimates, producing a higher-order result. In general, the tableau recurrence combines neighboring entries with factors determined by 4^j. Each column removes one leading term, which is why the table is triangular and why the diagonal is often the most accurate sequence.

The theory depends on smoothness over the entire interval and compatible nested grids. If f has an endpoint singularity, a jump, or a derivative that is unbounded, the error may not have the assumed power series. In such cases Romberg entries can oscillate or converge irregularly. It is not enough to compute a high diagonal and call it highly accurate; one must consider whether the asymptotic model applies and compare refinements.

### Logarithm example with independent checks

For I=∫_1^2 dx/x, the exact value is ln 2. The one-panel trapezoid is

$$
T_1=\frac{2-1}{2}\left(1+\frac12\right)=\frac34.
$$

With h=1/2, the two-panel rule gives

$$
T_2=\frac{h}{2}\left[f(1)+2f(1.5)+f(2)\right]
=\frac14\left(1+\frac43+\frac12\right)
=\frac{17}{24}\approx0.7083333.
$$

Because f''(x)=2/x^3>0, the function is convex; each chord lies above its graph, so both trapezoidal estimates overestimate the integral. The refined result is closer to ln 2≈0.6931472, and its error has the expected reduction direction.

The first Romberg value is

$$
R_{1,1}=\frac{4T_2-T_1}{3}
=\frac{4(17/24)-3/4}{3}
=\frac{25}{36}\approx0.6944444.
$$

This lies only about 0.00130 above ln 2. The exact integral is used to assess the approximation, not in the extrapolation. The arithmetic also gives three independent checks: the weight pattern, the expected convexity sign, and comparison with the known value.

### Reading the Romberg triangle

With the initial trapezoid estimate labelled R_(0,0), a common indexing convention defines R_(k,0) as the composite trapezoid with 2^k subintervals. Then each higher column is computed by

$$
R_{k,j}=R_{k,j-1}+
\frac{R_{k,j-1}-R_{k-1,j-1}}{4^j-1}.
$$

The row index k denotes refinement; the column j denotes extrapolation order. At row k, only columns 0 through k exist. A correct table therefore has one more entry in each successive row. If a worksheet uses a different starting index, translate it explicitly before using the recurrence.

The fine and coarse entries must be neighbors in refinement and from the same column. Using a value from a different column or reversing the difference can destroy the intended cancellation. Keep exact fractions or several guard digits until the diagonal is calculated. Since extrapolation combines differences, premature rounding can make two close estimates appear equal and erase useful information.

### Distinguishing estimated convergence from a bound

If successive diagonal values agree to several digits, that is evidence of numerical stability. It is not automatically a rigorous bound on the error. A formal bound requires an error theorem with known derivative information or an interval-arithmetic argument. If the integral is known exactly, calculate the observed error. If not, report the difference between refinements as an indicator and label it accordingly.

The observed ratio between errors on successive mesh widths can be compared with the expected factor 4 for trapezoidal leading error or 16 for Simpson's leading error. A ratio near the theoretical value suggests that the asymptotic regime may have been reached. A ratio far from it can indicate a coarse grid, a nonsmooth function, roundoff, or an arithmetic mistake. It should prompt investigation rather than an automatic claim that the method failed.

### Method choice and numerical cost

Nested Romberg grids reuse previously computed ordinates. Refining from 2^k to 2^(k+1) subintervals requires only the new midpoint evaluations, so the cost grows more slowly than recomputing a full independent grid at every level. The method is attractive when f is smooth and each evaluation is available at the needed points.

If the function is expensive or the interval contains localized behavior, adaptive panel refinement may use evaluations more efficiently. If only a fixed equally spaced data table is given, Simpson or trapezoidal rules may be directly applicable, while Romberg may require additional evaluations not present in the data. A sound comparison states these constraints and does not infer a universal winner from asymptotic order alone.
'''

add[(204,"level_1")]=r'''### Understanding the moment conditions

The three-point Legendre weights can be checked by integrating simple functions. On [−1,1], the integral of 1 is 2, so the weights must sum to 2. The integral of x² is 2/3 and x⁴ is 2/5. For symmetric nodes −r,0,r and weights A,B,A, the corresponding sums are 2A+B, 2Ar², and 2Ar⁴. Matching these moments yields r²=3/5, A=5/9, and B=8/9.

These checks are useful when a node-weight table is copied from memory. If the weights do not sum to two, even a constant integrand is wrong. If the second or fourth moment fails, the claimed degree of precision is not supported. Odd moments provide further checks because both the true integral and symmetric weighted sum vanish.

Moment matching also clarifies the difference between choosing weights and choosing nodes. With fixed nodes, integrating the Lagrange basis determines weights and gives exactness through degree n−1. Gaussian quadrature chooses nodes as well, through orthogonal-polynomial roots, which is why n points can reach degree 2n−1. The nodes and weights form a coordinated rule.

### Mapping while preserving orientation

The affine map x=c+dt uses c=(a+b)/2 and d=(b−a)/2. The transformed differential is dx=d dt, so d—not the full interval length—is the factor multiplying the reference sum. For f=1, the reference weights sum to 2 and the answer becomes 2d=b−a. This check is a compact way to detect a missing factor or a mistaken half-width.

If a>b, the half-width d is negative. The same change of variables then yields a negative integral, respecting the orientation of the limits. Replacing d by |d| without restoring the sign changes the mathematical problem. Most standard tables assume a<b, but a general formula should retain the signed width.

On a composite partition, compute a separate midpoint and half-width for each subinterval. Each local rule contributes its own d_j times a weighted sum. Reusing the whole-interval d for every panel multiplies the scale incorrectly. This local map also explains how the reference nodes are reused without re-deriving a new quadrature formula on each piece.

### What a smoothness assumption contributes

Polynomial exactness is an algebraic guarantee. It says that the error is zero for a finite-dimensional class of functions; it does not quantify the error for every smooth function. Smoothness matters because it permits approximation by polynomials and supports remainder estimates. If a function is discontinuous or has a singularity, the high-degree exactness result still holds for test polynomials but may provide little practical guidance for that integrand.

For example, a function with a narrow peak between Gaussian nodes may be sampled poorly by a single global panel even when the rule has high polynomial precision. Subdividing the interval places nodes closer to the feature. A jump should generally be used as a panel boundary. These choices do not contradict the Gaussian theorem; they address a different issue—the representativeness of the samples for a non-polynomial integrand.

The three-node rule integrates x^6 with a known nonzero difference because its degree exceeds five. The exponential example is close to exact but not covered by the polynomial theorem. These examples should be described separately: the first is a polynomial counterexample just beyond the precision range; the second is a smooth non-polynomial comparison with an available antiderivative.

### Reading a final approximation

A numerical result should state which rule and interval were used, show that the transformed nodes lie inside the interval, include the half-width, and explain whether exactness or approximation applies. If f is a polynomial through degree five, the three-node rule is exact in exact arithmetic. Otherwise, state an approximation and any independent error comparison.

Keep the three sampled values distinct until each is multiplied by its weight. Simplifying by symmetry is valid only when the transformed integrand is symmetric about the panel midpoint. For a general f on [a,b], the left and right node values may differ. Averaging them without justification can change the integral estimate.

Finally, round after adding the weighted contributions and applying the scale. If the ordinates were rounded or measured, the final digits cannot be more reliable than those inputs. A formula can be exact for a polynomial in symbolic arithmetic while a calculator result differs in the last place because of floating-point rounding; distinguish mathematical exactness from finite computation.
'''

add[(204,"level_2")]=r'''### Interpolatory weights and the Gaussian improvement

For fixed nodes x_i, define L_i(x) as the Lagrange basis polynomial that is one at x_i and zero at every other node. The interpolating polynomial is ∑f(x_i)L_i(x), and integrating it gives the quadrature weights A_i=∫L_i(x)dx. This rule reproduces all polynomials of degree at most n−1, because interpolation is exact in that degree range.

Gaussian quadrature improves the node selection. Let q_n be an orthogonal polynomial of degree n, and choose its roots as the quadrature nodes. Any polynomial p of degree at most 2n−1 can be divided into q_ns+r, with both s and r of degree at most n−1. Orthogonality eliminates the integral of q_ns, while its roots eliminate that term at every node. The remainder is already exactly integrated by the interpolatory rule. This is the structural reason for the doubled precision.

The proof shows why arbitrary nodes do not inherit Gaussian precision. They may yield an excellent interpolatory formula, but unless their node polynomial has the required orthogonality, the divisible part need not vanish in the integral. The moment derivation for three nodes and the orthogonality proof are two views of the same construction: one solves a concrete small system; the other explains the general theorem.

### The role of the Legendre weight

Gauss–Legendre quadrature uses the constant weight function one on [−1,1]. Its orthogonal polynomials are Legendre polynomials. For three nodes, P_3(x)=(5x^3−3x)/2 has roots 0 and ±√(3/5). The nodes are symmetric because the polynomial is odd. The weights obtained by integrating the Lagrange basis are 5/9,8/9,5/9.

Different weight functions or integration intervals lead to different Gaussian families. A Legendre table should not be used indiscriminately for an integral with a nonconstant weight unless that weight is incorporated into the integrand or another quadrature family is selected. Likewise, the Legendre node table is defined for the reference interval; the affine map is required to use it on [a,b].

The root locations are all interior to the reference interval. This distinguishes the Gaussian rule from endpoint-based Newton–Cotes formulas. The weights are positive in this standard Legendre case and sum to the interval's reference length. These properties are useful checks, but they do not imply that every nonnegative integrand is approximated from above or below.

### A two-panel composite Gaussian construction

Suppose [a,b] is divided at m=(a+b)/2. On each half, use the same three reference nodes and weights, but map them using that panel's midpoint and half-width. The full composite estimate is the sum of the left-panel and right-panel contributions. Each contribution has its own scale factor; no endpoint values are required by the local Gaussian nodes.

The composite rule remains exact for a polynomial of degree at most five on each panel, and therefore for the sum over the full interval. This follows by applying the local exactness theorem separately. It does not become a six-node global Gaussian rule: the points are grouped by subinterval and the weights carry separate half-width scales.

Subdivision is useful when the function changes noticeably across the interval. It places three nodes in each local region, which can resolve a peak or curvature variation missed by a single global panel. However, the extra function evaluations cost time. One should compare the one-panel and subdivided estimates or use a relevant error theorem rather than subdividing without a goal.

### Error evidence without an exact antiderivative

If an exact integral is known, calculate the observed absolute error |I−Q| and, if meaningful, the relative error. If it is not known, compare a higher node order or a composite refinement. The difference between two estimates is a practical indicator, but it is not automatically a rigorous upper bound. An error theorem requires its own smoothness and derivative conditions.

Roundoff is separate from quadrature truncation. Nodes such as √(3/5) are represented approximately on a computer; function values and weighted products are rounded as well. If the integrand values are supplied as measurements, their uncertainty is propagated through the weighted sum. A polynomial exactness theorem assumes exact inputs and exact arithmetic, so it does not remove these sources of error.

When reporting precision, do not claim more digits than the function evaluations or error evidence support. Retain guard digits, show the scale factor, and state whether accuracy is known from an exact comparison or inferred from refinement. This is especially important when extrapolated or weighted sums involve cancellation.
'''

add[(204,"level_3")]=r'''### A basis verification of the three-point precision

The polynomials 1,x,x²,x³,x⁴,x⁵ form a basis for all polynomials of degree at most five. The integral and the quadrature sum are linear. Therefore it is sufficient to check equality on those six monomials. The moment equations give agreement for 1,x²,x⁴; symmetry gives zero for x,x³,x⁵ on both the integral and quadrature sides. This proves degree-five exactness without testing an arbitrary polynomial one at a time.

The argument also explains the three-point rule's failure on x^6. That monomial is outside the verified basis. The resulting difference 2/7−6/25=8/175 is not a contradiction or an anomaly; it is a concrete witness that the guarantee cannot be extended to all degree-six polynomials. A particular higher-degree polynomial may still be integrated exactly by coincidence, but that would not change the stated degree of precision.

### Constructing and checking the weights

Write the unknown symmetric rule as A f(−r)+B f(0)+A f(r). Exactness for the constant gives 2A+B=2. Exactness for x² gives 2Ar²=2/3; exactness for x⁴ gives 2Ar⁴=2/5. Dividing the last equation by the second yields r²=3/5. Substitution then gives A=5/9 and B=8/9. The unknown node and weights are solved together.

This derivation is more than a shortcut. If r were fixed arbitrarily and only the weights solved, the rule would not generally reach degree five. The additional freedom in node placement is the source of the improved exactness. In the general Gaussian construction, orthogonal-polynomial roots choose those locations systematically.

An independent implementation check applies the rule to 1, x², and x⁴. The weights sum to two; the second moment is 2/3; the fourth moment is 2/5. Also test an odd monomial to verify symmetry. These low-cost checks catch a misordered table entry or a mistyped radical before the rule is used on a complicated integrand.

### The affine map as a Jacobian calculation

Let c=(a+b)/2 and d=(b−a)/2, and set x=c+dt. Then t=−1 maps to a, t=1 maps to b, and dx=d dt. Substitution transforms the integral to d∫_(−1)^1 f(c+dt)dt. The factor d is the Jacobian of the change of variable, not an optional normalization.

For three nodes, the mapped points are c−d√(3/5), c, and c+d√(3/5). A direct check with f=1 gives d(5/9+8/9+5/9)=2d=b−a. This verifies both the sum of weights and the scale. If a>b, d is negative, preserving the orientation of the definite integral. If one uses |d|, the sign must be restored separately.

On a composite partition, each panel has its own c_j and d_j. The rule is

$$
\sum_j d_j\sum_{i=1}^{3}A_i f(c_j+d_jt_i).
$$

The local half-width cannot be replaced with a global value unless the panels are known to have that same width. Writing the two nested sums makes it clear how the quadrature values and panel scales are organized.

### Limits of the exactness theorem

The Gaussian precision theorem is exact and strong within its scope: an n-node rule integrates every polynomial of degree at most 2n−1 exactly on the reference interval, and affine transformation preserves that property for a polynomial integrand on a finite interval. It does not state that the error for every smooth function is below a fixed tolerance, nor that increasing n always improves every computed result under finite precision.

For non-polynomial functions, a practical error analysis needs additional information. Smoothness can support a Gaussian remainder formula, but the relevant derivative bound may be difficult to obtain. Alternatively, compare a higher-order rule or subdivide the interval and examine stability. Such comparisons are useful evidence but are not automatically rigorous bounds. State exactly which kind of evidence is available.

If f has a discontinuity, a singularity, or a sharply localized feature, one global polynomial approximation may be poor. Split the integral at known discontinuities, transform endpoint singularities if appropriate, or refine panels where the integrand varies rapidly. These are method adaptations, not exceptions to the polynomial theorem.

### Interpreting x^6 and the exponential comparison

For x^6, the center sample is zero and both outer samples equal (3/5)^3. The weighted sum is 6/25=0.24, while the exact integral is 2/7≈0.285714. The exact difference is 8/175≈0.0457143, so the rule underestimates this particular even function. Positivity and symmetry alone do not prove a general direction of error; the conclusion belongs to this integrand.

For e^x on [0,1], the mapped three-point estimate is approximately 1.7182810044 and the exact integral e−1≈1.7182818285. This is a close approximation but not an exact result. The observed error is about 8.24×10^−7. The result depends on the interval and function; it is not a uniform performance guarantee for all exponentials or all smooth functions.

Together these examples test two different claims. The x^6 example tests the boundary of polynomial precision. The exponential example demonstrates practical approximation of a smooth non-polynomial and permits an observed error calculation. A well-written answer identifies which role the example plays.

### Reproducible algorithm and verification sequence

An implementation can be organized in a short, auditable sequence: store the reference nodes and weights; for every panel compute its midpoint and signed half-width; map each node; evaluate f; form the weighted sum; multiply by the half-width; and sum panels. Keep node-weight pairing intact and avoid rounding the mapped points prematurely.

Verify the implementation first with f=1, then with low-degree monomials. The constant check verifies scaling; the second- and fourth-moment checks verify the three-point table; an odd test verifies symmetry. Only after these checks should a more complicated integrand be used. This is more reliable than debugging solely from one final decimal.

The final report should name the rule, node count, interval transformation, approximation, and error evidence. If a source exercise supplies an exact comparison, calculate it directly. If no exact integral is known, explain whether the result was checked by refinement, a higher order, or a formal remainder estimate. This makes the numerical claim reproducible and appropriately cautious.
'''

def save_group(tid, ids):
    from django.db import transaction
    from django.utils import timezone
    from prep.models import PrepTopic, PrepContentCache
    from services.prep_ai_router import (
        _cache_payload_as_dict, _note_validation_options, _note_completion_issues,
        _topic_notes_cache_signature, _course_study_profile_version,
        _topic_content_rules_version, NOTE_VALIDATION_STATE,
    )
    from services.prep_blocks import parse_markdown_to_blocks
    topic=PrepTopic.objects.get(pk=tid,course_id=48)
    rows={x.pk:x for x in PrepContentCache.objects.filter(
        pk__in=ids.values(),topic=topic,content_type="topic_notes")}
    if set(rows)!=set(ids.values()):raise RuntimeError(f"Rows changed for {tid}")
    options=_note_validation_options(topic.course,topic.title,topic.summary,topic.subtopics,topic_obj=topic)
    sig=_topic_notes_cache_signature(topic.course,topic,topic.title,topic.subtopics)
    candidates={}
    for level,rid in ids.items():
        row=rows[rid];payload=_cache_payload_as_dict(row.payload)
        if payload.get("level")!=level:raise RuntimeError(f"Level changed {rid}")
        original=str(payload.get("content") or "")
        content=r["replace_section"](original,5,r["section"](original,5)+"\n\n"+add[(tid,level)])
        content=r["norm"](content)
        words=prose_word_count(content)
        if words<=5000:raise RuntimeError(f"{rid} has only {words} prose words")
        issues=_note_completion_issues(content,topic.title,level=level,allow_validated_legacy_headings=False,**options)
        if issues:raise RuntimeError(f"{rid} validation failed: {issues}")
        blocks=parse_markdown_to_blocks(content)
        if not blocks:raise RuntimeError(f"No blocks for {rid}")
        candidates[rid]=(level,payload,original,content,blocks,words)
        print("CANDIDATE",rid,level,"prose",words,"blocks",len(blocks))
    if os.environ.get("SMA330_SAVE")!="1":
        print("PREFLIGHT_ONLY",tid);return
    with transaction.atomic():
        for rid,(level,payload,original,content,blocks,words) in candidates.items():
            row=PrepContentCache.objects.select_for_update().get(
                pk=rid,topic_id=tid,course_id=48,content_type="topic_notes")
            current=_cache_payload_as_dict(row.payload)
            if current.get("level")!=level or current.get("content")!=original:
                raise RuntimeError(f"Cache {rid} changed immediately before edit")
            payload.update({
                "content":content,"blocks":blocks,"source_signature":sig,
                "validation_state":NOTE_VALIDATION_STATE,"validated_at":timezone.now().isoformat(),
                "source_references":options.get("source_references") or [],
                "study_profile_version":_course_study_profile_version(topic.course),
                "topic_content_rules_version":_topic_content_rules_version(topic),
            })
            row.payload=payload;row.save(update_fields=["payload","updated_at"])
    print("UPDATED_TOPIC",tid,sorted(candidates))

save_group(203,{"level_1":1294,"level_2":1259,"level_3":1336})
save_group(204,{"level_1":1296,"level_2":1260,"level_3":1337})
