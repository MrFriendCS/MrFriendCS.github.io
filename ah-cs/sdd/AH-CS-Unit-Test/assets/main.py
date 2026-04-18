# Title: Unit Test - Code to Test
# Author: Mr Friend
# Date: 18 Apr 2026

def add(a, b):
    """Add two values together and return the result."""
    
    # Calculate and return
    return a + b


def multiply(a, b):
    """Multiply two values together and return the result."""
    
    # Calculate and return
    return a * b


class Person:
    """Declare a class to define a person."""

    def __init__(self, name="", age=0):
        """Object constructor method.  Automatically called when an object is created."""
        
        # Class properties - Private
        self.__name = name
        self.__age = age

    def getAge(self):
        """Getter method for age."""
        return self.__age

    def setAge(self, age=0):
        """Setter method for age."""
        self.__age = age

    def getName(self):
        """Getter method for name."""
        return self.__name
