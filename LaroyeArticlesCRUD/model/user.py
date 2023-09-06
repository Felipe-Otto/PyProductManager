# Define the User model class
class User:
    def __init__(self, user_key, user_name, user_password):
        # Constructor method: initializes the attributes
        self.user_key = user_key
        self.user_name = user_name
        self.user_password = user_password

    def get_user_key(self):
        return self.user_key

    def set_user_key(self, user_key):
        self.user_key = user_key

    def get_user_name(self):
        return self.user_name

    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_user_password(self):
        return self.user_password

    def set_user_password(self, user_password):
        self.user_password = user_password
