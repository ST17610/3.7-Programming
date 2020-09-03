import tkinter as tk
from tkinter import ttk


class BaseWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self)
        main_frame.grid(row = 0,column= 0)
        base = tk.Frame(self)
        #base.pack(side="top", fill="both", expand=True)
        base.grid(row = 0,column= 1,sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.pages = {}
        
        for P in (Food, Drink, Dessert, Cart):

            page = P(base, self)

            self.pages[P] = page
            page.config(background='#F0EFF4')

            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(Food)
        
        button1 = ttk.Button(self, text="Food",
                            command=lambda: self.show_page(Food))

        button2 = ttk.Button(self, text="Drink",
                            command=lambda: self.show_page(Drink))

        button3 = ttk.Button(self, text="Dessert",
                            command=lambda: self.show_page(Dessert))

        button4 = ttk.Button(self, text="Cart",
                            command=lambda: self.show_page(Cart))

        button1.grid(in_=main_frame,row=0, column=0, sticky="nsew")
        button2.grid(in_=main_frame,row=1, column=0, sticky="nsew")
        button3.grid(in_=main_frame,row=2, column=0, sticky="nsew")
        button4.grid(in_=main_frame,row=3, column=0, sticky="nsew")
    """"
        main_frame.button1.pack()
        main_frame.button2.pack()
        main_frame.button3.pack()
        
        """
        
      
    def show_page(self, page_num):
        page = self.pages[page_num]
        page.tkraise()

class Food(tk.Frame):
    def __init__(self, parent, BaseWindow):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Food")
        label.pack(pady=10,padx=10)

        
class Drink(tk.Frame):
    def __init__(self, parent, BaseWindow):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Drink")
        label.pack(pady=10,padx=10)


class Dessert(tk.Frame):
    def __init__(self, parent, BaseWindow):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Dessert")
        label.pack(pady=10,padx=10)


class Cart(tk.Frame):
    def __init__(self, parent, BaseWindow):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Cart")
        label.pack(pady=10,padx=10)

        
if __name__ == "__main__":
    root = BaseWindow()
    root.mainloop()
