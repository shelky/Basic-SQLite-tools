import sqlite3

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

    def insert(self, table, *values):
        print("Adding row to the table...")
        self.cursor.execute(f"INSERT INTO {table} VALUES ({','.join('?' for _ in values)})", values)
        self.connection.commit()
