import google.generativeai as genai

from app.config.env_config import GEMINI_API_KEY, GEMINI_MODEL

genai.configure(api_key=GEMINI_API_KEY)
model_gemini = genai.GenerativeModel(f"models/{GEMINI_MODEL}")