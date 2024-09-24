# Title: LaGuardia Temperatures - Fahrenheit to Celsius
# Author: 
# Date: 

def getData():
    # Declare local arrays
    dateValues = []
    timeValues = []
    tempValues = []

    # Get data from file




    return dateValues, timeValues, tempValuesF


def convertFtoC(tempValuesF):
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


def writeData(maxC, minC, dateValues, timeValues, tempValuesC):
    # Write data to 'LaGuardia-C.csv'

    None # Delete this line later





# Main program

# Get data
tempDate, tempTime, tempF = getData()

# Convert temperatures
tempC = convertFtoC(tempF)

# Find maximum temperature
maxTemp = getMax(tempC)

# Find minimum temperature
minTemp = getMin(tempC)

# Write data to file
writeData(maxTemp, minTemp, tempDate, tempTime, tempC)
