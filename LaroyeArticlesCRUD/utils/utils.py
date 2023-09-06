# Importing necessary libraries
from customtkinter import CTkToplevel, CTkLabel, CTk

from model.user import User
from styles.styles import DARK_GRAY_COLOR, RED_COLOR, GREEN_COLOR, MESSAGE_FONT
from model.product import Product
from dao.product_dao import ProductDAO
from dao.user_dao import UserDAO

# Dictionary that saves windows identifier
window_identifier = {'Login': None, 'Sign up': None, 'Menu': None, 'Register': None, 'Deleter': None, 'Editor': None}


def create_window(properties, preceding=None):
    """
    Creates the specified window.

    Args:
        properties (dict): Specifications of the window.
            - width (int): Width of the window to be created.
            - height (int): Height of the window to be created.
            - id (str): ID of the window to be created.
        preceding (CTk, optional): Determine whether the screen being created overlaps with any existing screens.
    Returns:
        window (customtkinter.windows.ctk_tk.CTk): Window constructed with passed parameters.
    """

    # Creating Window
    window = CTkToplevel(preceding) if preceding else CTk()

    # Setting window title
    window.title(properties['id'])

    # Storing window identifier
    window_identifier[properties['id']] = window.winfo_id()

    # Defining background screen color
    window.configure(bg=DARK_GRAY_COLOR)

    # Obtaining computer screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculating coordinates to center window on the computer screen
    position_x = (screen_width // 2) - (properties['width'] // 2)
    position_y = (screen_height // 2) - (properties['height'] // 2)

    # Centering window on the computer screen
    window.geometry(f'{properties["width"]}x{properties["height"]}+{position_x}+{position_y}')

    # Returning window
    return window


def generate_message(window, properties, temporary=False):
    """
    Positions the specified message in the window.

    Args:
        window (CTk): Window where message will be positioned.
        properties (dict): Specifications of the message.
            - 'text' (str): Message text content.
            - 'row' (int): Row in the window grid where the message will be positioned.
            - 'column (int)': Column in the window grid where the message will be positioned.
            - 'columnspam' (int): Number of columns the message will occupy.
            - 'pady' (tuple): Message vertical borders (top border, bottom border).
            - 'text_color' (str): Message text color.
        temporary (bool, optional): Parameter used to determine if message should be temporarily displayed on the window.
    Returns:
        None
    """

    # Creating message
    message_label = CTkLabel(window, text=properties['text'], font=MESSAGE_FONT, text_color=properties['text_color'])
    # Positioning message on the window
    message_label.grid(row=properties['row'], column=properties['column'], columnspan=properties['columnspan'],
                       pady=properties['pady'], sticky='we')

    # Removing the message from the window after 1.5 s
    if temporary: message_label.after(1500, message_label.destroy)


def populate_treeview(treeview, enable_filter=False, query=None):
    """
    Populates treeview (TKinter library method) fields with product data from database.

    Args:
        treeview (Tkinter.ttk.Treeview): Treeview that will be populate with data.
        enable_filter (bool, optional): Determines whether the listing should be done with filter. If is set to True,
                                        query variable will be used as a parameter for the listing.
        query (str, optional): Query used for listing.
    Returns:
        treeview (Tkinter.ttk.Treeview): Treeview populated with product data.
    """

    # Cleaning treeview values
    treeview = clear_treeview(treeview)

    # Selecting product data
    products = ProductDAO().select_product_filter(query) if enable_filter else ProductDAO().select_all_products()

    # Populating treeview with product data
    [treeview.insert('', 'end', values=(product[0], product[1], product[2], product[3])) for product in products]

    # Returning treeview
    return treeview


def clear_treeview(treeview):
    """
    Cleans passed treeview fields.

    Args:
        treeview (Tkinter.ttk.Treeview): Treeview that will have fields clean.
    Returns:
        treeview (Tkinter.ttk.Treeview): Treeview with clean fields.
    """

    # Cleaning treeview fields
    [treeview.delete(row) for row in treeview.get_children()]

    # Returning treeview
    return treeview


def handling_input(window, user=None, product=None, treeview=None):
    """
    Treats the entries values, avoiding data non-standardization

    Args:
        window (CTk): Window open during entries values (Login, Register or Editor).
        user (dict, optional): Login values entered
            - username (str): Username value entered
            - password (str): Password value entered
            - confirm (str, optional): Password confirmation value entered
        product (dict, optional): Product values entered
            - id (int, optional): Product identifier value
            - name (str): Product name value
            - description (str): Product description value
            - price (str): Product price value
        treeview (Tkinter.ttk.Treeview, optional): Treeview that will be repopulated.
    Returns:
        user (User): User object to check credentials
    """

    # Treating login values entered
    if window.winfo_id() == window_identifier['Login']:
        # Defining the foundation of message properties
        message_properties = {'row': 3, 'column': 0, 'columnspan': 3, 'pady': 0, 'text_color': RED_COLOR}
        # Checking if login username and password fields are empty
        if not user['username'] and not user['password']:
            # Defining message text and positioning it
            message_properties['text'] = 'Please fill in the fields above'
            generate_message(window, message_properties)
        # Checking if login username field is empty
        elif not user['username']:
            # Defining message text and positioning it
            message_properties['text'] = 'Please fill in the username field'
            generate_message(window, message_properties)
        # Checking if login password field is empty
        elif not user['password']:
            # Defining message text and positioning it
            message_properties['text'] = 'Please fill in password field'
            generate_message(window, message_properties)
        else:
            # Creating an user object
            user = User(None, user['username'], user['password'])
            return user
    # Treating sing-up values entered
    elif window.winfo_id() == window_identifier['Sign up']:
        # Defining the foundation of message properties
        message_properties = {'row': 4, 'column': 0, 'columnspan': 3, 'pady': 0, 'text_color': RED_COLOR}
        # Checking if sign-up username password and confirm password fields are empty
        if not user['username'] and not user['password'] and not user['confirm']:
            # Defining message text and positioning it
            message_properties['text'] = 'Please fill in the fields above'
            generate_message(window, message_properties)
        # Checking if sign-up username field is empty
        elif not user['username']:
            # Defining message text and positioning it
            message_properties['text'] = 'Please fill in the username field'
            generate_message(window, message_properties)
        # Checking if sign-up password field is empty
        elif not user['password']:
            # Defining message text and positioning it
            message_properties['text'] = 'Please fill in password field'
            generate_message(window, message_properties)
        # Checking if sign-up confirm password field is empty
        elif not user['confirm']:
            # Defining message text and positioning it
            message_properties['text'] = 'Please fill in confirm password field'
            generate_message(window, message_properties)
        # Checking if the sign-up password matches the typed confirmation.
        elif user['confirm'] != user['password']:
            # Defining message text and positioning it
            message_properties['text'] = 'Password does not match the confirmation'
            generate_message(window, message_properties)
        else:
            # Creating an user object
            user = User(None, user['username'], user['password'])
            insert_user(window, user)
    else:
        # Defining the foundation of message properties
        message_properties = {'row': 4, 'column': 0, 'columnspan': 4, 'pady': 0, 'text_color': RED_COLOR}
        # Checking if product price  and name fields is empty
        if not product['name'] and not product['price']:
            # Defining message text and positioning it
            message_properties['text'] = 'Please fill in the fields above'
            generate_message(window, message_properties)
        # Checking if product name field is empty
        elif not product['name']:
            # Defining message text and positioning it
            message_properties['text'] = 'Please fill in the product name field'
            generate_message(window, message_properties)
        # Checking if product price field is empty
        elif not product['price']:
            # Defining message text and positioning it
            message_properties['text'] = 'Please fill in the product price field'
            generate_message(window, message_properties)
        # Treating product price entered
        elif not product['price'].replace('.', '', 1).isdigit():
            # Defining message text
            message_properties['text'] = 'Please fill a valid product price'
            # Positioning message on the window
            generate_message(window, message_properties)
        else:
            # Transforming price variable type (str to float)
            product['price'] = float(product['price'])
            # Creating a product object
            product = Product(product['id'], product['name'], product['description'], product['price'])
            # Identifying what window is open at the moment to forward to the right functionality
            if window.winfo_id() == window_identifier['Register']:
                insert_product(window, product, treeview)
            else:
                update_product(window, product, treeview)


def insert_user(window, user):
    """
    Checks if user already registered and insert into databse

    Args:
        window (CTk): Sign Up window.
        user (User): Specification of the user
            - name (str): User name entered that will be checked for insert.
            - password (str): User password entered that will be inserted.
    Returns:
        None
    """
    # Defining the foundation of message properties
    message_properties = {'row': 4, 'column': 0, 'columnspan': 3, 'pady': 0}
    # Checking existence of the product on the database
    if UserDAO().select_user_by_key(user.user_name):
        # Defining the rest of the message properties and positioning it
        message_properties.update({'text': 'Username already in use', 'text_color': RED_COLOR})
        generate_message(window, message_properties)
    else:
        # Inserting user on database
        UserDAO().insert_user(user)
        # Defining the rest of the message properties and positioning it
        message_properties.update({'text': 'User successfully registered', 'text_color': GREEN_COLOR})
        generate_message(window, message_properties)
        # Closing window after 1.5 s of the 'Create user' button being pressed
        window.after(1500, window.destroy)


def insert_product(window, product, treeview):
    """
    Checks if product already registered and insert into database.

    Args:
        window (CTk): Register window.
        product (Product): Specifications of the product.
            - name (str): Product name entered that will be checked for insert.
            - price (float): Product price entered that will be inserted.
            - description (str): Product description entered that will be inserted.
        treeview (Tkinter.ttk.Treeview): Treeview that will be repopulated.
    Returns:
        None
    """

    # Defining the foundation of message properties
    message_properties = {'row': 4, 'column': 0, 'columnspan': 4, 'pady': 0}

    # Checking existence of the product on the database
    if not ProductDAO().select_product_by_key(product.product_name):
        # Defining the rest of the message properties and positioning it
        message_properties.update({'text': 'Please insert a non registered product', 'text_color': RED_COLOR})
        generate_message(window, message_properties)
    else:
        # Inserting product on database
        ProductDAO().insert_product(product)
        # Defining the rest of the message properties and positioning it
        message_properties.update({'text': 'Product successfully registered', 'text_color': GREEN_COLOR})
        generate_message(window, message_properties)

        # Repopulating treeview fields
        populate_treeview(treeview)

        # Closing window after 1.5 s of the 'Register' button being pressed
        window.after(1500, window.destroy)


def update_product(window, product, treeview):
    """
    Verifies if the values were changed, updates information of the chosen product in the database and repopulate treeview.

    Args:
        window (CTk): Editor window witch calls this function.
        product (Product): Product object.
            - id (int): Identifier of the passed product.
            - name (str): New product name entered.
            - description (str): New product description entered.
            - price (float) New product price entered.
        treeview (Tkinter.ttk.Treeview): Treeview that will be repopulated.
    Returns:
        None
    """

    # Defining the foundation of message properties
    message_properties = {'row': 4, 'column': 0, 'columnspan': 4, 'pady': 0}

    # Creating a new object with the values of selection by key
    select = Product(*ProductDAO().select_product_by_id(product.product_key))

    # Comparing objects to identify if changed any value
    if product == select:
        # Defining message text and positioning it
        message_properties.update({'text': 'Please, fill in fields above with new values ', 'text_color': RED_COLOR})
        generate_message(window, message_properties)
    else:
        # Updating product on the database
        ProductDAO().update_product(product)

        # Defining message text and positioning it
        message_properties.update({'text': 'Data successfully updated', 'text_color': GREEN_COLOR})
        generate_message(window, message_properties)

        # Updating The Product List In The Main Window
        populate_treeview(treeview)

        # Closing Product Editor Window Automatically After 3 Seconds After Pressed 'Update' Button
        window.after(1500, window.destroy)


def delete_product(window, confirmation_window, product_id, treeview):
    """
    Deletes the chosen product in the database and repopulate treeview.

    Args:
        window (CTk): Window open during delete command.
        confirmation_window (CTk): Window of delete confirmation.
        product_id (int): ID of the chosen product.
        treeview (Tkinter.ttk.Treeview): Treeview that will be repopulated.
    Returns:
        None
    """

    # Closing confirmation window
    confirmation_window.destroy()

    # Deleting product from database
    ProductDAO().delete_product(product_id)

    # Defining the foundation of message properties
    message_properties = {'text': 'Data Successfully Deleted!', 'row': 4, 'text_color': GREEN_COLOR}

    # Identifying which window will receive the message (Editor or Main)
    if window.winfo_id() == window_identifier['Editor']:
        # Defining the rest of the message properties and positioning it
        message_properties.update({'column': 0, 'columnspan': 4, 'pady': 0})
        generate_message(window, message_properties)

        # Closing window after 1.5 s of the 'Delete' button being pressed
        window.after(1500, window.destroy)
    else:
        # Defining the rest of the message properties and positioning it
        message_properties.update({'column': 5, 'columnspan': 9, 'pady': 15})
        generate_message(window, message_properties, temporary=True)

    # Repopulating treeview fields
    populate_treeview(treeview)


def filter_treeview(filter, treeview):
    """
    Filters the products in the menu according to what is being typed in the product name and description fields.

    Args:
        filter (dict): Filter with product name and description entered.
            - name (str): Product name entered on filter field.
            - description (str): Product description entered on filter field.
        treeview (Tkinter.ttk.Treeview): Treeview that will be repopulated.
    Returns:
        None
    """

    # Checking if product name and description fields is empty
    if not filter['name'] and not filter['description']:
        return populate_treeview(treeview)
    else:
        # Constructing query according with what is being typed
        query = f'SELECT * FROM Product '
        where = ''
        if filter['name']:
            where += f'ProductName LIKE \'{filter["name"]}%\' '
        if filter['description']:
            if where:
                where += 'AND '
            where += f'ProductDescription LIKE \'{filter["description"]}%\' '
        if where:
            query += f'WHERE {where}'

        # Repopulating a treeview
        populate_treeview(treeview, enable_filter=True, query=query)


