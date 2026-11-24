# Title: N5 SDD Arcade
# Author: Mr Friend
# Date: 24 Nov 2026

# Initialise variables
score: int = 0
player: int = 0
scores: list[int] = [0 for index in range(5)]

# Display header
print("Arcade Tournament")
print("-----------------")
print()
print("Enter the scores:")
print()
    
# Loop 5 times - Data in
for index in range(5):

    # Get valid score
    score = int(input("  Player " + str(index + 1) + ": "))
    
    # Validate score
    while score < 0 or score > 200:
        
        # Error message
        print()
        print("  Score must be between 0 and 200.")
        
        # Get valid score
        score = int(input("  Player " + str(index + 1) + ": "))
    
    # Store score
    scores[index] = score

# Display sub-heading
print()
print("-----------------")
print()
print("Tournament Results")
print("------------------")
print()

# Loop 5 times - Data out
for index in range(5):
    
    print("Player " + str(index + 1) + " scored " + str(scores[index]) + " points")

# Display sub-heading
print()
print("------------------")
print()
print("Individual Result")
print("-----------------")
print()

# Get valid player number
player = int(input("Enter a player's number: "))

# Validate player number
while player < 1 or player > 5:
    
    # Error message
    print()
    print("Player's number must be between 1 and 5.")
    
    # Get valid player number
    player = int(input("Enter a player's number: "))

# Display selected player's number
print()
print("Player " + str(player) + " scored " + str(scores[player - 1]) + " points")

# Display footer
print()
print("=================")
