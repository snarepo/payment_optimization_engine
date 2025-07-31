import sqlite3

DB_PATH = "./data/experiment.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.executescript(open("sql/create_tables.sql").read())
    conn.commit()
    conn.close()
