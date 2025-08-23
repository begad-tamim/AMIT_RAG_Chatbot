import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            database="ragdb",        # your DB name
            user="postgres",         # your username
            password="yourpassword", # your password
            host="127.0.0.1",
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print("❌ Error connecting:", e)
        return None


def create_tables(conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE EXTENSION IF NOT EXISTS vector;

            CREATE TABLE IF NOT EXISTS documents (
                id SERIAL PRIMARY KEY,
                filename TEXT,
                content TEXT,
                embedding VECTOR(768)  -- adjust dimension to match your embedding model
            );
        """)
        conn.commit()
        cur.close()
        print("✅ Tables created successfully.")
    except psycopg2.Error as e:
        print("❌ Error creating tables:", e)


if __name__ == "__main__":
    conn = get_connection()
    if conn:
        print("✅ Connected to PostgreSQL.")
        create_tables(conn)
        conn.close()
    else:
        print("⚠️ Connection failed.")



   
