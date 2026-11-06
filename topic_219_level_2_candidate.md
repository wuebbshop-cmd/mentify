## 1. Decision making when probabilities are unknown

Decision making under uncertainty applies when the decision maker can list the states of nature but has no reliable probabilities for them. The choice cannot be based on an expected monetary value because the probability weights needed for an expectation are missing. Instead, the decision maker selects a criterion that expresses how they treat the unknown.

The approved lesson focuses on three payoff criteria: pessimism or conservatism (maximin), optimism or aggression (maximax), and the coefficient-of-optimism method (Hurwicz). The lesson’s introduction also mentions least regret, which is developed fully in the next lesson. Do not invent state probabilities or average the columns unless a problem explicitly supplies an equal-likelihood rule.

## 2. Payoff table and decision rules

Write each alternative as a row and each state as a column. Let $a_{ij}$ be the payoff from alternative $i$ when state $j$ occurs. The module’s worked investment table is:

| Strategy | High growth | Medium growth | No change | Low growth |
| --- | ---: | ---: | ---: | ---: |
| Bonds | 12 | 8 | 7 | 3 |
| Stock | 15 | 5 | 5 | -2 |
| Deposits | 7 | 7 | 7 | 7 |

Payoffs are rates of return in percent. Because these are gains to maximize, larger values are preferred. If the entries represented costs, the direction of the rules would need to be adapted.

### Maximax: optimistic criterion

For each alternative, find its best possible payoff, then choose the largest of those row maxima:

$$
M_i=\max_j a_{ij},\qquad \text{choose } i \text{ maximizing } M_i.
$$

Here the row maxima are 12 for bonds, 15 for stock, and 7 for deposits. Maximax selects stock, whose best possible return is 15%. It is an aggressive rule: it focuses on the favorable state and does not penalize a poor result elsewhere.

### Maximin: pessimistic or conservative criterion

For each alternative, find its worst payoff, then choose the largest of those row minima:

$$
m_i=\min_j a_{ij},\qquad \text{choose } i \text{ maximizing } m_i.
$$

The row minima are 3 for bonds, -2 for stock, and 7 for deposits. Maximin selects deposits, guaranteeing a 7% return in every listed state. It protects against the worst case, but may reject a strategy with a better high-state outcome.

## 3. Hurwicz coefficient of optimism

Hurwicz’s method combines each row’s best and worst payoff. Choose an optimism coefficient $\alpha$ with $0\le\alpha\le1$: $\alpha=1$ gives full weight to optimism and $\alpha=0$ gives full weight to pessimism. For each alternative calculate

$$
H_i=\alpha(\text{row maximum})+(1-\alpha)(\text{row minimum}),
$$

then select the largest $H_i$ for a payoff table.

Using the source example with $\alpha=0.6$:

$$
H_{B}=0.6(12)+0.4(3)=8.4,
$$

$$
H_{S}=0.6(15)+0.4(-2)=8.2,
$$

$$
H_{D}=0.6(7)+0.4(7)=7.0.
$$

Hurwicz selects bonds. Check that the weights add to one and that the minimum payoff remains negative when appropriate. A common arithmetic error is to multiply the minimum by $\alpha$ instead of $1-\alpha$.

The role of $\alpha$ can be inspected rather than treated as a mysterious input. For this table,

$$
H_B=3+9\alpha,\qquad H_S=-2+17\alpha,\qquad H_D=7.
$$

Deposits remain the largest Hurwicz value while $\alpha<4/9$, because the fixed deposit return is 7. Bonds overtake deposits at $\alpha=4/9$. Bonds and stock tie when $3+9\alpha=-2+17\alpha$, giving $\alpha=5/8=0.625$. Therefore deposits are selected below $4/9$, bonds between $4/9$ and $5/8$, and stock above $5/8$ (with ties at the boundaries). At the source value $\alpha=0.6$, bonds narrowly beat stock. This sensitivity check shows how the recommendation depends on the decision maker’s stated optimism.

## 4. Applying the criteria to the assessment cases

The module’s investment-grade exercise gives four alternatives and three quality states:

| Strategy | Grade 1 | Grade 2 | Grade 3 |
| --- | ---: | ---: | ---: |
| A | 600 | 700 | 750 |
| B | 500 | 650 | 550 |
| C | 450 | 290 | 420 |
| D | 300 | 420 | 620 |

For maximax, the row maxima are 750, 650, 450, and 620, so choose A. For maximin, the row minima are 600, 500, 290, and 300, so choose A. With $\alpha=0.7$, the Hurwicz values are A: $0.7(750)+0.3(600)=705$; B: $0.7(650)+0.3(500)=605$; C: $0.7(450)+0.3(290)=402$; and D: $0.7(620)+0.3(300)=524$. Again choose A. The same choice under all three rules is a result of these payoffs, not a general property of the criteria.

This example also permits a dominance check. Alternative A yields 600, 700, and 750, which is higher than B’s 500, 650, and 550 in every state. It is also higher than C’s 450, 290, and 420 and D’s 300, 420, and 620 in every state. A therefore strictly dominates B, C, and D: it gives a better payoff regardless of which listed state occurs. Once dominance is verified, all three rules must prefer A, although calculating the requested criteria is still necessary when the question asks for their values. If an alternative is worse in every state, it cannot become optimal under any row-based payoff criterion that respects the ordering of outcomes.

Dominance does not replace criterion selection when one alternative is better in some states but worse in others. The bonds/stock/deposit example is not resolved by dominance: stock has the highest best-case return, deposits have the highest worst-case return, and bonds have the best Hurwicz score at the stated coefficient. The analyst must expose that trade-off rather than announce one universally correct choice.

In the land example, drilling has payoffs 700 if oil is found and -100 if dry; selling gives 90 in either state. Its row minima are -100 and 90, so maximin selects selling. Its row maxima are 700 and 90, so maximax selects drilling. This makes the attitude trade-off explicit. Although the source also supplies probabilities 0.25 and 0.75, those probabilities are not used by maximin or maximax; they belong to a risk/expected-value analysis.

The same land example also shows exactly how Hurwicz differs from the endpoint criteria. Hurwicz uses the best and worst payoff in each row, not the state probabilities. With optimism coefficient $\alpha$, the scores are

$$
H_{drill}=700\alpha+(-100)(1-\alpha)=800\alpha-100,
\qquad H_{sell}=90\alpha+90(1-\alpha)=90.
$$

Drilling is chosen when $800\alpha-100>90$, or $\alpha>0.2375$. This threshold is based on the payoff extremes and the optimism coefficient, not the prior probability of oil.

If the problem instead explicitly asks for EMV and uses the stated oil probability, then the calculation is different:

$$
EMV(drill)=0.25(700)+0.75(-100)=100,\qquad EMV(sell)=0.25(90)+0.75(90)=90.
$$

EMV selects drilling, but for a different reason than maximax or Hurwicz. The three criteria should not be blended: the requested information rule determines which calculation answers the question.

The presence of the 0.25/0.75 prior does not make the optimistic and pessimistic calculations “wrong”; it means the problem contains information that those specified criteria deliberately do not use. If asked to compare all methods, report each result under its own assumption: maximax takes the best possible payoff, maximin protects the worst payoff, Hurwicz uses the declared optimism coefficient, and EMV uses the probability distribution. EMV is not more appropriate merely because it uses more numbers; it is appropriate when expected payoff is the requested decision rule.

The assumptions behind the table should also be checked. States should be mutually exclusive so that only one column applies on a trial, and collectively exhaustive so that no material outcome is omitted. Payoffs must use a consistent unit and a consistent definition of net return. If a table includes a “no action” alternative, keep it in the comparison; omitting it can make every listed choice look artificially attractive. If two actions tie under a criterion, report the tie and apply any additional stated preference rather than breaking it silently.

For a cost-minimization problem, optimism means hoping for a low cost, so the optimistic rule becomes the smallest row minimum (minimin); the conservative rule becomes the smallest row maximum (minimax cost). The objective must be translated before applying payoff-language formulas. Under the common Hurwicz convention, weight the row’s minimum cost by the optimism weight and its maximum cost by the pessimism weight, then choose the smallest weighted cost. State the convention explicitly because some texts define the coefficient with the opposite label.

## 5. Interpretation and limits

These criteria are decision rules, not forecasts of which state will happen. Maximax is appropriate only when the decision maker accepts a highly optimistic stance; maximin is protective; Hurwicz makes the compromise weight explicit. None uses the full distribution of possible outcomes, and none guarantees the selected act will have the best realized result.

Regret is a separate comparison: it asks how far an act falls short of the best act for the state that occurs. The next lesson formalizes that criterion. When credible probabilities are available, use risk criteria such as EMV rather than pretending that the uncertain-state rules are expected values.

## 6. Exam procedure and common mistakes

1. Confirm that probabilities are absent or that the question specifically requests an uncertainty criterion.
2. Label rows as alternatives and columns as states; preserve the payoff units.
3. For maximax, calculate each row maximum and choose the greatest.
4. For maximin, calculate each row minimum and choose the greatest minimum.
5. For Hurwicz, calculate each row’s maximum and minimum, apply $\alpha$ and $1-\alpha$, then choose the highest weighted value.
6. State the selected act and explain the criterion’s attitude to uncertainty.

Typical mark losses include taking the minimum across the entire table instead of row by row, selecting the smallest row minimum under maximin, applying Hurwicz to all outcomes rather than the row extremes, confusing a payoff objective with a cost objective, and treating the existence of probabilities in the problem statement as a reason to use them even when the requested criterion ignores them.