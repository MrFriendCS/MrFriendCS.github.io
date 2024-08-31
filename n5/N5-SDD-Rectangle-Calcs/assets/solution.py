# Title: N5 SDD Rectangle Calculations
# Author: Mr Friend
# Date: 31 Aug 2024

# Display header
print("Rectangle Calculations")
print("----------------------")
print()

# Inputs - Whole numbers only
width = int(input("What is the width? "))
height = int(input("What is the height? "))

# Processes
perimeter = 2 * (width + height)
area = width * height

# Outputs
print()
print("The perimeter is " + str(perimeter) +" units")
print("The area is " + str(area) + " units squared")
