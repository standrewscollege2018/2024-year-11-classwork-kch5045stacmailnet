# Write your code here :-)

keep_asking = True
while keep_asking == True:
    try:
        age = float(input("Enter your age in years: "))
        weight = float(input("Enter your weight in kg: "))
        if age <= 16:
            print("You are not eligible.")
            keep_asking = False
        elif weight <= 50:
                print("You are not eligible.")
                keep_asking = False
        else:
            print("You are eligible.")
            keep_asking = False
    except ValueError:
        print("Please try again, perhaps enter a positive number or do not add units.")
