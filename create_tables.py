import connect_postgres_db as cdb

create_users_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
"""

create_status_table_query = """
CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);
"""

insert_status_query = """
INSERT INTO status (name) VALUES
('new'),
('in progress'),
('completed')
ON CONFLICT (name) DO NOTHING;
"""

create_tasks_table_query = """
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (status_id) REFERENCES status (id),
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);
"""


with cdb.create_connection(cdb.db_config) as conn:
    with conn.cursor() as cursor:

        cursor.execute(create_users_table_query)
        print("Table 'users' created successfully.")
        
        cursor.execute(create_status_table_query)
        print("Table 'status' created successfully.")
        
        cursor.execute(insert_status_query)
        print("Status entries inserted successfully.")
        
        cursor.execute(create_tasks_table_query)
        print("Table 'tasks' created successfully.")

# if __name__ == "__main__":
#     create_connection()