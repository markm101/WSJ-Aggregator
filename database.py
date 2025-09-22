import sqlite3 as sq3


connection = sq3.connect('data.db')
cursor = connection.cursor()


def make_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER UNIQUE,
        headline TEXT,
        date INTEGER,
        month TEXT
    )
    """)

def get_latestID():
    cursor.execute("""
    SELECT id FROM news ORDER BY id DESC LIMIT 1
    """)
    last = cursor.fetchall()
    ID = (last[0][0] + 1)

    return(ID)

def add_articles(headline, date, month):
    try:
        last = get_latestID()
    except:
        last = 1
    try:
        cursor.execute("""
        INSERT INTO news VALUES 
        ({}, '{}', {}, {})
        
        
        """.format(last, headline, date, month))
        connection.commit()
    except:
        print("Invalid Entries, please retry")


def all_articles():

    num = get_latestID()
    i = 0
    while i < 3:
        cursor.execute("""
        SELECT * FROM news
        WHERE id = '{}'
        """.format(i))

        print(cursor.fetchall())
