import tkinter as tk
import json


class BaseWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("640x480")
        self.title("Voorhoeve's Takeaway")
        self.base = tk.Frame(self)
        
        self.base.pack(side="top", fill="both", expand=True)
        self.base.grid_rowconfigure(0, weight=1)
        self.base.grid_columnconfigure(0, weight=1)
        
        self.pages = {}
        for P in (Food, Drink, Dessert, Cart):
            self.page = P(self.base, self)
            

            self.pages[P] = self.page
            
            self.page.grid(row=0, column=0, sticky="nsew")

        self.show_page(Food)
        #print(self.pages)
        
    def show_page(self, page_num):
        self.page = self.pages[page_num]
        self.page.tkraise()
    
    def create_quantity(self,food):
        self.page = Quantity(self.base, self, food)
        self.pages[Quantity] = self.page
        self.page.grid(row=0, column=0, sticky="nsew")
        self.page.tkraise()
        

        

class BasePage():
    file = open("Items.json","r")
    item_data = json.load(file)
    file.close()
    
    def __init__(self, parent, BaseWindow, name):
       
        parent.header = tk.Frame(parent, bg="#E94F37", height = 50)
        parent.nav = tk.Frame(parent, bg="#44BBA4")
        parent.menubox = tk.Frame(parent, bg="#F0EFF4")
        parent.footer = tk.Frame(parent, bg="#3F88C5", height = 35)

        parent.header.grid(column=0, row=0, columnspan=2, sticky="nsew")
        parent.nav.grid(column=0, row=1, sticky="nsew")
        parent.menubox.grid(column=1, row=1, sticky="nsew")
        parent.footer.grid(column=0, row=3, columnspan=2, sticky="nsew")

        parent.columnconfigure(1, weight=1)
        parent.rowconfigure(1, weight=1)
        
        parent.label = tk.Label(parent.menubox, text=name)
        #parent.label.grid(column=1, row=0, pady=10, padx=10)
        
        parent.button1 = tk.Button(parent.nav, text="Food",bg="#F0EFF4",
                                   highlightthickness=0,
                                   pady=20,
                                   command=lambda: BaseWindow.show_page(Food))

        parent.button2 = tk.Button(parent.nav, text="Drink",bg="#F0EFF4",
                                   highlightthickness=0,
                                   pady=20,
                                   command=lambda: BaseWindow.show_page(Drink))

        parent.button3 = tk.Button(parent.nav, text="Dessert",bg="#F0EFF4",
                                   highlightthickness=0,
                                   pady=20,
                                   command=lambda: BaseWindow.show_page(Dessert))

        parent.button4 = tk.Button(parent.nav, text="Cart",bg="#F0EFF4",
                                   highlightthickness=0,
                                   pady=20,
                                   command=lambda: BaseWindow.show_page(Cart))
        
        parent.button1.grid(row=0, column=0, sticky="nsew")
        parent.button2.grid(row=1, column=0, sticky="nsew")
        parent.button3.grid(row=2, column=0, sticky="nsew")
        parent.button4.grid(row=3, column=0, sticky="nsew")
        
        parent.box=[]
        i = 0
        if name in BasePage.item_data.keys():
            for food in BasePage.item_data[name].keys():
                parent.menubox.columnconfigure(0, weight=1)
                parent.menubox.rowconfigure(i, weight=1)
                parent.box.append(tk.Button(parent.menubox,
                                            bg="#F0EFF4",
                                            highlightthickness=0,
                                            text=food,
                                            command=lambda food=food :BaseWindow.create_quantity(food)))
                parent.box[i].grid(row=i, column=0, sticky="nsew")
                i+=1
        
        
        
class Food(tk.Frame):
    def __init__(self, parent, BaseWindow):
        tk.Frame.__init__(self,parent)
        BasePage(self, BaseWindow, "Food")
        

        
class Drink(tk.Frame):
    def __init__(self, parent, BaseWindow):
        tk.Frame.__init__(self,parent)
        BasePage(self, BaseWindow, "Drink")
        

class Dessert(tk.Frame):
    def __init__(self, parent, BaseWindow):
        tk.Frame.__init__(self,parent)
        BasePage(self, BaseWindow, "Dessert")
        

class Quantity(tk.Frame):
    def __init__(self, parent, BaseWindow, food):
        tk.Frame.__init__(self,parent)
        BasePage(self, BaseWindow, "Quantity")
        self.menubox.columnconfigure(0, weight=1)
        self.menubox.rowconfigure(0, weight=1)
        self.menubox.rowconfigure(1, weight=1)
        self.menubox.rowconfigure(2, weight=1)
        self.menubox.rowconfigure(3, weight=1)
        self.menubox.rowconfigure(4, weight=1)
        
        self.num = 0
        self.food_label = tk.Label(self.menubox, text=food,
                                   bg="#F0EFF4",
                                   highlightthickness=0,)
        self.num_label = tk.Label(self.menubox, text=self.num,
                                  bg="#F0EFF4",
                                  highlightthickness=0,)
        def int_button_control(self, state):
            if state == '+':
                self.num += 1 
            if state == '-':
                self.num -= 1 
            self.num_label.configure(text=self.num)
                
    
        self.up = tk.Button(self.menubox, text="↑",bg="#F0EFF4",
                            highlightthickness=0,
                            command=lambda:int_button_control(self,'+'))
        self.down = tk.Button(self.menubox, text="↓",bg="#F0EFF4",
                              highlightthickness=0,
                              command=lambda:int_button_control(self, '-'))
        self.enter = tk.Button(self.menubox, text="Enter",bg="#F0EFF4",
                               highlightthickness=0,
                               command=lambda:Cart.add_cart(BaseWindow.pages[Cart], food, self.num))
        
        self.food_label.grid(row=0, column=0, sticky="nsew")
        self.up.grid(row=1, column=0, sticky="nsew")
        self.num_label.grid(row=2, column=0, sticky="nsew")
        self.down.grid(row=3, column=0, sticky="nsew")
        self.enter.grid(row=4, column=0, sticky="nsew")
        

class Cart(tk.Frame):
    def __init__(self, parent, BaseWindow):
        tk.Frame.__init__(self,parent)
        BasePage(self, BaseWindow, "Cart")
        self.checkout = tk.Button(self.footer,
                                  bg="#F0EFF4",
                                  highlightthickness=0,
                                  text="Checkout",
                                  command=lambda:map(self.cart.print_info(), self.cart))
        self.checkout.grid(row=0 ,column=0, sticky="nsew")
        self.cart = []
        self.loc = 0
        
    def add_cart(self, food, num):
        self.Items(food, num)
        self.menubox.columnconfigure(0, weight=1)
        self.menubox.rowconfigure(self.loc, weight=1)
        self.box.append(tk.Button(self.menubox,
                                  bg="#F0EFF4",
                                  highlightthickness=0,
                                  text=f"{food} Quantity : {num}"))
                                    #command=lambda food=food :BaseWindow.create_quantity(food)))
        self.box[self.loc].grid(row=self.loc, column=0, sticky="nsew")
        print(self.cart)
        self.loc+=1
    
    def Items(self, food, num):
        for i in range(num):
            self.cart.append(Items(food))
       
            
        
class Items():
    file = open("Items.json","r")
    item_data = json.load(file)
    file.close()
    def __init__(self, item):
        for name in Items.item_data.keys():
            if item in Items.item_data[name].keys():
                self.info = Items.item_data[name][item]
                
    def print_info(self):
        print(self.info)
        

        
if __name__ == "__main__":
    root = BaseWindow()
    root.mainloop()
