import logging
from typing import Optional
from fastapi import HTTPException
from qdrant_client.http.exceptions import UnexpectedResponse
from google.api_core.exceptions import GoogleAPIError, RetryError, InvalidArgument

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class ErrorHandler:
    @staticmethod
    def handle_qdrant_error(e: Exception, context: Optional[str] = ""):
        if isinstance(e, UnexpectedResponse):
            logger.error(f"Error Qdrant ({context}): {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Error BD Qdrant: {e}"
            )
        else:
            logger.exception(f"Error Qdrant ({context}): {e}")
            raise HTTPException(
                status_code=500,
                detail="Internal error when interacting with Qdrant"
            )

    @staticmethod
    def handle_embedding_error(e: Exception, text: Optional[str] = ""):
        logger.exception(f"Error generating embedding fot text: {text}\n{e}")
        raise HTTPException(
            status_code=500,
            detail="Error generating embeddings of text"
        )

    @staticmethod
    def handle_gemini_error(e: Exception, context: str = "Gemini request"):
        if isinstance(e, InvalidArgument):
            logger.error(f"[Gemini] Invalid argument in {context}: {e.message}")
            raise HTTPException(
                status_code=400,
                detail=f"Invalid request to Gemini: {e.message}"
            )
        elif isinstance(e, RetryError):
            logger.warning(f"[Gemini] Retry error in {context}: {str(e)}")
            raise HTTPException(
                status_code=503,
                detail="Gemini service temporarily unavailable (retry failed)"
            )
        elif isinstance(e, GoogleAPIError):
            logger.error(f"[Gemini] API error in {context}: {str(e)}")
            raise HTTPException(
                status_code=502,
                detail="Error communicating with the Gemini API"
            )
        else:
            logger.exception(f"[Gemini] Unexpected error in {context}: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail="Internal server error while processing Gemini response"
            )

    @staticmethod
    def handle_general_error(e: Exception, context: Optional[str] = ""):
        logger.exception(f"General Error ({context}): {e}")
        raise HTTPException(
            status_code=500,
            detail="An internal server error occurred"
        )
