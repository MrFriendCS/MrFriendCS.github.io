# Title: N5-SDD-Rounding Part 2
# Author: Mr Friend
# Date: 24 Aug 2025

# Initialise variables
pi = 3.1415
radius = 5
diameter = 0.0
circumference = 0.0
area = 0.0

# Calculations
diameter = 2 * radius
circumference = pi * diameter
area = pi * radius**2

# Round values
diameter = round(diameter, 2)
circumference = round(circumference, 2)
area = round(area, 2)

# Display results
print("Given a radius of " + str(radius) + " units.")
print()

print("The diameter is " + str(diameter) + " units.")
print()

print("The circumference is " + str(circumference) + " units.")
print()

print("The area is " + str(area) + " units squared.")
