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

a = True
while a:
    name = input("Enter the name: ")
    like_name = f"%{name}%"
    cursor.execute("SELECT name, class, age, fare, survived FROM person WHERE name LIKE ?", (like_name,))
    people = cursor.fetchall()
    print(f"{len(people)} result(s) found")
