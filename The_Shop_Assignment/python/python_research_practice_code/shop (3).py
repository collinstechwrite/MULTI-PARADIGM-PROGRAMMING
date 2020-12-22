from dataclasses import dataclass, field
from typing import List
import csv
import re

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
            quantity = float(row[1])
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
    for item in c.shopping_list:
        check_val = find_product_price(item.product.name)
        if check_val == 0:
            print('')
            print(f'Error no {item.product.name} in Shop stock.List item ignored')
        else:
            print_product(item.product)
            print(f'{c.name} ORDERS {item.quantity} OF ABOVE PRODUCT')
            if int(find_product_qty(item.product.name)) < int(item.quantity):
                data = {
                    "product_name" : item.product.name,
                    "availble_qty" : find_product_qty(item.product.name),
                    "need_qty": item.quantity
                }
                out_of_stock.append(data)
            cost = item.quantity * item.product.price
            total = total + cost
            print(f'The cost to {c.name} will be €{str(round(cost, 2))}')
    print('--------------------------------------------------')
    print(f'The total cost to {c.name} will be €{total}')

    if len(out_of_stock) == 0:
        if float(c.budget) >= float(total):
            s = Shop()
            print('--------------------------------------------------')
            print('SUCCESS !')
            print(f"{c.name}'s budget is {c.budget}")
            print(f"{c.name} has enough money")
            print(f"total of {total} will be deducted from {c.name}'s budget")
            print(f"total of {total} added to shop")
            print(f"Shop has {s.cash}")
        else:
            s = Shop()
            print('--------------------------------------------------')
            print('FAIL !')
            print(f"{c.name}'s budget is {c.budget}")
            print(f"{c.name} has enough money")
            print(f"total of {total} will be deducted from {c.name}'s budget")
            print(f"total of {total} added to shop")
            print(f"Shop has {s.cash}")
    else:
        for out_stock in out_of_stock:
            print(f"Not enough {out_stock['product_name']} in stock")
            print(f"{out_stock['availble_qty']} {out_stock['product_name']} in stock")
            print(f"{c.name} want {out_stock['need_qty']} {out_stock['product_name']}")
            print("Please revise order and upload again!")

        
def print_shop(s):
    print(f'Shop has {s.cash} in cash')
    for item in s.stock:
        print_product(item.product)
        print(f'The Shop has {item.quantity} of the above')

active = True  # This is our on/off switch for the program. True is on and False is off.

print("---------------------------------------------------")
s = create_and_stock_shop()
print_shop(s)
print("---------------------------------------------------")


while active:  # We make a while loop. So while active(True) - keep repeating everything inside
    print("1) for live mode") # This is our menu and list options for the user - It's inside a while loop so that the entire program doesn't run once and then exit.
    print("2) customer_too_much_bread.csv")
    print("3) customer.csv")
    print("4) customer_not_enough_money.csv")
    print('')
    print("0) Exit")

    try:  # This is a try statement used to handle errors
        answer = input("Option: ")  # This is a variable which stores the value a user enters
                                    # The input function makes the program wait for user input
                                    # Input returns integers, so letters and special characters cause errors
        print('') # These blank print statements are for neatness
       

        if int(answer) == 1: 
            print("---------------------------------------------------")
            print('Live Mode')
            custom_budget = input('Enter your budget : ')
            print(custom_budget)
            print("---------------------------------------------------")
        elif int(answer) == 3:
            print("---------------------------------------------------")
            c = read_customer("../customer.csv")
            print_customer(c)
            print("---------------------------------------------------")

        elif int(answer) == 0:  # This is how we exit the program. We make active go from True to False.
            print('Your option is : 1) for live mode')               # This has to do with how we designed the while loop. Since it's dependant on the active variable to run
            active = False
        else:  # This is for if the user enters any number that's not on the list
            print('')
            print("0) Exit")
            print('')
    except NameError:  # This is part of the try statement. This is how we handle the errors
                       # If it's a NameError - Do this and so on
                       # NameError means we entered letters or rather variable names that are not defined in the code.
        print('')
        print("NameError: Please Use Numbers Only")
        print('')
    except SyntaxError:  # SyntaxError means we typed letters or special characters i.e !@#$%^&*( or if we tried to run python code
        print('')
        print("SyntaxError: Please Use Numbers Only")
        print('')
    except TypeError:  # TypeError is if we entered letters and special characters or tried to run python code
        print('')
        print("TypeError: Please Use Numbers Only")
        print('')
    except AttributeError:  # AttributeError handles rare occurances in the code where numbers not on the list are handled outside of the if statement
        print('')
        print("AttributeError: Please Use Numbers Only")
        print('')

