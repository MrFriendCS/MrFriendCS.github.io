# Title: H SDD House Prices
# Author: Mr Friend
# Date: 12 Oct 2023

#
# Subprograms
#

def newPrice(value, percent):
    """Change a value by a percentage.  Round to 0 dp."""

    # Calculate new value
    newValue = round(value * (1 + percent/100))

    # Return new value
    return newValue

def updatePostcode(postcode):
    """Change first 3 digits of postcode to HS1."""

    # Create new postcode
    newPostcode = "HS1 " + postcode[-3: ]

    # Return new postcode
    return newPostcode

def readData():
    """Read data from file into parallel arrays."""

    # Declare local variables
    line = ""
    data = [""] * 2
    postcodes = [""] * 1000
    origValues = [0] * 1000

    # Make connection to file
    file = open("housePrices.csv", "r")

    # For each line of data    
    for index in range(len(postcodes)):

        # Read next line from file
        line = file.readline()

        # Split data at commas
        data = line.split(",")
        
        # Assign values to parrallel arrays
        postcodes[index]  = data[0].strip()
        origValues[index] = int(data[1].strip())

    # close the connection to the file
    file.close()

    # Return data
    return postcodes, origValues

def countHS0(postcodes):
    """Find and count all HS0 postcodes.  Write results to file."""

    # Declare local variables
    count = 0

    # Loop for each postcode
    for index in range(len(postcodes)):

        # Check postcode
        if postcodes[index][0:3] == "HS0":
            # Increment count
            count = count + 1

    # Make connection to file
    file = open("errorPostcodes.txt", "w")

    # Write result to file
    file.write("There were ")
    file.write(str(count))
    file.write(" incorrect postcodes.\n\n")

    file.write("Errors\n")
    file.write("------\n")

    # Loop for each postcode
    for index in range(len(postcodes)):

        # Check postcode
        if postcodes[index][0:3] == "HS0":
            # Write to file
            file.write(postcodes[index] + "\n")

    # Close connection to file
    file.close()

def updatePostcodes(postcodes):
    """Find and change all HS0 postcodes to HS1."""

    # Loop for each postcode
    for index in range(len(postcodes)):
        
        # Check postcode
        if postcodes[index][0:3] == "HS0":
            
            # Update postcode
            postcodes[index] = updatePostcode(postcodes[index])

    # Return postcodes
    return postcodes

def newPrices(postcodes, origValues):
    """Updates house prices depending on postcodes."""

    # Declare local variables
    newValues = [0] * len(origValues)
    digit = 0

    # Loop for each property
    for index in range(len(postcodes)):
            
        # Get digit postcode
        digit = int(postcodes[index][2])

        # Set percentage change
        if digit < 6:
            newValues[index] = newPrice(origValues[index], -2)
        elif digit < 9:
            newValues[index] = newPrice(origValues[index], 2)
        elif digit == 9:
            newValues[index] = newPrice(origValues[index], 5)

    # Return new house prices
    return newValues

def writeData(postcodes, origValues, newValues):
    """Write postcodes, old prices, and new prices to file."""

    # Make a connection to the file
    file = open("newPrices.csv", "w")

    # Loop for each house
    for index in range(len(postcodes)):

        # Write a line of data
        file.write(postcodes[index] + ",")
        file.write(str(origValues[index]) + ",")
        file.write(str(newValues[index]) + "\n")

def findMinMax(newValues):
    """Find lowest and highest house prices."""

    # Declare local variables
    lowest = 0
    highest = 0

    # Assign first value as lowest
    lowest = newValues[0]
    
    # Loop for remaining house prices
    for index in range(1, len(newValues)):

        # Check value
        if newValues[index] < lowest:
            # Update lowest
            lowest = newValues[index]

    # Assign first value as highest
    highest = newValues[0]
    
    # Loop for remaining house prices
    for index in range(1, len(newValues)):

        # Check value
        if newValues[index] > highest:
            # Update highest
            highest = newValues[index]

    # Return lowest and highest house prices
    return lowest, highest

def findExtremes(postcodes, newValues, lowest, highest):
    """find the most expensive 2% and least expensive 2% of properties.  Write results to file."""

    # Declare local variables
    priceRange = 0
    twoPercent = 0.0
    topTwo = 0.0
    bottomTwo = 0.0

    # Calculate range of values
    priceRange = highest - lowest

    # Calculate 2% of range
    twoPercent = priceRange * 0.02

    # Calculate highest 2% value
    topTwo = highest - twoPercent

    # Calculate lowest 2% value
    bottomTwo = lowest + twoPercent

    # Make a connection to the file
    file = open("extremes.txt", "w")
    
    # Write results to file
    file.write("The most expensive house cost ")
    file.write("£" + str(highest) + ".\n")
    file.write("The least expensive house cost ")
    file.write("£" + str(lowest) + ".\n\n")

    file.write("The top 2% of properties are:\n\n")
    
    # Loop for each property - top 2 percent
    for index in range(len(postcodes)):

        # Check value
        if newValues[index] >= topTwo:

            # Write a line of data
            file.write(postcodes[index] + ",")
            file.write(str(newValues[index]) + "\n")

    file.write("\nThe bottom 2% of properties are:\n\n")

    # Loop for each property - top 2 %
    for index in range(len(postcodes)):

        # Check value
        if newValues[index] <= bottomTwo:

            # Write a line of data
            file.write(postcodes[index] + ",")
            file.write(str(newValues[index]) + "\n")

    # Close connection to file
    file.close()

#
# Main Program
#

# Declare global variables
postcodes = [""] * 1000
origValues = [0] * 1000
newValues = [0] * 1000
lowest = 0
highest = 0

# 1. Read in the postcodes and current house prices
postcodes, origValues = readData()

# 2. Find and count all HS0 postcodes
countHS0(postcodes)

# 3. Amend all HS0 postcodes to HS1
postcodes = updatePostcodes(postcodes)

# 4. Calculate the new house prices
newValues = newPrices(postcodes, origValues)

# 5. Write postcodes, old prices, and new prices to file
writeData(postcodes, origValues, newValues)

# 6. Find the lowest and highest house prices.
lowest, highest = findMinMax(newValues)

# 7. Find and write highest 2% and lowest 2% of properties
findExtremes(postcodes, newValues, lowest, highest)
