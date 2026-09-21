# Title: Boccia
# Author: Mr Friend
# Date: 21 Sep 2026

# Initilise variables
winner: str = ""
score: int = 0
redScore: int = 0
blueScore: int = 0

# Heading
print("Paris Paralympics")
print("Individual Boccia")
print("-----------------")

# Loop for four ends
for end in range(4):
    
    # Get end winner
    winner = input("\nEnd " + str(end+1) + " winner: ")
    
    # Only accept red, blue, draw
    while winner != "red" and winner != "blue" and winner != "draw":
        
        # Error message
        print("\nWinner must be red, blue, or draw")
        
        # Get end winner
        winner = input("End " + str(end+1) + " winner: ")
        
    # Get points
    if winner != "draw":
        
        # Get points
        score = int(input("End " + str(end+1) + " points: "))
        
        # Only accept 1 to 6
        while score < 1 or score > 6:
            
            # Error message
            print("\nPoints must be 1 to 6")
            
            # Get points
            score = int(input("End " + str(end+1) + " points: "))
        
        # Add score
        if winner == "red":
            
            redScore = redScore + score
            
        else:
            
            blueScore = blueScore + score
    
    # Draw
    else:
        
        # Draw: one point each
        redScore = redScore + 1
        blueScore = blueScore + 1

# Text
print("\n=================\n")

print("Result")
print("------\n") 

# Scores
print("Red:  " + str(redScore))
print("Blue: " + str(blueScore) + "\n")

# Decide winner
if redScore > blueScore:
    
    print("Red wins!")
    print("=========")
    
elif blueScore > redScore:
    print("Blue wins!")
    print("==========")
    
else:
    
    print("Draw after four Ends")
    print("Now tie-break Ends until one team wins!")
        