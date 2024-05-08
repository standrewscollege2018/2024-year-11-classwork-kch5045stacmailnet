# setting up and connecting
# import sqlite library
import sqlite3

DATABASE = "cars.db"

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# get plate from user and run search
plate = input("Enter plate number: ")

'''# this is for exact match
cursor.execute("SELECT * FROM car WHERE plate = ?", (plate,))
'''
# this is a fuzzy search
# one must pre-prepare the variable
like_plate = f"%{plate}%"
cursor.execute("SELECT * FROM car WHERE plate LIKE ?", (like_plate,))
results = cursor.fetchall()


for car in results:
    print(f"{car}")

# how to run a dynamic query with two inputs
name = input("Name: ")
model = input("Model: ")
cursor.execute("SELECT * FROM car WHERE owner = ? AND model = ?", (name,model))
results = cursor.fetchall()

for car in results:
    print(car)
