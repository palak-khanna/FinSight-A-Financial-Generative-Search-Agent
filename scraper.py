# core/scraper.py
import requests, re, pandas as pd
from bs4 import BeautifulSoup
from config import REQUEST_TIMEOUT

TXT_TAGS = {"p", "span", "li"}

def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()

def scrape(url: str) -> dict:
    """
    Fetch a URL and return:
      - raw_text   : cleaned article text
      - tables     : list[pd.DataFrame] extracted with read_html()
    """
    try:
        r = requests.get(url, timeout=REQUEST_TIMEOUT, headers={"User-Agent":"Mozilla/5.0"})
        r.raise_for_status()
    except Exception as e:
        return {"raw_text": "", "tables": []}

    soup = BeautifulSoup(r.text, "html.parser")
    paragraphs = " ".join(_clean(t.get_text()) for t in soup.find_all(TXT_TAGS))
    try:
        tables = pd.read_html(r.text)[:3]  # limit to first 3 tables
    except ValueError:
        tables = []

    return {"raw_text": paragraphs, "tables": tables}
