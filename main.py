import sqlite3
from sys import argv

DB_NAME: str = 'database.db'

class database:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, sql: str):
        # Add this stage: ID, string, int
        print("Creating new table...")
        self.cursor.execute(sql)
        self.connection.commit()


print(argv)

if len(argv) > 1 and argv[1] == 'setup':
    db = database(DB_NAME)
    db.create_table(" CREATE TABLE example_table (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT, number INTEGER)")
