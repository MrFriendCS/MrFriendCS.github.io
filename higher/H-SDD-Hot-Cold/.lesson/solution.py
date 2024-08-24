# Title: Hot & Cold
# Author: Mr Friend
# Date: 27 Sep 2022

#
# Functions and procedures
#

def getData():
    '''Read data from file.  Return parallel arrays.'''
    
    # Declare local variables and data structures
    size = 8759
    localDates = [""] * size
    localTimes = [""] * size
    localTemps = [0.0] * size
    tempArray = [""] * 3
    
    # Read data from file
    file = open("Temperature Data.csv", "r")
    
    for index in range(len(localDates)):
        # Read the next line from the file
        line = file.readline()
        # Split the line and create an array
        tempArray = line.split(",")

        # Assign values to parralel arrays
        localDates[index] = tempArray[0].strip()
        localTimes[index] = tempArray[1].strip()
        localTemps[index] = float(tempArray[2].strip())

    # Close the connection
    file.close()

    # Return parallel arrays
    return localDates, localTimes, localTemps

def findMax(localTemps):
    '''Find the maximum temperature.'''
    
    # Declare local variable
    localMax = 0.0

    # Set max to first value in array
    localMax = localTemps[0]

    # Loop from second value
    for index in range(1, len(localTemps)):
        if localTemps[index] > localMax:
            # Set new maximum
            localMax = localTemps[index]

    # Return max temperature
    return localMax

def findMin(localTemps):
    '''Find the minimum temperature.'''
    
    # Declare local variable
    localMin = 0.0

    # Set max to first value in array
    localMin = localTemps[0]

    # Loop from second value
    for index in range(1, len(localTemps)):
        if localTemps[index] < localMin:
            # Set new minimum
            localMin = localTemps[index]

    # Return min temperature
    return localMin

def writeResults(localMax, localMin, localDates, localTimes, localTemps):
    '''Write results to text file.'''

    # Create or overwrite file
    file = open("Hot and Cold.txt", "w")

    # Write hot results
    file.write("The maximum temperature was ")
    file.write(str(localMax) + " degrees Fahrenheit.  ")
    file.write("This temperature occurred at the following dates and times:\n\n")

    # Find all max temperatures
    for index in range(len(localTemps)):
        if localTemps[index] == localMax:
            file.write(dates[index] + "," + times[index] + "\n")

    # Write cold results
    file.write("\nThe minimum temperature was ")
    file.write(str(localMin) + " degrees Fahrenheit.  ")
    file.write("This temperature occurred at the following dates and times:\n\n")

    # Find all min temperatures
    for index in range(len(localTemps)):
        if localTemps[index] == localMin:
            file.write(dates[index] + ",")
            file.write(times[index] + "\n")

    # Close the connection
    file.close()

    
#
# Main Program
#

# Declare global variables and data structures
size = 8759
dates = [""] * size
times = [""] * size
temps = [0.0] * size
max = 0.0
min = 0.0

# Get values from file
dates, times, temps = getData()

# Get maximum temperature
max = findMax(temps)

# Get minimum temperature
min = findMin(temps)

# Write results to file
writeResults(max, min, dates, times, temps)