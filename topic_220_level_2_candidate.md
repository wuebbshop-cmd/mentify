## 1. Regret as a state-by-state comparison

Decision making under regret evaluates an alternative by comparing its outcome with the best outcome that could have been obtained in the same state of nature. Regret is also called opportunity loss: it is the payoff forgone because another alternative would have done better after the state is known. The decision maker does not know the state in advance; the comparison is constructed separately within each state column.

For payoff maximization, the regret for act $i$ in state $j$ is

$$
R_{ij}=\max_k(a_{kj})-a_{ij}.
$$

Thus the best payoff in each column receives zero regret, and other acts receive nonnegative regret. The minimax-regret rule then controls the largest regret each act could incur.

## 2. Minimax-regret procedure

Use this sequence:

1. Build the payoff table with alternatives as rows and states as columns.
2. In each state column, identify the best payoff among all alternatives.
3. Subtract each cell payoff from that state’s best payoff to form the regret table.
4. Find the maximum regret in each alternative row.
5. Choose the alternative with the smallest row maximum.

The criterion can be written as

$$
R_i^{max}=\max_j R_{ij},\qquad
\text{choose }i\text{ minimizing }R_i^{max}.
$$

It is a conservative rule, but the quantity it protects is regret, not the worst payoff. Do not confuse minimax regret with maximin payoff: maximin compares row minima in the original payoff table; minimax regret first transforms every column into opportunity losses.

The transformation is column-based because the regret question is conditional on the state that actually occurs. Once the state is fixed, compare all available actions under that same state and identify the best one. A row-based benchmark would compare an action with its own performance in other states, which answers a different question. The zero in each regret column is therefore a diagnostic: it marks the action that would have been best with hindsight for that state.

## 3. Worked investment example

The source uses the following returns for bonds, stock, and deposits:

| Strategy | High growth | Medium growth | No change | Low growth |
| --- | ---: | ---: | ---: | ---: |
| Bonds | 12 | 8 | 7 | 3 |
| Stock | 15 | 5 | 5 | -2 |
| Deposits | 7 | 7 | 7 | 7 |

The best payoff in each state is 15, 8, 7, and 7. Subtract each payoff from its column maximum:

| Strategy | High growth | Medium growth | No change | Low growth | Maximum regret |
| --- | ---: | ---: | ---: | ---: | ---: |
| Bonds | 3 | 0 | 0 | 4 | 4 |
| Stock | 0 | 3 | 2 | 9 | 9 |
| Deposits | 8 | 1 | 0 | 0 | 8 |

Bonds has the smallest maximum regret, 4, so minimax regret selects bonds. This differs from maximax (stock) and maximin (deposits). The conclusion reflects the regret criterion, not a mistake: each rule answers a different decision question.

The calculation can be checked column by column. Under high growth, stock’s 15 is the best return, so bonds regret 3 and deposits regret 8. Under medium growth, bonds’ 8 is best, so stock regrets 3 and deposits regret 1. Under no change, bonds and deposits tie at 7, so both have zero regret and stock regrets 2. Under low growth, deposits’ 7 is best; bonds regret 4 and stock regrets 9. The maximum regret for each act is then read across the completed row: 4, 9, and 8. Selecting the smallest of these worst cases yields bonds.

Compare this result with the original payoff criteria. Maximax selects stock because its best return is 15. Maximin selects deposits because their worst return is 7. Minimax regret selects bonds because its largest shortfall from a statewise best is only 4. These recommendations are not contradictory: they measure different notions of protection. Maximin protects realized payoff; minimax regret protects against looking back and seeing a large avoidable loss.

## 4. Cost outcomes require the opposite column benchmark

The rule “column maximum minus cell” applies when larger payoffs are better. For a cost table, lower is better, so opportunity loss is

$$
R_{ij}=c_{ij}-\min_k(c_{kj}),
$$

where $c_{ij}$ is the cost of act $i$ in state $j$. For each state, subtract the smallest cost from each alternative’s cost, then minimize each row’s maximum regret.

The module’s telecommunications activity gives annual costs in thousands of shillings:

| Staffing option | High demand | Average demand | Low demand |
| --- | ---: | ---: | ---: |
| Own staff | 650 | 900 | 800 |
| Outsource | 650 | 600 | 650 |
| Combination | 600 | 300 | 500 |

The minimum costs by state are 600, 300, and 500. The correct opportunity-loss table is:

| Staffing option | High demand | Average demand | Low demand | Maximum regret |
| --- | ---: | ---: | ---: | ---: |
| Own staff | 50 | 600 | 300 | 600 |
| Outsource | 50 | 300 | 150 | 300 |
| Combination | 0 | 0 | 0 | 0 |

The minimax-regret recommendation is the combination option. The source also reproduces a printed table that incorrectly uses the payoff rule (largest cost minus each cost), which would give a misleading choice. The objective must be checked before computing regret.

The difference is visible in the high-demand state. The lowest cost is 600, so the combination option has zero loss and the two 650 options each have loss 50. In the average-demand state, 300 is the lowest cost, so own staff loses 600, outsourcing loses 300, and combination loses zero. In the low-demand state, the minimum is 500, giving losses 300, 150, and zero. The worst regrets are therefore 600 for own staff, 300 for outsourcing, and zero for combination. If the “largest cost minus cell” rule were used, the comparison would reward higher costs and reverse the meaning of the problem.

This example is also a practical reminder that the word “regret” does not always mean “best payoff minus chosen payoff.” It means the loss relative to the best feasible outcome for the state. For profit, the best outcome is the maximum; for cost, it is the minimum. The objective defines the benchmark.

## 5. Relation to expected opportunity loss

Minimax regret does not require probabilities. It uses the worst regret in each row, then chooses the smallest such worst case. If probabilities are available and the requested objective is expected opportunity loss, calculate a probability-weighted average for each alternative instead. These two criteria may select different acts because one emphasizes a maximum and the other an average.

For a payoff table, the EOL of act $i$ is $\sum_j p_jR_{ij}$. In the investment table above, probabilities are not supplied for the regret calculation, so do not compute EOL unless a later part gives them. The minimax rule remains valid without probabilities, provided the regret table is constructed from the correct column bests.

The difference can be written explicitly. Minimax regret chooses

$$
\arg\min_i\max_jR_{ij},
$$

whereas expected opportunity loss chooses

$$
\arg\min_i\sum_jp_jR_{ij}.
$$

The first calculation is driven by the single worst regret for each act; the second incorporates every regret and weights it by its probability. A rare state with a very large regret can control the minimax result but contribute relatively little to EOL. Conversely, a moderately large regret in a very likely state can dominate EOL.

Regret rankings have useful scale properties. Adding the same constant to every payoff in a state column leaves that column’s regret values unchanged, because both the column best and every cell move by the same amount. Multiplying all payoffs by the same positive factor multiplies all regrets by that factor but does not change the minimax choice. These properties can help detect arithmetic mistakes: a common statewise offset should not alter the regret table.

Minimax regret is also sensitive to which alternatives are feasible. Adding a new act that becomes the best payoff in one state raises the regret of the existing acts in that column, even though their original payoffs did not change. Therefore the feasible action set must be defined before the regret table is built; adding an impossible or irrelevant alternative can distort the benchmark. A strictly dominated payoff row can be removed without affecting the column bests if it never exceeds another act, but a newly introduced act that is best in any state changes the comparison.

The criterion is most useful when probabilities are unavailable or the decision maker wants a transparent limit on hindsight loss. It does not claim that every state is equally likely, and it does not minimize the expected loss unless that separate calculation is requested. The decision maker should report the largest regret of the selected act and, when relevant, compare it with the worst-regret values of the alternatives. This makes the degree of protection visible rather than hiding it behind the chosen label.

## 6. Examination checklist and pitfalls

- Preserve the original table’s objective: maximize profit/payoff or minimize cost.
- Determine the best outcome separately for every state, not separately for every act.
- For a payoff, subtract each cell from the column maximum; for a cost, subtract the column minimum from each cell.
- Verify that every regret is nonnegative and that at least one entry in every state column is zero.
- Find each row maximum only after completing the regret table.
- Select the smallest row maximum and state the corresponding alternative.

Common errors are subtracting row maxima instead of column maxima, choosing the largest rather than smallest maximum regret, treating regret as a negative payoff, comparing expected regret without probabilities, and applying a payoff maximization rule to a cost table. Show the column benchmarks and the row maxima in the working so the decision is auditable.