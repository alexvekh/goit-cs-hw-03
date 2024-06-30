Database Query Operations

## 1. PostgreSQL + Python

This repository includes a PostgreSQL database setup with tables for managing users, tasks, and task statuses. Below are examples of SQL queries and corresponding Python scripts to interact with the database using psycopg2.

1. Pytyhon PostgreSQL connestion
2. Create tables script (3 tables)
3. filling up database with fake data
4. Execute queries.

### To use these queries:

1. Ensure PostgreSQL is installed and running locally or within a Docker container.
2. Adjust the database connection parameters (db_config) in the Python scripts to match your environment.
3. Run the Python scripts:
   - create_tables.py: for create 3 tables(users, tasks, status)
   - seed.py: for filleng up tables with fake data
   - queries.py: for execute the queries and observe the results.

### Dependencies

psycopg2: Python library for PostgreSQL database interactions.
PostgreSQL: The relational database management system used for storing data.
fake: Python library for generate fake data

Author: _Oleksiy Verkhulevskyy_
