from shop_search.synonyms import expand_query


def test_no_words():
    assert expand_query([]) == []


def test_word_without_synonyms_stays():
    assert expand_query(["zzz"]) == ["zzz"]
