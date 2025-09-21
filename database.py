import sqlite3 as sq3


connection = sq3.connect('data.db')
cursor = connection.cursor()


def make_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER UNIQUE,
        headline TEXT,
        date INTEGER,
        month TEXT,

    )
    """)