def int_error_catch(user_input):
    try:
        if user_input.strip(" ") == "":
            return False
        else:
            int(user_input)
            return True
    except ValueError:
        return False


def str_error_catch(user_input):
    try:
        if user_input.strip(" ") == "":
            return False
        else:
            int(user_input)
            return False
    except ValueError:
        return True
'''

a = input("a")

print(str_error_catch(a))

testing = "PLEASE WORK FOR GOODNESS SAKE"
print(testing.lower())

grr = input("why ")
while grr != "stop":
    grr = input(f"Enter the name of item : ")'''

item_name = "temp value"
reserve_price = "100000"
get_items_and_reserves = True
while get_items_and_reserves == True:
    get_item = True
    while get_item:
        item_name = input(f"Enter the name of item: ")
        if str_error_catch(item_name) == True:
            if item_name.lower() == "stop":
                get_item = False
                get_items_and_reserves = False
            else:
                get_item = False

