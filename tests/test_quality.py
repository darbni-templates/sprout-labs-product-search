from shop_search.quality import evaluate_search


def test_perfect_results():
    result = evaluate_search([["p1"]], [["p1"]])
    assert result["mrr"] == 1.0
