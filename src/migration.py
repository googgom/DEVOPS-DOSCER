from db import get_db_connection

def run_migrations():
    try:
        print("Executing migrations...")
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL
                )
            """)
        conn.commit()
        print("Migrations done!")
    except Exception as e:
        print(f"Migration ERROR: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    run_migrations()
