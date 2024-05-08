# setting up and connecting
# import sqlite library
import sqlite3

DATABASE = "people.db"

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# extension task - loop
no_quitting = True
while no_quitting:
    # while loop for error catching and asking for the class if they enter an invalid input
    get_class = True
    while get_class:
        try:
            # get class from user and run search
            passenger_class = int(input("What class do you want to search on? (1-3) "))
            # not valid integer
            if passenger_class > 3 or passenger_class < 1:
                print("Please enter an integer from 1 to 3.")
            # they entered valid input
            else:
                get_class = False
        # not an integer
        except ValueError:
            print("Please enter an integer from 1 to 3.")

    # while loop for error catching and asking for if the passenger survived if they enter an invalid input
    get_survived = True
    while get_survived:
        try:
            # get living status from user and run search
            living_status = int(input("Enter 1 for list of survivors or 0 for deceased: "))
            # not valid integer
            if living_status > 1 or living_status < 0:
                print("Please enter either 1 or 0.")
            # they entered valid input
            else:
                get_survived = False
        # not an integer
        except ValueError:
            print("Please enter either 1 or 0.")

    # execute function and search
    cursor.execute("SELECT name FROM person WHERE class = ? AND survived = ?", (passenger_class,living_status))
    passengers = cursor.fetchall()

    # print how many results
    print(f"There are {len(passengers)} results found")
    # print the passengers' names
    for passenger in passengers:
        print(f"{passenger[0]}")
    print()
