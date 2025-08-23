
# TODO: Implement database connection using psycopg3
# TODO: Initialize the vector database schema using pgvector

import psycopg
# import numpy as np

# اتصال بالـ DB
conn = psycopg.connect(
    dbname="mydb",
    user="myuser",
    password="mypassword",
    host="localhost"
)

# vector الناتج من الموديل (list of floats)
embedding = [0.01, -0.02, 0.03, ...]

with conn.cursor() as cur:
    cur.execute(
        "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
        ("hello world", embedding)
    )
    conn.commit()
