# core/search.py
from googlesearch import search
from config import RESULT_LIMIT

def google_search(query: str, num: int = RESULT_LIMIT) -> list[str]:
    """Return a list of result URLs for the query."""
    return list(search(query, num_results=num))
