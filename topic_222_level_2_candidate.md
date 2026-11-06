## 1. Opportunity loss and decision purpose

Opportunity loss is the payoff forgone when an act is chosen instead of the best act for the state that actually occurs. It is also called regret. The decision maker chooses before knowing the state, but the loss table asks a useful question for every possible state: “If this state occurred, how much worse would this act be than the best act for that state?”

This comparison is made state by state because the best action may change with the event. An alternative is not judged against the single largest payoff anywhere in the entire table. It is judged against the best payoff available in the specific column. Regret is therefore a hindsight measure: it describes the cost of not having selected the column’s winner after learning which state occurred.

For payoff maximization, the opportunity loss of act $i$ in state $j$ is

$$
L_{ij}=\max_k(a_{kj})-a_{ij}.
$$

The best payoff in each column has loss zero. When probabilities are available, expected opportunity loss (EOL) for act $i$ is

$$
EOL_i=\sum_j p_jL_{ij}.
$$

Choose the act with the smallest EOL. This is a risk criterion because it needs probabilities; it is different from minimax regret, which does not require probabilities and minimizes the largest loss in each row.

## 2. Constructing the loss table

Follow four steps:

1. Write the payoff matrix, alternatives, states, and probabilities.
2. In each state column, find the best payoff among the alternatives.
3. Subtract each cell payoff from its column’s best payoff to obtain the opportunity loss.
4. Multiply each loss by the probability of its state, add across each row, and choose the smallest expected loss.

Before calculating, verify that the table is a payoff table. If it is a cost table, lower cost is better and the appropriate loss is cost minus the minimum cost in that state. Do not apply a maximization rule to costs.

## 3. Source worked example: toy manufacturing

The module’s payoff table gives profits for three toy designs under light, moderate, and heavy demand:

| Demand | Probability | Gears and levers | Action springs | Weights and pulleys |
| --- | ---: | ---: | ---: | ---: |
| Light | 0.1 | 25,000 | -10,000 | -125,000 |
| Moderate | 0.7 | 400,000 | 440,000 | 400,000 |
| Heavy | 0.2 | 650,000 | 740,000 | 750,000 |

The column bests are 25,000, 440,000, and 750,000. Subtracting each payoff from its column best gives:

| Demand | Probability | Gears and levers | Action springs | Weights and pulleys |
| --- | ---: | ---: | ---: | ---: |
| Light | 0.1 | 0 | 35,000 | 150,000 |
| Moderate | 0.7 | 40,000 | 0 | 40,000 |
| Heavy | 0.2 | 100,000 | 10,000 | 0 |
| **EOL** | | **48,000** | **5,500** | **43,000** |

For example, the EOL of gears and levers is

$$
0.1(0)+0.7(40{,}000)+0.2(100{,}000)=48{,}000.
$$

The EOL of action springs is

$$
0.1(35{,}000)+0.7(0)+0.2(10{,}000)=5{,}500.
$$

Action springs has the smallest expected opportunity loss, so it is preferred by the EOL criterion. This does not mean it has the highest payoff in every state; it means its probability-weighted foregone payoff is smallest.

For completeness, the EOL of weights and pulleys is

$$
0.1(150{,}000)+0.7(40{,}000)+0.2(0)=43{,}000.
$$

The row is evaluated using the probability printed for each demand state. Do not average its three losses equally: light, moderate, and heavy demand have different probabilities. First determine the regret values, then weight those values. A zero in one cell does not make the entire act loss-free. Gears and levers has zero loss under light demand but can lose 100,000 relative to the best choice under heavy demand.

## 4. Profit versus cost losses

For a profit table, regret is column maximum minus cell. For a cost table, regret is cell minus column minimum:

$$
L_{ij}^{cost}=c_{ij}-\min_k(c_{kj}).
$$

The module’s garment exercise converts fixed and variable costs into profit first. At a selling price of 75 dollars, production of $D$ units has profit $(75-v)D-F$, where $v$ is variable cost per unit and $F$ is fixed cost. The resulting payoff table is:

| Sales | Probability | Design A | Design B | Design C |
| --- | ---: | ---: | ---: | ---: |
| 4,000 | 0.30 | 120,000 | 130,000 | 120,000 |
| 7,000 | 0.50 | 255,000 | 295,000 | 300,000 |
| 10,000 | 0.20 | 390,000 | 460,000 | 480,000 |

The best profits by state are 130,000, 300,000, and 480,000. Therefore the loss rows are A: 10,000, 45,000, 90,000; B: 0, 5,000, 20,000; and C: 10,000, 0, 0. Weighting gives EOLs 43,500, 6,500, and 3,000, so design C minimizes EOL. If the task instead provides costs without converting them to profit, use the minimum cost in each column as the benchmark.

The profit formula can be checked from the wording. For Design B at 4,000 sales, contribution after variable cost is $(75-20)(4{,}000)=220{,}000$; subtract the 90,000 fixed cost to obtain 130,000 profit. For Design C at 10,000 sales, $(75-15)(10{,}000)-120{,}000=480{,}000$. Once every payoff is net profit, take the best profit in each sales column and subtract other designs’ profits from it. The resulting EOLs are

$$
EOL(A)=0.30(10{,}000)+0.50(45{,}000)+0.20(90{,}000)=43{,}500,
$$

$$
EOL(B)=0.30(0)+0.50(5{,}000)+0.20(20{,}000)=6{,}500,
$$

$$
EOL(C)=0.30(10{,}000)+0.50(0)+0.20(0)=3{,}000.
$$

Design C has the smallest expected loss, so it is selected. This exercise illustrates why the decision variable and payoff definition must be established before the opportunity-loss step: a cost input becomes part of the profit calculation, and the loss table is then built from the profit outcomes.

## 5. Interpretation and relation to EMV

EOL is an expected amount of forgone payoff, not the payoff itself. Lower is better. The calculation uses the probability of each state, not the probability of each decision. If the probabilities change, the EOLs can change and a different action may become optimal.

Under the same payoff table and probabilities, EMV and EOL are linked. For each action, its expected payoff plus its expected opportunity loss equals the expected payoff under perfect information (EPPI). Therefore minimizing EOL selects the same act as maximizing EMV, and the minimum EOL equals EVPI. Topic 224 derives this relationship and its conditions in detail.

Do not confuse EOL with the maximum regret used in the minimax-regret criterion. EOL averages losses using probabilities; minimax regret compares row worst cases without weighting states.

The source’s advertising-budget activity gives another complete example. Payoffs are in millions of dollars, and the four state probabilities are 0.20, 0.25, 0.40, and 0.15:

| State | High advertising | Average advertising | Low advertising |
| --- | ---: | ---: | ---: |
| Severe recession | -10 | -6 | 0 |
| Mild recession | -5 | -1 | 1 |
| Weak recovery | 4 | 3 | 2 |
| Strong recovery | 12 | 9 | 4 |

The column maxima are 0, 1, 4, and 12. The resulting loss rows are high advertising: 10, 6, 0, 0; average advertising: 6, 2, 1, 3; and low advertising: 0, 0, 2, 8. Therefore

$$
EOL(high)=0.20(10)+0.25(6)+0.40(0)+0.15(0)=3.50,
$$

$$
EOL(average)=0.20(6)+0.25(2)+0.40(1)+0.15(3)=2.55,
$$

$$
EOL(low)=0.20(0)+0.25(0)+0.40(2)+0.15(8)=2.00.
$$

Thus low advertising minimizes expected loss. High advertising can be best under a strong recovery, but its lost payoff in recession states matters after those states are weighted. This shows why expected loss combines both the size of the shortfall and the probability of the state.

The same advertising table also shows that EOL is not minimax regret. The maximum regret by action is 10 for high advertising, 6 for average advertising, and 8 for low advertising. Minimax regret therefore selects average advertising because 6 is the smallest worst-case regret. EOL selects low advertising because its probability-weighted average loss is 2.00. The recommendations differ because one method treats the largest regret as decisive while the other uses the full probability distribution.

EOL is measured in the same units as the payoffs, here millions of dollars. If the task gives a budget for additional information, the minimum EOL provides a direct comparison: information that reduces the expected loss by more than its cost may be worthwhile, subject to the information actually being available and reliable. If state probabilities change, recalculate EOL; the loss table itself may stay the same, but its weighted row totals need not.

For payoff maximization, the connection to expected payoff can be derived directly. Let $b_j$ be the best payoff in state $j$. For action $i$,

$$
EOL_i=\sum_jp_j(b_j-a_{ij})
=\sum_jp_jb_j-\sum_jp_ja_{ij}
=EPPI-EMV_i.
$$

The first term does not depend on the chosen action. Therefore an act with greater EMV has smaller EOL under the same payoff table and probabilities. This identity is a useful check on a completed calculation and is explored further in Topic 224.

## 6. Examination checklist and common errors

- Identify whether outcomes are profits/payoffs or costs before choosing a column benchmark.
- Find each column best independently; do not compare row maxima.
- For a payoff, compute best payoff minus actual payoff; for a cost, actual cost minus best (minimum) cost.
- Check that losses are nonnegative and each column has at least one zero.
- Multiply by the matching state probabilities and sum across each alternative.
- Select the smallest EOL and interpret it in the payoff’s units.

Common errors include maximizing EOL, omitting a probability, weighting a row with the wrong state probability, treating an unweighted maximum regret as EOL, and using the highest cost as the benchmark. Always display enough intermediate values to make the final recommendation verifiable.