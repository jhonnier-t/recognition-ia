from qdrant_client.models import Distance, VectorParams

from app.config.env_config import COLLECTION
from app.config.exception_handler_config import ErrorHandler
from app.config.qdrant_config import client_qdrant


def create_collection():
    try:
        if not client_qdrant.collection_exists(collection_name=COLLECTION):
            client_qdrant.create_collection(
                collection_name=COLLECTION,
                vectors_config=VectorParams(size=384, distance=Distance.COSINE),
            )
    except Exception as e:
        ErrorHandler.handle_qdrant_error(e, context="create_collection")

def create_points_vectorial_db(points):
    try:
        client_qdrant.upsert(collection_name=COLLECTION, points=points)
    except Exception as e:
        ErrorHandler.handle_qdrant_error(e, context="create_points_vectorial")