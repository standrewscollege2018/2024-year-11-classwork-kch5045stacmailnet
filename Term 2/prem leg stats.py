'''this program codes for the user to search for results for the 20 premier league football clubs from the 2023-24 season, up to date on april 29'''
# setting up and connecting
# import sqlite library
import sqlite3
DATABASE = "premlegstats.db"
# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# functions for error catching if the input is an integer, string, or if the integer is in range with valid values
def int_error_catch(user_input):
    try:
        if user_input.strip(" ") == "":
            print(f"Please enter an integer, and not a blank.")
            return False
        else:
            int(user_input)
            return True
    except ValueError:
        print(f"Please enter an integer..")
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

# names of fields
field_names = ["team", "average_age", "possession", "goals", "assists", "xG"]

get_name = True
while get_name:
    name = input("Please enter your name: ")
    if name.strip(" ") != "":
        get_name = False

# welcome message
print(f"Hello {name}.")

# running the code
searching = True
while searching:
    # ask if user wants to search the database or quit the program
    print("Would you like to:\n1. Search the database\n2. Quit the program")
    search_or_quit = True
    while search_or_quit:
        user_run = input()
        if int_error_catch(user_run) == True:
            if in_range(1, 2, user_run) == True:
                search_or_quit = False
    # user wanted to quit
    if user_run == 2:
        searching = False
    else:
        # user wants to search the database + menu
        print("How would you like to search the database?")
        print("""1. See all statistics
2. Team with the oldest or youngest age
3. The team with the most possessions
4. The team(s) scored the most goals
5. The team(s) outperformed their xG by the most (or underperformed)""")
        print("Please select which field you would like to search with by inputting the corresponding number (1-6)")
        # ask user for which field they want to search with
        get_field = True
        while get_field:
            field = input()
            if int_error_catch(field) == True:
                if in_range(1, 6, field) == True:
                    get_field = False
        # user chose the older or younger age
        if field == 2:
            print("Would you like the team(s) with the:\n1. Youngest average age\n2. Oldest average age")
            get_age = True
            while get_age:
                age_field = input()
                if int_error_catch(age_field) == True:
                    if in_range(1, 2, age_field) == True:
                        get_age = False
        if field == 5:
            print("Would you like the team(s) who:\n1. Underperformed their xG\n2. Overperformed their xG")
            get_xG = True
            while get_xG:
                user_xG = input()
                if int_error_catch(user_xG) == True:
                    if in_range(1, 2, user_xG) == True:
                        get_xG = False

        # search
        cursor.execute("SELECT ")





