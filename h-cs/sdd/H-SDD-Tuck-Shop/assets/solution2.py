# Title: H SDD Update Prices
# Author: Mr Friend
# Date 22 Aug 2024

#
# Subprograms
#

def getData() -> tuple[list[str], list[int], list[float]]:
    """Return parallel arrays from costs.csv"""

    # Declare local variable and arrays
    line = ""
    
    subNames = [""] * 11
    subWeights = [0] * 11
    subPrices = [0.0] * 11
    
    data = [""] * 3
    
    # Open connection to file
    file = open("tuckshop.csv", "r", encoding="UTF-8")

    # Loop for each line of data
    for index in range(len(subNames)):
        # Read line of data
        line = file.readline()

        # Split line - array
        data = line.split(",")

        # Assign values to arrays
        subNames[index] = data[0].strip()
        subWeights[index] = int(data[1].strip())
        subPrices[index] = float(data[2].strip())
        

    # close connection to file
    file.close()

    # Return data
    return subNames, subWeights, subPrices


def increase(subPrices: list[float]) -> list[float]:
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


def firstLetter(subNames: list[str]) -> list[str]:
    """Return array of strings.  Each starts with a cpital letter."""

    # Declare local variables and array
    firstChr = ""
    
    # Loop for each name
    for index in range(len(subNames)):

        # Get first letter
        firstChr = subNames[index][0]
        
        # ASCII value
        ascii = ord(firstChr)
        
        if ascii >= 97 and ascii <= 122:
            firstChr = chr(ascii-32)
            subNames[index] = firstChr + subNames[index][1: ]
    
    # Return values
    return subNames


def saveData(subNames: list[str], subWeights: list[int],
             subPrices: list[float]) -> None:
    """Save parallel arrays to saleprices.csv"""
    
    # Open connection to file
    file = open("saleprices.csv", "w", encoding="UTF-8")

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
names = [""] * 11
weights = [0] * 11
prices = [0.0] * 11
newPrices = [0.0] * 11
newNames = [""] * 11

# Get data
names, weights, prices = getData()

# Increase population
newPrices = increase(prices)

# Increase population
newNames = firstLetter(names)

# Save data
saveData(newNames, weights, newPrices)
