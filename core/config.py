from dotenv import load_dotenv
import os

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini").lower()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def validate_config():
    if LLM_PROVIDER == "gemini" and not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY is missing. Add it to your .env file.")

    if LLM_PROVIDER == "openrouter" and not OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY is missing. Add it to your .env file.")
