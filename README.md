# Sprout Labs product search

Shoppers ask the chatbot for products ("blue mug under 15", "wool socks"), and this search
finds them in the shop's catalog. It works, but shop owners keep asking for changes: smarter
matching, better ranking, and proof that the changes help. That's this project.

## Your tasks
**Your exact task is in Darbni.** Open the task there and read its description: it has the
rules for YOUR version. Every intern gets their own version of each task, so a solution
copied from someone else will fail the tests.

Most tasks change code that already exists. Read it first.

## Where things are
| File | What it does |
|---|---|
| `shop_search/query.py` | turns the shopper's query into words |
| `shop_search/synonyms.py` | adds synonyms to the query |
| `shop_search/typos.py` | finds the word the shopper probably meant |
| `shop_search/catalog.py` | reads a shop's product catalog |
| `shop_search/filters.py` | price filters |
| `shop_search/display.py` | how product titles look in the chat |
| `shop_search/scoring.py` | how well a product matches a query |
| `shop_search/search.py` | the search itself: score, rank, return the best |
| `shop_search/quality.py` | measures search quality on labelled queries |
| `shop_search/experiments.py` | A/B test reports |

## Run the tests
Only the Python standard library is used. You need pytest:
```
pip install pytest
pytest tests/test_query.py      # the tests of the file your task is about
pytest                          # everything (tests for tasks you haven't done yet fail)
```
The tests in `tests/` are only a few examples that work for every version. Darbni runs
more tests, made for your version, when you submit.

## Submitting
Commit and push your work, then submit your repo URL and the full commit SHA in Darbni.
