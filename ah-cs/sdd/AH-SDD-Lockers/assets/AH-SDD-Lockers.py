# Title: AH SDD Locker
# Author: Mr Friend
# Date: 19 May 2026


class Locker:
    '''Declare a class to define a smart locker.'''
    
    def __init__(self, number=0, locked=False):
        '''Constructor method. ''' \
        '''Automatically called when an object is created.'''
    
        # Class properties - Private
        self.__lockerNo = number
        self.__isLocked = locked
    
    def lock(self):
        '''Method to lock a locker.'''
        
        # Update locked status
        self.__isLocked = True
            
        # Display message
        print(f'Locker {self.__lockerNo} has been locked.\n')
    
    def unlock(self):
        '''Method to unlock a locker.'''
        
        # Update locked status
        self.__isLocked = False
            
        # Display message
        print(f'Locker {self.__lockerNo} has been unlocked.\n')
            
    def status(self):
        '''Method to display the status of a locker.'''
        
        # Local variable
        status = ''
        
        # Determine status
        if self.__isLocked == True:
            status = 'Locked'
        else:
            status = 'Unlocked'
            
        # Display message
        print(f'Locker: {self.__lockerNo}')
        print(f'Status: {status}\n')
    
    
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
        arrayOfObjects.append(Locker(lockerNo, isLocked))
        
    return arrayOfObjects
    

objects = readData()
'''
newLocker = Locker(1)

newLocker.status()

newLocker.lock()

newLocker.status()

newLocker.unlock()

newLocker.status()
'''