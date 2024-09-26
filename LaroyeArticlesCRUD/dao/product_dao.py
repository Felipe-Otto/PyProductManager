# Import the necessary modules and classes
from database.database_connection import SQLite3DatabaseConnection
from model.product import Product


class ProductDAO:
    def __init__(self):
        pass

    @staticmethod
    def define_key():
        try:
            query = f'SELECT MAX(ProductKey) ' \
                    f'FROM Product;'
            with SQLite3DatabaseConnection() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                if row[0] is not None:
                    return row[0] + 1
                else:
                    return 1
        except Exception as e:
            print(f'Error while trying to select the greater product key from \033[1;31mProduct\033[0m:\n{e}')

    @staticmethod
    def select_all_products():
        try:
            query = 'SELECT * FROM Product;'
            with SQLite3DatabaseConnection() as cursor:
                cursor.execute(query)
                products = cursor.fetchall()
                return products
        except Exception as e:
            print(f'Error while trying to select all data from \033[1;31mProduct\033[0m:\n{e}')

    @staticmethod
    def delete_product(product_key):
        try:
            query = f'DELETE FROM Product ' \
                    f'WHERE ProductKey = {product_key};'
            with SQLite3DatabaseConnection() as cursor:
                cursor.execute(query)
                cursor.commit()
        except Exception as e:
            print(f'Error while trying to delete data from \033[1;31mProduct\033[0m:\n{e}')

    @staticmethod
    def update_product(product):
        try:
            query = f'UPDATE  Product ' \
                    f'SET ProductName = \'{product.product_name}\', ' \
                    f'    ProductDescription = \'{product.product_description}\', ' \
                    f'    ProductPrice = {product.product_price} ' \
                    f'WHERE ProductKey = {product.product_key};'
            with SQLite3DatabaseConnection() as cursor:
                cursor.execute(query)
                cursor.commit()
        except Exception as e:
            print(f'Error while trying to update data from \033[1;31mProduct\033[0m:\n{e}')

    @staticmethod
    def insert_product(product):
        product_key = ProductDAO.define_key()
        try:
            query = f'INSERT INTO Product (ProductKey, ProductName, ProductDescription, ProductPrice) ' \
                    f'VALUES ({product_key}, \'{product.product_name}\', ' \
                    f'    \'{product.product_description}\', {product.product_price});'
            with SQLite3DatabaseConnection() as cursor:
                cursor.execute(query)
                cursor.commit()
        except Exception as e:
            print(f'Error while trying to insert data into \033[1;31mProduct\033[0m:\n{e}')

    @staticmethod
    def select_product_by_key(product_name):
        try:
            query = f'SELECT * FROM Product ' \
                    f'WHERE ProductName = \'{product_name}\';'
            with SQLite3DatabaseConnection() as cursor:
                cursor.execute(query)
                product = cursor.fetchone()
                if product is None:
                    return True
                else:
                    return False
        except Exception as e:
            print(f'Error while trying to select data from \033[1;31mProduct\033[0m with specific key:\n{e}')

    @staticmethod
    def select_product_by_id(product_key):
        try:
            query = f'SELECT * FROM Product ' \
                    f'WHERE ProductKey = {product_key};'
            with SQLite3DatabaseConnection() as cursor:
                cursor.execute(query)
                product = cursor.fetchone()
                return product

        except Exception as e:
            print(f'Error while trying to select data from \033[1;31mProduct\033[0m with specific key:\n{e}')

    @staticmethod
    def select_product_filter(query):
        try:
            with SQLite3DatabaseConnection() as cursor:
                cursor.execute(query)
                products = cursor.fetchall()
                return products
        except Exception as e:
            print(f'Error while trying to filter data from \033[1;31mProduct\033[0m:\n{e}')
