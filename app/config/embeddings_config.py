from fastembed.embedding import DefaultEmbedding
import logging

from app.config.env_config import EMBEDDINGS_MODEL

logger = logging.getLogger(__name__)

class FastEmbedService:
    def __init__(self, model_name: str, cache_dir: str = ".cache"):
        self.embedder = DefaultEmbedding(model_name=model_name, cache_dir=cache_dir)

    def get_embedding(self, text: str) -> list:
        try:
            return next(self.embedder.embed([text]))
        except Exception as e:
            logger.exception(f"Failed to generate embedding: {e}")
            return []

model_embeddings = FastEmbedService(model_name=EMBEDDINGS_MODEL)

