# Title: N5 SDD School Enrolment
# Date: 18 Dec 2025
# Author: Mr Friend

# Declare variable
age = 0

# Display header
print("School Enrolment")
print("----------------")
print()

# Get age from user
age = int(input("Age: "))

# Only accept ages 3 to 18
while age < 3 or age > 18:
    
    # Error message
    print()
    print("Age must be from 3 to 18")
    
    # Get age from user
    age = int(input("Re-enter age: "))

# Pre-school: 3, 4
if age < 5:
    
    # Display school
    print("Pre-school")

# Primary: 5 to 11
elif age < 12:
    
    # Display school
    print("Primary")

# Secondary: 12 to 18
else:
    
    # Display school
    print("Secondary")

# Display footer
print()
print("================")
