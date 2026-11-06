## 1. Why use a decision tree?

A payoff table represents one decision followed by one state. Some problems have several stages: choose an action, observe an uncertain event, and then make another decision. A decision tree displays that sequence and keeps the alternatives, probabilities, and final outcomes in their correct order.

The tree is evaluated by **rollback** or **foldback**: start at the terminal outcomes and work from right to left toward the initial decision. At a chance node, calculate the probability-weighted expected value of its branches. At a decision node, select the branch with the best value for the stated objective. For profit, choose the larger value; for cost or time, choose the smaller value.

## 2. Components and construction

A standard decision tree uses:

- a decision node (commonly a square) where the decision maker chooses an action;
- a chance node (commonly a circle) where one of several states occurs with stated probabilities;
- branches that label actions or events;
- terminal endpoints that show the final payoff, cost, or net present value.

To draw one:

1. Define the decision and alternatives at the left of the page.
2. From each alternative, add the chance events that can follow, with probabilities that sum to one at each chance node.
3. Add any later decision nodes after the relevant information is observed.
4. Continue until each complete path ends in a payoff.
5. Include every cost exactly once. If a cost is already included in a net payoff, do not subtract it again during rollback.

The order of nodes matters. A decision made before an event cannot use information from that event. If the event is observed before a later choice, represent that later choice after the chance node.

A path through a tree is one complete scenario: it begins with an initial choice, follows one possible outcome at each chance node, includes any later action selected after that outcome, and ends at one terminal payoff. The tree should include all paths that can actually occur, but not combinations that are logically impossible. At a chance node, each branch probability is conditional on reaching that node; the outgoing probabilities must sum to one. If a later node is reached only after a particular earlier outcome, do not mix its probabilities with those of a different branch.

When a decision follows an observed outcome, solve that later decision before calculating the expected value of the earlier chance node. This is the essential reason rollback proceeds from right to left. The best future action may differ between branches, and the initial decision should receive the value of the best policy available after each event.

## 3. Rollback calculations

At a chance node with outcomes $x_j$ and probabilities $p_j$, its expected value is

$$
EV=\sum_j p_jx_j.
$$

At a decision node, compare the values of the available branches and keep the best one. Then carry that selected value backward to the previous node. This procedure captures the optimal policy: a conditional action may be chosen differently for different states or signals observed earlier.

An expected value at a chance node is not a guaranteed outcome. It is the value used to compare branches under the supplied probabilities. If probabilities or payoffs are missing, the tree is incomplete and should not be evaluated as if the missing data were known.

## 4. Worked example: hire a mechanic?

Joe’s garage can hire a mechanic for an additional annual cost of USD 50,000 or leave the operation unchanged. If it does not hire, use a baseline incremental payoff of USD 0. If it hires, the source solution uses a payoff of USD 70,000 when accidents are numerous (probability 0.70) and -USD 20,000 when accidents are few (probability 0.30). The expected net value of hiring is

$$
0.70(70{,}000)+0.30(-20{,}000)-50{,}000
=49{,}000-6{,}000-50{,}000=-7{,}000.
$$

The decision node compares -USD 7,000 from hiring with USD 0 from not hiring, so rollback recommends not hiring.

There is a discrepancy in the source: the example introduction says the high-accident additional revenue is USD 75,000, while its solution uses USD 70,000. Using the introduction’s figure gives

$$
0.70(75{,}000)+0.30(-20{,}000)-50{,}000=-3{,}500.
$$

Both values still favor not hiring; a careful answer notes which figure is used.

Read the garage tree from the terminal outcomes backward. The “do not hire” branch has an incremental payoff of zero. Under the solution’s 70,000 figure, the chance node for hiring has expected additional revenue $0.70(70{,}000)+0.30(-20{,}000)=43{,}000$. Subtracting the annual 50,000 mechanic cost gives -7,000. The decision node compares -7,000 with 0 and selects “do not hire.” If the introductory 75,000 figure is used, expected additional revenue is 46,500 and net value is -3,500, so the first decision is unchanged. The discrepancy changes the size of the loss but not the recommended action.

Do not treat the chance-node average, 43,000, as the final branch value before charging the salary. Nor should the salary be subtracted once from every terminal payoff and again after averaging; either approach is valid if the cost is included exactly once. Labeling terminal payoffs as incremental profit makes this check easier.

## 5. Multi-stage example: the quarry

Tom and Joe can sell the quarry now for USD 50,000 or keep it for two years. If they keep it, demand has a 0.60 chance of increasing and a 0.40 chance of not increasing. If demand increases, they can operate for USD 75,000 profit or sell to a new buyer for USD 60,000; choose operation at that later decision node because 75,000 is larger. If demand does not increase, they can sell to the current buyer for USD 30,000 or operate for USD 10,000; choose the 30,000 sale.

Rollback at the chance node for keeping gives

$$
EV(keep)=0.60(75{,}000)+0.40(30{,}000)=57{,}000.
$$

Compare this with USD 50,000 for selling now. Under the stated payoffs and probabilities, keeping has the higher expected value. The key is that the later choices are optimized separately after observing demand; evaluating “keep” using one fixed action at both later nodes would miss the flexibility represented by the tree.

The rollback can be displayed in three stages:

1. After increased demand, compare operating for 75,000 with selling for 60,000; retain the operating branch worth 75,000.
2. After no increase, compare operating for 10,000 with selling to the current buyer for 30,000; retain the sale branch worth 30,000.
3. Before demand is known, weight those retained branch values: $0.60(75{,}000)+0.40(30{,}000)=57{,}000$. Compare that with 50,000 from selling now.

The contingent plan is therefore “keep; operate if demand increases; sell to the current buyer if it does not.” This is more informative than simply saying “keep,” because it specifies what to do at the later decision nodes.

The value of that flexibility can be seen by comparing it with a restricted plan that must commit to one later action regardless of demand. If the owners promise to operate in either state, the expected profit from keeping is $0.60(75{,}000)+0.40(10{,}000)=49{,}000$, below the 50,000 available now. If they commit to selling in both states, the later sale values are 60,000 after an increase and 30,000 otherwise, with expected value 48,000. The tree’s 57,000 results from choosing the better action after observing the state; it is not achieved by either fixed commitment.

For a general increase probability $p$, the flexible keep strategy is worth $75{,}000p+30{,}000(1-p)=30{,}000+45{,}000p$. It exceeds the 50,000 current offer when $p>4/9$. The source estimate is $p=0.60$, so keeping is preferred. This threshold is a sensitivity check, not a substitute for drawing the tree.

### Vegetable Farms activity

The module also gives a two-action, three-state problem. Same-size acreage has payoffs 50,000, 40,000, and 30,000 under high, medium, and low demand. Expanded acreage has payoffs 100,000, 40,000, and -40,000. The probabilities are 0.50, 0.30, and 0.20. The tree has one initial decision node followed by a demand chance node on each action branch. The EMVs are

$$
EMV(same)=0.50(50{,}000)+0.30(40{,}000)+0.20(30{,}000)=43{,}000,
$$

$$
EMV(expand)=0.50(100{,}000)+0.30(40{,}000)+0.20(-40{,}000)=54{,}000.
$$

Rollback therefore selects expand under the stated expected-value objective. The low-demand loss of -40,000 must remain negative; changing it to a gain would overstate the expansion value by 16,000 in the probability-weighted total.

## 6. Exam method and common mistakes

1. Draw the tree in chronological/information order, with decisions before the events they cannot yet observe.
2. Put probabilities on chance branches and verify each chance-node total is 1.
3. Label terminal values as profit, cost, or incremental NPV, and keep units consistent.
4. Start at the far right. Calculate chance-node expected values and write them beside the nodes.
5. At every decision node, select the branch consistent with the objective and mark the rejected alternatives.
6. Continue rolling back until the initial decision is reached; state the full contingent policy, not only the first branch.
7. Check whether fixed costs are already included and whether source inputs conflict with the solution.

Common errors include summing chance payoffs without probabilities, averaging over branches with unequal probabilities, subtracting a cost twice, maximizing when the problem asks for minimum cost, selecting a decision before rolling back its future consequences, and treating an expected value as a guaranteed payoff. A tree is useful only when its branches preserve what is known at each decision point.