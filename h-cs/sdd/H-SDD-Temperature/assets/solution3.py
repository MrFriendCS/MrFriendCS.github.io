# Title: H SDD Temperature v3
# Date: 12 Sep 2023
# Author: Mr Friend

# 
# Subprograms
#

def getData():
    """Read data from csv file and return parallel arrays"""

    # Declare local varaibles and arrays
    line = ""
    data = [""] * 3
    dates = [""] * 8759
    times = [""] * 8759
    temps = [0.0] * 8759
    
    # Open connection to file
    file = open("tempF.csv", "r")
    
    # Loop for each row of data
    for index in range(len(dates)):
    
        # Read row of data
        line = file.readline()
    
        # Split data into array
        tempArray = line.split(",")
    
        # Assign data to arrays
        dates[index] = data[0].strip()
        times[index] = data[1].strip()
        temps[index] = float(data[2].strip())
    
    # Close connection to file
    file.close()

    # Return parallel arrays
    return dates, times, temps


def convert(oldTemps):
    """Convert fahrenheit to centigrade"""

    # Declare local varaiables and array
    tempF = 0.0
    tempC = 0.0
    newTemps = [0.0] * len(oldTemps)
    
    # Loop for each temperature
    for index in range(len(oldTemps)):
    
        # Get fahrenheit
        tempF = oldTemps[index]
    
        # Calculate centigrade
        tempC = (tempF - 32) * (5 / 9)
    
        # Assign centigrade value
        newTemps[index]  = round(tempC, 1)

    # Return values
    return newTemps


def findMin(temps):
    """Find minimum temperature"""

    # Declare local variable
    min = 0.0

    # Assign first value as minimum
    min = temps[0]

    # Loop for remianing values
    for index in range (1, len(temps)):

        # Compare min with currect value
        if min > temps[index]:

            # Update min value
            min = temps[index]

    # Return min value
    return min


def findMax(temps):
    """Find maximum temperature"""

    # Declare local variable
    max = 0.0

    # Assign first value as minimum
    max = temps[0]

    # Loop for remianing values
    for index in range (1, len(temps)):

        # Compare max with currect value
        if max < temps[index]:

            # Update max value
            max = temps[index]

    # Return min value
    return max


def writeData(dates, times, temps, min, max):
    """Write data to csv file"""
    
    # Open connection to file
    file = open("results.txt", "w")

    # Write minimum temp to file
    file.write("The minimum temperature was " + str(min) + " deg C on the following dates:\n")
    
    # Loop for each row of data
    for index in range(len(dates)):

        # Compare min with currect value
        if min == temps[index]:

            # Write date to file
            file.write(dates[index] + "\n")

    # Write minimum temp to file
    file.write("\nThe maximum temperature was " + str(max) + " deg C on the following dates:\n")
    
    # Loop for each row of data
    for index in range(len(dates)):

        # Compare min with currect value
        if max == temps[index]:

            # Write date to file
            file.write(dates[index] + "\n")

    # Write data to file
    file.write("\nData:\n")
    
    # Loop for each row of data
    for index in range(len(dates)):
    
        # Write row of data
        file.write(dates[index] + ",")
        file.write(times[index] + ",")    
        file.write(str(temps[index]) + "\n")
    
    # Close connection to file
    file.close()


#
# Main program
#

# Declare global variables and arrays
dates = [""] * 8759
times = [""] * 8759
tempFs = [0.0] * 8759
tempCs = [0.0] * 8759
minTemp = 0.0
maxTemp = 0.0

# Read data from csv file
dates, times, tempFs = getData()

# Convert temperatures
tempCs = convert(tempFs)

# Find minimum
minTemp = findMin(tempCs)

# Find maximum
maxTemp = findMax(tempCs)

# Write data to txt file
writeData(dates, times, tempCs, minTemp, maxTemp)
