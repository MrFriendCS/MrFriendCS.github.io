# Title: N5 SDD Summer 1 Part 1
# Author: Mr Friend
# Date: 24 Jun 2026

# Initilise variables
length: float = 0.0
breadth: float = 0.0
perimeter: float = 0.0
area: float = 0.0

# Set values
length = 2.25
breadth = 7.25

# Calculations
perimeter = 2 * (length + breadth)
area = length * breadth

# Round values
perimeter = round(perimeter, 2)
area = round(area, 2)

# Display eader
print("Rectangle Fun")
print("-------------")
print()

# Display values
print("Length:")
print(length)
print()
print("Breadth")
print(breadth)
print()

# Display perimeter
print("Perimeter:")
print(perimeter)
print("units")
print()

# Display area
print("Area:")
print(area)
print("square units")
print()

# Display footer
print("=============")
