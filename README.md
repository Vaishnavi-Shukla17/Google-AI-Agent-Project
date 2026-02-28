# 🔍 ResearchNova – AI Research Assistant

AI-powered research assistant built with Streamlit and Google Gemini.  
It helps users generate structured research reports, summarize long text, and analyze PDF research papers.

## ✨ Features

- 🧠 **Research Agent**  
  Enter any research question and get a structured report with:
  - Abstract  
  - Key findings in bullet points  
  - Brief conclusion  

- 📝 **Text Summarizer**  
  Paste long text (articles, notes, blogs) and get a concise summary in 3–5 bullet points.

- 📄 **PDF Reader & Analyzer**  
  Upload a PDF research paper and automatically extract and summarize the key content
  (first few pages, title, main points, and findings).

- 🎨 **Simple 4‑Tab UI**  
  Clean Streamlit interface with separate tabs for:
  - Home  
  - Research Agent  
  - Text Summarizer  
  - PDF Reader  

## 🛠 Tech Stack

- **Language:** Python  
- **UI Framework:** Streamlit  
- **AI Model:** Google Gemini (via `google-generativeai` Python library)  
- **PDF Processing:** PyPDF2  
- **Environment Management:** Python virtual environment (`venv`)  
- **Config & Secrets:** `.env` with `python-dotenv`

## 📁 Project Structure

ResearchNova/
app.py # Main Streamlit application (all tabs)
requirements.txt # Python dependencies
.env # Local API key (NOT committed – ignored by git)
.env.example # Example env file for others
.gitignore # Ignore venv, .env, caches, etc.
test_api.py # Small script to test Gemini API key
test_search.py # (Optional) DuckDuckGo search test
 list_models.py # Script to list available Gemini models

## 🚀 Getting Started

### 1. Clone the repository

### 2. Create and activate virtual environment


### 3. Install dependencies


### 4. Configure API key

1. Get a Gemini API key from: https://aistudio.google.com/app/apikey  
2. Create a `.env` file in the project root (same folder as `app.py`) with:

### 5. Run the app

Open the URL shown in the terminal (usually http://localhost:8501) in your browser.

## 💡 How It Works

- The app loads your Gemini API key from `.env` and configures the Gemini client.  
- **Research Agent** uses Gemini to generate a structured report directly from your question.  
- **Summarizer** sends your pasted text to Gemini with a “summarize in bullets” prompt.  
- **PDF Reader** extracts text from the uploaded PDF (first few pages) using PyPDF2, then sends that text to Gemini for analysis and summarization.

## 🔐 Security & Good Practices

- API key is stored only in `.env` locally.  
- `.env` and `venv/` are ignored by Git via `.gitignore`.  
- The repo contains `.env.example` so others know how to configure their own keys.

## ✅ Status

- Research Agent tab: **Working**  
- Text Summarizer tab: **Working**  
- PDF Reader tab: **Working**  
- Repo: Clean (no venv, no secrets)

## 📌 Possible Future Improvements

- Export reports as PDF or Markdown.  
- Add citation formatting (APA/MLA).  
- Support multiple languages.  
- Deploy on Streamlit Cloud or another hosting platform.

---

Feel free to fork or extend this project for your own research workflows or portfolio.
