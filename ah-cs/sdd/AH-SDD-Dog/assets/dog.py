class Dog:
    
    def __init__(self, name: str="", age=0):
        """Create a new dog."""
        
        self.__name = name
        self.__age = age
    
    def getName(self) -> str:
        """Returns the name of a dog."""
        
        return self.__name
    
    def getAge(self) -> int:
        """Returns the age of a dog."""
        
        return self.__age
    
    def birthday(self) -> None:
        """Adds 1 to the dog's age."""
        
        self.__age += 1
    
    def eat(self, food: str="") -> None:
        """A dog's got to eat!"""
        
        print(f'Woof! That {food.lower()} is tasty!')

fido = Dog('Cindy', 16)
        