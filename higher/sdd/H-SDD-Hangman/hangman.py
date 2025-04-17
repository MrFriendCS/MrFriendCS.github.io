# Title: Hangman
# Author: Mr Friend
# Date: 16 Apr 2025

# Get extra code
import random

# Intialise variables
words = []
word = ""
correct = ""
letter = ""
left = ""
right = ""
incorrect = ""
lives = 7
found = False

# Read in word list

# Make connection to file
file = open("wordlist.txt", "r")

# Read first word
line = file.readline().strip()

# Repeat for each word in wordlist
while line != "":
    
    # Add to to wordlist
    words = words + [line]
    
    # Read next line
    line = file.readline().strip()

# Close connection to file
file.close()


# Pick a random word
word = words[random.randint(0, len(words)-1)]

# Make blank word
correct = "_" * len(word)


print("Word: " + correct + "?")

# Loop until all lives lost or correct
while lives > 0 and word != correct:
    
    # Get a letter
    letter = input("\nLetter? ")
    
    while len(letter) != 1:
        # Error message
        print("\nA single letter is required.")
        
        # Get a letter
        letter = input("Letter? ")
    
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
    print("Incorrect: " + incorrect)
    
if lives > 0:
    print("\nSaved!")

else:
    print("\nOh dear!  It was " + word + ".")