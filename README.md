# 🔍 IntelliQuest AI: Generative Search & Intelligence Engine

> **“From Query to Summary, QA, and Insights — Seamlessly.”**

**IntelliQuest AI** is an intelligent web-based search engine that augments traditional search with generative capabilities. It fetches real-time data from websites, summarizes it using LLMs, extracts citations, enables Q&A over content, and stores every session for later retrieval. Ideal for enterprise use cases like financial analysis, e-commerce intelligence, market research, and more.

---

## 📽️ Demo

[![Watch the Demo(https://i.imgur.com/YOUR_THUMBNAIL_ID.png](https://github.com/palak-khanna/FinSight-A-Financial-Generative-Search-Agent/blob/EDA-AIML/thumbnail.png)](https://drive.google.com/file/d/1TNDEBer_gZECG1xhjP6QwLJS0m77Ro2b/view?usp=drive_link)

> 🎥 *Click the image above to watch a live walkthrough of the app.*
---

## 🚀 Features

- 🌐 **Live Web + YouTube Scraping**
- ✍️ **LLM-powered Summarization (via OpenAI/GPT)**
- ❓ **Conversational Q&A over summarized content**
- 🧠 **Memory of past sessions (stored via session state)**
- 📊 **CSV Export of Summaries, QA, Sources**
- 🔍 **Cited Source Snippets (Web & YouTube)**
- 💬 **Multi-topic chat history with navigation**
- 🧾 **RAG (Retrieval-Augmented Generation) Backbone**
- 🧩 Modular pipelines for summary, QA, and search

---

## 🛠️ Technologies Used

| Component        | Description                      |
|------------------|----------------------------------|
| `Streamlit`      | UI framework                     |
| `BeautifulSoup`  | Web scraping                     |
| `yt-dlp`         | YouTube video metadata & captions |
| `LangChain`      | Summarization, memory, RAG       |
| `OpenAI API`     | LLM-based summarizer & Q&A       |
| `FAISS`          | Semantic search index            |
| `pandas`         | Data export & tabular summaries  |
| `Session State`  | Session-based chat retention     |

---

## 🧰 Project Structure
```bash
├── app.py                # Main Streamlit app
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── core/                 # Core logic modules
│   ├── pipeline.py       # Orchestration pipeline
│   ├── summariser.py     # LLM-based summary generator
│   ├── plotter.py        # Trend visualizations
│   ├── scraper.py        # Web content scraper
│   ├── qa.py             # Question-answer engine
│   ├── utils.py          # Helpers & utilities
│   └── ...
├── exports/              # Exported CSVs
├── sessions/             # Search & chat history
```

---

## 🧪 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/intelliquest-ai.git
cd intelliquest-ai

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 📤 CSV Output Format
| Title              | Summary              | Source URL                         | Tags/Keywords      |
| ------------------ | -------------------- | ---------------------------------- | ------------------ |
| Company X Earnings | Short LLM summary... | [https://xyz.com](https://xyz.com) | finance, quarterly |


## 📚 Example Use Cases

- 📈 Financial Market Analysis (e.g., Goldman Sachs use case)
- 🛒 E-commerce Insights (product trends, pricing)
- 📰 News Monitoring and Summary
- 📊 Investor Reports Auto-generation
- 🧑‍💼 Competitor Intelligence

##💡 Future Enhancements

1. 🧭 Add Task Chaining + Action Planning (LangGraph or AutoGen)
2. 🗄️ Vector DB Persistence with ChromaDB or Weaviate
3. 🛡️ Built-in Fact-checker Module
4. 🔒 Auth layer for team use
5. 🌐 Browser automation for dynamic pages (via Playwright)

## 📜 License
MIT © 2025 Palak Khanna
