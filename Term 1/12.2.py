"""Write a program that asks the user to enter 2 integers
Sample:
Enter a number: 3
Enter another number: 5"""

# function to produce result - options of multiplication, division, addition, or subtraction
def result(a, b):
    type = input("Would you like multiplication, division, addition, or subtraction? ")
    if "multiplication" in type:
        ab = a * b
    elif "division" in type:
        ab = a / b
    elif "addition" in type:
        ab = a + b
    elif "subtraction" in type:
        ab = a - b
    else:
        return 0
    return ab

# function to ask for numbers, while loop - error catching + asking for numbers
def request(c)
    keep_asking = True
    while keep_asking == True:
        try:
            # get numbers
            a = float(input("Enter a number: "))
            b = float(input("Enter another number: "))
            keep_asking = False
        except ValueError:
            print("Please enter a number(s) instead.")
    return (a, b)

answer = result(a, b)
while answer != float:
    print("Please try again.")
    keep_asking = True
    while keep_asking == True:
        try:
            # get numbers
            a = float(input("Enter a number: "))
            b = float(input("Enter another number: "))
            keep_asking = False
            answer = result(a, b)
        except ValueError:
            print("Please enter a number(s) instead.")

