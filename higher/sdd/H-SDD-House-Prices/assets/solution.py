# Title: H-SDD-House-Prices
# Author: Mr Friend
# Date: 5 Oct 2024


def readData():
    """Read data from file into parallel arrays."""

    # Initialise local variables
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
    """Count all HS0 postcodes."""

    # Initialise local variables
    count = 0

    # Loop for each postcode
    for index in range(len(postcodes)):

        # Check postcode
        if postcodes[index][0:3] == "HS0":
            
            # Increment count
            count = count + 1

    return count


def fixHS0(postcodes):
    """Find and change all HS0 postcodes to HS1."""

    # Loop for each postcode
    for index in range(len(postcodes)):
        
        # Check postcode
        if postcodes[index][0:3] == "HS0":
            
            # Update postcode
            postcodes[index] = "HS1 " + postcodes[index][3: ]

    # Return postcodes
    return postcodes


def newPrices(postcodes, origValues):
    """Updates house prices depending on postcodes."""

    # Initialise local variables
    newValues = [0] * len(origValues)
    currentValue = 0
    newValue = 0
    digit = 0
    percent = 0

    # Loop for each property
    for index in range(len(postcodes)):
            
        # Get digit postcode
        digit = int(postcodes[index][2])

        # Set percentage change
        if digit < 6:
            # 2% less
            percent = -2
            
        elif digit < 9:
            # 2% more
            percent = 2
            
        elif digit == 9:
            # 5% more
            percent = 5
        
        # Get current value
        currentValue = origValues[index]
        
        # Calculate new price.  Round to 0 dp.
        newValue = round(currentValue * (1 + percent/100))
            
        # Update price
        newValues[index] = newValue

    # Return new house prices
    return newValues


def findLowest(newValues):
    """Find lowest house price."""

    # Initialise local variables
    lowest = 0

    # Assign first value as lowest
    lowest = newValues[0]
    
    # Loop for remaining house prices
    for index in range(1, len(newValues)):

        # Check value
        if newValues[index] < lowest:
            # Update lowest
            lowest = newValues[index]

    return lowest


def findHighest(newValues):
    """Find highest house price."""

    # Initialise local variables
    highest = 0

    # Assign first value as highest
    highest = newValues[0]
    
    # Loop for remaining house prices
    for index in range(1, len(newValues)):

        # Check value
        if newValues[index] > highest:
            # Update highest
            highest = newValues[index]

    return highest


def countValues(newValues, target):
    """Count house prices that match the target"""
    
    # Initialise local variable
    count = 0

    # Loop for each house price
    for index in range(len(newValues)):

        # Check postcode
        if newValues[index] == target:
            
            # Increment count
            count = count + 1

    return count


def writeSummary(badCodes, lowest, highest, lowCount, highCount, postcodes, newValues):
    """Write summary information to file."""

    # Initialise local variables

    # Make a connection to the file
    file = open("summary.txt", "w")
    
    # Header
    file.write("Summary\n")
    file.write("-------\n\n")
    
    # HS0 errors
    file.write("HS0 errors: " + str(badCodes) + "\n\n")
    
    # Highest and lowest prices
    file.write("Lowest value:  £" + str(lowest) + "\n")
    file.write("Highest value: £" + str(highest) + "\n\n")
    
    # Lowest count
    file.write("Lowest value houses: " + str(lowCount) + "\n")
    
    # Loop for each house price
    for index in range(len(postcodes)):
        
        # Check
        if newValues[index] == lowest:
            
            # Write postcode to file
            file.write("\t" + postcodes[index] + "\n")
    
    # Highest count
    file.write("\nHighest value houses: " + str(highCount) + "\n")
    
    # Loop for each house price
    for index in range(len(postcodes)):
        
        # Check
        if newValues[index] == highest:
            
            # Write postcode to file
            file.write("\t" + postcodes[index] + "\n")
    
    # Footer
    file.write("\n=======\n")
    
    # Close connection to file
    file.close()


def writeData(postcodes, origValues, newValues):
    """Write data to file."""

    # Make a connection to the file
    file = open("updatedPrices.csv", "w")

    # Loop for each house
    for index in range(len(postcodes)):

        # Write a line of data
        file.write(postcodes[index] + ",")
        file.write(str(origValues[index]) + ",")
        file.write(str(newValues[index]) + "\n")

    # Close connection to file
    file.close()


def main():
    """Main program."""

    # Initialise variables
    badCodes = 0
    postcodes = [""] * 1000
    origValues = [0] * 1000
    newValues = [0] * 1000
    lowest = 0
    highest = 0
    lowCount = 0
    highCount = 0

    # 1. Read values from file
    postcodes, origValues = readData()

    # 2. Count HS0 postcodes
    badCodes = countHS0(postcodes)

    # 3. Correct HS0 postcodes
    postcodes = fixHS0(postcodes)

    # 4. Calculate new house prices
    newValues = newPrices(postcodes, origValues)

    # 5. Find the lowest house price
    lowest = findLowest(newValues)

    # 6. Find the highest house price
    highest = findHighest(newValues)

    # 7. Count houses with lowest price
    lowCount = countValues(newValues, lowest)

    # 8. Count houses with highest price
    highCount = countValues(newValues, highest)

    # 9. Write summary information to file
    writeSummary(badCodes, lowest, highest, lowCount, highCount, postcodes, newValues)

    # 10. Write data to file
    writeData(postcodes, origValues, newValues)


# Call main()
main()
