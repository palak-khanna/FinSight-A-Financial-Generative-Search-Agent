# core/plotter.py
import re, matplotlib.pyplot as plt, pandas as pd, io, base64

NUM_RE = re.compile(r"(\$|₹)?([\d,]+(\.\d+)?)")

def _extract_metrics(text: str) -> dict[str, float]:
    """
    Naive pattern search for keywords like 'revenue', 'sales', 'profit' and
    associated numbers. Returns a dict metric -> value.
    """
    metrics = {}
    for key in ("revenue", "sales", "profit", "income"):
        pattern = rf"{key}[^$₹\d]{{0,15}}{NUM_RE.pattern}"
        m = re.search(pattern, text, flags=re.I)
        if m and m.group(2):  # check group(2) exists and is not empty
            value_str = m.group(2).replace(",", "").strip()
            try:
                val = float(value_str)
                metrics[key.lower()] = val
            except ValueError:
                continue  # skip if value_str is still invalid (e.g., "--", "N/A")
    return metrics


def build_plot(metrics: dict) -> str | None:
    """
    Given metrics dict, build a bar chart and return a base64 PNG string
    ready for Streamlit `st.image`.
    """
    if not metrics: return None
    df = pd.Series(metrics)
    fig, ax = plt.subplots()
    ax.bar(df.index, df.values)
    ax.set_title("Extracted Financial Metrics")
    ax.set_ylabel("Amount (in original units)")
    buf = io.BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png")
    plt.close(fig)
    return base64.b64encode(buf.getvalue()).decode("utf-8")
