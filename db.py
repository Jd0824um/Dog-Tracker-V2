import sqlite3
import logging


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
        logging.info(sqle.with_traceback)
        print('An error has occurred')

    # Closes connections
    finally:
        conn.close()


def add_holder(Holder):
    try:
        # Connects to DB
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        # Sql template/statement to add a new record holder to the database using prepared and parametrize statements
        sql_template = 'INSERT INTO {} ({}, {}, {}) VALUES (?, ?, ?))'\
            .format(RECORDS_TABLE, NAME, COUNTRY, NUMBER_OF_CATCHES)

        sql_values = (Holder.name, Holder.country, Holder.catches)

        cur.execute(sql_template, sql_values)

        logging.info("Added record holder " + Holder.name)

    except sqlite3.Error as sqle:
        print('An error has occurred')
        logging.info(sqle.with_traceback)

        # Closes connections
    finally:
        conn.close()


def search_holder(name):
    try:
        # Connects to DB
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        # Query to search for the requested holder by name using a parametrized statement
        sql_query = 'SELECT * FROM {} WHERE {} = ?'.format(RECORDS_TABLE, NAME)

        sql_values = name

        logging.info("Searched for " + name)

        return cur.execute(sql_query, sql_values)

    except sqlite3.Error as sqle:
        print('An error has occurred')
        logging.info(sqle.with_traceback)

        # Closes connections
    finally:
        conn.close()


def update_catches(name, catches):
    try:
        # Connects to DB
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        # Uses a update query to update the catches of a record holder
        sql_template = 'UPDATE {} SET {} = ? WHERE {} = ?'.format(RECORDS_TABLE, NUMBER_OF_CATCHES, NAME)

        sql_values = (catches, name)

        cur.execute(sql_template, sql_values)

        logging.info("Catches were updated for " + name + " to " + catches)

        # returns true if the catches were updated
        return cur.rowcount > 0

    except sqlite3.Error as sqle:
        print('An error has occurred')
        logging.info(sqle.with_traceback)

        # Closes connections
    finally:
        conn.close()


def delete_holder(name):
    try:
        # Connects to DB
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        # Deletes a holder by name from the database.
        sql_template = 'DELETE FROM {} WHERE {} = ?'.format(RECORDS_TABLE, NAME)
        sql_values = name

        cur.execute(sql_template, sql_values)

        logging.info("Deleted " + name)

        # Returns true if the holder was deleted
        return cur.rowcount > 0

    except sqlite3.Error as sqle:
        print('An error has occurred')
        logging.info(sqle.with_traceback)

        # Closes connections
    finally:
        conn.close()
