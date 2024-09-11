# Title: N5 SDD Cat Food
# Author: Mr Friend
# Date: 11 Sep 2024

# Initialise variables
age = 0
food = ""

# Get the cat's age from the user
age = int(input("How old is the cat? "))

# Only accept valid ages
while age < 0 or age > 25:

    # Display an error message
    print("\nEnter an age of 0 - 25")
    
    # Get the cat's age from the user
    age = int(input("How old is the cat? "))

# Decide the type of cat food
if age == 0:
    food = "kitten"
elif age < 7:
    food = "adult cat"
else:
    food = "senior cat"

# Display cat age
print("\nYour cat is " + str(age) + " years old.")

# Display cat food type
print("Feed it " + food + " food.")