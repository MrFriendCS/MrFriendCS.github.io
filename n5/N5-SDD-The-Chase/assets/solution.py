# Title: N5 SDD The Chase
# Author: Mr Friend
# Date: 18 Sep 2023

# Declare variables
score = 0
answer = ""

# Get answer to question 1
answer = input("What animal says 'meow'? ")

# Is answer 1 correct?
if answer == "cat":
    # Yes
    
    # Add 1 to score
    score = score + 1

    # Display correct
    print("Correct!")

else:
    # No
    
    # Display correct answer
    print("Wrong.  It's a cat!")

# Get answer to question 2
answer = input("\nWhat animal says 'woof'? ")

# Is answer 2 correct?
if answer == "dog":
    # Yes
    
    # Add 1 to score
    score = score + 1

    # Display correct
    print("Correct!")

else:
    # No
    
    # Display correct answer
    print("Wrong.  It's a dog!")

# Get answer to question 1
answer = input("\nWhat animal says 'oink'? ")

# Is answer 3 correct?
if answer == "pig":
    # Yes
    
    # Add 1 to score
    score = score + 1

    # Display correct
    print("Correct!")

else:
    # No
    
    # Display correct answer
    print("Wrong.  It's a pig!")

# Is score equal to 3?
if score == 3:
    # Yes
    # Display Genius!
    print("\nGenius!")

else:
    # No

    # Is score equal to 0?
    if score == 0:
        # Yes
        
        # Display Oh dear!
        print("\nOh dear!")

    else:
        # No
        
        # Display Good effort!
        print("\nGood effort!")
