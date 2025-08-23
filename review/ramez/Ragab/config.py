
# TODO: Add configuration settings for the project
# TODO: Load API keys, database connection info, and model names from environment variables
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "BAAI/bge-small-en")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_NAME = os.getenv("DB_NAME", "ragdb")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
