## 1. Three related decision quantities

Expected monetary value (EMV) is the probability-weighted payoff for an act. Expected opportunity loss (EOL) is the probability-weighted regret for that same act. Expected payoff under perfect information (EPPI) is the expected payoff if the state of nature were known before the act was selected. Expected value of perfect information (EVPI) is the improvement from having that information compared with choosing now using the best EMV.

For a payoff-maximization problem with states $j$, probabilities $p_j$, and payoff $a_{ij}$ for act $i$:

$$
EMV_i=\sum_jp_ja_{ij},\qquad
EPPI=\sum_jp_j\max_i(a_{ij}).
$$

The maximum inside EPPI is taken separately for each state because perfect information lets the decision maker choose a different best act after learning which state occurred.

## 2. Deriving the EOL identity

The opportunity loss in state $j$ for act $i$ is

$$
L_{ij}=\max_k(a_{kj})-a_{ij}.
$$

Weight by probabilities and sum:

$$
EOL_i=\sum_jp_jL_{ij}
=\sum_jp_j\max_k(a_{kj})-\sum_jp_ja_{ij}
=EPPI-EMV_i.
$$

Therefore, for every act,

$$
EMV_i+EOL_i=EPPI.
$$

Because EPPI is the same for every act, the act with the largest EMV has the smallest EOL. Taking the best current act gives

$$
EVPI=EPPI-\max_iEMV_i=\min_iEOL_i.
$$

This is the module’s central relationship. It is valid when the payoff table, states, probabilities, and objective are consistent across the calculations. For cost minimization, the analogous analysis must be formulated with costs and the best (minimum) conditional cost; do not mix a cost criterion with payoff formulas.

## 3. Toy-company example from the module

The source reports the following results for the toy designs:

| Act | EMV | EOL | EMV + EOL |
| --- | ---: | ---: | ---: |
| Gears and levers | 412,500 | 48,000 | 460,500 |
| Action springs | 455,000 | 5,500 | 460,500 |
| Weights and pulleys | 417,500 | 43,000 | 460,500 |

Each act’s EMV plus EOL is 460,500, so that amount is EPPI. The maximum EMV is 455,000, attained by action springs. Hence

$$
EVPI=460{,}500-455{,}000=5{,}500.
$$

The minimum EOL is also 5,500. The decision without additional information is action springs. Perfect information could improve the expected payoff by at most 5,500, so it would not be rational to pay more than that for perfect information under this model.

This example supports two independent checks. First, every row sum is the same: $412{,}500+48{,}000=460{,}500$, $455{,}000+5{,}500=460{,}500$, and $417{,}500+43{,}000=460{,}500$. Second, the row with the largest EMV is the one with the smallest EOL. If either check fails, revisit the column bests or the probability-weighted sums.

## 4. Worked verification: real-estate investment

The assessment gives these population-growth outcomes:

| State | Probability | Apartment $A_1$ | Mall $A_2$ | Office $A_3$ |
| --- | ---: | ---: | ---: | ---: |
| High | 0.50 | 150,000 | 75,000 | 100,000 |
| Average | 0.30 | 10,000 | 30,000 | 50,000 |
| Slow | 0.20 | -75,000 | 15,000 | -200,000 |

The EMVs are

$$
EMV(A_1)=0.5(150{,}000)+0.3(10{,}000)+0.2(-75{,}000)=63{,}000,
$$

$$
EMV(A_2)=0.5(75{,}000)+0.3(30{,}000)+0.2(15{,}000)=49{,}500,
$$

$$
EMV(A_3)=0.5(100{,}000)+0.3(50{,}000)+0.2(-200{,}000)=25{,}000.
$$

The statewise best payoffs are 150,000, 50,000, and 15,000. Thus

$$
EPPI=0.5(150{,}000)+0.3(50{,}000)+0.2(15{,}000)=93{,}000.
$$

So $EVPI=93{,}000-63{,}000=30{,}000$. The EOL table gives A1: 30,000; A2: 43,500; A3: 68,000. The minimum EOL agrees with EVPI. The source prints 65,000 for A3, but its own weighted terms add to $25{,}000+0+43{,}000=68{,}000$; use the recomputed value and explain the correction.

For clarity, the complete loss table is:

| State | Probability | Apartment $A_1$ | Mall $A_2$ | Office $A_3$ |
| --- | ---: | ---: | ---: | ---: |
| High | 0.50 | 0 | 75,000 | 50,000 |
| Average | 0.30 | 40,000 | 20,000 | 0 |
| Slow | 0.20 | 90,000 | 0 | 215,000 |
| **EOL** | | **30,000** | **43,500** | **68,000** |

The EOL for the office is

$$
0.50(50{,}000)+0.30(0)+0.20(215{,}000)=68{,}000.
$$

The module’s 65,000 is inconsistent with its displayed probabilities and losses. The corrected value does not change the result because the apartment has the smallest EOL and largest EMV.

The perfect-information policy can be stated explicitly. If growth is high, choose the apartment for 150,000; if growth is average, choose the office for 50,000; if growth is slow, choose the mall for 15,000. Its expectation is 93,000. Without information, the investor must select one alternative now; the apartment has the largest EMV at 63,000. The expected improvement is therefore 30,000. For the apartment decision, the regret row is 0 in the high-growth state, 40,000 in the average state, and 90,000 in the slow state, so its EOL is $0.5(0)+0.3(40{,}000)+0.2(90{,}000)=30{,}000$.

The other rows provide a second audit of the same identity: $49{,}500+43{,}500=93{,}000$ for the mall and $25{,}000+68{,}000=93{,}000$ for the office. The office figure must use the corrected EOL of 68,000; using the printed 65,000 would break the constant-sum check.

## Source activity: a second identity check

The lesson’s activity uses this payoff table:

| Event | Probability | $A_1$ | $A_2$ | $A_3$ |
| --- | ---: | ---: | ---: | ---: |
| $E_1$ | 0.3 | 10 | 20 | 30 |
| $E_2$ | 0.5 | 40 | -20 | 20 |
| $E_3$ | 0.2 | 20 | 10 | -10 |

The EMVs are

$$
EMV(A_1)=0.3(10)+0.5(40)+0.2(20)=27,
$$

$$
EMV(A_2)=0.3(20)+0.5(-20)+0.2(10)=-2,
\qquad
EMV(A_3)=0.3(30)+0.5(20)+0.2(-10)=17.
$$

The column bests are 30, 40, and 20, so the regret rows are $A_1=(20,0,0)$, $A_2=(10,60,10)$, and $A_3=(0,20,30)$. Thus

$$
EOL(A_1)=0.3(20)=6,\qquad
EOL(A_2)=0.3(10)+0.5(60)+0.2(10)=35,
$$

$$
EOL(A_3)=0.5(20)+0.2(30)=16.
$$

Expected payoff under certainty is $EPPI=0.3(30)+0.5(40)+0.2(20)=33$. Therefore $EVPI=33-27=6$, matching the minimum EOL. This short table verifies both the algebraic identity and the decision: choose $A_1$ without information, and its expected gain from perfect information is 6 payoff units.

The remaining rows confirm the identity independently: $EMV(A_2)+EOL(A_2)=-2+35=33$ and $EMV(A_3)+EOL(A_3)=17+16=33$. Each action’s EMV plus EOL reaches the same EPPI, even though the action values and expected losses differ. The action with the greatest EMV, $A_1$, is also the action with the least EOL.

## 5. What perfect information is worth

EVPI is an upper bound on the amount a decision maker should pay for perfect information before making the decision. It is nonnegative because knowing the state allows the decision maker to choose the best act for that state; the information cannot force a worse choice if it can be ignored. EVPI is zero when one act is already best in every state with positive probability, or when there is no expected improvement from switching by state.

The nonnegativity follows directly from the equations. For every act $i$ and state $j$, the statewise best payoff satisfies $\max_k(a_{kj})\ge a_{ij}$. Multiplying by nonnegative probabilities and summing gives $EPPI\ge EMV_i$ for every act. In particular, $EPPI\ge\max_iEMV_i$, hence $EVPI\ge0$. If a payoff-maximization calculation produces negative EVPI, recheck the statewise maxima, probability weights, or the comparison of the two totals.

EVPI is not the value of an imperfect forecast. A forecast may be wrong, so its expected value must account for signal accuracy and posterior probabilities. Bayes’ decision analysis evaluates such sample information. In practice, compare the cost of information with the expected improvement it produces, and use only values from a consistent payoff table.

Perfect information means the state is known before choosing, so the selected act may vary by state. It does not mean that one act is selected now and then receives a better outcome later. If one alternative is best in every state with positive probability, learning the state cannot improve the decision and EVPI is zero. States with probability zero do not affect EMV, EOL, EPPI, or EVPI, although they may still matter for a separate worst-case criterion.

## 6. Exam method and common pitfalls

1. Calculate each EMV by multiplying row payoffs by their state probabilities.
2. Find the largest EMV; that is the best act without information.
3. For each state, identify its best payoff; then weight those statewise bests to calculate EPPI.
4. Subtract maximum EMV from EPPI to calculate EVPI.
5. Independently construct EOL and check that its minimum equals EVPI and that each act satisfies EMV + EOL = EPPI.
6. State the interpretation and units.

Common errors include taking the largest row payoff for EPPI instead of the best payoff in each state, using a different probability set for EMV and EOL, failing to weight a statewise maximum, treating EVPI as a guaranteed realized gain, and copying a source total that does not agree with its own arithmetic. The identity is also a useful diagnostic: if $EMV_i+EOL_i$ differs across acts, recheck the payoff, regret, and probability calculations.

For a complete written response, report four things: the best act without information, the statewise best act under perfect information, the EPPI and its units, and the difference between EPPI and maximum EMV. If asked to use the loss method, show the regret column benchmarks, expected-loss row totals, and the minimum EOL. Finish by interpreting EVPI as a ceiling on the purchase price of perfect information, not as guaranteed revenue. If an alternative forecast is imperfect, move to posterior expected values rather than treating its prediction as the known state.

Keep the order of operations visible. First select the best act in each state to form EPPI; only then multiply those statewise best payoffs by their probabilities and sum. Separately, calculate each act’s EMV by weighting across its row. These are different paths through the same table, and swapping a row maximum for the statewise maxima is a common reason an otherwise careful EVPI calculation fails.