# Title: Animal Class
# Author: Mr Friend
# Date: 10 Jun 2026


class Animal:
    """A class to represent a zoo animal."""    
    
    def __init__(self, name: str='', age: int=0,
                 weight: float=0.0, alive: bool=True):
        """Create an animal object."""
    
        # Instance variables - Private
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__alive = alive
    
    def get_name(self) -> str:
        """A method to access the name of the animal."""
        
        return self.__name
    
    def get_age(self) -> int:
        """A method to access the age of the animal."""
        
        return self.__age
    
    def birthday(self) -> None:
        """A method to increase the animal's age by 1."""
        
        self.__age += 1
    
    def get_weight(self) -> float:
        """A method to access the weight of the animal."""
        
        return self.__weight
    
    def set_weight(self, weight: float=0.0) -> None:
        """A method to update the weight of the animal."""
        
        self.__weight = weight
    
    def get_alive(self) -> bool:
        """A method to check if the animal is alive."""
        
        return self.__alive
    
    def die(self) -> None:
        """A method to acknowledge the sad passing of the animal."""
        
        self.__alive = False
