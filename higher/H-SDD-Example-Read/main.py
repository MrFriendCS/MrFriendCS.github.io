# Title: H SDD Example Read
# Author: Mr Friend
# Data: 2 Oct 2023

"""
A program to demonstrate reading from a file.
"""

# Declare variables
line = ""
count = 0  # Count lines in file
maxLength = 20

# Declare data structures
"""
The first array is for the split data.
The other arrays are the parallel arrays.
"""
data = [""] * 3  # Number of parallel arrays
cities = [""] * maxLength
countries = [""] * maxLength
populations = [0.0] * maxLength


"""
Determine how many lines of data there are in the csv file.
"""

# Make a connection to the file
file = open("europe.csv", "r")

# Read the first line of the file
line = file.readline()

# Loop for each line in the file
while line != "":

    # Increment counter
    count = count + 1

    # Read next line
    line = file.readline()

# Close the connection to the file
file.close()


"""
Read the data from the csv file a line at a time.
Split the data and assign to an array.
Assign individual elements to parallel arrays, and
  cast if required,
"""

# Make a connection to the file
file = open("europe.csv", "r")

# Loop for each line of data
for index in range(count):

    # Read a line
    line = file.readline()

    # Split line at commas
    data = line.split(",")

    # Assign data to parallel arrays
    cities[index] = data[0].strip()
    countries[index] = data[1].strip()
    populations = float(data[2].strip())  # Cast

# Close the connection to the file
file.close()

"""
Info only.
Display the data held in one of the parralel arrays.
"""

# Loop for each line of data
for index in range(count):

    # Display current city
    print(cities[index])
