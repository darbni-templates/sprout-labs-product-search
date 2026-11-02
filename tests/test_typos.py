from shop_search.typos import closest_words


def test_empty_vocabulary():
    assert closest_words("mug", []) == []


def test_unrelated_word():
    assert closest_words("mug", ["blanket"]) == []
