"""

This assignment is building on the shop program which I developed in the video series. You are tasked to add some
additional functionality:
Functionality
 The shop CSV should hold the initial cash value for the shop.
 Read in customer orders from a CSV file.
– That file should include all the products they wish to buy and in what quantity.
– It should also include their name and their budget.
 The shop must be able to process the orders of the customer.
– Update the cash in the shop based on money received.
* It is important that the state of the shop be consistent.
* You should create customer test files (CSVs) which cannot be completed by the shop e.g. customer wants 400
loaves of bread but the shop only has 20, or the customer wants 2 cans of coke but can only afford 1.
* If these files don’t exist marks penalties will be applied.
– Know whether or not the shop can fill an order.
* Thrown an appropriate error.
 Operate in a live mode, where the user can enter a product by name, specify a quantity, and pay for it. The user should
be able to buy many products in this way.
Notes
 The above described functionality should be completed in Python and C. This is to be done in a procedural programming
style.
 The second part of the assessment involves replicating the functionality of the shop in Java. This must be done in an
Object Oriented manner.
 You must complete a short report, around 3-5 pages, which compares the solutions achieved using the procedural
approach and the object oriented approach.
 The live mode, and the input files, should have the exact same behaviour in ALL implementations.
– For example I should be able to use the Java implementation in the same way as the C one i.e. same CSV files,
and the same process when doing an order in live mode.
– The “user experience” of each implementation should be identical.

"""

#below is solution in python in procedural style

from typing import List
import csv
import re
import os
from glob import glob

class Product:

    def __init__(self, name, price=0):
        self.name = name
        self.price = price
    
    def __repr__(self):
        str = f"PRODUCT NAME: {self.name}\n"
        str += f'PRODUCT PRICE {self.price}\n'
        return str

class ProductStock:
    
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def name(self):
        return self.product.name
    
    def unit_price(self):
        return self.product.price

    def get_available_qty(self):
        return self.quantity
    
    def update_qty(self, qty):
        self.quantity = qty
        
    def cost(self):
        return self.unit_price() * self.quantity
        
    def __repr__(self):
        return f"{self.product}The Shop has {int(self.quantity)} of the above \n"

class Customer:

    def __init__(self, path):
        self.shopping_list = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.name = first_row[0]
            self.budget = float(first_row[1])
            for row in csv_reader:
                name = row[0]
                quantity = float(row[1])
                price = s.find_product_price(name)
                p = Product(name, price)
                ps = ProductStock(p, quantity)
                self.shopping_list.append(ps) 
                
    def calculate_costs(self, price_list):
        for shop_item in price_list:
            for list_item in self.shopping_list:
                if (list_item.name() == shop_item.name()):
                    list_item.product.price = shop_item.unit_price()
    
    def order_cost(self):
        cost = 0
        
        for list_item in self.shopping_list:
            cost += list_item.cost()
        
        return cost
    
    def __repr__(self):
        
        str = f"CUSTOMER NAME : {self.name}\n"
        str += f"CUSTOMER BUDGET: {self.budget}\n"
        total = 0.0
        out_of_stock = []
        active_product_list = []

        for item in self.shopping_list:
            check_val = s.find_product_price(item.name())
            if check_val == 0:
                str += '\n'
                str += f'Error no {item.name()} in Shop stock.List item ignored'
            else:
                str += f'\nPRODUCT NAME: {item.name()} \nPRODUCT PRICE: {item.unit_price()}'
                str += f'\n{self.name} ORDERS {item.get_available_qty()} OF ABOVE PRODUCT'
                if int(s.find_product_qty(item.name())) < int(item.get_available_qty()):
                    data = {
                        "product_name" : item.name(),
                        "availble_qty" : int(s.find_product_qty(item.name())),
                        "need_qty": int(item.get_available_qty())
                    }
                    out_of_stock.append(data)

            cost = int(item.get_available_qty()) * float(item.unit_price())
            buying_data = {
                "product" : item.name(),
                "qty" : item.get_available_qty(),
                "sub_tot" : cost
            }
            active_product_list.append(buying_data)
            total = total + cost
            str += f'\nThe cost to {self.name} will be €{round(cost, 2)}'
        
        str += '\n--------------------------------------------------'
        str += f'\nThe total cost to {self.name} will be €{total}'

        if len(out_of_stock) == 0:
            if float(c.budget) >= float(total):
                str += '\n--------------------------------------------------'
                str += '\nSUCCESS !'
                str += f"\n{self.name}'s budget is {self.budget}"
                str += f"\n{self.name} has enough money"
                str += f"\ntotal of {total} will be deducted from {self.name}'s budget"

                # updating the stock
                for stock in s.stock:
                    # print(stock)
                    for product in active_product_list:
                        if stock.name() == product['product']:
                            qty = int(stock.quantity) - int(product['qty'])
                            stock.update_qty(qty)
                            
                self.budget = float(self.budget) - float(total)
                shop_total = float(s.cash) + float(total)
                s.update_cash(shop_total)

                str += f"\n{self.name}'s budget is {self.budget}"
                str += f"\ntotal of {total} added to shop"
                str += f"\nShop has {s.cash}"
            else:
                str += '\n--------------------------------------------------'
                str += '\nFAIL !'
                str += f"\n{self.name}'s budget is {self.budget}"
                str += f'\nThe total cost of all items is ...! {float(total)}'
                str += f"\n{self.name} does not have enough money"
                str += f"\ntotal of 0 will be deducted from {self.name}'s budget"
                str += f"\n{self.name}'s budget is {self.budget}"
                str += f"\ntotal of 0 added to shop"
                str += f"\nShop has {s.cash} in cash"
        else:
            for out_stock in out_of_stock:
                str += f"\nNot enough {out_stock['product_name']} in stock"
                str += f"\n{out_stock['availble_qty']} {out_stock['product_name']} in stock"
                str += f"\n{self.name} want {out_stock['need_qty']} {out_stock['product_name']}"
                str += "\nPlease revise order and upload again!"
        
        return str 
        
class Shop:
    
    def __init__(self, path):
        self.stock = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.cash = float(first_row[0])
            for row in csv_reader:
                p = Product(row[0], float(row[1]))
                ps = ProductStock(p, float(row[2]))
                self.stock.append(ps)

    def find_product(self, product_name):
        for item in self.stock:
            if str(product_name) == str(item.name()):
                return 1
        return 0

    def find_product_qty(self, product_name):
        for item in self.stock:
            if str(product_name) == str(item.name()):
                return item.get_available_qty()
        return 0
    
    def find_product_price(self, product_name):
        for item in self.stock:
            if str(product_name) == str(item.name()):
                return item.unit_price()
        return 0
    
    def update_cash(self, cash):
        self.cash = cash
    
    def __repr__(self):
        str = ""
        str += f'Shop has {self.cash} in cash\n'
        str += f'The Shop has the following stock which will be cheked against your order\n'
        str += f'\n'
        for item in self.stock:
            str += f"{item}\n"
        return str

s = Shop("../stock.csv")
active = True  # This is our on/off switch for the program. True is on and False is off.


while active:  # We make a while loop. So while active(True) - keep repeating everything inside
    print('Welcome to the shop')
    print("---------------------------------------------------")
    print(s)
    print("---------------------------------------------------")
    print("1 ) for live mode") # This is our menu and list options for the user - It's inside a while loop so that the entire program doesn't run once and then exit.
    PATH = "../"
    EXT = "*.csv"
    all_csv_files_ = [file
                    for path, subdir, files in os.walk(PATH)
                    for file in glob(os.path.join(path, EXT))]
    
    all_csv_files = []
    for file_path in all_csv_files_:
        if file_path != "../stock.csv":
            all_csv_files.append(file_path)

    index = 1
    for file_name in all_csv_files:
        index = index + 1
        print(index,')',file_name)

    print('')
    print("0) Exit")
    print('')
    print('Choose your customer file or live move : e.g type  for live mode, 2+ for file 3')
    print('')

    try:  # This is a try statement used to handle errors
        answer = input("Option: ")  # This is a variable which stores the value a user enters
                                    # The input function makes the program wait for user input
                                    # Input returns integers, so letters and special characters cause errors
        print('') # These blank print statements are for neatness
       

        if int(answer) == 1:

            custom_active = True
            print("---------------------------------------------------")
            print('Live mode')
            custom_budget = input('Type your budget : ')
            active_product_list = []

            while custom_active:

                custom_product = input('Enter a product name you would like? Eg: Coke Can, Bread, Spaghetti, Tomato Sauce, Big Bags : ')
                if not s.find_product(custom_product):
                    print('This product : {} not in stock '.format(custom_product))
                else:
                    print('Entered Product is {}'.format(custom_product))
                    custom_count = input('How many do you want? : ')

                    if int(s.find_product_qty(custom_product)) >= int(custom_count):

                        custom_sub_total = float(s.find_product_price(custom_product)) * int(custom_count)
                        print('The cost to you will be {} '.format(round(custom_sub_total, 2)))
                        data = {
                            "product" : custom_product,
                            "qty" : custom_count,
                            "sub_tot" : custom_sub_total
                        }
                        active_product_list.append(data)

                    else:
                        print('')
                        print('FAIL ! ')
                        print(f'Not enough {custom_product} in stock ')
                        print(f'{int(s.find_product_qty(custom_product))} {custom_product} in stock')
                        print(f'You want {custom_count} {custom_product}')
                        print('Please revise order and try again!')

                close_tag = input('Would you like another product? Y/N ')
                if close_tag == 'N':
                    custom_active = False
                    print('Summary')
                        
            if len(active_product_list) > 0:
                total = 0
                for product in active_product_list:
                    total = total + float(product['sub_tot'])
                
                if float(total) > float(custom_budget):
                    print('FAIL! ')
                    print(f"Your budget is ...")
                    print(f'The total cost of all items is ...! {total}')
                    print("You do not have enough money")
                    print(f"Total of 0 will be deducted from your budget")
                    print(f"Your budget is {custom_budget}")
                    print(f"Total of 0 added to shop")
                    print(f"Shop has {round(float(s.cash), 2)} in cash")

                else:
                    print('SUCCESS! ')
                    print(f"Your budget is {custom_budget}")
                    print("You have enough money")
                    print(f"Total of {round(total,2)} will be deducted from your budget")
                    print(f"Total of {round(total,2)} added to shop")
                    #update the stock
                    for stock in s.stock:
                        # print(stock)
                        for product in active_product_list:
                            if stock.name() == product['product']:
                                # print('product name is there')
                                qty = int(stock.quantity) - int(product['qty'])
                                stock.update_qty(qty)


                    shop_total = float(s.cash) + float(total)
                    s.update_cash(shop_total)
                    custom_budget = float(custom_budget) - float(total)
                    # print(s.stock[0].product.name, s.stock[0].quantity)
                    
                    # print(f"Shop has {round(shop_total, 2)} in cash")
            else:
                print('something went wrong')

            print("---------------------------------------------------")

        elif int(answer) == 2:
            print("---------------------------------------------------")
            customer_csv_path = all_csv_files[int(answer)-2]
            print(f'you selected {customer_csv_path} as a current customer data')
            print('')
            c = Customer(customer_csv_path)
            print(c)
            print('')
            print("---------------------------------------------------")

        elif int(answer) == 3:
            print("---------------------------------------------------")
            customer_csv_path = all_csv_files[int(answer)-2]
            print(f'you selected {customer_csv_path} as a current customer data')
            print('')
            c = Customer(customer_csv_path)
            print(c)
            print('')
            print("---------------------------------------------------")
        
        elif int(answer) == 4:
            print("---------------------------------------------------")
            customer_csv_path = all_csv_files[int(answer)-2]
            print(f'you selected {customer_csv_path} as a current customer data')
            print('')
            c = Customer(customer_csv_path)
            print(c)
            print('')
            print("---------------------------------------------------")

        elif int(answer) == 0:  # This is how we exit the program. We make active go from True to False.
            print('Your option is : 1) for live mode')               # This has to do with how we designed the while loop. Since it's dependant on the active variable to run
            active = False
        else:  # This is for if the user enters any number that's not on the list
            print('')
            print("0) Exit")
            print('')

    except Exception as e: 
        print('')
        print(e)
        print("NameError: Please Use Numbers Only")
        print('')



