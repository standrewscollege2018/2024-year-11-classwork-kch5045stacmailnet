# setting up and connecting
# import sqlite library
import sqlite3

DATABASE = "students.db"
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()
