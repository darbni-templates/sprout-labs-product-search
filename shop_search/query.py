def tokenize_query(query: str) -> list[str]:
    """Split a shopper's search query into words."""
    return query.lower().split()
