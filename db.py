import sqlite3

DB_NAME = 'Juggling_Records.db'
RECORDS_TABLE = 'Records'
NAME = 'Chainsaw Juggling Record Holder'
COUNTRY = 'Country'
NUMBER_OF_CATCHES = 'Number of Catches'


def setup():
    try:
        # Connects to DB
        conn = sqlite3.connect(DB_NAME)

        # Creates a table if it doesn't exist using prepared statements
        sql_statement = 'CREATE TABLE IF NOT EXISTS {} ( {} TEXT, {} TEXT, {} INTEGER)'\
            .format(RECORDS_TABLE, NAME, COUNTRY, NUMBER_OF_CATCHES)

        conn.execute(sql_statement)
        conn.commit()

    except sqlite3.Error as sqle:
        print('An error has occurred')
        print(sqle)

    # Closes connections
    finally:
        conn.close()


def add_holder():
    try:
        # Connects to DB
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        # Sql template/statement to add a new record holder to the database using prepared and parametrize statements
        sql_template = 'INSERT INTO {} ({}, {}, {}) VALUES (?, ?, ?))'\
            .format(RECORDS_TABLE, NAME, COUNTRY, NUMBER_OF_CATCHES)

        sql_values = (holder.name, holder.country, holder.catches)

        cur.execute(sql_template, sql_values)

    except sqlite3.Error as sqle:
        print('An error has occurred')
        print(sqle)

        # Closes connections
    finally:
        conn.close()


def search_holder(name):
    try:
        # Connects to DB
        conn = sqlite3.connect(DB_NAME)

        # Query to search for the requested holder by name
        sql_query = 'SELECT * FROM {} WHERE {} = {}'.format(RECORDS_TABLE, NAME, name)

        return sql_query

    except sqlite3.Error as sqle:
        print('An error has occurred')
        print(sqle)

        # Closes connections
    finally:
        conn.close()
