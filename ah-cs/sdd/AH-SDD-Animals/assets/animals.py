# Title: Animal Class
# Author: Mr Friend
# Date: 10 Jun 2026

# Import Animal class
from animal import Animal


class Animals:
    """A class to represent a collection of zoo animal."""    
    
    def __init__(self):
        """Create a collection object."""
    
        # Instance variables - Private
        self.__number_of_animals: int = 0
        self.__animals: list[Animal] = []
    
    def add_animal(self, animal: Animal) -> None:
        """A method to add an animal to the collection."""
        
        # Add the animal
        self.__animals += [animal]
        
        # Increment the number of animals
        self.__number_of_animals += 1
        
    def get_number_of_animals(self) -> int:
        """A method to access the number of animals."""
        
        return self.__number_of_animals
        
    def find_oldest(self) -> tuple[int, str]:
        """A method to find the age and name of the oldest animal."""
        
        # Local variables
        
        oldest_age: int = -1
        oldest_name: str = 'TBC'
        
        # Loop for each animal
        for index in range(self.__number_of_animals):
            
            # Check if current animal is older
            if self.__animals[index].get_age() > oldest_age \
                and self.__animals[index].get_alive() == True:
                
                # Update oldest details
                oldest_age = self.__animals[index].get_age()
                oldest_name = self.__animals[index].get_name()
        
        return oldest_age, oldest_name
    
    def get_animals(self) -> list[Animal]:
        """A method to get the array of animals."""
        
        return self.__animals
    
    def order_by_age(self) -> None:
        """A bubble sort to order the animals by age descending."""
        
        # Get number of elements
        n: int = self.__number_of_animals

        # Turn sort on
        sort: bool = True

        # Sort if needed
        while sort == True:

            # Turn sort off
            sort = False

            # Loop from start of array
            for index in range(n - 1):

                # Compare current element with next element
                if self.__animals[index].get_age() \
                   < self.__animals[index + 1].get_age():

                    # Swap values
                    temp = self.__animals[index]
                    self.__animals[index]  = self.__animals[index + 1]
                    self.__animals[index + 1] = temp

                    # Sorting still needed
                    sort = True

            # Reduce the number elements to be checked
            n = n - 1
    
    def order_by_weight(self) -> None:
        """An insertion sort to order the animals by weight descending."""
        
        # Variables
        animal: Animal
        position: int = 0

        # Loop over array of Animal objects
        for index in range(1, len(self.__animals)):

            # Get current object from array
            animal = self.__animals[index]

            # Get current position
            position = index

            # Loop if current value is smaller then value to the left
            while (position > 0) \
                  and (animal.get_weight() >
                       self.__animals[position-1].get_weight()):

                # Move value left
                self.__animals[position] = self.__animals[position-1]

                # Decrement position
                position = position - 1

            # Set current position to the original value
            self.__animals[position] = animal
