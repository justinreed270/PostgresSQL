import psycopg2
from psycopg2 import sql

def create_database(database_name):
    conn = psycopg2.connect(dbname='postgres', user='your_username', password='your_password', host='localhost')
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), (database_name,))
    exists = cursor.fetchone()
    if not exists:
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database_name)))
        print("Database created.")
    else:
        print("Database already exists.")

    cursor.close()
    conn.close()

create_database('database_name')
