# Title: AH SDD Locker
# Author: Mr Friend
# Date: 17 May 2026


class Locker:
    '''Declare a class to define a smart locker.'''
    
    def __init__(self, id=0, locked=False):
        '''Constructor method. ''' \
        '''Automatically called when an object is created.'''
    
        # Class properties - Private
        self.__id = id
        self.__isLocked = locked
    
    def lock(self):
        '''Method to lock a locker.'''
        
        # Update locked status
        self.__isLocked = True
            
        # Display message
        print(f'Locker {self.__id} has been locked.\n')
    
    def unlock(self):
        '''Method to unlock a locker.'''
        
        # Update locked status
        self.__isLocked = False
            
        # Display message
        print(f'Locker {self.__id} has been unlocked.\n')
            
    def status(self):
        '''Method to display the status of a locker.'''
        
        # Local variable
        status = ""
        
        # Determine status
        if self.__isLocked == True:
            status = "Locked"
        else:
            status = "Unlocked"
            
        # Display message
        print(f'Locker: {self.__id}')
        print(f'Status: {status}\n')

        
newLocker = Locker(1)

newLocker.status()

newLocker.lock()

newLocker.status()

newLocker.unlock()

newLocker.status()
