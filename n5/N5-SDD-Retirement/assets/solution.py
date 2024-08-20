# Title: N5 SDD Retirement
# Author: Mr Friend
# Date: 22 Aug 2023

# Declare variables
name = ""
age = 0
yearsLeft = 0

# Get user name
name = input("What is your name? ")

# Get user age
age = int(input("\nHow old are you " + name + "? "))

# Is age valid?
while age < 0:
    print("\nAge must be 0 or more.")
    age = int(input("\nHow old are you " + name + "? "))

# Calculate years to retirement
yearsLeft = 68 - age

# Display a blank line
print()

# Display years left
if yearsLeft > 1:
    print(name + ", you will be eligible for your pension in " + str(yearsLeft) + " years.")
    
elif yearsLeft == 1:
    print(name + ", you will be eligible for your pension next year.")
    
else:
    print(name + ", you've got your pension!")
