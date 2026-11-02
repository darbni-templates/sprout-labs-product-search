from shop_search.search import rank_results


def test_best_score_first():
    scored = [
        {"id": "a", "score": 1, "price_cents": 100, "title": "A"},
        {"id": "b", "score": 5, "price_cents": 100, "title": "B"},
    ]
    assert rank_results(scored) == ["b", "a"]
