# Title: AH SDD Locker
# Author: Mr Friend
# Date: 22 May 2026


# Get extra code
from Locker import Locker
    
    
def readData():
    '''Read CSV data into an array of Locker objects.'''

    # Local variables
    contents = ''
    temp = []
    data = []
    arrayOfObjects = []
    isLocked = False

    # Connect to a file
    file = open('Lockers.csv', 'r', encoding='utf-8')

    # Read contents, remove end \n
    contents = file.read().strip()
    
    # Close the connection to the file
    file.close()

    # Split at newlines
    temp = contents.split('\n')

    # Loop for each object - Ignore first row
    for index in range(1, len(temp)):
        
        # Split data
        data = temp[index].split(',')
        
        # Extract values
        lockerNo = int(data[0])
        lock = int(data[1])
        
        # Check lock status
        if lock == 1:
            isLocked = True
        else:
            isLocked = False
        
        # Append new locker object to array
        arrayOfObjects.append(Locker(lockerNo, '', isLocked))
        
    return arrayOfObjects


def findLocked(arrayOfObjects):
    '''Procedure to find locked lockers, and display their numbers.'''
    
    # Loop for each locker
    for index in range(len(arrayOfObjects)):
        
        currentLocker = arrayOfObjects[index].details()
        
        if currentLocker[2] == True:
            
            print(currentLocker[0])


def findPupil(arrayOfObjects, pupilName):
    '''Procedure to find a pupil's locker, and display the number.'''
    
    # Loop for each locker
    for index in range(len(arrayOfObjects)):
        
        currentLocker = arrayOfObjects[index].details()
        
        if currentLocker[1] == pupilName:
            
            print(currentLocker[0])


#
# Main program
#

objects = readData()

objects[1].assign('Tom')

print(objects[1].details())

findLocked(objects)

findPupil(objects, 'Tom')

'''
newLocker = Locker(1, 'Tom')

print(newLocker.status())

print(newLocker.lock())

print(newLocker.lock())

print(newLocker.unlock())

print(newLocker.unlock())

print(newLocker.status())
'''
