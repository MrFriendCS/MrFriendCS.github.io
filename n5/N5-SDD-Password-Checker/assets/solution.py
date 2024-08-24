# Title: N5 SDD Password Checker
# Author: Mr Friend
# Date: 10 Oct 2023

# Declare variables
toCheck = 0
part1 = ""
part2 = ""
part3 = 0
part4 = ""
valid1 = False
valid2 = False
valid2 = False
valid4 = False
result = ""
password = ""
results = [""] * 5
passwords = [""] * 5

# Get valid number of passwords to check
while toCheck < 1 or toCheck > 5:
    # Get number
    toCheck = int(input("How many passwords to check? "))

    # Check if valid
    if toCheck < 1 or toCheck > 5:
        # Error message
        print("Value must be from 1 to 5.")

# Loop for each password
for index in range(toCheck):

    # Get Part 1
    part1 = input("\nPart 1: ")
    
    # Check Part 1 validity
    if part1 >= "A" and part1 <= "Z" and len(part1) == 1:
        valid1 = True
    else:
        valid1 = False
    
    # Get Part 2
    part2 = input("Part 2: ")
    
    # Check Part 2 validity
    if len(part2) == 6:
        valid2 = True
    else:
        valid2 = False
    
    # Get Part 3
    part3 = int(input("Part 3: "))
    
    # Check Part 3 validity
    if part3 >= 10 and part3 <= 99:
        valid3 = True
    else:
        valid3 = False
    
    # Get Part 4
    part4 = input("Part 4: ")
    
    # Check Part 4 validity
    if part4 == "!" or part4 == "?" or part4 == "$":
        valid4 = True
    else:
        valid4 = False

    # Check password validity
    if valid1 and valid2 and valid3 and valid4:
        # True
        result = "Valid"

    else:
        # False
        result = "Invalid:"

        # Part 1
        if not valid1:
            result = result + " Capital"

        # Part 2
        if not valid2:
            result = result + " Length"

        # Part 3
        if not valid3:
            result = result + " Number"

        # Part 4
        if not valid4:
            result = result + " Special"

    # Store result
    results[index] = result
    
    # Combine password parts
    password = part1 + part2 + str(part3) + part4

    # Store password
    passwords[index] = password

# Display passwords
print("\nPasswords")
print("---------")

# Loop for each password
for index in range(toCheck):
    print(str(index + 1) + ". " + passwords[index])

# Display results
print("\nResults")
print("-------")

# Loop for each result
for index in range(toCheck):
    print(str(index + 1) + ". " + results[index])
