# Title: Locker Class
# Author: Mr Friend
# Date: 22 May 2026


class Locker:
    '''Declare a class to define a smart locker.'''
    
    
    def __init__(self, lockerNo: int=0, pupilName: str='', \
                 locked: bool=True):
        '''Constructor method. ''' \
        '''Automatically called when a locker object is created.'''
    
        # Instance variables - Private
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
    
    
    def details(self) -> tuple:
        '''Method to return the details of a locker.'''
        
        return self.__lockerNo, self.__pupil, self.__isLocked
    
    
    def assign(self, pupilName) -> None:
        '''Method to assign a locker to a pupil.'''
        
        # Assign locker to pupil
        self.__pupil = pupilName
