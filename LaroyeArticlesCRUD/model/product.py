class Product:
    def __init__(self, product_key, product_name, product_description, product_price):
        self.product_key = product_key
        self.product_name = product_name
        self.product_description = str(product_description).capitalize()
        self.product_price = float(product_price)

    def __eq__(self, other):
        if isinstance(other, Product):
            return (self.product_key == other.product_key and
                    self.product_name == other.product_name and
                    self.product_description == other.product_description and
                    self.product_price == other.product_price)
        return False

    def get_product_key(self):
        return self.product_key

    def set_product_key(self, product_key):
        self.product_key = product_key

    def get_product_name(self):
        return self.product_name

    def set_product_name(self, product_name):
        self.product_name = product_name

    def get_product_description(self):
        return self.product_description

    def set_product_description(self, product_description):
        self.product_description = product_description

    def get_product_price(self):
        return self.product_price
