
# TODO: Implement the embedding service
# TODO: Use HuggingFace BAAI model to generate embeddings from text

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from sentence_transformers import SentenceTransformer


MODEL_NAME = "BAAI/bge-m3"   
model = SentenceTransformer(MODEL_NAME)

app = FastAPI(title="Embedding Service")

class EmbeddingRequest(BaseModel):
    input: List[str]
    
class EmbeddingResponse(BaseModel):
    model: str
    dimensions: int
    data: List[List[float]]

@app.post("/embeddings", response_model=EmbeddingResponse)
def get_embeddings(req: EmbeddingRequest):
    embeddings = model.encode(req.input, normalize_embeddings=True)
    return EmbeddingResponse(
        model=MODEL_NAME,
        dimensions=len(embeddings[0]),
        data=embeddings.tolist()
    )