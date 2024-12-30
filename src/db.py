import psycopg2
import os
from dotenv import load_dotenv

#Loading from .env
load_dotenv()

def get_db_connection():
    try:
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        return connection
    except Exception as e:
        print(f"Failed to connect to database: {e}")
        raise
