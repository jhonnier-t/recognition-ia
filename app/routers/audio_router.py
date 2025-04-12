from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from app.modules.transcriber_module import transcribe_with_gemini

router = APIRouter()

@router.post("/upload")
async def upload_audio(audio: UploadFile = File(...)):
    return await transcribe_with_gemini(audio)


