import psycopg

def init_vector_db():
    # Step 1: Connect to PostgreSQL
    conn = psycopg.connect(
    dbname="postgres",
    user="postgres",
    password="mypassword",   # the password you set during installation
    host="localhost",
    port="5432"
)


    # Step 2: Create pgvector extension & table
    with conn.cursor() as cur:
        # Enable pgvector extension
        cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
        
        # Create a table with a vector column (dimension = 1536, like OpenAI embeddings)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id SERIAL PRIMARY KEY,
                content TEXT,
                embedding vector(1536)
            );
        """)
        conn.commit()

    print("✅ Vector DB schema initialized successfully!")
    return conn


# Example usage
if __name__ == "__main__":
    conn = init_vector_db()
    conn.close()
