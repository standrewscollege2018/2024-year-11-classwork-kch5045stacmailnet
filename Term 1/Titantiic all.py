# setting up and connecting
# import sqlite library
import sqlite3

DATABASE = "people.db"

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

def in_range(smaller, larger, user_number):
    if user_number < smaller or user_number > larger:
        return False
    else:
        return True

# print welcome message
welcome = "Welcome to the Titanic passenger database"
print(welcome)
print("=" * len(welcome))

error_message = ["Please try again. Enter", "an integer between", "either"]

# while loop so user can continually ask
continuous = True
while continuous:
    # ask and get user's field search preference + error catch for integers and blanks
    ask_quit = True
    while ask_quit:
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

        # ask for which field the user wants to search by
        get_field = True
        while get_field:
            smaller = 1
            larger = 3
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

        # user wants to search by name
        if user_option == 1:
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
                        # input of name from user and fuzzy search for results of name
                        like_name = f"%{name}%"
                        cursor.execute("SELECT name, class, age, fare, gender, survived FROM person WHERE name LIKE ?", (like_name,))
                        get_name = False

        # user wants to search by class
        if user_option == 2:
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
                        cursor.execute("SELECT name, class, age, fare, gender, survived FROM person WHERE class = ?", (passenger_class,))
                        get_class = False
                except ValueError:
                    # error catch for not integer
                    print(f"{error_message[0]} {error_message[1]} {smaller} and {larger}.")

        # user wants to search by living status
        if user_option == 3:
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
                        # search query for passengers with desired living status
                        cursor.execute("SELECT name, class, age, fare, gender, survived FROM person WHERE survived = ?", (passenger_status,))
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
        # usr quitted program
        print("Farewell!")
        continuous = False
