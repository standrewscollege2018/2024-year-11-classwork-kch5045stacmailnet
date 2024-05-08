# setting up and connecting
# import sqlite library
import sqlite3

DATABASE = "cars.db"

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()


#Task 1: Select and display the number plate, make and model of every car
'''cursor.execute("SELECT plate, make, model FROM car")
results = cursor.fetchall()
print(f"{'Plate':8} {'Make':15} {'Model':15}")
print("=" * 35)
for car in results:
    print(f"{car[0]:8} {car[1]:15} {car[2]:15}")'''

#Task 2: Select and display all information about ever red car
'''cursor.execute("SELECT * FROM car WHERE colour = 'Red'")
results = cursor.fetchall()
print(f"{'ID':3} {'Plate':8} {'Owner':10} {'Make':12} {'Model':9} {'Year':6} Colour")
print("="*69)
for car in results:
    print(f"{car[0]:3} {car[1]:8} {car[2]:10} {car[3]:12} {car[4]:8} {car[5]:5}   {car[6]}")'''

#Task 3: Select and display all information about every car, arranging by number plate order
'''cursor.execute("SELECT * FROM car ORDER BY plate")
results = cursor.fetchall()
print(f"{'ID':3} {'Plate':8} {'Owner':17} {'Make':15} {'Model':12} {'Year':6} Colour")
print("="*69)
for car in results:
    print(f"{car[0]:3} {car[1]:8} {car[2]:17} {car[3]:15} {car[4]:12} {car[5]:5}   {car[6]}")'''

#Task 4: Select and display all information about Fords, arranging in alphabetical order by driver name
'''cursor.execute("SELECT * FROM car WHERE make = 'Ford' ORDER BY owner")
results = cursor.fetchall()
print(f"{'ID':3} {'Plate':8} {'Owner':10} {'Make':7} {'Model':9} {'Year':6} Colour")
print("="*55)
for car in results:
    print(f"{car[0]:3} {car[1]:8} {car[2]:10} {car[3]:7} {car[4]:8} {car[5]:5}   {car[6]}")'''

#Task 5: Select and display all information about cars with a B somewhere in the number plate
'''cursor.execute("SELECT * FROM car WHERE plate LIKE '%B%'")
results = cursor.fetchall()
print(f"{'ID':3} {'Plate':8} {'Owner':9} {'Make':15} {'Model':9} {'Year':6} Colour")
print("="*69)
for car in results:
    print(f"{car[0]:3} {car[1]:8} {car[2]:9} {car[3]:15} {car[4]:9} {car[5]:4}   {car[6]}")'''

#Task 6: Select and display the number plate and name of the owner of every Ford and Kia
'''cursor.execute("SELECT plate, owner FROM car WHERE make = 'Ford' OR make = 'Kia'")
results = cursor.fetchall()
print(f"{'Plate':8} {'Owner':10}")
print("=" * 16)
for car in results:
    print(f"{car[0]:8} {car[1]:10}")'''

# Task 7: Count how many red cars there are
'''cursor.execute("SELECT * FROM car WHERE colour = 'Red'")
results = cursor.fetchall()
print(len(results))'''
