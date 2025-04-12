from qdrant_client.models import Distance, VectorParams

from app.config.exception_handler_config import ErrorHandler
from app.config.qdrant_config import client_qdrant


def create_collection(collection_name):
    try:
        if not client_qdrant.collection_exists(collection_name=collection_name):
            client_qdrant.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(size=384, distance=Distance.COSINE),
            )
    except Exception as e:
        raise ErrorHandler.handle_qdrant_error(e, context="create_collection")

def create_points_vectorial_db(collection_name, points):
    try:
        create_collection(collection_name)
        client_qdrant.upsert(collection_name=collection_name, points=points)
    except Exception as e:
        raise ErrorHandler.handle_qdrant_error(e, context="create_points_vectorial")