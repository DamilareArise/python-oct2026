# Database: A place where datas are stored, retrieved or managed
# Database management system: a system that helps manage databases
# Types
# a. Relational DBMS (SQL- Structured query language)
# Data is stored in tables (rows and columns)
# Tables are related to each other through primary and foreign keys
# e.g. MySQL, PostgreSQL, Oracle, Microsoft SQL Server, MariaDB, SQLite



# b. No SQL / Non Relational DBMS
# Data is stored in a non tabular format (key-value pairs, documents, graphs, etc.)
# e.g. MongoDB, Cassandra, Redis, CouchDB, Neo4j

# pip install mysql-connector-python
import mysql.connector as sql

conn = sql.connect(
    host="localhost",
    user="root",
    password="password",
    port=3306,
    database="oct26"
)

cursor = conn.cursor()
conn.autocommit = True

# cursor.execute("SHOW DATABASES")
# print(cursor.fetchall())

# 1. Database definition language (DDL): used to define and manage database structures (e.g., CREATE, ALTER, DROP, TRUNCATE)

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

# query = "DROP TABLE users"
query = "TRUNCATE TABLE users"


# query = "ALTER TABLE users ADD COLUMN password_salt VARCHAR(100) AFTER password"

# cursor.execute(query)



# 2. Database manipulation language (DML): used to manipulate data within the database (e.g INSERT, UPDATE, DELETE)
# pip install pwinput
import hashlib, os, pwinput as pw, random as rd


def set_password():
    pass1 = pw.pwinput()
    pass2 = pw.pwinput("Confirm Password: ")
    if pass1 != pass2:
        print("Password do not match")
        return set_password()
    
    else:
        salt = os.urandom(16)
        hashed = hashlib.pbkdf2_hmac(
            "sha256",
            pass1.encode(),
            salt,
            500_000
        )

        return salt.hex(), hashed.hex()
    
# print(set_password()) 


def register():
    fullname = input("Fullname: ")
    email = input("Email: ")
    salt, hashed = set_password()
    account_no = rd.randint(1000000000, 1099999999)
    
    query = "INSERT INTO users(fullname, email, password, password_salt, account_no) VALUES(%s, %s, %s, %s, %s)"
    values = (fullname, email, hashed, salt, account_no)
    cursor.execute(query, values)
    print("Registration successful")
    
register()

# query = "UPDATE users SET fullname = %s WHERE id = %s"
# values = ("Ebunoluwa Shoyemi", 1)
# cursor.execute(query, values)


# query = "DELETE FROM users WHERE id = %s"
# value = (1,)
# cursor.execute(query,value)

    

# 3. Database query language (DQL): used to query and retrieve data from the database (e.g SELECT)

