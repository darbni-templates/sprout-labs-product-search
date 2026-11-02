from shop_search.display import display_title


def test_short_title_is_unchanged():
    assert display_title("Blue mug") == "Blue mug"
