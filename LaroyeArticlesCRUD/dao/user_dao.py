# Import the necessary modules and classes
from database.database_connection import SQLite3DatabaseConnection


class UserDAO:
    def __init__(self):
        pass

    @staticmethod
    def select_user_by_key(name, password):
        try:
            query = f'SELECT * FROM User ' \
                    f'WHERE name = \'{name}\' ' \
                    f'AND password = \'{password}\';'
            with SQLite3DatabaseConnection() as cursor:
                cursor.execute(query)
                user = cursor.fetchone()
                if user:
                    return True
                else:
                    return False
        except Exception as error:
            print(f'Error while trying to select data from \033[1;31mUser\033[0m with specific key:\n{error}')