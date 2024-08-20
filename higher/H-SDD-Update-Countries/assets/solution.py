# Title: H SDD Update Countries
# Author: Mr Friend
# Date 5 Sep 2023

#
# Subprograms
#

def getData():
    """Return parallel arrays from countries.csv"""

    # Declare local variable and arrays
    line = ""
    
    caps = [""] * 6
    states = [""] * 6
    pops = [0.0] * 6
    
    temp = [""] * 3
    
    # Open connection to file
    file = open("countries.csv", "r")

    # Loop for each line of data
    for index in range(len(caps)):
        # Read line of data
        line = file.readline()

        # Split line - array
        temp = line.split(",")

        # Assign values to arrays
        caps[index] = temp[0].strip()
        states[index] = temp[1].strip()
        pops[index] = float(temp[2].strip())

    # close connection to file
    file.close()

    # Return data
    return caps, states, pops


def increase(values):
    """Return array of real, increased by 10%"""

    # Declare local variables and array
    value = 0.0
    newValue = 0.0
    
    newValues = [0.0] * len(values)

    # Loop for each value
    for index in range(len(values)):

        # Extract population
        value = values[index]

        # Increase by 10% and round to 1 dp
        newValue = round(value * 1.1, 1)

        # Store new value
        newValues[index] = newValue

    # Return values
    return newValues


def saveData(states, caps, pops):
    """Save parallel arrays to updated.csv"""
    
    # Open connection to file
    file = open("updated.csv", "w")

    # Loop for each line of data
    for index in range(len(caps)):
        file.write(states[index] + ",")
        file.write(caps[index] + ",")
        file.write(str(pops[index]) + "\n")

    # close connection to file
    file.close()


#
# Main program
#

# Declare global variables and arrays
countries = [""] * 6
capitals = [""] * 6
populations = [0.0] * 6
newPops = [0.0] * 6

# Get data
capitals, countries, populations = getData()

# Increase population
newPops = increase(populations)

# Save data
saveData(countries, capitals, newPops)
