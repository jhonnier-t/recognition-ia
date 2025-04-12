import json

from starlette.responses import JSONResponse

from app.config.gemini_config import model_gemini
from app.config.env_config import TEXT_PROMPT


async def transcribe_with_gemini(audio):
    audio_bytes = await audio.read()
    audio_part = {
        "mime_type": audio.content_type,
        "data": audio_bytes,
    }
    response = model_gemini.generate_content([
        TEXT_PROMPT,
        audio_part
    ])
    return JSONResponse(content= json.loads(response.text) )
