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

    pip install psycopg2

## 2. mangoDB + Python

File mango_CRUD.py contains Python scripts for interacting with MongoDB using the pymongo library. It includes functions for basic CRUD operations (Create, Read, Update, Delete) on a collection of cats, demonstrating how to connect to a MongoDB database, perform operations such as inserting, updating, querying, and deleting documents.

### Features

- Connecting to MongoDB: Establishing a connection to a MongoDB database using pymongo.
- Inserting Data: Functions for inserting one or multiple documents into a MongoDB collection.
- Querying Data: Retrieving data by name or fetching all documents from the collection.
- Updating Data: Updating a document's age or adding new features.
- Deleting Data: Removing a document from the collection by name or deleting all documents.

### Dependencies

pymongo: Python library for mongoDB database interactions.

    pip install pymongo

### How to use:

- Update the MongoDB connection details in the scripts (host, port, database name, collection name).
- Execute the Python scripts in your preferred environment.

### Examples:

    add_one("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    update_age("barsik", 4)
    delete_by_name("barsik")
    get_all()

Author: _Oleksiy Verkhulevskyy_
