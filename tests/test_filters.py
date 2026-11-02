from shop_search.filters import filter_by_price

MUG = {"id": "p1", "price_cents": 1200}


def test_no_limits():
    assert filter_by_price([MUG]) == [MUG]


def test_inside_the_range():
    assert filter_by_price([MUG], 1000, 1500) == [MUG]
