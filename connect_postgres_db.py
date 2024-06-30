import psycopg2
from contextlib import contextmanager

@contextmanager
def create_connection(db_config):
    """Create a database connection to a PostgreSQL database"""
    conn = psycopg2.connect(**db_config)
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

# Конфігурація підключення до бази даних
db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'password12345',
    'host': 'localhost',
    'port': '5432'
}