import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-pro-exp-03-25")
VECTOR_DB_PROVIDER = os.getenv("VECTOR_DB_PROVIDER", "qdrant")
UPLOAD_FOLDER = "uploads"
COLLECTION = "audios"
LANGUAGE = "es"
TEXT_PROMPT = """
Quiero que transcribas el siguiente audio en español y segmentes por hablante si es posible. 
Sin texto adicional ni explicaciones. Devuélveme la respuesta en el siguiente formato:

Speaker = {"speaker": str, "time_stamp": "00:00:00.248", "text": str},
Return: list[Speaker]

⚠️ IMPORTANTE:
- No pongas el JSON dentro de bloques de código (nada de ```json ni ```).
- No agregues ningún texto antes ni después del JSON.
- No expliques nada, ni digas “Aquí tienes la transcripción” ni nada parecido.
- Solo devuelve el JSON puro, exactamente con ese formato.
- No devuelvas el JSON como una cadena (nada de escapado con \").
"""
FORMATS = ["audio/wav", "audio/mp3", "audio/m4a", "audio/ogg"]
