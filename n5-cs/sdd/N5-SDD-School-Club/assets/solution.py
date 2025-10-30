# Title: N5 SDD School Club
# Author: Mr Friend
# Date: 30 Oct 2025

# Initialise variables
age = 0
parentPermission = ""
teacherPermission = ""

# Header
print("Castlebay eSports Club")
print("Eligibility Checker")
print("----------------------")
print()

# Get age
age = int(input("How old are you? ")) 

# Permission options
if age >= 13:
    
    # Get parental permission
    parentPermission = input("Do you have parental permission? ")
    
elif age == 12:
    
    # Get teacher permission
    teacherPermission = input("Do you have teacher permission? ")
    

if (age >= 13 and parentPermission == "yes") or (age == 12 and teacherPermission == "yes"):
    
    # Welcome to the club
    print()
    print("You can join the eSports club!")
    
else:
    
    # Not yet
    print()
    print("You can't join the club just now.")

# Footer
print()
print("======================")
