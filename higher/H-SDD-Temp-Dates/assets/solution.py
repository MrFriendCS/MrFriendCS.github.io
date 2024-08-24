# Title: H SDD Temperature Dates v1
# Author: Mr Friend
# Date: 9 Oct 2023

#
# Subprograms
#

def f2c(tempF):
    """Converts fahrenheit to celsius.  Rounds to 1 dp."""

    # Declare local variable
    tempC = 0.0

    # Convert
    tempC = (tempF - 32) * 5 / 9

    # Round
    tempC = round(tempC, 1)

    # Return celsius value
    return tempC


def us2iso(dateUS):
    """Converts mm-dd-yyyy to yyyy-mm-dd."""

    # Declare local variables
    dateISO = ""
    dd = ""
    mm = ""
    yyyy = ""

    # Extract values
    dd = dateUS[3:5]
    mm = dateUS[0:2]
    yyyy = dateUS[-4: ]

    # Combine value
    dateISO = yyyy + "-" + mm + "-" + dd

    # Return ISO format date
    return dateISO


def readData():
    """Read data from file and assign to parallel arrays."""

    # Declare local variables
    line = ""
    data = [""] * 3
    dates = [""] * 8759
    times = [""] * 8759
    temps = [0.0] * 8759

    # Open connection to the file
    file = open("tempF.csv", "r")

    # Read each row of data
    for index in range(len(dates)):

        # Read line of data
        line = file.readline()

        # Split line at commas
        data = line.split(",")

        # Assign data to parallel arrays
        dates[index] = data[0].strip()
        times[index] = data[1].strip()
        temps[index] = float(data[2].strip())

    # Close connection to the file
    file.close()

    # Return arrays
    return dates, times, temps


def convertTemps(temps):
    """Convert array: fahrenheit to celsius."""

    # Loop for each value
    for index in range(len(temps)):
        temps[index] = f2c(temps[index])

    # Return values
    return temps


def convertDates(dates):
    """Convert array: US to ISO."""

    # Loop for each value
    for index in range(len(dates)):
        dates[index] = us2iso(dates[index])

    # Return values
    return dates


def writeData(dates, times, temps):
    """Write data to file from parallel arrays."""

    # Create file
    file = open("tempC.csv", "w")
    
    # Loop for each value
    for index in range(len(dates)):

        # Write a line of data
        file.write(dates[index] + ",")
        file.write(times[index] + ",")
        file.write(str(temps[index]) + "\n")

    # Close connection to the file
    file.close()

    
#
# Main program
#

# Declare global variables
dates = [""] * 8759
times = [""] * 8759
temps = [0.0] * 8759

# 1. Read the data from a csv file: tempF.csv
dates, times, temps = readData()

# 2. Convert the temperatures from Fahrenheit to Centigrade
temps = convertTemps(temps)

# 3. Convert the dates from US to ISO format
dates = convertDates(dates)

# 4. Write the data to a csv file: tempC.csv
writeData(dates, times, temps)
