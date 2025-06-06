# Title: H 2019 Task 2 Part B
# Author: Mr Friend
# Date: 26 Feb 2025

# Import module
from dataclasses import dataclass


@dataclass
class Member:
    """A record to represent a member."""
    forename: str = ""
    surname: str = ""
    distance: float = 0.0


def getData():
    """Read members’ data from file into array of records"""

    # Initialise local variable and arrays
    line = ""
    data = [""] * 3
    membersArray = [Member() for i in range(20)]
    
    # 1.1 Open members.txt file
    file = open("members.txt", "r")

    # 1.2 Start loop for each member
    for index in range(len(membersArray)):

        # 1.3-4 Get member forename, surname, distance
        line = file.readline()

        # Split the line
        data = line.split(",")
        
        # 1.6 Store member forename, surname and distance in members() array
        membersArray[index].forename = data[0].strip()
        membersArray[index].surname = data[1].strip()
        membersArray[index].distance = float(data[2].strip())

    # 1.7 End loop

    # 1.8 Close members.txt file
    file.close()
 
    # Return the array of records
    return membersArray


def findFurthest(membersData):
    """Find the furthest distance walked."""

    # Initialise local variable
    furthestWalked = 0.0

    # 2.1 Set furthest to distance stored for first member in members() array
    furthestWalked = membersData[0].distance
    
    # 2.2 Start fixed loop from second member to end of array
    for index in range(1, len(members)):

        # 2.3 If distance the current member walked is greater than furthest Then
        if membersData[index].distance > furthestWalked:

            # 2.4 Set furthest to current distance
            furthestWalked = membersData[index].distance

        # 2.5 End If

    # 2.6 End fixed loop
    
    # Return furthest distance walked
    return furthestWalked


def displayFurthest(furthestWalked):
    """Display the furthest distance walked."""

    print("The furthest distance walked was " + str(furthestWalked) + " miles.")


def writePrizeWinnersFile(membersArray, furthestWalked):
    """Write club prize winners to file."""
    
    # Initialise local variable
    wholeMarathons = 0
    
    # 4.1 Open results.txt file
    file = open("results.txt", "w")

    # 4.2 Write “The prize winning members are:” to the results.txt file
    file.write("The prize winning members are:\n")

    # 4.3 Start loop for each record in members() array
    for index in range(len(membersArray)):

        # 4.4 If the distance the member walked is greater than 0.7*furthest
        if membersArray[index].distance > 0.7 * furthestWalked:

            # 4.5 write the forename and surname to the results.txt file
            file.write(membersArray[index].forename + ",")
            file.write(membersArray[index].surname + "\n")
        
        # 4.6 End if

    # 4.7 End loop

    # 4.8 Write “The number of whole marathons walked by each member is”
    #     to the results.txt file
    file.write("The number of whole marathons walked by each member is:\n")

    # 4.9 Start loop for each record in members() array
    for index in range(len(membersArray)):

        # 4.10 Calculate the number of whole marathons walked
        wholeMarathons = int(membersArray[index].distance / 26.22)

        # 4.11  Write the forename, surname and the number of
        #       whole marathons to the results.txt file
        file.write(membersArray[index].forename + ",")
        file.write(membersArray[index].surname + ",")
        file.write(str(wholeMarathons) + "\n")

    # 4.12 End loop

    # 4.13 Close the results.txt file
    file.close()


#
## Main Program
#

# Initialise global variables and arrays
furthest = 0.0
members = [Member() for i in range(20)]

# 1. Read members' data into an array of records
members = getData()

# 2. Find the furthest distance walked
furthest = findFurthest(members)

# 3. Display the furthest distance walked
displayFurthest(furthest)

# 4. Write club prize winners to file
writePrizeWinnersFile(members, furthest)

