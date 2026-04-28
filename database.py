import sqlite3

DB_NAME = "files.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY,
            name TEXT,
            path TEXT,
            ext TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_file(name, path, ext):
    conn = connect()
    c = conn.cursor()

    c.execute("INSERT INTO files (name, path, ext) VALUES (?, ?, ?)",
              (name, path, ext))

    conn.commit()
    conn.close()

def get_all_files():
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT name, path, ext FROM files")
    rows = c.fetchall()

    conn.close()
    return rows
