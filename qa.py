# core/qa.py
from openai import OpenAI
from config import OPENAI_API_KEY

MODEL_QA = "gpt-4o-mini"

client = OpenAI(api_key=OPENAI_API_KEY)

def ask(question: str, context: str) -> str:
    prompt = f"Context:\n{context}\n\nQuestion: {question}"

    response = client.chat.completions.create(
        model=MODEL_QA,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()
