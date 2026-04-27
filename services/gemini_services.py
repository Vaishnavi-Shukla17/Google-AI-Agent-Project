import google.generativeai as genai
from core.config import GOOGLE_API_KEY, validate_config

validate_config()
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash")

def generate_text(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text
