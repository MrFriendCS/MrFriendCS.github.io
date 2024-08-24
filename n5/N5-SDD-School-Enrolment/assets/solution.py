# Title: S3 SDD School Enrolment
# Date: 16 Sep 2023
# Author: Mr Friend

# Declare variable
age = 0

# Get age from user
age = int(input("Age: "))

# Only accept ages 3 to 18
while age < 3 or age > 18:
    print("Age must be from 3 to 18")
    age = int(input("Re-enter age: "))

# Pre-school: 3, 4
if age < 5:
    print("Pre-school")

# Primary: 5 to 11
elif age < 12:
    print("Primary")

# Secondary: 12 to 18
else:
    print("Secondary")
