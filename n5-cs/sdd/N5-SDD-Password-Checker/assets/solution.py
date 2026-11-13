# Title: N5 SDD Password Checker
# Author: Mr Friend
# Date: 12 Nov 2026

# Declare variables
part1: str = ""
part2: str = ""
part3: int = 0
part4: str = ""
result: str = ""
password: str = ""

# Display header
print("Password Checker")
print("----------------")

# Get Part 1
part1 = input("\nPart 1: ")

# Check Part 1 validity
if not (part1 >= "A" and part1 <= "Z" and len(part1) == 1):
    
    result = result + "Capital "

# Get Part 2
part2 = input("Part 2: ")

# Check Part 2 validity
if len(part2) != 6:
    
    result = result + "Length "

# Get Part 3
part3 = int(input("Part 3: "))

# Check Part 3 validity
if not (part3 >= 10 and part3 <= 99):
    
    result = result + "Number "

# Get Part 4
part4 = input("Part 4: ")

# Check Part 4 validity
if not (part4 == "!" or part4 == "?" or part4 == "$"):
    
    result = result + "Special"

# Combine password parts
password = part1 + part2 + str(part3) + part4

# Check validity
if result == "":
    
    result = "Valid"
    
else:
    
    result = "Invalid - " + result

# Display password
print()
print("Password:. " + password)

# Display validity
print()
print("Validity: " + result)

# Display footer
print()
print("================")
