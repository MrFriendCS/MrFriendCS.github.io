# Title: Create H Santa Data
# Author: Mr Friend
# Date: 15 Dec 2024

"""
Create the data and export as CSV.
Seperate list of naughty children used to overwrite random records.
Naughty children are removed from the gift list, as they don't deserve them!
"""

# Import Extra Code
import sys
from dataclasses import dataclass
import random


# Find DDDhelper file
shool = "C:\\Users\\afriend1r\\AppData\\Local\\Programs\\Thonny"

start1 = "C:\\Users\\afriend1r\\OneDrive - Glow Scotland\\"
start2 = "D:\\OneDrive - Glow Scotland\\"

folder1 = "GitHub\\MrFriendCS.github.io\\"
folder2 = "SQA - CS - N5\\DDD\\Database Files\\"  # Definately N5 folder

# Check if directory exists
if shool in sys.path:
    # School laptop
    sys.path.append(start1 + folder1)
    school = True
    
else:
    # Personal laptop
    sys.path.append(start2 + folder1)
    school = False

# Get extra code
import DDDhelper


def createChildData(count):
    """Create the data, apart from nice, for the child entity."""
    
    
    @dataclass
    class Child:
        """Record to represent a child."""
        childID: int = 0
        first: str = ""
        last: str = ""
        nice: bool = True
        
    
    # Initialise local variables
    children = [Child() for index in range(count)]
    
    # Loop for each child
    for index in range(count):
        children[index].childID = index + 1
        children[index].first = DDDhelper.getForename()
        children[index].last = DDDhelper.getSurname()
    
    return children


def createGiftData(noOfGifts, noOfKids):
    """Create the data for the gift entity."""
    
    
    @dataclass
    class Gift:
        """A record to represent a gift."""
        giftID: int = 0
        childID: int = 0
        gift: str = ""
        cost: float = 0.0
        
    # Initialise local variables
    listOfGifts = []
    listOfCosts = []
    gifts = [Gift() for index in range(noOfGifts)]
    
        
    # Get Gift data
    
    fileIn = open("../CSV files/GiftList.csv", "r")
    
    line = fileIn.readline()  # Ignore heading row
    line = fileIn.readline()


    while line != "":
    
        data = line.split(",")
        
        listOfGifts = listOfGifts + [data[0].strip()]
        listOfCosts = listOfCosts + [data[1].strip()]
        
        line = fileIn.readline()
        
    fileIn.close()
    
    
    # Loop for each gift
    for index in range(noOfGifts):
        gifts[index].giftID = index + 1
        gifts[index].childID = DDDhelper.getNumber(1, noOfKids)
        
        giftIndex = random.randint(0, len(listOfGifts)-1)
        
        gifts[index].gift = listOfGifts[giftIndex]
        gifts[index].cost = listOfCosts[giftIndex]
        
        
    # Check childID 172 has at least two gifts
    # Used for an update task
    
    count = 0
    
    for index in range(len(gifts)):
        
        if gifts[index].childID == 172:
            count = count + 1
    
    if count < 2:
        
        for counter in range(2-count):
            
            gifts[random.randint(0, len(gifts)-1)].childID = 172
    
    return gifts


def naughtyKids(children, gifts):
    """Insert naughty children and update all their gifts."""
    
    # Naughty children - 2D array
    naughtyFirst = []
    naughtyLast = []
    
    if school:
        location = start1 + folder2
    else:
        location = start2 + folder2
        
    file = open(location + "naughtyList.csv", "r")
    
    line = file.readline()  # ignore header
    line = file.readline()
    
    while line != "":
        
        data = line.split(",")
        
        naughtyFirst = naughtyFirst + [data[0].strip()]
        naughtyLast = naughtyLast + [data[1].strip()]
        
        line = file.readline()
    
    # List of numbers 
    naughtyNumbers = [index for index in range(1, len(children)-1)]
    
    # Pick index positions of naughty children
    naughtyIDs = random.sample(naughtyNumbers, k=len(naughtyFirst))

    # Loop for each naughty child
    for index in range(len(naughtyFirst)):
        
        children[naughtyIDs[index]].first = naughtyFirst[index]
        children[naughtyIDs[index]].last = naughtyLast[index]
        children[naughtyIDs[index]].nice = False

    """
    pointer = 0
    
    # Loop for each naughty child
    for index in range(len(children)):
        
        if children[index].childID in naughtyIDs:
            children[index].first = naughtyFirst[pointer]
            children[index].last = naughtyLast[pointer]
            children[index].nice = False
            
            pointer = pointer + 1
    """
    
    
    # Convert index positions to numbers
    for index in range(len(naughtyFirst)):
        naughtyIDs[index] = naughtyIDs[index] + 1 
    
    
    # Loop for each gift - Set to coal
    for index in range(len(gifts)):
        
        if gifts[index].childID in naughtyIDs:
            gifts[index].gift = "Lump of coal"
            gifts[index].cost = 0.50
            
                      
    return children, gifts


def writeChildCSV(children):
    """Create CSV file for data."""
    
    file = open("../CSV files/Child.csv", "w")
    
    # Headers
    file.write("childID,firstName,lastName,nice\n")

    # Loop for each child
    for child in children:
        
        file.write(str(child.childID) + ",")
        file.write(    child.first + ",")
        file.write(    child.last + ",")
        file.write(str(child.nice).upper() +"\n")
        
    file.close()
        

def writeGiftCSV(gifts):
    """Create CSV file for data."""
    
    file = open("../CSV files/Gift.csv", "w")
    
    # Headers
    file.write("giftID,childID,gift,cost\n")
    
    # Loop for each gift
    for gift in gifts:
        file.write(str(gift.giftID) + ",")
        file.write(str(gift.childID) + ",")
        file.write(    gift.gift + ",")
        file.write(str(gift.cost) + "\n")
        
    file.close()


def main():
    """Main program."""

    # Initialise variables
    noOfKids = 200
    noOfGifts = 400
    
    # 1 - Get child entity data
    children = createChildData(noOfKids)
    
    # 2 - Get gift entity data
    gifts = createGiftData(noOfGifts, noOfKids)
    
    # 3 - Add 'naughty' children (maybe)
    if input("Include naughty children (y/n)? ") == "y":
        
        children, gifts = naughtyKids(children, gifts)
    
    # 4 - Write child table
    writeChildCSV(children)
    
    # 5 - Write gift table
    writeGiftCSV(gifts)


# Call main()
main()
