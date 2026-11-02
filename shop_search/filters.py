def filter_by_price(
    products: list[dict], min_cents: int | None = None, max_cents: int | None = None
) -> list[dict]:
    """The products whose price_cents is between min_cents and max_cents (both inclusive).
    None means no limit on that side."""
    result = []
    for p in products:
        if min_cents is not None and p["price_cents"] < min_cents:
            continue
        if max_cents and p["price_cents"] >= max_cents:
            continue
        result.append(p)
    return result
