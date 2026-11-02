def search(query: str, products: list[dict]) -> list[str]:
    """Find products for a shopper's query. Returns up to 10 product ids, best first."""
    words = query.lower().split()
    scored = []
    for p in products:
        score = 0
        title = p["title"].lower()
        for w in words:
            if w in title.split():
                score = score + 3
            if w in [t.lower() for t in p.get("tags", [])]:
                score = score + 1
        scored.append(
            {"id": p["id"], "score": score, "price_cents": p["price_cents"], "title": p["title"]}
        )
    # sort: best score first, then cheaper first, then by title
    result = []
    for item in sorted(scored, key=lambda s: (-s["score"], s["price_cents"], s["title"].lower())):
        if item["score"] > 0:
            result.append(item["id"])
    return result[:10]
