#get name
name = input()

# set up list of names
names = []

# error catching & loop to ask for names
ask = True
while ask == True:
    try:
        please_work = int(name)
        print("Please try again.")
    except ValueError:
        pass
    name = name.lower()
    # stop if input is stop
    if name == "stop":
        ask = False
    # check if it is blank
    elif name.strip(" ") == "":
        print("Please try again.")
        ask == False
        name = input()
        ask == True
    # check if number
    else:
        # add name
        name = name.capitalize()
        names.append(name)
        name = input()
"""    else:
        for letter in name:
            try:
                please_work = int(letter)
                print("Please try again.")
                ask == False
                name = input()
                ask == True
            except ValueError:
                pass
"""


# printing the names
names.sort()
ind = 1
ind2 = 0
for nam in names:
    print(str(ind) + ".", nam)
    ind = int(ind) + 1
