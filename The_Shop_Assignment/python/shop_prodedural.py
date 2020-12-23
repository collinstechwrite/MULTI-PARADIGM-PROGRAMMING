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


from dataclasses import dataclass, field
from typing import List
import csv
import re
import os
from glob import glob



@dataclass
class Product:
    name: str
    price: float = 0.0

@dataclass 
class ProductStock:
    product: Product
    quantity: int

@dataclass 
class Shop:
    cash: float = 0.0
    stock: List[ProductStock] = field(default_factory=list)

@dataclass
class Customer:
    name: str = ""
    budget: float = 0.0
    shopping_list: List[ProductStock] = field(default_factory=list)

def create_and_stock_shop():
    # create shop and assign values
    s = Shop()
    with open('../stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        s.cash = float(first_row[0])
        for row in csv_reader:
            p = Product(row[0], float(row[1]))
            ps = ProductStock(p, float(row[2]))
            s.stock.append(ps)
            #print(ps)
    return s

def filter_lines(f):
    """this generator funtion uses a regular expression
    to include only lines that have a `$` and end with a `#`.
    """
    filter_regex = r'.*\$.*\#$'
    for line in f:
        line = line.strip()
        m = re.match(filter_regex, line)
        if m:
            yield line

def find_product_price(product_name):
    with open('../stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        for row in csv_reader:
            if product_name == row[0]:
                return row[1]
        return 0

def find_product(product_name):
    with open('../stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        for row in csv_reader:
            if product_name == row[0]:
                return 1
        return 0

def find_product_qty(product_name):
    with open('../stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        for row in csv_reader:
            if product_name == row[0]:
                return row[2]
        return 0

def read_customer(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        c = Customer(first_row[0], float(first_row[1]))
        for row in csv_reader:
            name = row[0]
            quantity = int(row[1])
            price = float(find_product_price(name))
            p = Product(name, price)
            ps = ProductStock(p, quantity)
            c.shopping_list.append(ps)
        return c 
        

def print_product(p):
    print(f'\nPRODUCT NAME: {p.name} \nPRODUCT PRICE: {p.price}')

def print_customer(c):
    print(f'CUSTOMER NAME: {c.name} \nCUSTOMER BUDGET: {c.budget}')
    total = 0.0
    out_of_stock = []
    active_product_list = []

    for item in c.shopping_list:
        # check weather this product in stock
        check_val = find_product_price(item.product.name)
        if check_val == 0:
            print('')
            print(f'Error no {item.product.name} in Shop stock.List item ignored')
        else:
            print_product(item.product)
            print('')
            print(f'{c.name} ORDERS {item.quantity} OF ABOVE PRODUCT')
            if int(find_product_qty(item.product.name)) < int(item.quantity):
                data = {
                    "product_name" : item.product.name,
                    "availble_qty" : find_product_qty(item.product.name),
                    "need_qty": item.quantity
                }
                out_of_stock.append(data)

            cost = item.quantity * item.product.price
            buying_data = {
                "product" : item.product.name,
                "qty" : item.quantity,
                "sub_tot" : cost
            }
            active_product_list.append(buying_data)
            
            total = total + cost
            print(f'The cost to {c.name} will be €{str(round(cost, 2))}')
    print('--------------------------------------------------')
    print(f'The total cost to {c.name} will be €{total}')

    if len(out_of_stock) == 0:
        if float(c.budget) >= float(total):
            print('--------------------------------------------------')
            print('SUCCESS !')
            print(f"{c.name}'s budget is {c.budget}")
            print(f"{c.name} has enough money")
            print(f"total of {total} will be deducted from {c.name}'s budget")
            # updating the stock
            for stock in s.stock:
                # print(stock)
                for product in active_product_list:
                    if stock.product.name == product['product']:
                        # print('product name is there')
                        stock.quantity = float(stock.quantity) - float(product['qty'])
                        
            c.budget = float(c.budget) - float(total)
            s.cash = float(s.cash) + float(total)
            print(f"John's budget is {c.budget}")
            print(f"total of {total} added to shop")
            print(f"Shop has {s.cash}")
        else:
            print('--------------------------------------------------')
            print('FAIL !')
            print(f"{c.name}'s budget is {c.budget}")
            print(f'The total cost of all items is ...! {float(total)}')
            print(f"{c.name} does not have enough money")
            print(f"total of 0 will be deducted from {c.name}'s budget")
            print(f"John's budget is {c.budget}")
            print(f"total of 0 added to shop")
            print(f"Shop has {s.cash} in cash")
    else:
        for out_stock in out_of_stock:
            print(f"Not enough {out_stock['product_name']} in stock")
            print(f"{out_stock['availble_qty']} {out_stock['product_name']} in stock")
            print(f"{c.name} want {out_stock['need_qty']} {out_stock['product_name']}")
            print("Please revise order and upload again!")

        
def print_shop(s):
    print(f'Shop has {s.cash} in cash')
    print('The Shop has the following stock which will be cheked against your order')
    print('')
    for item in s.stock:
        print_product(item.product)
        print(f'The Shop has {int(item.quantity)} of the above')

active = True  # This is our on/off switch for the program. True is on and False is off.
s = create_and_stock_shop()

while active:  # We make a while loop. So while active(True) - keep repeating everything inside
    print('Welcome to the shop')
    print("---------------------------------------------------")
    print_shop(s)
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
                if not find_product(custom_product):
                    print('This product : {} not in stock '.format(custom_product))
                else:
                    print('Entered Product is {}'.format(custom_product))
                
                    custom_count = input('How many do you want? : ')
                    if int(find_product_qty(custom_product)) >= int(custom_count):

                        custom_sub_total = float(find_product_price(custom_product)) * int(custom_count)
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
                        print(f'{int(find_product_qty(custom_product))} {custom_product} in stock')
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
                            if stock.product.name == product['product']:
                                # print('product name is there')
                                stock.quantity = float(stock.quantity) - float(product['qty'])


                    shop_total = float(s.cash) + float(total)
                    s.cash = shop_total
                    custom_budget = float(custom_budget) - float(total)
                    print(s.stock[0].product.name, s.stock[0].quantity)
                    
                    print(f"Shop has {round(shop_total, 2)} in cash")
            else:
                print('something went wrong')
                
            print("---------------------------------------------------")

        elif int(answer) == 2:
            print("---------------------------------------------------")
            customer_csv_path = all_csv_files[int(answer)-2]
            print(f'you selected {customer_csv_path} as a current customer data')
            print('')
            c = read_customer(str(customer_csv_path))
            print_customer(c)
            print('')
            print("---------------------------------------------------")

        elif int(answer) == 3:
            print("---------------------------------------------------")
            customer_csv_path = all_csv_files[int(answer) -2]
            print(f'you selected {customer_csv_path} as a current customer data')
            print('')
            c = read_customer(str(customer_csv_path))
            print_customer(c)
            print('')
            print("---------------------------------------------------")
        
        elif int(answer) == 4:
            print("----------------------4-----------------------------")
            customer_csv_path = all_csv_files[int(answer) -2]
            print(f'you selected {customer_csv_path} as a current customer data')
            print('')
            c = read_customer(str(customer_csv_path))
            print_customer(c)
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

