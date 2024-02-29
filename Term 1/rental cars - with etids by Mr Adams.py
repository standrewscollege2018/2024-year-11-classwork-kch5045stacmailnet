''' I am a docstring '''

# cars in list for each option and to check which car they prefer
# When a car is booked, "Unavailable" is appended to the sub-list
cars = [
    [1, "1. Toyota Corolla (4)", "Toyota Corolla"],
    [2, "2. Honda CRV (4)", "Honda CRV"],
    [3, "3. Suzuki Swift (4)", "Suzuki Swift"],
    [4, "4. Mitsubishi Airtrek (4)", "Mitsubishi Airtrek"],
    [5, "5. Nissan DC Ute (4)", "Nissan DC Ute"],
    [6, "6. Toyota Previa (7)", "Toyota Previa"],
    [7, "7. Toyota Hi Ace (12)", "Toyota Hi Ace"],
    [8, "8. Toyota Hi Ace (12)", "Toyota Hi Ace"],
]
# variables to set up while loops
get_car = True
welcome_and_options = True
message_and_questions = True
available_cars_counter = 8
while message_and_questions == True:
    while welcome_and_options == True:
        # while loop to ask for preferred car
        while get_car == True:
            # welcome message
            print("""Welcome to the University vehicle rental system.
The vehicles are:""")
            # prints car options
            for vehicle in range(len(cars)):
                # If there are 5 items in the car list, it is unavailable
                if len(cars[vehicle]) == 5:
                    print(f"{vehicle+1}. {cars[vehicle][1]} + {cars[vehicle][3]}")
                else:
                    print(f"{vehicle+1}. {cars[vehicle][1]}")
            # ask for preferred car
            preferred_car = input("Which vehicle would you like to book? ")
            # error catch for spaces and values
            try:
                if preferred_car.strip(" ") == "":
                    print("Please try again. Please enter a singular integer from 1 - 8.")
                    print("")
                else:
                    preferred_car = int(preferred_car)
                    if preferred_car == 0:
                        get_car = False
                        welcome_and_options = False
                        message_and_questions = False
                    elif preferred_car > 8 or preferred_car < 0:
                        print("Please try again. Try from 1 to 8.")
                        print("")
                    else:
                        if "- Unavailable" in (cars[preferred_car-1]:
                            print("Unavailable")
                        else:
                            cars[preferred_car-1].append("- Unavailable")
                            # Get name
                            # Error check
                            # Append name to cars[preferred-1]

                        # check for/updating availability
                        for car in range(len(cars)):
                            if preferred_car == cars[car][0]:
                                availability = "- Unavailable"
                                if availability in cars[car]:
                                    print("** This vehicle is already booked. Please choose another **")
                                    print("")
                                else:
                                    cars[car].append(availability)
                                    print(f"You have booked the {cars[car][2]}")
                                    # while loop to ask for name
                                    get_name = True
                                    while get_name == True:
                                        name = input("What is your name? ")
                                        try:
                                            int(name)
                                            print("Please try again.")
                                        except ValueError:
                                            pass
                                            if name.strip(" ") == "":
                                                print("Please enter your name.")
                                            else:
                                                print(f"Thanks {name}")
                                                print("")
                                                cars[car].append(name)
                                                for check_availability in cars:
                                                    if "- Unavailable" in check_availability:
                                                        available_cars_counter = available_cars_counter - 1
                                                    # checking how many cars are still available - if all rented out, loop stops
                                                    if available_cars_counter == -28:
                                                        print("All cars have been rented out today.")
                                                        message_and_questions = False
                                                        get_car = False
                                                        welcome_and_options = False
                                                get_name = False
            except ValueError:
                print("Please try again. Please enter an integer.")
# print(available_cars_counter)

unavailable_cars_counter = 0
if message_and_questions == False:
    print("Daily summary")
    for vehicles in cars:
        if len(vehicles) == 5:
            print(vehicles[2], "-", vehicles[4])
            unavailable_cars_counter = unavailable_cars_counter + 1
if unavailable_cars_counter == 0:
    print("No cars were rented out today.")
