#  Database: A place where datas are stored, retrieved or managed
# Database management system: a system that helps manage databases
# Types
# a. Relational DBMS (SQL- Structured query language)
# Data is stored in tables (rows and columns)
# Tables are related to each other through primary and foreign keys
# e.g. MySQL, PostgreSQL, Oracle, Microsoft SQL Server, MariaDB, SQLite



# b. No SQL / Non Relational DBMS
# Data is stored in a non tabular format (key-value pairs, documents, graphs, etc.)
# e.g. MongoDB, Cassandra, Redis, CouchDB, Neo4j


import mysql.connector as sql

conn = sql.connect(
    host="localhost",
    user="root",
    password="password",
    port=3306,
    database="oct26"
)

cursor = conn.cursor()

# cursor.execute("SHOW DATABASES")
# print(cursor.fetchall())

# 1. Database definition language (DDL): used to define and manage database structures (e.g., CREATE, ALTER, DROP)

# query = "DROP DATABASE oct26"
# query = "CREATE DATABASE oct26"

query = """
    CREATE TABLE users (
        id INT PRIMARY KEY AUTO_INCREMENT,
        fullname VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        password VARCHAR(100),
        account_no VARCHAR(10) UNIQUE,
        balance DECIMAL(10, 2) DEFAULT 0.00,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
"""

# query = "ALTER TABLE users ADD COLUMN phone_number VARCHAR(15) AFTER email"
# query = "ALTER TABLE users DROP COLUMN phone_number"
# query = "ALTER TABLE users CHANGE COLUMN phone_number phone VARCHAR(15) AFTER email"

cursor.execute(query)



# 2. Database manipulation language (DML): used to manipulate data within the database (e.g INSERT, UPDATE, DELETE)
# 3. Database query language (DQL): used to query and retrieve data from the database (e.g SELECT)

