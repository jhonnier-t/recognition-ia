from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

from app.config.env_config import TO_EMAILS
from app.modules.email_module import email_notifier
from app.modules.embeddings_module import create_segments_point
from app.modules.transcriber_module import transcribe_with_gemini
from app.modules.vectorial_db_module import create_points_vectorial_db

router = APIRouter()

@router.post("/upload")
async def upload_audio(audio: UploadFile = File(...)):
    try:
        segments = await transcribe_with_gemini(audio)
        points = create_segments_point(segments)
        create_points_vectorial_db(points)
        email_notifier.send_email(
            subject=f"Audio {audio.filename} transcribed and segmented",
            body="Summarization successful",
            to_emails=TO_EMAILS
        )
        return JSONResponse(content={"content":f"Audio {audio.filename} transcribed and segmented. Also saved in db"},
                            status_code=200)
    except Exception as e:
        email_notifier.send_email(
            subject="Error: Summarization failed",
            body=f"An error occurred while trying to summarize audio segment: {e}",
            to_emails=TO_EMAILS
        )
        return JSONResponse(content={"content":f"Error: Summarization failed {e}"},
                            status_code=50)


