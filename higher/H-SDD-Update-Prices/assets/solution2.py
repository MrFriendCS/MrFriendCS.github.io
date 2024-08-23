# Title: H SDD Update Prices
# Author: Mr Friend
# Date 22 Aug 2024

#
# Subprograms
#

def getData():
    """Return parallel arrays from costs.csv"""

    # Declare local variable and arrays
    line = ""
    
    subNames = [""] * 7
    subWeights = [""] * 7
    subPrices = [0.0] * 7
    
    temp = [""] * 4
    
    # Open connection to file
    file = open("costs.csv", "r")

    # Loop for each line of data
    for index in range(len(subNames)):
        # Read line of data
        line = file.readline()

        # Split line - array
        temp = line.split(",")

        # Assign values to arrays
        subNames[index] = temp[0].strip()
        subWeights[index] = int(temp[1].strip())
        subPrices[index] = float(temp[2].strip())
        

    # close connection to file
    file.close()

    # Return data
    return subNames, subWeights, subPrices


def increase(subPrices):
    """Return array of real, increased by 10%"""

    # Declare local variables and array
    price = 0.0
    newPrice = 0.0
    
    subNewPrices = [0.0] * len(subPrices)

    # Loop for each value
    for index in range(len(subPrices)):

        # Extract population
        price = subPrices[index]

        # Increase by 10% and round to 2 dp
        newPrice = round(price * 1.1, 2)

        # Store new value
        subNewPrices[index] = newPrice

    # Return values
    return subNewPrices


def saveData(subNames, subWeights, subPrices):
    """Save parallel arrays to updated.csv"""
    
    # Open connection to file
    file = open("updated.csv", "w")

    # Loop for each line of data
    for index in range(len(subNames)):
        file.write(subNames[index] + ",")
        file.write(str(subWeights[index]) + ",")
        file.write(str(subPrices[index]) + "\n")

    # close connection to file
    file.close()


#
# Main program
#

# Declare global variables and arrays
names = [""] * 7
weights = [0] * 7
prices = [0.0] * 7
newPrices = [0.0] * 7

# Get data
names, weights, prices = getData()

# Increase population
newPrices = increase(prices)

# Save data
saveData(names, weights, newPrices)
