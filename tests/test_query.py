from shop_search.query import tokenize_query


def test_empty_query():
    assert tokenize_query("") == []


def test_lowercase_words():
    assert tokenize_query("Blue MUG") == ["blue", "mug"]
