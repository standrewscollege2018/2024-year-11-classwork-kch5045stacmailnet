# empty list to store names
opp_names = []
# variables to calculate scores
your_final_score = 0
opp_final_score = 0
# greeting
print("Hello, welcome to the tournament.")
# while loop to continue to ask for team name that isnt blank
ask_1 = True
while ask_1 == True:
    team_name = input("Please enter the name of the opposing team. ").lower()
    # error catching - integer and blanks
    try:
        int(team_name)
        print("Please try again.")
    except ValueError:
        pass
        # check for blank
        if team_name.strip(" ") == "":
            print("Please try again.")
        # stop loop when "done" entered
        elif team_name.lower() == "done":
            ask_1 = False
        else:
            # adding names
            team_name = team_name.capitalize()
            opp_names.append(team_name)
ask_2 = True
while ask_2 == True:
    for result_2 in opp_names:
        # getting score for your team
        your_score = input("Please enter the result of your team. ")
        try:
            int(your_score)
            if your_score.strip(" ") == "":
                print("Please try again.")
            else:
                opp_score = input("Please enter the result of the opposing team. ")
                try:
                    int(opp_score)
                    if opp_score.strip(" ") == "":
                        print("Please try again.")
                    elif your_score > opp_score:
                        your_final_score = your_final_score + 3
                    elif your_score == opp_score:
                        your_final_score = your_final_score + 2
                    else:
                        your_final_score = your_final_score + 1
                    ask_2 = False
                except:
                    print("Please try again.")
                    ask_2 = True
        except:
            print("Please try again.")
            ask_2 = True

# prints result
print(f"Your team has won {your_final_score} points in the tournament.")
