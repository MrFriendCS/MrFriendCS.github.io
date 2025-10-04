# Title: N5 SDD Sport Results
# Author: Mr Friend
# Date 4 Oct 2025

# Initialise variables
nameTeam1 = ""
nameTeam2 = ""
scoreTeam1 = 0
scoreTeam2 = 0

# Display header
print("BBC Sport Results")
print("-----------------")


# Get name of Team 1
print()
nameTeam1 = input("Team 1 name: ")

# Get name of Team 2
nameTeam2 = input("Team 2 name: ")


# Get score of Team 1
print()
scoreTeam1 = int(input(nameTeam1 + " score: "))

# Get score of Team 2
scoreTeam2 = int(input(nameTeam2 + " score: "))


# Display seperator
print()
print("-----------------")
print()


# Is Team 1 score same as Team 2 score?
if scoreTeam1 == scoreTeam2:
    
    # Display draw message
    print("It's a draw!")
    
else:
    
    # Is Team 1 score more than Team 2 score?
    if scoreTeam1 > scoreTeam2:
    
        # Display Team 1 wins message
        print(nameTeam1 + " wins!")
        
    else:
    
        # Display Team2 wins message
        print(nameTeam2 + " wins!")


# Display scores
print()
print(nameTeam1 + " " + str(scoreTeam1) + ":" +
      str(scoreTeam2) + " " + nameTeam2)

# Display footer
print()
print("=================")
