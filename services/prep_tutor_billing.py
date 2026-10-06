"""Provider-specific pricing and credit estimates for topic tutor requests."""

from __future__ import annotations

import logging
import math
from datetime import datetime, timezone as datetime_timezone
from decimal import Decimal, InvalidOperation, ROUND_CEILING

from django.conf import settings

logger = logging.getLogger(__name__)

_DEEPSEEK_RATES_USD_PER_MILLION = {
    "deepseek-flash": {
        "off_peak": {"input": "0.15", "cached_input": "0.003", "output": "0.60"},
        "peak": {"input": "0.30", "cached_input": "0.006", "output": "1.20"},
    },
    "deepseek-v4-pro": {
        "off_peak": {"input": "0.66", "cached_input": "0.022", "output": "1.98"},
        "peak": {"input": "1.32", "cached_input": "0.044", "output": "3.96"},
    },
}
_TOGETHER_RATES_USD_PER_MILLION = {
    "deepseek-ai/deepseek-v4.1-flash": {
        "input": "0.30",
        "cached_input": "0.006",
        "output": "1.20",
    },
}
_MILLION = Decimal("1000000")


class TutorPricingError(ValueError):
    """Raised when pricing inputs or deployment conversion settings are invalid."""


def is_deepseek_peak_period(at: datetime | None = None) -> bool:
    """DeepSeek peak schedule: weekdays 01-04 and 06-10 UTC."""
    now = at or datetime.now(datetime_timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=datetime_timezone.utc)
    now = now.astimezone(datetime_timezone.utc)
    return now.weekday() < 5 and (
        1 <= now.hour < 4 or 6 <= now.hour < 10
    )


def _decimal_setting(name: str, default: str) -> Decimal:
    try:
        value = Decimal(str(getattr(settings, name, default)))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise TutorPricingError(f"{name} must be a valid decimal number.") from exc
    if not value.is_finite() or value <= 0:
        raise TutorPricingError(f"{name} must be greater than zero.")
    return value


def _deepseek_rate_key(model_name: str) -> str:
    model = str(model_name or "").strip().casefold()
    if "pro" in model or "reason" in model or model == "deepseek-r1":
        return "deepseek-v4-pro"
    if "flash" in model or model in {"deepseek-chat", "deepseek-v3"}:
        return "deepseek-flash"
    logger.warning(
        "Unknown DeepSeek tutor model %r; pricing it at the highest configured DeepSeek rate.",
        model_name,
    )
    return "deepseek-v4-pro"


def _usage_token_counts(usage: dict | None) -> dict:
    """Normalize DeepSeek/Together usage fields, including cached prompt tokens."""
    usage = usage if isinstance(usage, dict) else {}
    prompt_details = usage.get("prompt_tokens_details")
    if not isinstance(prompt_details, dict):
        prompt_details = usage.get("input_tokens_details")
    if not isinstance(prompt_details, dict):
        prompt_details = {}

    prompt_tokens = int(usage.get("prompt_tokens") or usage.get("input_tokens") or 0)
    cached_tokens = int(
        usage.get("prompt_cache_hit_tokens")
        or usage.get("cached_prompt_tokens")
        or usage.get("cached_tokens")
        or prompt_details.get("cached_tokens")
        or prompt_details.get("cache_read_tokens")
        or 0
    )
    cache_miss_tokens = int(usage.get("prompt_cache_miss_tokens") or 0)
    if cache_miss_tokens and not prompt_tokens:
        prompt_tokens = cached_tokens + cache_miss_tokens
    elif prompt_tokens and cache_miss_tokens:
        cached_tokens = max(0, prompt_tokens - cache_miss_tokens)
    cached_tokens = min(prompt_tokens, max(0, cached_tokens))
    output_tokens = int(usage.get("completion_tokens") or usage.get("output_tokens") or 0)
    if not prompt_tokens and not output_tokens:
        total = int(usage.get("total_tokens") or 0)
        # Without a prompt/output split, price every token at the higher output
        # rate rather than accidentally undercharging an output-heavy request.
        output_tokens = total
    return {
        "input_tokens": prompt_tokens,
        "cached_input_tokens": cached_tokens,
        "cache_miss_input_tokens": max(0, prompt_tokens - cached_tokens),
        "output_tokens": output_tokens,
        "total_tokens": prompt_tokens + output_tokens,
    }


def calculate_provider_cost(
    provider: str,
    model_name: str,
    usage: dict | None,
    *,
    at: datetime | None = None,
    force_peak: bool = False,
) -> dict:
    """Return exact configured token rates and estimated provider USD cost."""
    provider_key = str(provider or "").strip().casefold()
    model_key = str(model_name or "").strip().casefold()
    tokens = _usage_token_counts(usage)
    peak = force_peak or is_deepseek_peak_period(at)
    if provider_key == "deepseek":
        rate_key = _deepseek_rate_key(model_key)
        rate_period = "peak" if peak else "off_peak"
        rates = _DEEPSEEK_RATES_USD_PER_MILLION[rate_key][rate_period]
    elif provider_key == "together":
        rate_key = next(
            (
                known
                for known in _TOGETHER_RATES_USD_PER_MILLION
                if known == model_key
            ),
            None,
        )
        if rate_key is None:
            raise TutorPricingError(
                f"No configured Together pricing for tutor model {model_name!r}."
            )
        rate_period = "standard"
        rates = _TOGETHER_RATES_USD_PER_MILLION[rate_key]
    else:
        raise TutorPricingError(f"Unsupported tutor provider: {provider!r}.")

    input_rate = Decimal(rates["input"])
    cached_rate = Decimal(rates["cached_input"])
    output_rate = Decimal(rates["output"])
    cost_usd = (
        Decimal(tokens["cache_miss_input_tokens"]) * input_rate
        + Decimal(tokens["cached_input_tokens"]) * cached_rate
        + Decimal(tokens["output_tokens"]) * output_rate
    ) / _MILLION
    return {
        **tokens,
        "provider": provider_key,
        "model": model_name,
        "pricing_model": rate_key,
        "rate_period": rate_period,
        "is_peak": peak if provider_key == "deepseek" else False,
        "rates_usd_per_million": {
            "input": str(input_rate),
            "cached_input": str(cached_rate),
            "output": str(output_rate),
        },
        "estimated_cost_usd": str(cost_usd.quantize(Decimal("0.00000001"))),
    }


def provider_cost_credits(cost: dict, *, minimum: int = 1) -> int:
    """Convert provider USD cost to credits with configured FX and margin."""
    usd_to_kes = _decimal_setting("PREP_USD_TO_KES_RATE", "130")
    net_kes_per_credit = _decimal_setting("PREP_NET_KES_PER_CREDIT", "0.75")
    margin = _decimal_setting("PREP_AI_COST_MARGIN_MULTIPLIER", "2")
    cost_kes = Decimal(str(cost["estimated_cost_usd"])) * usd_to_kes
    billable_kes = cost_kes * margin
    credits = int((billable_kes / net_kes_per_credit).to_integral_value(rounding=ROUND_CEILING))
    return max(int(minimum), credits)


def estimate_chat_reservation(
    system_prompt: str,
    user_prompt: str,
    model_name: str,
    *,
    output_token_cap: int,
) -> tuple[int, dict]:
    """Conservatively reserve peak-priced, uncached input plus capped output."""
    text_tokens = math.ceil((len(system_prompt) + len(user_prompt)) / 3.5)
    multiplier = _decimal_setting("PREP_CHAT_RESERVE_MULTIPLIER", "2")
    input_reserve = int(
        (Decimal(text_tokens) * multiplier).to_integral_value(rounding=ROUND_CEILING)
    )
    output_reserve = int(
        (Decimal(max(1, output_token_cap)) * multiplier).to_integral_value(rounding=ROUND_CEILING)
    )
    quote = calculate_provider_cost(
        "deepseek",
        model_name,
        {
            "prompt_tokens": input_reserve,
            "completion_tokens": output_reserve,
        },
        force_peak=True,
    )
    quote["reservation_input_tokens"] = input_reserve
    quote["reservation_output_tokens"] = output_reserve
    return provider_cost_credits(quote), quote


def quote_summary(quote: dict, credits: int) -> dict:
    """Create JSON-safe pricing evidence to persist on ledger rows."""
    return {
        **quote,
        "usd_to_kes_rate": str(_decimal_setting("PREP_USD_TO_KES_RATE", "130")),
        "net_kes_per_credit": str(_decimal_setting("PREP_NET_KES_PER_CREDIT", "0.75")),
        "cost_margin_multiplier": str(
            _decimal_setting("PREP_AI_COST_MARGIN_MULTIPLIER", "2")
        ),
        "credits_charged": int(credits),
    }
