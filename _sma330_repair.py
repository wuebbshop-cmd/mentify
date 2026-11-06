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
def repair_topic(tid,expected,supplements,examples=None):
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
extras={}
extras['level_1']=r'''### Reading the triangular table

The Romberg array is triangular because a correction needs two estimates that already exist. Its left edge contains ordinary composite trapezoidal values. Moving down that edge halves the panel width and doubles the number of trapezia. Moving one column to the right does something different: it combines two adjacent approximations to remove a leading error term. It does not introduce a new set of function values. Keeping those roles separate helps make sense of the table: rows record refinement of the mesh, while columns record extrapolation.

For one composite trapezoidal estimate, each panel contributes its width times the average of its two endpoint heights. When neighboring panels are added, an interior height belongs to two panels, so it is counted twice; the two boundary heights occur only once. This explains the familiar endpoint-once, interior-twice formula. If the panel width is h and there are n panels, check that nh equals b−a before evaluating the weighted sum. The resulting area has units of a function value times a horizontal interval, which is a useful dimensional check.

A curve can bend above or below a straight chord. The trapezoidal bias therefore depends on curvature. It is not safe to memorize that this rule always overestimates or always underestimates: that direction follows only under additional shape conditions. For a smooth function, however, halving h changes the leading global error in a predictable way. Romberg uses this predictable scaling to improve a result without fitting a new polynomial to the function.

### Why the first correction uses three

Suppose a coarse approximation has a leading error proportional to h squared. Halving the panel width changes that error by a factor of one quarter. If the coarse error is E, the fine error is approximately E/4. The difference between the fine and coarse estimates is then approximately −3E/4, so adding one third of that signed difference to the fine estimate cancels the leading bias. That is the reason for the factor one third; it is not a convenient average chosen by trial and error.

The first Romberg correction can be written with a named coarse value and fine value so that the sign remains visible:

$$
R_{1,1}=T_2+\frac{T_2-T_1}{3}.
$$

Here T_2 uses the finer of the two grids. If the fine estimate is smaller, the correction is negative; if it is larger, the correction is positive. Taking an absolute difference before using the formula destroys this information and can send the estimate in the wrong direction.

After the h-squared term is canceled, the next leading error behaves like h to the fourth power. Halving h now scales that term by one sixteenth. The next denominator is therefore fifteen, the difference between sixteen and one. Later denominators follow the same pattern: the j-th correction uses 4 to the power j minus one. The table makes the cancellation visible but does not remove the need to track which entry is coarse and which is fine.

### Source-sized calculation for the logarithm

The lesson's sample integral is the area under 1/x from 1 to 2. Its exact value is ln 2, which can be used after the numerical calculation as a check. On the first grid the width is one and the endpoint heights are one and one half. Their average gives the first trapezoid:

$$
T_1=\frac{1}{2}\left(1+\frac12\right)=0.7500000.
$$

The two-panel grid adds the midpoint 3/2, where the height is 2/3. Its two panels give

$$
T_2=\frac{1/2}{2}\left[1+2\left(\frac23\right)+\frac12\right]=0.7083333.
$$

Continuing the same composite formula gives T_4 approximately 0.6970238, T_8 approximately 0.6941219, and T_16 approximately 0.6933912. These are all raw trapezoidal estimates. They approach ln 2 gradually, showing that merely increasing the number of panels can be less efficient than correcting the leading error.

For the first extrapolation, pair T_1 with T_2. The signed difference is negative, so the correction moves downward:

$$
R_{1,1}=0.7083333+\frac{0.7083333-0.7500000}{3}\approx0.6944444.
$$

The next pair gives

$$
R_{2,1}=0.6970238+\frac{0.6970238-0.7083333}{3}\approx0.6932539.
$$

The next columns use denominators fifteen, sixty-three, and so forth. Completing the table with the nested grids yields a diagonal close to 0.69314718, agreeing with ln 2 to the digits supported by this example. Each step is a repeatable application of the same recurrence, not a fresh quadrature rule.

### Choosing a stopping point and reporting digits

The diagonal of the Romberg table is a useful place to watch for stabilization. A practical calculation can stop when the change between consecutive diagonal values is below a chosen tolerance. But that difference is an indicator, not automatically a guaranteed error bound. Rounded function values may limit the accuracy, and a curve with a jump, corner, or sharp feature may not follow the smooth error pattern that Romberg expects.

A sound report states the panel counts, the final diagonal entry, and how the previous diagonal compares with it. If the exact integral is known, calculate the actual absolute difference. If it is not known, say that the diagonal values have stabilized to the observed precision; do not claim exact digits from a table alone. Avoid printing more decimal places than the data or error analysis justify. One extra column does not restore information lost through rounded ordinates.

Three quick checks prevent many mistakes. The panel counts double at every row; the sum of panel widths remains b−a; and each extrapolated cell uses the adjacent entries specified by the recurrence. If the table behaves oddly, check its labels and arithmetic before assuming the function is unsuitable. If the arithmetic is correct but the values oscillate, inspect smoothness and the quality of the input data instead of blindly extending the triangle.
'''
extras['level_2']=r'''### Error expansion and the logic of Richardson extrapolation

The composite trapezoidal rule can be derived panel by panel. On [x_i,x_{i+1}], replace f by its linear interpolant through the two endpoint values and integrate that line. The local area is h(f_i+f_{i+1})/2. Summation over all panels counts each interior ordinate twice and each endpoint once. This derivation explains the weights and makes clear that the compact formula assumes a uniform h. On a nonuniform partition, each panel must retain its own width; one cannot use a single common h without changing the rule.

For a sufficiently smooth integrand over a fixed interval, the global trapezoidal error has an expansion in even powers of h. The leading term is proportional to h squared, followed by terms proportional to h to the fourth power, h to the sixth power, and so on. If T(h)=I+c_2h^2+c_4h^4+…, then T(h/2)=I+c_2h^2/4+c_4h^4/16+…. Subtracting these expressions and forming a suitable linear combination removes c_2h^2. The first Romberg value is therefore more accurate in the asymptotic regime than either of its trapezoidal inputs.

Once the leading term has been removed, the next error term scales by one sixteenth when h is halved. A second extrapolation eliminates that term. Repeating the operation produces the triangular Romberg table. If R_{k,0}=T_{2^k}, where the subscript denotes the number of panels, the recurrence is

$$
\begin{aligned}
R_{k,j}&=R_{k,j-1}+\frac{R_{k,j-1}-R_{k-1,j-1}}{4^j-1},\\
k&\geq j,\qquad j=1,2,\ldots .
\end{aligned}
$$

The denominator belongs to the extrapolation column, not to the total row count. The first column uses three; the second uses fifteen; the third uses sixty-three. Some books use reversed superscript and subscript conventions, so an answer should define its notation before populating the array. This prevents a plausible-looking but misindexed table.

The formal gain in order is conditional. The smooth even-power expansion is useful when f has enough derivatives and the mesh sizes are in a regime where asymptotic behavior has begun. A discontinuity, singular endpoint, sharp boundary layer, noisy measurement, or heavily rounded table can make early rows misleading. A high-order label does not guarantee high accuracy for arbitrary inputs. In a rigorous analysis, state the smoothness assumptions and separate the extrapolation's truncation-error cancellation from errors already present in the function values.

### Recursive evaluation on nested meshes

The nested-grid property avoids recomputing every ordinate. Suppose T_n is based on n panels of width h_n=(b−a)/n. The refined grid has 2n panels of width h_n/2; it consists of all old nodes and n new midpoints. The sum of the old-node contributions is one half of T_n, while each new midpoint contributes h_n/2 times its function value. Thus

$$
T_{2n}=\frac12T_n+\frac{h_n}{2}\sum_{i=0}^{n-1}f\!\left(a+\left(i+\frac12\right)h_n\right).
$$

Equivalently, if h_{2n}=h_n/2, the coefficient on the midpoint sum is h_{2n}. Both forms are the same identity. The equation is an efficient way to build the left edge of the Romberg table; it is not a new integration method. Check that the midpoint sum has n terms, that the old endpoint values are retained, and that no newly inserted node is counted twice.

For hand computation, the direct composite formula is often clearer on the first few rows. For a program or a long table, recursive refinement saves evaluations. A robust calculation can compute the first row directly, then use the recurrence, while independently checking one refined row by direct summation. The mesh label should include n or h, since “row 3” alone says nothing about whether the estimate uses four or eight panels.

### Source assessment: estimating pi

The lesson's assessment estimates pi from 4/(1+x²) on [0,1]. Four doublings after the initial one-panel estimate use panel counts 1, 2, 4, 8, 16. The composite trapezoidal values are approximately

$$
\begin{aligned}
T_1&=3.0000000000, &T_2&=3.1000000000,\\
T_4&=3.1311764706, &T_8&=3.1389884945,\\
T_{16}&=3.1409416120.
\end{aligned}
$$

The first correction is

$$
R_{1,1}=T_2+\frac{T_2-T_1}{3}=3.1000000000+\frac{0.1000000000}{3}=3.1333333333.
$$

Continuing the first extrapolation column gives 3.1415686275, 3.1415925025, and 3.1415926512. Using denominator fifteen for the next column gives 3.1421176471, 3.1415940941, and 3.1415926611. The next denominator is sixty-three, and the final one is 255. The fourth extrapolation produces approximately 3.1415926653, which rounds to 3.1415927 and agrees with the module's answer. The exact value of pi is 3.1415926536…; the discrepancy in this known example is about 1.2×10⁻⁸.

This table is also a sign check. The first fine trapezoid exceeds the coarse one, so the first correction is positive. Reversing the difference while retaining the plus sign would give a value below 3.1 and contradict the computed change. Later entries need not move monotonically because the extrapolations remove successive error terms whose coefficients can have different signs. Use the recurrence rather than assuming a direction.

### Interpreting error and selecting a method

If an exact integral I is available, the actual absolute error of a computed estimate Q is |I−Q| and the relative error is |I−Q|/|I| when I is nonzero. These definitions describe the observed error; they do not supply a bound unless I is known. When the exact answer is unavailable, the difference between adjacent diagonal values is a practical convergence indicator. It can be a sensible stopping rule when combined with a maximum iteration count and a check for stable behavior, but it is not a theorem guaranteeing that the true error is no larger than that difference.

Composite trapezoidal integration is a transparent choice when the function is tabulated on equally spaced nodes, a low-cost baseline is needed, or nested refinement is convenient. Romberg is more attractive when repeated evaluations are possible and f is smooth enough for the error expansion to be informative. For a nonsmooth or noisy integrand, the extrapolation can amplify uncertainty or mistake a pre-asymptotic sequence for convergence. A practical decision therefore considers smoothness, available nodes, function-evaluation cost, and input precision—not simply which formula has the highest formal order.

In a written solution, separate evidence from assurance. Give panel counts and step sizes; show the trapezoidal sequence; state the recurrence and its denominators; identify the final diagonal value; and describe how the diagonal changes. If the task requests an accuracy comment, report an exact comparison when available. Otherwise, state that the computed entries stabilize and explicitly call the diagonal difference an indicator. This makes the conclusion reproducible without claiming more than the numerical evidence supports.
'''
extras['level_3']=r'''### Derivation of the extrapolation factor and its order

The composite trapezoidal rule is the integral of the piecewise-linear interpolant. This construction explains both the endpoint weights and the leading error term. If f is sufficiently smooth on [a,b], the global error can be expanded as c_2h^2+c_4h^4+c_6h^6+…, where the coefficients depend on endpoint derivatives. Romberg integration exploits the powers of two in this expansion, not a special property of one sample integrand.

Let T(h)=I+c_2h^2+c_4h^4+…. On the mesh h/2, the leading term becomes c_2h^2/4. The combination T(h/2)+(T(h/2)−T(h))/3 has coefficient c_2h^2/4+(c_2h^2/4−c_2h^2)/3=0. Thus the h² term cancels, leaving an error of order h⁴ under the expansion assumptions. After that cancellation, the next pair of estimates has a leading h⁴ term whose scale changes by 1/16, so the next denominator is 15. In general, the j-th column removes the h^{2j} contribution and uses 4^j−1.

This explains why the Romberg table is triangular. Let R_{k,0}=T_{2^k}, and define

$$
R_{k,j}=R_{k,j-1}+\frac{R_{k,j-1}-R_{k-1,j-1}}{4^j-1},\qquad k\ge j.
$$

The first column is the trapezoidal sequence; each later column cancels one additional term. The diagonal has progressively higher formal order as long as the assumed expansion remains valid. This order is not a guarantee for every data set: a nonsmooth integrand, endpoint singularity, coarse pre-asymptotic mesh, or rounded measurements can dominate before the predicted cancellation appears. A careful report distinguishes formal order from observed accuracy.

### Recursive trapezoidal refinement

The cost of constructing a Romberg table can be reduced by reusing the nested grid. For n panels, let h_n=(b−a)/n and let T_n denote the composite trapezoidal estimate. The refined grid has 2n panels; the old nodes are still present, and each former panel contributes one new midpoint. The endpoint and old-node terms together equal half the preceding estimate, while the midpoint terms carry coefficient h_n/2:

$$
T_{2n}=\frac12T_n+\frac{h_n}{2}\sum_{i=0}^{n-1}f\!\left(a+\left(i+\frac12\right)h_n\right).
$$

This identity can be checked by expanding both sides as weighted sums. Each old interior node has fine-grid coefficient h_n/2, which is half its old coefficient h_n; the two endpoints likewise have coefficient h_n/4 after refinement. Every inserted midpoint has coefficient h_n/2. If the fine spacing h_{2n}=h_n/2 is used, the midpoint coefficient is simply h_{2n}. This alternate notation is useful but easy to mishandle: multiplying the midpoint sum by h_{2n}/2 would halve it twice.

For an implementation, store T_n, evaluate only the n new midpoints, and calculate T_{2n}. Then append the new first-column value and compute the newly available extrapolated cells. Validate the indexing by checking that the second column begins only at the two-panel row, the third only at the four-panel row, and so forth. A robust numerical implementation should also guard against excessive refinement once floating-point rounding makes successive corrections smaller than the arithmetic noise.

### Four-doubling assessment for pi

For the source assessment, f(x)=4/(1+x²) and I=∫_0^1 f(x)dx=π. Four mesh doublings after the initial one-panel estimate use n=1,2,4,8,16. The composite trapezoidal values are T_1=3.0000000000, T_2=3.1000000000, T_4=3.1311764706, T_8=3.1389884945, and T_16=3.1409416120. The first extrapolations use the denominator three and are 3.1333333333, 3.1415686275, 3.1415925025, and 3.1415926512. The second column uses denominator fifteen, giving 3.1421176471, 3.1415940941, and 3.1415926611. The third uses sixty-three, and the last uses 255; the final diagonal is approximately 3.1415926653.

The exact value 3.141592653589… differs by approximately 1.17×10⁻⁸, and the numerical estimate rounds to 3.1415927 as in the module's answer key. The first correction sign is positive because T_2−T_1=0.1. The later diagonal entries are close but not strictly monotone, so monotonic improvement should not be assumed. The calculation illustrates why table structure, labels, and signed differences matter as much as the final decimal.

### How to assess reliability without an exact answer

For an unknown integral, calculate the change between successive diagonal entries and compare it with the requested tolerance. This gives an a posteriori indicator of stabilization. It is not automatically a bound: two successive estimates can be close while sharing an unresolved bias, and a rounded input table may make the apparent correction artificially small. The smooth error expansion supplies a rationale only when its hypotheses are credible. State the indicator accurately and avoid calling it a guaranteed error estimate unless a separate bound has been proved.

If the exact value is known, the actual absolute error is |I−R_{k,k}| and the relative error is that quantity divided by |I|. If only a function table is supplied, assess the stability of the diagonal, the precision of the ordinates, and the geometry of the sampled function. If the function has a sharp change between nodes, doubling may reveal a large new contribution; if it has an endpoint singularity, the standard smooth expansion may fail. Neither case is repaired by reporting additional digits.

For a hand solution, write the step size for each row and make the panel count explicit. State the recurrence once, then show enough entries that each denominator and neighbor choice is auditable. Keep several guard digits during arithmetic and round only in the reported result. The first Romberg column is a trapezoidal sequence, the second is first-order extrapolation, and only the diagonal entries combine all available levels. Labeling them correctly avoids the common mistake of describing an off-diagonal entry as the final result.

### Decision procedure and limits

Use composite trapezoidal integration when the available data are equally spaced, the rule is requested, or a transparent baseline is useful. Use Romberg when nested refinements can be evaluated and the integrand is smooth enough for the even-power error model. If the ordinates are measured and noisy, the corrections may be smaller than the uncertainty in the data. If a kink or singularity is known, consider splitting the interval at that feature or selecting a method designed for it rather than extrapolating across it.

A strong accuracy comment has three separate statements: what the numerical table produced; what evidence of convergence the successive diagonal values provide; and what, if anything, is known rigorously about the actual error. For the pi exercise the exact integral provides a direct check. For a general integrand, the table alone supports a practical stabilization claim, not a universal bound. This distinction is the most important safeguard against treating an algorithm's formal order as a substitute for checking its assumptions.
'''
extras2={}
extras2['level_1']=r'''### Working carefully with endpoints, panel counts, and units

Before arithmetic, draw or list the partition. For an interval [a,b] and n equal panels, the nodes are x_i=a+ih and h=(b−a)/n. The last node must be b; if it is not, either the panel count or the step is wrong. In a composite trapezoid, the first and last heights appear once, and all other heights appear twice. This count follows from the panels touching each point. It also gives a quick check on a long addition: the bracket is f_0+2(f_1+…+f_{n−1})+f_n, not the unweighted sum of all heights.

A common route to error is to round each function value or intermediate weighted sum too early. Keep enough digits through the triangle, then round the final reported approximation. If the problem supplies a short table, do not claim more information than the table contains. The trapezoidal rule can be exact for a straight-line integrand over the entire interval, but a curved function generally leaves an approximation error. A finer mesh usually improves a smooth case, while Romberg attempts to cancel the leading pattern in that error.

### Applying a stopping rule in practice

A learner can use the change in successive diagonal values as a signal to stop refining. Suppose the newest two diagonal entries agree to four decimal places and the requested tolerance is about one part in ten thousand. That agreement supports reporting the result to that precision, but only if the function is smooth and the ordinates are reliable. If the values fail to settle, do not keep adding columns automatically. Check the recurrence, the panel counts, the midpoint evaluations, and the behavior of the integrand.

The lesson's pi assessment gives an especially clear check: its final Romberg estimate rounds to 3.1415927. This agrees with the familiar value of pi, but a different integral will not come with a known answer. In that case, say exactly what the table supports: for example, “the last two diagonal estimates differ by less than the chosen tolerance.” That is more accurate than calling their difference a guaranteed error bound. If a separate error theorem is used, state its assumptions and how they apply to the particular integrand.

### Why a table is not just arithmetic

The first column displays what uniform refinement alone does. The next column displays the correction after the first error term is removed. Later columns show further cancellation. Thus the table tells a story about how the numerical approximation changes as information is refined. It also makes method failures visible: an unexpected jump may indicate a wrong function value, a missed midpoint, a sign error, or a feature of the integrand that the old grid did not see.

When presenting a result, keep four labels visible: the interval, the number of panels, the corresponding width, and whether the value is trapezoidal or extrapolated. Without these labels, two correct numbers can be placed in the wrong table cell and produce a wrong result. With them, another reader can reproduce the computation, verify the triangle, and decide whether the stated precision is credible.
'''
extras2['level_2']=r'''### Separating discretization error from input uncertainty

Romberg extrapolation targets discretization error: the difference between the exact integral of the represented function and the composite trapezoidal approximation on a finite mesh. It does not remove error in the ordinates themselves. If each f(x_i) is a measured or rounded value, the quadrature sum is a weighted combination of those uncertainties. The signed cancellations that are useful for truncation error can also magnify uncertainty when extrapolated entries are formed. Consequently, the observed stabilization of a Romberg diagonal is persuasive only when the function values are substantially more accurate than the requested integral tolerance.

This distinction is especially important when the table values are given to a limited number of decimal places. Carry guard digits through the arithmetic, but do not interpret guard digits as new measurement information. If the integral is evaluated from an analytic function, the values can be recomputed at higher precision. If they are supplied measurements, reducing h further may produce no trustworthy improvement. The relevant method choice depends not only on formal order but also on the quality and repeatability of function evaluation.

### A structured exam response

A full answer can be organized in a short reproducible sequence. First identify [a,b], n, h, and the nodes. Next state the composite trapezoidal formula and show the values or sum used. Then add the next mesh level by halving h, rather than inventing unrelated ordinates. Build the extrapolation triangle using the factor 4^j−1 for column j. Finally give the last available diagonal value and a measured comment on its stability. If the problem provides an exact answer, compare against it; otherwise label the diagonal difference as a practical indicator.

For the source example estimating pi, the initial panel counts 1, 2, 4, 8, 16 give a coherent left edge. Four doublings produce the final estimate approximately 3.1415926653, which rounds to the printed answer 3.1415927. Retaining enough digits is essential because the extrapolation subtracts close estimates. If each row is rounded too aggressively before the next correction, the small difference can be dominated by arithmetic rounding and the final digit becomes unreliable.

### Diagnosing an unexpected table

If the first column does not approach a stable region, inspect whether the integrand is sufficiently smooth, whether the grid resolves a rapid change, and whether endpoints or midpoints have been entered correctly. If the first column looks plausible but the extrapolation column suddenly diverges, check the sign and denominator in the recurrence. The second column uses 15, not 3; the third uses 63. A missing row changes the pair of estimates and invalidates every subsequent entry.

A table with tiny differences can also be misleading. A rounded function table may cause repeated values, while cancellation may make two successive estimates close even though their common bias remains. Compare more than one diagonal transition where possible, and use any exact value, derivative information, or independent method that the problem supplies. Do not equate decimal agreement with a proof of accuracy.
'''
extras2['level_3']=r'''### Deriving the recursive trapezoidal update

The Romberg first column can be built either by recomputing every composite sum or by exploiting the nesting of the grids. Let n panels of width h_n=(b−a)/n produce T_n. Refinement to 2n panels retains all old nodes and inserts one midpoint in each old panel. In the new sum, every old interior point has half its previous coefficient, while the two endpoints also have half their old coefficients. These old contributions together are T_n/2. Every new midpoint appears once with coefficient h_n/2. Therefore

$$
T_{2n}=\frac12T_n+\frac{h_n}{2}\sum_{i=0}^{n-1}f\!\left(a+\left(i+\frac12\right)h_n\right).
$$

Writing h_{2n}=h_n/2 gives the equivalent coefficient h_{2n} in front of the midpoint sum. The two forms are useful for different bookkeeping conventions. A dimensional check confirms that the coefficient multiplying a function value has units of length. A direct expansion verifies the recurrence: the old endpoint weights become h_n/4, the old interior weights become h_n/2, and each inserted value also receives h_n/2.

In code or long hand work, maintain a single sequence of newly inserted midpoints. At the n-to-2n refinement there are exactly n new values, not 2n. Computing them only once reduces evaluations and avoids repeated rounding of old ordinates. Verify one refined result against the direct trapezoidal sum on a small grid before trusting the full array. Common implementation defects are a factor of two on the midpoint term, a midpoint formula using h_{2n} instead of the old interval spacing h_n, and an endpoint mistakenly included in the midpoint sum.

### Stability, convergence, and failure diagnosis

The error expansion is an asymptotic description, not a command that the sequence must improve monotonically from its first row. The coarse grids may not yet be fine enough for the leading even-power term to dominate. Later, rounded arithmetic can also cause apparent stagnation. Thus the difference of adjacent diagonal entries should be treated as an empirical convergence test, supplemented by an iteration cap and a check of the underlying data.

If the first-column trapezoid estimates oscillate or move unexpectedly, inspect the function's curvature and the panel values. If an extrapolated column grows dramatically, check index alignment, signed differences, and the denominator 4^j−1. If all rows repeat the same rounded number, the available precision may be exhausted. If the function has a discontinuity or a singular derivative, subdividing the interval at the feature or changing the formulation is more defensible than extending a formal high-order extrapolation.

A posteriori stability is not a certified error bound. A formal bound requires derivative information or a theorem that applies to the actual integrand and interval. The source's exact pi example allows a direct check because the target value is known; this is unusually helpful. For most integrals, report the observed diagonal change and explain why the smoothness assumptions appear plausible. Separate the statements “the last two estimates agree” and “the true error is bounded by this number.” The second statement requires proof that the first does not supply.

### Computation and rounding discipline

The recurrence subtracts neighboring approximations that may already be close. Premature rounding can erase a meaningful correction or change its sign. Retain several guard digits in the first column, perform each extrapolation with those digits, and round once at the end. Nevertheless, do not report more digits than the function evaluations, measurement quality, or error analysis supports. Arithmetic precision and information precision are different concepts.

For the source pi task, four doublings after the first trapezoid correspond to n=1,2,4,8,16. The final diagonal is approximately 3.1415926653 and the module rounds it to 3.1415927. The exact pi is 3.1415926536…, giving a difference near 1.2×10⁻⁸. That impressive match should not be generalized to every integral; it follows from this smooth integrand and the successful convergence of this particular nested sequence.

When using a supplied table, the ordinates may be the dominant uncertainty. The trapezoidal weights are positive, so an upper bound δ on each ordinate's absolute uncertainty leads to an immediate bound δ times the sum of the absolute quadrature weights for the trapezoidal sum. Romberg entries are linear combinations of those sums, so their uncertainty may be amplified by the extrapolation coefficients. This gives another reason to monitor input precision and not treat a stable sequence as a substitute for an uncertainty analysis.
'''
examples={}
examples['level_1']=r'''### Worked source example: Romberg integration of 1/x

The module asks for the integral of 1/x from 1 to 2. First use one trapezoid. The interval width is one, and the endpoint heights are 1 and 1/2:

$$
T_1=\frac12\left(1+\frac12\right)=0.7500000.
$$

With two panels, the midpoint is 3/2 and its height is 2/3:

$$
T_2=\frac{1/2}{2}\left[1+2\left(\frac23\right)+\frac12\right]=0.7083333.
$$

Refining to four panels gives T_4≈0.6970238; eight panels give T_8≈0.6941219; sixteen panels give T_16≈0.6933912. These are trapezoidal estimates, not yet the corrected Romberg answers. At each refinement, the new grid keeps the previous points and adds midpoints.

The first correction uses the two coarsest estimates. The finer value T_2 is used first; the signed difference T_2−T_1 is negative:

$$
R_{1,1}=T_2+\frac{T_2-T_1}{3}
=0.7083333+\frac{0.7083333-0.7500000}{3}\approx0.6944444.
$$

For the next pair,

$$
R_{2,1}=T_4+\frac{T_4-T_2}{3}
=0.6970238+\frac{0.6970238-0.7083333}{3}\approx0.6932539.
$$

A further first-column correction gives approximately 0.6931545. The next Romberg columns use denominators fifteen, sixty-three, and so on. Continuing the triangle gives a final diagonal value near 0.69314718. The exact integral is ln 2≈0.69314718, so the computed diagonal agrees to the displayed precision.

The lesson of the example is not that every integral should equal ln 2; it is how the estimates are organized. The trapezoidal values make the left edge, while the corrections use neighboring entries to remove their leading error terms. Keep the fine-minus-coarse sign: reversing it would move the first correction in the wrong direction. When an exact integral is unavailable, compare diagonal entries and report this as convergence evidence rather than a certified bound.
'''
examples['level_2']=r'''### Worked assessment: estimating pi with four doublings

Use the source integral

$$
\pi=\int_0^1\frac{4}{1+x^2}\,dx.
$$

Let T_n denote the composite trapezoidal estimate using n equal panels. Four doublings after the initial one-panel estimate use n=1,2,4,8,16. The corresponding values are

$$
\begin{aligned}
T_1&=3.0000000000, &T_2&=3.1000000000,\\
T_4&=3.1311764706, &T_8&=3.1389884945,\\
T_{16}&=3.1409416120.
\end{aligned}
$$

For the first extrapolation, use the formula with denominator 3:

$$
R_{1,1}=T_2+\frac{T_2-T_1}{3}=3.1000000000+\frac{0.1000000000}{3}=3.1333333333.
$$

The next adjacent pairs give R_{2,1}=3.1415686275, R_{3,1}=3.1415925025, and R_{4,1}=3.1415926512. To form the second column, the denominator is 4²−1=15. Its entries are 3.1421176471, 3.1415940941, and 3.1415926611. The third column uses 4³−1=63 and gives 3.1415857838 and 3.1415926384. The last entry uses 4⁴−1=255:

$$
R_{4,4}=R_{4,3}+\frac{R_{4,3}-R_{3,3}}{255}\approx3.1415926653.
$$

Thus the Romberg estimate rounds to 3.1415927, as in the module's answer. The exact pi is 3.141592653589…, so this example's actual difference is about 1.2×10⁻⁸. A full table should label its left edge as trapezoidal approximations and each subsequent column by the extrapolation order; the panel count and the column number mean different things.

The observed closeness to pi confirms this worked computation, but it does not prove that the Romberg table always supplies a rigorous error bound. In a new problem with no exact value, report the final diagonal and compare consecutive diagonal entries. Explain that this is a practical stabilization check, and state that a mathematical bound would need additional derivative information and verified hypotheses.
'''
examples['level_3']=r'''### Model solution: Romberg estimate of pi with four mesh doublings

The source assessment uses

$$
I=\int_0^1\frac{4}{1+x^2}\,dx=\pi.
$$

Set T_n equal to the composite trapezoidal rule with n equal panels. Begin with one panel and double four times. The first-column values, calculated from the trapezoidal rule or its nested-grid recurrence, are

$$
\begin{aligned}
T_1&=3.0000000000,\quad T_2=3.1000000000,\\
T_4&=3.1311764706,\quad T_8=3.1389884945,\\
T_{16}&=3.1409416120.
\end{aligned}
$$

Define R_{k,0}=T_{2^k}. The first extrapolation column uses denominator 3:

$$
R_{k,1}=R_{k,0}+\frac{R_{k,0}-R_{k-1,0}}{3}.
$$

It yields, for panel counts 2,4,8,16, the values 3.1333333333, 3.1415686275, 3.1415925025, and 3.1415926512. The second column uses denominator 15 and yields 3.1421176471, 3.1415940941, and 3.1415926611. The third column uses denominator 63 and yields 3.1415857838 and 3.1415926384. The fourth and final correction is

$$
R_{4,4}=R_{4,3}+\frac{R_{4,3}-R_{3,3}}{4^4-1}
=R_{4,3}+\frac{R_{4,3}-R_{3,3}}{255}\approx3.1415926653.
$$

The complete triangular arrangement is

$$
\begin{array}{c|ccccc}
n&T_n&R_{k,1}&R_{k,2}&R_{k,3}&R_{k,4}\\
1&3.0000000000&&&&\\
2&3.1000000000&3.1333333333&&&\\
4&3.1311764706&3.1415686275&3.1421176471&&\\
8&3.1389884945&3.1415925025&3.1415940941&3.1415857838&\\
16&3.1409416120&3.1415926512&3.1415926611&3.1415926384&3.1415926653
\end{array}
$$

The exact value is pi≈3.141592653589793, so the final difference is about 1.17×10⁻⁸ and the estimate rounds to 3.1415927. This is the result printed in the lesson. A small nonmonotone movement in the last columns does not invalidate the recurrence: later extrapolations cancel successive error terms and need not approach the answer monotonically.

For a reproducible exam solution, state that “four iterations” means four doublings after T_1, show the first-column mesh sizes, and use the correct denominator for each column. The difference between the last diagonal entries can be used as an empirical stopping indicator, but the actual error comparison above is possible only because this integral is exactly pi. For a general integrand, do not claim that a diagonal difference is a guaranteed bound without an independent error theorem.
'''

extras3={}
extras3['level_1']=r'''### The lesson's pi question as a final check

The module also asks students to estimate pi from the area under 4/(1+x²) between zero and one and comment on accuracy. This is a useful companion to the logarithm example because the answer is known in advance for checking, but the trapezoidal and Romberg calculations still use sampled values. Start with one panel: the endpoint heights are 4 and 2, so the first trapezoid is 3. Doubling the panels gives 3.1; four panels give approximately 3.1311765; eight give 3.1389885; and sixteen give 3.1409416. The raw estimates steadily approach pi in this example.

The first Romberg correction from 3.0 and 3.1 is 3.1333333. The next one uses 3.1 and 3.1311765, while later entries are formed from their own neighboring corrected values. After four mesh doublings the final diagonal is approximately 3.1415926653, which rounds to 3.1415927. The result is close to pi, and the difference between adjacent diagonal values is small. This is a reasonable comment on the computed convergence.

A student should not say that the method “always gives an exact answer after four steps.” It does not. This assessment is unusually convenient because the integral is a representation of pi, and the integrand is smooth on the interval. For another function, the same calculation may converge more slowly or behave irregularly. The justified conclusion is about this table: its diagonal entries stabilize and its final value agrees closely with the known value.

### Translating the method into a checklist

When the question gives an interval, first write its length and divide it by n to obtain h. Mark the endpoints and interior nodes. Apply the composite trapezoidal formula with each endpoint counted once and each interior value counted twice. To build Romberg values, halve h at each refinement and apply the recurrence column by column. Keep the signs and carry enough digits. At the end, state whether the final number is raw trapezoidal or extrapolated and explain what the changes between estimates show.

This checklist is useful because arithmetic errors often arise before the difficult part of the method. If the panel width does not fit the interval, every trapezoid is wrong. If a node is missed, both the left edge and the extrapolation triangle will be contaminated. If a denominator from the wrong column is used, the table may still look orderly but its values have no Romberg meaning. Naming the panel count and column for every number helps prevent these mistakes.
'''
extras3['level_2']=r'''### Accuracy comments that respect what the table can prove

Numerical analysis separates a computed approximation from a guarantee about its error. The Romberg table supplies a sequence of values. When the diagonal stabilizes, this is practical evidence that further refinement is changing the result only slightly. It is not, on its own, a rigorous upper bound on the difference from the exact integral. A bound needs more information, such as a derivative estimate together with an applicable error theorem. This distinction should be stated whenever a problem asks for a comment rather than supplying a known answer.

In the pi assessment, the exact integral is known. The final diagonal value 3.1415926653 differs from 3.1415926536… by about 1.2×10⁻⁸. This actual error is a property of that particular function, interval, and number of refinements. It is not inferred solely from the difference between two diagonal values. For the source logarithm example, ln 2 is likewise available for an after-the-fact check. If neither exact value is known, do not manufacture one; compare consecutive diagonal entries and call their difference an empirical indicator.

Precision of the input also matters. If f(x_i) is rounded, the quadrature result combines these rounded values with nonnegative trapezoidal weights. Increasing n may reduce discretization error while simultaneously increasing the number of approximate ordinates. Romberg's linear combinations can magnify the effect of those input uncertainties. A table whose entries are reported to three decimal places cannot support a claim of ten accurate digits merely because the recurrence prints them.

### When to refine and when to change the plan

Mesh refinement is sensible when a smooth function is under-resolved and additional evaluations are affordable. Romberg is especially effective when the trapezoidal error follows its expected even-power expansion over the available mesh widths. If the first two diagonal entries change substantially, another refinement can be useful. If they stop improving, test the arithmetic, inspect whether the integrand has a kink or endpoint feature, and check whether input rounding has become dominant.

The composite trapezoidal rule remains a useful baseline for irregular behavior because it is easy to interpret panel by panel. Romberg's extrapolation assumes more structure than the trapezoidal rule itself. A singularity or discontinuity can violate that structure, and a noisy table can cause the corrections to chase noise. In those cases, subdivide at known discontinuities, transform the interval only when the change of variables is justified, or choose another quadrature family. Blindly increasing the Romberg order is not a substitute for diagnosing the integrand.

An exam response can earn a clear accuracy conclusion with three facts: the final diagonal estimate, the change from the preceding diagonal value, and the known exact value if the exercise provides one. Add a sentence about assumptions. For an unknown integral, say that the diagonal appears stable to the shown precision, not that the true error is proved to be below the diagonal difference. Such wording is mathematically careful and still answers the question directly.
'''
extras3['level_3']=r'''### A posteriori diagnostics versus a priori error guarantees

Romberg tables invite an intuitive stopping test: compare successive diagonal estimates and stop once their difference is below a target τ. In implementation, require this condition for more than one refinement where practical, enforce a maximum row count, and detect stagnation due to floating-point rounding. A single small difference can occur by cancellation even when both estimates share a bias. A stable sequence is meaningful evidence only in the context of a smooth integrand and trustworthy function values.

This is an a posteriori diagnostic because it uses computed outputs. A priori error analysis instead bounds the error from properties of f before the computation or from derivative information. The two should not be conflated. The source assessment for pi permits an actual error check because I=π is known. The logarithm example permits comparison with ln 2. In general applications, an exact integral may not be available, so the honest conclusion is based on convergence evidence and explicit assumptions, not an invented reference value.

### Round-off and data uncertainty in extrapolated values

Every extrapolated entry is a linear combination of trapezoidal estimates. As the column index grows, the coefficients can become larger in magnitude and cancellation more pronounced. This is desirable for removing truncation terms but can amplify round-off and uncertainty in supplied ordinates. The mathematically derived asymptotic order describes truncation behavior under smoothness assumptions; it does not include errors in f evaluations unless those are separately analyzed.

For a trapezoidal weighted sum with node errors bounded by δ, a first bound on the data contribution is δ times the sum of the absolute quadrature weights. An extrapolated entry combines several such sums, so its data uncertainty can be bounded using the absolute values of its combination coefficients, but that bound may grow with the extrapolation level. Consequently, a high-order entry is not automatically more reliable when the function values are noisy. Stop before data uncertainty overwhelms the truncation-error reduction.

Arithmetic should retain guard digits because the recurrence subtracts nearby estimates. At the same time, significant figures in the final answer must be supported by input accuracy and by convergence evidence. If the table values themselves have only a few given decimals, reporting many extra digits misrepresents the available information. For analytic f, evaluate the new midpoint values accurately enough that the extrapolation, rather than input rounding, controls the result.

### Indexing conventions and triangular-table construction

A notation error is easy to make because references use either R_{k,j} or T_k^{(j)} and may count the starting trapezoid as row zero or row one. Define the convention explicitly. With R_{k,0}=T_{2^k}, the valid entries satisfy k≥j and

$$
R_{k,j}=R_{k,j-1}+\frac{R_{k,j-1}-R_{k-1,j-1}}{4^j-1}.
$$

Thus the first extrapolation at k=1 uses T_2 and T_1 with denominator 3; the second extrapolation at k=2 uses two first-column-corrected values with denominator 15; and so forth. An entry at (k,j) is not computed directly from two trapezoidal values except when j=1. Each higher column uses its own neighboring column.

A reliable table-building procedure is: calculate and label all T values; compute the first extrapolation column from adjacent T pairs; compute each later column from adjacent entries in the immediately preceding column; and stop when the requested depth or convergence criterion is met. Verify one cell manually and confirm that the table has k−j+1 valid entries in row k under this indexing. These checks make the table auditable and catch off-by-one mistakes.

### Interpreting the module's two Romberg examples

For ∫_1^2 dx/x, the trapezoidal sequence for n=1,2,4,8,16 is approximately 0.7500000, 0.7083333, 0.6970238, 0.6941219, and 0.6933912. Extrapolation rapidly approaches ln 2. This example demonstrates the method on a simple monotone integrand with a known comparison value. Its numerical success should be interpreted as a worked case, not as evidence that Romberg always converges at the same rate.

For the assessment integral of 4/(1+x²) from 0 to 1, the five raw trapezoid values and the extrapolation triangle yield approximately 3.1415926653 after four doublings, rounding to 3.1415927. The final value differs from π by roughly 1.2×10⁻⁸. The module's answer therefore agrees with a calculation that counts the initial n=1 trapezoid followed by four refinements. If an instructor counts the initial approximation as an iteration, the phrase “four iterations” could be ambiguous; listing n explicitly resolves the convention without changing the method.

### Method selection and defensible reporting

Choose composite trapezoidal integration when equally spaced ordinates are supplied, a transparent baseline is needed, or repeated values must be reused. Choose Romberg when nested grids can be evaluated and the integrand is smooth enough for the predictable even-power error expansion. If the function is nonsmooth, data are noisy, or refinement is prohibitively costly, the theoretical order alone is a poor decision criterion.

A concise but complete report states the interval and panel counts, the composite formula or recursive update, the extrapolation recurrence, the final diagonal value, and the evidence used to judge it. Keep the error statement separate: “the diagonal has stabilized” is an observation; “the absolute error is at most τ” is a bound and needs a proof. This separation is both mathematically precise and useful in numerical practice.
'''
extras4={}
extras4['level_1']=r'''### Final audit before submitting the table

Before submitting a Romberg answer, re-read the labels as if another learner had to reproduce your work. The interval endpoints should match the first and last nodes; the sum of all panel widths must be exactly the interval length. The raw trapezoid sequence should identify its panel counts, and each extrapolated cell should be attached to a clear row and column. The sign of a correction should follow the written fine-minus-coarse formula, not a remembered expectation about whether the estimate ought to rise or fall.

For the source assessment of pi, the panel counts are 1, 2, 4, 8, and 16 when four doublings follow the starting trapezoid. A verbal report that says “four iterations” but lists only four rows may leave the convention unclear. Writing n explicitly avoids that ambiguity. The final value near 3.1415926653 is a Romberg diagonal value; 3.1409416120 is the last raw trapezoid. Confusing the two numbers would misstate both the method and its achieved accuracy.

A useful interpretation states that the diagonal values settle near the known answer, while also admitting that a table is not a universal proof. This final distinction is part of responsible numerical work: answer the calculation, identify the evidence for the reported precision, and do not claim a stronger bound than the calculation supplies.
'''
extras4['level_2']=r'''### Mesh interpretation for non-unit intervals

The examples in the module use intervals of width one, but the bookkeeping is unchanged on any [a,b]. With n panels, h=(b−a)/n and x_i=a+ih. On a longer interval, halving h doubles n while leaving a and b fixed. A frequent mistake is to halve the endpoint interval or to retain the old h after doubling the panel count. The node formula and the equality nh=b−a detect both mistakes immediately.

The composite trapezoidal sum is an approximation to an integral, so its scale should reflect both the ordinate and the interval width. If f is multiplied by a constant c, every trapezoidal and Romberg value is multiplied by c. If the interval is shortened, the area usually changes accordingly. These simple invariance checks help catch errors in weights, factors of h, and interval transformations.

When intervals are subdivided at a known feature, each subinterval can be integrated separately and the results added. This is often more defensible than asking a single uniform grid to straddle a jump or sharp corner. The smooth error expansion underlying Romberg should be assessed on each smooth piece; it should not be assumed across a discontinuity. This practical observation connects method selection to the shape of the actual integrand rather than to a formula alone.
'''
extras4['level_3']=r'''### Linearity and scaling checks for computed tables

Both the composite trapezoidal rule and each Romberg extrapolation are linear in the sampled function values. If f is replaced by cf, every table entry should be multiplied by c; if two sampled functions are added, their corresponding table entries add. This gives inexpensive checks on a numerical implementation and a way to diagnose a missing factor in the quadrature formula. The step width is the only factor that changes when the interval is rescaled, and every entry still has units of f times x.

A change of interval is not a reason to reuse the same tabulated T values. The nodes and h depend on [a,b]. For a fixed number of panels n, enlarging b−a enlarges h and changes every evaluation point. For a fixed h, changing the interval changes n and may make the number of panels nonintegral. Explicitly record which quantity is held fixed before comparing two grids.

If the integrand is split over adjacent intervals, add the resulting integral estimates and preserve the split locations in the record. A discontinuity should be an endpoint of a subproblem, not an interior point across which a smooth error model is assumed. The Romberg table on each smooth subinterval can then be checked separately. Summing independently stabilized estimates may be safer than extrapolating across a nonsmooth junction.

### A reproducibility record for numerical integration

A complete calculation record contains the integrand definition, limits, node rule, panel counts, h values, raw trapezoidal entries, extrapolation recurrence, rounding policy, and any stopping test. Such a record lets another person distinguish a mathematical discrepancy from a transcription error. A minimal table without function definition and panel labels cannot be independently checked, even if its final number looks familiar.

For reproducibility, store unrounded or guard-digit values during computation and round only in the display. If values are taken from a printed function table, note their supplied precision. If evaluated from an expression, state enough digits to permit recalculation. When the source gives a final result, treat it as a cross-check rather than a substitute for showing the sequence. The lesson's pi answer, 3.1415927, is a check on the row with 16 panels and four extrapolation stages; it does not determine the intermediate entries by itself.

A method report should state exactly what “accuracy” means in context. The absolute error is a comparison with the exact integral, when known. A relative error scales that difference by the magnitude of the exact result. A diagonal difference is a convergence indicator. A formal upper bound needs an error theorem and its hypotheses. Keeping those quantities distinct prevents a numerical result from being overinterpreted and makes the conclusion useful outside a classroom exercise.
'''
extras5={}
extras5['level_1']=r'''### Relating a correction to the original area

An extrapolated value should still be interpreted as an estimate of the same definite integral, not as the area of an additional geometric region. The correction is a numerical adjustment that estimates and removes a leading bias in the trapezoidal values. Its size may be positive or negative. If it is much larger than the difference between the two raw estimates would suggest, check the denominator and row pairing. If it is tiny, that may indicate stabilization, but also check the number of digits carried through the subtraction.

The composite rule itself remains easy to visualize: every panel is a trapezoid, and adjoining panels share a vertical side. This mental picture explains the weighting but does not replace the formula. When the integrand is curved, the straight sides approximate rather than exactly trace the graph. The refinement and extrapolation are systematic ways to improve that representation, and their reliability depends on the function and the values used.
'''
extras5['level_2']=r'''### Why the weights and error scaling must be kept separate

Two different sets of weights occur in a Romberg computation. The trapezoidal weights arise from integrating the piecewise-linear interpolant and assign half contributions to the two endpoints of the interval and full contributions to interior grid points. The extrapolation coefficients arise from canceling the mesh-error expansion and depend on the Romberg column. Confusing these layers can lead to incorrect sums: first compute a valid trapezoidal value, then combine those valid values with the extrapolation recurrence.

The factor four in the error scaling comes from h² when the mesh is halved. It is not the factor by which the number of function evaluations grows. Panel counts double, while the leading error quarters. Later powers follow from the remaining error terms. This conceptual separation is helpful both for derivations and for checking code: panel recursion handles function values; extrapolation handles already computed quadrature approximations.
'''
extras5['level_3']=r'''### Independent checks and limitations of the answer

When possible, verify a Romberg result with a different calculation, such as a known antiderivative, an exact value listed in the module, or an independently implemented trapezoidal refinement. Agreement does not prove correctness if the same transcription mistake is shared, but it provides independent evidence. For the source pi example, the familiar exact value is a strong final check after the full table is computed.

Do not treat increased table depth as a universal cure. The linear combinations used for higher extrapolation columns can become sensitive to round-off, and nonsmooth input can invalidate the assumed expansion. A sensible solver uses the requested depth, checks diagonal stability and data precision, then stops or changes strategy when assumptions fail. Reporting that limitation is part of the mathematical conclusion, not an apology for the numerical method.
'''
repair_topic(203,{'level_1':1294,'level_2':1259,'level_3':1336},
 {k:extras[k]+'\n\n'+extras2[k]+'\n\n'+extras3[k]+'\n\n'+extras4[k]+'\n\n'+extras5[k] for k in extras},examples)
