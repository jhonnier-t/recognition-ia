from datetime import datetime

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

from app.config.env_config import TO_EMAILS, COLLECTION
from app.config.template_config import read_email_template
from app.modules.email_module import email_notifier
from app.modules.embeddings_module import create_segments_point
from app.modules.transcriber_module import transcribe_with_gemini
from app.modules.vectorial_db_module import create_points_vectorial_db

router = APIRouter()

@router.post("/upload")
async def upload_audio(audio: UploadFile = File(...)):
    name_collection = f"{COLLECTION}_{audio.filename}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    try:
        segments = await transcribe_with_gemini(audio)
        points = create_segments_point(segments)
        create_points_vectorial_db(name_collection, points)
        html_template = read_email_template(True, name_collection)
        email_notifier.send_email(
            subject=f"Audio {audio.filename} transcribed and segmented",
            body=html_template,
            to_emails=TO_EMAILS,
            html=True
        )
        return JSONResponse(content={"content":f"Audio {audio.filename} transcribed and segmented. Also saved in db"},
                            status_code=200)
    except Exception as e:
        error_message = f"Error: Summarization failed {e}"
        html_template = read_email_template(False, name_collection, error_message)
        email_notifier.send_email(
            subject="Error: Summarization failed",
            body=html_template,
            to_emails=TO_EMAILS,
            html=True
        )
        return JSONResponse(content={"content": error_message}, status_code=50)


