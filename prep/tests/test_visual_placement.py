from django.test import SimpleTestCase

from services.prep_ai_router import _insert_required_visual_markers


class ApprovedVisualPlacementTests(SimpleTestCase):
    def test_figure_is_placed_after_its_whole_explanatory_subsection(self):
        content = """## 2. Graphical Analysis

### 2.1 Production Possibilities Frontier

The frontier shows attainable combinations of beans and maize under the available resources.

The curve becomes concave as increasing opportunity cost means progressively more maize is sacrificed.

### 2.2 Worked Calculation

Problem. Given the demand and supply functions, find the equilibrium quantity.

$$Q_d = 100 - 2P$$

Substituting the supply function and solving gives the equilibrium.
"""
        manifest = [{
            "id": "ppf-figure",
            "marker": "[[VISUAL:ppf-figure]]",
            "crop_url": "/cdn/assets/ppf-figure.jpg",
            "caption": "Concave production possibility frontier showing increasing opportunity cost",
            "labels": ["beans", "maize", "PPF"],
            "auto_match_terms": ["concave", "increasing opportunity cost"],
            "placement_context": "The curve becomes concave as increasing opportunity cost rises.",
            "context_before": "",
            "context_after": "",
            "required": False,
        }]
        content = content.replace(
            "The curve becomes concave",
            "The curve becomes concave [[VISUAL:ppf-figure]]",
        )

        updated = _insert_required_visual_markers(content, manifest)

        image_position = updated.index("[[VISUAL:ppf-figure]]")
        subsection_position = updated.index("### 2.2 Worked Calculation")
        self.assertGreater(
            image_position,
            updated.index("progressively more maize is sacrificed."),
        )
        self.assertLess(image_position, subsection_position)
        self.assertIn("Problem. Given the demand and supply functions", updated)
        self.assertLess(
            updated.index("### 2.2 Worked Calculation"),
            updated.index("Problem. Given the demand and supply functions"),
        )

    def test_figure_uses_specific_explanation_not_generic_topic_intro(self):
        content = """## 1. Core Ideas

### 1.1 Price Theory

Price theory explains how demand and supply interact to determine market prices.

### 1.2 Market Stability

> **Definition (Unstable Equilibrium).** A market can move further from equilibrium when a disturbance occurs, including when labour supply slopes downward for target workers.

### 1.3 Worked Example

Problem. Given the demand and supply functions, calculate the equilibrium.
"""
        manifest = [{
            "id": "labor-supply",
            "marker": "[[VISUAL:labor-supply]]",
            "crop_url": "/cdn/assets/labor-supply.jpg",
            "caption": "Downward-sloping abnormal labor supply curve for target workers",
            "labels": ["Wages", "Hours worked"],
            "auto_match_terms": ["demand", "price", "supply", "theory"],
            "placement_context": "Target workers set an income goal before reducing hours.",
            "context_before": "",
            "context_after": "",
            "required": False,
        }]
        content = content.replace(
            "Price theory explains",
            "Price theory [[VISUAL:labor-supply]] explains",
        )

        updated = _insert_required_visual_markers(content, manifest)

        image_position = updated.index("[[VISUAL:labor-supply]]")
        stability_position = updated.index("### 1.2 Market Stability")
        worked_example_position = updated.index("### 1.3 Worked Example")
        self.assertGreater(image_position, stability_position)
        self.assertLess(image_position, worked_example_position)

    def test_figure_in_problem_waits_until_the_whole_solution_finishes(self):
        content = """## 4. Worked Example

### 4.1 Problem

The demand schedule gives a list of market prices and corresponding quantities demanded for each price level in this exercise.

### 4.2 Step-by-Step Solution

Set quantity demanded equal to quantity supplied, then solve for the equilibrium price.

### 4.3 Interpretation

At this price, the market clears and the equilibrium quantity is established.

## 5. Key Takeaways
"""
        manifest = [{
            "id": "demand-schedule",
            "marker": "[[VISUAL:demand-schedule]]",
            "crop_url": "/cdn/assets/demand-schedule.jpg",
            "caption": "Individual demand schedule table listing market prices and quantities demanded",
            "labels": ["Price", "Quantity demanded"],
            "auto_match_terms": ["price", "demand"],
            "placement_context": "Demand schedule table with price and quantity columns.",
            "context_before": "",
            "context_after": "",
            "required": False,
        }]
        content = content.replace(
            "The demand schedule gives",
            "The demand schedule [[VISUAL:demand-schedule]] gives",
        )

        updated = _insert_required_visual_markers(content, manifest)

        image_position = updated.index("[[VISUAL:demand-schedule]]")
        self.assertGreater(
            image_position,
            updated.index("At this price, the market clears"),
        )
        self.assertLess(image_position, updated.index("## 5. Key Takeaways"))
