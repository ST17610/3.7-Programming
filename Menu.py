import tkinter as tk
import json


class BaseWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("640x480")
        self.title("Voorhoeve's Takeaway")
        base = tk.Frame(self)
        
        base.pack(side="top", fill="both", expand=True)
        base.grid_rowconfigure(0, weight=1)
        base.grid_columnconfigure(0, weight=1)
        
        self.pages = {}
        for P in (Food, Drink, Dessert, Cart):
            page = P(base, self)
            

            self.pages[P] = page
            
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(Food)
        
    def show_page(self, page_num):
        page = self.pages[page_num]
        page.tkraise()

class BasePage():
    file = open("Items.json","r")
    item_data = json.load(file)
    
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
        
        parent.button1 = tk.Button(parent.nav, text="Food",
                            command=lambda: BaseWindow.show_page(Food))

        parent.button2 = tk.Button(parent.nav, text="Drink",
                            command=lambda: BaseWindow.show_page(Drink))

        parent.button3 = tk.Button(parent.nav, text="Dessert",
                            command=lambda: BaseWindow.show_page(Dessert))

        parent.button4 = tk.Button(parent.nav, text="Cart",
                            command=lambda: BaseWindow.show_page(Cart))
        
        parent.button1.grid(row=0, column=0, sticky="nsew")
        parent.button2.grid(row=1, column=0, sticky="nsew")
        parent.button3.grid(row=2, column=0, sticky="nsew")
        parent.button4.grid(row=3, column=0, sticky="nsew")
        
        parent.box=[]
        parent.item_box=[]
        i = 0
        if name in BasePage.item_data.keys():
            for food in BasePage.item_data[name].keys():
                parent.menubox.columnconfigure(0, weight=1)
                parent.menubox.rowconfigure(i, weight=1)
                parent.box.append(tk.Button(parent.menubox,
                                          bg="#F0EFF4",
                                          highlightthickness=0,
                                          text=food))
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
        


class Cart(tk.Frame):
    def __init__(self, parent, BaseWindow):
        tk.Frame.__init__(self,parent)
        BasePage(self, BaseWindow, "Cart")
       
            
        
class Items():
    def __init__(self):
        pass
        

        
if __name__ == "__main__":
    root = BaseWindow()
    root.mainloop()
