"""Cost calculation and formatting helpers."""

SMALL_COST_THRESHOLD = 0.001


def calculate_cost(
    input_tokens: int, output_tokens: int, input_price: float, output_price: float
) -> float:
    """Return the dollar cost for the given token counts and per-token prices."""
    return input_tokens * input_price + output_tokens * output_price


def format_cost(cost: float) -> str:
    """Format a dollar cost, using extra decimal places for very small amounts."""
    if cost < SMALL_COST_THRESHOLD:
        return f"${cost:.6f}"
    return f"${cost:.4f}"
