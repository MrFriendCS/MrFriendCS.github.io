# Title: AH SDD Locker
# Author: Mr Friend
# Date: 21 May 2026


class Locker:
    '''Declare a class to define a smart locker.'''
    
    def __init__(self, lockerNo: int=0, pupilName: str="", \
                 locked: bool=True):
        '''Constructor method. ''' \
        '''Automatically called when an object is created.'''
    
        # Class properties - Private
        self.__lockerNo = lockerNo
        self.__pupil = pupilName
        self.__isLocked = locked
    
    def lock(self) -> bool:
        '''Method to lock a locker.'''
        
        # Local variable
        success = False
        
        # Check locked status
        if self.__isLocked == False:
            
            # Update locked status
            self.__isLocked = True
            
            # Update success
            success = True
        
        # Return result
        return success
    
    def unlock(self) -> bool:
        '''Method to unlock a locker.'''
        
        # Local variable
        success = False
        
        # Check locked status
        if self.__isLocked == True:
            
            # Update locked status
            self.__isLocked = False
            
            # Update success
            success = True
        
        # Return result
        return success
            
    def status(self) -> tuple:
        '''Method to return the status of a locker.'''
        
        return self.__lockerNo, self.__pupil, self.__isLocked
    
    
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
    for index in range(arrayOfObjects):
        '''Encapsulation!'''
        if arrayOfObjects[index].__isLocked == True:
            
            arrayOfObjects[index].status()


#
# Main program
#

objects = readData()

newLocker = Locker(1, 'Tom')

print(newLocker.status())

print(newLocker.lock())

print(newLocker.lock())

print(newLocker.unlock())

print(newLocker.unlock())

print(newLocker.status())

