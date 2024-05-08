# setting up and connecting
# import sqlite library
import sqlite3

DATABASE = "cars.db"

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# get plate from user and run search
plate = input("Enter plate number: ")

# this is for exact match
cursor.execute("SELECT * FROM car WHERE plate = ?", (plate,))
results = cursor.fetchall()

for car in results:
    print(f"{car[1]:10} {car[2]:10}")

# this is a fuzzy search
cursor.execute("SELECT * FROM car WHERE plate = ?", (plate,))
