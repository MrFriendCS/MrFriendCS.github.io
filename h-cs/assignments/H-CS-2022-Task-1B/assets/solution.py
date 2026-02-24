# Title: H CS 2022 Task 1 Part B
# Author: Mr Friend
# Date: 26 Feb 2025

# Import code for records
from dataclasses import dataclass


@dataclass
class Sighting:
    """A record to represent a sighting."""
    
    town: str = ""
    mammal: str = ""
    date: str = ""
    age: int = 0


def getSightings():
    """Read from text file into sightings array of records."""
    
    # Initialise local variables
    town = ""
    mammal = ""
    date = ""
    age = 0
    data = [""] * 4
    sightingsData = [Sighting() for i in range(200)]

    # Connect to the file
    file = open("mammals.txt", "r")

    # Loop for 200 sightings
    for index in range(len(sightingsData)):

        # Read a line from the file
        line = file.readline()

        # Split line
        data = line.split(",")

        # Assign data to record
        sightingsData[index].town = data[0].strip()
        sightingsData[index].mammal = data[1].strip()
        sightingsData[index].date = data[2].strip()
        sightingsData[index].age = int(data[3].strip())

    return sightingsData


def displayOldest(sightingsData):
    """Find and display the age of the oldest walker in the sightings data."""
    
    # Initialise local variables
    oldest = 0
    
    # Set furthest to first value
    oldest = sightingsData[0].age
    
    # Loop through all records
    for index in range(1, len(sightingsData)):
        if sightingsData[index].age > oldest:
            oldest = sightingsData[index].age
    
    # Display oldest walker
    print("Age of the oldest walker: " + str(oldest))


def displaySightings(sightingsData):
    """Find and display the dates of sightings of a 
    chosen mammal in a particular town."""
    
    # Initialise local variables
    town = ""
    mammal = ""

    # 3.1 Ask user to enter town
    town = input("Which town? ")

    # 3.2 Call a function to return a string input
    #     that starts with an upper-case character
    town = upperChr(town)

    # 3.3 Ask user to enter mammal
    mammal = input("Which mammal? ")

    # 3.4 Call a function to return a string input
    #     that starts with an upper-case character
    mammal = upperChr(mammal)

    # 3.5 Display “The dates of sightings were:”
    print("The dates of sightings were:")

    # 3.6 Start loop for each sighting in array of records
    for index in range(len(sightingsData)):

        # 3.7 If sighting matches entered town and mammal then
        if sightingsData[index].town == town and sightingsData[index].mammal == mammal:

            # 3.8 Display date
            print(sightingsData[index].date)
        
        # 3.9 End if
    
    # 3.10 End loop


def upperChr(word):
    """Return a string that starts with an upper-case character."""
    
    # Declare local variables
    firstChar = 0

    # Set firstChar to ASCII value of first character in string 
    firstChar = ord(word[0])

    # If the firstChar is between 97 and 122 then
    if firstChar >= 97 and firstChar <= 122:

        # Set firstChar to firstChar −32
        firstChar = firstChar - 32

        # Set string to concatenation of the new first character and the remaining string
        word = chr(firstChar) + word[1:]
    
    # End if

    # Return the string
    return word


def countSightings(sightingsData):
    """Count and display the number of sightings
    for each date in the text file."""
    
    # Declare local variables
    dayToCount = ""
    count = 0

    # 4.1 Set dayToCount to first date in sightings array
    dayToCount = sightingsData[0].date
    
    # 4.2 Set count to 1
    count = 1

    # 4.3 Start loop from second record to end of sightings array
    for index in range(1, len(sightingsData)):
        
        # 4.4 If date in current record is the same as dayToCount then
        if sightingsData[index].date == dayToCount:

            # 4.5 Add 1 to count
            count = count + 1
        
        # 4.6 Else
        else:

            # 4.7 Display dayToCount and count
            print(dayToCount + " - " + str(count))

            # 4.8 Set dayToCount to date in current record
            dayToCount = sightingsData[index].date

            # 4.9 Set count to 1 
            count = 1
        
        # 4.10 End if

    # 4.11  End loop

    # 4.12  Display dayToCount and count
    print(dayToCount + " - " + str(count))


#
## Main Program
#

# Declare global variables
sightings = [Sighting() for i in range(200)]

# 1 Read from text file into sightings array
#   of records
sightings = getSightings()

# 2 Find and display the age of the
#   oldest walker in the sightings data
displayOldest(sightings)

# 3 Find and display the dates of sightings
#   of a chosen mammal in a particular town
displaySightings(sightings)

# 4 Count and display the number of sightings 
#   for each date in the text file
countSightings(sightings)
