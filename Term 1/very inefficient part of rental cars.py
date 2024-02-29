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
