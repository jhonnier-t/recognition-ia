from qdrant_client import QdrantClient

from app.config.env_config import QDRANT_HOST

client_qdrant = QdrantClient(host=QDRANT_HOST, port=6333)


