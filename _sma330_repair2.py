import os, re, json, hashlib, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings.development')
import django
django.setup()
from django.db import transaction
from django.utils import timezone
from prep.models import PrepTopic, PrepContentCache
from services.prep_ai_router import (_cache_payload_as_dict, _note_validation_options,
    _note_completion_issues, _topic_notes_cache_signature,
    _course_study_profile_version, _topic_content_rules_version, NOTE_VALIDATION_STATE)
from services.prep_blocks import parse_markdown_to_blocks
LABELS={1:'Foundational Concepts, Definitions, and Axioms',2:'Theorems, Lemmas, and Analytical Properties',3:'Formal Proofs, Derivations, and Methods',4:'Representative Worked Examples and Solutions',5:'Mathematical Extensions, Limits, and Common Errors'}
def replace_section(text,number,body):
    m=list(re.finditer(r'(?m)^##\s+'+str(number)+r'\.\s+[^\n]*\n',text))
    if len(m)!=1: raise RuntimeError(f'heading {number}: {len(m)}')
    start=m[0].end(); n=re.search(r'(?m)^##\s+\d+\.\s+',text[start:]); end=start+n.start() if n else len(text)
    return text[:start]+body.strip()+'\n\n'+text[end:]
def section(text,number):
    m=list(re.finditer(r'(?m)^##\s+'+str(number)+r'\.\s+[^\n]*\n',text))
    if len(m)!=1: raise RuntimeError(f'heading {number}: {len(m)}')
    start=m[0].end(); n=re.search(r'(?m)^##\s+\d+\.\s+',text[start:]); end=start+n.start() if n else len(text)
    return text[start:end].strip()
def norm(text):
    return re.sub(r'(?m)^##\s+([1-5])\.\s+[^\n]*',lambda m:f'## {m.group(1)}. {LABELS[int(m.group(1))]}',text)
def repair_topic(tid,expected,supplements,examples=None,section_bodies=None):
    t=PrepTopic.objects.get(pk=tid,course_id=48)
    rows={r.pk:r for r in PrepContentCache.objects.filter(pk__in=expected.values(),topic=t,content_type='topic_notes')}
    if set(rows)!=set(expected.values()): raise RuntimeError(f'{tid}: cache rows changed {sorted(rows)}')
    opts=_note_validation_options(t.course,t.title,t.summary,t.subtopics,topic_obj=t)
    sig=_topic_notes_cache_signature(t.course,t,t.title,t.subtopics)
    cand={}
    for lev,rid in expected.items():
        row=rows[rid]; payload=_cache_payload_as_dict(row.payload)
        if payload.get('level')!=lev: raise RuntimeError(f'{rid}: level changed')
        original=str(payload.get('content') or '')
        content=original
        if examples and lev in examples: content=replace_section(content,4,examples[lev])
        if section_bodies and lev in section_bodies:
            for secno,body in section_bodies[lev].items(): content=replace_section(content,secno,body)
        content=replace_section(content,5,section(content,5)+'\n\n'+supplements[lev])
        content=norm(content)
        wc=len(re.findall(r"\b[\w’'-]+\b",content))
        if wc<=5000: raise RuntimeError(f'{rid} only {wc} words')
        issues=_note_completion_issues(content,t.title,level=lev,allow_validated_legacy_headings=False,**opts)
        if issues: raise RuntimeError(f'{rid}: validation {issues}')
        blocks=parse_markdown_to_blocks(content)
        if not blocks: raise RuntimeError(f'{rid}: no parsed blocks')
        cand[rid]=(lev,payload,original,content,blocks,wc)
        print('CANDIDATE',rid,lev,'words',wc,'blocks',len(blocks))
    with transaction.atomic():
        for rid,(lev,payload,original,content,blocks,wc) in cand.items():
            row=PrepContentCache.objects.select_for_update().get(pk=rid,topic_id=tid,course_id=48,content_type='topic_notes')
            current=_cache_payload_as_dict(row.payload)
            if current.get('level')!=lev or current.get('content')!=original: raise RuntimeError(f'{rid}: changed before edit')
            p=dict(payload); p.update({'content':content,'blocks':blocks,'source_signature':sig,'validation_state':NOTE_VALIDATION_STATE,
                'validated_at':timezone.now().isoformat(),'source_references':opts.get('source_references') or [],
                'study_profile_version':_course_study_profile_version(t.course),'topic_content_rules_version':_topic_content_rules_version(t)})
            row.payload=p; row.save(update_fields=['payload','updated_at'])
    print('UPDATED_TOPIC',tid,sorted(cand))
sections={}
sections['level_1']={}
sections['level_1'][3]=r'''### Deriving the three-node Gauss–Legendre rule

The lesson's three-point rule is built on the reference interval from −1 to 1. Because the interval is symmetric, choose three symmetric nodes: −r, 0, r. Seek a weighted sum whose end nodes have the same weight A and whose center has weight B. Symmetry automatically makes the rule exact for odd functions: both the integral and the quadrature sum are zero. To determine A, B, and r, require exactness for the even monomials 1 and x² as well.

For f(x)=1, the exact integral is 2. The weighted sum is 2A+B, so 2A+B=2. For f(x)=x², the exact integral is 2/3 and the weighted sum is 2Ar², so 2Ar²=2/3. To ensure the highest possible degree for three nodes, also use the x⁴ moment: its integral is 2/5 and the rule gives 2Ar⁴=2/5. Dividing the x⁴ equation by the x² equation yields r²=3/5. Substituting into the x² moment gives A=5/9, and the constant equation gives B=8/9.

The resulting nodes and weights are

$$
\begin{aligned}
x_1&=-\sqrt{3/5},&x_2&=0,&x_3&=\sqrt{3/5},\\
A_1&=5/9,&A_2&=8/9,&A_3&=5/9.
\end{aligned}
$$

Thus

$$
\int_{-1}^{1}f(x)\,dx\approx\frac59f\!\left(-\sqrt{3/5}\right)+\frac89f(0)+\frac59f\!\left(\sqrt{3/5}\right).
$$

This simple moment calculation explains why the weights are not equal: the central point represents a different share of the interval's polynomial area than either outer point. It also shows how an undetermined-coefficient method works. Propose a formula with unknown nodes and weights, apply it to a set of test polynomials, and solve the resulting equations. A symmetric choice reduces the algebra because odd moments vanish.

### Why three nodes give precision through degree five

The three weights and three nodes are selected so that the rule integrates polynomial test functions exactly up to degree five. In general, an n-node Gauss–Legendre rule is exact for every polynomial through degree 2n−1. For three nodes, that means degree five. Exactness for all such polynomials follows from the construction based on the orthogonal polynomial whose roots are the nodes; it is stronger than merely matching three or six isolated examples.

A quick check uses symmetry. The rule is exact for x, x³, and x⁵ because each is odd and integrates to zero on the symmetric interval. It is exact for 1, x², and x⁴ because the moment equations were chosen to match those integrals. These six monomials form a basis for all polynomials of degree at most five, so linearity implies exactness for every polynomial in that space. The statement says nothing that all non-polynomial functions will be integrated exactly. For them, the rule remains an approximation, though a smooth function may be approximated effectively by polynomials.

The standard three-point rule uses interior nodes, not interval endpoints. This is different from the composite trapezoidal rule, which uses endpoint values and evenly spaced samples. The Gaussian nodes are chosen to maximize polynomial exactness for a given node count; they are not selected simply because they are convenient points on a uniform grid. If function values are supplied only at equally spaced points, a Gaussian rule may not be usable without evaluating or interpolating at its nodes.
'''
sections['level_2']={}
sections['level_2'][3]=r'''### Constructing the three-point rule by moments and orthogonality

The source's Gaussian quadrature theorem can be understood in two connected ways. The direct calculation determines unknown nodes and weights by matching moments; the orthogonality argument explains why an n-point Gaussian rule reaches degree 2n−1. On [−1,1], symmetry suggests three nodes −r,0,r and weights A,B,A. Exactness for 1, x², and x⁴ gives

$$
2A+B=2,\qquad 2Ar^2=\frac23,\qquad 2Ar^4=\frac25.
$$

Dividing the last relation by the second gives r²=3/5, and back-substitution yields A=5/9 and B=8/9. Odd moments vanish on both sides by symmetry. Thus the rule is exact through degree five, not merely through degree two, because the even moments through degree four and all intervening odd moments agree.

For a general n-node Gaussian rule, let q_n be a degree-n polynomial orthogonal on the interval to every polynomial of degree at most n−1. Its n roots are the quadrature nodes. To see the exactness, divide any polynomial p of degree at most 2n−1 by q_n:

$$
p(x)=q_n(x)s(x)+r(x),\qquad \deg s\le n-1,\quad \deg r\le n-1.
$$

Orthogonality makes the integral of q_ns vanish. At every Gaussian node x_i, q_n(x_i)=0, so the quadrature sum of q_ns also vanishes. The remainder r has degree at most n−1 and is integrated exactly by the interpolatory rule determined by the nodes and weights. Therefore the quadrature and the true integral agree for p. This decomposition is the core reason Gaussian quadrature doubles the exactness degree relative to a simple “n conditions for n weights” intuition.

For Legendre weight one on [−1,1], the degree-three orthogonal polynomial is proportional to 5x³−3x. Its roots are 0 and ±√(3/5), matching the moment derivation. The corresponding Lagrange basis polynomials integrate to 5/9, 8/9, 5/9. This second route explains the general theorem while the moment equations are usually quicker when a three-point rule must be derived by hand.

### Mapping the reference rule to a general interval

A tabulated Gauss–Legendre rule on [−1,1] is transferred to [a,b] using the linear map x=c+dt, where c=(a+b)/2 and d=(b−a)/2. Then dx=d dt, and the integral becomes

$$
\int_a^b f(x)\,dx=d\int_{-1}^{1}f(c+dt)\,dt
\approx d\sum_{i=1}^{n}A_i f(c+dt_i).
$$

The factor d multiplies the weighted sum; omitting it is a common scaling error. The transformed nodes are x_i=c+dt_i and remain inside [a,b]. For a reversed interval, d is negative and the signed integral changes orientation consistently.

For example, on [0,1], c=d=1/2. The three nodes become (1−√(3/5))/2, 1/2, and (1+√(3/5))/2. Applying the reference weights requires one function evaluation at each of these nonuniform points, then multiplication of the weighted sum by one half. This transformed form is preferable to re-deriving a new rule on every interval.
'''
sections['level_3']={}
sections['level_3'][3]=r'''### Orthogonality proof of Gaussian exactness

Let q_n be a degree-n polynomial orthogonal on [a,b] with weight w(x) to every polynomial of degree less than n, and let its n distinct roots x_1,…,x_n be the Gaussian nodes. Define the interpolatory quadrature weights by integrating the Lagrange basis functions associated with those nodes. The resulting rule is exact for every polynomial of degree at most n−1 by construction. The stronger degree 2n−1 result follows from polynomial division.

For any polynomial p with deg p≤2n−1, write p=q_ns+r with deg s≤n−1 and deg r≤n−1. Orthogonality gives ∫wq_ns=0. At each quadrature node q_n(x_i)=0, so the discrete sum of w(x_i)q_n(x_i)s(x_i) also vanishes. The remainder r is exactly integrated by the interpolatory rule. Hence the quadrature sum of p equals its weighted integral. The Gaussian choice therefore achieves exactness through degree 2n−1 while using only n evaluations. The node selection is crucial: arbitrary distinct nodes with interpolatory weights do not in general have this doubled precision.

For the Legendre case, w(x)=1 on [−1,1]. For three nodes, the orthogonal cubic is proportional to P_3(x)=(5x³−3x)/2. Its roots are −√(3/5), 0, √(3/5). Symmetry forces equal outer weights. Moment matching yields 5/9, 8/9, 5/9. The Gaussian theorem says the resulting formula is exact for every polynomial through degree five; this is also checked by matching the even moments 1, x², x⁴ and using symmetry for x, x³, x⁵.

The theorem assumes an appropriate orthogonal polynomial and distinct nodes in the interval. Its exactness conclusion is algebraic; it does not by itself quantify the error for a general smooth non-polynomial function. A higher node count increases the degree of polynomial exactness, but the actual error depends on the integrand and the interval. Do not infer a universal error bound merely from the degree-of-precision statement.

### Undetermined coefficients as an alternative derivation

On the symmetric reference interval, begin with unknown symmetric nodes −r,0,r and weights A,B,A. Matching moments gives 2A+B=2, 2Ar²=2/3, and 2Ar⁴=2/5. The ratio of the last two equations gives r²=3/5; the remaining equations give A=5/9 and B=8/9. This calculation illustrates the general undetermined-coefficients method described in the lecture: choose an ansatz, impose exactness on an appropriate polynomial basis, and solve for the unknown constants.

A subtle point is that merely matching n monomials for n weights at fixed nodes produces exactness through degree n−1, not automatically 2n−1. Gaussian precision comes from selecting the nodes as roots of the orthogonal polynomial. The moment derivation with free symmetric nodes makes this extra freedom visible: the node location r is solved along with the weights. This distinction helps identify why a Gaussian rule is special rather than just another interpolatory sum.

### Affine transformation and orientation

Set c=(a+b)/2 and d=(b−a)/2. Under x=c+dt, t ranges from −1 to 1, dx=d dt, and

$$
\int_a^b f(x)\,dx=d\int_{-1}^{1}f(c+dt)\,dt\approx d\sum_{i=1}^n A_i f(c+dt_i).
$$

When a<b, d>0. If the integration limits are reversed, d<0 and the mapped rule preserves the sign of the oriented integral. This is a useful consistency check. The transformed nodes are not uniformly spaced; for the three-point rule they are c−d√(3/5), c, c+d√(3/5). The weights themselves stay the same on the reference scale, while the common Jacobian factor d rescales all contributions.
'''
# Save section-3 derivations and continue adding level-specific quadrature exposition below.
extras={}
extras['level_1']=r'''### Using the three-point rule on a new interval

Once the reference nodes and weights are known, an integral on another interval becomes a substitution task. Find the midpoint c=(a+b)/2 and half-width d=(b−a)/2. Replace each reference node t_i by x_i=c+dt_i, evaluate f at the three new x values, add each value times its weight, and finally multiply by d. The node locations move with the interval, but the weights 5/9, 8/9, 5/9 do not change. The outside factor d accounts for the change in interval length.

For [0,1], c=d=1/2. The outer nodes lie at about 0.1127 and 0.8873, while the central node is 0.5. These are not equally spaced: Gaussian quadrature chooses them to give high polynomial exactness, not to make a uniform table. A learner should not substitute the endpoints 0 and 1 into the rule. Nor should the factor one half be omitted; doing so would double the result on this interval.

A useful routine is to write a small table with columns for the reference node t_i, the mapped point x_i, the weight A_i, and the weighted function value A_i f(x_i). That table keeps the interval transformation visible. After the weighted sum is formed, multiply by d and check the scale. If f is the constant one, the result must be b−a, since the weights sum to two and d=(b−a)/2. This constant-function check catches a missing Jacobian immediately.

### Exactness as a practical test

The three-point Gauss–Legendre formula exactly integrates every polynomial of degree at most five on the reference interval. This is a powerful check but not a promise that all functions are exact. A polynomial x^4 should be reproduced exactly; x^6 is outside the guaranteed range and can show a difference. A smooth exponential is also not a polynomial, so its result is an approximation that can be compared with its known integral if one is available.

The guarantee helps choose a rule. If the function is a polynomial of degree five or less, one application of the three-point formula is exact in exact arithmetic. For a higher-degree polynomial or a non-polynomial integrand, the rule still gives a useful weighted estimate but there is truncation error. If the interval is long or the function changes rapidly, using subintervals can improve resolution. For each subinterval, map the same three reference nodes and add the resulting estimates. A single high-degree exactness statement does not eliminate the need to examine the function's behavior.

### How to explain the answer

In a written solution, identify the three-point Gaussian rule, list its nodes and weights, show the interval map, and substitute the function values. Keep the final factor (b−a)/2 visible. Then state whether the calculation is exact by polynomial degree or is an approximation. When an exact integral is known, compare the two; otherwise avoid unsupported claims about the number of correct digits.

The nodes are selected in advance for the rule; the weights describe how much each sampled function value contributes. Their sum is two on [−1,1], the area under the constant function one. The outer weights sum to 10/9 and the central weight is 8/9, so the center carries a little less than half of the total weight. These checks make the formula easier to remember and help detect a copied weight or node with the wrong sign.
'''
extras['level_2']=r'''### Degree of precision and what it does not say

A quadrature rule's degree of precision is the largest integer m for which it integrates every polynomial of degree at most m exactly. This is stronger than testing one polynomial: every linear combination of the basis monomials through degree m is then exact by linearity. The n-point Gauss–Legendre rule has degree 2n−1, so the three-point rule has degree five. Its exactness is a structural property of the chosen nodes and weights, not a result of using a very fine mesh.

Degree of precision must be distinguished from an error bound on a general function. For a non-polynomial f, the output depends on how well its behavior is represented by the sampled values and the rule's implied polynomial approximation. A smooth exponential may be accurate even though it is not integrated exactly; a polynomial just beyond degree five may show a more visible error. The exactness theorem alone does not provide the error for either case. Avoid statements such as “three points give six correct digits” unless a separate estimate establishes them.

The three-point rule's moments provide a diagnostic. For constants, the weighted sum is 2. For x² it is 2/3, and for x⁴ it is 2/5. Odd powers have zero integral and cancel because the nodes and weights are symmetric. These moment checks validate the node/weight table and are more reliable than memorizing decimals. They also reveal that the center point cannot be assigned the same weight as the outer nodes: doing so would fail the constant and second-moment equations.

### Source example beyond the exactness range

For f(x)=x^6 on [−1,1], the exact integral is 2/7. The three-point formula uses the two outer nodes whose sixth powers are (3/5)^3=27/125; the center term is zero. Therefore

$$
Q_3[x^6]=\frac59\frac{27}{125}+\frac89(0)+\frac59\frac{27}{125}=\frac{6}{25}=0.24.
$$

The exact value 2/7 is approximately 0.285714, so the error is about 0.0457143. This agrees with the lesson's listed value 0.045714285. The discrepancy is expected: x^6 has degree six, one more than the exactness limit of five. It would be a mistake to call the Gaussian rule inaccurate merely because this polynomial lies outside its guarantee; the example illustrates precisely where the guarantee ends.

By contrast, for x^4 the exact integral and Gaussian sum are both 2/5. This contrast is a useful verification pair: the method matches a degree-four polynomial and does not have to match a degree-six polynomial. In either case, the comparison should be based on the exact integral rather than on a vague statement that the result “looks close.”

### Comparison with equally spaced Newton–Cotes rules

The source distinguishes Newton–Cotes formulas, which use equally spaced nodes, from Gaussian quadrature, which chooses nodes and weights to achieve high exactness. Composite trapezoidal and Simpson formulas are especially convenient when values are already tabulated on a uniform grid. A Gaussian rule is attractive when the function can be evaluated at its nonuniform nodes and a high polynomial degree of precision per evaluation is useful.

These methods answer the same broad question—approximating a definite integral—but have different data requirements. Do not apply a Gauss–Legendre weight table to arbitrary equally spaced table entries; first map the reference nodes and obtain values at those points. Conversely, do not claim Gaussian quadrature is automatically superior when only fixed-grid observations are available. Method choice must fit both the integrand and the permitted evaluations.
'''
extras['level_3']=r'''### Exactness proof and error interpretation

For n Gaussian nodes, the orthogonality construction selects a degree-n polynomial q_n whose roots are the nodes. If p has degree at most 2n−1, polynomial division gives p=q_ns+r with both s and r of degree at most n−1. Orthogonality makes the integral of q_ns vanish. At every Gaussian node q_n is zero, so the quadrature sum of q_ns vanishes as well. The remainder r is integrated exactly by the interpolatory weights. Therefore the full p is exact. This proof identifies the key premise: the nodes are roots of the appropriate orthogonal polynomial. Equal node count alone does not give the degree 2n−1 guarantee.

For three-point Legendre quadrature, q_3 is proportional to 5x³−3x and the roots are 0 and ±√(3/5). The weights 5/9, 8/9, 5/9 integrate the Lagrange basis polynomials. The direct moment approach is often shorter for hand calculation, but the orthogonality proof explains the n-to-2n−1 result used by the lecture. These are complementary derivations, not competing formulas.

The exactness result is not an error estimate for an arbitrary f. In particular, do not infer a universal error expression merely from the phrase “degree 2n−1.” Error formulas require smoothness and a theorem specific to the Gaussian rule. For this course's task, the reliable conclusions are: the rule is exact through degree five for three nodes; it approximates other functions; and accuracy should be assessed with a suitable comparison or error analysis rather than an unsupported digit count.

### Mapping, scaling, and composite use

On [a,b], let c=(a+b)/2 and d=(b−a)/2. The affine map x=c+dt transforms the reference interval and its quadrature rule:

$$
\int_a^b f(x)\,dx=d\int_{-1}^{1}f(c+dt)\,dt\approx d\sum_{i=1}^{n}A_i f(c+dt_i).
$$

For the three-point rule, the physical nodes are c−d√(3/5), c, and c+d√(3/5), with the same weights and a common factor d. The sum of the reference weights is two, so applying the rule to f=1 returns 2d=b−a. This provides a decisive normalization check. If a and b are reversed, d changes sign and the integral orientation is preserved.

A composite Gaussian procedure partitions [a,b] into smaller intervals and applies the mapped rule on each, summing the local estimates. This resolves variation that one three-point panel might miss while preserving the same node/weight table. Each local mapping must use that panel's own midpoint and half-width. Reusing the whole-interval d for every subpanel produces a wrong scale. The result is not identical to a composite trapezoidal rule: each local panel samples three specially placed interior points instead of two endpoints.

### Source assessment: x^6 and the three-point formula

The lesson asks for the three-point Gauss–Legendre evaluation of x^6 on [−1,1]. Let r=√(3/5). The nodes are −r,0,r and the weights are 5/9,8/9,5/9. Since x^6 is even, the two outer function values are equal; since the center value is zero, only the outer contributions remain:

$$
\begin{aligned}
Q_3[x^6]&=\frac59(-r)^6+\frac89(0)^6+\frac59r^6\\
&=\frac{10}{9}\left(\frac35\right)^3=\frac{6}{25}=0.24.
\end{aligned}
$$

The exact value is

$$
\int_{-1}^{1}x^6\,dx=\left[\frac{x^7}{7}\right]_{-1}^{1}=\frac27\approx0.2857142857.
$$

Thus the Gaussian estimate is lower by about 0.0457142857, which rounds to the answer listed in the module. The result is not a contradiction: x^6 is degree six, outside the three-point rule's degree-five exactness. If the same calculation is repeated for x^4, both exact integral and quadrature sum equal 2/5. Contrasting these cases is a direct test of the stated precision.

### A transformed exponential example

To see how a non-polynomial integrand is handled on a general interval, estimate ∫_0^1 e^x dx. Map t∈[−1,1] to x=(1+t)/2. The Jacobian is one half, so the three-point approximation is

$$
Q=\frac12\left[\frac59e^{(1-\sqrt{3/5})/2}+\frac89e^{1/2}+\frac59e^{(1+\sqrt{3/5})/2}\right].
$$

Evaluating the terms gives approximately 1.7182810044. The exact integral is e−1≈1.7182818285, so the absolute difference is about 8.24×10⁻⁷. The function is smooth and the estimate is close, but not exact: the Gaussian precision theorem covers polynomials through degree five, not exponentials. The example also shows the practical cost: three evaluations at nonuniform interior points and one interval scale factor.

### Selecting a quadrature method and stating a conclusion

Use a Gaussian rule when the function can be evaluated at its specified nodes and a high degree of exactness with relatively few evaluations is valuable. Use composite Newton–Cotes formulas when data are already equally spaced or when local panel interpretation is preferred. For rapidly varying or nonsmooth functions, subdividing the interval can be more important than simply increasing a Gaussian order. Selection should account for node availability, smoothness, interval scaling, function-evaluation cost, and the accuracy required.

When answering an exam question, identify the reference formula, map the interval, substitute nodes and weights, include the Jacobian factor, and state what degree of precision applies. If the integrand is a polynomial of degree at most five, say that the result is exact in exact arithmetic. For x^6 or e^x, report an approximation and use an exact value or independent error information if available. Do not claim a formal error bound from node count alone.
'''
examples={}
examples['level_1']=r'''### Worked example: evaluate x^6 with the three-point rule

Use the Gaussian formula on [−1,1] for f(x)=x^6. Its three nodes are −r, 0, r where r=√(3/5); the weights are 5/9, 8/9, 5/9. At the middle node the function value is zero. At either outer node, x^6=(3/5)^3=27/125. Therefore

$$
Q_3=\frac59\left(\frac{27}{125}\right)+\frac89(0)+\frac59\left(\frac{27}{125}\right)=\frac{6}{25}=0.24.
$$

The exact integral is 2/7≈0.285714. The absolute difference is about 0.0457143, so the estimate is not exact. This is expected: x^6 has degree six, while a three-node Gauss–Legendre formula guarantees exactness only through degree five. For comparison, applying the same rule to x^4 gives 2/5 exactly. The pair of examples shows how the degree-of-precision statement guides interpretation.

### Worked example: map the exponential to [−1,1]

Estimate the integral of e^x from 0 to 1. The midpoint and half-width are both 1/2, so the reference point t maps to x=(1+t)/2. The Jacobian contributes a factor 1/2. Substitute the three nodes and weights:

$$
Q=\frac12\left[\frac59e^{(1-\sqrt{3/5})/2}+\frac89e^{1/2}+\frac59e^{(1+\sqrt{3/5})/2}\right]\approx1.7182810.
$$

The exact integral e−1 is approximately 1.7182818. The estimate is close, but not exact because the exponential is not a polynomial of degree at most five. Notice the order of work: transform the nodes, evaluate the function, weight and add the values, then multiply by the half-width. Omitting that last factor would produce about twice the correct integral.
'''
examples['level_2']=r'''### Worked source exercise: Gauss–Legendre approximation of x^6

On [−1,1], the three-point nodes are −r,0,r with r=√(3/5), and the weights are 5/9,8/9,5/9. For x^6, symmetry makes the two outer contributions equal and the central contribution vanishes:

$$
\begin{aligned}
Q_3[x^6]&=\frac59(-r)^6+\frac89(0)^6+\frac59r^6\\
&=\frac{10}{9}\left(\frac35\right)^3=\frac{6}{25}=0.24.
\end{aligned}
$$

The exact value is

$$
\int_{-1}^{1}x^6\,dx=\left[\frac{x^7}{7}\right]_{-1}^{1}=\frac27\approx0.2857142857.
$$

The absolute error is 2/7−6/25=8/175≈0.0457143, the value given for this exercise. This is a deliberate degree-of-precision test. The theorem guarantees exactness through degree five, not six. For x^4, in contrast, both the exact integral and the Gaussian result are 2/5.

### Worked interval transformation: integrate e^x on [0,1]

Let c=d=1/2 and map t∈[−1,1] to x=c+dt=(1+t)/2. Then dx=dt/2, and the transformed three-point formula is

$$
Q=\frac12\left[\frac59e^{(1-\sqrt{3/5})/2}+\frac89e^{1/2}+\frac59e^{(1+\sqrt{3/5})/2}\right].
$$

The evaluations give Q≈1.7182810044. Since the exact integral equals e−1≈1.7182818285, the absolute difference is approximately 8.24×10⁻⁷. The smooth exponential is approximated well by the rule but is not exactly integrated by the degree-five polynomial guarantee. A sound answer reports the method's exactness class and the observed error separately.
'''
examples['level_3']=r'''### Examination exemplar: three-point Gauss–Legendre rule

The rule on [−1,1] has t_1=−√(3/5), t_2=0, t_3=√(3/5), with A_1=A_3=5/9 and A_2=8/9. Apply it to the source exercise f(x)=x^6:

$$
\begin{aligned}
Q_3[f]&=\frac59f(-\sqrt{3/5})+\frac89f(0)+\frac59f(\sqrt{3/5})\\
&=\frac{10}{9}\left(\frac35\right)^3=\frac{6}{25}=0.24.
\end{aligned}
$$

The exact integral is 2/7, hence

$$
E=\int_{-1}^{1}x^6\,dx-Q_3[f]=\frac27-\frac6{25}=\frac8{175}\approx0.0457142857.
$$

This matches the module's listed result. Since degree six exceeds the rule's precision degree five, nonzero error is expected and does not disprove the exactness theorem. As a calibration check, x^4 lies within the guaranteed range and is integrated exactly: the Gaussian sum and integral both equal 2/5.

### General-interval exemplar and accuracy comparison

For ∫_0^1e^x dx, set c=d=1/2 and x=c+dt. The transformed nodes are (1−√(3/5))/2, 1/2, (1+√(3/5))/2. Include the Jacobian d=1/2:

$$
Q=\frac12\left[\frac59e^{(1-\sqrt{3/5})/2}+\frac89e^{1/2}+\frac59e^{(1+\sqrt{3/5})/2}\right]\approx1.7182810044.
$$

The exact value e−1≈1.7182818285, so |E|≈8.24×10⁻⁷. This is an observed error because the exact answer is available. The theorem alone only guarantees exactness for polynomials through degree five; it does not claim that e^x is exact. A solution should distinguish the numerical comparison from the polynomial precision guarantee.

A quick scaling check sets f=1. The reference weights sum to 2, and after multiplying by d=1/2 the rule returns 1, the length of [0,1]. This verifies that the Jacobian is present. If the factor were omitted, the constant integral would be 2, immediately exposing the error.
'''
extras2={}
extras2['level_1']=r'''### What a Gaussian node represents

A node is a location where the function is sampled; a weight tells how strongly that sample contributes to the approximate integral. The three-point rule gives the central value weight 8/9 and each outer value weight 5/9. The total is two, which is exactly the integral of the constant one over [−1,1]. The nodes and weights are not arbitrary: they are chosen together so that polynomial moments match the true integral as far as possible with three evaluations.

This explains why the rule may use fewer function evaluations than a uniform composite rule for smooth functions. It does not mean the Gaussian rule always wins. Its sample points are generally nonuniform and interior, so it requires the ability to evaluate f at those locations. If a data set contains only fixed equally spaced ordinates, the prescribed Gaussian samples may be unavailable. A Newton–Cotes rule may then be more practical even though its degree of precision per point is lower.

### Interpreting accuracy rather than guessing it

A polynomial exactness guarantee is a precise statement: all polynomials up to the stated degree give zero truncation error in exact arithmetic. For functions outside that class, accuracy depends on the function, interval, and node choice. Testing one integrand gives an example, not a universal bound. A value that is close to an exact answer can be described as accurate for that example; it should not be used to claim that all smooth functions have the same number of correct digits.

The three-point rule's error on x^6 illustrates the distinction. Its degree-six error is known exactly in the source exercise, and the exact integral can be computed independently. In a real problem without an exact antiderivative, one might compare against a higher-resolution or composite calculation, but that comparison is evidence, not proof. Report both the approximation and how its accuracy was assessed.
'''
extras2['level_2']=r'''### How many nodes should be used?

The theorem gives a direct relation between node count and polynomial precision: n Gaussian nodes integrate degree at most 2n−1 exactly. This helps estimate how many nodes may be useful when the integrand is well represented by a low-degree polynomial. For the source's three-node rule, the guaranteed degree is five. Increasing n raises the guaranteed polynomial degree, but the theorem does not say that the error for every non-polynomial function decreases monotonically at each increase.

Method selection should begin with the data and the integrand. If f can be evaluated at Gaussian nodes and is smooth, an n-point rule may achieve high accuracy with few evaluations. If values are supplied at equally spaced points, a Newton–Cotes formula uses those observations directly. If f varies sharply in part of the interval, composite application on subintervals can resolve the feature; simply using more global nodes may not be the best choice. Computation cost, node availability, smoothness, and requested precision all matter.

### Numerical error and reproducible reporting

A Gaussian approximation has two kinds of numerical uncertainty. Truncation error comes from replacing the integral by the weighted sample sum. Evaluation and rounding error comes from approximating f(x_i) and forming the weighted sum in finite arithmetic. The polynomial exactness theorem addresses the first type only for a specified class; it does not remove arithmetic error or errors in supplied measurements.

For a known exact integral I, report absolute error |I−Q| and, when I is nonzero, relative error |I−Q|/|I|. If I is unknown, do not invent an exact comparison. Report the quadrature rule, node count, transformed nodes, weights, and an independent comparison or refinement if available. Keep intermediate digits during calculation and round the final number to a precision consistent with inputs.

### Exactness checks by moments

The three-point moment equations provide an efficient verification checklist. The weights must satisfy A_1+A_2+A_3=2; symmetry gives A_1=A_3; the second moment must equal 2/3; and the fourth moment must equal 2/5. These conditions yield the familiar nodes and weights. Odd moments vanish because the interval and rule are symmetric. A table copied from a reference can therefore be checked without evaluating a complicated test function.

If the weights sum to something other than two, the constant integral fails. If the second moment fails, a scaling or node error has occurred. If the x^4 moment fails, the rule does not have the stated degree-five precision. Testing moments isolates the source of a mistake more effectively than checking only one unrelated integral.
'''
extras2['level_3']=r'''### Evaluating the Gaussian rule against Newton–Cotes methods

Newton–Cotes rules use equally spaced nodes; the Gaussian construction chooses nodes as roots of an orthogonal polynomial. The composite trapezoidal rule and Simpson's rule are convenient on uniform tables and can be repeated over subintervals. Gauss–Legendre quadrature achieves degree 2n−1 with n optimally selected nodes on the reference interval. These are complementary design choices, not a claim that one method is universally preferable.

A Gauss–Legendre rule is attractive when f can be evaluated at the nonuniform nodes, the integrand is reasonably smooth, and function evaluations are costly. A composite equally spaced rule is often natural when data are already tabulated at regular locations. For localized rapid variation, subdividing the interval can improve resolution. For a singularity or discontinuity, the method and interval partition must account for it; the nominal polynomial exactness of a global rule does not cure nonsmoothness.

When assessing a result, distinguish quadrature truncation from function-evaluation uncertainty. If each sampled ordinate has an error, the weighted sum inherits a combination of those errors. High-order exactness cannot recover information missing from noisy or rounded inputs. Likewise, a theorem about exact polynomials does not certify the error of an arbitrary analytic function without an appropriate remainder theorem. The safest report gives the rule and nodes, shows the transformed sum, and states the basis of any accuracy claim.

### Constructing the weights and checking implementation

For fixed nodes, an interpolatory quadrature rule integrates the Lagrange basis polynomials to obtain its weights. In the Gaussian construction, the nodes themselves are selected from the orthogonal polynomial, increasing the exactness beyond the degree of the interpolating polynomial. For the three-point Legendre case, symmetry reduces the unknowns to r, A, and B. Matching the zeroth, second, and fourth moments gives r²=3/5, A=5/9, and B=8/9. This derivation is compact enough to reproduce in an examination answer and transparent enough to catch transcription errors.

A numerical implementation should keep the reference nodes and weights in one table, map the nodes using c and d for each interval, evaluate f at each mapped point, then multiply the weighted sum by d. Check that the mapped nodes lie within the interval, the weights sum to two before scaling, and the constant function integrates to b−a after scaling. Reversing a and b should reverse the sign. These checks cover node mapping, Jacobian, and orientation.

### Reporting exactness and error carefully

When f is a polynomial of degree at most five, the three-node rule's exactness theorem supplies a strong conclusion: in exact arithmetic, Q equals the integral. For x^6, it does not. The lesson's x^6 calculation gives Q=6/25 while the exact integral is 2/7, yielding 8/175 absolute error. This explicit counterexample is an effective guard against extending the degree-five guarantee by one degree.

For a non-polynomial function such as e^x, the rule can be highly accurate without being exact. On [0,1], the computed value approximately 1.7182810044 differs from e−1 by about 8.24×10⁻⁷. This observed error can be reported because the exact integral is available. Without that reference, compare another rule or refine the interval and label the result as an estimate; do not state a guaranteed tolerance merely because the rule has three Gaussian nodes.
'''

addendum={}
addendum['level_1']=r'''### A practical checklist for a first Gaussian calculation

The three-node formula is easiest to use when the calculation is separated into four jobs. First identify the interval and the reference rule. Second map the nodes from [−1,1] to the interval. Third evaluate the integrand at those mapped nodes and form the weighted sum. Fourth multiply by the half-width. Writing these stages separately keeps the geometric transformation visible instead of hiding it inside a long substitution.

On an interval [a,b], let c=(a+b)/2 and d=(b−a)/2. The reference nodes −r,0,r become c−dr,c,c+dr. The value of the integral is d times the reference weighted sum. Before using a decimal calculator, preserve r=√(3/5) and the weights as exact fractions. Only after the function values are obtained should the terms be combined and rounded. This approach makes a wrong node, an omitted factor, or premature rounding much easier to locate.

A useful unit check follows from integrating f(x)=1. The reference formula gives

$$
\frac59+\frac89+\frac59=2,
$$

and scaling by d gives 2d=b−a. Thus the formula returns the interval length, as any quadrature formula for the constant should. The check is short enough to include in a solution and catches a common mistake: applying a reference-interval formula directly to a different interval without the Jacobian.

Symmetry offers another check. For an odd function on [−1,1], the exact integral is zero. Symmetric nodes and equal outer weights cancel the two outer terms, and the center term is zero for an odd function. For an even function, the two outer function values agree, so the sum can be simplified by doubling one outer contribution. These observations are not shortcuts that replace the rule; they are ways to verify that its symmetry has been used consistently.

### Reading a tabulated rule correctly

A Gauss–Legendre table gives nodes and weights for the reference interval with weight function one. The entries are paired: each weight belongs to the node in the same position. Sorting nodes from left to right is harmless only if the corresponding weights are kept with them. In the three-node case the symmetry makes the two outer weights equal, but that visual symmetry should not lead to an assumption that all weights are equal.

The number of nodes is not the same as the number of subintervals. A single three-node application uses three function values over one panel. A composite calculation divides the original interval into several panels and repeats the three-node rule on each panel, using a distinct midpoint and half-width for each. If there are m panels, the computation uses 3m evaluations unless points happen to coincide and are reused. The local estimates are added; the weights from separate panels are not pooled before their own scale factors have been applied.

This distinction also clarifies when the method is practical. If a function is available as a callable expression, evaluations at the Gaussian points can usually be made. If only observations at an equally spaced grid are supplied, those three interior points might not appear in the table. Interpolating a table to create new ordinates introduces a separate approximation and should be stated. A composite trapezoidal or Simpson rule may be the honest choice when the problem explicitly provides uniform data.

### Precision is not a promise about every function

The three-node rule exactly integrates any polynomial through degree five. That statement follows from the construction and is independent of the particular coefficients of the polynomial. It does not say that the rule gives six correct digits for every function, nor that an arbitrary smooth function has a known error from the degree alone. A student should use the precision theorem to decide whether exactness is guaranteed for a polynomial, not to guess the rounded accuracy of other integrands.

The source exercise with x^6 is a useful boundary test. The result 6/25 is not 2/7 because degree six lies just outside the guaranteed range. By contrast, x^4 is inside the range and is integrated exactly. The example is stronger than merely repeating the theorem: it makes clear that “one degree higher” can already produce a nonzero error.

For e^x on [0,1], the three-point result is close to e−1, but closeness is a property of that example and interval. The exact integral allows an observed error to be calculated. If an antiderivative is unavailable, an analyst can compare composite estimates or use a more detailed error theorem when its hypotheses are known. A comparison is a diagnostic rather than an automatic proof. In a written solution, make the distinction explicit: state exactness when the polynomial hypothesis applies; otherwise call the numerical result an approximation.

### Arithmetic discipline and final interpretation

The node √(3/5) is approximately 0.7745966692. On [0,1], the mapped nodes are approximately 0.1127016654, 0.5, and 0.8872983346. These values show that Gaussian sampling is not the same as evaluating at the endpoints and midpoint. Entering 0, 0.5, and 1 into the function would instead correspond to a different rule.

Keep the function values and weighted terms distinguishable in a calculation. The outer node values need not be equal unless the transformed integrand is symmetric about the interval midpoint. When they are not equal, each must be multiplied by its own weight before addition. After applying d, round the final estimate to a sensible number of places; reporting many digits from rounded exponentials would suggest unjustified precision.

A concise conclusion should name the interval, node count, result, and status of the result. For example, “The three-point Gauss–Legendre estimate on [0,1] is approximately 1.7182810; comparison with e−1 gives an observed absolute error of about 8.24×10⁻⁷.” This says what was computed and what evidence supports the accuracy claim. It does not elevate an observed comparison into a universal guarantee.

### A two-panel mapping exercise

Consider applying the three-point rule to [0,2] using two equal panels, [0,1] and [1,2]. Each panel has half-width 1/2, but the midpoints are different: 1/2 for the first and 3/2 for the second. The first panel's nodes are approximately 0.1127, 0.5, and 0.8873; the second panel's are approximately 1.1127, 1.5, and 1.8873. The global interval's endpoints, 0 and 2, are not sampled. Each local weighted sum is multiplied by 1/2, and the two results are added.

This layout helps students distinguish panel subdivision from increasing the node count of a single rule. A two-panel composite three-point calculation uses six evaluations, with three located inside each panel. It is not the six-point Gaussian rule on the full interval: the node locations, weights, and exactness argument differ. The composite construction retains the same local three-point exactness on each panel, while the global six-point Gaussian construction would have a different reference table and degree guarantee.

For a constant function, each panel estimate is 1, since its width is one. Their sum is 2, matching the total interval length. For any polynomial of degree at most five, each local panel is integrated exactly after the affine change of variable, so the sum of panel integrals is also exact. This follows panel by panel and does not require the polynomial to be centered around either midpoint.

### Deciding whether subdivision is useful

Subdivision is a way to control where information is gathered. If the function bends more strongly in one region than another, separate panels place local nodes around that behavior. A uniform partition is simple, while a nonuniform partition can allocate more panels to a region of rapid variation if the problem and accuracy strategy allow it. In either case, the total integral is the sum of panel estimates, and every panel must use its own mapping.

Subdivision increases the number of function evaluations. One should not subdivide mechanically without considering the cost or whether the integrand is already well represented over the full interval. A comparison between a one-panel and a two-panel estimate can be useful evidence of stability, but without an error theorem it remains a diagnostic. Agreement may happen accidentally, and a feature missed by both approximations may still be present.

If there is a known discontinuity, split the interval at that point rather than asking one smooth approximation to cross it. If the function has a narrow peak, choose panel boundaries so that the peak lies within a panel and then check that the node locations resolve it. The basic Gaussian formula does not remove the need to understand the function's behavior; it organizes the weighted sampling once the interval has been chosen.

### Explaining the formula in words

For a clear written explanation, state that Gaussian quadrature chooses sample locations and weights jointly so that polynomial moments match the integral to high degree. In the three-node Legendre rule, the nodes are symmetric, the outer nodes lie at ±√(3/5), and the center is zero. The central weight is 8/9 and each outer weight is 5/9. On an arbitrary finite interval, the affine map moves the nodes and the half-width scales the sum.

Then distinguish the rule's guaranteed property from the numerical outcome. The degree-five exactness means that a polynomial integrand of degree at most five is integrated exactly in exact arithmetic. For another integrand, the weighted sum is an approximation whose quality depends on its behavior and the interval. This two-part explanation is more informative than simply presenting a decimal answer or calling Gaussian quadrature “very accurate.”

Finally, connect the result to the task. If the problem asks for an approximation, give the weighted sum and a sensible rounded value. If it asks why an answer is not exact, identify whether the integrand exceeds degree five or is not a polynomial in that class. If it asks for method choice, mention node availability and function smoothness as well as the formal precision. These habits produce answers that show both the calculation and its meaning.
'''

addendum['level_2']=r'''### Interpreting polynomial exactness with a basis argument

The degree-five conclusion can be verified without testing every possible polynomial separately. Every polynomial p of degree at most five has a unique representation

$$
p(x)=c_0+c_1x+c_2x^2+c_3x^3+c_4x^4+c_5x^5.
$$

Integration and the quadrature sum are linear operations. It is therefore sufficient to check that they agree on the six monomials 1,x,x²,x³,x⁴,x⁵. The three-point Legendre rule matches the even moments 1,x²,x⁴ through its moment equations; symmetry makes both the integral and rule vanish for x,x³,x⁵. Agreement on a basis proves agreement for every linear combination, hence for every polynomial in the degree range.

This reasoning also explains why an example with a single polynomial is not a proof of degree of precision. Checking x^4 confirms one moment. It does not establish exactness for every polynomial up to that degree unless the remaining basis elements have also been considered or a general theorem has been invoked. The orthogonality proof supplies that theorem for n nodes and degree at most 2n−1.

The three-point rule provides a vivid counterexample outside the range. For x^6, the quadrature value is 6/25 whereas the exact integral is 2/7. Thus degree five is the highest guaranteed degree; exactness on a particular higher-degree polynomial could occur accidentally, but cannot be asserted for all degree-six polynomials. Precision is a universal guarantee within a vector space, not a claim that every function outside it must fail.

### Relation between interpolatory and Gaussian construction

Given n distinct nodes, one can form the degree-(n−1) Lagrange interpolating polynomial through the sampled values and integrate that polynomial. The resulting interpolatory rule has weights obtained by integrating the Lagrange basis. Because interpolation reproduces all polynomials through degree n−1, the rule is exact at least through that degree. If the nodes are arbitrary, one should not expect the degree to double.

Gaussian quadrature changes the nodes as well as the weights. Choosing them as the zeros of an appropriate orthogonal polynomial makes the rule exact to degree 2n−1. The polynomial-division proof shows exactly where this improvement enters: the part divisible by q_n has zero integral by orthogonality and zero quadrature contribution because q_n vanishes at every node. The remaining polynomial has degree below n and is already handled by interpolation. The extra exactness is therefore a consequence of a coordinated node-and-weight construction.

For n=3 and Legendre weight one, P_3(x)=(5x³−3x)/2. Its roots are 0 and ±√(3/5). The root polynomial is orthogonal to lower-degree polynomials, and its roots lead to the same nodes obtained by the symmetric moment equations. The orthogonal-polynomial route generalizes; the symmetric equations are an efficient concrete derivation for this low-order case.

### Change of variable as a linear functional

The affine map is more than a device for moving points. It transforms both the limits and the differential. With x=c+dt, the endpoints t=−1 and t=1 map to a and b, while dx=d dt. Thus

$$
\int_a^b f(x)\,dx=d\int_{-1}^{1}f(c+dt)\,dt.
$$

Applying the reference rule to the transformed integrand produces the mapped nodes and the shared factor d. The same derivation works for any panel, which is why the composite method can reuse a single table. Omitting d changes the units and scales the constant integral incorrectly; using b−a instead of d doubles the result.

In a partition a=x_0<x_1<\cdots<x_m=b, panel j has midpoint c_j=(x_{j-1}+x_j)/2 and half-width d_j=(x_j−x_{j-1})/2. Its three mapped points are c_j−d_jr,c_j,c_j+d_jr. The composite estimate is the sum over panels of d_j times each panel's weighted values. Writing the panel index prevents accidental reuse of the global midpoint or width.

If every panel is a uniform width h, then d_j=h/2 for all j. This may simplify the outer scale, but the evaluation points are still Gaussian interior points within each panel, not the uniform grid endpoints. The total computation cost and sample pattern should be described accordingly. A function's values at panel boundaries are not required by the three-point Gauss rule unless they coincide with one of its interior nodes, which generally they do not.

### Building a defensible accuracy statement

There are three distinct statements that are often confused. “The rule is exact for degree at most five” is a theorem about polynomials in exact arithmetic. “This computed value differs from a known integral by a certain amount” is an error measurement for one problem. “The error is guaranteed below a tolerance” requires a valid error bound and verified hypotheses. The first statement alone does not imply the third.

For the exponential example, the antiderivative gives an exact reference, so the absolute error can be computed as |(e−1)−Q|. A relative error may also be reported because the integral is nonzero. When no exact reference exists, repeating the calculation on smaller panels or comparing different orders can reveal sensitivity. However, agreement between two approximations is not a formal guarantee unless a convergence or error theorem is used.

Function evaluation may itself be rounded or noisy. If the sampled ordinates have errors, the quadrature sum reflects weighted versions of those errors. Increasing the formal polynomial precision cannot undo inaccurate input values. This is especially important when measurements rather than analytic function evaluations are used. State whether the values are exact, rounded, or measured if that information affects interpretation.

### Selecting between global and composite application

A global Gaussian rule puts all its nodes across the full interval. It is efficient for sufficiently smooth integrands whose values can be evaluated at those locations. Composite application localizes the approximation by dividing the interval; this is useful when behavior varies across the domain, because each subinterval receives its own midpoint and nodes. Subdivision also increases evaluation cost, so it should be guided by the desired accuracy and observed behavior rather than applied blindly.

Newton–Cotes methods retain an important practical advantage: their equally spaced nodes fit common tables and can be repeated over a uniform partition. Gaussian quadrature offers more polynomial precision per node but demands nonuniform evaluations. The right comparison therefore includes data access, smoothness, computational cost, and the required result quality. No universal ranking follows from degree of precision alone.
'''

addendum['level_3']=r'''### Why the division proof is the decisive argument

An interpolatory rule with n nodes is immediately exact through degree n−1, because those polynomials are reproduced by interpolation. The surprising Gaussian result is exactness through degree 2n−1. To justify the stronger statement, one must use a property not shared by arbitrary interpolation nodes: their defining polynomial q_n is orthogonal to every polynomial of lower degree.

Polynomial division gives p=q_ns+r. The degree bound on p ensures deg s≤n−1 and deg r≤n−1. Orthogonality eliminates the integral of the first term. At the nodes, q_n is zero, so that same term contributes nothing to the weighted sum. The remaining r is integrated exactly by the interpolatory rule. This argument proves agreement of the integral and quadrature for the entire class, not merely for a list of examples.

Each premise has a role. Orthogonality concerns the continuous integral with its weight. The roots make the discrete contribution vanish. The remainder degree ensures the lower-degree exactness of the interpolatory rule applies. Omitting any of these links leaves a gap. In particular, saying only that the nodes are roots does not prove exactness unless the orthogonality and remainder arguments are also supplied.

For the Legendre three-node case, the weight function is one and q_3 can be taken as P_3=(5x³−3x)/2. Its three roots lie within the reference interval. The resulting weights integrate the Lagrange basis and are 5/9,8/9,5/9. This construction therefore has degree of precision five. The moment approach confirms the same result directly, while the division proof explains its general origin.

### A detailed error reading of the source polynomial example

The source's x^6 exercise deliberately uses a polynomial just beyond the exactness range. At the two nonzero nodes r=√(3/5), the sixth power is r^6=(3/5)^3=27/125; at zero it is zero. The outer terms combine to

$$
Q_3=\frac{10}{9}\frac{27}{125}=\frac{6}{25}.
$$

The antiderivative gives ∫_{−1}^{1}x^6 dx=2/7. Subtracting the quadrature value from the exact value gives

$$
\frac27-\frac6{25}=\frac{50-42}{175}=\frac8{175}\approx0.0457143.
$$

This difference is positive, so the rule underestimates this even integrand on this interval. That observed sign is specific to x^6; it is not a general rule that Gaussian quadrature underestimates positive functions. The example establishes a boundary of the degree guarantee, not a universal direction for error.

For x^4, the same nodes produce the exact moment 2/5. For odd monomials up to degree five, symmetry yields zero exactly. Together these checks make a complete basis verification. The x^6 discrepancy then illustrates what can happen immediately outside that space. A careful solution distinguishes “the rule has degree five” from “this particular result happens to be close.”

### Interval maps, panel maps, and orientation

For a general interval, c=(a+b)/2 and d=(b−a)/2. The transformed integrand is f(c+dt), and the scale is d. In a composite rule, the same formula is applied independently to each panel. Replacing d with the interval length is a factor-of-two error; mapping t using c but forgetting to transform dx is another. These mistakes can be caught by applying the procedure to the constant integrand, whose exact integral is b−a.

Orientation is also encoded in d. If the limits are reversed, then d<0 and the change of variables yields a negative integral, as required by the definition ∫_b^a f=−∫_a^b f. A procedure that takes an absolute half-width without separately restoring orientation loses that sign. Most exercises use a<b, but a general derivation should retain the signed half-width.

For a partition, each panel contributes d_j times a reference weighted sum. This is not equivalent to applying one global formula and then dividing its answer among panels. Local mapping changes the evaluation points and scales for every subinterval. Writing the local formula before summing makes the composite structure explicit and allows panel-level refinement where the integrand varies most.

### Comparison with equally spaced quadrature

The trapezoidal and Simpson formulas use equally spaced ordinates, and their composite versions are convenient when a regular table is given. Gaussian formulas instead optimize node locations for polynomial precision. With n Gaussian evaluations, degree 2n−1 is integrated exactly; this high precision can be valuable when function evaluation is expensive and the nodes are available.

That comparison concerns exactness on polynomials, not total practical accuracy in all settings. A table containing only equally spaced data cannot supply Gaussian values at arbitrary interior points without additional approximation. If the integrand has sharp local variation, a composite method may represent that variation more transparently than a single global panel. If there is a discontinuity or singularity, the interval should be treated in a way that respects it; smooth-function intuition should not be carried over without checking assumptions.

The method choice should be justified from the actual information available. Ask whether function evaluation is permitted, whether data are tabulated, whether the function is smooth over the entire interval, and how much accuracy is needed. The Gaussian formula is a powerful option, not an instruction to disregard these constraints.

### Numerical reporting and reproducibility

A reproducible numerical answer identifies the interval, the specific node-weight rule, the transformed nodes, and the scale factor. It should show enough intermediate work to verify the weighted sum. For the exponential example, preserve the three transformed abscissae and evaluate each exponential there; combine the center and outer contributions with their distinct weights, then multiply by one half. This transparent sequence makes the approximation independently checkable.

Report a useful number of digits rather than every digit produced by a calculator. If an exact reference is available, give an absolute error and, where useful, a relative error. If it is unavailable, state that the answer is an approximation and describe any comparison or refinement used. A rounded decimal is not itself an error guarantee.

Finally, separate mathematical truncation from arithmetic effects. Exactness for a polynomial says that the ideal weighted sum equals its integral. In floating-point computation, node representations, function values, multiplication, addition, and final rounding can introduce small discrepancies. Those effects do not invalidate the theorem, but they explain why a computed exact-polynomial test may differ in its last digits. A robust check compares within an appropriate numerical tolerance and retains exact fractions as long as practical.
'''
