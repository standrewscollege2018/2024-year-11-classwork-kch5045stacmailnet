# empty list to store names
opp_names = []
yourScore = 0
yourFinalScore = 0
oppScore = 0
oppFinalScore = 0

ask1 = True
ask2 = True
print("Hello, welcome to the tournament.")


# while loop to continue to ask for team name that isnt blank
while ask1 == True:
    tname = input("Please enter the name of the opposing team. ").lower()
    # error catching - integer and blanks
    try:
        int(tname)
        print("Please try again.")
    except ValueError:
        pass
        if tname.strip(" ") == "":
            print("Please try again.")
        else:

            ask1 = False



        """ we want names of the teams, not their members silly.
            # while loop to ask for opposition's names value (error catching)
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
                        # adding names
                        name = name.capitalize()
                        opp_names.append(name)
"""
# getting score for your team
result1 = int(input("Please enter the results of your team. "))
while ask2 == True:
    try:
        int(result1)
        yourScore = yourScore + result1
        if result1 == "stop":
            ask2 = False
        else:
            result2 = input("Please enter the results of the opposing team. ")
            # getting score of opposing team
            try:
                int(result2)
                oppScore = oppScore + result2
            except:
                print("Please try again.")
    except:
        print("Please try again.")

# prints statement
try:
    if yourScore > oppScore:
        yourFinalScore = yourFinalScore + 3
        print(
            f"Your team won. Your team gained {yourFinalScore} points, and the opposing team gained {oppFinalScore} points."
        )
    elif yourScore == oppScore:
        print(f"Your team tied with {tname.capitalize()} at {yourFinalScore} points.")
    else:
        print(
            f"Your team lost. Your team gained {yourFinalScore} points, and the opposing team gained {oppFinalScore} points."
        )

except:
    ask1 = True
    ask2 = True
