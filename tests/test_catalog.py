import json

from shop_search.catalog import load_catalog


def test_one_product():
    text = json.dumps(
        [{"id": "p1", "title": " Mug ", "tags": ["Kitchen"], "description": "Blue.", "price_cents": 900}]
    )
    assert load_catalog(text) == [
        {"id": "p1", "title": "Mug", "tags": ["kitchen"], "description": "Blue.", "price_cents": 900}
    ]
