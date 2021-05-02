import sqlite3
from sys import argv


class database:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

print(argv)

if len(argv) > 1 and argv[1] == 'setup':
    print("Creating new table...")