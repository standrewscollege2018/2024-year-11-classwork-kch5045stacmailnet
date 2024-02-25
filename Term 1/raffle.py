import random
# list of names
names = []
ask1 = True
ask2 = True
ask3 = True
print("Hello, welcome to this raffle.")


# while loop to continue to ask for a prize that isnt blank
while ask1 == True:
    prize = input("Please enter a prize. ").lower()
    if prize.strip(" ") == "":
        print("Please try again.")
    else:
        ask1 = False
        # while loop to ask for prize value
        while ask2 == True:
            try:
                worth = input("Please enter the prize's value. ")
                int(worth)
                if worth.strip(" ") == "":
                    print("Please try again.")
                else:
                    ask2 = False
                    # while loop to continue to ask for names
                    while ask3 == True:
                        name = input("Please enter the names of the contenders. ")
                        try:
                            work = int(name)
                            print("Please enter a valid name.")
                        except ValueError:
                            pass
                            if name.strip(" ") == "":
                                print("Please try again.")
                            elif name.lower() == "end":
                                ask3 = False
                            else:
                                name = name.capitalize()
                                names.append(name)
            except ValueError:
                print("Please try again.")


# prints statements
try:
    if len(names) > 1:
        print(f"There are {len(names)} people in the raffle.")
    else:
        print(f"There is {len(names)} person in the raffle.")
    print(f"{names[random.randint(0, len(names))]} has won the {prize}.")
except:
    ask1 = True
    ask2 = True
