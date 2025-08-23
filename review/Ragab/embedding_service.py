
# TODO: Implement the embedding service
# TODO: Use HuggingFace BAAI model to generate embeddings from text
from sentence_transformers import SentenceTransformer
from typing import List
from app.core.config import Config
from app.db.connection import get_db_connection

class EmbeddingService:
    def __init__(self):
        # Load embedding model
        self.model = SentenceTransformer(Config.EMBEDDING_MODEL_NAME)

    def embed_text(self, text: str) -> List[float]:

        return self.model.encode(text, convert_to_numpy=True).tolist()

    def embed_documents(self, documents: List[str]) -> List[List[float]]:

        return self.model.encode(documents, convert_to_numpy=True).tolist()

    def insert_document(self, content: str):

        embedding = self.embed_text(content)

        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO documents (content, embedding)
                    VALUES (%s, %s)
                    RETURNING id;
                    """,
                    (content, embedding)
                )
                new_id = cur.fetchone()["id"]
            conn.commit()
        return new_id

    def search_similar_documents(self, query: str, top_k: int = 5):

        query_embedding = self.embed_text(query)

        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, content, embedding <=> %s AS distance
                    FROM documents
                    ORDER BY embedding <=> %s
                    LIMIT %s;
                    """,
                    (query_embedding, query_embedding, top_k)
                )
                results = cur.fetchall()
        return results

