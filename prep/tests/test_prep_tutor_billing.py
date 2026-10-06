from datetime import datetime, timezone
from decimal import Decimal

from django.test import SimpleTestCase, override_settings

from services.prep_tutor_billing import (
    TutorPricingError,
    calculate_provider_cost,
    is_deepseek_peak_period,
    provider_cost_credits,
)


class TutorPricingTests(SimpleTestCase):
    def test_deepseek_peak_schedule_is_weekday_utc(self):
        self.assertTrue(is_deepseek_peak_period(datetime(2026, 10, 5, 1, tzinfo=timezone.utc)))
        self.assertTrue(is_deepseek_peak_period(datetime(2026, 10, 5, 9, 59, tzinfo=timezone.utc)))
        self.assertFalse(is_deepseek_peak_period(datetime(2026, 10, 5, 4, tzinfo=timezone.utc)))
        self.assertFalse(is_deepseek_peak_period(datetime(2026, 10, 10, 2, tzinfo=timezone.utc)))

    def test_deepseek_cost_counts_cached_input_at_its_separate_rate(self):
        cost = calculate_provider_cost(
            "deepseek",
            "deepseek-flash",
            {
                "prompt_tokens": 1_000_000,
                "prompt_cache_hit_tokens": 100_000,
                "completion_tokens": 200_000,
            },
            at=datetime(2026, 10, 10, 12, tzinfo=timezone.utc),
        )

        self.assertEqual(cost["cache_miss_input_tokens"], 900_000)
        self.assertEqual(cost["cached_input_tokens"], 100_000)
        self.assertEqual(cost["estimated_cost_usd"], "0.25530000")
        self.assertEqual(cost["rate_period"], "off_peak")

    def test_total_only_usage_is_conservatively_priced_as_output(self):
        cost = calculate_provider_cost(
            "deepseek",
            "deepseek-flash",
            {"total_tokens": 100},
            at=datetime(2026, 10, 10, 12, tzinfo=timezone.utc),
        )

        self.assertEqual(cost["input_tokens"], 0)
        self.assertEqual(cost["output_tokens"], 100)
        self.assertEqual(cost["estimated_cost_usd"], "0.00006000")

    def test_together_model_requires_an_explicit_known_price(self):
        with self.assertRaises(TutorPricingError):
            calculate_provider_cost("together", "unpriced-model", {"total_tokens": 100})

    @override_settings(
        PREP_USD_TO_KES_RATE="130",
        PREP_NET_KES_PER_CREDIT="0.75",
        PREP_AI_COST_MARGIN_MULTIPLIER="2",
    )
    def test_cost_conversion_rounds_up_and_respects_minimum(self):
        cost = {"estimated_cost_usd": "0.01"}
        self.assertEqual(provider_cost_credits(cost), 4)
        self.assertEqual(
            provider_cost_credits({"estimated_cost_usd": "0"}, minimum=3),
            3,
        )

    @override_settings(PREP_NET_KES_PER_CREDIT="0")
    def test_invalid_credit_conversion_setting_fails_explicitly(self):
        with self.assertRaises(TutorPricingError):
            provider_cost_credits({"estimated_cost_usd": "0.01"})
