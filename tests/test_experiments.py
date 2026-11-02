from shop_search.experiments import ab_report


def test_no_events_is_not_enough_data():
    assert ab_report([])["winner"] == "not_enough_data"
