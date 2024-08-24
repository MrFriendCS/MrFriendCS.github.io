# Title: N5 CS Specimen Task 1C
# Author: Mr Friend
# Date: 5 Sep 2023

# Declare variables
word = ""
length = 0
average = 0.0
noOfWords = 0
totalLetters = 0

# Declare array
words = [""] * 20

# Get sentance length
noOfWords = int(input("How many words? "))

# Ensure valid number of words
while noOfWords < 1 or noOfWords > 20:
    print("Enter a number from 1 to 20")
    noOfWords = int(input("How many words? "))

# Loop for each word
for index in range(noOfWords):
    
    # Get and store next word
    word = input("Enter a word: ")
    words[index] = word
    
    # Calculate length of word
    length = len(word)
    
    # Add length of word on to total
    totalLetters = totalLetters + length

# Calculate average
average = totalLetters / noOfWords

# Loop for each word
for index in range(noOfWords):
    # Display next word on a new line
    print(words[index])

# Display average
print("The average word length is: " + str(average))

# Display message about average length
if average < 5:
    print("Short words - suitable for junior readers")
elif average >= 5 and average <= 7:
    print("Medium words - suitable for teen readers")
else:
    print("Long words - suitable for senior readers")
