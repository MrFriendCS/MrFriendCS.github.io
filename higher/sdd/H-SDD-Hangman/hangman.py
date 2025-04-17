# Title: Hangman
# Author: Mr Friend
# Date: 16 Apr 2025

word = "hangman"
correct = "_" * len(word)
letter = ""
left = ""
right = ""
incorrect = ""
lives = 7
found = False

# Loop until all lives lost or correct
while lives > 0 and word != correct:
    
    # Get a letter
    letter = input("Letter: ")
    
    while len(letter) != 1:
        # Error message
        print("A single letter is required.")
        
        # Get a letter
        letter = input("Letter: ")
    
    # Check word for letter
    
    # Reset found
    found = False
    
    # Loop for each character in word
    for index in range(len(word)):
        
        # Compare current character to letter
        if word[index] == letter:
            
            found = True
            
            # Left
            left = correct[ :index]
            right = correct[index+1: ]
            
            # Combine
            correct = left + letter + right
            
    if not found:
        # Reduce number of lives
        lives = lives - 1
        
        # Add letter to list of incorrect
        incorrect = incorrect + letter

    print("\nLives: " + str(lives))
    print("Correct: " + correct)
    print("Incorrect: " + incorrect + "\n")
    
if lives > 0:
    print("\nSaved!")

else:
    print("Oh dear!")