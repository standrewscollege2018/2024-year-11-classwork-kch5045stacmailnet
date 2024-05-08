# setting up and connecting
# import sqlite library
import sqlite3

DATABASE = "people.db"

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# welcome message
welcome = "Welcome to the Titanic passengers database"
print(welcome)
print("=" * len(welcome))
print("Here you can search for passengers and their details")
print()

# error catching
get_name = True
while get_name:
    # get input from user
    name = input("Enter the name: ")
    try:
        # error catch for integer
        int(name)
        print("Please do not enter an integer. There are no passengers with numbers in their name.")
    except ValueError:
        # error catch for blank
        if name.strip(" ") == "":
            print("Please try again. Please do not enter a blank.")
        else:
            # input of name from user and fuzzy search for results of name
            like_name = f"%{name}%"
            cursor.execute("SELECT name, class, age, fare, survived FROM person WHERE name LIKE ?", (like_name,))
            people = cursor.fetchall()
            print(f"{len(people)} result(s) found")
            get_name = False


# prints titles and the line division
print()
titles = f"{'Name':40} {'Class':3} {'Age':5} {'Fare':5}{'Status'}"
print(titles)
print("=" * (len(titles) + 2))
# prints each person
for person in people:
    # add their status of living
    if person[4] == 1:
        status = "Survived"
    else:
        status = "Deceased"
    # prints people and their information
    print(f"{person[0]:40} {person[1]:3} {person[2]:5} {person[3]:>6} {status}")
