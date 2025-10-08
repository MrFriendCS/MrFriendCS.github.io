# Title: N5 SDD Word Length
# Author: Mr Friend
# Date: 8 Oct 2025

# Initialise Variables
word = ""
wordLength = 0


# Display header
print("Word Length")
print("-----------")


# Get word from user
print()
word = input("Enter a word: ")

# Calculate word length
wordLength = len(word)

# Display word length
print()
print("Letters: " + str(wordLength))

# 0 Letters in word?
if wordLength == 0:
    
    # Display nothing entered message
    print()
    print("Nothing entered!") 

# Less than 5 letters in word?
elif wordLength < 5:
    
    # Display short word message
    print()
    print("'" + word + "' is a short word.")

# Less than 10 letters in word?
elif wordLength < 10:
    
    # Display medium word message
    print()
    print("'" + word + "' is a medium word.")

else:
    
    # Display medium word message
    print()
    print("'" + word + "' is a long word.")


# Display footer
print()
print("===========")
