# core/summariser.py
from openai import OpenAI
from config import OPENAI_API_KEY
import tiktoken

client = OpenAI(api_key=OPENAI_API_KEY)

MODEL_SUMMARY = "gpt-4o"
MAX_TOKENS = 14000  # Stay well below the 16k limit
# Tokenizer to estimate token count
def num_tokens_from_string(string: str, model_name: str = MODEL_SUMMARY) -> int:
    encoding = tiktoken.encoding_for_model(model_name)
    return len(encoding.encode(string))

# Split into smaller chunks
def chunk_text(text: str, max_tokens: int = MAX_TOKENS) -> list:
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        chunk_text = " ".join(current_chunk)
        if num_tokens_from_string(chunk_text) > max_tokens:
            # Remove last word and start new chunk
            current_chunk.pop()
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def summarise(context: str, topic: str) -> str:
    chunks = chunk_text(context)
    summaries = []

    for idx, chunk in enumerate(chunks):
        print(f"Summarizing chunk {idx + 1} of {len(chunks)}...")
        response = client.chat.completions.create(
            model=MODEL_SUMMARY,
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize the following about '{topic}':\n{chunk}"
                }
            ],
            temperature=0.3,
            max_tokens=600
        )
        summaries.append(response.choices[0].message.content.strip())

    # Merge all partial summaries into one final summary
    final_summary = "\n\n".join(summaries)
    return final_summary
