import sqlite3
from sqlite3 import Error

class Cerebelo:
    def __init__(self, dbname):
        self.db=dbname
        self.conn=sqlite3.connect(self.db)
        
    # def connection(self):
    #     """ create a database connection to a SQLite database """
    #     conn = None
    #     try:
    #         conn = sqlite3.connect(self.db)
    #         print(f'Connected to DB version: {sqlite3.version}.')
    #     except Error as e:
    #         print(e)
    #     return conn

    def drop_table(self, tablename):
        
        sql_drop_table = f'DROP TABLE {tablename}'
        cursor = self.conn.cursor() # type: ignore
        cursor.execute(sql_drop_table) # type: ignore
        cursor.close()
        self.conn.close() # type: ignore
        
        return print(f'Table: {tablename} dropped.')

    def insert_into_msg(self,tuple):
        
        sql_insert=f"INSERT INTO Message (name, message) VALUES (?, ?)"
        cursor = self.conn.cursor() # type: ignore
        cursor.execute(sql_insert, tuple)
        self.conn.commit() # type: ignore
        cursor.close()
        
    def add_status(self,tuple):
        
        sql_insert=f"INSERT INTO chat_status (chat_id, status) VALUES (?, ?)"
        cursor = self.conn.cursor() # type: ignore
        cursor.execute(sql_insert, tuple)
        self.conn.commit() # type: ignore
        cursor.close()


    def update_status(self, tuple):
        
        sql_update=f"UPDATE chat_status SET status = {tuple[1]} where chat_id = {tuple[0]}"
        cursor = self.conn.cursor() # type: ignore
        cursor.execute(sql_update)
        self.conn.commit() # type: ignore
        cursor.close()
    
    def get_status(self,chat_id):
        
        sql_get_status=f"SELECT status FROM chat_status WHERE chat_id = {chat_id}"
        cursor = self.conn.cursor() # type: ignore
        cursor.execute(sql_get_status)
        status=cursor.fetchone() # type: ignore
        cursor.close()
        
        return bool(int(status[0]))
    
    def query_rowid(self, rowid):
        
        sql_query = f'SELECT *, rowid FROM message WHERE rowid={rowid}'
        cursor = self.conn.cursor() # type: ignore 
        cursor.execute(sql_query)
        row=cursor.fetchone()
        cursor.close()
        
        return row

    def query_name(self, name):
        
        sql_query = f'SELECT *, rowid FROM message WHERE name="{name}"'
        cursor = self.conn.cursor() # type: ignore 
        cursor.execute(sql_query)
        row=cursor.fetchone()
        cursor.close()
        
        return row

    def query_msg(self, msg):
        try:
            sql_query = f'SELECT *, rowid FROM message WHERE message like "%{msg}%"'
            cursor = self.conn.cursor() # type: ignore 
            cursor.execute(sql_query)
            row=cursor.fetchone()
            cursor.close()
            return row
        except:
            return print(Error)

    def execute_sql(self, sql) -> None:
        cursor=self.conn.cursor()
        cursor.execute(sql)
        return print('SQL command executed.')
    
    def query_command_quem(self, msg):
        sql_query = f'SELECT name FROM message WHERE message like "%{msg}%"'
        cursor = self.conn.cursor() # type: ignore 
        cursor.execute(sql_query)
        row=cursor.fetchall()
        cursor.close()       
        
        return set([a[0] for a in row])

    def close_conn(self):
        self.conn.close()
        return print(f'Connection to {self.db} closed.')

if __name__ == '__main__':
    Brain=Cerebelo('frases.db')
    c=Brain.conn
    sql_create_status = """ CREATE TABLE IF NOT EXISTS chat_status (
                                        chat_id INT PRIMARY KEY,
                                        status text
                                    ); """
    sql_create_message = """ CREATE TABLE IF NOT EXISTS messages (
                                        name text,
                                        message text
                                    ); """
    
    c.execute('PRAGMA encoding="UTF-8";')  # type: ignore
    Brain.execute_sql(sql_create_message)  # type: ignore
    Brain.execute_sql(sql_create_status)
    Brain.close_conn()  # type: ignore
    