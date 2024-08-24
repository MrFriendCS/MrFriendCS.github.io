# Title: H SDD Temperature v1
# Date: 12 Sep 2023
# Author: Mr Friend

# Declare variables and arrays
dates = [""] * 8759
times = [""] * 8759
tempFs = [0.0] * 8759
tempCs = [0.0] * 8759
line = ""
data = [""] * 3
tempF = 0.0
tempC = 0.0

# Read data from csv file

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
    tempFs[index] = float(data[2].strip())

# Close connection to file
file.close()

# Loop for each temperature
for index in range(len(tempFs)):

    # Get fahrenheit
    tempF = tempFs[index]

    # Calculate centigrade
    tempC = (tempF - 32) * (5 / 9)

    # Assign centigrade value
    tempCs[index]  = round(tempC, 1)

# Open connection to file
file = open("tempC.csv", "w")

# Loop for each row of data
for index in range(len(dates)):

    # Write row of data
    file.write(dates[index] + ",")
    file.write(times[index] + ",")    
    file.write(str(tempCs[index]) + "\n")

# Close connection to file
file.close()