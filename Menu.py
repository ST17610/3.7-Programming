#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from functools import partial
from random import randint
import json


class BaseWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1000x700")
        self.title("Voorhoeve's Takeaway")
        
        self.base = tk.Frame(self)
        self.base.pack(side="top", fill="both", expand=True)
        self.base.grid_rowconfigure(0, weight=1)
        self.base.grid_columnconfigure(0, weight=1)
        
        self.pages = {}
        for P in (Food, Drink, Dessert, Cart, Quantity):
            
            self.page = P(self.base, self)
            self.pages[P] = self.page
            self.page.grid(row=0, column=0, sticky="nsew")

        self.show_page(Food)
        
    def show_page(self, page_num):
        self.page = self.pages[page_num]
        self.page.tkraise()
    


class BasePage():
    def __init__(self, parent, BaseWindow, name):
        FONT = ("Arab", "20")
       
        parent.header = tk.Frame(parent, bg="#E94F37",)
        parent.Label = tk.Label(parent.header, 
                                text="Reinhard's Diner",
                                font=FONT,
                                bg="#E94F37",
                                height = 2).pack(anchor='center')
        
        parent.nav = tk.Frame(parent, bg="#44BBA4")
        parent.menubox = tk.Frame(parent, bg="#F0EFF4")
        parent.footer = tk.Frame(parent, bg="#3F88C5", height = 35)

        parent.header.grid(column=0, row=0, columnspan=2, sticky="nsew")
        parent.nav.grid(column=0, row=1, sticky="nsew")
        parent.menubox.grid(column=1, row=1, sticky="nsew")
        parent.footer.grid(column=0, row=3, columnspan=2, sticky="nsew")

        parent.columnconfigure(1, weight=1)
        parent.rowconfigure(1, weight=1)
        
        
        parent.food = tk.Button(parent.nav, 
                                text="Food",
                                font = FONT,
                                bg="#F0EFF4",
                                highlightthickness=0,
                                pady=20,
                                command=lambda: BaseWindow.show_page(Food))

        parent.drink = tk.Button(parent.nav, 
                                 text="Drink",
                                 font = FONT,
                                 bg="#F0EFF4",
                                 highlightthickness=0,
                                 pady=20,
                                 command=lambda: BaseWindow.show_page(Drink))

        parent.dessert = tk.Button(parent.nav, 
                                   text="Dessert",
                                   font = FONT,
                                   bg="#F0EFF4",
                                   highlightthickness=0,
                                   pady=20,
                                   command=lambda: BaseWindow.show_page(Dessert))

        parent.cart = tk.Button(parent.nav, 
                                text="Cart",
                                font = FONT,
                                bg="#F0EFF4",
                                highlightthickness=0,
                                pady=20,
                                command=lambda: BaseWindow.show_page(Cart))
        
        parent.food.grid(row=0, column=0, sticky="nsew")
        parent.drink.grid(row=1, column=0, sticky="nsew")
        parent.dessert.grid(row=2, column=0, sticky="nsew")
        parent.cart.grid(row=3, column=0, sticky="nsew")
        
        parent.box=[]
        i = 0
        if name in item_data.keys():
            for obj in item_data[name].keys():
                parent.menubox.columnconfigure(0, weight=1)
                parent.menubox.rowconfigure(i, weight=1)
                parent.box.append(tk.Button(parent.menubox,
                                            font=FONT,
                                            bg="#F0EFF4",
                                            highlightthickness=0,
                                            text=f'{obj} - Price: ${item_data[name][obj]["Price"]}',
                                            command=lambda obj=obj:Quantity.food_page(BaseWindow.pages[Quantity], BaseWindow, obj)))
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
    def __init__(self, parent, BaseWindow):
        tk.Frame.__init__(self,parent)
        BasePage(self, BaseWindow, "Quantity")
       
    def food_page(self, BaseWindow, food):
        FONT = ("Arab", "18")
        BaseWindow.show_page(Quantity)
        
        self.menubox.columnconfigure(0, weight=1)
        for i in range(4):
            self.menubox.rowconfigure(i, weight=1)

        self.num = 0
        self.food_label = tk.Label(self.menubox, 
                                   text=food,
                                   font=FONT,
                                   bg="#F0EFF4",
                                   highlightthickness=0,)
        
        self.num_label = tk.Label(self.menubox, 
                                  font=FONT,
                                  text=self.num,
                                  bg="#F0EFF4",
                                  highlightthickness=0,)
        
        def int_button_control(self, state):
            if state == '+':
                self.num += 1 
            if state == '-':
                self.num -= 1 
            self.num_label.configure(text=self.num)
                
    
        self.up = tk.Button(self.menubox, 
                            text="↑",
                            font=FONT,
                            bg="#F0EFF4",
                            highlightthickness=0,
                            command=lambda:int_button_control(self,'+'))
        
        self.down = tk.Button(self.menubox,
                              text="↓",
                              font=FONT,
                              bg="#F0EFF4",
                              highlightthickness=0,
                              command=lambda:int_button_control(self, '-'))
        
        self.enter = tk.Button(self.menubox, 
                               text="Enter",
                               font=FONT,
                               bg="#F0EFF4",
                               height=2,
                               highlightthickness=0,
                               command=lambda:Cart.add_cart(BaseWindow.pages[Cart], BaseWindow, food, self.num))
        
        self.food_label.grid(row=0, column=0, sticky="nsew")
        self.up.grid(row=1, column=0, sticky="nsew")
        self.num_label.grid(row=2, column=0, sticky="nsew")
        self.down.grid(row=3, column=0, sticky="nsew")
        self.enter.grid(row=4, column=0, sticky="nsew")
        

class Cart(tk.Frame):
    def __init__(self, parent, BaseWindow):
        tk.Frame.__init__(self,parent)
        BasePage(self, BaseWindow, "Cart")
        FONT = ("Arab", "18")
        self.cart = {}
        self.checkout = tk.Button(self.footer,
                                  font=FONT,
                                  bg="#F0EFF4",
                                  highlightthickness=0,
                                  text="Checkout",
                                  command=lambda: Checkout_Reset(self))
        self.checkout.grid(row=0, column=0, sticky="nsew")
        
        self.local_menubox = 0
        
    def add_cart(self, BaseWindow, food, num):
        FONT = ("Arab", "18")
        
        BaseWindow.show_page(Cart)
        
        
        if food not in self.cart.keys():
            self.menubox.columnconfigure(0, weight=1)
            #self.menubox.rowconfigure(self.local_menubox, weight=1)
            self.cart.update({food : [tk.Button(self.menubox,
                                      bg="#F0EFF4",
                                      font=FONT,
                                      highlightthickness=0,
                                      text=f"{food} Quantity : {num}"), num]})
            self.cart[food][0].grid(row=self.local_menubox, column=0, sticky="nsew")
            self.local_menubox+=1
        else:
            num+=self.cart[food][1]
            self.cart[food][1] = num
            self.cart[food][0].config(text=f"{food} Quantity : {num}")
            
        print(self.cart)
        
class Checkout_Reset():
    def __init__(self, partner):
        self.cr_box = tk.Toplevel()
        self.cr_box.geometry("300x200")
        self.cr_box.title("Checkout")
        self.cr_box.grab_set()
        self.cr_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
        
        self.id = randint(0,300)
        self.price = 0
        
        self.cr_box.Label = tk.Label(self.cr_box, 
                                text=f"ID - {self.id}",
                                font=("Arab", "18"),
                                height = 2).pack(anchor='center')
        for obj in partner.cart:
            for name in item_data.keys():
                if obj in item_data[name].keys():
                    for i in range (partner.cart[obj][1]):
                        self.price+=item_data[name][obj]["Price"]
                    partner.cart[obj][0].destroy()
                        
        tk.Label(self.cr_box, 
                 text=f"Total Price - ${self.price}",
                 font=("Arab", "18"),
                    height = 2).pack(anchor='center')

    def close_help(self, partner):
        partner.cart = {}
        self.cr_box.grab_release()  
        self.cr_box.destroy() 
                   
class Items():
    
    def __init__(self, item):
        for name in item_data.keys():
            if item in item_data[name].keys():
                self.info = item_data[name][item]
                #self.print_info()
                
    def print_info(self):
        print(self.info)
        

        
file = open("Items.json","r")
item_data = json.load(file)
file.close()
root = BaseWindow()
root.mainloop()
