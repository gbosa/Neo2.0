import sqlite3
from sqlite3 import Error

def connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f'Connected to DB version: {sqlite3.version}.')
    except Error as e:
        print(e)
    return conn

def drop_table(dbname,tablename):
    sql_drop_table = f'DROP TABLE {tablename}'
    c=connection(dbname)
    c.execute(sql_drop_table) # type: ignore
    c.close # type: ignore
    return print(f'Table: {tablename} dropped.')

def insert_into_msg(dbname,tuple):
    sql_insert=f"INSERT INTO Message (name, message) VALUES (?, ?)"
    cursor = connection(dbname).cursor() # type: ignore
    cursor.execute(sql_insert, tuple)
    connection(dbname).commit() # type: ignore

def query_msg(dbname, rowid):
    sql_query = f'SELECT * FROM message WHERE rowid={rowid}'
    cursor = connection(dbname).cursor() # type: ignore 
    cursor.execute(sql_query)
    row=cursor.fetchall()
    return print(row)

if __name__ == '__main__':
    c=connection(r"frases.db")
    sql_create_msg_table = """ CREATE TABLE IF NOT EXISTS Message (
                                        name text,
                                        message text
                                    ); """
    c.execute('PRAGMA encoding="UTF-8";')  # type: ignore
    c.execute(sql_create_msg_table)  # type: ignore
    #drop_table('Message')
    c.close  # type: ignore
    print('Connection to DB closed.')