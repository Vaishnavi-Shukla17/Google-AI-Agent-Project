import streamlit as st
from services.pdf_service import extract_pdf_text, chunk_text
from services.search_service import collect_research_context
from utils.prompts import (
    research_prompt,
    summary_prompt,
    pdf_chunk_summary_prompt,
    pdf_final_summary_prompt,
)
from services.llm_service import generate_text
from services.search_service import search_web, scrape_content
from utils.prompts import research_prompt, summary_prompt, pdf_analysis_prompt
import streamlit as st

st.set_page_config(
    page_title="ResearchNova",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
html, body, [class*="css"]  {
    font-size: 20px;
}
p, li, label, div {
    font-size: 25px !important;
}
h1 {
    font-size: 45px !important;
}
h2 {
    font-size: 38px !important;
}
h3 {
    font-size: 30px !important;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="ResearchNova", page_icon="🔍")
st.title("🔍 ResearchNova – AI Research Assistant")

if "latest_report" not in st.session_state:
    st.session_state.latest_report = ""

if "latest_sources" not in st.session_state:
    st.session_state.latest_sources = []

tabs = st.tabs(["Home", "Research Agent", "Summarizer", "PDF Reader"])

with tabs[0]:
    st.subheader("Welcome to ResearchNova 🚀")
    st.write("AI-powered assistant for research, summarization, and PDF analysis.")

with tabs[1]:
    st.subheader("🧠 Research Agent")
    query = st.text_input("Enter your research question:")

    if st.button("🚀 Run Research Agent") and query.strip():
        with st.spinner("Searching and researching..."):
            try:
                context = collect_research_context(query, max_results=3)

                if not context:
                    st.warning("No web context could be collected for this query.")
                else:
                    response = generate_text(research_prompt(query, context))
                    st.session_state.latest_report = response
                    st.session_state.latest_sources = sources
                    st.success("✅ Research complete!")
            except Exception as e:
                st.error(f"Research error: {e}")

    if st.session_state.latest_report:
        st.markdown(st.session_state.latest_report)

    if st.session_state.latest_sources:
        st.markdown("### Sources used")
        for source in st.session_state.latest_sources:
            st.markdown(f"- [{source['title']}]({source['url']})")

with tabs[2]:
    st.subheader("📝 Text Summarizer")
    text_input = st.text_area("Paste text:", height=250)

    if st.button("✨ Summarize") and text_input.strip():
        with st.spinner("Summarizing..."):
            try:
                summary = generate_text(summary_prompt(text_input))
                st.markdown(f"**Summary:**\n{summary}")
            except Exception as e:
                st.error(f"Summarization error: {e}")

with tabs[3]:
    st.subheader("📄 PDF Reader")
    pdf_file = st.file_uploader("Upload PDF:", type=["pdf"])

    if pdf_file:
        try:
            full_text = extract_pdf_text(pdf_file, max_pages=None)
            st.success("✅ PDF loaded successfully!")

            with st.expander("📖 Preview"):
                st.text_area("Extracted text preview", full_text[:1500], height=200)

            if st.button("✨ Analyze PDF"):
                with st.spinner("Analyzing full PDF in chunks..."):
                    chunks = chunk_text(full_text, chunk_size=2500, overlap=200)

                    if not chunks:
                        st.warning("No readable text could be extracted from this PDF.")
                    else:
                        chunk_summaries = []

                        for i, chunk in enumerate(chunks[:5], start=1):
                            summary = generate_text(pdf_chunk_summary_prompt(chunk, i))
                            chunk_summaries.append(f"Chunk {i} Summary:\n{summary}")

                        combined_summaries = "\n\n".join(chunk_summaries)
                        final_result = generate_text(pdf_final_summary_prompt(combined_summaries))

                        st.markdown(final_result)
                        st.markdown(f"**Chunks processed:** {min(len(chunks), 5)} / {len(chunks)}")

        except Exception as e:
            st.error(f"PDF error: {e}")
