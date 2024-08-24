# Title: Qualifying Runners
# Author: Mr Friend
# Date: 14 Nov 2021

from dataclasses import dataclass

@dataclass
class runner:
    name: str = ""
    distance: int = 0
    time: float = 0.0


def getData():
    '''
    Read data from text file into array of records
    '''

    # Declare local variables
    line = ""
    data= [""] * 3
    runnerName = ""
    runnerDist = 0
    runnerTime = 0.0
    runners = [runner()] * 15

    # Open connection to the file
    file = open("maleRunners.txt")

    # Read and store each row of data
    for index in range(len(runners)):
        # Read next line
        line = file.readline()

        # Split line
        data = line.split(",")

        # Get individual values
        runnerName = data[0].strip()
        runnerDist = int(data[1].strip())
        runnerTime = float(data[2].strip())

        # Store values in array of records
        runners[index] = runner(runnerName, runnerDist, runnerTime)

    return runners


def getDistance():
    '''
    Ask the user to enter the length of the race (100, 200 or 400)
    '''

    # Declare local variable
    userDist = 0

    # Only accept valid distance
    while userDist != 100 and userDist != 200 and userDist != 400:

        # Get value from user
        userDist = int(input("Enter the length of the race: "))

        # Display error
        if userDist != 100 and userDist != 200 and userDist != 400:
            print("Distance must be 100, 200, or 400")

    return userDist


def getTime():
    '''
    Ask the user to enter the qualifying time
    '''

    # Declare local variable
    userTime = 0.0

    # Get value from user
    userTime = float(input("Enter the qualifying time: "))

    return userTime


def displayQualified(runners, runDist, runTime):
    '''
    Display all the runners, for the selected race, who have run faster than the qualifying time
    '''

    # Loop for each runner
    for index in range(len(runners)):

        # Find who matches the criteria
        if runners[index].distance == runDist and runners[index].time < runTime:

            # Display qualifying runner with time
            print(runners[index].name + ", " + str(runners[index].time))


#
## Main Program
#

# Declare global variables
sprinters = [runner()] * 15
qualDistance = 0
qualTime = 0.0

# Get sprinters
sprinters = getData()

# Get qualifying distance
qualDistance = getDistance()

# Get qualifying time
qualTime = getTime()

# Display qualifying runners
displayQualified(sprinters, qualDistance, qualTime)
