# Title: H SDD Temperature Part 1
# Date: 9 Sep 2025
# Author: Mr Friend

# 
# Subprograms
#

def readData():
    """Read data from csv file and return parallel arrays."""

    # Declare local varaibles and arrays
    line = ""
    data = [""] * 3
    dates = [""] * 8759
    times = [""] * 8759
    temps = [""] * 8759
    
    # Open connection to file
    file = open("tempF.csv", "r")
    
    # Loop for each row of data
    for index in range(len(dates)):
    
        # Read row of data
        line = file.readline()
    
        # Split data into array
        data = line.split(",")
    
        # Assign data to parallel arrays
        dates[index] = data[0].strip()
        times[index] = data[1].strip()
        temps[index] = float(data[2].strip())
    
    # Close connection to file
    file.close()

    # Return parallel arraya
    return dates, times, temps


def convertTemps(temps):
    """Convert fahrenheit to centigrade, to 1 dp, and return an array."""

    # Declare local variables
    newTemps = [0.0] * len(temps)
    
    # Loop for each temperature
    for index in range(len(temps)):
    
        # Calculate centigrade and assign to array
        newTemps[index] = round((temps[index] - 32) * (5 / 9), 1)
    
    # Return values
    return newTemps


def convertDates(dates):
    """Convert US dates to ISO dates and return an array."""

    # Declare local variables
    newDates = [0.0] * len(dates)
    tempDate = ""
    year = ""
    month = ""
    day = ""
    
    # Loop for each date
    for index in range(len(dates)):
    
        # Get current US date
        tempDate = dates[index]
        
        # Extract month, day, year
        month = tempDate[ :2]
        day = tempDate[3:5]
        year = tempDate[6: ]
        
        # Create ISO date and assign to array
        newDates[index] = year + "-" + month + "-" + day
    
    # Return ISO dates
    return newDates
  

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
    datesUS = [""] * 8759
    times = [""] * 8759
    tempsF = [0.0] * 8759
    datesISO = [""] * 8759
    tempsC = [0.0] * 8759

    # Read data from csv file
    datesUS, times, tempsF = readData()

    # Convert temperatures from F to C (1 dp)
    tempsC = convertTemps(tempsF)
    
    # Convert dates from US to ISO format
    datesISO = convertDates(datesUS)
    
    # Write data to csv file
    writeData(datesISO, times, tempsC)
    
# Call main()
main()
