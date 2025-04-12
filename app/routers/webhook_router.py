from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("")
async def webhook(file: UploadFile = File(...)):
    return JSONResponse(content={"message": "File received", "filename": file.filename})