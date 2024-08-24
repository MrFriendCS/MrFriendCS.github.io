# Title: Various functions
# Author: Mr Friend
# Date: 18 Nov 2020

# Do not change this program!

from functions import *

# Calculate the area of a square
length = 5

answer = areaSquare(length)

print("The area of the square is " + str(answer) + " units squared")


# Calculate the area of a rectangle
length = 5
breadth = 4

answer = areaRectangle(length, breadth)

print("\nThe area of the rectangle is " + str(answer) + " units squared")


# Calculate the area of a triangle
base = 5
height = 4

answer = areaTriangle(base, height)

print("\nThe area of the triangle is " + str(answer) + " units squared")


# Calculate the area of a circle
radius = 5

answer = areaCircle(radius)

print("\nThe area of the circle is " + str(answer) + " units squared")


# Calculate the volume of a cube
length = 5

answer = volCube(length)

print("\nThe volume of the cube is " + str(answer) + " units cubed")


# Calculate the volume of a cuboid
length = 2
breadth = 3
height = 4

answer = volCuboid(length,breadth,height)

print("\nThe volume of the cuboid is " + str(answer) + " units cubed")


# Calculate the volume of a cylinder
radius = 3
height = 4

answer = volCylinder(radius, height)

print("\nThe volume of the cylinder is " + str(answer) + " units cubed")


# Find the index of the @ symbol
text = "bill@microsoft.com"

answer = findAt(text)

print("\nThe index of the @ symbol is " + str(answer))


# Is character in the text?
text = "bill@microsoft.com"
character = "."

answer = findChar(text, character)

print("\nCharacter found: " + str(answer))