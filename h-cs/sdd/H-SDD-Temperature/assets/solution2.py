# Title: H SDD Temperature Part 2
# Date: 9 Sep 2025
# Author: Mr Friend

# Get extra code
from dataclasses import dataclass


@dataclass
class HourlyValue:
    """A record to hold temperature data."""
    
    # Fields
    date: str = ""
    time: str = ""
    temp: float = 0.0


# 
# Subprograms
#

def readData():
    """Read data from csv file and return an array of records."""

    # Declare local varaibles and arrays
    line = ""
    data = [""] * 3
    hourlyValues = [HourlyValue() for index in range(8759)]
    
    # Open connection to file
    file = open("tempF.csv", "r")
    
    # Loop for each row of data
    for index in range(len(hourlyValues)):
    
        # Read row of data
        line = file.readline()
    
        # Split data into array
        data = line.split(",")
    
        # Assign data to arrays
        hourlyValues[index].date = data[0].strip()
        hourlyValues[index].time = data[1].strip()
        hourlyValues[index].temp = float(data[2].strip())
    
    # Close connection to file
    file.close()

    # Return array of records
    return hourlyValues


def convertTemps(hourlyValues):
    """Convert fahrenheit to centigrade, to 1 dp, and return an array."""

    # Declare local variables
    newTemps = [0.0] * len(hourlyValues)
    
    # Loop for each temperature
    for index in range(len(hourlyValues)):
    
        # Calculate centigrade and assign to array
        newTemps[index] = round((hourlyValues[index].temp - 32) * (5 / 9), 1)
    
    # Return values
    return newTemps


def convertDates(hourlyValues):
    """Convert US dates to ISO dates and return an array."""

    # Declare local variables
    newDates = [0.0] * len(hourlyValues)
    tempDate = ""
    year = ""
    month = ""
    day = ""
    
    # Loop for each date
    for index in range(len(hourlyValues)):
    
        # Get current US date
        tempDate = hourlyValues[index].date
        
        # Extract month, day, year
        month = tempDate[ :2]
        day = tempDate[3:5]
        year = tempDate[6: ]
        
        # Create ISO date and assign to array
        newDates[index] = year + "-" + month + "-" + day
    
    # Return ISO dates
    return newDates


def extractTimes(hourlyValues):
    """Extract times and return an array."""

    # Declare local variables
    newTimes = [0.0] * len(hourlyValues)
    
    # Loop for each time
    for index in range(len(hourlyValues)):
    
        # Calculate centigrade and assign to array
        newTimes[index] = hourlyValues[index].time
    
    # Return times
    return newTimes
    

def writeData(dates, times, temps):
    """Write data to text file."""
    
    # Open connection to file
    file = open("tempC.csv", "w")
    
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

def main():
    
    # Declare global variables and arrays
    hourlyValues = [HourlyValue() for index in range(8759)]
    tempsC = [0.0] * len(hourlyValues)
    datesISO = [""] * len(hourlyValues)
    times = [""] * len(hourlyValues)

    # Read data from csv file
    hourlyValues = readData()

    # Convert temperatures from F to C (1 dp)
    tempsC = convertTemps(hourlyValues)
    
    # Convert dates from US to ISO format
    datesISO = convertDates(hourlyValues)
    
    # Extract times
    times = extractTimes(hourlyValues)

    # Write data to csv file
    writeData(datesISO, times, tempsC)
    
# Call main()
main()
