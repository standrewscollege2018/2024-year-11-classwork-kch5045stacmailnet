''' This program enables users to add students to the database '''

####### This is the setup stuff that will appear on every program ############

# Start by importing the sqlite3 library
import sqlite3

# Set the database that we will connect to
DATABASE = "students.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

error_message = "Please try again. Enter"

def int_error_catch(user_input):
    try:
        if user_input.strip(" ") == "":
            print(f"{error_message} an integer, and not a blank.")
            return False
        else:
            int(user_input)
            return True
    except ValueError:
        print(f"{error_message} an integer.")
        return False

def str_error_catch(user_input):
    try:
        if user_input.strip(" ") == "":
            print(f"{error_message} a string of characters, and not a blank.")
            return False
        else:
            int(user_input)
            print(f"{error_message} a string of characters, and not integers.")
            return False
    except ValueError:
        return True

def in_range(smaller, larger, user_number):
    if user_number < smaller or user_number > larger:
        return False
    else:
        return True

#### Menu system for the program #######
run_program = True
while run_program:
    menu = "Main Menu"
    print(menu)
    print("="*len(menu))
    print("""1. Add a student
2. Search for students
3. See all students
4. Quit""")

    # get menu selection
    get_selection = True
    while get_selection:
        try:
            selection = int(input("Enter selection: "))
            if in_range(1, 4, selection) == False:
                print("You must enter a number from 1 to 4")
            else:
                get_selection = False
        except ValueError:
            print("Only numbers from 1 to 4 allowed")

    # Now that we have the selection, do what the user wants

    ### Add student - asks for each field ###
    if selection == 1:
        print("\nAdd new student")
        fields = ["Enter the first name: ", "Enter the first name: ", "Enter the last name: ", "Enter the last name: ", "Enter the tutor group: ", "Enter the city: ", "Enter the year group: ", "Enter the year group: "]
        for field in fields:
            fields[fields.index(field)] = input(field)
            while str_error_catch(field) != True or int_error_catch(field) != True:
                fields[fields.index(field)] = input(field)
        cursor.execute("INSERT INTO student (firstName, lastName, tutorGroup, city, yearGroup) VALUES (?, ?, ?, ?, ?)", (fields[0], fields[1], fields[2], fields[3], fields[4]))
        connection.commit()

    ### Search for a student ###
    elif selection == 2:
        print("\nSearch for students")
        search_field = input("""Search students by:
1. First name
2. Last name
3. Tutor group
4. City
5. Year group
Enter desired search field: """)
        while int_error_catch(search_field) != True:
            if in_range(1, 5, search_field) != True:
                search_field = input("Enter desired search field: ")

        if search_field == "1":
            first_name = input("Enter the first name: ")
            while str_error_catch(first_name) != True:
                first_name = input("Enter the first name: ")
                like_first_name = f"%{first_name}%"
            cursor.execute("SELECT * FROM student WHERE firstName LIKE ?", (like_first_name,))
        if search_field == 2:
            surname = input("Enter the last name: ")
            while str_error_catch(surname) != True:
                surname = input("Enter the last name: ")
                like_surname = f"%{surname}%"
            cursor.execute("SELECT * FROM student WHERE lastName LIKE ?", (like_surname,))
        if search_field == 3:
            tutor_group = input("Enter the tutor group code: ")
            while str_error_catch(tutor_group) != True:
                tutor_group = input("Enter the tutor group code: ")
                like_tutor = f"%{tutor_group}%"
            cursor.execute("SELECT * FROM student WHERE tutorGroup LIKE ?", (like_tutor,))
        if search_field == 4:
            city = input("Enter the city: ")
            while str_error_catch(city) != True:
                city = input("Enter the city: ")
                like_city = f"%{city}%"
            cursor.execute("SELECT * FROM student WHERE city LIKE ?", (like_city,))
        if search_field == 5:
            year = input("Enter the year group: ")
            while int_error_catch(year) != True:
                year = input("Enter the year group: ")
            cursor.execute("SELECT * FROM student WHERE year = ?", (year,))


    ### Show all students ###
    elif selection == 3:
        print("\nAll students")
        cursor.execute("SELECT * FROM student")

    # prints students
    students = cursor.fetchall()
    for individual in students:
        print(f"{individual[1]:15} {individual[2]:15} {individual[3]:5} {individual[4]:15} {individual[5]}")

    ### Quit program ###
    else:
        run_program = False
