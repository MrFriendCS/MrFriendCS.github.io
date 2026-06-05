# Title: Locker Class
# Author: Mr Friend
# Date: 29 May 2026


class Locker:
    """A class to define a smart locker."""
    
    
    def __init__(self, locker_no: int=0, pupil_name: str='',
                 locked: bool=True):
        """Create a new locker."""
    
        # Instance variables - Private
        self.__locker_no = locker_no
        self.__pupil_name = pupil_name
        self.__islocked = locked
    
    
    def lock(self) -> bool:
        """Method to lock the locker."""
        
        # Local variable
        success = False
        
        # Check locked status
        if self.__islocked == False:
            
            # Update locked status
            self.__islocked = True
            
            # Update success
            success = True
        
        # Return result
        return success
    
    
    def unlock(self) -> bool:
        """Method to unlock the locker."""
        
        # Local variable
        success = False
        
        # Check locked status
        if self.__islocked == True:
            
            # Update locked status
            self.__islocked = False
            
            # Update success
            success = True
        
        # Return result
        return success
    
    
    def details(self) -> tuple:
        """Method to return the details of the locker."""
        
        return self.__locker_no, self.__pupil_name, self.__islocked
    
    
    def assign(self, pupil_name:str='') -> None:
        """Method to assign a locker to the pupil."""
        
        # Assign locker to pupil
        self.__pupil_name = pupil_name
