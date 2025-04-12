from fastapi import FastAPI

from app.config.logger_config import setup_logging
from app.routers import audio_router, webhook_router

setup_logging()
app = FastAPI(title="Recognition App",
              description="Recognition app with IA Gemini, embeddings, qdrant, 8n8, notifications email",
              version='1.0.0',
              root_path="/api",
              docs_url="/docs",
              redoc_url="/redoc",
              summary='Recognition IA for Sofka',
              openapi_url="/openapi.json")
app.include_router(router=audio_router.router, prefix="/audio", tags=["Audio"])
app.include_router(router=webhook_router.router, prefix="/webhook", tags=["Webhook"])


