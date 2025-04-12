from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import uuid

from app.config.env_config import COLLECTION

client_qdrant = QdrantClient(":memory:")

def create_collection():
    if not client_qdrant.collection_exists(collection_name=COLLECTION):
        client_qdrant.create_collection(
            collection_name=COLLECTION,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )

def index_text(text, vector):
    client_qdrant.upsert(
        collection_name=COLLECTION,
        points=[{
            "id": str(uuid.uuid4()),
            "vector": vector,
            "payload": {"text": text}
        }]
    )
