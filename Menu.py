"""This Program is a basic menu gui for a takeaway shop."""
import tkinter as tk  # This is the GUI framework
from tkinter import messagebox, PhotoImage  # This required to make the error message
from functools import partial  # This gives us access to higher level function
from random import randint  # This is used to generate the ID's for customers
import json  # This allows python to handle json files
import os  # This gives us access to os tools


class BaseWindow(tk.Tk):
    """The BaseWindow class makes all the pages needed for my program and is
    also the main Tk window."""

    def __init__(self, *args, **kwargs):
        """Handles the creation of pages and tk window"""
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(1000, 700)
        self.title("Voorhoeve's Takeaway")

        """This is changing the settings of the window to allow resizing"""
        self.base = tk.Frame(self)
        self.base.pack(side="top", fill="both", expand=True)
        self.base.grid_rowconfigure(0, weight=1)
        self.base.grid_columnconfigure(0, weight=1)

        self.pages = {}  # Page Initializer
        for P in (Food, Drink, Dessert, Cart, Quantity):
            self.page = P(self.base, self)
            self.pages[P] = self.page
            self.page.grid(row=0, column=0, sticky="nsew")

        self.show_page(Food)

    def show_page(self, page_num):
        '''This is used to switch between pages'''
        self.page = self.pages[page_num]
        self.page.tkraise()


class BasePage:
    """BasePage is used to create a default page for Food, Drink, Dessert and
    Cart """

    def __init__(self, parent, basewindow, page):
        FONT = ("Arab", "20")

        """Page Styling"""
        parent.header = tk.Frame(parent, bg="#E94F37", )
        parent.Label = tk.Label(parent.header,
                                text="Voorhoeve's Takeaway",
                                font=FONT,
                                bg="#E94F37",
                                height=2).pack(anchor='center')

        parent.nav = tk.Frame(parent, bg="#44BBA4")
        parent.menubox = tk.Frame(parent, bg="#F0EFF4")
        parent.footer = tk.Frame(parent, bg="#3F88C5", height=35)

        parent.header.grid(column=0, row=0, columnspan=2, sticky="nsew")
        parent.nav.grid(column=0, row=1, sticky="nsew")
        parent.menubox.grid(column=1, row=1, sticky="nsew")
        parent.footer.grid(column=0, row=3, columnspan=2, sticky="nsew")
        parent.columnconfigure(1, weight=1)  # Allow Resizing
        parent.rowconfigure(1, weight=1)  # Allow Resizing

        """Nav button creation"""
        parent.food = tk.Button(parent.nav,
                                text="Food",
                                font=FONT,
                                bg="#F0EFF4",
                                highlightthickness=0,
                                pady=20,
                                command=lambda: basewindow.show_page(Food))

        parent.drink = tk.Button(parent.nav,
                                 text="Drink",
                                 font=FONT,
                                 bg="#F0EFF4",
                                 highlightthickness=0,
                                 pady=20,
                                 command=lambda: basewindow.show_page(Drink))

        parent.dessert = tk.Button(parent.nav,
                                   text="Dessert",
                                   font=FONT,
                                   bg="#F0EFF4",
                                   highlightthickness=0,
                                   pady=20,
                                   command=lambda: basewindow.show_page(Dessert))

        parent.cart = tk.Button(parent.nav,
                                text="Cart",
                                font=FONT,
                                bg="#F0EFF4",
                                highlightthickness=0,
                                pady=20,
                                command=lambda: basewindow.show_page(Cart))

        # Puts all the buttons on the screen
        parent.food.grid(row=0, column=0, sticky="nsew")
        parent.drink.grid(row=1, column=0, sticky="nsew")
        parent.dessert.grid(row=2, column=0, sticky="nsew")
        parent.cart.grid(row=3, column=0, sticky="nsew")

        parent.box = []  # This list holds all the item buttons
        i = 0
        if page in item_data.keys():  # Finding the right data for this page
            for item in item_data[page].keys():  # Looping through to get item
                parent.menubox.columnconfigure(0, weight=1)  # Allow Resizing
                parent.menubox.rowconfigure(i, weight=1)  # Allow Resizing
                parent.box.append(tk.Button(parent.menubox,  # Button creation
                                            font=FONT,
                                            bg="#F0EFF4",
                                            highlightthickness=0,
                                            text=f'{item} - Price: ${item_data[page][item]["Price"]}',
                                            command=lambda new_item=item: basewindow.pages[Quantity].food_quantity(basewindow,
                                                                                                                   new_item,
                                                                                                                   1)))
                parent.box[i].grid(row=i, column=0, sticky="nsew")
                i += 1


class Food(tk.Frame):
    """Food page"""

    def __init__(self, parent, basewindow):
        tk.Frame.__init__(self, parent)  # Makes Tk Frame
        BasePage(self, basewindow, "Food")  # Creates instance of basepage


class Drink(tk.Frame):
    """Drink page"""

    def __init__(self, parent, basewindow):
        tk.Frame.__init__(self, parent)  # Makes Tk Frame
        BasePage(self, basewindow, "Drink")  # Creates instance of basepage


class Dessert(tk.Frame):
    """ Dessert page"""

    def __init__(self, parent, basewindow):
        tk.Frame.__init__(self, parent)  # Makes Tk Frame
        BasePage(self, basewindow, "Dessert")  # Creates instance of basepage


class Quantity(tk.Frame):
    """Quantity page handles the input of data from the user"""

    def __init__(self, parent, basewindow):
        tk.Frame.__init__(self, parent)
        # BasePage(self, basewindow, "Quantity")

    def food_quantity(self, basewindow, item, quantity):
        """This is called when an item is pressed and it creates the pop up
        that take the user's input"""

        """This is basic pop up styling and management"""
        FONT = ("Arab", "18")
        self.cr_box = tk.Toplevel()
        self.cr_box.geometry("630x380")
        self.cr_box.resizable(0, 0)
        self.cr_box.title("Quantity")
        self.cr_box.grab_set()
        self.cr_box.protocol('WM_DELETE_WINDOW', partial(self.close_quantity))

        self.cr_box.columnconfigure(0, weight=1)  # Allow Resizing
        for i in range(5):
            self.cr_box.rowconfigure(i, weight=1)  # Allow Resizing

        self.tknum = tk.StringVar()  # This is a tkinter var for the GUI
        self.quantity = quantity  # Var allows me to use arrows for quantity selection
        self.tknum.set(self.quantity)  # sets tknum = quantity

        self.food_label = tk.Label(self.cr_box,
                                   text=item,
                                   font=FONT,
                                   bg="#F0EFF4",
                                   highlightthickness=0)

        for page in item_data.keys():  # Finding the right data for this label
            if item in item_data[page].keys():  # Looping through to get item
                self.food_description = tk.Label(self.cr_box,  # Label for description creation
                                                 text=f'Description \n{item_data[page][item]["Description"]}',
                                                 font=FONT,
                                                 wraplength=400,
                                                 bg="#F0EFF4",
                                                 highlightthickness=0)

        def int_button_control(self, state):
            """This allows the arrows to change the quantity"""
            if state == '+':
                if self.entry_num(self.tknum):  # Validates the input
                    if int(self.tknum.get()) < 30:  # Validates the input
                        self.tknum.set(int(self.tknum.get()) + 1)
            if state == '-':
                if self.entry_num(self.tknum):  # Validates the input
                    if int(self.tknum.get()) > 1:  # Validates the input
                        self.tknum.set(int(self.tknum.get()) - 1)

        """Button creation of arrows and entry box"""
        self.up = tk.Button(self.cr_box,
                            text="↑",
                            font=FONT,
                            bg="#F0EFF4",
                            highlightthickness=0,
                            command=lambda: int_button_control(self, '+'))

        self.down = tk.Button(self.cr_box,
                              text="↓",
                              font=FONT,
                              bg="#F0EFF4",
                              highlightthickness=0,
                              command=lambda: int_button_control(self, '-'))

        self.entry = tk.Entry(self.cr_box,
                              textvariable=self.tknum,
                              font=FONT,
                              bg="#F0EFF4",
                              highlightthickness=0)

        """This weird lambda is required as the Value error would
        occur in the button thus tkinter callback and I cant put a try there"""

        self.enter = tk.Button(self.cr_box,
                               text="Enter",
                               font=FONT,
                               bg="#F0EFF4",
                               height=2,
                               highlightthickness=0,
                               command=lambda: ((self.close_quantity(),
                                                basewindow.pages[Cart].add_cart(basewindow,
                                                                                item,
                                                                                int(self.tknum.get())))
                                                if self.entry_num(self.tknum) else print('')))
        self.del_item = tk.Button(self.cr_box,  # This remove the item from cart
                                  text="DELETE",
                                  font=FONT,
                                  bg="#F0EFF4",
                                  highlightthickness=0,
                                  command=lambda: ((self.close_quantity(),
                                                    basewindow.pages[Cart].del_cart(basewindow,
                                                                                    item,))))
        # Puts all the buttons on the screen
        self.food_label.grid(row=0, column=0, sticky="nsew")
        self.up.grid(row=1, column=0, sticky="nsew")
        self.entry.grid(row=2, column=0, sticky="nsew")
        self.down.grid(row=3, column=0, sticky="nsew")
        self.enter.grid(row=4, column=0, sticky="nsew")
        self.del_item.grid(row=5, column=0, sticky="nsew")
        self.food_description.grid(row=0, column=1, rowspan=5, sticky="nsew")

    def entry_num(self, num):
        """Validates the input is a positive number"""
        try:
            num = int(num.get())  # Turns string to int if error then not int
            if num >= 1 and num <= 30:  # Must be a positive number
                return True
            else:
                self.tknum.set(1)  # if num - number it sets it to 1
                self.quantity = 1  # if num - number it sets it to 1
                messagebox.showerror("Error",  # Error message
                                     "Please Enter a Positive Number! 1~30")
                return False
        except ValueError:
            self.tknum.set(1)  # if num - number it sets it to 1
            self.quantity = 1  # if num - number it sets it to 1
            messagebox.showerror("Error",  # Error message
                                 "Please Enter a Positive Number! 1~30")
            return False

    def close_quantity(self):
        self.cr_box.grab_release()  # Sets focus back to main window
        self.cr_box.destroy()  # closes pop up


class Cart(tk.Frame):
    """Creates a cart page with empty cart"""

    def __init__(self, parent, basewindow):
        tk.Frame.__init__(self, parent)
        BasePage(self, basewindow, "Cart")
        FONT = ("Arab", "18")
        self.cart = {}  # Empty cart
        self.price = 0  # Initialize price var

        self.total = tk.Label(self.footer,  # Making a total on the cart page
                              font=FONT,
                              bg="#3F88C5",
                              text=f"Total Price - ${self.price}")

        self.checkout = tk.Button(self.footer,  # checkout button creation
                                  font=FONT,
                                  bg="#F0EFF4",
                                  highlightthickness=0,
                                  text="Checkout",
                                  command=lambda: CheckoutReset(self) if len(self.cart) != 0 else print(''))

        # Puts all the buttons on the screen
        self.checkout.grid(row=0, column=0, sticky="nsew")
        self.total.grid(row=0, column=1, sticky="nsew")
        self.local_menubox = 0

    def add_cart(self, basewindow, item, num):
        """This is the function to add items to the cart"""

        FONT = ("Arab", "18")

        basewindow.show_page(Cart)  # brings up quantity

        if item not in self.cart.keys():
            """Check if this is a new item if it is then it creates a new
            button and added the item to the cart"""
            self.menubox.columnconfigure(0, weight=1)
            self.cart.update({item: [tk.Button(self.menubox,
                                               bg="#F0EFF4",
                                               font=FONT,
                                               highlightthickness=0,
                                               text=f"{item} Quantity : {num}",
                                               command=lambda new_item=item: basewindow.pages[Quantity].food_quantity(basewindow,
                                                                                                                      new_item,
                                                                                                                      num)),
                                     num]})
            self.cart[item][0].grid(row=self.local_menubox, column=0, sticky="nsew")
            self.local_menubox += 1

        else:
            """Changes the Quantity of a already created item."""
            self.cart[item][1] = num
            self.cart[item][0].config(text=f"{item} Quantity : {num}")

        # This updates the total on the cart page
        self.price = 0
        for item in self.cart:
            for page in item_data.keys():
                if item in item_data[page].keys():
                    self.price += item_data[page][item]["Price"]*self.cart[item][1]
                    self.total.config(text=f"Total Price - ${self.price}")

    def del_cart(self, basewindow, item):
        """If the item is in the cart it deletes the item"""
        if item in self.cart.keys():
            self.cart[item][0].destroy()
            self.cart.pop(item)
        else:
            pass


class CheckoutReset:
    """Creates the checkout pop up"""

    def __init__(self, partner):
        """This is basic pop up styling and management"""
        self.cr_box = tk.Toplevel()
        self.cr_box.minsize(230, 200)
        self.cr_box.title("Checkout")
        self.cr_box.grab_set()  # Sets this to focus
        self.cr_box.protocol('WM_DELETE_WINDOW',  # Function to run when closed
                             partial(self.close_checkout, partner, False))

        """This uses the os module to check if that file exists and if it does
        it creates a file with the same name but a new iteration"""
        self.order_id = 1
        while os.path.exists(f"order{self.order_id}.txt"):
            self.order_id += 1

        self.price = 0  # Variable for price

        self.cr_box.ID = tk.Label(self.cr_box,
                                  text=f"ID - {self.order_id}",
                                  font=("Arab", "18"),
                                  height=2).pack(anchor='center')

        # This updates the total and creates the receipt
        for item in partner.cart:
            for page in item_data.keys():
                if item in item_data[page].keys():
                    self.price += item_data[page][item]["Price"]*partner.cart[item][1]
                    tk.Label(self.cr_box,
                             font=("Arab", "14"),
                             text=f'{partner.cart[item][1]} X {item} ---- ${item_data[page][item]["Price"]}',
                             highlightthickness=0).pack()

        # This creates the total label
        tk.Label(self.cr_box,
                 text=f"Total Price - ${self.price}",
                 font=("Arab", "18"),
                 height=2).pack(anchor='center')

        # This creates the confirmation button
        self.cr_box.confirm = tk.Button(self.cr_box,
                                        text="Confirm",
                                        font=("Arab", "18"),
                                        command=lambda: self.close_checkout(partner, True),
                                        height=2).pack(anchor='center')

    def close_checkout(self, partner, confirmed):
        """This checks if the person has confirmed their order and closed or
        has just close but wants to change their order and if confirmed save
        order to file and get ready for next customer"""

        if confirmed:
            self.order = open(f"order{self.order_id}.txt", "w")  # create order file
            self.order.write(f"Order ID - {self.order_id}\n")
            partner.price = 0
            partner.total.config(text=f"Total Price - ${partner.price}")
            for i in partner.cart:
                self.order.write(f"{i} -- {partner.cart[i][1]}\n")
                partner.cart[i][0].destroy()  # wipe this order for next user
            partner.cart = {}
        self.cr_box.grab_release()  # Gives back focus to main program
        self.cr_box.destroy()


if __name__ == "__main__":
    file = open("Items.json", "r")  # This reads the json file data
    item_data = json.load(file)
    file.close()
    root = BaseWindow()
    root.mainloop()  # This starts the gui of the program
