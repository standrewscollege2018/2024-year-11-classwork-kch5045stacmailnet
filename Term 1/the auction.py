''' This program enables users to add items to the database '''

####### This is the setup stuff that will appear on every program ############

# Start by importing the sqlite3 library
import sqlite3

# Set the database that we will connect to
DATABASE = "auction.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# functions for error catching if the input is an integer, string, or if the integer is in range with valid values
def float_error_catch(user_input):
    try:
        if user_input.strip(" ") == "":
            print(f"Please enter a number, and not a blank.")
            return False
        else:
            float(user_input)
            return True
    except ValueError:
        print(f"Please enter a number, and not a string of characters.")
        return False

def str_error_catch(user_input):
    try:
        if user_input.strip(" ") == "":
            print(f"Please enter a string of characters, and not a blank.")
            return False
        else:
            int(user_input)
            print(f"Please enter a string of characters, and not integers.")
            return False
    except ValueError:
        return True

def in_range(smaller, larger, user_number):
    if user_number < smaller or user_number > larger:
        return False
    else:
        return True
print('To stop entering items, enter "stop"')
counter = 1
#start asking for item names
item_name = "temp value"
reserve_price = "100000"
get_items_and_reserves = True
while get_items_and_reserves == True:
    get_reserve = False
    get_item = True
    while get_item:
        item_name = input(f"Enter the name of item {counter}: ")
        if str_error_catch(item_name) == True:
            if item_name.lower() == "stop":
                get_item = False
                get_items_and_reserves = False
            else:
                get_item = False
                get_reserve = True
    while get_reserve == True:
        reserve_price = input(f'Enter the reserve price of the item "{item_name}": ')
        if float_error_catch(reserve_price) == True:
            get_reserve = False
    if item_name != "stop":
        cursor.execute("INSERT INTO item (name, reserve) VALUES (?, ?)", (item_name, reserve_price))
    connection.commit()
    counter = counter + 1

cursor.execute("SELECT name, reserve FROM item")
items = cursor.fetchall()
for item in items:
    get_purchaser = True
    while get_purchaser == True:
        purchaser = input(f'Enter the name of the purchaser of "{item[0]}": ')
        if str_error_catch(purchaser) == True:
            get_purchaser = False
    get_sale_price = True
    while get_sale_price == True:
        sale_price = input(f'Enter how much the purchaser is willing to pay for "{item[0]}": ')
        if float_error_catch(sale_price) == True:
            get_sale_price = False
    cursor.execute("UPDATE item SET purchaser = ?, salePrice = ?", (purchaser, sale_price))
