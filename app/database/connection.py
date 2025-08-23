import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection(dbname="ragdb", user="postgres", password="1234", host="127.0.0.1", port="5432"):

    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
            cursor_factory=RealDictCursor  # عشان ترجع النتائج كـ dict بدل tuple
        )
        print("✅ Connected to PostgreSQL successfully!")
        return conn
    except psycopg2.Error as e:
        print("❌ Error connecting to PostgreSQL:", e)
        return None
if __name__ == "__main__":
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        print(cur.fetchone())
        cur.close()
        conn.close()


   
