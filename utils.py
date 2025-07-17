from keybert import KeyBERT

kw_model = KeyBERT()

def compress_topic(topic: str, max_keywords: int = 5) -> str:
    """
    Extracts most relevant keywords to shorten the topic.
    Returns a compressed, query-efficient version of the original topic.
    """
    keywords = kw_model.extract_keywords(topic, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=max_keywords)
    shortened = " ".join([kw for kw, _ in keywords])
    return shortened if shortened else topic  # fallback to original
