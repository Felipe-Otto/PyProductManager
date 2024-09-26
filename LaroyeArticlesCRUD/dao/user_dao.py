# Import the necessary modules and classes
from database.database_connection import SQLite3DatabaseConnection


class UserDAO:
    def __init__(self):
        pass

    @staticmethod
    def define_key():
        try:
            query = f'SELECT MAX(UserKey) ' \
                    f'FROM User;'
            with SQLite3DatabaseConnection() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                if row[0] is not None:
                    return row[0] + 1
                else:
                    return 1
        except Exception as e:
            print(f'Error while trying to select the greater user key from \033[1;31mUser\033[0m:\n{e}')

    @staticmethod
    def select_user_by_key(user_name):
        try:
            query = f'SELECT * FROM User ' \
                    f'WHERE username = \'{user_name}\';'
            with SQLite3DatabaseConnection() as cursor:
                cursor.execute(query)
                user = cursor.fetchone()
                if user:
                    return True
                else:
                    return False
        except Exception as error:
            print(f'Error while trying to select data from \033[1;31mUser\033[0m with specific key:\n{error}')

    @staticmethod
    def insert_user(user):
        user_key = UserDAO.define_key()
        try:
            query = f'INSERT INTO User (UserKey, UserName, UserPassword) ' \
                    f'VALUES ({user_key}, \'{user.user_name}\', \'{user.user_password}\');'
            with SQLite3DatabaseConnection() as cursor:
                cursor.execute(query)
                cursor.commit()
        except Exception as e:
            print(f'Error while trying to insert data into \033[1;31mUser\033[0m:\n{e}')

    @staticmethod
    def select_user_credentials(user):
        try:
            query = f'SELECT * FROM User ' \
                    f'WHERE username = \'{user.user_name}\'' \
                    f'AND userpassword = \'{user.user_password}\';'
            with SQLite3DatabaseConnection() as cursor:
                cursor.execute(query)
                user = cursor.fetchone()
                if user:
                    return True
                else:
                    return False
        except Exception as error:
            print(f'Error while trying to select data from \033[1;31mUser\033[0m with specific key:\n{error}')
