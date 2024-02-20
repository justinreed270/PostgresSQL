import psycopg2
from psycopg2 import sql

def check_and_create_db(db_name):
    conn = psycopg2.connect(
        dbname='postgres',  # connect to default db to create new db
        user='your_username',
        host='localhost',
        password='your_password'
    )
    conn.autocommit = True  # enable autocommit to create new db
    cur = conn.cursor()

    cur.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = {}")
                .format(sql.Identifier(db_name)))

    exists = cur.fetchone()
    if not exists:
        cur.execute(sql.SQL("CREATE DATABASE {}")
                    .format(sql.Identifier(db_name)))

    cur.close()
    conn.close()

    # Connect to the new/existing database
    conn = psycopg2.connect(
        dbname=db_name,
        user='your_username',
        host='localhost',
        password='your_password'
    )
    return conn
