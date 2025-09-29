import sqlite3 as sq3


connection = sq3.connect('data.db')
cursor = connection.cursor()


def make_table(choice):

    if choice == 1:
        cursor.execute(f"DROP TABLE IF EXISTS news1;")
    if choice == 2:
        cursor.execute(f"DROP TABLE IF EXISTS news2;")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news1 (
        id INTEGER UNIQUE,
        headline TEXT,
        date INTEGER,
        month TEXT,
        column TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news2 (
        id INTEGER UNIQUE,
        headline TEXT,
        date INTEGER,
        month TEXT,
        column TEXT
    )
    """)


def get_latestID(choice):
    if choice == 1:
        cursor.execute("""
        SELECT id FROM news1 ORDER BY id DESC LIMIT 1
        """)
        last = cursor.fetchall()
        ID = (last[0][0] + 1)

        return(ID)

    if choice == 2:
        cursor.execute("""
        SELECT id FROM news2 ORDER BY id DESC LIMIT 1
        """)
        last = cursor.fetchall()
        ID = (last[0][0] + 1)

        return(ID)

def add_articles(headline, date, month, column, choice):
    if choice == 1:
        try:
            last = get_latestID(1)
        except:
            last = 1
        #try:
        cursor.execute("""
        INSERT INTO news1 VALUES 
        ({}, '{}', {}, '{}', '{}')    

        """.format(last, headline, date, month, column))
        connection.commit()
        #except:
            #print("Invalid Entries, please retry")

    if choice == 2:
        try:
            last = get_latestID(2)
        except:
            last = 1
        #try:
        cursor.execute("""
        INSERT INTO news2 VALUES 
        ({}, '{}', {}, '{}', '{}')    

        """.format(last, headline, date, month, column))
        connection.commit()
        #except:
            #print("Invalid Entries, please retry")


def all_articles(choice):
    if choice == 1:
        last = get_latestID(1)
        x = 0
        while x < last:
            cursor.execute("""
                SELECT * FROM news1
                WHERE id = '{}'
                """.format(x))

            print(cursor.fetchall())
            print('\n')

            x += 1

    if choice == 2:
        last = get_latestID(2)
        x = 0
        while x < last:
            cursor.execute("""
                SELECT * FROM news2
                WHERE id = '{}'
                """.format(x))

            print(cursor.fetchall())
            print('\n')

            x += 1

