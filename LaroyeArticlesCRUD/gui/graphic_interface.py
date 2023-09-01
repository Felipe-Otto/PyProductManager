# Importing necessary libraries
from customtkinter import CTkEntry, CTkButton, CTkImage
from tkinter import ttk, Menu, CENTER, NO, StringVar
from utils.utils import *
from PIL import Image
from styles.styles import *


# Function that creates login window
def login_window():
    # Defining window properties
    window_properties = {'width': 450, 'height': 250, 'id': 'Login'}

    # Function That Creates Window
    login_window = create_window(window_properties)

    # Defining Images Icon For The Register Product (30px)
    user_icon = CTkImage(dark_image=Image.open('../images/user_icon.png'), size=(30, 30))
    password_icon = CTkImage(dark_image=Image.open('../images/password_icon.png'), size=(30, 30))

    # Crating Window Labels
    title_label = CTkLabel(login_window, text='Login Screen', font=TITTLE_FONT, width=window_properties['width'])
    title_label.grid(row=0, column=0, columnspan=3, pady=(10, 30), sticky='ew')

    # Positioning Icons On The Window
    user_icon_label = CTkLabel(login_window, image=user_icon, text='')
    user_icon_label.grid(row=1, column=0, sticky='ew', padx=(0, 55))

    password_icon_label = CTkLabel(login_window, image=password_icon, text='')
    password_icon_label.grid(row=2, column=0, sticky='ew', padx=(0, 55), pady=(20, 5))

    # Positioning Window Entries
    username_entry = CTkEntry(login_window, font=ENTRIES_FONT, width=200, height=32, placeholder_text='Username')
    username_entry.grid(row=1, column=0, columnspan=4, sticky='we', padx=(100, 70))

    password_entry = CTkEntry(login_window, font=ENTRIES_FONT, width=200, height=32, placeholder_text='Password',
                              show='•')
    password_entry.grid(row=2, column=0, columnspan=4, sticky='we', padx=(100, 70), pady=(20, 5))

    # Creating Screen Buttons
    sing_up_button = CTkButton(login_window, text='Sign Up', font=BUTTON_FONT, width=125, height=32,
                               command=login_window.destroy,
                               fg_color=MEDIUM_GRAY_COLOR, hover_color='green')
    sing_up_button.place(x=50, y=195)

    sing_in_button = CTkButton(login_window, text='Sign In', font=BUTTON_FONT, width=125, height=32,
                               fg_color=MEDIUM_GRAY_COLOR,
                               hover_color='green', command=lambda: handling_input(login_window,
                                                                                   {'username': username_entry.get(),
                                                                                    'password': password_entry.get()}))
    sing_in_button.place(x=275, y=195)

    # Starting Screen
    login_window.mainloop()


# Function that creates main window
def main_window():
    # Defining window properties
    window_properties = {'width': 1100, 'height': 715, 'id': 'Menu'}

    # Function That Creates Window
    main_window = create_window(window_properties)

    # Defining Images Icon For The Register Product (30px)
    product_icon = CTkImage(dark_image=Image.open('../images/product_icon.png'), size=(30, 30))
    description_icon = CTkImage(dark_image=Image.open('../images/description_icon.png'), size=(30, 30))

    # Configuring The Screen To Contain A Menu Bar
    menu_bar = Menu(main_window)
    main_window.configure(menu=menu_bar)

    # Crating Window Labels
    title_label = CTkLabel(main_window, text='Products View', font=TITTLE_FONT, width=window_properties['width'])
    title_label.grid(row=0, column=0, columnspan=20, padx=(0, 8), pady=(10, 30), sticky='ew')

    # Positioning Icons On The Window
    product_icon_label = CTkLabel(main_window, image=product_icon, text='')
    product_icon_label.grid(row=1, column=0, padx=(50, 0), pady=(0, 10), sticky='w')

    description_icon_label = CTkLabel(main_window, image=description_icon, text='')
    description_icon_label.grid(row=1, column=18, columnspan=2, padx=(4, 0), pady=(0, 10), sticky='w')

    # Positioning Window Entries
    product_name_filter_entry = CTkEntry(main_window, font=ENTRIES_FONT, width=200, height=32,
                                         placeholder_text='Product Name')
    product_name_filter_entry.grid(row=1, column=0, padx=(77, 0), pady=(0, 10))

    # Product Description Label
    product_description_filter_entry = CTkEntry(main_window, font=ENTRIES_FONT, width=200, height=32,
                                                placeholder_text='Product Description')
    product_description_filter_entry.grid(row=1, column=19, padx=(0, 50), pady=(0, 10))

    # Creating A Treeview For Data Visualization
    # Defining Treeview Style
    treeview_style = ttk.Style(main_window)
    # Picking A Theme
    treeview_style.theme_use('default')
    # Configuring Treeview Colors
    treeview_style.configure('Treeview', background='#3C3F41',
                             fieldbackground='#3C3F41',
                             font=('Ariel', 12),
                             foreground='#BBBBBB',
                             rowheight=25)
    # Changing Selected Row Color
    treeview_style.map('Treeview', background=[('selected', '#697E37')])
    # Creating TreeView
    treeview = ttk.Treeview(main_window, show='headings', height=20)
    # Defining Treeview Columns
    treeview['columns'] = ('ProductKey', 'Name', 'Description', 'Price')
    # Creating Treeview Headers
    treeview.heading('ProductKey', text='Product Key')
    treeview.heading('Name', text='Product Name')
    treeview.heading('Description', text='Product Description')
    treeview.heading('Price', text='Product Price')
    # Changing Header Font Propriety's
    treeview_style.configure("Treeview.Heading", font=('Arial bold', 13), background='#2B2B2B', foreground='#BBBBBB',
                             rowheight=40)
    # Changing Selected Header Column Color
    treeview_style.map('Treeview.Heading', background=[('selected', '#697E37')])
    # Defining Columns Width:
    treeview.column('#0', width=0, stretch=NO)
    treeview.column('ProductKey', width=150, anchor=CENTER)
    treeview.column('Name', width=300, anchor=CENTER)
    treeview.column('Description', width=500, anchor=CENTER)
    treeview.column('Price', width=150, anchor=CENTER)

    # Positioning Treeview
    treeview.grid(row=3, column=0, columnspan=20, sticky='ew')

    # Creating Screen Buttons
    delete_product_button = CTkButton(main_window, text='Delete', font=BUTTON_FONT, width=300, height=32,
                                      fg_color=MEDIUM_GRAY_COLOR,
                                      hover_color='green',
                                      command=lambda: confirmation(main_window,
                                                                   treeview.item(treeview.selection())['values'],
                                                                   treeview))
    delete_product_button.place(x=100, y=653)

    # Continue Button
    register_product_button = CTkButton(main_window, text='Register Product', font=BUTTON_FONT, width=300, height=32,
                                        fg_color=MEDIUM_GRAY_COLOR, hover_color='green',
                                        command=lambda: register_window(main_window, treeview))
    register_product_button.place(x=700, y=653)

    # Updating Products Data List
    treeview = populate_treeview(treeview)

    # Adding Double Click Event On Treeview To Edit Products Data
    treeview.bind('<Double-1>', lambda event: editor_window(main_window, treeview))

    # Adding Typing Recognizer Event On Product Name Filter Field
    product_name_filter_entry.bind('<KeyRelease>', lambda event: filter_treeview({'name': product_name_filter_entry.get(),
                                                                                  'description': product_description_filter_entry.get()},
                                                                                 treeview))

    # Adding Typing Recognizer Event On Product Description Filter Field
    product_description_filter_entry.bind('<KeyRelease>',
                                          lambda event: filter_treeview({'name': product_name_filter_entry.get(),
                                                                         'description': product_description_filter_entry.get()},
                                                                        treeview))

    # Creating A Menu Named 'Files'
    menu_file = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Files', menu=menu_file)

    # Implementing The Menu With The Register Functionality
    menu_file.add_command(label='Register', command=lambda: register_window(main_window, treeview))

    # Implementing The Menu With The Exit Functionality
    menu_file.add_command(label='Exit', command=main_window.destroy)

    # Starting Screen
    main_window.mainloop()


# Function that creates product editor window
def editor_window(main_window, treeview):
    # Defining window properties
    window_properties = {'width': 450, 'height': 301, 'id': 'Editor'}

    # Function That Creates Window
    editor_window = create_window(window_properties, preceding=main_window)

    # Defining Images Icon For The Register Product (30px)
    product_icon = CTkImage(dark_image=Image.open('../images/product_icon.png'), size=(30, 30))
    description_icon = CTkImage(dark_image=Image.open('../images/description_icon.png'), size=(30, 30))
    price_icon = CTkImage(dark_image=Image.open('../images/price_icon.png'), size=(30, 30))

    # Crating Window Labels
    title_label = CTkLabel(editor_window, text='Product Editor', font=TITTLE_FONT, width=window_properties['width'])
    title_label.grid(row=0, column=0, columnspan=3, pady=(10, 30), sticky='ew')

    # Positioning Icons On The Window
    product_icon_label = CTkLabel(editor_window, image=product_icon, text='')
    product_icon_label.grid(row=1, column=0, sticky='ew', padx=(0, 55))

    price_icon_label = CTkLabel(editor_window, image=price_icon, text='')
    price_icon_label.grid(row=2, column=0, sticky='ew', padx=(0, 55), pady=20)

    description_icon_label = CTkLabel(editor_window, image=description_icon, text='')
    description_icon_label.grid(row=3, column=0, sticky='ew', padx=(0, 55), pady=(0, 10))

    # A Sla Nego
    # Obtaining Selected Row In Treeview
    selected_row_product = treeview.selection()
    # Obtaining Values From Selected Row
    row_product_values = treeview.item(selected_row_product)['values']

    # Positioning Window Entries
    product_name_edit_entry = CTkEntry(editor_window, font=ENTRIES_FONT, width=200, height=32,
                                       textvariable=StringVar(value=row_product_values[1]))
    product_name_edit_entry.grid(row=1, column=0, columnspan=4, sticky='we', padx=(100, 70))

    product_price_edit_entry = CTkEntry(editor_window, font=ENTRIES_FONT, width=200, height=32,
                                        textvariable=StringVar(value=row_product_values[3]))
    product_price_edit_entry.grid(row=2, column=0, columnspan=4, sticky='we', padx=(100, 70))

    product_description_edit_entry = CTkEntry(editor_window, font=ENTRIES_FONT, width=200, height=32,
                                              textvariable=StringVar(value=row_product_values[2]))
    product_description_edit_entry.grid(row=3, column=0, columnspan=4, sticky='we', padx=(100, 70))

    # Creating Screen Buttons
    delete_button = CTkButton(editor_window, text='Delete', font=BUTTON_FONT, width=125, height=32,
                              fg_color=MEDIUM_GRAY_COLOR,
                              hover_color='green',
                              command=lambda: confirmation_window(editor_window,
                                                                  row_product_values[0], treeview))
    delete_button.place(x=50, y=246)
    # Update Button
    update_button = CTkButton(editor_window, text='Update', font=BUTTON_FONT, width=125, height=32,
                              fg_color=MEDIUM_GRAY_COLOR,
                              hover_color='green',
                              command=lambda: handling_input(editor_window,
                                                             product={'id': row_product_values[0],
                                                                      'name': product_name_edit_entry.get().title(),
                                                                      'description': product_description_edit_entry.get(),
                                                                      'price': product_price_edit_entry.get()},
                                                             treeview=treeview))
    update_button.place(x=275, y=246)


# Function that creates confirm delete window
def confirmation_window(window, product_id, treeview):
    # Defining window properties
    window_properties = {'width': 300, 'height': 170, 'id': 'Deleter'}

    # Function That Creates Window
    confirmation_window = create_window(window_properties, preceding=window)

    # Defining Images Icon For The Register Product (72px)
    warning_icon = CTkImage(dark_image=Image.open('../images/warning_icon.png'), size=(72, 72))

    # Positioning Icons On The Window
    warning_icon_label = CTkLabel(confirmation_window, image=warning_icon, text='')
    warning_icon_label.grid(row=1, column=0, columnspan=3, sticky='ew', padx=114, pady=(10, 5))

    # Creating Screen Labels
    confirm_delete_label = CTkLabel(confirmation_window, text='Confirm Delete', font=MESSAGE_FONT)
    confirm_delete_label.grid(row=2, column=0, columnspan=3, stick='we', pady=(0, 10))

    # Creating Screen Buttons
    # Cancel Button
    cancel_button = CTkButton(confirmation_window, text='Cancel', font=BUTTON_FONT, width=125, height=32,
                              fg_color=MEDIUM_GRAY_COLOR,
                              hover_color='green', command=lambda: confirmation_window.destroy())
    cancel_button.grid(row=5, column=0, columnspan=1, padx=(20, 0), sticky='w')
    # Confirm Button
    confirm_button = CTkButton(confirmation_window, text='Confirm', font=BUTTON_FONT, width=125, height=32,
                               fg_color=MEDIUM_GRAY_COLOR,
                               hover_color='green',
                               command=lambda: delete_product(window, confirmation_window, product_id,
                                                              treeview))
    confirm_button.grid(row=5, column=2, columnspan=4, padx=(0, 20), sticky='e')

    # Overlaying Window
    confirmation_window.grab_set()


# Function that creates product register window
def register_window(main_window, treeview):
    # Defining window properties
    window_properties = {'width': 450, 'height': 301, 'id': 'Register'}

    # Function That Creates Window
    register_window = create_window(window_properties, preceding=main_window)

    # Defining Images Icon For The Register Product (30px)
    product_icon = CTkImage(dark_image=Image.open('../images/product_icon.png'), size=(30, 30))
    description_icon = CTkImage(dark_image=Image.open('../images/description_icon.png'), size=(30, 30))
    price_icon = CTkImage(dark_image=Image.open('../images/price_icon.png'), size=(30, 30))

    # Crating Window Labels
    title_label = CTkLabel(register_window, text='Product Registrar', font=TITTLE_FONT,
                           width=window_properties['width'])
    title_label.grid(row=0, column=0, columnspan=3, pady=(10, 30), sticky='ew')

    # Positioning Icons On The Window
    product_icon_label = CTkLabel(register_window, image=product_icon, text='')
    product_icon_label.grid(row=1, column=0, sticky='ew', padx=(0, 55))

    price_icon_label = CTkLabel(register_window, image=price_icon, text='')
    price_icon_label.grid(row=2, column=0, sticky='ew', padx=(0, 55), pady=20)

    description_icon_label = CTkLabel(register_window, image=description_icon, text='')
    description_icon_label.grid(row=3, column=0, sticky='ew', padx=(0, 55), pady=(0, 10))

    # Positioning Window Entries
    product_name_entry = CTkEntry(register_window, font=ENTRIES_FONT, width=200, height=32,
                                  placeholder_text='Product Name')
    product_name_entry.grid(row=1, column=0, columnspan=4, sticky='we', padx=(100, 70))

    product_price_entry = CTkEntry(register_window, font=ENTRIES_FONT, width=200, height=32,
                                   placeholder_text='Product Price')
    product_price_entry.grid(row=2, column=0, columnspan=4, sticky='we', padx=(100, 70))

    product_description_entry = CTkEntry(register_window, font=ENTRIES_FONT, width=200, height=32,
                                         placeholder_text='Product Description')
    product_description_entry.grid(row=3, column=0, columnspan=4, sticky='we', padx=(100, 70))

    # Creating Screen Buttons
    exit_button = CTkButton(register_window, text='Exit', font=BUTTON_FONT, width=125, height=32,
                            fg_color=MEDIUM_GRAY_COLOR,
                            hover_color='green',
                            command=register_window.destroy)
    exit_button.place(x=50, y=246)
    # Update Button
    insert_button = CTkButton(register_window, text='Insert', font=BUTTON_FONT, width=125, height=32,
                              fg_color=MEDIUM_GRAY_COLOR,
                              hover_color='green',
                              command=lambda: handling_input(register_window,
                                                             product={'id': None,
                                                                      'name': product_name_entry.get().title(),
                                                                      'description': product_description_entry.get(),
                                                                      'price': product_price_entry.get()},
                                                             treeview=treeview))
    insert_button.place(x=275, y=246)

    # Overlaying Window
    register_window.grab_set()

    # Function that verifies if any product has been selected on the main window to be excluded


def confirmation(main_window, selected_product, treeview):
    # Confirming if any row was selected in the main
    if selected_product == '':
        message_properties = {'text': 'Please Select Any Product', 'row': 4, 'column': 5, 'columnspan': 9,
                              'pady': 15, 'text_color': '#A94228'}
        # Positioning Warning On The Window
        generate_message(main_window, message_properties, temporary=True)
    else:
        confirmation_window(main_window, selected_product[0], treeview)


def verify_credentials(window, properties):
    """
    Checks credentials authenticity on database.

    Args:
        window: Login window.
        properties (dict): Specifications of the login.
            - username (str): Username entered that will be checked.
            - password (str): Password entered that will be checked.
    Returns:
        True
    """

    # Checking credentials on database
    approval = UserDAO().select_user_by_key(properties['username'], properties['password'])

    if approval:
        # Destroying Login Window
        window.destroy()
        # Create Menu Window
        main_window()
    else:
        # Defining message properties and positioning it
        message_properties = {'text': 'Username Or Password Is Incorrect',
                              'row': 3, 'column': 0, 'columnspan': 3, 'pady': 0, 'text_color': RED_COLOR}
        generate_message(window, message_properties)