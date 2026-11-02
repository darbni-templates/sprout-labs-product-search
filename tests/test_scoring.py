from shop_search.scoring import score_product

PRODUCT = {"title": "Blue mug", "tags": ["kitchen"], "description": "A mug."}


def test_no_words_no_score():
    assert score_product([], PRODUCT) == 0


def test_unrelated_word_scores_zero():
    assert score_product(["zzz"], PRODUCT) == 0
