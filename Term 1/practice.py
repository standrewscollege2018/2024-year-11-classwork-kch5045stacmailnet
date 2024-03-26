# setting up and connecting

# set up database we are connecting to
# uppercase -> constant
# files in same folder

# import sqlite library
import sqlite3

DATABASE = "students.db"

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# run a query
cursor.execute("SELECT * FROM student LIMIT 100")
# get results
results = cursor.fetchall()

print(f"{'First Name':10} {'Last Name':15} Tutor Group")
print("="*38)

# loop over results list and display each result
for student in results:
    print(f"{student[0]} {student[1]}")
'''
# 'looks neater if want counter'
for i in range(len(results)):
    print(results[i])



for student in results:
    print(f"{student[0:len(student)]}")'''
