# core/session.py
import os, json, hashlib, datetime as dt
from config import SESSION_DIR

os.makedirs(SESSION_DIR, exist_ok=True)

def _file(topic: str) -> str:
    slug = hashlib.sha1(topic.lower().encode()).hexdigest()[:12]
    return os.path.join(SESSION_DIR, f"{slug}.json")

def save_session(topic: str, summary: str, citations: list[dict]):
    data = {"topic": topic,
            "summary": summary,
            "citations": citations,
            "timestamp": dt.datetime.utcnow().isoformat()}
    with open(_file(topic), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_session(topic: str) -> dict | None:
    fp = _file(topic)
    if os.path.exists(fp):
        return json.load(open(fp, encoding="utf-8"))
    return None
