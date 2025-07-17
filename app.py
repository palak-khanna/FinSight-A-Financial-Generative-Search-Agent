import streamlit as st
from core import pipeline  # <-- Make sure core/pipeline.py exists
import os
import uuid

st.set_page_config(page_title="GenAI Search Engine", layout="wide")

# Initialize session state
if "history" not in st.session_state:
    st.session_state["history"] = []
if "selected_slug" not in st.session_state:
    st.session_state["selected_slug"] = None
if "qa_inputs" not in st.session_state:
    st.session_state["qa_inputs"] = {}

st.title("💡 FinSight: Your Financial assistant")

# Sidebar - Search History
st.sidebar.header("📁 Search History")
for entry in st.session_state["history"]:
    if st.sidebar.button(entry["topic"], key=f"sidebar-{entry['slug']}"):
        st.session_state["selected_slug"] = entry["slug"]

# Main Interface
with st.form(key="search_form"):
    topic = st.text_input("🔍 Enter a topic to search", "")
    submitted = st.form_submit_button("Search")
    if submitted and topic:
        result = pipeline.run_pipeline(topic)  # Summary + citations + CSV + context
        slug = str(uuid.uuid4())
        st.session_state["selected_slug"] = slug
        st.session_state["history"].append({
            "slug": slug,
            "topic": topic,
            "summary": result["summary"],
            "citations": result["citations"],
            "csv_path": result["csv_path"],
            "context": result["context"]
        })

# Show results if any chat is selected
if st.session_state["selected_slug"]:
    entry = next((e for e in st.session_state["history"] if e["slug"] == st.session_state["selected_slug"]), None)
    if entry:
        st.subheader(f"📌 {entry['topic']}")
        st.write(entry["summary"])
        st.subheader("📚 Citations")
        st.dataframe(entry["citations"])

        if entry["csv_path"] and os.path.exists(entry["csv_path"]):
            with open(entry["csv_path"], "rb") as f:
                st.download_button("📥 Download CSV", f, file_name=os.path.basename(entry["csv_path"]))

        # Q&A Section
        st.markdown("## 🤖 Ask Questions")
        q_key = f"qa-{entry['slug']}"
        if q_key not in st.session_state["qa_inputs"]:
            st.session_state["qa_inputs"][q_key] = ""

        question = st.text_input("Your Question", key=q_key)
        if st.button("Get Answer", key=f"btn-{entry['slug']}"):
            answer = pipeline.answer_question(question, entry["context"])
            st.markdown(f"**Answer:** {answer}")
