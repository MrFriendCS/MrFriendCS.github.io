# Title: Straight line
# Author: Mr Friend
# Date: 27 Nov 2020

def getCoord(point):
    # Define local variables
    xcoord = 0
    ycoord = 0

    # Define local array
    coord = [0.0] * 2

    xcoord = float(input("Enter a value for x" + str(point) + ": "))
    ycoord = float(input("Enter a value for y" + str(point) + ": "))

    print() # blank line

    coord = [xcoord, ycoord]

    return(coord)

def calcGradient(point1, point2):
    # Declare local variables
    x1 = 0.0
    y1 = 0.0
    x2 = 0.0
    y2 = 0.0
    m = 0.0

    # Get values
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]

    # Calculate the gradient
    m = (y2 - y1) / (x2 - x1)

    return m

def calcMidpoint(point1, point2):
    # Declare local variables
    x1 = 0.0
    y1 = 0.0
    x2 = 0.0
    y2 = 0.0
    xMid = 0.0
    yMid = 0.0

    # Declare local array
    coord = [0.0] * 2

    # Get values
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]

    # Calculate the midpoint
    xMid = (x1 + x2) / 2
    yMid = (y1 + y2) / 2
    coord = [xMid, yMid]

    return coord

def calcDistance(point1, point2):
    # Declare local variables
    x1 = 0.0
    y1 = 0.0
    x2 = 0.0
    y2 = 0.0
    xDist = 0.0
    yDist = 0.0
    dist = 0.0

    # Get values
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]

    # Calculate distance
    xDist = x1 - x2
    yDist = y1 - y2

    dist = (xDist**2 + yDist**2)**0.5

    return dist


# Main program

# Declare global variables
gradient = 0.0
distance = 0.0

# Declare global arrays
coord1 = [0.0] * 2
coord2 = [0.0] * 2
midpoint = [0.0] * 2

# Get coordinates
coord1 = getCoord(1)
coord2 = getCoord(2)

# Calculate gradient
gradient = calcGradient(coord1, coord2)

# Calculate midpoint
midpoint = calcMidpoint(coord1, coord2)

# Calculate distance
distance = calcDistance(coord1, coord2)

# Display results
print("Coordinate 1: " + str(coord1))
print("Coordinate 2: " + str(coord2))

print("\nMidpoint: " + str(midpoint))

print("\nThe gradient is " + str(gradient))

print("\nThe distance between the coordinates is " + str(distance))
