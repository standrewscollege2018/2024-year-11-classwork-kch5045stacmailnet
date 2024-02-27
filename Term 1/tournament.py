# empty list to store names
opp_names = []
# variables to calculate scores
your_final_score = 0
opp_final_score = 0
# variables to index
ind = 0
ind_2 = 0
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
    try:
        # getting score for your team
        your_score = input(
            f"Please enter the result of your team against {opp_names[ind]}. "
        )
        if str(your_score).strip(" ") == "":
            print("Please try again.")
        elif int(your_score) < 0:
            print("Please try again.")
        else:
            int(your_score)
            try:
                # getting score of opposite team
                opp_score = input(f"Please enter the result of {opp_names[ind_2]}. ")
                # test for blanks or negative points
                if str(opp_score).strip(" ") == "":
                    print("Please try again.")
                elif int(opp_score) < 0:
                    print("Please try again.")
                # calculating points
                elif int(your_score) > int(opp_score):
                    your_final_score = your_final_score + 3
                    ind = ind + 1
                    ind_2 = ind_2 + 1
                elif int(your_score) == int(opp_score):
                    your_final_score = your_final_score + 2
                    ind = ind + 1
                    ind_2 = ind_2 + 1
                elif int(your_score) < int(opp_score):
                    your_final_score = your_final_score + 1
                    ind = ind + 1
                    ind_2 = ind_2 + 1
            except ValueError:
                print("Please try again.")
    except ValueError:
        print("Please try again.")
    except IndexError:
        ask_2 = False

# prints result
if your_final_score > len(opp_names):
    print(f"Wahoo! Your team has won {your_final_score} points in the tournament.")
elif your_final_score == len(opp_names):
    print(
        f"Try better. Your team has won {len(opp_names)} points in the tournament and it's time for you to consider training."
    )
