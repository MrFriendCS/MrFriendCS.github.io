# Title: N5-SDD-Rounding
# Author: Mr Friend
# Date: 21 Aug 2025

# Initialise variables
pi: float = 3.1415
radius: int = 5
diameter: int = 0
circumference: float = 0.0
area: float = 0.0

# Calculations
diameter = 2 * radius
circumference = pi * diameter
area = pi * radius**2

# Round values
diameter = round(diameter, 2)
circumference = round(circumference, 2)
area = round(area, 2)

# Display header
print("Circles Fun")
print("-----------")

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
print(area)
print("units squared")

# Display footer
print("===========")