
# TODO: Implement database connection using psycopg3
# TODO: Initialize the vector database schema using pgvector


import psycopg2

# Database connection parameters
DB_HOST = "localhost"
DB_USER = "postgres"         # change if different
DB_PASSWORD = "your_password"  # the password you set in PostgreSQL
DB_NAME = "postgres"         # default database, or create your own
DB_PORT = 5432

def connect_db():
    return psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME,
        port=DB_PORT
    )

def create_table(conn):
    cursor = conn.cursor()

    # SQL query to create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id SERIAL PRIMARY KEY,
            filename TEXT,
            content TEXT
        );
    """)

    conn.commit()
    cursor.close()
    print("✅ Table 'documents' created successfully!")

if __name__ == "__main__":
    conn = connect_db()
    create_table(conn)
    conn.close()
