import json


def load_catalog(json_text: str) -> list[dict]:
    """Read a shop's product catalog (a JSON list of products from the shop platform)."""
    products = json.loads(json_text)
    catalog = []
    for p in products:
        catalog.append(
            {
                "id": p["id"],
                "title": p["title"].strip(),
                "tags": [t.strip().lower() for t in p["tags"]],
                "description": p["description"].strip(),
                "price_cents": p["price_cents"],
            }
        )
    return catalog
