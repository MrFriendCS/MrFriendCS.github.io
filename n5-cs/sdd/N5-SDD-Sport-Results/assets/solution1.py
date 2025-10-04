# Title: N5 SDD Sport Results
# Author: Mr Friend
# Date 4 Oct 2025

# Initialise variables
nameTeamA = ""
nameTeamB = ""
scoreTeamA = 0
scoreTeamB = 0

# Display header
print("BBC Sport Results")
print("-----------------")


# Get name of Team A
print()
nameTeamA = input("Team A name: ")

# Get name of Team B
nameTeamB = input("Team B name: ")


# Get score of Team A
print()
scoreTeamA = int(input(nameTeamA + " score: "))

# Get score of Team B
scoreTeamB = int(input(nameTeamB + " score: "))


# Display seperator
print()
print("-----------------")
print()


# Is Team A score same as Team B score?
if scoreTeamA == scoreTeamB:
    
    # Display draw message
    print("It's a draw!")
    
else:
    
    # Is Team A score same as Team B score?
    if scoreTeamA > scoreTeamB:
    
        # Display Team A wins message
        print(nameTeamA + " wins!")
        
    else:
    
        # Display Team B wins message
        print(nameTeamB + " wins!")


# Display scores
print()
print(nameTeamA + " " + str(scoreTeamA) + ":" +
      str(scoreTeamB) + " " + nameTeamB)

# Display footer
print()
print("=================")
