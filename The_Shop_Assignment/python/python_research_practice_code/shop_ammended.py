
import csv
import pandas as pd
import numpy as np
from dataclasses import dataclass, field
from typing import List
import os



"""---------------------------------------------------------------------------------------------------------------"""
# Method 1 collecting data from the stock CSV file


print('--------------------------------------------------------------------------')


df = pd.read_csv('../stock.csv')
mylist =[]


mystockdict = {"product":[1.00,5]}

for col in df.columns: 
    mylist.append(col) 


shop_cash = mylist[0]
shop_cash = float(shop_cash)

print("Shop cash is", shop_cash)
print('The shop has the following stock which will be checked against your orders')

#https://docs.python.org/3/library/csv.html
with open('../stock.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    myproducts = mylist[0]
    
    for row in reader:
        mystockdict[row[myproducts]] = [row['charge'],row['quantity']]
        print(row[myproducts],row['charge'], row['quantity'])
print('--------------------------------------------------------------------------')

"""---------------------------------------------------------------------------------------------------------------"""

def go_to_csv_mode():
    # Method 1 collecting data from the customer CSV file


    df = pd.read_csv('../customer.csv')
    mylist2 =[]


    mycustomerdict = {}

    for col in df.columns: 
        mylist2.append(col) 

    print(mylist2)

    #https://docs.python.org/3/library/csv.html

    use_this_file = '../' + choice_of_file #using customer file chosen from dictionary value

    with open(use_this_file , newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        my_customer_name = mylist2[0] # this is also used for indexing column 1
        my_customer_quantity = mylist2[1] # this is also used for indexing column 2
        customer_budget = mylist2[1]
        cost_of_shopping_list = 0

        print("Customer name is:", my_customer_name)
        print("Customer budget is:", customer_budget)
              

        
        for row in reader:
            abc = row[my_customer_name]

            key_for_getting_price = row[my_customer_name] #this takes the product name from the customer list


            try:
                price = mystockdict[key_for_getting_price]

                print("price",price)

                ed_price = price[0]
                cost_of_shopping_list += float(ed_price) * float(row[my_customer_quantity]) 

                
                mycustomerdict[abc] = ed_price, row[my_customer_quantity]
            except KeyError:
                print("The shop does not have any: ", key_for_getting_price)
                pass
            



            
            print(row[my_customer_name], ed_price, row[my_customer_quantity])

    print(mycustomerdict)

    """---------------------------------------------------------------------------------------------------------------"""

    customer_budget = float(customer_budget)


    print("Customer budget is", customer_budget, "Customer shopping list is:",cost_of_shopping_list)

    if cost_of_shopping_list > customer_budget:
        print("shop cash is", shop_cash)
        print("customer does not have enough money")

        
    else:
        print("shop cash is", shop_cash)
        print("customer has enough money")
        shop_cash += cost_of_shopping_list
        print("money added to shop")
        print("shop cash is", shop_cash)
        print("money subtracted from customer")
        print("Customer cash was", customer_budget)
        customer_budget -= cost_of_shopping_list
        print("Customer cash is now",customer_budget)


    print(mystockdict)
    for key,value in mycustomerdict.items():
        print(key,value[1])

        update = [0,value[1]] - [0,value[1]] - [0,value[1]]
        dict_value = mystockdict.get(update)
        mystockdict[update] = dict_value


    print(mystockdict)
    #mystockdict


"""---------------------------------------------------------------------------------------------------------------"""




def go_to_live_mode():
    print("Welcome to the shop live mode")
    exit

"""-------------------------- Setting up customer greeting menu and choices ------------------------------------"""

print("Welcome to the shop")

"""--------------------------Code for displaying customer files -------------------------------------------------"""
#https://stackoverflow.com/questions/9234560/find-all-csv-files-in-a-directory-using-python/12280052

files = os.listdir("../")    
files = list(filter(lambda f: f.endswith('.csv'), files))

customer_file_menu = {1 : 'for live mode'}
print('1 for live mode')

count = 2
for file in files:
    if file == 'stock.csv':
        pass
    else:
        print(count, file)
        customer_file_menu[count] = file
    count += 1

choose_customer_file = int(input("Choose your customer file or live move: e.g type 1 for live mode, 2+ for file"))


choice_of_file = customer_file_menu[choose_customer_file]
print("You chose" , choice_of_file)

if choice_of_file == 1:
    go_to_live_mode()
else:
    go_to_csv_mode()







"""
John	100.20


Coke Can	10 qty 1.1 price
Bread	3 qty 0.7 price
Jam	1 qty ---- not found
"""


{'Coke Can': (['1.1', '100'], ' 10'), 'Bread': (['0.7', '30'], ' 3')}

"""---------------------------------------------------------------------------------------------------------------"""




"""
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
            
            print(ps)
    return s
    
def read_customer(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        c = Customer(first_row[0], float(first_row[1]))
        for row in csv_reader:
            name = row[0]
            quantity = float(row[1])
            p = Product(name)
            ps = ProductStock(p, quantity)
            c.shopping_list.append(ps)
        return c 
        

def print_product(p):
    print(f'\nPRODUCT NAME: {p.name} \nPRODUCT PRICE: {p.price}')

def print_customer(c):
    print(f'CUSTOMER NAME: {c.name} \nCUSTOMER BUDGET: {c.budget}')
    
    for item in c.shopping_list:
        print_product(item.product)
        
        print(f'{c.name} ORDERS {item.quantity} OF ABOVE PRODUCT')
        cost = item.quantity * item.product.price
        print(f'The cost to {c.name} will be €{cost}')
        
def print_shop(s):
    print(f'Shop has {s.cash} in cash')
    for item in s.stock:
        print_product(item.product)
        print(f'The Shop has {item.quantity} of the above')

s = create_and_stock_shop()
print_shop(s)

c = read_customer("../customer.csv")
print_customer(c)
"""
