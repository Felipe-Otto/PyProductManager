# Import the necessary modules
from pyodbc import connect, Error


# Define a class for SQLite3 database database
class SQLite3DatabaseConnection:
    def __init__(self, driver='{SQLite3 ODBC Driver}', database='..\database\LaroyeStore.db'):
        try:
            # Construct the database string and establish a database
            connection_string = f'Driver={driver};Database={database}'
            self.connection = connect(connection_string)
            self.cursor = self.connection.cursor()
            print('foi sim fio')
        except Error as error:
            # Handle database errors
            print(f'\033[91mError while trying to connect with database: {error}\033[0m')
            self.connection = None
            self.cursor = None

    def __enter__(self):
        # Context manager method: executed upon entering the context
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Context manager method: executed upon exiting the context
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
