# Define the User model class
class User:
    def __init__(self, user_key, name, password):
        # Constructor method: initializes the attributes
        self.user_key = user_key
        self.name = name
        self.password = password