# import sqlite library
import sqlite3

DATABASE = "cars.db"

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# run a query
cursor.execute("SELECT * FROM car LIMIT 10")
# get results
cars = cursor.fetchall()

print(f"{'ID':4} {'Plate':10} {'Colour':10} {'Driver':15} {'Make':10} Model")
print("="*38)

# print results
for car in cars:
    print(f"{car[0]}")
