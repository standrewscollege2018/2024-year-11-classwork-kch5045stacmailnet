# setting up and connecting
# import sqlite library
import sqlite3

DATABASE = "people.db"

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

user = int(input("tesitng: "))
testing2 = user

cursor.execute("SELECT name, class, age, fare, gender, survived FROM person WHERE class = ?", (testing2,))

people = cursor.fetchall()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS "person_limited" (
	"name"  TEXT,
    "class" INTEGER,
    "age"   INTEGER,
    "fare"  INTEGER,
    "gender"    TEXT,
    "survived"  INTEGER)''')

testing = 1

for person in people:
    cursor.execute("INSERT INTO person_limited (name, class, age, fare, gender, survived) VALUES (?, ?, ?, ?, ?, ?)", (person[0], person[1], person[2], person[3], person[4], person[5]))

cursor.execute("SELECT * FROM person_limited")
b = cursor.fetchall()
for i in b:
    print(i)

cursor.execute("DELETE FROM person_limited")
connection.commit()

cursor.execute("SELECT * FROM person_limited")
a = cursor.fetchall()
if len(a) == 0:
    print("Yippee it worked")

# create table and use that
