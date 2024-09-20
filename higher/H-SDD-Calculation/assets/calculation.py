# Title: H-SDD-Calculation
# Author: Mr Friend
# Date: 19 Sep 2024

def areaOfSquare(length):
    """Returns the area of a square: length x length"""
    
    # Check length is valid
    if length <= 0:
        return -1

    # Calculate area
    area = length**2

    # return value
    return area


def areaOfRectangle(width, height):
    """Returns the area of a rectangle: width x height"""
    
    # Check width and height are valid
    if width <= 0 or height <= 0:
        return -1

    # Calculate area
    area = width * height

    # return value
    return area


def areaOfTriangle(base, height):
    """Returns the area of a traingle: 0.5 x base x height"""
    
    # Check base and height are valid
    if base <= 0 or height <= 0:
        return -1

    # Calculate area
    area = 0.5 * base * height

    # return value
    return area


def areaOfCircle(value, option):
    """Returns the area of a circle: pi x radius x radius"""
    
    # Initialise local variable
    ascii = 0
    newOption = ""
    pi = 3.14
    
    # Ensure 'option' is lowercase
    for letter in option:
        ascii = ord(letter)
        
        # Uppercase?
        if ascii >= 65 and ascii <= 90:
            ascii = ascii + 32
            
        # Create string
        newOption = newOption + chr(ascii)
        
    # Check value is valid
    if value <= 0 or (option != "radius" and option != "diameter"):
        return -1
    
    # Have radius value
    if option != "radius":
        value = value / 2

    # Calculate area
    area = pi * value**2  

    # return value
    return area


def volOfCube(length):
    """Returns the volume of a cube: length x length x length"""
    
    # Check length valid
    if length <= 0:
        return -1
    
    # Calculate volume
    volume = length**3

    # return value
    return volume


def volOfCuboid(length, breadth, height):
    """Returns the volume of a cube: length x breadth x height"""
    
    # Check width and height are valid
    if length <= 0 or breadth <= 0 or height <= 0:
        return -1
    
    # Calculate volume
    volume = length * breadth * height
    
    # return value
    return volume


def volOfCylinder(height, value, option):
    """Returns the volume of a cylinder: pi x radius x radius x height"""
    
    # Check height and value are valid
    if height <= 0 or value <= 0:
        return -1
    
    # Declare local variable
    pi = 3.14

    # Calculate volume
    volume = pi * value**2 * height
      

    # return value
    return volume


def volOfSphere(value, option):
    """Returns the volume of a sphere: (3/4) * pi * radius * radius * radius"""
    
    # Check value is valid
    if value <= 0:
        return -1
    
    # Declare local variable
    pi = 3.14

    # Calculate volume
    volume = (3/4) * pi * value**3

    # return value
    return volume
