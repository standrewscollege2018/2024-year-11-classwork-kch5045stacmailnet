# setting up and connecting
# import sqlite library
import sqlite3

DATABASE = "people.db"

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# create an SQL table to refine results if user decides to search with more than one field
cursor.execute('''
    CREATE TABLE IF NOT EXISTS "person_limited" (
	"name"  TEXT,
    "class" INTEGER,
    "age"   INTEGER,
    "fare"  INTEGER,
    "gender"    TEXT,
    "survived"  INTEGER)''')

# function to check if the user's number is within a valid range
def in_range(smaller, larger, user_number):
    if user_number < smaller or user_number > larger:
        return False
    else:
        return True

# print welcome message and ask for name for user-friendliness
welcome = "Welcome to the Titanic passenger database"
print(welcome)
print("=" * len(welcome))
user_name = input("What is your name?\n").capitalize()
if user_name.strip(" ") == "":
    user_name = "neglected child"

error_message = ["\nPlease try again. Enter", "an integer between", "either"]

# while loop so user can continually ask
continuous = True
while continuous:
    # ask if user wants to search database + error catch for integers and blanks
    ask_quit = True
    while ask_quit:
        # these two following variables are for the function and error message (same for rest of code)
        smaller = 1
        larger = 2
        try:
            user_quit = int(input(f"Hello {user_name}, would you like to search the database or quit the program? (1 to search the database, 2 to quit the program) "))
            if in_range(smaller, larger, user_quit) == True:
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
3. Search by survival status
4. Search by fare paid\n""")

        # see how many fields the user wants to search the database with + error checking
        get_more_field = True
        while get_more_field:
            smaller = 1
            larger = 4
            try:
                number_of_fields = int(input("How many fields would you like to search the database with? "))
                if in_range(smaller, larger, number_of_fields) == False:
                    print(f"{error_message[0]} {error_message[1]} {smaller} and {larger}.")
                else:
                    get_more_field = False
            except ValueError:
                print(f"{error_message[0]} {error_message[1]} {smaller} and {larger}.")

        # list to store options the user chooses
        fields = []

        # while loop to make sure user doesn't choose the same option more than once
        while number_of_fields != 0:
            # ask for which field the user wants to search by
            get_field = True
            while get_field:
                smaller = 1
                larger = 4
                try:
                    user_option = int(input("\nWhich field would you like to search the database with? (1 - 4) "))
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
                if user_option not in fields:
                    get_name = True
                    while get_name:
                        # get name input from user
                        name = input("\nEnter the name: ")
                        try:
                            # error catch for integer and blank
                            int(name)
                            print("Please do not enter an integer. There are no passengers with numbers in their name.")
                        except ValueError:
                            # error catch for blank
                            if name.strip(" ") == "":
                                print("Please try again. Do not enter a blank.")
                            else:
                                # user entered valid input, option get appended to list for query, fields counter goes down just in case user decided to input two things for 1 field
                                like_name = f"%{name}%"
                                fields.append(user_option)
                                number_of_fields = number_of_fields - 1
                                get_name = False
                else:
                    print("Please try again. You have already chosen this field.")

            # user wants to search by class
            if user_option == 2:
                if user_option not in fields:
                    get_class = True
                    while get_class:
                        # get class input from user
                        passenger_class = input("\nEnter the class of the passengers (1 - 3): ")
                        try:
                            # error check for blank and integer
                            passenger_class = int(passenger_class)
                            if in_range(smaller, larger, passenger_class) == False:
                                print(f"{error_message[0]} {error_message[1]} {smaller} and {larger}.")
                            else:
                                # user entered valid input
                                fields.append(user_option)
                                number_of_fields = number_of_fields - 1
                                get_class = False
                        except ValueError:
                            # error catch for not integer
                            print(f"{error_message[0]} {error_message[1]} {smaller} and {larger}.")
                else:
                    print("Please try again. You have already chosen this field.")

            # user wants to search by living status
            if user_option == 3:
                if user_option not in fields:
                    get_status = True
                    while get_status:
                        smaller = 0
                        larger = 1
                        # get living status input from user
                        passenger_status = input("\nEnter the living status of the passengers (0 for deceased, 1 for survived): ")
                        try:
                            # error catch for integer or blank
                            passenger_status = int(passenger_status)
                            if in_range(smaller, larger, passenger_status) == False:
                                print(f"{error_message[0]} {error_message[2]} {smaller} or {larger}.")
                            else:
                                # user entered valid input, option get appended to list for query, fields counter goes down just in case user decided to input two things for 1 field
                                fields.append(user_option)
                                number_of_fields = number_of_fields - 1
                                get_status = False
                        except ValueError:
                            print(f"{error_message[0]} {error_message[2]} {smaller} or {larger}.")
                else:
                    print("Please try again. You have already chosen this field.")

            if user_option == 4:
                if user_option not in fields:
                    get_fare = True
                    while get_fare:
                        smaller = 0
                        larger = 512.3292
                        lowest_fare = 0
                        highest_fare = 0
                        try:
                            # get class input from user
                            fare_1, fare_2 = input("\nEnter the range of the passengers' fare as numbers separated with a space between 0 and 512.3292: ").split(" ")
                            # error check for blank and integer
                            fare_1 = float(fare_1)
                            fare_2 = float(fare_2)
                            if in_range(smaller, larger, fare_1) == False or in_range(smaller, larger, fare_2) == False:
                                print(f"{error_message[0]} {error_message[1]} {smaller} and {larger}.")
                            else:
                                # organise to make which value the lowest and highest
                                if fare_1 > fare_2:
                                    highest_fare = fare_1
                                    lowest_fare = fare_2
                                elif fare_1 < fare_2:
                                    highest_fare = fare_2
                                    lowest_fare = fare_1
                                else:
                                    highest_fare = fare_1
                                    lowest_fare = highest_fare
                                # user entered valid input, option get appended to list for query, fields counter goes down just in case user decided to input two things for 1 field
                                fields.append(user_option)
                                number_of_fields = number_of_fields - 1
                                get_fare = False
                        except:
                            # error catch for not integer or not 2 numbers
                            print(f"{error_message[0]} two numbers between {smaller} and {larger}, separated with a space.")
                else:
                    print("\nPlease try again. You have already chosen this field.")

        cursor.execute("SELECT name, class, age, fare, gender, survived FROM person")
        limited_people = cursor.fetchall()
        for person in limited_people:
            cursor.execute("INSERT INTO person_limited(name, class, age, fare, gender, survived) VALUES (?, ?, ?, ?, ?, ?)", (person[0], person[1], person[2], person[3], person[4], person[5]))
        if 1 in fields:
            cursor.execute("DELETE FROM person_limited WHERE name NOT LIKE ?", (like_name,))
        if 2 in fields:
            cursor.execute("DELETE FROM person_limited WHERE class != ?", (passenger_class,))
        if 3 in fields:
            cursor.execute("DELETE FROM person_limited WHERE survived != ?", (passenger_status,))
        if 4 in fields:
            cursor.execute("DELETE FROM person_limited WHERE fare >= ? AND fare <= ?", (highest_fare, lowest_fare))

        # gets and prints how many results
        cursor.execute("SELECT * FROM person_limited")
        people = cursor.fetchall()
        if len(people) == 1:
            print(f"{len(people)} result found\n")
        else:
            print(f"{len(people)} results found\n")
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
