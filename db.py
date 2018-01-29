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
