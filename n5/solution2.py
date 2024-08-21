# Title: N5 SDD Tasks
# Author: Mr Friend
# Date: 4 Aug 2024

#
# Task 1
#

# Initilise variables
value = 0
root = 0.0

# Get value from user
while value <= 0:
    value = float(input("Enter a value: "))
    
    # Check value
    if value <= 0:
        print("Value must be greater than zero.\n")

# Calculate sqaure result
root = value ** 0.5

# Display result
if root == round(root):
    print("The square root is: " + str(round(root)))
else:
    print("The square root is: " + str(round(root, 3)))


#
# Task 2
#

# Import module
import random

# Initilise variables
numbers = 0
maximum = 0
value = 0
sumText = ""
sumTotal = 0
answer = 0

# Get number of numbers from user
while numbers < 2 or numbers > 5:
    numbers = int(input("How many numbers: "))
    
    # Check value
    if numbers < 2 or numbers > 5:
        print("Value must be between 2 and 5.\n")

# Get maximum value from user
while maximum <= 0:
    maximum = int(input("Largest number: "))
    
    # Check value
    if maximum <= 0:
        print("Value must be greater than 0.\n")

# Create problem
for counter in range(numbers):
    
    # Generate value to add
    value = random.randint(1, maximum)
    
    # Add value to text
    sumText = sumText + "  " + str(value)
    
    # Add value to total
    sumTotal = sumTotal + value

# Display problem
print("\nAdd the following numbers together:")
print(sumText)

# Get value from user
answer = int(input("\nWhat is the sum? "))

# Display result
if answer == sumTotal:
    print("\nCorrect!")
else:
    print("\nWrong.  It's " + str(sumTotal) + "!")


#
# Task 3
#

# Initilise variables
answer = ""
pupil = False
area = ""
time = ""

# Ask if user is a puil
answer = input("Are you a pupil at Castlebay School? ")

if answer == "yes" or answer == "Yes":
    pupil = True
else:
    print("\nPhone 810100, Mon-Fri, after 9.30 am.")


if pupil:
    while area != "Nursery" and area != "Primary" and area != "Secondary":
        area = input("\nWhere are you a pupil? ")
        
        if area != "Nursery" and area != "Primary" and area != "Secondary":
            print("Choice must be Nursery, Primary, or Secondary.")
    
    # Decide start time
    if area == "Nursery":
        time = "8.30"
    elif area == "Primary":
        time = "8.55"
    else:
        time = "8.50"
    
    # Display message
    print("\nYour learning fun starts at " + time + " am.")


#
# Task 4
#

import random

# Initilise variables
determiner = ["A", "My", "The"]
adjective = ["blue", "big", "rainbow"]
noun = ["wind", "seagull", "dog"]
verb = ["slept", "ate", "ran"]
adverb = ["playfully", "slowly", "happily"]

ranDet = 0
ranAdj = 0
ranNou = 0
ranVer = 0
ranAdv = 0

# Pick random words
ranDet = random.randint(0, len(determiner)-1)
ranAdj = random.randint(0, len(adjective)-1)
ranNou = random.randint(0, len(noun)-1)
ranVer = random.randint(0, len(verb)-1)
ranAdv = random.randint(0, len(adverb)-1)

# Create a line of poetry
print(determiner[ranDet] + " " + adjective[ranAdj] + " " + noun[ranNou] + " " + verb[ranVer] + " " + adverb[ranAdv])
    
