from dotenv import load_dotenv
import google.generativeai as genai
import os

print("🔍 DEBUGGING API KEY...")

# Check .env file exists
if os.path.exists('.env'):
    print("✅ .env file FOUND")
else:
    print("❌ .env file MISSING")

# Load and check key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print(f"API Key: {api_key[:10]}..." if api_key else "❌ API KEY = None/Empty")

# Test Gemini
if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        response = model.generate_content("Say 'API WORKS!'")
        print(f"✅ GEMINI TEST: {response.text}")
    except Exception as e:
        print(f"❌ GEMINI ERROR: {e}")
else:
    print("❌ NO API KEY - Fix .env first")
