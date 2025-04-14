from qdrant_client.http.models import PointStruct
import uuid

from app.config.embeddings_config import model_embeddings
from app.config.exception_handler_config import ErrorHandler

def create_segments_point(filename, segments):
    try:
        points = []
        for segment in segments:
            vector = model_embeddings.get_embedding(segment["text"])
            payload = {
                "filename": filename,
                "speaker": segment["speaker"],
                "time_stamp": segment["time_stamp"],
                "text": segment["text"]
            }
            points.append(
                PointStruct(id=str(uuid.uuid4()), vector=vector, payload=payload)
            )
        return points
    except Exception as e:
        raise ErrorHandler.handle_embedding_error(e)