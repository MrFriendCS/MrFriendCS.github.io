# Title: AH SDD Locker
# Author: Mr Friend
# Date: 24 May 2026


# Locker class
from Locker import Locker


def readData() -> list:
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
        pupilName = data[1]
        lock = int(data[2])
        
        # Check lock status
        if lock == 1:
            isLocked = True
        else:
            isLocked = False
        
        # Append new locker object to array
        arrayOfObjects.append(Locker(lockerNo, pupilName, isLocked))
        
    return arrayOfObjects


def findLocked(arrayOfObjects) -> list:
    '''Procedure to find locked lockers, and return their numbers.'''
    
    # Local variable
    lockers = []
    
    # Loop for each locker
    for locker in arrayOfObjects:
        
        currentLocker = locker.details()
        
        if currentLocker[2] == True:
            
            lockers = lockers + [currentLocker[0]]
    
    return lockers


def findLockerNo(arrayOfObjects, pupilName:str='') -> list:
    '''Function find a pupil's locker number(s). ''' \
    '''Returns the locker number(s), or an empty array.'''
    
    # Local variable
    lockers = []
    
    # Loop for each locker
    for locker in arrayOfObjects:
        
        # Get current locker details
        details = locker.details()
        
        # Compare pupil name
        if details[1] == pupilName:
            
            # Assign lock number to array
            lockers = lockers + [details[1]]
    
    # Return locker number(s)
    return lockers


def assignLocker(arrayOfObjects, lockerNo=-1, pupilName='') -> bool:
    '''Assigns a locker to a pupil. ''' \
    '''Returns True if successful, else returns False.'''
    
    # Local variables
    assigned = False
    index = 0
    
    # Loop for each locker until found
    while assigned == False and index < len(arrayOfObjects)-1:
        
        # Get current locker details
        currentLocker = arrayOfObjects[index].details()
        
        # Compare locker number
        if currentLocker[0] == lockerNo:
            
            # Assign locker to pupil
            arrayOfObjects[index].assign(pupilName)
            
            # Update assigned
            assigned = True
        
        # Increment index
        index += 1
    
    # Return result
    return assigned


#
# Main program
#

# Read data from file
objects = readData()


findLocked(objects)

print(findLockerNo(objects, 'Jodie Whittaker'))

print(assignLocker(objects, 14,'Ncuti Gatwa'))

print(findLockerNo(objects, 'Ncuti Gatwa'))

print(findLocked(objects))
