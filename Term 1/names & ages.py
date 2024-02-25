people = []
ask = True
while ask == True:
    person = []
    # get name
    name = input("Please state your name. ")
    name = name.lower()
    try:
        int(name)
        print("Please try again, unless you are Elon Musk's child.")
    except ValueError:
        pass
        if name == "stop":
            ask = False
        elif name.strip(" ") == "":
            print("Please try again, unless you do not have a name, in which case, I am sorry for you.")
        else:
            age = input("Now tell me your age or else I'll beat you up. ")
            try:
                a = int(age)
            except:
                print("Please try again.")
            a = int(age)
            if age.strip(" ") == "":
                print("Please try again.")
            elif a <= 0:
                print("Please try again.")
            elif a >= 120:
                print("Please try again.")
            else:
                person.append(name.capitalize())
                person.append(age)
                people.append(person)

num = 1

for person in people:
    print(f"{num}. {person[0]} {person[1]}")
    num = num + 1
