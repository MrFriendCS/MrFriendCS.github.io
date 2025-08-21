# Title: N5-SDD-Rounding
# Author: Mr Friend
# Date: 21 Aug 2025

# Initialise variables
pi = 3.1415
diameter = 0.0
circumference = 0.0
area = 0.0
radius = 5

# Calculations
diameter = 2 * radius
circumference = pi * diameter
area = pi * radius**2

# Round values
diameter = round(diameter, 2)
circumference = round(circumference, 2)
area = round(area, 2)

# Display results
print("Given a radius of")
print(radius)
print("units")
print()

print("The diameter is")
print(diameter)
print("units")
print()

print("The circumference is")
print(circumference)
print("units")
print()

print("The area is")
print("78.73")
print("units squared")
