
# RAG Chatbot Project

This project is a Retrieval-Augmented Generation (RAG) chatbot. It uses:
- **Gemini 2.0 Flash** as the language model (LLM) for generating answers
- **Google BAAI embedding model** for converting text to embeddings
- **PostgreSQL with pgvector** for storing and searching document embeddings

## What is a RAG Chatbot?
A RAG chatbot answers user questions by first searching for relevant information in a set of documents, then sending both the user question and the found information to a language model (Gemini 2.0 Flash) to generate a helpful answer.

## What You Need to Do
You will complete the code in each file to build a working RAG chatbot. Each file has TODO comments to guide you. Here is what each file/folder does and what you should implement:

### Top-level files
- **ingest.py**: Script to read documents from the `docs/` folder, generate embeddings using the embedding service, and store them in the vector database. 
	- Implement: Document reading, embedding generation, and storing logic.

### app/
This folder contains the main code, organized by responsibility:

- **api/main.py**: FastAPI app for the chatbot API.
	- Implement: Endpoints for `/chat` (get answer from chatbot) and `/chat/history` (get previous chats).

- **chatbot/rag_pipeline.py**: The core RAG pipeline logic.
	- Implement: Retrieve relevant context from the vector DB, call Gemini 2.0 Flash with the context and user query, and return the answer.

- **core/config.py**: Configuration settings.
	- Implement: Load API keys, DB connection info, and model names from environment variables.

- **database/connection.py**: Database connection code.
	- Implement: Connect to PostgreSQL using psycopg3, initialize the vector DB schema with pgvector.

- **embeddings/embedding_service.py**: Embedding service.
	- Implement: Use the Google BAAI model (via HuggingFace) to generate embeddings from text.

- **retrieval/vector_store.py**: Vector store logic.
	- Implement: Insert embeddings into Postgres/pgvector and retrieve the most similar documents for a query.

### tests/
- **test_api.py**: Tests for the API endpoints.
	- Implement: Tests for root, `/chat`, and `/chat/history` endpoints.

### docs/
- Add your source documents here. These will be ingested and used by the chatbot.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Add your documents to the `docs/` folder.
3. Run the ingestion script: `python ingest.py`
4. Start the API: `uvicorn app.api.main:app --reload`
5. Use the API endpoints to chat with your RAG chatbot!

---
**Tip:** Each file contains TODO comments to help you know what to implement. Follow them step by step!

