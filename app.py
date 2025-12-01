import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('models/gemini-2.5-flash')

st.set_page_config(page_title="ResearchNova", page_icon="🔍")
st.title("🔍 ResearchNova – AI Research Assistant")

tabs = st.tabs(["Home", "Research Agent", "Summarizer", "PDF Reader"])


def search_web(query, max_results=5):
    try:
        with DDGS() as ddgs:
            return [r for r in ddgs.text(query, max_results=max_results)]
    except:
        return []

def scrape_content(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        for script in soup(["script", "style"]):
            script.decompose()
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        return text[:3000]
    except:
        return ""

def run_research_agent(topic):
    st.info("🔍 Researching with Gemini AI...")
    
    # Gemini does EVERYTHING (no DDG needed)
    prompt = f"""
    Create professional research report on: "{topic}"
    
    Use your latest knowledge. Format EXACTLY:
    
    ## Abstract
    2-3 sentences summary.
    
    ## Key Findings
    - Bullet 1 with facts
    - Bullet 2 with data  
    - Bullet 3 with insights
    
    ## Conclusion
    1-2 sentences final thoughts.
    """
    
    try:
        response = model.generate_content(prompt)
        st.success("✅ Research complete!")
        return response.text
    except Exception as e:
        return f"❌ Error: {e}"


with tabs[0]:
    st.subheader("Welcome to ResearchNova 🚀")
    
with tabs[1]:
    st.subheader("🧠 Research Agent")
    query = st.text_input("Enter your research question:")
    if st.button("🚀 Run Research Agent") and query:
        with st.spinner("Researching..."):
            response = run_research_agent(query)
        st.markdown(response)


with tabs[2]:
    st.subheader("📝 Text Summarizer")
    text_input = st.text_area("Paste text:", height=250)
    if st.button("✨ Summarize") and text_input.strip():
        with st.spinner("Summarizing..."):
            prompt = f"Summarize in 3-5 bullets:\n\n{text_input[:4000]}"
            summary = model.generate_content(prompt)
            st.markdown(f"**Summary:**\n{summary.text}")


with tabs[3]:
    st.subheader("📄 PDF Reader")
    pdf_file = st.file_uploader("Upload PDF:", type=["pdf"])
    
    if pdf_file:
        try:
            import PyPDF2
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            full_text = ""
            for page in pdf_reader.pages[:5]:
                full_text += page.extract_text() + "\n"
            
            st.success(f"✅ PDF loaded! {len(pdf_reader.pages)} pages.")
            with st.expander("📖 Preview"):
                st.text_area("", full_text[:1000], height=150)
            
            if st.button("✨ Analyze PDF"):
                with st.spinner("Analyzing..."):
                    prompt = f"""Analyze research paper:

## Title
## Key Points
## Findings
## Conclusion

Content: {full_text[:4000]}"""
                    summary = model.generate_content(prompt)
                    st.markdown(f"**{summary.text}**")
        except Exception as e:
            st.error(f"PDF error: {e}")
