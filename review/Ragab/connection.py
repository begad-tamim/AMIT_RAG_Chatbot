
# TODO: Implement database connection using psycopg3
# TODO: Initialize the vector database schema using pgvector
import os
import psycopg
from psycopg.rows import dict_row
from app.core.config import Config

def get_db_connection():
    """
    Open a connection to PostgreSQL
    """
    conn = psycopg.connect(
        host=Config.DB_HOST,
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        row_factory=dict_row  # return rows as dict instead of tuple
    )
    return conn


def init_vector_schema():
    """
    Enable pgvector extension and create documents table
    """
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            # Enable pgvector extension
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")

            # Create table for documents + embeddings
            cur.execute("""
                CREATE TABLE IF NOT EXISTS documents (
                    id SERIAL PRIMARY KEY,
                    content TEXT,
                    embedding vector(768)  -- embedding size (BAAI model = 768)
                );
            """)
        conn.commit()



