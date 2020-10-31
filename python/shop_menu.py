import os
"""
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
"""

def clear_screen(): #this function is used for clearing the screen
    os.system("cls")

def display_menu(): #this funtion is used to display the menu
    print("Chris's Shop")
    print("--------")
    print("MENU")
    print("====")
    print("1 – Customer Menu")
    print("2 - Shop Keeper Menu")
    print("x – Exit application")


def Customer_Menu():
    print("Chris's Shop")
    print("--------")
    print("CUSTOMER MENU")
    print("====")
    print("1 – Load My Orders From CSV")
    print("2 – Buy Products By Name")
    print("x – Exit Menu")

    while True:
        choice = input("Enter choice: ")
        if (choice == "1"):
            clear_screen()
        elif (choice == "x"):
            break;
        else:
            display_menu()


def Shop_Keeper_Menu():
    print("Chris's Shop")
    print("--------")
    print("SHOP KEEPER MENU")
    print("====")
    print("1 – Check shop cash")
    print("x – Exit Menu")

    while True:
        choice = input("Enter choice: ")
        if (choice == "1"):
            clear_screen()
        elif (choice == "x"):
            break;
        else:
            display_menu()






# Main function , code was repurposed from lecture menu
def main():
    # Initialise array
    array = []
    display_menu() #This function calls the user menu



    while True:
        choice = input("Enter choice: ")
        if (choice == "1"):
            clear_screen()
            Customer_Menu()
            display_menu()
        elif (choice == "2"):
            clear_screen()
            Shop_Keeper_Menu()
            display_menu()

        elif (choice == "x"):
            break;
        else:
            display_menu()

clear_screen()
if __name__ == "__main__":
    # execute only if run as a script
    main()
