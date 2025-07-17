# core/pipeline.py
from core.utils import compress_topic  # assuming function is in utils.py
from hashlib import sha1
from .search import google_search
from .scraper import scrape
from .summariser import summarise
from .qa import ask
from .plotter import _extract_metrics
from .csv_writer import write_csv
from .session import save_session

def run_pipeline(topic: str) -> dict:
    """
    Returns a dict with:
      summary, citations(list), plot_b64(str), slug
    """
    urls = google_search(topic)
    citations = []
    big_corpus = ""

    for url in urls:
        page = scrape(url)
        text  = page["raw_text"]
        tables = page["tables"]

        if not text: continue
        big_corpus += text + "\n"
        metrics = _extract_metrics(text)
        citations.append({
            "source": url,
            "snippet": text[:250] + "...",
            "metrics": metrics
        })

        # Optional: parse tables for numeric metrics
        for tb in tables:
            for col in tb.columns:
                if isinstance(col, str) and any(k in col.lower() for k in ("revenue","sales")):
                    try:
                        val = float(tb[col].iloc[0])
                        metrics[col] = val
                    except: pass

    short_topic = compress_topic(topic)
    corpus = scrape(short_topic)
    summary = summarise(big_corpus, topic)
    slug = sha1(topic.lower().encode()).hexdigest()[:12]
    csv_path = write_csv(citations, slug)

    # Build plot from merged metrics across pages
    aggregate_metrics = {}
    for c in citations:
        aggregate_metrics.update(c["metrics"])
    from .plotter import build_plot
    plot_b64 = build_plot(aggregate_metrics)

    save_session(topic, summary, citations)

    return {
        "slug"      : slug,
        "summary"   : summary,
        "citations" : citations,
        "plot_b64"  : plot_b64,
        "csv_path"  : csv_path,
        "context"   : big_corpus   # for downstream QA
    }

def answer_question(question: str, context: str) -> str:
    return ask(question, context)
