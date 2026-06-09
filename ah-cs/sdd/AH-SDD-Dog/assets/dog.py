# Title: AH-SDD-Dog
# Author: 
# Date: 3 Jun 2026


class Dog:
    """A class to represent a virtual dog."""
    
    def __init__(self, name: str='', age: int=0):
        """Creates a new dog.
           
           name -- the name of the dog (default '')
           age  -- the age of the dog (default 0)
           """
        
        self.__name = name
        self.__age = age
    
    def get_name(self) -> str:
        """Returns the name of the dog."""
        
        return self.__name
    
    def get_age(self) -> int:
        """Returns the age of the dog."""
        
        return self.__age
    
    def birthday(self) -> None:
        """Adds 1 to the dog's age."""
        
        self.__age += 1
    
    def eat(self, food: str="") -> None:
        """A dog's got to eat!"""
        
        print(f'\nWoof! {food.capitalize()} is tasty!\n')

myDogs = [Dog("A",1), Dog("B",2)]