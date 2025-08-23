# ingest.py
import os
import psycopg2
from psycopg2.extras import execute_values
from PyPDF2 import PdfReader
from app.embeddings.embedding_service import EmbeddingService

def ingest():
    # ===== 1. Connect to PostgreSQL =====
    conn = psycopg2.connect(
        dbname="ragdb",
        user="postgres",
        password="yourpassword",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id SERIAL PRIMARY KEY,
        content TEXT,
        embedding VECTOR(768)  -- depends on embedding model dimension
    );
    """)
    conn.commit()

    # ===== 2. Initialize embedding service =====
    embedder = EmbeddingService(model_name="BAAI/bge-base-en")

    # ===== 3. Read documents from /docs folder =====
    docs_folder = "docs"
    documents = []

    for filename in os.listdir(docs_folder):
        file_path = os.path.join(docs_folder, filename)

        # Handle .txt files
        if filename.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
                documents.append(text)

        # Handle .pdf files
        elif filename.endswith(".pdf"):
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            documents.append(text)

    if not documents:
        print("[INFO] No documents found in docs/ folder.")
        return

    # ===== 4. Generate embeddings =====
    embeddings = embedder.embed_documents(documents)

    # ===== 5. Store in PostgreSQL =====
    data_to_insert = [(doc, embedding) for doc, embedding in zip(documents, embeddings)]

    insert_query = """
    INSERT INTO documents (content, embedding)
    VALUES %s
    """
    execute_values(cur, insert_query, data_to_insert)
    conn.commit()

    print(f"[INFO] Inserted {len(documents)} documents with embeddings into PostgreSQL.")

    # ===== 6. Close connection =====
    cur.close()
    conn.close()

# Run directly
if __name__ == "__main__":
    ingest()
