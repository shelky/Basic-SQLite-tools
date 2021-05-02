from database import database
from sys import argv

DB_NAME: str = 'database.db'
print(argv)

if len(argv) == 2 and argv[1] == 'setup':
    db = database(DB_NAME)
    db.create_table(" CREATE TABLE example_table (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT, number INTEGER)")

if len(argv) > 1 and argv[1] == 'add_row':
    text = argv[2]
    number = argv[3]
    db = database(DB_NAME)
    db.insert('example_table', None, text, number)
