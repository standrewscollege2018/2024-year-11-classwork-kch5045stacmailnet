import random

# empty list to store names
opp_names = []

ask1 = True
ask2 = True
ask3 = True
print("Hello, welcome to the tournament.")


# while loop to continue to ask for team name that isnt blank
while ask1 == True:
    tname = input("Please enter the name of the opposing team. ").lower()
    try:
        int(tname)
        print("Please try again.")
    except ValueError:
        pass
        if tname.strip(" ") == "":
            print("Please try again.")
        else:
            ask1 = False
            # while loop to ask for opposition's names value
            while ask2 == True:
                name = input("Please enter the names of the opposing team's members. ")
                try:
                    work = int(name)
                    print("Please enter a valid name.")
                except ValueError:
                    pass
                    if name.strip(" ") == "":
                        print("Please try again.")
                    elif name.lower() == "done":
                        ask2 = False
                    else:
                        name = name.capitalize()
                        opp_names.append(name)
                        # getting results
                        result = input("Please enter the results of the team. "))
                        try:
                            int(result)
                            print("Please enter


# prints statements
try:
    if len(opp_names) > 1:
        print(f"There are {len(opp_names)} people in the raffle.")
    else:
        print(f"There is {len(opp_names)} person in the raffle.")
    print(f"{opp_names[random.randint(0, len(opp_names))]} has won the tournament.")
except:
    ask1 = True
    ask2 = True
