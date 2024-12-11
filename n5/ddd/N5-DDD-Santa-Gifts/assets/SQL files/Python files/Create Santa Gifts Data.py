# Title: Create Santa Gifts Data
# Author: Mr Friend
# Date: 11 Dec 2024

"""
Create the data and export as CSV.
Seperate list of naughty children used to overwrite random records.
Naughty children are removed from the gift list, as they don't deserve them!
"""

# Import Extra Code
import sys
from dataclasses import dataclass


# Find DDDhelper file
shool = "C:\\Users\\afriend1r\\AppData\\Local\\Programs\\Thonny"

start1 = "C:\\Users\\afriend1r\\OneDrive - Glow Scotland\\"
start2 = "D:\\OneDrive - Glow Scotland\\"

folder1 = "GitHub\\MrFriendCS.github.io\\"
folder2 = "SQA - CS - N5\\DDD\\Database Files\\"

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


def getChildData(count):
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


def getGiftData(noOfGifts, noOfKids):
    """Create the data for the gift entity."""
    
    
    @dataclass
    class Gift:
        """A record to represent a gift."""
        giftID: int = 0
        childID: int = 0
        gift: str = ""
    
    # Initialise local variables
    gifts = [Gift() for index in range(noOfGifts)]
    
    # Loop for each gift
    for index in range(noOfGifts):
        gifts[index].giftID = index + 1
        gifts[index].childID = DDDhelper.getNumber(1, noOfKids)
        gifts[index].gift = DDDhelper.getGift()
    
    return gifts


def naughtyKids(children, gifts):
    """Insert naughty children and remove all their gifts."""
    
    # Get extra code
    import random
    
    # Naughty children - 2D array
    naughty = []
    
    if school:
        location = start1 + folder2
    else:
        location = start2 + folder2
        
    file = open(location + "naughtyList.csv", "r")
    
    line = file.readline()  # ignore header
    line = file.readline()
    
    while line != "":
        
        data = line.split(",")
        
        naughty = naughty + [[data[0].strip(), data[1].strip()]]
        
        line = file.readline()
    
    # List of even numbers 
    naughtyNumbers = [index for index in range(0, len(children), 2)]
    
    # Pick index positions of naughty children
    naughtyIDs = random.sample(naughtyNumbers, k=len(naughty))
    
    # Loop for each naughty child
    for index in range(len(naughty)):
        
        children[naughtyIDs[index]].first = naughty[index][0]
        children[naughtyIDs[index]].last = naughty[index][1]
        children[naughtyIDs[index]].nice = False
     
    # Convert index positions to numbers
    for index in range(len(naughty)):
        naughtyIDs[index] = naughtyIDs[index] + 1    
    
    # Loop for each gift - remove naughty kids
    for index in range(len(gifts)):
        
        if gifts[index].childID in naughtyIDs:
            gifts[index].childID = gifts[index].childID + 1
            
            # Catch out of range
            if gifts[index].childID == len(children) + 1:
                gifts[index].childID = 1
                      
    return children, gifts


def writeChildCSV(children):
    """Create CSV file for data."""
    
    file = open("../CSV files/Child.csv", "w")
    
    # Headers
    file.write("giftID,firstName,lastName,nice\n")

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
    file.write("giftID,childID,gift\n")
    
    # Loop for each gift
    for gift in gifts:
        file.write(str(gift.giftID) + ",")
        file.write(str(gift.childID) + ",")
        file.write(    gift.gift + "\n")
        
    file.close()


def main():
    """Main program."""

    # Initialise variables
    noOfKids = 200
    noOfGifts = 400
    
    # 1 - Get child entity data
    children = getChildData(noOfKids)
    
    # 2 - Get gift entity data
    gifts = getGiftData(noOfGifts, noOfKids)
    
    # 3 - Update with 'naughty' children (maybe)
    if input("Add naughty children (y/n)? ") == "y":
        
        children, gifts = naughtyKids(children, gifts)
    
    # 4 - Write child table
    writeChildCSV(children)
    
    # 5 - Write gift table
    writeGiftCSV(gifts)


# Call main()
main()
