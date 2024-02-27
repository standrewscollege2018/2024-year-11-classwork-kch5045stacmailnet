''' This program runs a raffle. It prompts the user to add all of the names
of those people entering the raffle, randomly selecting the winner. '''

# Import the random package
import random

# List of names of those entered in the raffle
names = []

# First, get the name and value of the prize being raffled
print("Welcome to the raffle program")
prize = input("What is the prize being raffled? ")
value = input(f"What is the value of the {prize} (do not enter the $ sign) ")
print()

# Get the names of those being entered. User enters 'end' to stop
get_name = True
while get_name:
    name = input("Enter name of entrant: ")
    if name.strip(" ") == "":
        print("Name can not be blank")
    elif name == "end":
        get_name = False
    else:
        names.append(name)

# Now we display a short message saying how many people are in the raffle
print(f"There are {len(names)} people in the draw for the {prize}.")

# Select the winner
winner = random.randint(0,len(names)-1)
print(f"And the winner of the {prize}, valued at ${value}, is..... {names[winner]}!")
