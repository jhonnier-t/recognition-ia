from sentence_transformers import SentenceTransformer

from app.config.env_config import EMBEDDINGS_MODEL

model_embeddings = SentenceTransformer(EMBEDDINGS_MODEL)