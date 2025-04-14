import os
from dotenv import load_dotenv

load_dotenv()

#CONFIG ENV GLOBAL
LANGUAGE = "es"

#CONFIG ENV EMAIL
SMTP_SERVER= os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT=os.getenv("SMTP_PORT", 587)
SENDER_EMAIL=os.getenv("SENDER_EMAIL")
SENDER_PASSWORD=os.getenv("SENDER_PASSWORD")
TO_EMAILS=[SENDER_EMAIL]

#CONFIG ENV EMBEDDINGS
EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL", "BAAI/bge-small-en")

#CONFIG ENV BD VECTORIAL
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
VECTOR_DB_PROVIDER = os.getenv("VECTOR_DB_PROVIDER", "qdrant")
COLLECTION = "audio"

#CONFIG ENV GEMINI
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-pro-exp-03-25")
TEXT_PROMPT = """
Quiero que transcribas el siguiente audio en español y segmentes por hablante si es posible.
Sin texto adicional ni explicaciones. Devuélveme la respuesta en el siguiente formato:

Speaker = {"speaker": str, "time_stamp": "00:00:00.248", "text": str},
Return: list[Speaker]

⚠️ IMPORTANTE:

- No pongas la palabra json dentro de bloques de código (nada de json, ni ).
- No pongas las comillas hacia atrás ``` en el objeto JSON.
- No pongas salto de línea \n en el objeto JSON.
- No devuelvas caracteres de escape (nada de \", \\n, etc).
- No agregues ningún texto antes ni después del objeto JSON.
- No expliques nada, ni digas “Aquí tienes la transcripción” ni nada parecido.
- Devuelve solo la lista de objetos Speaker como JSON válido, limpio y directo.
- El texto debe estar sin errores y con puntuación correcta.
"""
