# Title: LaGuardia Temperatures - Fahrenheit to Celsius v2 (Records)
# Author: 
# Date: 


# Import module


# Define record



def getData():
    # Declare local variables
    

    # Declare local array
    values = []

    # Get data from file


    return values


def convertFtoC(tempValuesF):
    # Declare local variable


    # Declare local array
    tempValuesC = []

    # Convert temperatures to 1 deciaml place




    return tempValuesC


def getMax(tempValuesC):
    # Declare local variable
    maxC = 0

    # Find maximum temperature
 

    return maxC


def getMin(tempValuesC):
    # Declare local variable
    minC = 0

    # Find maximum temperature


    return minC


def writeData(maxC, minC, tempValuesC):
    # Declare local variables


    # Write data to 'LaGuardia-C.csv'

    None



# Main program

# Declare global arrays
tempF = []
tempC = []

# Get data
tempF = getData()

# Convert temperatures
tempC = convertFtoC(tempF)

# Find maximum temperature
maxTemp = getMax(tempC)

# Find minimum temperature
minTemp = getMin(tempC)

# Write data to file
writeData(maxTemp, minTemp, tempC)
