import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env")

genai.configure(api_key=api_key)

def generate_text(prompt: str, max_retries: int = 3) -> str:
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            if "429" in str(e) or "quota" in str(e).lower():
                if attempt < max_retries - 1:
                    retry_delay = 30  # Wait 30 seconds for quota retry
                    print(f"Quota hit, retrying in {retry_delay}s... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(retry_delay)
                    continue
                return "Quota exceeded. Please wait a few minutes and try again."
            raise
    
    return "Max retries exceeded."
