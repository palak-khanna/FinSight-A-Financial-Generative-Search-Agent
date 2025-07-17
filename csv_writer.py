# core/csv_writer.py
import csv, os
from config import CSV_DIR

os.makedirs(CSV_DIR, exist_ok=True)

def write_csv(citations: list[dict], topic_slug: str) -> str:
    """
    citations: list of dicts -> {source, snippet, metric_json}
    Returns filepath of CSV written.
    """
    fp = os.path.join(CSV_DIR, f"{topic_slug}.csv")
    keys = citations[0].keys() if citations else ["source","snippet","metrics"]
    with open(fp, "w", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=keys).writeheader()
        csv.DictWriter(f, fieldnames=keys).writerows(citations)
    return fp
