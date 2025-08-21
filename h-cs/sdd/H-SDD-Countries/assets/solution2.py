# Title: H-SDD-Countries Part 2
# Author: Mr Friend
# Date: 21 Aug 2025

# Initialise variables
countries = [""] * 6
capitals = [""] * 6
populations = [0] * 6

# Make connection to file
file = open("countries.csv", "r")

# Loop for each record
for index in range(len(countries)):
    
    # Read a line from the file
    line = file.readline()
    
    # Split the line
    data = line.split(",")
    
    # Assign data to parallel arrays
    countries[index] = data[0].strip()
    capitals[index] = data[1].strip()
    populations[index] = float(data[2].strip())

# Close connection to file
file.close()


# Display data
print("Country : Population : Capital")
print("-------   ----------   -------\n")

# Loop for each record
for index in range(len(countries)):
    
    print(countries[index] + " : " +
          capitals[index]  + " : " +
          str(populations[index]))