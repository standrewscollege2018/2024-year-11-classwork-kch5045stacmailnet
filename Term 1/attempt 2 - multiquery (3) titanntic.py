# setting up and connecting
# import sqlite library
import sqlite3

DATABASE = "people.db"

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

def in_range(smaller_number, larger_number, user_number):
    if user_number < smaller_number or user_number > larger_number:
        return False
    else:
        return True

# print welcome message
welcome = "Welcome to the Titanic passenger database"
print(welcome)
print("=" * len(welcome))

# error message, error_message[0] and error_message[1] together is for 2 or more options, whereas error_message[0] and error_message[2] together is for only 2 options
error_message = ["Please try again. Enter", "an integer between", "either"]

# while loop so user can continually ask
continuous = True
while continuous:
    # ask and get user's field search preference + error catch for integers and blanks
    ask_quit = True
    while ask_quit:
        # (also for rest of the code) smaller is to indicate the lower bound of the valid input with the function, larger is for upper bound
        smaller = 1
        larger = 2
        try:
            user_quit = int(input("Would you like to search the database or quit the program? (1 to search the database, 2 to quit the program) "))
            if in_range(1, 2, user_quit) == True:
                ask_quit = False
            else:
                print(f"{error_message[0]} {error_message[2]} {smaller} or {larger}.")
        except ValueError:
            print(f"{error_message[0]} {error_message[2]} {smaller} or {larger}.")

    if user_quit == 1:
        # print menu + options
        print("\nMenu")
        print("=" * 4)
        print("""1. Search by name
2. Search by passenger class
3. Search by survival status\n""")

        # see how many fields the user wants to search the database with
        get_more_field = True
        while get_more_field:
            smaller = 1
            larger = 3
            try:
                number_of_fields = int(input("How many fields would you like to search the database with? "))
                if in_range(smaller, larger, number_of_fields) == False:
                    print(f"{error_message[0]} {error_message[1]} {smaller} and {larger}.")
                else:
                    get_more_field = False
            except ValueError:
                print(f"{error_message[0]} {error_message[1]} {smaller} and {larger}.")

        for i in range(number_of_fields):
            # ask for which field the user wants to search by
            get_field = True
            while get_field:
                try:
                    user_option = int(input("Which field would you like to search the database with? (1-3) "))
                    # error catch - an integer more/less than the options
                    if in_range(smaller, larger, user_option) == True:
                        get_field = False
                    else:
                        print(f"{error_message[0]} {error_message[1]} {smaller} and {larger}.")
                except ValueError:
                    # not an integer
                    print(f"{error_message[0]} {error_message[1]} {smaller} and {larger}.")

        for user_input in fields:
            # user wants to search by name
            if user_input == 1:
                get_name = True
                while get_name:
                    # get name input from user
                    name = input("Enter the name: ")
                    try:
                        # error catch for integer and blank
                        int(name)
                        print("Please do not enter an integer. There are no passengers with numbers in their name.")
                    except ValueError:
                        # error catch for blank
                        if name.strip(" ") == "":
                            print("Please try again. Do not enter a blank.")
                        else:
                            # all are valid
                            get_name = False

            # user wants to search by class
            if user_input == 2:
                get_class = True
                while get_class:
                    # get class input from user
                    passenger_class = input("Enter the class of the passengers (1 - 3): ")
                    try:
                        # error check for blank and integer
                        passenger_class = int(passenger_class)
                        if in_range(smaller, larger, passenger_class) == False:
                            print(f"{error_message[0]} {error_message[1]} {smaller} and {larger}.")
                        else:
                            # search query for desired class
                            get_class = False
                    except ValueError:
                        # error catch for not integer
                        print(f"{error_message[0]} {error_message[1]} {smaller} and {larger}.")

            # user wants to search by living status
            if user_input == 3:
                get_status = True
                while get_status:
                    smaller = 0
                    larger = 1
                    # get living status input from user
                    passenger_status = input("Enter the living status of the passengers (0 for deceased, 1 for survived): ")
                    try:
                        # error catch for integer or blank
                        passenger_status = int(passenger_status)
                        if in_range(smaller, larger, passenger_status) == False:
                            print(f"{error_message[0]} {error_message[2]} {smaller} or {larger}.")
                        else:
                            get_status = False
                    except ValueError:
                        print(f"{error_message[0]} {error_message[2]} {smaller} or {larger}.")


        # gets and prints how many results
        people = cursor.fetchall()
        print(f"{len(people)} result(s) found\n")
        if len(people) > 0:
            # prints titles and the line division
            titles = f"{'Name':55} {'Class':6} {'Age':8} {'Fare':2} {'Gender':9} {'Status'}"
            print(titles)
            print("=" * (len(titles) + 2))
            # prints each person
            for person in people:
                # add their status of living
                if person[5] == 1:
                    status = "Survived"
                else:
                    status = "Deceased"
                # prints people and their information
                print(f"{person[0][0:55]:55} {person[1]:3} {person[2]:5} {person[3]:>10} {person[4]:10}{status}")
            print()

    else:
        # user quitted program
        print("Farewell!")
        continuous = False
