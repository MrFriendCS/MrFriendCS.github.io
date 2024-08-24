# Title: H SDD Temperature v2
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
        data = line.split(",")
    
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


def writeData(dates, times, temps):
    """Write data to text file"""
    
    # Open connection to file
    file = open("tempC.txt", "w")
    
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

# Read data from csv file
dates, times, tempFs = getData()

# Convert temperatures
tempCs = convert(tempFs)

# Write data to txt file
writeData(dates, times, tempCs)
