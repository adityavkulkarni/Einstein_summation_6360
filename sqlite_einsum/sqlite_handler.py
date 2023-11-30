import sqlite3
import time


class SQLiteHandler:
    def __init__(self, db_name, debug=False):
        self.db_name = None
        self.connection = None
        self.cursor = None
        self._debug = debug
        self._connect(db_name)

    def _log(self, s):
        if self._debug:
            print(s)

    def _connect(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self._log(f"--- Connected to SQLite database: {self.db_name} ---\n")

    def check_table_exist(self, name):
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name}';"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return True if result else False

    def execute_query(self, query):
        start_time = time.time()
        self.cursor.execute(query)
        end_time = time.time()
        self.connection.commit()
        self._log(f"--- Query executed successfully:\n {query}")
        self._log(f"--- {format((end_time - start_time)*1000, '.5f')} seconds ---\n")

    def fetch_all_rows(self, query):
        start_time = time.time()
        self.cursor.execute(query)
        end_time = time.time()
        rows = self.cursor.fetchall()
        self._log(f"--- Query executed successfully:\n {query}")
        if rows:
            for row in rows:
                self._log(row)
        self._log(f"--- {format(end_time - start_time, '.5f')} seconds ---\n")
        return rows, format((end_time - start_time)*1000, '.5f')

    def close_connection(self):
        self.connection.close()
        self._log("\n--- Connection closed  ---\n")


if __name__ == "__main__":
    sqlite_handler = SQLiteHandler("example.db")

    create_table_query = """CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER); """
    sqlite_handler.execute_query(create_table_query)

    insert_data_query = "INSERT INTO students (name, age) VALUES ('John Doe', 25);"
    for i in range(100):
        sqlite_handler.execute_query(insert_data_query)

    select_query = "SELECT * FROM students;"
    results = sqlite_handler.fetch_all_rows(select_query)

    sqlite_handler.close_connection()
