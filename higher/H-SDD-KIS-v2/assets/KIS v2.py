# Title: LaGuardia Temperatures - Fahrenheit to Celsius v2 (Records)
# Author: Mr Friend
# Date: 24 Nov 2020


# import module
from dataclasses import dataclass

# Define record
@dataclass
class tempData:
    date: str   # Not changed in program
    time: str   # Not changed in program
    temp: float # Farhrenheit / Celsius values


def getData():
    # Declare local variables
    file = ""
    line = ""
    lineDate = ""
    lineTime = ""
    lineTemp = 0.0

    # Declare local array
    values = []

    # Connect to file
    file = open("LaGuardia.csv", "r")

    # Read first line
    line = file.readline()

    # Loop through the file
    while line:
        # Split the values into an array 
        tempArray = line.split(",")

        # Store each value in a seperate variable
        lineDate = tempArray[0].strip()
        lineTime = tempArray[1].strip()
        lineTemp = float(tempArray[2].strip())

        # Create a record
        tempRecord = tempData(lineDate, lineTime, lineTemp)

        # Append the record to the array
        values.append(tempRecord)

        # Read the next line
        line = file.readline()

    return values


def convertFtoC(tempValuesF):
    # Declare local variable
    tempCelsius = 0.0
    tempFahrenheit = 0.0

    # Declare local array
    tempValuesC = []

    # Convert temperatures to 1 deciaml place
    for index in range(len(tempValuesF)):

        # Get the temperature value from the record
        tempFahrenheit = tempValuesF[index].temp

        # Convert value from F to C
        tempCelsius = (tempFahrenheit - 32) * 5 / 9

        # Round C value to 1 dp
        tempCelsius = round(tempCelsius, 1)

        # Create a record
        tempRecord = tempData(tempValuesF[index].date, tempValuesF[index].time, tempCelsius)

        # Append record to new array
        tempValuesC.append(tempRecord)

    return tempValuesC


def getMax(tempValuesC):
    # Declare local variable
    maxC = 0

    # Find maximum temperature
    maxC = tempValuesC[1].temp

    for index in range(1, len(tempValuesC)):
        if tempValuesC[index].temp > maxC:
            maxC = tempValuesC[index].temp

    return maxC


def getMin(tempValuesC):
    # Declare local variable
    minC = 0

    # Find maximum temperature
    minC = tempValuesC[1].temp

    for index in range(1, len(tempValuesC)):
        if tempValuesC[index].temp < minC:
            minC = tempValuesC[index].temp

    return minC


def writeData(maxC, minC, tempValuesC):
    # Declare local variables
    recDate = ""
    recTime = ""
    recTemp = 0.0

    # Write data to 'LaGuardia-C.csv'

    file = open("LaGuardia-C.csv", "w")

    file.write("All temperatures are Celsius.\n\n")
    file.write("The maximum temperature is: " + str(maxC) + "\n\n")
    file.write("The minimum temperature is: " + str(minC) + "\n\n")

    for index in range(len(tempValuesC)):
        recDate = tempValuesC[index].date
        recTime = tempValuesC[index].time
        recTemp = tempValuesC[index].temp

        file.write(recDate + "," + recTime + "," + str(recTemp) + "\n")

    file.close()

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

print("Finished.")
