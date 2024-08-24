# Title: Frequency analysis
# Author: Mr Friend
# Date: 31 Jan 2020

# Declare variables
text = ""
char = 0

# Declare array
letters = [0] * 26

# Get text to analyse
text = str(input("Type of paste some text: "))

for letter in text:
    char = ord(letter)

    # Make all values uppercase, c to C
    if char > 90:
        char = char - 32
    
    # Reduce value so A = 0
    char = char - 65

    # Log only values for A to Z
    if char >= 0 and char <= 25:
        letters [char] = letters [char] + 1

print("\nFrequency Analysis Results\n")

char = 65 # Start at A

for letter in letters:
    print(chr(char) + " - " + str(letter))
    char = char + 1