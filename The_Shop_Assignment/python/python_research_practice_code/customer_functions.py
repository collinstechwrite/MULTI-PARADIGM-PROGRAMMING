from dataclasses import dataclass, field
from typing import List
import csv

"""-------------------------------------------------------"""
#These classes are needed for the customer class to work

@dataclass
class Product:
    name: str
    price: float = 0.0

@dataclass 
class ProductStock:
    product: Product
    quantity: int

"""-------------------------------------------------------"""

@dataclass
class Customer:
    name: str = ""
    budget: float = 0.0
    shopping_list: List[ProductStock] = field(default_factory=list)

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

"""----------------------------------------------------------"""
# This function is needed for customer to work

def print_product(p):
    print(f'\nPRODUCT NAME: {p.name} \nPRODUCT PRICE: {p.price}')

"""----------------------------------------------------------"""

def print_customer(c):
    print(f'CUSTOMER NAME: {c.name} \nCUSTOMER BUDGET: {c.budget}')
    
    for item in c.shopping_list:
        print_product(item.product)
        
        print(f'{c.name} ORDERS {item.quantity} OF ABOVE PRODUCT')
        cost = item.quantity * item.product.price
        print(f'The cost to {c.name} will be €{cost}')

c = read_customer("../customer.csv")
print_customer(c)
