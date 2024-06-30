# import psycopg2
# from contextlib import contextmanager

import connect_postgres_db as cdb
from faker import Faker

# @contextmanager
# def create_connection(db_config):
#     """Create a database connection to a PostgreSQL database"""
#     conn = psycopg2.connect(**db_config)
#     try:
#         yield conn
#         conn.commit()
#     except Exception as e:
#         conn.rollback()
#         raise e
#     finally:
#         conn.close()

# # Конфігурація підключення до бази даних
# db_config = {
#     'dbname': 'postgres',
#     'user': 'postgres',
#     'password': 'password12345',
#     'host': 'localhost',
#     'port': '5432'
# }

# Ініціалізація Faker
fake = Faker()

def seed_users(cursor, num_users=10):
    for _ in range(num_users):
        fullname = fake.name()
        email = fake.unique.email()
        cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

def seed_tasks(cursor, num_tasks=30):
    cursor.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]
    
    cursor.execute("SELECT id FROM status")
    status_ids = [row[0] for row in cursor.fetchall()]

    for _ in range(num_tasks):
        title = fake.sentence(nb_words=6)
        description = fake.text()
        status_id = fake.random.choice(status_ids)
        user_id = fake.random.choice(user_ids)
        cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", 
                       (title, description, status_id, user_id))

with cdb.create_connection(cdb.db_config) as conn:
    with conn.cursor() as cursor:
        # Seed users
        seed_users(cursor)
        print("Users table seeded successfully.")
        
        # Seed tasks
        seed_tasks(cursor)
        print("Tasks table seeded successfully.")