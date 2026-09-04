# Title: N5 SDD Rectangle Calculations
# Author: Mr Friend
# Date: 31 Aug 2024

# Initialise variables
width: int = 0
height: int = 0
perimeter: int = 0
area: int = 0

# Display header
print("Rectangle Calculations")
print("----------------------")
print()

# Display diagram

print("   width")
print("  -------")
print(" h|     |")
print(" e|     |")
print(" i|     |")
print(" g|     |")
print(" h|     |")
print(" t|     |")
print("  -------")
print()

# Inputs - Whole numbers only
width = int(input("What is the width? "))
height = int(input("What is the height? "))

# Processes
perimeter = 2 * (width + height)
area = width * height

# Outputs
print()
print("The perimeter is " + str(perimeter) + " units")
print("The area is " + str(area) + " units squared")
